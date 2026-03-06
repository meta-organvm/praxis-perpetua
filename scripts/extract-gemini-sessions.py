#!/usr/bin/env python3
"""Extract structured prompt files from all Gemini CLI session JSONs.

Covers two locations:
1. ~/.local/share/gemini/tmp/*/chats/*.json  (Gemini CLI project sessions)
2. ~/.local/share/gemini/antigravity/brain/*/task.md  (Antigravity tasks)
3. ~/.local/share/gemini/antigravity/conversations/*.pb  (binary — cataloged only)

Usage:
    python3 scripts/extract-gemini-sessions.py [--dry-run]
"""

import json
import os
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

GEMINI_TMP = Path.home() / ".local" / "share" / "gemini" / "tmp"
GEMINI_PLANS = Path.home() / ".local" / "share" / "gemini" / "plans"
ANTIGRAVITY = Path.home() / ".local" / "share" / "gemini" / "antigravity"
OUTPUT_BASE = Path(__file__).resolve().parent.parent / "sessions" / "gemini"

NOISE_RE = [
    re.compile(r"^\s*$"),
    re.compile(r"^ok$", re.I),
    re.compile(r"^y$", re.I),
    re.compile(r"^yes$", re.I),
]

CATEGORIES = {
    "Directives": re.compile(r"\b(implement|build|create|add|write|stage|commit|push|merge|deploy|generate|make|fix|update)\b", re.I),
    "Questions": re.compile(r"\?|^(how|what|where|when|why|is |are |can |do |does )", re.I),
    "Reviews": re.compile(r"\b(check|verify|review|audit|clean|inspect|summarize|analyze|look|read|show)\b", re.I),
    "Continuations": re.compile(r"\b(continue|next|more|go ahead|proceed)\b", re.I),
}


def is_noise(text):
    return any(r.match(text.strip()) for r in NOISE_RE)


def categorize(text):
    cats = []
    for name, regex in CATEGORIES.items():
        if regex.search(text[:300]):
            cats.append(name)
    return cats or ["Uncategorized"]


def process_gemini_chat(chat_json_path, project_slug):
    """Process a single Gemini CLI chat JSON."""
    try:
        data = json.loads(chat_json_path.read_text())
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None

    # Gemini chat JSON: {sessionId, projectHash, startTime, lastUpdated, messages[]}
    # Each message: {id, timestamp, type: "user"|"gemini"|"info"|"error", content: [{text}]}
    messages = []
    if isinstance(data, dict):
        messages = data.get("messages", [])
        session_meta = {
            "sessionId": data.get("sessionId", ""),
            "startTime": data.get("startTime", ""),
            "lastUpdated": data.get("lastUpdated", ""),
        }
    elif isinstance(data, list):
        messages = data
        session_meta = {}

    if not messages:
        return None

    prompts = []
    for msg in messages:
        # Gemini uses type="user", not role="user"
        msg_type = msg.get("type", msg.get("role", ""))
        if msg_type not in ("user", "human"):
            continue

        # Content is [{text: "..."}, ...] or a string
        text = ""
        content = msg.get("content", msg.get("parts", msg.get("text", "")))
        if isinstance(content, str):
            text = content.strip()
        elif isinstance(content, list):
            for part in content:
                if isinstance(part, str):
                    text += part
                elif isinstance(part, dict):
                    text += part.get("text", "")
        elif isinstance(content, dict):
            text = content.get("text", "")

        if not text or len(text) < 3 or is_noise(text):
            continue

        ts = msg.get("timestamp", "")
        prompts.append({
            "index": len(prompts) + 1,
            "timestamp": ts,
            "text": text.strip(),
            "categories": categorize(text),
        })

    if not prompts:
        return None

    # Get date from session metadata or first prompt timestamp or file mtime
    date_str = "unknown"
    start_time = session_meta.get("startTime", "")
    if start_time:
        try:
            dt = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
            date_str = dt.strftime("%Y-%m-%d")
        except Exception:
            pass
    if date_str == "unknown":
        mtime = chat_json_path.stat().st_mtime
        date_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")

    # Compute duration
    duration_str = "unknown"
    st = session_meta.get("startTime", "")
    et = session_meta.get("lastUpdated", "")
    if st and et:
        try:
            t0 = datetime.fromisoformat(st.replace("Z", "+00:00"))
            t1 = datetime.fromisoformat(et.replace("Z", "+00:00"))
            delta = (t1 - t0).total_seconds()
            if delta < 60:
                duration_str = f"~{int(delta)}s"
            elif delta < 3600:
                duration_str = f"~{int(delta/60)} min"
            else:
                duration_str = f"~{int(delta/3600)}h {int((delta%3600)/60)}m"
        except Exception:
            pass

    cat_counts = Counter()
    for p in prompts:
        for c in p["categories"]:
            cat_counts[c] += 1

    return {
        "session_id": chat_json_path.stem,
        "project": project_slug,
        "date": date_str,
        "duration": duration_str,
        "prompt_count": len(prompts),
        "prompts": prompts,
        "cat_counts": dict(cat_counts),
        "source": "gemini-cli",
        "total_messages": len(messages),
    }


