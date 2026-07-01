#!/usr/bin/env python3
"""Track B: Reverse-chronological prompt chain — from NOW toward the past.

Walks the sequenced corpus backward in time, reconstructing the actual sequence
of prompts as fired. Groups rapid-fire sequences (< 5 min gap) into bursts.
Surfaces prompts that were "lost to chaos" — fired in quick succession without
adequate response processing time.

Outputs:
  reverse-chain.jsonl — prompts in reverse chronological order with burst grouping
  REVERSE-CHAIN-REPORT.md — human-readable chain showing recoverable intent
"""

import json
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict


def parse_ts(ts_str: str) -> datetime | None:
    """Parse ISO timestamp."""
    if not ts_str:
        return None
    for fmt in ("%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S%z",
                "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S"):
        try:
            return datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
        except ValueError:
            continue
    return None


def main():
    corpus_dir = Path(__file__).parent
    input_path = corpus_dir / "sequenced-prompts.jsonl"
    output_path = corpus_dir / "reverse-chain.jsonl"
    report_path = corpus_dir / "REVERSE-CHAIN-REPORT.md"

    # Load all prompts
    prompts = []
    with open(input_path) as f:
        for line in f:
            if line.strip():
                prompts.append(json.loads(line))

    # Filter to those with timestamps and sort descending (most recent first)
    timestamped = []
    for p in prompts:
        ts_str = p.get("source", {}).get("timestamp", "")
        ts = parse_ts(ts_str)
        if ts:
            p["_ts"] = ts.isoformat()
            timestamped.append((ts, p))

    timestamped.sort(key=lambda x: x[0], reverse=True)

    # Group into bursts (< 5 min gap = same burst)
    BURST_GAP = timedelta(minutes=5)
    bursts = []
    current_burst = []

    for i, (ts, prompt) in enumerate(timestamped):
        if not current_burst:
            current_burst.append((ts, prompt))
        else:
            prev_ts = current_burst[-1][0]
            gap = prev_ts - ts  # positive because we're going backward
            if gap <= BURST_GAP:
                current_burst.append((ts, prompt))
            else:
                bursts.append(current_burst)
                current_burst = [(ts, prompt)]

    if current_burst:
        bursts.append(current_burst)

    # Classify bursts
    rapid_fire = [b for b in bursts if len(b) >= 3]  # 3+ prompts in < 5 min = chaos zone
    singles = [b for b in bursts if len(b) == 1]
    normal = [b for b in bursts if 1 < len(b) < 3]

    # Write reverse chain JSONL
    chain_entries = []
    for burst_idx, burst in enumerate(bursts):
        for ts, prompt in burst:
            entry = dict(prompt)
            entry["burst_id"] = burst_idx
            entry["burst_size"] = len(burst)
            entry["is_rapid_fire"] = len(burst) >= 3
            chain_entries.append(entry)

    with open(output_path, "w") as f:
        for entry in chain_entries:
            # Remove datetime objects for serialization
            entry.pop("_ts", None)
            f.write(json.dumps(entry) + "\n")

    # Write report
    with open(report_path, "w") as f:
        f.write("# Track B: Reverse-Chronological Prompt Chain\n\n")
        f.write(f"**Generated:** {__import__('datetime').datetime.now().isoformat()[:19]}Z\n")
        f.write(f"**Total timestamped prompts:** {len(timestamped)}\n")
        f.write(f"**Total bursts:** {len(bursts)}\n")
        f.write(f"**Rapid-fire bursts (3+ in <5min):** {len(rapid_fire)}\n")
        f.write(f"**Prompts in rapid-fire zones:** {sum(len(b) for b in rapid_fire)}\n\n")

        f.write("## Burst Statistics\n\n")
        f.write(f"| Type | Count | Prompts |\n")
        f.write(f"|------|-------|--------|\n")
        f.write(f"| Single | {len(singles)} | {len(singles)} |\n")
        f.write(f"| Normal (2) | {len(normal)} | {sum(len(b) for b in normal)} |\n")
        f.write(f"| Rapid-fire (3+) | {len(rapid_fire)} | {sum(len(b) for b in rapid_fire)} |\n")

        # Most recent 30 bursts — the NOW→PAST chain
        f.write("\n## Recent Chain (most recent first)\n\n")
        for burst_idx, burst in enumerate(bursts[:30]):
            first_ts = burst[0][0].strftime("%Y-%m-%d %H:%M")
            last_ts = burst[-1][0].strftime("%H:%M") if len(burst) > 1 else ""
            organ = burst[0][1].get("organ", "?")
            agent = burst[0][1].get("source", {}).get("agent", "?")
            slug = burst[0][1].get("source", {}).get("project_slug", "?")

            marker = "🔥" if len(burst) >= 3 else "→"
            f.write(f"### Burst {burst_idx} {marker} [{agent}/{organ}] {first_ts}")
            if last_ts:
                f.write(f"–{last_ts}")
            f.write(f" ({slug}, {len(burst)} prompts)\n\n")

            for ts, prompt in burst:
                text = prompt.get("content", {}).get("text", "")[:300].replace("\n", " ")
                seed_types = prompt.get("seed_types", [])
                seed_tag = f" **[SEED: {', '.join(seed_types)}]**" if seed_types else ""
                ptype = prompt.get("classification", {}).get("prompt_type", "")
                f.write(f"- `{ts.strftime('%H:%M:%S')}` ({ptype}){seed_tag} {text}\n\n")

        # Rapid-fire zones — these are the "lost to chaos" candidates
        f.write("\n---\n\n## Rapid-Fire Zones (most likely lost prompts)\n\n")
        f.write("These are sequences of 3+ prompts fired within 5 minutes — ")
        f.write("high probability of intent that didn't get fully processed.\n\n")

        for burst in rapid_fire[:20]:
            first_ts = burst[0][0].strftime("%Y-%m-%d %H:%M")
            organ = burst[0][1].get("organ", "?")
            slug = burst[0][1].get("source", {}).get("project_slug", "?")
            f.write(f"### 🔥 {first_ts} [{organ}/{slug}] — {len(burst)} rapid prompts\n\n")
            for ts, prompt in burst:
                text = prompt.get("content", {}).get("text", "")[:400].replace("\n", " ")
                f.write(f"- `{ts.strftime('%H:%M:%S')}` {text}\n\n")

    print(f"Track B complete:")
    print(f"  Timestamped prompts: {len(timestamped)}")
    print(f"  Bursts: {len(bursts)}")
    print(f"  Rapid-fire bursts: {len(rapid_fire)} ({sum(len(b) for b in rapid_fire)} prompts)")
    print(f"  Written to: {output_path}")
    print(f"  Report: {report_path}")


if __name__ == "__main__":
    main()
