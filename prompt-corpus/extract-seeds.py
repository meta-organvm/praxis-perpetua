#!/usr/bin/env python3
"""Phase 4: Seed extraction — identify prompts carrying durable design intent.

Reads sequenced-prompts.jsonl, classifies each prompt into seed types based on
the user's Design Grammar (DEFINE→TRANSFORM) and Prompt Sequence Protocol
(SEED→HANDOFF).

Seed types:
  - design_directive: names things, defines structures, declares architectures
  - theoretical_grounding: invokes concepts, theories, formal frameworks
  - consolidation_order: directs merging, collapsing, absorbing, reducing
  - naming_act: creates names (double-hyphen, organ names, function names)
  - rejection_correction: says "no, not that" — defines boundaries
  - strategic_vision: declares goals, outcomes, end-states
  - process_definition: defines workflows, protocols, sequences

Outputs seeds.jsonl and SEED-CATALOGUE.md
"""

import json
import re
from pathlib import Path
from collections import defaultdict


# --- Seed detection patterns ---

DESIGN_DIRECTIVE_PATTERNS = [
    re.compile(r"\b(?:define|declare|architect|structure|design|schema|format)\b", re.I),
    re.compile(r"\b(?:should be|must be|needs to be|has to be)\b.*\b(?:flat|hierarchical|recursive|modular)\b", re.I),
    re.compile(r"\b(?:formation|genome|contract|interface|protocol|specification)\b", re.I),
    re.compile(r"\b(?:create|build|implement|construct)\b.*\b(?:system|framework|engine|pipeline|architecture)\b", re.I),
]

THEORETICAL_PATTERNS = [
    re.compile(r"\b(?:telos|pragma|praxis|receptio|polis)\b", re.I),
    re.compile(r"\b(?:dispersio|palingenesis|portal|asymptot|phase.?boundary)\b", re.I),
    re.compile(r"\b(?:ontolog|epistem|axiomat|theorem|proof|formal|invariant)\b", re.I),
    re.compile(r"\b(?:gravitas|culturalis|trivium|dialectica|cosmogon)\b", re.I),
    re.compile(r"\b(?:biological|organism|organ|circulatory|digestive|nervous|immune|skeletal)\b", re.I),
    re.compile(r"\b(?:alchemy|transmut|distill|crucible|furnace)\b", re.I),
    re.compile(r"\b(?:SPEC-\d+|SOP-|IRF-|INST-)\b"),
]

CONSOLIDATION_PATTERNS = [
    re.compile(r"\b(?:consolidat|merg|collaps|absorb|fus[ei]|reduc|flatten|simplif)\b", re.I),
    re.compile(r"\b(?:redundan|duplicat|overlap|repetit)\b", re.I),
    re.compile(r"\b(?:kill|remove|delete|eliminate|dissolve|deprecat)\b.*\b(?:script|module|layer|file|function)\b", re.I),
    re.compile(r"\b(?:unif[yi]|single.?source|one.?(?:system|store|registry|loader))\b", re.I),
]

NAMING_PATTERNS = [
    re.compile(r"(?:call(?:ed)?|name[ds]?|titled?|label(?:ed)?)\s+[\"'`]?[\w][\w-]+--[\w-]+", re.I),
    re.compile(r"\b(?:rename|rebrand|rechrist[ei]n)\b", re.I),
    re.compile(r"[A-Z][a-z]+(?:[A-Z][a-z]+)+"),  # CamelCase naming
    re.compile(r"\$[A-Z_]+\b"),  # $VARIABLE notation (Design Grammar D3)
    re.compile(r"--[a-z]+", re.I),  # double-hyphen naming convention
]

REJECTION_PATTERNS = [
    re.compile(r"^(?:no[,.]?\s|not that|don'?t|stop|wrong|that'?s not)", re.I),
    re.compile(r"\b(?:instead|rather|actually|correction)\b", re.I),
    re.compile(r"\b(?:never|always)\b.*\b(?:do|use|create|make|call|name)\b", re.I),
]

STRATEGIC_PATTERNS = [
    re.compile(r"\b(?:vision|mission|goal|endgame|end.?state|north.?star)\b", re.I),
    re.compile(r"\b(?:revenue|monetiz|commercial|business|market)\b", re.I),
    re.compile(r"\b(?:scale|growth|expansion|maturity|graduation)\b", re.I),
    re.compile(r"\b(?:pixar|studio|enterprise|production)\b", re.I),
]

