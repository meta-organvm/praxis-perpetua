#!/usr/bin/env python3
"""Extract structured prompt files from all Claude Code session JSONLs.

Reads every top-level session JSONL (excluding subagents), extracts human
prompts with timestamps and tool-call actions, then writes a structured
markdown file per session into praxis-perpetua/sessions/claude/<project-slug>/.

Usage:
    python3 scripts/extract-claude-sessions.py [--dry-run] [--project SLUG]
"""

import json
import os
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

CLAUDE_PROJECTS = Path.home() / ".claude" / "projects"
OUTPUT_BASE = Path(__file__).resolve().parent.parent / "sessions" / "claude"

# Noise filters — skip these as "prompts"
NOISE_PATTERNS = [
    r"^Tool loaded\.$",
    r"^<task-notification>",
    r"^<system-reminder>",
    r"^\s*$",
]
NOISE_RE = [re.compile(p, re.DOTALL) for p in NOISE_PATTERNS]

# Prompt category heuristics
CATEGORIES = {
    "Directives": re.compile(
        r"\b(implement|build|create|add|write|stage|commit|push|merge|deploy|generate|make)\b", re.I
    ),
    "Questions": re.compile(r"\?|^(how|what|where|when|why|is |are |can |do |does )", re.I),
    "Fixes": re.compile(r"\b(fix|error|bug|broken|fail|issue|wrong|crash)\b", re.I),
    "Reviews": re.compile(r"\b(check|verify|review|audit|clean|inspect|summarize|analyze)\b", re.I),
    "Continuations": re.compile(r"\b(continue|all |every |more|next|rest|remaining)\b", re.I),
    "Meta": re.compile(r"\b(export|session|transcript|memory|history|save)\b", re.I),
}


def extract_text(content):
    """Pull human-readable text from message content."""
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts = []
        for c in content:
            if isinstance(c, dict):
                if c.get("type") == "text":
                    parts.append(c.get("text", ""))
                elif c.get("type") == "tool_result":
                    continue  # skip tool results
        return "\n".join(parts).strip()
    return ""


def extract_tool_calls(messages, start_idx, end_idx):
    """Extract tool call names between two user messages."""
    tools = []
    for msg in messages[start_idx:end_idx]:
        if msg.get("type") == "assistant":
            content = msg.get("message", {}).get("content", [])
            if isinstance(content, list):
                for block in content:
                    if isinstance(block, dict) and block.get("type") == "tool_use":
                        name = block.get("name", "unknown")
                        inp = block.get("input", {})
                        # Summarize the tool call
                        if name in ("Read", "read_file"):
                            detail = inp.get("file_path", inp.get("path", ""))
                            tools.append(f"Read `{detail}`")
                        elif name in ("Write", "write_file"):
                            detail = inp.get("file_path", inp.get("path", ""))
                            tools.append(f"Write `{detail}`")
                        elif name in ("Edit", "edit_file"):
                            detail = inp.get("file_path", inp.get("path", ""))
                            tools.append(f"Edit `{detail}`")
                        elif name == "Bash":
                            cmd = inp.get("command", "")[:80]
                            tools.append(f"Bash: `{cmd}`")
                        elif name == "Glob":
                            pat = inp.get("pattern", "")
                            tools.append(f"Glob `{pat}`")
                        elif name == "Grep":
                            pat = inp.get("pattern", "")
                            tools.append(f"Grep `{pat}`")
                        elif name == "Agent":
                            prompt = inp.get("prompt", "")[:60]
                            tools.append(f"Agent: \"{prompt}\"")
                        elif name == "WebSearch":
                            q = inp.get("query", "")[:60]
                            tools.append(f"WebSearch: \"{q}\"")
                        elif name == "WebFetch":
                            u = inp.get("url", "")[:60]
                            tools.append(f"WebFetch: `{u}`")
                        else:
                            tools.append(f"{name}")
    return tools


def is_noise(text):
    """Check if text matches noise patterns."""
    for r in NOISE_RE:
        if r.match(text):
            return True
    return False


def categorize_prompt(text):
    """Return list of matching categories."""
    cats = []
    for name, regex in CATEGORIES.items():
        if regex.search(text[:300]):
            cats.append(name)
    return cats or ["Uncategorized"]


def project_slug(project_dir_name):
    """Convert Claude project dir name to readable slug."""
    # -Users-4jp-Workspace-4444J99-portfolio -> workspace/4444j99/portfolio
    parts = project_dir_name.split("-")
    # Remove leading empty and Users/4jp
    cleaned = []
    skip_next = 0
    raw = project_dir_name
    # Simpler: just strip the prefix
    raw = re.sub(r"^-Users-4jp-?", "", raw)
    raw = re.sub(r"^Workspace-?", "", raw)
    if not raw:
        raw = "home"
    return raw.lower()


