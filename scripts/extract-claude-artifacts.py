#!/usr/bin/env python3
"""Extract Claude plans, tasks, todos, memory files, and history into praxis-perpetua.

Covers:
1. ~/.claude/plans/**/*.md  (293 plan files)
2. ~/.claude/tasks/*/       (229 task JSONs across 569 dirs)
3. ~/.claude/todos/*.json   (341 todo files)
4. ~/.claude/projects/*/memory/MEMORY.md  (22 memory files)
5. ~/.claude/history.jsonl  (3829 entries — session-level history)

Usage:
    python3 scripts/extract-claude-artifacts.py [--dry-run]
"""

import json
import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

CLAUDE_DIR = Path.home() / ".claude"
OUTPUT_BASE = Path(__file__).resolve().parent.parent / "sessions" / "claude-artifacts"


def project_slug(name):
    slug = re.sub(r"^-Users-4jp-?", "", name)
    slug = re.sub(r"^Workspace-?", "", slug) or "home"
    return slug.lower()


def process_plans(dry_run):
    """Extract all plan files with metadata."""
    plans_dir = CLAUDE_DIR / "plans"
    if not plans_dir.exists():
        return 0

    out_dir = OUTPUT_BASE / "plans"
    count = 0

    for md_file in sorted(plans_dir.rglob("*.md")):
        rel = md_file.relative_to(plans_dir)
        out_path = out_dir / rel

        count += 1
        if dry_run:
            continue

        out_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(md_file, out_path)

    return count


def process_tasks(dry_run):
    """Extract task JSONs with summary."""
    tasks_dir = CLAUDE_DIR / "tasks"
    if not tasks_dir.exists():
        return 0, 0

    out_dir = OUTPUT_BASE / "tasks"
    session_count = 0
    task_count = 0
    summaries = []

    for session_dir in sorted(tasks_dir.iterdir()):
        if not session_dir.is_dir():
            continue
        session_count += 1
        session_id = session_dir.name

        tasks = []
        for task_json in sorted(session_dir.glob("*.json")):
            task_count += 1
            try:
                data = json.loads(task_json.read_text())
                tasks.append({
                    "id": task_json.stem,
                    "status": data.get("status", "unknown"),
                    "description": (data.get("description", data.get("content", ""))[:200]
                                   if isinstance(data.get("description", data.get("content", "")), str)
                                   else str(data.get("description", ""))[:200]),
                })
            except (json.JSONDecodeError, UnicodeDecodeError):
                tasks.append({"id": task_json.stem, "status": "parse_error", "description": ""})

        summaries.append({
            "session_id": session_id,
            "task_count": len(tasks),
            "tasks": tasks,
        })

        if not dry_run:
            sess_out = out_dir / session_id
            sess_out.mkdir(parents=True, exist_ok=True)
            for task_json in session_dir.glob("*.json"):
                shutil.copy2(task_json, sess_out / task_json.name)

    # Write task summary index
    if not dry_run and summaries:
        lines = ["# Claude Task Index", ""]
        lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        lines.append(f"**Sessions with tasks:** {session_count}")
        lines.append(f"**Total tasks:** {task_count}")
        lines.append("")
        lines.append("| Session | Tasks | Statuses |")
        lines.append("|---------|-------|----------|")
        for s in summaries:
            statuses = ", ".join(set(t["status"] for t in s["tasks"]))
            lines.append(f"| `{s['session_id'][:8]}` | {s['task_count']} | {statuses} |")
        lines.append("")
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "INDEX.md").write_text("\n".join(lines))

    return session_count, task_count


def process_todos(dry_run):
    """Extract todo JSONs."""
    todos_dir = CLAUDE_DIR / "todos"
    if not todos_dir.exists():
        return 0

    out_dir = OUTPUT_BASE / "todos"
    count = 0

    for todo_json in sorted(todos_dir.glob("*.json")):
        count += 1
        if not dry_run:
            out_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(todo_json, out_dir / todo_json.name)

    # Write summary
    if not dry_run and count > 0:
        summaries = []
        for todo_json in sorted(todos_dir.glob("*.json")):
            try:
                data = json.loads(todo_json.read_text())
                items = data if isinstance(data, list) else data.get("todos", data.get("items", []))
                if isinstance(items, list):
                    total = len(items)
                    done = sum(1 for i in items if isinstance(i, dict) and
                              i.get("status") in ("done", "completed", "complete"))
                else:
                    total = 0
                    done = 0
                summaries.append({
                    "file": todo_json.name,
                    "total": total,
                    "done": done,
                })
            except (json.JSONDecodeError, UnicodeDecodeError):
                summaries.append({"file": todo_json.name, "total": 0, "done": 0})

        lines = ["# Claude Todo Index", ""]
        lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        lines.append(f"**Todo files:** {count}")
        lines.append("")
        lines.append("| File | Items | Done |")
        lines.append("|------|-------|------|")
        for s in summaries:
            lines.append(f"| `{s['file'][:40]}` | {s['total']} | {s['done']} |")
        lines.append("")
        (out_dir / "INDEX.md").write_text("\n".join(lines))

    return count


