#!/usr/bin/env python3
"""Merge, deduplicate, and sequence the full prompt corpus.

Reads:
  annotated-prompts.jsonl   (from organvm prompts narrate)
  supplementary-prompts.jsonl (from ingest-supplementary.py)

Outputs:
  sequenced-prompts.jsonl   (unified, deduped, timestamp-sorted)

Deduplication: exact text match within a 60-second window.
"""

import json
import sys
from pathlib import Path


CORPUS_DIR = Path(__file__).parent
DEDUP_WINDOW_SECONDS = 60


def parse_timestamp(ts: str) -> float:
    """Convert ISO timestamp to epoch seconds for sorting. Returns 0 for empty."""
    if not ts:
        return 0.0
    # Handle various formats
    ts = ts.replace("Z", "+00:00")
    try:
        from datetime import datetime, timezone
        # Try ISO format
        dt = datetime.fromisoformat(ts)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.timestamp()
    except (ValueError, TypeError):
        return 0.0


def load_jsonl(path: Path) -> list[dict]:
    records = []
    if not path.exists():
        print(f"  Not found: {path}")
        return records
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    print(f"  Loaded {len(records)} from {path.name}")
    return records


def get_text(record: dict) -> str:
    """Extract comparable text from a record."""
    # Primary sources use raw_text, supplementary uses content.text
    return record.get("raw_text", "") or record.get("content", {}).get("text", "")


def deduplicate(records: list[dict]) -> list[dict]:
    """Remove exact-text duplicates within a 60-second window."""
    # Sort by timestamp first
    records.sort(key=lambda r: parse_timestamp(r.get("source", {}).get("timestamp", "")))

    seen: dict[str, float] = {}  # text hash -> last seen timestamp
    deduped = []
    removed = 0

    for r in records:
        text = get_text(r).strip()
        if not text:
            continue

        # Normalize for comparison (collapse whitespace)
        normalized = " ".join(text.split())
        ts = parse_timestamp(r.get("source", {}).get("timestamp", ""))

        if normalized in seen:
            last_ts = seen[normalized]
            if ts > 0 and last_ts > 0 and abs(ts - last_ts) < DEDUP_WINDOW_SECONDS:
                removed += 1
                continue

        seen[normalized] = ts
        deduped.append(r)

    print(f"  Deduplication: {removed} duplicates removed")
    return deduped


def main():
    print("Loading sources...")
    primary = load_jsonl(CORPUS_DIR / "annotated-prompts.jsonl")
    supplementary = load_jsonl(CORPUS_DIR / "supplementary-prompts.jsonl")

    # Merge
    all_records = primary + supplementary
    print(f"\nMerged: {len(all_records)} total records")

    # Deduplicate
    print("\nDeduplicating...")
    deduped = deduplicate(all_records)
    print(f"After dedup: {len(deduped)} records")

    # Sort by timestamp (already done in deduplicate, but ensure)
    deduped.sort(key=lambda r: parse_timestamp(r.get("source", {}).get("timestamp", "")))

    # Write sequenced output
    output_path = CORPUS_DIR / "sequenced-prompts.jsonl"
    with open(output_path, "w") as f:
        for r in deduped:
            f.write(json.dumps(r) + "\n")

    # Stats
    agents = {}
    for r in deduped:
        agent = r.get("source", {}).get("agent", "unknown")
        agents[agent] = agents.get(agent, 0) + 1

    print(f"\nSequenced corpus written to: {output_path}")
    print(f"Total prompts: {len(deduped)}")
    print(f"\nAgent distribution:")
    for agent, count in sorted(agents.items(), key=lambda x: -x[1]):
        print(f"  {agent}: {count}")

    # Timestamp range
    timestamps = [
        parse_timestamp(r.get("source", {}).get("timestamp", ""))
        for r in deduped if parse_timestamp(r.get("source", {}).get("timestamp", "")) > 0
    ]
    if timestamps:
        from datetime import datetime, timezone
        earliest = datetime.fromtimestamp(min(timestamps), tz=timezone.utc)
        latest = datetime.fromtimestamp(max(timestamps), tz=timezone.utc)
        print(f"\nTemporal range: {earliest.date()} to {latest.date()}")
        print(f"Span: {(latest - earliest).days} days")


if __name__ == "__main__":
    main()