def process_session(jsonl_path, project_name):
    """Process a single JSONL into structured data."""
    messages = []
    with open(jsonl_path) as f:
        for line in f:
            try:
                messages.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    if not messages:
        return None

    # Extract session metadata
    session_id = jsonl_path.stem

    # Find timestamps
    timestamps = []
    for msg in messages:
        ts = msg.get("timestamp") or msg.get("message", {}).get("timestamp")
        if ts:
            timestamps.append(ts)

    start_time = None
    end_time = None
    if timestamps:
        try:
            start_time = min(timestamps)
            end_time = max(timestamps)
        except (TypeError, ValueError):
            pass

    # Extract human prompts
    prompts = []
    for i, msg in enumerate(messages):
        if msg.get("type") != "user":
            continue
        content = msg.get("message", {}).get("content", "")
        if not content:
            content = msg.get("content", "")
        text = extract_text(content)
        if not text or len(text) < 3 or is_noise(text):
            continue

        ts = msg.get("timestamp") or msg.get("message", {}).get("timestamp")
        prompts.append({
            "index": len(prompts) + 1,
            "line": i,
            "timestamp": ts,
            "text": text,
            "categories": categorize_prompt(text),
        })

    if not prompts:
        return None

    # Extract tool calls per prompt
    for j, prompt in enumerate(prompts):
        start = prompt["line"]
        end = prompts[j + 1]["line"] if j + 1 < len(prompts) else len(messages)
        prompt["actions"] = extract_tool_calls(messages, start, end)

    # Compute duration
    duration_str = "unknown"
    if start_time and end_time:
        try:
            if isinstance(start_time, str):
                t0 = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
                t1 = datetime.fromisoformat(end_time.replace("Z", "+00:00"))
            elif isinstance(start_time, (int, float)):
                t0 = datetime.fromtimestamp(start_time / 1000 if start_time > 1e12 else start_time, tz=timezone.utc)
                t1 = datetime.fromtimestamp(end_time / 1000 if end_time > 1e12 else end_time, tz=timezone.utc)
            else:
                t0 = t1 = None
            if t0 and t1:
                delta = (t1 - t0).total_seconds()
                if delta < 60:
                    duration_str = f"~{int(delta)}s"
                elif delta < 3600:
                    duration_str = f"~{int(delta/60)} min"
                else:
                    duration_str = f"~{int(delta/3600)}h {int((delta%3600)/60)}m"
        except Exception:
            pass

    # Category summary
    cat_counts = Counter()
    for p in prompts:
        for c in p["categories"]:
            cat_counts[c] += 1

    # Date for filename
    date_str = "unknown"
    if start_time:
        try:
            if isinstance(start_time, str):
                dt = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
            elif isinstance(start_time, (int, float)):
                dt = datetime.fromtimestamp(start_time / 1000 if start_time > 1e12 else start_time, tz=timezone.utc)
            else:
                dt = None
            if dt:
                date_str = dt.strftime("%Y-%m-%d")
        except Exception:
            pass

    return {
        "session_id": session_id,
        "project": project_name,
        "date": date_str,
        "duration": duration_str,
        "start_time": start_time,
        "prompt_count": len(prompts),
        "prompts": prompts,
        "cat_counts": dict(cat_counts),
        "total_messages": len(messages),
    }


