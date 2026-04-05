#!/usr/bin/env python3
"""Extract pure human↔AI dialogue from all session transcripts.

Strips: tool results, /copy, /export, progress, task notifications,
file-history-snapshots, system-reminders, tool_use blocks.

Preserves: human prompts and AI text responses — the actual conversation.

Output: One markdown file per session (dialogue-only), plus a unified
chronological dialogue corpus.
"""

import json
import re
import glob
import hashlib
from pathlib import Path
from datetime import datetime
from collections import defaultdict


# Noise patterns to filter from user messages
USER_NOISE = [
    re.compile(r"^<command-name>", re.DOTALL),
    re.compile(r"^<local-command-", re.DOTALL),
    re.compile(r"^<task-notification>", re.DOTALL),
    re.compile(r"^<system-reminder>", re.DOTALL),
    re.compile(r"^\[Request interrupted"),
    re.compile(r"^Tool loaded"),
    re.compile(r"^Plan (saved|approved|file)"),
]

# Noise patterns in assistant text
ASSISTANT_NOISE = [
    re.compile(r"^<thinking>.*?</thinking>\s*", re.DOTALL),
]


def extract_human_text(entry: dict) -> str:
    """Extract human-written text, return empty string if it's noise."""
    msg = entry.get("message", {})
    if not isinstance(msg, dict):
        return ""

    content = msg.get("content", "")
    text = ""

    if isinstance(content, str):
        text = content.strip()
    elif isinstance(content, list):
        text_parts = []
        for block in content:
            if isinstance(block, dict):
                if block.get("type") == "text":
                    text_parts.append(block.get("text", ""))
                elif block.get("type") == "tool_result":
                    return ""  # pure tool result — skip
            elif isinstance(block, str):
                text_parts.append(block)
        text = "\n".join(text_parts).strip()

    if not text or len(text) < 3:
        return ""

    # Filter noise
    for pattern in USER_NOISE:
        if pattern.match(text):
            return ""

    return text


def extract_assistant_text(entry: dict) -> str:
    """Extract AI text response, stripping tool_use and thinking blocks."""
    msg = entry.get("message", {})
    if not isinstance(msg, dict):
        return ""

    content = msg.get("content", [])
    if not isinstance(content, list):
        return ""

    text_parts = []
    for block in content:
        if isinstance(block, dict):
            btype = block.get("type", "")
            if btype == "text":
                t = block.get("text", "").strip()
                if t:
                    text_parts.append(t)
            # Skip: tool_use, tool_result, thinking, signatures

    text = "\n\n".join(text_parts).strip()

    # Strip thinking blocks if they leaked through
    for pattern in ASSISTANT_NOISE:
        text = pattern.sub("", text)

    return text.strip()


def derive_slug(entry: dict) -> str:
    slug = entry.get("slug", "")
    if slug:
        return slug
    cwd = entry.get("cwd", "")
    if cwd:
        parts = cwd.rstrip("/").split("/")
        return parts[-1] if parts else ""
    return ""


def process_session(session_path: str) -> dict | None:
    """Extract dialogue turns from a session. Returns None if no dialogue."""
    try:
        with open(session_path) as f:
            entries = [json.loads(l) for l in f if l.strip()]
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None

    session_id = Path(session_path).stem
    turns = []
    project_slug = ""
    first_ts = ""
    last_ts = ""

    i = 0
    while i < len(entries):
        entry = entries[i]
        entry_type = entry.get("type", "")
        timestamp = entry.get("timestamp", "")

        if entry_type == "user":
            text = extract_human_text(entry)
            if text:
                if not project_slug:
                    project_slug = derive_slug(entry)
                if not first_ts:
                    first_ts = timestamp
                last_ts = timestamp

                # Collect the assistant response that follows
                response_text = ""
                response_parts = []
                for j in range(i + 1, len(entries)):
                    if entries[j].get("type") == "assistant":
                        part = extract_assistant_text(entries[j])
                        if part:
                            # Deduplicate — same assistant message ID means continuation
                            msg_id = entries[j].get("message", {}).get("id", "")
                            if not response_parts or msg_id != response_parts[-1][0]:
                                response_parts.append((msg_id, part))
                    elif entries[j].get("type") == "user":
                        break  # next human turn

                # Merge unique assistant response parts
                seen_ids = set()
                unique_parts = []
                for msg_id, part in response_parts:
                    if msg_id not in seen_ids:
                        seen_ids.add(msg_id)
                        unique_parts.append(part)
                response_text = "\n\n".join(unique_parts)

                turns.append({
                    "role": "human",
                    "text": text,
                    "timestamp": timestamp,
                })
                if response_text:
                    turns.append({
                        "role": "assistant",
                        "text": response_text,
                        "timestamp": "",
                    })
        i += 1

    if not turns:
        return None

    # Count actual human turns
    human_turns = sum(1 for t in turns if t["role"] == "human")
    if human_turns == 0:
        return None

    return {
        "session_id": session_id,
        "project_slug": project_slug,
        "first_timestamp": first_ts,
        "last_timestamp": last_ts,
        "human_turns": human_turns,
        "total_turns": len(turns),
        "turns": turns,
    }


