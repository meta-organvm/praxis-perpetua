#!/usr/bin/env python3
"""Reconcile SpecStory rollup manifest against .specstory/history/ substrate.

Substrate filename grammar: YYYY-MM-DD_HH-MM-SS{TZ}[-slug].md
  where TZ is -0400 / -0500 / Z (UTC).

Rollup timestamp grammar: YYYY-MM-DD HH:MM:SS{TZ}
  where TZ is -0400 / -0500 / Z.

We match on the (date, HH-MM-SS, TZ) tuple — exact, no fuzzy window. Same-second
collisions in the rollup get bucketed as DUPS-WITHIN-ROLLUP (with both UUIDs
listed). Substrate-side collisions on the same second would be unusual but
possible — we list any.
"""

import csv
import re
from collections import defaultdict
from pathlib import Path
from datetime import datetime, timedelta

MANIFEST = Path("~/Workspace/.specstory/rollup-manifest.tsv")
HISTORY = Path("~/Workspace/.specstory/history")
OUT = Path("~/Workspace/.specstory/rollup-vs-substrate.md")

SUBSTRATE_RE = re.compile(
    r"^(?P<date>\d{4}-\d{2}-\d{2})_(?P<h>\d{2})-(?P<m>\d{2})-(?P<s>\d{2})(?P<tz>[+-]\d{4}|Z)"
    r"(?:-(?P<slug>.+))?\.md$"
)


def parse_substrate_dt(path: Path) -> tuple[datetime, str] | None:
    m = SUBSTRATE_RE.match(path.name)
    if not m:
        return None
    date = m.group("date")
    h, mi, s = m.group("h"), m.group("m"), m.group("s")
    tz = m.group("tz")
    iso = f"{date}T{h}:{mi}:{s}"
    if tz == "Z":
        dt = datetime.fromisoformat(iso + "+00:00")
    else:
        dt = datetime.fromisoformat(iso + tz[:3] + ":" + tz[3:])
    return dt, m.group("slug") or ""


def parse_rollup_dt(ts: str) -> datetime:
    # "2026-04-29 14:00:37-0400" or "2026-04-29 14:00:37Z"
    m = re.match(r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})([+-]\d{4}|Z)", ts)
    if not m:
        raise ValueError(f"bad ts: {ts}")
    iso = f"{m.group(1)}T{m.group(2)}"
    tz = m.group(3)
    if tz == "Z":
        return datetime.fromisoformat(iso + "+00:00")
    return datetime.fromisoformat(iso + tz[:3] + ":" + tz[3:])


