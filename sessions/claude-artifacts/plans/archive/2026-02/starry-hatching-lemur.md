# Plan: Reorganize Root Directory — Minimal Root with Ontological Naming

## Context

The project root has **43 items** (37 files + 6 directories). This violates the "Minimal Root" philosophy from the `github-repository-standards` skill, where the root should contain only architectural pillars and implementation details belong in subdirectories. The file names are also inconsistent (mixed SCREAMING-CASE, Title-Case, kebab-case, URL slugs) making the project opaque to outsiders.

**Goal:** Reduce root to ~10 items (including hidden), rename files ontologically for outsider legibility, create a `DIRECTORY.md` map, and follow the `github-repo-curator` and `github-repository-standards` skill protocols.

---

## Target Root Structure (10 items total)

```
ingesting-organ-document-structure/
├── .github/              # GitHub community health (required at root)
├── .gitignore            # Git convention
├── README.md             # Landing page
├── LICENSE               # CC BY-SA 4.0
├── CLAUDE.md             # Claude Code agent context
├── DIRECTORY.md          # NEW: concise corpus directory map
├── registry-v2.json      # Single source of truth (kept at root — 56 cross-refs)
├── .config/              # Org naming configuration
│   ├── organvm.env
│   ├── organvm.config.json
│   └── organvm.env.local (gitignored)
└── docs/                 # ALL documentation
    ├── ANNOTATED-MANIFEST.md
    ├── genesis/           # Layer 0: foundational transcripts & audit
    ├── planning/          # Layer 1: numbered planning toolkit (01–05)
    ├── strategy/          # Layer 2: execution strategy & roadmap
    ├── implementation/    # Layer 3: v2 active specs
    ├── evaluation/        # Layer 4: cross-AI validation & review
    ├── standards/         # Layer 5: repo & development standards
    ├── agents/            # AI agent onboarding docs
    ├── validation-runs/   # Frozen CLI validation artifacts
    ├── archive/           # Frozen v1 predecessors
    ├── memory/            # Project constitution
    └── specs/             # Sprint specifications
```

**Count:** 4 hidden (.github, .gitignore, .config, .DS_Store) + 5 visible (README.md, LICENSE, CLAUDE.md, DIRECTORY.md, registry-v2.json) + 1 visible dir (docs/) = **~10 items**.

---

## Complete File Mapping (OLD → NEW)

### Stays at root (unchanged)

| File | Reason |
|------|--------|
| `README.md` | GitHub convention |
| `LICENSE` | GitHub convention |
| `CLAUDE.md` | Claude Code convention |
| `registry-v2.json` | SSOT, 56 cross-refs |
| `.gitignore` | Git convention |
| `.github/` | GitHub convention (contents unchanged) |

### Deleted (byte-identical duplicates confirmed via md5)

| File | Original lives at |
|------|-------------------|
| `THREE_CLI_COMPARISON_ANALYSIS.md` | `github-copilot-cli/THREE_CLI_COMPARISON_ANALYSIS.md` |
| `three_run_comparison_report.md` | `codex-cli/runs/20260209-135130/three_run_comparison_report.md` |
| `triptych_comparison_report.md` | `gemini-cli/triptych_comparison_report.md` |
| `gemini_vs_copilot_comparison.md` | `gemini-cli/gemini_vs_copilot_comparison.md` |

### Config → `.config/`

| Current | New |
|---------|-----|
| `organvm.env` | `.config/organvm.env` |
| `organvm.config.json` | `.config/organvm.config.json` |
| `organvm.env.local` (gitignored) | `.config/organvm.env.local` |

### Genesis → `docs/genesis/`

| Current | New | Rename rationale |
|---------|-----|-----------------|
| `00-a-let-s-ingest-digest-the-document-in-the-project-files-ORGAN-i-vii-sub-ORGANS.md` | `docs/genesis/00-a-system-genesis-transcript.md` | URL slug from ChatGPT export → readable name |
| `00-b-Organizing-Local-Remote-Structure.md` | `docs/genesis/00-b-local-remote-structure-transcript.md` | Normalize case, clarify format |
| `00-c-MASTER-SUMMARY.md` | `docs/genesis/00-c-master-summary.md` | Normalize case |
| `00-00-ORGAN_SYSTEM_AUDIT.md` | `docs/genesis/00-d-organ-system-audit.md` | `00-00` → `00-d` for consistent lettered genesis series |

### Planning → `docs/planning/`