def render_markdown(data):
    """Render session data as structured markdown."""
    lines = []
    lines.append(f"# Session Prompts: {data['date']}")
    lines.append("")
    lines.append(f"**Session ID:** `{data['session_id']}`")
    lines.append(f"**Project:** `{data['project']}`")
    lines.append(f"**Duration:** {data['duration']}")
    lines.append(f"**Prompts:** {data['prompt_count']}")
    lines.append(f"**Total JSONL messages:** {data['total_messages']}")
    lines.append("")
    lines.append("---")
    lines.append("")

    for p in data["prompts"]:
        ts_display = ""
        if p["timestamp"]:
            try:
                if isinstance(p["timestamp"], str):
                    dt = datetime.fromisoformat(p["timestamp"].replace("Z", "+00:00"))
                    ts_display = dt.strftime("%Y-%m-%d %H:%M:%S")
                elif isinstance(p["timestamp"], (int, float)):
                    ts_val = p["timestamp"] / 1000 if p["timestamp"] > 1e12 else p["timestamp"]
                    dt = datetime.fromtimestamp(ts_val, tz=timezone.utc)
                    ts_display = dt.strftime("%Y-%m-%d %H:%M:%S UTC")
            except Exception:
                ts_display = str(p["timestamp"])

        lines.append(f"### P{p['index']}" + (f" — {ts_display}" if ts_display else ""))
        lines.append("")

        # Truncate very long prompts to first 500 chars
        text = p["text"]
        if len(text) > 500:
            text = text[:500] + "\n\n*[truncated — full text in JSONL]*"
        lines.append(text)
        lines.append("")

        if p["actions"]:
            lines.append("**Actions taken:**")
            for a in p["actions"][:20]:  # cap at 20 actions per prompt
                lines.append(f"- {a}")
            if len(p["actions"]) > 20:
                lines.append(f"- *...and {len(p['actions']) - 20} more*")
            lines.append("")

        lines.append("---")
        lines.append("")

    # Summary
    lines.append("## Prompt Summary")
    lines.append("")
    lines.append(f"**Total prompts:** {data['prompt_count']}")
    lines.append(f"**Session duration:** {data['duration']}")
    lines.append("")
    lines.append("### Prompt Categories")
    lines.append("")
    for cat, count in sorted(data["cat_counts"].items(), key=lambda x: -x[1]):
        lines.append(f"- **{cat}**: {count}")
    lines.append("")

    return "\n".join(lines)


def main():
    dry_run = "--dry-run" in sys.argv
    project_filter = None
    if "--project" in sys.argv:
        idx = sys.argv.index("--project")
        if idx + 1 < len(sys.argv):
            project_filter = sys.argv[idx + 1]

    # Discover all top-level session JSONLs
    sessions = []
    for project_dir in sorted(CLAUDE_PROJECTS.iterdir()):
        if not project_dir.is_dir():
            continue
        slug = project_slug(project_dir.name)
        if project_filter and project_filter not in slug:
            continue
        for jsonl in sorted(project_dir.glob("*.jsonl")):
            if "subagent" in jsonl.name:
                continue
            sessions.append((jsonl, slug, project_dir.name))

    print(f"Found {len(sessions)} sessions across {len(set(s[1] for s in sessions))} projects")

    total_prompts = 0
    processed = 0
    skipped = 0
    errors = 0

    # Per-project index data
    project_index = {}

    for jsonl_path, slug, raw_dir in sessions:
        try:
            data = process_session(jsonl_path, slug)
        except Exception as e:
            print(f"  ERROR: {jsonl_path.name}: {e}")
            errors += 1
            continue

        if data is None or data["prompt_count"] == 0:
            skipped += 1
            continue

        processed += 1
        total_prompts += data["prompt_count"]

        # Output path
        out_dir = OUTPUT_BASE / slug
        filename = f"{data['date']}--{data['session_id'][:8]}--prompts.md"
        out_path = out_dir / filename

        if slug not in project_index:
            project_index[slug] = []
        project_index[slug].append({
            "session_id": data["session_id"],
            "date": data["date"],
            "duration": data["duration"],
            "prompts": data["prompt_count"],
            "filename": filename,
        })

        if dry_run:
            print(f"  [DRY] {slug}/{filename} — {data['prompt_count']} prompts, {data['duration']}")
            continue

        out_dir.mkdir(parents=True, exist_ok=True)
        md = render_markdown(data)
        out_path.write_text(md)

    # Write master index
    if not dry_run and project_index:
        index_lines = ["# Claude Session Index", ""]
        index_lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        index_lines.append(f"**Sessions processed:** {processed}")
        index_lines.append(f"**Total prompts extracted:** {total_prompts}")
        index_lines.append(f"**Skipped (empty):** {skipped}")
        index_lines.append(f"**Errors:** {errors}")
        index_lines.append("")

        for slug in sorted(project_index.keys()):
            entries = project_index[slug]
            total_p = sum(e["prompts"] for e in entries)
            index_lines.append(f"## `{slug}` ({len(entries)} sessions, {total_p} prompts)")
            index_lines.append("")
            index_lines.append("| Date | Session | Prompts | Duration |")
            index_lines.append("|------|---------|---------|----------|")
            for e in sorted(entries, key=lambda x: x["date"]):
                index_lines.append(
                    f"| {e['date']} | [`{e['session_id'][:8]}`]({slug}/{e['filename']}) "
                    f"| {e['prompts']} | {e['duration']} |"
                )
            index_lines.append("")

        index_path = OUTPUT_BASE / "INDEX.md"
        index_path.write_text("\n".join(index_lines))

    print(f"\nDone: {processed} sessions, {total_prompts} prompts, {skipped} skipped, {errors} errors")
    if not dry_run:
        print(f"Output: {OUTPUT_BASE}/")


if __name__ == "__main__":
    main()