def session_to_markdown(session: dict) -> str:
    """Render a session as clean markdown dialogue."""
    lines = []
    slug = session["project_slug"]
    ts = session["first_timestamp"][:10] if session["first_timestamp"] else "unknown"

    lines.append(f"# {slug} — {ts}")
    lines.append(f"Session: `{session['session_id'][:12]}`")
    lines.append(f"Turns: {session['human_turns']} human, {session['total_turns']} total")
    lines.append("")

    for turn in session["turns"]:
        if turn["role"] == "human":
            ts_short = turn["timestamp"][11:19] if len(turn["timestamp"]) > 19 else ""
            lines.append(f"## Human {ts_short}")
            lines.append("")
            lines.append(turn["text"])
            lines.append("")
        else:
            # Truncate very long assistant responses to keep dialogue readable
            text = turn["text"]
            if len(text) > 3000:
                text = text[:3000] + f"\n\n*[...truncated, {len(turn['text'])} chars total]*"
            lines.append("## Assistant")
            lines.append("")
            lines.append(text)
            lines.append("")

    return "\n".join(lines)


def main():
    corpus_dir = Path(__file__).parent
    dialogue_dir = corpus_dir / "dialogues"
    dialogue_dir.mkdir(exist_ok=True)

    unified_path = corpus_dir / "dialogue-corpus.jsonl"
    index_path = corpus_dir / "DIALOGUE-INDEX.md"

    all_sessions = []
    stats = {"sessions": 0, "with_dialogue": 0, "human_turns": 0, "total_turns": 0}

    # Process all Claude sessions
    print("Extracting dialogue from Claude sessions...")
    session_files = sorted(glob.glob(str(Path.home() / ".claude/projects/*/*.jsonl")))

    for sp in session_files:
        stats["sessions"] += 1
        session = process_session(sp)
        if session and session["human_turns"] > 0:
            all_sessions.append(session)
            stats["with_dialogue"] += 1
            stats["human_turns"] += session["human_turns"]
            stats["total_turns"] += session["total_turns"]

    # Sort by first timestamp
    all_sessions.sort(key=lambda s: s.get("first_timestamp", "") or "9999")

    # Write unified JSONL
    with open(unified_path, "w") as f:
        for session in all_sessions:
            f.write(json.dumps(session) + "\n")

    # Write per-session markdown files (only for sessions with 3+ human turns)
    md_count = 0
    for session in all_sessions:
        if session["human_turns"] >= 3:
            slug = session["project_slug"] or "unknown"
            ts = session["first_timestamp"][:10] if session["first_timestamp"] else "nodate"
            sid = session["session_id"][:8]
            safe_slug = re.sub(r"[^\w-]", "_", slug)[:40]
            filename = f"{ts}_{safe_slug}_{sid}.md"
            md_path = dialogue_dir / filename
            md_path.write_text(session_to_markdown(session))
            md_count += 1

    # Write index
    with open(index_path, "w") as f:
        f.write("# Dialogue Index — Pure Human↔AI Conversation\n\n")
        f.write(f"**Generated:** {datetime.now().isoformat()[:19]}Z\n")
        f.write(f"**Sessions scanned:** {stats['sessions']}\n")
        f.write(f"**Sessions with dialogue:** {stats['with_dialogue']}\n")
        f.write(f"**Human turns total:** {stats['human_turns']}\n")
        f.write(f"**Dialogue files written:** {md_count} (sessions with 3+ human turns)\n\n")

        # Group by project
        by_project = defaultdict(list)
        for s in all_sessions:
            by_project[s["project_slug"]].append(s)

        f.write("## By Project\n\n")
        f.write("| Project | Sessions | Human Turns | Date Range |\n")
        f.write("|---------|----------|-------------|------------|\n")
        for slug, sessions in sorted(by_project.items(), key=lambda x: -len(x[1])):
            total_ht = sum(s["human_turns"] for s in sessions)
            dates = [s["first_timestamp"][:10] for s in sessions if s["first_timestamp"]]
            date_range = f"{min(dates)}→{max(dates)}" if dates else "?"
            f.write(f"| {slug} | {len(sessions)} | {total_ht} | {date_range} |\n")

        f.write("\n## Recent Dialogues (last 30)\n\n")
        for s in all_sessions[-30:]:
            ts = s["first_timestamp"][:16] if s["first_timestamp"] else "?"
            slug = s["project_slug"]
            ht = s["human_turns"]
            first_prompt = ""
            for t in s["turns"]:
                if t["role"] == "human":
                    first_prompt = t["text"][:120].replace("\n", " ")
                    break
            f.write(f"- **{ts}** [{slug}] ({ht} turns) — {first_prompt}...\n")

    print(f"\nDialogue extraction complete:")
    print(f"  Sessions scanned: {stats['sessions']}")
    print(f"  Sessions with dialogue: {stats['with_dialogue']}")
    print(f"  Human turns: {stats['human_turns']}")
    print(f"  Dialogue markdown files: {md_count}")
    print(f"  Corpus: {unified_path}")
    print(f"  Index: {index_path}")
    print(f"  Dialogues: {dialogue_dir}/")


if __name__ == "__main__":
    main()