| Current | New |
|---------|-----|
| `01-README-AUDIT-FRAMEWORK.md` | `docs/planning/01-readme-audit-framework.md` |
| `02-REPO-INVENTORY-AUDIT.md` | `docs/planning/02-repo-inventory-audit.md` |
| `03-PER-ORGAN-README-TEMPLATES.md` | `docs/planning/03-per-organ-readme-templates.md` |
| `04-PER-ORGAN-VALIDATION-CHECKLISTS.md` | `docs/planning/04-per-organ-validation-checklists.md` |
| `05-RISK-MAP-AND-SEQUENCING.md` | `docs/planning/05-risk-map-and-sequencing.md` |

### Strategy → `docs/strategy/`

| Current | New |
|---------|-----|
| `PARALLEL-LAUNCH-STRATEGY.md` | `docs/strategy/parallel-launch-strategy.md` |
| `PHASE-1-EXECUTION-INDEX.md` | `docs/strategy/phase-1-execution-index.md` |
| `there+back-again.md` | `docs/strategy/roadmap-there-and-back-again.md` |

### Implementation → `docs/implementation/`

| Current | New |
|---------|-----|
| `IMPLEMENTATION-PACKAGE-v2.md` | `docs/implementation/implementation-package-v2.md` |
| `orchestration-system-v2.md` | `docs/implementation/orchestration-system-v2.md` |
| `public-process-map-v2.md` | `docs/implementation/public-process-map-v2.md` |
| `github-actions-spec.md` | `docs/implementation/github-actions-spec.md` |

### Evaluation → `docs/evaluation/`

| Current | New |
|---------|-----|
| `06-EVALUATION-TO-GROWTH-ANALYSIS.md` | `docs/evaluation/06-evaluation-to-growth-analysis.md` |
| `07-CROSS-AI-LOGIC-CHECK-PROMPTS.md` | `docs/evaluation/07-cross-ai-logic-check-prompts.md` |
| `07-CROSS-AI-LOGIC-CHECK-RESULTS.md` | `docs/evaluation/07-cross-ai-logic-check-results.md` |
| `08-CANONICAL-ACTION-PLAN.md` | `docs/evaluation/08-canonical-action-plan.md` |
| `09-E2G-CORPUS-COHERENCE-REVIEW.md` | `docs/evaluation/09-corpus-coherence-review.md` |

### Standards → `docs/standards/`

| Current | New |
|---------|-----|
| `10-REPOSITORY-STANDARDS.md` | `docs/standards/10-repository-standards.md` |
| `11-SPECIFICATION-DRIVEN-DEVELOPMENT.md` | `docs/standards/11-specification-driven-development.md` |

### Agent docs → `docs/agents/`

| Current | New |
|---------|-----|
| `AGENTS.md` | `docs/agents/AGENTS.md` |
| `GEMINI.md` | `docs/agents/GEMINI.md` |

### Existing directories → inside `docs/`

| Current | New |
|---------|-----|
| `archive/` | `docs/archive/` (contents unchanged — frozen) |
| `memory/` | `docs/memory/` (contents unchanged) |
| `specs/` | `docs/specs/` (contents unchanged) |
| `codex-cli/` | `docs/validation-runs/codex-cli/` (contents unchanged — frozen) |
| `gemini-cli/` | `docs/validation-runs/gemini-cli/` (contents unchanged — frozen) |
| `github-copilot-cli/` | `docs/validation-runs/github-copilot-cli/` (contents unchanged — frozen) |

### Manifest

| Current | New |
|---------|-----|
| `ANNOTATED-MANIFEST.md` | `docs/ANNOTATED-MANIFEST.md` |

### New file

| File | Purpose |
|------|---------|
| `DIRECTORY.md` | Concise directory key/map at root |

---

## Cross-Reference Update Strategy

### What NOT to update (frozen artifacts)

- Everything inside `docs/validation-runs/` (codex-cli, gemini-cli, github-copilot-cli) — point-in-time snapshots
- Everything inside `docs/archive/` — frozen by project rule

### Two types of references

1. **Markdown links** `[text](filename.md)` — need correct relative paths based on the referencing file's new location
2. **Backtick references** `` `filename.md` `` — update to new filename only (no path prefix needed; DIRECTORY.md provides lookup)

### Relative path rules

| Referencing file location | Target at root | Target in same docs/ subdir | Target in different docs/ subdir |
|--------------------------|----------------|----------------------------|---------------------------------|
| Root (README.md, CLAUDE.md) | `filename` | `docs/subdir/filename` | `docs/subdir/filename` |
| `docs/planning/` | `../../filename` | `./filename` | `../otherdir/filename` |
| `docs/evaluation/` | `../../filename` | `./filename` | `../otherdir/filename` |

