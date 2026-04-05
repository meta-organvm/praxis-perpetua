#!/usr/bin/env python3
"""Ingest supplementary prompt sources not covered by organvm-engine.

Handles:
- Paste.app clipboard export (ai-prompts-clipboard-export.json)
- ChatGPT markdown exports (## User delimited)
- ChatGPT JSON exports (role: "Prompt" / "user")
- Claude /export TXT files (❯ prefix marks user prompts)
- SpecStory markdown history (_**User ...**_ blocks)

Outputs JSONL in the same schema as organvm prompts narrate, with
agent field set to clipboard/<app>, chatgpt, claude-export, or specstory.
"""

import json
import re
import hashlib
import sys
from pathlib import Path


def compute_id(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:12]


def make_entry(
    text: str,
    agent: str,
    source_file: str,
    timestamp: str | None,
    prompt_index: int,
    prompt_count: int,
    project_slug: str = "",
) -> dict:
    text = text.strip()
    if not text:
        return {}
    return {
        "id": compute_id(f"{agent}:{source_file}:{prompt_index}:{text[:200]}"),
        "source": {
            "session_id": compute_id(source_file),
            "agent": agent,
            "project_dir": str(Path(source_file).parent),
            "project_slug": project_slug or Path(source_file).parent.name,
            "timestamp": timestamp or "",
            "prompt_index": prompt_index,
            "prompt_count": prompt_count,
        },
        "content": {
            "text": text[:10000],
            "char_count": len(text),
            "word_count": len(text.split()),
            "line_count": text.count("\n") + 1,
        },
        "classification": {
            "prompt_type": "unclassified",
            "size_class": (
                "terse" if len(text) < 20
                else "short" if len(text) < 100
                else "medium" if len(text) < 500
                else "long"
            ),
            "session_position": "unknown",
            "is_continuation": False,
            "is_interrupted": False,
        },
        "signals": {
            "opening_phrase": "",
            "imperative_verb": "",
            "mentions_files": [],
            "mentions_tools": [],
            "tags": [f"supplementary:{agent}"],
        },
        "threading": {
            "thread_id": "",
            "thread_label": f"{agent}/{Path(source_file).stem}",
            "arc_position": "unknown",
        },
        "domain_fingerprint": "",
        "raw_text_truncated": len(text) > 10000,
    }


# --- Clipboard export (Paste.app) ---

def ingest_clipboard(file_path: Path) -> list[dict]:
    """Ingest Paste.app clipboard export JSON."""
    entries = []
    with open(file_path) as f:
        data = json.load(f)

    prompts = data.get("prompts", [])
    for p in prompts:
        text = p.get("text", "").strip()
        if not text:
            continue

        source_app = p.get("source_app", "unknown").lower()
        session_id = p.get("session_id", f"clipboard-{p.get('id', 0)}")

        entry = make_entry(
            text=text,
            agent=f"clipboard/{source_app}",
            source_file=str(file_path),
            timestamp=p.get("timestamp", ""),
            prompt_index=p.get("position_in_session", 0),
            prompt_count=p.get("session_size", 1),
        )
        if entry:
            # Override session_id to use the clipboard session grouping
            entry["source"]["session_id"] = str(session_id)
            entries.append(entry)

    return entries


# --- ChatGPT JSON exports ---

def ingest_chatgpt(file_path: Path) -> list[dict]:
    entries = []
    try:
        with open(file_path) as f:
            data = json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return []

    messages = data.get("messages", [])
    # Also handle mapping-style exports
    if not messages and "mapping" in data:
        for node in data["mapping"].values():
            msg = node.get("message")
            if msg and msg.get("author", {}).get("role") == "user":
                parts = msg.get("content", {}).get("parts", [])
                text = "\n".join(str(p) for p in parts if isinstance(p, str))
                if text.strip():
                    messages.append({"role": "Prompt", "say": text})

    prompts = [m for m in messages if m.get("role") in ("Prompt", "user")]
    for i, m in enumerate(prompts):
        text = m.get("say", "") or m.get("content", "")
        if isinstance(text, dict):
            text = str(text.get("parts", [""])[:1])
        entry = make_entry(
            text=str(text),
            agent="chatgpt",
            source_file=str(file_path),
            timestamp=None,
            prompt_index=i,
            prompt_count=len(prompts),
            project_slug=file_path.stem.replace("ChatGPT-", "").replace(" ", "-").lower()[:60],
        )
        if entry:
            entries.append(entry)
    return entries