def process_memory_files(dry_run):
    """Extract all MEMORY.md files."""
    projects_dir = CLAUDE_DIR / "projects"
    if not projects_dir.exists():
        return 0

    out_dir = OUTPUT_BASE / "memory"
    count = 0

    for project_dir in sorted(projects_dir.iterdir()):
        if not project_dir.is_dir():
            continue
        memory_file = project_dir / "memory" / "MEMORY.md"
        if not memory_file.exists():
            continue

        slug = project_slug(project_dir.name)
        count += 1

        if not dry_run:
            out_dir.mkdir(parents=True, exist_ok=True)
            out_path = out_dir / f"{slug}--MEMORY.md"
            shutil.copy2(memory_file, out_path)

    return count


def process_history(dry_run):
    """Extract Claude history.jsonl into a readable summary."""
    history_path = CLAUDE_DIR / "history.jsonl"
    if not history_path.exists():
        return 0

    entries = []
    with open(history_path) as f:
        for line in f:
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    if not dry_run and entries:
        out_dir = OUTPUT_BASE / "history"
        out_dir.mkdir(parents=True, exist_ok=True)

        lines = ["# Claude Command History", ""]
        lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        lines.append(f"**Total entries:** {len(entries)}")
        lines.append("")

        # Group by date
        by_date = {}
        for e in entries:
            ts = e.get("timestamp", e.get("ts", ""))
            cmd = e.get("command", e.get("input", e.get("text", "")))
            cwd = e.get("cwd", e.get("directory", ""))
            session = e.get("sessionId", e.get("session_id", ""))

            date = "unknown"
            if ts:
                try:
                    if isinstance(ts, str):
                        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                    elif isinstance(ts, (int, float)):
                        dt = datetime.fromtimestamp(ts / 1000 if ts > 1e12 else ts)
                    else:
                        dt = None
                    if dt:
                        date = dt.strftime("%Y-%m-%d")
                except Exception:
                    pass

            if date not in by_date:
                by_date[date] = []
            by_date[date].append({
                "cmd": str(cmd)[:200] if cmd else "",
                "cwd": str(cwd)[:100] if cwd else "",
                "session": str(session)[:8] if session else "",
            })

        for date in sorted(by_date.keys()):
            entries_for_date = by_date[date]
            lines.append(f"## {date} ({len(entries_for_date)} entries)")
            lines.append("")
            for e in entries_for_date[:50]:  # cap per day
                if e["cmd"]:
                    lines.append(f"- `{e['cmd'][:120]}`" + (f" (session: {e['session']})" if e["session"] else ""))
            if len(entries_for_date) > 50:
                lines.append(f"- *...and {len(entries_for_date) - 50} more*")
            lines.append("")

        (out_dir / "history-summary.md").write_text("\n".join(lines))

    return len(entries)


def main():
    dry_run = "--dry-run" in sys.argv

    print("=== Claude Plans ===")
    plan_count = process_plans(dry_run)
    print(f"  Plans: {plan_count}")

    print("\n=== Claude Tasks ===")
    task_sessions, task_count = process_tasks(dry_run)
    print(f"  Task sessions: {task_sessions}, Tasks: {task_count}")

    print("\n=== Claude Todos ===")
    todo_count = process_todos(dry_run)
    print(f"  Todos: {todo_count}")

    print("\n=== Claude Memory Files ===")
    memory_count = process_memory_files(dry_run)
    print(f"  Memory files: {memory_count}")

    print("\n=== Claude History ===")
    history_count = process_history(dry_run)
    print(f"  History entries: {history_count}")

    # Master index
    if not dry_run:
        OUTPUT_BASE.mkdir(parents=True, exist_ok=True)
        lines = ["# Claude Artifacts Index", ""]
        lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        lines.append("")
        lines.append(f"| Artifact | Count |")
        lines.append(f"|----------|-------|")
        lines.append(f"| Plans | {plan_count} |")
        lines.append(f"| Task sessions | {task_sessions} |")
        lines.append(f"| Individual tasks | {task_count} |")
        lines.append(f"| Todo files | {todo_count} |")
        lines.append(f"| Memory files | {memory_count} |")
        lines.append(f"| History entries | {history_count} |")
        lines.append("")
        (OUTPUT_BASE / "INDEX.md").write_text("\n".join(lines))

    print(f"\nDone. Output: {OUTPUT_BASE}/")


if __name__ == "__main__":
    main()