### Files requiring cross-reference updates (Category A — "live" documents)

Ordered by update complexity (most complex first):

1. **`CLAUDE.md`** — ~20+ references across Reading Order, Document Layers, Dependency Map, Working With This Corpus, Org Naming sections
2. **`docs/ANNOTATED-MANIFEST.md`** — references every file in the corpus; largest update surface
3. **`README.md`** — Quick Navigation table with 8+ markdown links
4. **All 28 moved markdown files** — each contains backtick references to sibling documents; some contain markdown links
5. **`docs/memory/constitution.md`** — ~5 references
6. **`docs/specs/bronze-sprint/spec.md`** — ~3 references
7. **`docs/specs/bronze-sprint/checklists/requirements.md`** — ~2 references
8. **`.github/PULL_REQUEST_TEMPLATE.md`** — ~1 reference
9. **`.gitignore`** — update `organvm.env.local` → `.config/organvm.env.local`

---

## Execution Order

### Phase 1: File moves (git mv)

1. Delete 4 duplicate comparison files
2. Create directory skeleton: `.config/`, `docs/{genesis,planning,strategy,implementation,evaluation,standards,agents,validation-runs}/`
3. `git mv` config files → `.config/`
4. `git mv` + rename genesis files → `docs/genesis/`
5. `git mv` + rename planning files → `docs/planning/`
6. `git mv` + rename strategy files → `docs/strategy/`
7. `git mv` + rename implementation files → `docs/implementation/`
8. `git mv` + rename evaluation files → `docs/evaluation/`
9. `git mv` + rename standards files → `docs/standards/`
10. `git mv` agent docs → `docs/agents/`
11. `git mv` existing directories → `docs/` (archive, memory, specs, 3 CLI dirs)
12. `git mv` ANNOTATED-MANIFEST.md → `docs/`
13. Move `organvm.env.local` (untracked) to `.config/`

### Phase 2: New files

14. Write `DIRECTORY.md` at root — concise map organized by directory with file→purpose tables
15. Update `.gitignore` — change `organvm.env.local` → `.config/organvm.env.local`

### Phase 3: Cross-reference updates

This is the most labor-intensive phase. Strategy: process files in batches by directory, using the mapping table for search-and-replace.

16. Update `README.md` — fix all markdown links in Quick Navigation and Document Architecture
17. Update `CLAUDE.md` — fix all references in Reading Order, Layers, Dependency Map, Working With This Corpus, Org Naming
18. Update all files in `docs/genesis/` — fix backtick references to sibling documents
19. Update all files in `docs/planning/` — fix backtick references
20. Update all files in `docs/strategy/` — fix backtick references
21. Update all files in `docs/implementation/` — fix backtick references
22. Update all files in `docs/evaluation/` — fix backtick references
23. Update all files in `docs/standards/` — fix backtick references
24. Update `docs/agents/AGENTS.md` and `docs/agents/GEMINI.md` — fix config file paths
25. Update `docs/memory/constitution.md` — fix references
26. Update `docs/specs/bronze-sprint/spec.md` and `checklists/requirements.md` — fix references
27. Update `docs/ANNOTATED-MANIFEST.md` — comprehensive update (file counts, all file paths, dependency map, reading order, quick reference table)

### Phase 4: Verification

28. Grep for every old filename across all Category A files — must return 0 matches
29. Validate `registry-v2.json` still parses (`python3 -m json.tool`)
30. Verify `DIRECTORY.md` matches actual filesystem tree
31. Verify `.gitignore` reflects new `.config/` path
32. Spot-check 5 markdown links from README.md to confirm they resolve

---

## Critical Files to Modify

| File | Path after reorg | Why critical |
|------|-----------------|--------------|
| `CLAUDE.md` | root (unchanged) | Every AI agent reads this first; most cross-refs |
| `README.md` | root (unchanged) | Public landing page; markdown links must work |
| `ANNOTATED-MANIFEST.md` | `docs/ANNOTATED-MANIFEST.md` | References every file; largest update surface |
| `.gitignore` | root (unchanged) | Must reflect `.config/` path |
| All 28 moved `.md` files | `docs/*/` | Internal cross-references need updating |

## Risk Mitigation

- **Cross-reference breakage:** Verify with grep after all updates; each old filename checked
- **CLAUDE.md staleness:** Update last, verify every path against filesystem
- **Frozen artifacts:** Validation-run dirs and archive/ are explicitly NOT touched
- **registry-v2.json:** Stays at root unchanged — zero risk
- **Git history:** Use `git mv` for all moves to preserve blame history
