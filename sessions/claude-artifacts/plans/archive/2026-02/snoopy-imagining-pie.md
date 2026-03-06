# Plan: Governance Invocation System — Quick-Reference & Context Summoning

## Context

The governance quadrilateral (roadmap + catalog + cadence + rolling TODO) plus the e2g-ii audit trail use **6 independent ID namespaces** with ~90+ short codes scattered across 5+ documents. When you encounter "X1" or "AP-3" or "#8" in conversation or during a Friday review, there's no way to quickly resolve what it means without opening the right file and scrolling to the right section.

**What we're building:** A three-layer invocation stack:
1. **Concordance document** — single-file symbol table mapping every ID to definition + source
2. **CLAUDE.md section** — teaches Claude the ID system for conversational lookups
3. **CLI script** — `scripts/invoke.py X1` for terminal-based context summoning

## Files to Create/Modify

| File | Action |
|------|--------|
| `docs/operations/concordance.md` | **CREATE** — master ID lookup across all 6 namespaces |
| `scripts/invoke.py` | **CREATE** — CLI tool that parses concordance.md and returns context |
| `CLAUDE.md` | **EDIT** — add "Invocation System" section after "Working With This Corpus" |
| `docs/operations/rolling-todo.md` | **EDIT** — add concordance.md to Companions line |
| `docs/operations/operational-cadence.md` | **EDIT** — add concordance.md to Companions line |
| MEMORY.md | **EDIT** — record the invocation system |

## 1. Create `docs/operations/concordance.md`

A flat lookup table organized by namespace. Each entry: ID, one-line definition, source document, status/constraint tag where applicable.

### Structure

```markdown
# Concordance — Governance ID Reference

## How to Use
(explain lookup patterns, link to invoke.py)

## TODO Items (from rolling-todo.md / e2g-ii)
| ID | Definition | Constraint | Source | Omega |
X1, X2, X3, X4, E1-E5, M1-II–M6-II, S1-II–S6-II, G1-G3
(23 entries)

## Omega Criteria (from there+back-again.md)
| # | Criterion | Horizon | Evidence |
#1–#17
(17 entries)

## Horizons (from there+back-again.md)
| ID | Name | Timeline | Focus |
H1–H5
(5 entries)

## Anti-Patterns (from operational-cadence.md)
| ID | Name | Test Question |
AP-1–AP-7
(7 entries)

## E2G-II Findings (from e2g-ii-action-items.md)
| ID | Finding | Action Items |
W1-II–W6-II, SP1-II–SP4-II, BS2-II, BS5-II, LC1-II–LC4-II, BL1-II, BL3-II, ET2-II, ET3-II, LO3-II
(~18 entries)

## Sprints (from sprint specs + catalog)
| # | Name | Status | Spec |
01–29 (completed), selected catalog entries
(29+ entries)

## Cross-Reference: Omega → TODO
(which TODO items advance which omega criteria — already partially in rolling-todo.md, collected here as a matrix)
```

**Total entries:** ~100 IDs across 6 namespaces.

### Data Sources (all already read in conversation)

- TODO items: `docs/operations/rolling-todo.md` (23 items)
- Omega criteria: `docs/strategy/there+back-again.md` lines 328-344
- Horizons: `docs/strategy/there+back-again.md` (H1-H5 in quick ref)
- Anti-patterns: `docs/operations/operational-cadence.md` lines 524-570
- E2G-II findings: `docs/evaluation/e2g-ii-action-items.md` lines 174-190
- Sprints: `docs/specs/sprints/` (29 files, filenames carry the data)

## 2. Create `scripts/invoke.py`

A Python CLI tool matching the existing script conventions (argparse, `#!/usr/bin/env python3`, `REPO_ROOT = Path(__file__).parent.parent`).

### Interface

```
Usage:
    python3 scripts/invoke.py X1                  # lookup single ID
    python3 scripts/invoke.py X1 E3 AP-2          # lookup multiple IDs
    python3 scripts/invoke.py --namespace todo     # list all TODO items
    python3 scripts/invoke.py --namespace omega    # list all omega criteria
    python3 scripts/invoke.py --tag INCOME         # filter by constraint tag
    python3 scripts/invoke.py --tag READY          # filter by constraint tag
    python3 scripts/invoke.py --search "stranger"  # full-text search across definitions
    python3 scripts/invoke.py --list               # list all namespaces and counts
```

### Implementation

- Parse `docs/operations/concordance.md` as the data source (markdown table parsing)
- Detect namespace from ID pattern:
  - `X\d`, `E\d`, `M\d`, `S\d`, `G\d` → TODO items
  - `#\d+` or bare number 1-17 → Omega criteria
  - `H[1-5]` → Horizons
  - `AP-\d` → Anti-patterns
  - `*-II` pattern → E2G-II findings
  - Two-digit number or sprint name → Sprints
- Output: formatted text block with ID, definition, source path, related IDs
- No external dependencies (stdlib only: argparse, pathlib, re, sys)

## 3. Edit `CLAUDE.md` — Add Invocation System Section

Insert after the "Working With This Corpus" section (after line ~143). Content:

```markdown
## Invocation System

The governance corpus uses short IDs across 6 namespaces. When the user references an ID (e.g., "what's X1?", "show me AP-3", "which items advance #8"), look up context in `docs/operations/concordance.md`.

| Prefix | Namespace | Source | Example |
|--------|-----------|--------|---------|
| X1–X4 | TODO: P0 hermetic seal | rolling-todo.md / e2g-ii | X1 = Submit Creative Lab Five |
| E1–E5 | TODO: P1 engagement | rolling-todo.md / e2g-ii | E3 = Google Creative Fellowship |
| M1-II–M6-II | TODO: P2 quality | rolling-todo.md / e2g-ii | M2-II = Stripe integration |
| S1-II–S6-II | TODO: P3 strategic | rolling-todo.md / e2g-ii | S2-II = Host first salon |
| G1–G3 | TODO: setup guide | rolling-todo.md | G2 = Render hosting |
| #1–#17 | Omega criteria | there+back-again.md | #8 = Product live |
| H1–H5 | Horizons | there+back-again.md | H3 = Generate Revenue |
| AP-1–AP-7 | Anti-patterns | operational-cadence.md | AP-1 = Don't start another sprint |
| W/SP/BS/LC/BL/ET/LO-II | E2G-II findings | e2g-ii-action-items.md | W1-II = Zero external contact |
| 01–29 | Completed sprints | docs/specs/sprints/ | 29 = AUTOMATA |

CLI: `python3 scripts/invoke.py <ID>` for terminal lookup.
```

## 4. Minor Edits

- **`docs/operations/rolling-todo.md`**: Add `[`concordance.md`](./concordance.md) (ID lookup)` to Companions line
- **`docs/operations/operational-cadence.md`**: Add `[`concordance.md`](./concordance.md) (ID lookup)` to Companions line
- **MEMORY.md**: Add note about invocation system (concordance + invoke.py + CLAUDE.md awareness)

## Verification

1. `python3 scripts/invoke.py X1` returns the Creative Lab Five entry with source link
2. `python3 scripts/invoke.py --namespace omega` returns all 17 criteria
3. `python3 scripts/invoke.py --tag INCOME` returns exactly the 4 INCOME-tagged items
4. `python3 scripts/invoke.py AP-3` returns the anti-pattern with its test question
5. `python3 scripts/invoke.py --search "stranger"` finds M1-II and #2
6. Every ID in concordance.md resolves to a real entry in its source document
7. CLAUDE.md invocation table matches concordance.md namespace structure