# --- ChatGPT markdown exports ---

def ingest_chatgpt_markdown(file_path: Path, project_slug: str = "") -> list[dict]:
    """Ingest ChatGPT markdown exports (## User delimited)."""
    entries = []
    content = file_path.read_text(encoding="utf-8", errors="replace")

    # Extract conversation ID from header
    conv_match = re.search(r"conversation_id:\s*(\S+)", content)
    conv_id = conv_match.group(1) if conv_match else file_path.stem

    # Split on ## User markers
    user_blocks = re.split(r"^## User\s*$", content, flags=re.MULTILINE)
    user_blocks = user_blocks[1:]  # First block is header

    for i, block in enumerate(user_blocks):
        # Extract text up to the next ## Assistant / ## ChatGPT marker
        assistant_split = re.split(
            r"^## (?:Assistant|ChatGPT)\s*$", block, flags=re.MULTILINE
        )
        text = assistant_split[0].strip()
        if not text or len(text) < 5:
            continue

        slug = project_slug or file_path.stem
        entry = make_entry(
            text=text,
            agent="chatgpt",
            source_file=str(file_path),
            timestamp="",
            prompt_index=i,
            prompt_count=len(user_blocks),
            project_slug=slug,
        )
        if entry:
            entries.append(entry)

    return entries


# --- Claude /export TXT ---

def ingest_claude_export(file_path: Path) -> list[dict]:
    entries = []
    try:
        text = file_path.read_text(errors="replace")
    except Exception:
        return []

    # Extract date from filename: 2026-04-04-152030-...
    date_match = re.match(r"(\d{4}-\d{2}-\d{2})-(\d{6})", file_path.name)
    base_ts = ""
    if date_match:
        d, t = date_match.groups()
        base_ts = f"{d}T{t[:2]}:{t[2:4]}:{t[4:6]}Z"

    # User prompts start with ❯
    prompt_pattern = re.compile(r"^❯\s*(.+?)(?=\n\n⏺|\n\n❯|\Z)", re.MULTILINE | re.DOTALL)
    matches = list(prompt_pattern.finditer(text))
    for i, m in enumerate(matches):
        prompt_text = m.group(1).strip()
        # Clean up line-continuation whitespace
        prompt_text = re.sub(r"\s*\n\s+", " ", prompt_text)
        entry = make_entry(
            text=prompt_text,
            agent="claude-export",
            source_file=str(file_path),
            timestamp=base_ts,
            prompt_index=i,
            prompt_count=len(matches),
        )
        if entry:
            entries.append(entry)
    return entries


# --- SpecStory markdown ---

def ingest_specstory(file_path: Path) -> list[dict]:
    entries = []
    try:
        text = file_path.read_text(errors="replace")
    except Exception:
        return []

    # Extract date from filename: 2025-11-21_23-22Z-...
    date_match = re.match(r"(\d{4}-\d{2}-\d{2})_(\d{2})-(\d{2})Z", file_path.name)
    base_ts = ""
    if date_match:
        d, h, m = date_match.groups()
        base_ts = f"{d}T{h}:{m}:00Z"

    # User blocks: _**User (timestamp)**_ followed by content until next ---
    user_pattern = re.compile(
        r"_\*\*User\s*\(([^)]*)\)\*\*_\s*\n\n(.*?)(?=\n---|\Z)",
        re.DOTALL,
    )
    matches = list(user_pattern.finditer(text))
    for i, m in enumerate(matches):
        ts_str, content = m.groups()
        entry = make_entry(
            text=content.strip(),
            agent="specstory",
            source_file=str(file_path),
            timestamp=ts_str.strip() or base_ts,
            prompt_index=i,
            prompt_count=len(matches),
        )
        if entry:
            entries.append(entry)
    return entries


# --- Main ---