def process_antigravity_task(task_md_path, brain_id):
    """Process an Antigravity brain task.md file."""
    try:
        text = task_md_path.read_text()
    except UnicodeDecodeError:
        return None

    if not text.strip():
        return None

    # Also grab resolved versions
    parent = task_md_path.parent
    resolved = sorted(parent.glob("task.md.resolved*"))

    mtime = task_md_path.stat().st_mtime
    date_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")

    return {
        "session_id": brain_id,
        "project": "antigravity",
        "date": date_str,
        "task_text": text.strip()[:2000],
        "resolved_count": len(resolved),
        "source": "antigravity-brain",
    }


def render_chat_md(data):
    lines = []
    lines.append(f"# Gemini Session: {data['date']}")
    lines.append("")
    lines.append(f"**Session ID:** `{data['session_id']}`")
    lines.append(f"**Project:** `{data['project']}`")
    lines.append(f"**Source:** {data['source']}")
    lines.append(f"**Duration:** {data.get('duration', 'unknown')}")
    lines.append(f"**Prompts:** {data['prompt_count']}")
    lines.append(f"**Total messages:** {data.get('total_messages', 'unknown')}")
    lines.append("")
    lines.append("---")
    lines.append("")

    for p in data["prompts"]:
        ts_display = ""
        ts = p.get("timestamp", "")
        if ts:
            try:
                dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                ts_display = dt.strftime("%Y-%m-%d %H:%M:%S")
            except Exception:
                ts_display = ts
        lines.append(f"### P{p['index']}" + (f" — {ts_display}" if ts_display else ""))
        lines.append("")
        text = p["text"]
        if len(text) > 500:
            text = text[:500] + "\n\n*[truncated]*"
        lines.append(text)
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("## Prompt Summary")
    lines.append("")
    lines.append(f"**Total prompts:** {data['prompt_count']}")
    lines.append("")
    lines.append("### Categories")
    lines.append("")
    for cat, count in sorted(data["cat_counts"].items(), key=lambda x: -x[1]):
        lines.append(f"- **{cat}**: {count}")
    lines.append("")
    return "\n".join(lines)


def render_task_md(data):
    lines = []
    lines.append(f"# Antigravity Task: {data['date']}")
    lines.append("")
    lines.append(f"**Brain ID:** `{data['session_id']}`")
    lines.append(f"**Source:** {data['source']}")
    lines.append(f"**Resolved versions:** {data['resolved_count']}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Task")
    lines.append("")
    lines.append(data["task_text"])
    lines.append("")
    return "\n".join(lines)


