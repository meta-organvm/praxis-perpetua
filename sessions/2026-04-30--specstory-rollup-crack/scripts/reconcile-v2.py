#!/usr/bin/env python3
"""Rollup ↔ substrate reconciliation, v2 — UUID-based matching.

Builds:
  1. A richer manifest (rollup-manifest.tsv) with an `agent` column.
  2. A reconciliation report (rollup-vs-substrate.md) using UUID as the
     universal join key. Substrate files without a UUID (rare/parse failures)
     fall back to slug+date matching.

Substrate doubling: SpecStory CLI writes the same session under two filenames
(local-TZ and UTC) when local_time_zone is toggled. We detect this by grouping
substrate files by UUID and emitting collapsed-substrate counts.
"""

import re
import csv
from collections import defaultdict
from pathlib import Path

ROLLUP = Path("~/Workspace/SpecStory, Markdown v2.md")
HISTORY = Path("~/Workspace/.specstory/history")
MANIFEST = Path("~/Workspace/.specstory/rollup-manifest.tsv")
REPORT = Path("~/Workspace/.specstory/rollup-vs-substrate.md")

HEADER_RE = re.compile(r"^# (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}(?:[+-]\d{4}|Z))$")
# Matches Claude Code / Codex CLI / Gemini CLI / Cursor / Droid session markers.
SESSION_RE = re.compile(
    r"^<!-- (?P<agent>[A-Za-z][A-Za-z ]*?) Session (?P<uuid>[0-9a-f-]+) \(.+\) -->$"
)
USER_RE = re.compile(r"^_\*\*User \(.+\)\*\*_$")


def build_rollup_manifest() -> list[dict]:
    sessions: list[dict] = []
    current: dict | None = None
    looking_for_marker = False
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
                    "agent": "",
                    "uuid": "",
                    "first_user_prompt": "",
                }
                looking_for_marker = True
                looking_for_user_marker = True
                capturing_first_prompt = False
                continue

            if current is None:
                continue

            if looking_for_marker:
                ms = SESSION_RE.match(stripped)
                if ms:
                    current["agent"] = ms.group("agent").strip()
                    current["uuid"] = ms.group("uuid")
                    looking_for_marker = False
                    continue
                if stripped and not stripped.startswith("<!--"):
                    looking_for_marker = False

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

    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST, "w", encoding="utf-8") as fh:
        fh.write("session_idx\tline_start\tline_end\ttimestamp\tagent\tuuid\tfirst_user_prompt\n")
        for s in sessions:
            prompt = s["first_user_prompt"].replace("\t", " ").replace("\r", " ")
            fh.write(
                f"{s['session_idx']}\t{s['line_start']}\t{s['line_end']}\t"
                f"{s['timestamp']}\t{s['agent']}\t{s['uuid']}\t{prompt}\n"
            )
    return sessions


def index_substrate() -> tuple[dict[str, list[Path]], list[Path]]:
    """Return (uuid -> list of substrate paths, list of files with no UUID)."""
    by_uuid: dict[str, list[Path]] = defaultdict(list)
    no_uuid: list[Path] = []
    for p in sorted(HISTORY.glob("*.md")):
        uuid_found = ""
        with open(p, "r", encoding="utf-8", errors="replace") as fh:
            for i, line in enumerate(fh):
                if i > 12:
                    break
                stripped = line.rstrip("\n")
                ms = SESSION_RE.match(stripped)
                if ms:
                    uuid_found = ms.group("uuid")
                    break
        if uuid_found:
            by_uuid[uuid_found].append(p)
        else:
            no_uuid.append(p)
    return by_uuid, no_uuid