PROCESS_PATTERNS = [
    re.compile(r"\b(?:workflow|pipeline|protocol|procedure|sequence|phase|stage)\b", re.I),
    re.compile(r"\b(?:SOP|sop|standard.?operating)\b"),
    re.compile(r"\b(?:step\s*\d|phase\s*\d|stage\s*\d)\b", re.I),
    re.compile(r"\b(?:first|then|next|after|before|finally)\b.*\b(?:do|run|execute|create|build)\b", re.I),
]


def classify_seed(text: str) -> list[str]:
    """Return list of seed types this prompt matches. Empty = not a seed."""
    seed_types = []
    checks = [
        ("design_directive", DESIGN_DIRECTIVE_PATTERNS, 2),
        ("theoretical_grounding", THEORETICAL_PATTERNS, 1),
        ("consolidation_order", CONSOLIDATION_PATTERNS, 1),
        ("naming_act", NAMING_PATTERNS, 2),
        ("rejection_correction", REJECTION_PATTERNS, 1),
        ("strategic_vision", STRATEGIC_PATTERNS, 2),
        ("process_definition", PROCESS_PATTERNS, 2),
    ]
    for seed_type, patterns, threshold in checks:
        matches = sum(1 for p in patterns if p.search(text))
        if matches >= threshold:
            seed_types.append(seed_type)
    return seed_types


def main():
    corpus_dir = Path(__file__).parent
    input_path = corpus_dir / "sequenced-prompts.jsonl"
    seeds_path = corpus_dir / "seeds.jsonl"
    catalogue_path = corpus_dir / "SEED-CATALOGUE.md"

    seeds = []
    total = 0
    type_counts = defaultdict(int)
    organ_seed_counts = defaultdict(int)

    with open(input_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += 1
            entry = json.loads(line)
            text = entry.get("content", {}).get("text", "")

            # Skip very short prompts (< 15 chars) — unlikely to be seeds
            if len(text) < 15:
                continue

            seed_types = classify_seed(text)
            if seed_types:
                entry["seed_types"] = seed_types
                seeds.append(entry)
                for st in seed_types:
                    type_counts[st] += 1
                organ_seed_counts[entry.get("organ", "?")] += 1

    # Write seeds JSONL
    with open(seeds_path, "w") as f:
        for entry in seeds:
            f.write(json.dumps(entry) + "\n")

    # Write human-readable catalogue
    with open(catalogue_path, "w") as f:
        f.write("# Seed Catalogue — Universal Prompt Archaeology\n\n")
        f.write(f"**Generated:** {__import__('datetime').datetime.now().isoformat()[:19]}Z\n")
        f.write(f"**Total prompts scanned:** {total}\n")
        f.write(f"**Seeds identified:** {len(seeds)} ({len(seeds)*100//max(total,1)}%)\n\n")

        f.write("## Seed Type Distribution\n\n")
        f.write("| Type | Count | % of Seeds |\n")
        f.write("|------|-------|------------|\n")
        for st, count in sorted(type_counts.items(), key=lambda x: -x[1]):
            pct = count * 100 // max(len(seeds), 1)
            f.write(f"| {st} | {count} | {pct}% |\n")

        f.write("\n## Seeds by Organ\n\n")
        f.write("| Organ | Seeds | % |\n")
        f.write("|-------|-------|---|\n")
        for organ, count in sorted(organ_seed_counts.items(), key=lambda x: -x[1]):
            pct = count * 100 // max(len(seeds), 1)
            f.write(f"| {organ} | {count} | {pct}% |\n")

        # Top seeds by type
        for seed_type in sorted(type_counts.keys()):
            f.write(f"\n## {seed_type.replace('_', ' ').title()}\n\n")
            typed_seeds = [s for s in seeds if seed_type in s.get("seed_types", [])]
            # Show top 10 by length (longer = more substantive)
            typed_seeds.sort(key=lambda s: -s.get("content", {}).get("char_count", 0))
            for s in typed_seeds[:10]:
                text = s.get("content", {}).get("text", "")[:300]
                agent = s.get("source", {}).get("agent", "?")
                organ = s.get("organ", "?")
                ts = s.get("source", {}).get("timestamp", "")[:10]
                f.write(f"- **[{agent}/{organ}]** ({ts}) {text}...\n\n")

    print(f"Seed extraction complete:")
    print(f"  Total prompts: {total}")
    print(f"  Seeds identified: {len(seeds)} ({len(seeds)*100//max(total,1)}%)")
    print(f"\n  Type distribution:")
    for st, count in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"    {st}: {count}")
    print(f"\n  Written to: {seeds_path}")
    print(f"  Catalogue: {catalogue_path}")


if __name__ == "__main__":
    main()