def main():
    dry_run = "--dry-run" in sys.argv

    total_prompts = 0
    processed = 0
    skipped = 0

    project_index = {}

    # 1. Process Gemini CLI sessions
    print("=== Gemini CLI Sessions ===")
    if GEMINI_TMP.exists():
        for project_dir in sorted(GEMINI_TMP.iterdir()):
            if not project_dir.is_dir():
                continue
            chats_dir = project_dir / "chats"
            if not chats_dir.exists():
                continue

            slug = project_dir.name
            # Truncate hash-based slugs
            if len(slug) > 20 and re.match(r'^[0-9a-f]+$', slug):
                slug = f"hash-{slug[:12]}"

            for chat_json in sorted(chats_dir.glob("*.json")):
                data = process_gemini_chat(chat_json, slug)
                if data is None:
                    skipped += 1
                    continue

                processed += 1
                total_prompts += data["prompt_count"]

                out_dir = OUTPUT_BASE / "cli" / slug
                filename = f"{data['date']}--{data['session_id'][:12]}--prompts.md"
                out_path = out_dir / filename

                if slug not in project_index:
                    project_index[slug] = []
                project_index[slug].append({
                    "session_id": data["session_id"],
                    "date": data["date"],
                    "duration": data.get("duration", "unknown"),
                    "prompts": data["prompt_count"],
                    "filename": f"cli/{slug}/{filename}",
                })

                if dry_run:
                    print(f"  [DRY] cli/{slug}/{filename} — {data['prompt_count']} prompts")
                    continue

                out_dir.mkdir(parents=True, exist_ok=True)
                out_path.write_text(render_chat_md(data))

    # 2. Process Antigravity brain tasks
    print("\n=== Antigravity Brain Tasks ===")
    brain_dir = ANTIGRAVITY / "brain"
    ag_count = 0
    if brain_dir.exists():
        for brain_id_dir in sorted(brain_dir.iterdir()):
            if not brain_id_dir.is_dir():
                continue
            task_md = brain_id_dir / "task.md"
            if not task_md.exists():
                continue

            brain_id = brain_id_dir.name
            data = process_antigravity_task(task_md, brain_id)
            if data is None:
                skipped += 1
                continue

            ag_count += 1

            out_dir = OUTPUT_BASE / "antigravity"
            filename = f"{data['date']}--{brain_id[:8]}--task.md"
            out_path = out_dir / filename

            if "antigravity" not in project_index:
                project_index["antigravity"] = []
            project_index["antigravity"].append({
                "session_id": brain_id,
                "date": data["date"],
                "prompts": data.get("resolved_count", 0),
                "filename": f"antigravity/{filename}",
            })

            if dry_run:
                print(f"  [DRY] antigravity/{filename} — {data['resolved_count']} resolved")
                continue

            out_dir.mkdir(parents=True, exist_ok=True)
            out_path.write_text(render_task_md(data))

    # 3. Catalog Antigravity conversations (protobuf — not parseable, just count)
    conv_dir = ANTIGRAVITY / "conversations"
    conv_count = 0
    if conv_dir.exists():
        conv_count = len(list(conv_dir.glob("*.pb")))

    print(f"\n  Antigravity conversations (protobuf, cataloged only): {conv_count}")
    print(f"  Antigravity brain tasks: {ag_count}")

    # 4. Copy Gemini plans
    print("\n=== Gemini Plans ===")
    plan_count = 0
    if GEMINI_PLANS.exists():
        plans_out = OUTPUT_BASE / "plans"
        for plan_file in sorted(GEMINI_PLANS.glob("*.md")):
            plan_count += 1
            if not dry_run:
                plans_out.mkdir(parents=True, exist_ok=True)
                (plans_out / plan_file.name).write_text(plan_file.read_text())
            print(f"  {'[DRY] ' if dry_run else ''}plans/{plan_file.name}")

    # Write index
    if not dry_run and project_index:
        index_lines = ["# Gemini Session Index", ""]
        index_lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        index_lines.append(f"**CLI sessions processed:** {processed}")
        index_lines.append(f"**Total prompts extracted:** {total_prompts}")
        index_lines.append(f"**Antigravity tasks:** {ag_count}")
        index_lines.append(f"**Antigravity conversations (protobuf):** {conv_count}")
        index_lines.append(f"**Gemini plans:** {plan_count}")
        index_lines.append(f"**Skipped (empty):** {skipped}")
        index_lines.append("")

        for slug in sorted(project_index.keys()):
            entries = project_index[slug]
            total_p = sum(e["prompts"] for e in entries)
            index_lines.append(f"## `{slug}` ({len(entries)} sessions)")
            index_lines.append("")
            index_lines.append("| Date | Session | Prompts | Duration |")
            index_lines.append("|------|---------|---------|----------|")
            for e in sorted(entries, key=lambda x: x["date"]):
                index_lines.append(
                    f"| {e['date']} | [`{e['session_id'][:12]}`]({e['filename']}) "
                    f"| {e['prompts']} | {e.get('duration', '')} |"
                )
            index_lines.append("")

        (OUTPUT_BASE / "INDEX.md").write_text("\n".join(index_lines))

    print(f"\nDone: {processed} CLI sessions, {total_prompts} prompts, {ag_count} brain tasks, {plan_count} plans, {skipped} skipped")


if __name__ == "__main__":
    main()