def main():
    intake = Path.home() / "Workspace" / "intake"
    output_path = Path(__file__).parent / "supplementary-prompts.jsonl"

    all_entries = []
    stats = {
        "clipboard": 0, "chatgpt-json": 0, "chatgpt-md": 0,
        "claude-export": 0, "specstory": 0, "files": 0, "errors": 0,
    }

    # 1. Clipboard export (Paste.app) — the biggest supplementary source
    clipboard_path = intake / "ai-prompts-clipboard-export.json"
    if clipboard_path.exists():
        print(f"Clipboard: {clipboard_path}")
        try:
            entries = ingest_clipboard(clipboard_path)
            all_entries.extend(entries)
            stats["clipboard"] += len(entries)
            stats["files"] += 1
        except Exception as e:
            print(f"  ERROR: {e}", file=sys.stderr)
            stats["errors"] += 1
    else:
        print(f"Clipboard export not found: {clipboard_path}")

    # 2. ChatGPT markdown exports (known locations)
    chatgpt_md_dirs = [
        (intake / "machina-mundi-canonici" / "conversations", "machina-mundi-canonici"),
        (intake / "dsp-alternative" / "conversations", "dsp-alternative"),
    ]
    for conv_dir, slug in chatgpt_md_dirs:
        if conv_dir.exists():
            print(f"ChatGPT markdown: {conv_dir}")
            for p in sorted(conv_dir.glob("*.md")):
                try:
                    entries = ingest_chatgpt_markdown(p, slug)
                    all_entries.extend(entries)
                    stats["chatgpt-md"] += len(entries)
                    stats["files"] += 1
                except Exception as e:
                    print(f"  ERROR {p.name}: {e}", file=sys.stderr)
                    stats["errors"] += 1

    # 3. ChatGPT JSON exports (scan intake for ChatGPT-*.json)
    print("Scanning ChatGPT JSON exports...")
    for p in sorted(intake.rglob("ChatGPT-*.json")):
        try:
            entries = ingest_chatgpt(p)
            all_entries.extend(entries)
            stats["chatgpt-json"] += len(entries)
            stats["files"] += 1
        except Exception as e:
            print(f"  ERROR {p.name}: {e}", file=sys.stderr)
            stats["errors"] += 1

    # 4. Claude /export TXT (scan home for export files)
    print("Scanning Claude /export files...")
    home = Path.home()
    for pattern in ["Workspace/*/2026-*-local-command-*.txt", "Downloads/2026-*.txt"]:
        for p in sorted(home.glob(pattern)):
            try:
                entries = ingest_claude_export(p)
                all_entries.extend(entries)
                stats["claude-export"] += len(entries)
                stats["files"] += 1
            except Exception as e:
                print(f"  ERROR {p.name}: {e}", file=sys.stderr)
                stats["errors"] += 1

    # 5. SpecStory history
    specstory_dir = home / ".specstory" / "history"
    if specstory_dir.exists():
        print(f"SpecStory: {specstory_dir}")
        for p in sorted(specstory_dir.glob("*.md")):
            try:
                entries = ingest_specstory(p)
                all_entries.extend(entries)
                stats["specstory"] += len(entries)
                stats["files"] += 1
            except Exception as e:
                print(f"  ERROR {p.name}: {e}", file=sys.stderr)
                stats["errors"] += 1
    else:
        print(f"SpecStory history empty or not found: {specstory_dir}")

    # Write output
    with open(output_path, "w") as f:
        for entry in all_entries:
            f.write(json.dumps(entry) + "\n")

    print(f"\nSupplementary extraction complete:")
    print(f"  Clipboard prompts:    {stats['clipboard']}")
    print(f"  ChatGPT JSON prompts: {stats['chatgpt-json']}")
    print(f"  ChatGPT MD prompts:   {stats['chatgpt-md']}")
    print(f"  Claude export prompts:{stats['claude-export']}")
    print(f"  SpecStory prompts:    {stats['specstory']}")
    print(f"  Total prompts:        {len(all_entries)}")
    print(f"  Files processed:      {stats['files']}")
    print(f"  Errors:               {stats['errors']}")
    print(f"  Written to:           {output_path}")


if __name__ == "__main__":
    main()