def write_report(rollup: list[dict], by_uuid: dict[str, list[Path]], no_uuid_files: list[Path]) -> None:
    rollup_by_uuid: dict[str, list[dict]] = defaultdict(list)
    rollup_without_uuid: list[dict] = []
    for r in rollup:
        if r["uuid"]:
            rollup_by_uuid[r["uuid"]].append(r)
        else:
            rollup_without_uuid.append(r)

    matched_uuids = set(rollup_by_uuid.keys()) & set(by_uuid.keys())
    export_only_uuids = set(rollup_by_uuid.keys()) - set(by_uuid.keys())
    substrate_only_uuids = set(by_uuid.keys()) - set(rollup_by_uuid.keys())

    # Same-second clusters (independent of UUID matching)
    rollup_by_ts: dict[str, list[dict]] = defaultdict(list)
    for r in rollup:
        rollup_by_ts[r["timestamp"]].append(r)
    dup_clusters = [v for v in rollup_by_ts.values() if len(v) > 1]

    # Substrate-only files that have no rollup twin
    substrate_only_files: list[Path] = []
    for u in sorted(substrate_only_uuids):
        substrate_only_files.extend(by_uuid[u])
    substrate_only_files.extend(no_uuid_files)
    substrate_only_files.sort()

    # Total substrate count
    total_substrate = sum(len(v) for v in by_uuid.values()) + len(no_uuid_files)
    unique_substrate = len(by_uuid) + len(no_uuid_files)

    with open(REPORT, "w", encoding="utf-8") as fh:
        fh.write("# Rollup ↔ Substrate Reconciliation Report (v2 — UUID-based)\n\n")
        fh.write(f"- **Manifest:** `{MANIFEST}`\n")
        fh.write(f"- **Substrate root:** `{HISTORY}`\n\n")

        fh.write("## Counts\n\n")
        fh.write(f"- Rollup sessions: **{len(rollup)}** (with UUID: {sum(1 for r in rollup if r['uuid'])}, without: {len(rollup_without_uuid)})\n")
        fh.write(f"- Substrate files: **{total_substrate}** (unique UUIDs: {len(by_uuid)}, no-UUID parsed: {len(no_uuid_files)})\n")
        fh.write(f"- Substrate doubling factor: **{total_substrate / max(unique_substrate, 1):.2f}×** (local-TZ + UTC dual-write)\n")
        fh.write(f"- BOTH (UUID matched): **{len(matched_uuids)}**\n")
        fh.write(f"- EXPORT-ONLY (rollup UUID has no substrate file): **{len(export_only_uuids)}**\n")
        fh.write(f"- SUBSTRATE-ONLY (substrate UUID has no rollup session): **{len(substrate_only_uuids) + len(no_uuid_files)}** ({len(substrate_only_uuids)} by UUID + {len(no_uuid_files)} no-UUID parsed)\n")
        fh.write(f"- Same-timestamp clusters in rollup: **{len(dup_clusters)}**\n")
        fh.write(f"- Rollup sessions WITHOUT UUID (likely TUI/non-Claude): **{len(rollup_without_uuid)}**\n\n")

        # Agent breakdown
        agent_counts: dict[str, int] = defaultdict(int)
        for r in rollup:
            agent_counts[r["agent"] or "(none)"] += 1
        fh.write("## Rollup agent distribution\n\n")
        for a, c in sorted(agent_counts.items(), key=lambda x: -x[1]):
            fh.write(f"- **{a}**: {c}\n")
        fh.write("\n")

        fh.write("## Same-timestamp clusters in rollup\n\n")
        if not dup_clusters:
            fh.write("*(none)*\n\n")
        else:
            for cluster in dup_clusters:
                ts = cluster[0]["timestamp"]
                fh.write(f"### {ts}\n\n")
                fh.write("| idx | line_start | line_end | uuid | first prompt |\n|---|---|---|---|---|\n")
                for r in cluster:
                    uuid_short = r["uuid"][:8] + "…" if r["uuid"] else "*(none)*"
                    prompt = (r["first_user_prompt"] or "").replace("|", "\\|")[:80]
                    fh.write(f"| {r['session_idx']} | {r['line_start']} | {r['line_end']} | `{uuid_short}` | {prompt} |\n")
                fh.write("\n")

        fh.write(f"## EXPORT-ONLY ({len(export_only_uuids)} sessions only in rollup)\n\n")
        if not export_only_uuids:
            fh.write("*(none — every UUID-tagged rollup session has a substrate twin)*\n\n")
        else:
            fh.write("These sessions exist in the rollup but no substrate file with a matching UUID was found. Candidates for recovery to `.specstory/history/`.\n\n")
            fh.write("| idx | timestamp | agent | uuid | line range | first prompt |\n|---|---|---|---|---|---|\n")
            for u in sorted(export_only_uuids):
                for r in rollup_by_uuid[u]:
                    prompt = (r["first_user_prompt"] or "").replace("|", "\\|")[:80]
                    fh.write(f"| {r['session_idx']} | {r['timestamp']} | {r['agent']} | `{r['uuid'][:12]}…` | {r['line_start']}-{r['line_end']} | {prompt} |\n")
            fh.write("\n")

        fh.write(f"## ROLLUP WITHOUT UUID ({len(rollup_without_uuid)} sessions)\n\n")
        fh.write("These rollup sessions have no recognizable session marker. Cannot be UUID-matched; we'd fall back to slug+date matching but skip for now.\n\n")
        if rollup_without_uuid:
            fh.write("| idx | timestamp | line range | first prompt |\n|---|---|---|---|\n")
            for r in rollup_without_uuid:
                prompt = (r["first_user_prompt"] or "").replace("|", "\\|")[:80]
                fh.write(f"| {r['session_idx']} | {r['timestamp']} | {r['line_start']}-{r['line_end']} | {prompt} |\n")
            fh.write("\n")

        fh.write(f"## SUBSTRATE-ONLY ({len(substrate_only_files)} files)\n\n")
        fh.write(f"({len(substrate_only_uuids)} unique-UUID sessions + {len(no_uuid_files)} unparseable files)\n\n")
        fh.write("```\n")
        for p in substrate_only_files:
            fh.write(f"{p.name}\n")
        fh.write("```\n\n")

        fh.write(f"## BOTH ({len(matched_uuids)} UUID-matched pairs — first 30 shown)\n\n")
        fh.write("| idx | timestamp | agent | line range | substrate file(s) |\n|---|---|---|---|---|\n")
        shown = 0
        for u in sorted(matched_uuids):
            if shown >= 30:
                break
            for r in rollup_by_uuid[u]:
                files = ", ".join(f"`{p.name}`" for p in by_uuid[u])
                fh.write(f"| {r['session_idx']} | {r['timestamp']} | {r['agent']} | {r['line_start']}-{r['line_end']} | {files} |\n")
                shown += 1
                if shown >= 30:
                    break
        fh.write(f"\n*(plus {max(0, len(matched_uuids) - shown)} more pairs not shown)*\n")

    print(f"BOTH: {len(matched_uuids)}")
    print(f"EXPORT-ONLY UUIDs: {len(export_only_uuids)}")
    print(f"SUBSTRATE-ONLY UUIDs: {len(substrate_only_uuids)} (+ {len(no_uuid_files)} no-UUID files)")
    print(f"Rollup-without-UUID: {len(rollup_without_uuid)}")
    print(f"Same-second clusters: {len(dup_clusters)}")
    print(f"Manifest: {MANIFEST}")
    print(f"Report: {REPORT}")


def main() -> None:
    print("[1/3] Building rollup manifest…")
    rollup = build_rollup_manifest()
    print(f"      {len(rollup)} sessions captured")
    print("[2/3] Indexing substrate by UUID…")
    by_uuid, no_uuid = index_substrate()
    print(f"      {sum(len(v) for v in by_uuid.values())} files with UUID, {len(no_uuid)} without")
    print("[3/3] Writing report…")
    write_report(rollup, by_uuid, no_uuid)


if __name__ == "__main__":
    main()
