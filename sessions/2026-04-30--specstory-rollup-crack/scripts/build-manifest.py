#!/usr/bin/env python3
"""Build SpecStory rollup manifest — single streaming pass.

Output TSV: session_idx, line_start, line_end, timestamp, uuid, first_user_prompt(120 chars).
"""

import re
import sys
from pathlib import Path

ROLLUP = Path("~/Workspace/SpecStory, Markdown v2.md")
OUT = Path("~/Workspace/.specstory/rollup-manifest.tsv")

HEADER_RE = re.compile(r"^# (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}(?:[+-]\d{4}|Z))$")
UUID_RE = re.compile(r"^<!-- Claude Code Session ([0-9a-f-]+) \(.+\) -->$")
USER_RE = re.compile(r"^_\*\*User \(.+\)\*\*_$")


def main() -> None:
    sessions: list[dict] = []
    current: dict | None = None
    looking_for_uuid = False
    looking_for_user_marker = False
    capturing_first_prompt = False
    total_lines = 0

    with open(ROLLUP, "r", encoding="utf-8", errors="replace") as fh:
        for lineno, raw in enumerate(fh, start=1):
            total_lines = lineno
            stripped = raw.rstrip("\n")

            m = HEADER_RE.match(stripped)
            if m:
                if current is not None:
                    current["line_end"] = lineno - 1
                    sessions.append(current)
                current = {
                    "session_idx": len(sessions) + 1,
                    "line_start": lineno,
                    "line_end": None,
                    "timestamp": m.group(1),
                    "uuid": "",
                    "first_user_prompt": "",
                }
                looking_for_uuid = True
                looking_for_user_marker = True
                capturing_first_prompt = False
                continue

            if current is None:
                continue

            if looking_for_uuid:
                mu = UUID_RE.match(stripped)
                if mu:
                    current["uuid"] = mu.group(1)
                    looking_for_uuid = False
                    continue
                if stripped and not stripped.startswith("<!--"):
                    looking_for_uuid = False

            if looking_for_user_marker and USER_RE.match(stripped):
                looking_for_user_marker = False
                capturing_first_prompt = True
                continue

            if capturing_first_prompt and stripped.strip():
                current["first_user_prompt"] = stripped.strip()[:120]
                capturing_first_prompt = False

    if current is not None:
        current["line_end"] = total_lines
        sessions.append(current)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("session_idx\tline_start\tline_end\ttimestamp\tuuid\tfirst_user_prompt\n")
        for s in sessions:
            prompt = s["first_user_prompt"].replace("\t", " ").replace("\r", " ")
            fh.write(
                f"{s['session_idx']}\t{s['line_start']}\t{s['line_end']}\t"
                f"{s['timestamp']}\t{s['uuid']}\t{prompt}\n"
            )

    print(f"sessions: {len(sessions)}", file=sys.stderr)
    print(f"total_lines: {total_lines}", file=sys.stderr)
    print(f"output: {OUT}", file=sys.stderr)


if __name__ == "__main__":
    main()
