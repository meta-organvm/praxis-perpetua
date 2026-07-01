#!/usr/bin/env python3
"""Phase 3: Merge all prompt sources, sort chronologically, deduplicate.

Reads:
  annotated-prompts.jsonl   (engine output, 5088 prompts)
  supplementary-prompts.jsonl (chatgpt/export/specstory, 464 prompts)

Produces:
  sequenced-prompts.jsonl   (unified timeline, deduped)
"""

import json
import hashlib
from pathlib import Path
from collections import defaultdict


def dedup_key(entry: dict) -> str:
    """Fingerprint by text content (first 500 chars) for deduplication."""
    text = entry.get("content", {}).get("text", "")[:500]
    return hashlib.sha256(text.encode()).hexdigest()[:16]


def derive_organ(project_slug: str) -> str:
    """Map project_slug to organ using known prefixes."""
    slug = project_slug.lower()
    organ_map = {
        "meta-organvm": "META",
        "organvm-i-": "ORGAN-I",
        "organvm-ii-": "ORGAN-II",
        "organvm-iii-": "ORGAN-III",
        "organvm-iv-": "ORGAN-IV",
        "organvm-v-": "ORGAN-V",
        "organvm-vi-": "ORGAN-VI",
        "organvm-vii-": "ORGAN-VII",
        "4444j99": "LIMINAL",
        "domus": "LIMINAL",
        "a-organvm": "SEED",
        "system-system": "AXIOM",
        "sovereign": "SEED",
    }
    for prefix, organ in organ_map.items():
        if prefix in slug:
            return organ
    return "UNCLASSIFIED"


def main():
    corpus_dir = Path(__file__).parent
    engine_path = corpus_dir / "annotated-prompts.jsonl"
    supp_path = corpus_dir / "supplementary-prompts.jsonl"
    output_path = corpus_dir / "sequenced-prompts.jsonl"

    all_prompts = []
    seen_keys = set()
    dupes = 0

    # Load engine prompts
    if engine_path.exists():
        with open(engine_path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                entry = json.loads(line)
                key = dedup_key(entry)
                if key in seen_keys:
                    dupes += 1
                    continue
                seen_keys.add(key)
                entry["organ"] = derive_organ(
                    entry.get("source", {}).get("project_slug", "")
                )
                all_prompts.append(entry)

    engine_count = len(all_prompts)

    # Load supplementary prompts
    if supp_path.exists():
        with open(supp_path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                entry = json.loads(line)
                key = dedup_key(entry)
                if key in seen_keys:
                    dupes += 1
                    continue
                seen_keys.add(key)
                entry["organ"] = derive_organ(
                    entry.get("source", {}).get("project_slug", "")
                )
                all_prompts.append(entry)

    supp_added = len(all_prompts) - engine_count

    # Sort by timestamp (entries without timestamp go to end)
    def sort_key(entry):
        ts = entry.get("source", {}).get("timestamp", "")
        return ts if ts else "9999"

    all_prompts.sort(key=sort_key)

    # Compute organ distribution
    organ_dist = defaultdict(int)
    agent_dist = defaultdict(int)
    for p in all_prompts:
        organ_dist[p.get("organ", "?")] += 1
        agent_dist[p.get("source", {}).get("agent", "?")] += 1

    # Write
    with open(output_path, "w") as f:
        for entry in all_prompts:
            f.write(json.dumps(entry) + "\n")

    print(f"Sequencing complete:")
    print(f"  Engine prompts: {engine_count}")
    print(f"  Supplementary added: {supp_added}")
    print(f"  Duplicates removed: {dupes}")
    print(f"  Total sequenced: {len(all_prompts)}")
    print(f"\nOrgan distribution:")
    for organ, count in sorted(organ_dist.items(), key=lambda x: -x[1]):
        print(f"  {organ}: {count}")
    print(f"\nAgent distribution:")
    for agent, count in sorted(agent_dist.items(), key=lambda x: -x[1]):
        print(f"  {agent}: {count}")
    print(f"\nWritten to: {output_path}")


if __name__ == "__main__":
    main()
