#!/usr/bin/env python3
"""Build the navigable index for the SpecStory rollup.

Reads:
  - ~/Workspace/.specstory/rollup-manifest.tsv
  - ~/Workspace/.specstory/history/*.md (for substrate UUID -> filename map)

Writes:
  - ~/Workspace/.specstory/SpecStory-v2.INDEX.md

The index is a chronologically-sorted table of all 109 rollup sessions with
direct line-jump coordinates and substrate cross-references. After this exists,
the rollup is fully tractable: any read against it is an index lookup.
"""

import csv
import re
from collections import defaultdict
from pathlib import Path

MANIFEST = Path("~/Workspace/.specstory/rollup-manifest.tsv")
HISTORY = Path("~/Workspace/.specstory/history")
ROLLUP = Path("~/Workspace/SpecStory, Markdown v2.md")
OUT = Path("~/Workspace/.specstory/SpecStory-v2.INDEX.md")

SESSION_RE = re.compile(
    r"^<!-- (?P<agent>[A-Za-z][A-Za-z ]*?) Session (?P<uuid>[0-9a-f-]+) \(.+\) -->$"
)


def index_substrate_uuids() -> dict[str, list[str]]:
    by_uuid: dict[str, list[str]] = defaultdict(list)
    for p in sorted(HISTORY.glob("*.md")):
        with open(p, "r", encoding="utf-8", errors="replace") as fh:
            for i, line in enumerate(fh):
                if i > 12:
                    break
                ms = SESSION_RE.match(line.rstrip("\n"))
                if ms:
                    by_uuid[ms.group("uuid")].append(p.name)
                    break
    return by_uuid


def main() -> None:
    rollup_rows: list[dict] = []
    with open(MANIFEST, "r") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            r["line_start"] = int(r["line_start"])
            r["line_end"] = int(r["line_end"])
            r["span"] = r["line_end"] - r["line_start"] + 1
            rollup_rows.append(r)

    rollup_rows.sort(key=lambda r: r["timestamp"])

    substrate_uuids = index_substrate_uuids()

    agent_counts = defaultdict(int)
    in_substrate = 0
    rollup_only = 0
    same_ts_clusters = defaultdict(list)
    for r in rollup_rows:
        agent_counts[r["agent"]] += 1
        same_ts_clusters[r["timestamp"]].append(r)
        if r["uuid"] in substrate_uuids:
            in_substrate += 1
        else:
            rollup_only += 1

    dups = [v for v in same_ts_clusters.values() if len(v) > 1]

    rollup_size_mb = ROLLUP.stat().st_size / (1024 * 1024)
    rollup_lines = max(r["line_end"] for r in rollup_rows) if rollup_rows else 0

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("# SpecStory Rollup v2 — Navigable Index\n\n")
        fh.write(f"**Source:** `{ROLLUP}` ({rollup_size_mb:.1f} MB, {rollup_lines:,} lines)  \n")
        fh.write(f"**Manifest:** `{MANIFEST}`  \n")
        fh.write(f"**Substrate:** `{HISTORY}` (200 files post-recovery, 116 unique UUIDs as of last reconciliation)  \n")
        fh.write(f"**Reconciliation report:** `rollup-vs-substrate.md`  \n\n")

        fh.write("## How to use this index\n\n")
        fh.write("To read any session in the rollup directly:\n\n")
        fh.write("```\nRead tool: \n  file_path = \"~/Workspace/SpecStory, Markdown v2.md\"\n  offset = <line_start>\n  limit = <span>  # i.e. line_end - line_start + 1\n```\n\n")
        fh.write("To read the same session in the substrate (preferred — pre-split, no offset math):\n\n")
        fh.write("```\nRead tool: \n  file_path = \"~/Workspace/.specstory/history/<filename>\"\n```\n\n")

        fh.write("## Counts\n\n")
        fh.write(f"- **Total rollup sessions:** {len(rollup_rows)}\n")
        fh.write(f"- **In substrate (BOTH):** {in_substrate}\n")
        fh.write(f"- **Rollup-only (recovered to substrate):** {rollup_only} (was 2 EXPORT-ONLY before Phase 2 recovery)\n")
        fh.write(f"- **Same-timestamp clusters:** {len(dups)}\n")
        fh.write(f"- **Agent distribution:**\n")
        for a, c in sorted(agent_counts.items(), key=lambda x: -x[1]):
            fh.write(f"  - {a}: {c}\n")
        fh.write("\n")

        fh.write("## Same-second clusters (require UUID disambiguation)\n\n")
        if not dups:
            fh.write("*(none)*\n\n")
        else:
            for cluster in dups:
                ts = cluster[0]["timestamp"]
                fh.write(f"- **{ts}** — {len(cluster)} sessions: ")
                fh.write(", ".join(f"#{r['session_idx']} (`{r['uuid'][:8]}…`)" for r in cluster))
                fh.write("\n")
            fh.write("\n")

        fh.write("## Sessions (chronological)\n\n")
        fh.write("| # | timestamp | agent | UUID | lines | span | substrate twin | first prompt |\n")
        fh.write("|---|---|---|---|---|---|---|---|\n")
        for r in rollup_rows:
            uuid_short = r["uuid"][:8] + "…" if r["uuid"] else "—"
            substrate_files = substrate_uuids.get(r["uuid"], [])
            substrate_cell = "—"
            if substrate_files:
                if len(substrate_files) == 1:
                    substrate_cell = f"`{substrate_files[0]}`"
                else:
                    short = substrate_files[0]
                    substrate_cell = f"`{short}` (+{len(substrate_files)-1})"
            prompt = (r["first_user_prompt"] or "").replace("|", "\\|").replace("`", "ʼ")[:80]
            fh.write(
                f"| {r['session_idx']} | {r['timestamp']} | {r['agent']} | `{uuid_short}` "
                f"| {r['line_start']}-{r['line_end']} | {r['span']:,} | {substrate_cell} | {prompt} |\n"
            )

        fh.write("\n## Footnotes\n\n")
        fh.write("- **Substrate doubling:** SpecStory CLI wrote some sessions twice (local-TZ + UTC filenames). When a row shows `(+N)` in the substrate-twin column, that session has N additional substrate filenames pointing at the same UUID.\n")
        fh.write("- **Recovered sessions:** rows with substrate-twin filename `*-recovered-from-rollup-*.md` were materialized in Phase 2 from the rollup; they were absent from the original substrate due to same-second filename collisions.\n")
        fh.write("- **First prompt:** truncated to 80 chars and stripped of pipe/backtick chars for table safety. See substrate file or rollup line range for full content.\n")

    print(f"sessions indexed: {len(rollup_rows)}")
    print(f"in substrate: {in_substrate}, rollup-only: {rollup_only}")
    print(f"output: {OUT}")


if __name__ == "__main__":
    main()