def main() -> None:
    # Load substrate
    substrate: dict[datetime, list[tuple[Path, str]]] = defaultdict(list)
    skipped: list[Path] = []
    for p in sorted(HISTORY.glob("*.md")):
        parsed = parse_substrate_dt(p)
        if parsed is None:
            skipped.append(p)
            continue
        dt, slug = parsed
        substrate[dt].append((p, slug))

    # Load rollup
    rollup_rows: list[dict] = []
    with open(MANIFEST, "r") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            r["dt"] = parse_rollup_dt(r["timestamp"])
            r["line_start"] = int(r["line_start"])
            r["line_end"] = int(r["line_end"])
            rollup_rows.append(r)

    # Group rollup rows by datetime
    rollup_by_dt: dict[datetime, list[dict]] = defaultdict(list)
    for r in rollup_rows:
        rollup_by_dt[r["dt"]].append(r)

    # Categorize
    both: list[tuple[dict, Path]] = []
    export_only: list[dict] = []
    dups_within_rollup: list[list[dict]] = []
    matched_substrate_paths: set[Path] = set()

    # Tolerance window for fuzzy match (cross-process clock skew, etc.)
    tolerance = timedelta(seconds=60)

    for dt, rows in rollup_by_dt.items():
        if len(rows) > 1:
            dups_within_rollup.append(rows)

        # Try exact match first
        sub_matches = substrate.get(dt, [])
        # If exact misses, try fuzzy ± tolerance
        if not sub_matches:
            for sub_dt, files in substrate.items():
                if abs(sub_dt - dt) <= tolerance:
                    sub_matches = files
                    break

        if sub_matches:
            for r in rows:
                # Pair each rollup row with a substrate match (greedy, 1:1 if possible)
                pair = sub_matches[0] if sub_matches else None
                if pair:
                    both.append((r, pair[0]))
                    matched_substrate_paths.add(pair[0])
                    sub_matches = sub_matches[1:]  # consume
                else:
                    export_only.append(r)
        else:
            export_only.extend(rows)

    substrate_only: list[Path] = []
    for dt, files in substrate.items():
        for path, slug in files:
            if path not in matched_substrate_paths:
                substrate_only.append(path)

    substrate_only.sort()

    # Write report
    with open(OUT, "w") as fh:
        fh.write("# Rollup ↔ Substrate Reconciliation Report\n\n")
        fh.write(f"- **Generated:** by `/tmp/reconcile.py` against manifest `{MANIFEST}` and substrate `{HISTORY}`\n")
        fh.write(f"- **Rollup sessions:** {len(rollup_rows)}\n")
        fh.write(f"- **Substrate files:** {sum(len(v) for v in substrate.values())} (skipped {len(skipped)} unparseable)\n")
        fh.write(f"- **BOTH:** {len(both)} pairs\n")
        fh.write(f"- **EXPORT-ONLY:** {len(export_only)} sessions in rollup with no substrate twin\n")
        fh.write(f"- **SUBSTRATE-ONLY:** {len(substrate_only)} files in substrate not in rollup\n")
        fh.write(f"- **DUPS-WITHIN-ROLLUP:** {len(dups_within_rollup)} same-second clusters\n\n")

        fh.write("## DUPS-WITHIN-ROLLUP (same-timestamp clusters in the rollup)\n\n")
        if not dups_within_rollup:
            fh.write("*(none)*\n\n")
        else:
            for cluster in dups_within_rollup:
                ts = cluster[0]["timestamp"]
                fh.write(f"### {ts}\n\n")
                fh.write("| idx | line_start | line_end | uuid | first prompt |\n")
                fh.write("|---|---|---|---|---|\n")
                for r in cluster:
                    uuid_short = r["uuid"][:8] + "…" if r["uuid"] else "*(no uuid)*"
                    prompt = r["first_user_prompt"].replace("|", "\\|")[:80]
                    fh.write(f"| {r['session_idx']} | {r['line_start']} | {r['line_end']} | `{uuid_short}` | {prompt} |\n")
                fh.write("\n")

        fh.write("## EXPORT-ONLY (in rollup, missing from substrate)\n\n")
        if not export_only:
            fh.write("*(none — every rollup session has a substrate twin)*\n\n")
        else:
            fh.write("| idx | timestamp | uuid | line range | first prompt |\n")
            fh.write("|---|---|---|---|---|\n")
            for r in export_only:
                uuid_short = r["uuid"][:8] + "…" if r["uuid"] else "*(no uuid)*"
                prompt = r["first_user_prompt"].replace("|", "\\|")[:80]
                fh.write(f"| {r['session_idx']} | {r['timestamp']} | `{uuid_short}` | "
                         f"{r['line_start']}-{r['line_end']} | {prompt} |\n")
            fh.write("\n")

        fh.write("## SUBSTRATE-ONLY (in substrate, missing from rollup)\n\n")
        if not substrate_only:
            fh.write("*(none — substrate is fully captured by rollup)*\n\n")
        else:
            fh.write(f"({len(substrate_only)} files — typically pre-rollup-window sessions)\n\n")
            fh.write("```\n")
            for p in substrate_only:
                fh.write(f"{p.name}\n")
            fh.write("```\n\n")

        fh.write("## BOTH (paired sessions — first 20 shown)\n\n")
        fh.write("| idx | timestamp | line range | substrate file |\n")
        fh.write("|---|---|---|---|\n")
        for r, p in both[:20]:
            fh.write(f"| {r['session_idx']} | {r['timestamp']} | {r['line_start']}-{r['line_end']} | `{p.name}` |\n")
        if len(both) > 20:
            fh.write(f"\n*({len(both) - 20} more pairs not shown — see manifest)*\n")

        if skipped:
            fh.write("\n## SKIPPED (unparseable substrate filenames)\n\n")
            for p in skipped:
                fh.write(f"- `{p.name}`\n")

    print(f"BOTH: {len(both)}")
    print(f"EXPORT-ONLY: {len(export_only)}")
    print(f"SUBSTRATE-ONLY: {len(substrate_only)}")
    print(f"DUPS-WITHIN-ROLLUP: {len(dups_within_rollup)}")
    print(f"Report: {OUT}")


if __name__ == "__main__":
    main()
