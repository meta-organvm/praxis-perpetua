# Prompt Corpus — Universal Prompt Archaeology

The primary source material for the ORGANVM system. Every user prompt across every session, every organ, every agent — extracted, sequenced, classified, and persisted.

**The code is derivative. The prompts are the seeds.**

## Latest Extraction: 2026-04-04 (re-run)

| Metric | Value |
|--------|-------|
| Sessions processed | 757 (Claude: ~713, Codex: 44) |
| Supplementary sources | 22 files (Clipboard/Paste.app: 833, ChatGPT-MD: 39, Claude-export: 29) |
| Raw prompts extracted | 6,013 |
| After deduplication | 5,703 |
| Seeds identified | 487 (prior extraction — see Phase 4 note) |
| Agents | 35 unique (claude, codex, chatgpt, claude-export, clipboard/[30+ apps]) |
| Date range | Nov 22 2025 – Apr 5 2026 (133 days) |

## Files

| File | Lines | Size | Purpose |
|------|-------|------|---------|
| `annotated-prompts.jsonl` | 5,112 | 55MB | Full engine extraction (Claude/Codex) |
| `supplementary-prompts.jsonl` | 901 | 1.7MB | Clipboard + ChatGPT-MD + Claude-export |
| `sequenced-prompts.jsonl` | 5,703 | 58MB | Unified timeline, deduped |
| `seeds.jsonl` | 487 | 11MB | Prompts carrying durable design intent (prior run) |
| `NARRATIVE-SUMMARY.md` | — | 4.7KB | Engine-generated narrative summary |
| `SEED-CATALOGUE.md` | — | 25KB | Human-readable seed catalogue by type |

## Seed Types

| Type | Count | Description |
|------|-------|-------------|
| theoretical_grounding | 272 | Invokes formal concepts, theories, frameworks |
| rejection_correction | 116 | "No, not that" — defines system boundaries |
| process_definition | 55 | Workflow, protocol, sequence definitions |
| naming_act | 32 | Creates names ($VARIABLE, double-hyphen, organ) |
| consolidation_order | 26 | Merge, collapse, reduce, simplify directives |
| strategic_vision | 23 | Goals, outcomes, end-states, commercial intent |
| design_directive | 21 | Names structures, declares architectures |

## How to Query

```bash
# Find all seeds about consolidation
cat seeds.jsonl | python3 -c "
import json, sys
for line in sys.stdin:
    e = json.loads(line)
    if 'consolidation_order' in e.get('seed_types', []):
        print(e['content']['text'][:200])
"

# Find all prompts from a specific organ
grep '"organ": "ORGAN-IV"' sequenced-prompts.jsonl | wc -l

# Find prompts mentioning a specific concept
grep -i 'dispersio\|palingenesis' sequenced-prompts.jsonl | wc -l

# Full re-extraction
organvm prompts narrate --output annotated-prompts.jsonl --summary NARRATIVE-SUMMARY.md
python3 ingest-supplementary.py
python3 sequence-and-merge.py
python3 extract-seeds.py
```

## Scripts

| Script | Purpose |
|--------|---------|
| `ingest-supplementary.py` | Extract prompts from Clipboard/Paste.app, ChatGPT-MD, Claude-export, SpecStory |
| `sequence-corpus.py` | Merge all sources, sort chronologically, deduplicate |
| `extract-seeds.py` | Classify prompts into 7 seed types |

## Theoretical Grounding

This corpus operationalizes three existing system plans:

1. **V2 Gravitational Collapse** (2026-03-30) — every directory submits proof of necessity. The prompts ARE the proofs — they are the human's original intent that justified each piece of the system.
2. **SPEC-022 Dispersio Formalis** (2026-04-01) — the system's relationship to its own intentions is asymptotic. This corpus captures the intentions; the code captures the dispersed implementations. The gap between them is the permanent wound.
3. **Logos Documentation Layer** (2026-04-03) — Telos/Pragma/Praxis/Receptio. The seeds are the Telos (what was intended). The code is the Pragma (what was built). The gap between them is the Praxis (what needs to happen next).
