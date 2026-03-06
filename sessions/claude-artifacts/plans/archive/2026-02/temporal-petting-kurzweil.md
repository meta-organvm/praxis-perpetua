# Platinum Sprint: Uniform Elevation of All Code Repos

## Context

The organvm system launched 2026-02-11 with ~270K words across 78 GitHub repos. All planned documentation work is complete. This sprint elevates **all repos with any code** (~38 repos) to **Platinum status** — the highest quality tier — with uniform treatment regardless of size.

### Key Audit Finding: The Documentation-Implementation Gap

Only 30 of 67 non-infrastructure repos have substantial code. 8 more have skeleton/minimal code. The remaining 32 are README-only. Per user decision, ALL repos with any code (including skeletons) get full Platinum.

### Per-Organ Implementation Reality

| Organ | Total | Has Code | Skeleton | Docs-Only |
|-------|-------|----------|----------|-----------|
| I (Theory) | 17 | 9 | 4 | 4 |
| II (Art) | 17 | 4 | 6 | 7 |
| III (Commerce) | 20 | 15 | 3 | 2 |
| IV (Orchestration) | 7 | 4 | 0 | 3 |
| V (Public) | 1 | 1 | 0 | 0 |
| VI (Community) | 3 | 0 | 0 | 3 |
| VII (Marketing) | 4 | 0 | 0 | 4 |
| META | 1 | 1 | 0 | 0 |
| **Total** | **70** | **34** | **13** | **23** |

Note: ORGAN-VI and VII are 100% docs-only — excluded from this sprint.

---

## Platinum Definition (Uniform)

Every code repo gets ALL of the following:

| Dimension | Deliverable |
|-----------|-------------|
| **CI/CD** | GitHub Actions workflow (language-appropriate: Python/TS/mixed/minimal) |
| **Badges** | 6+ badges: CI status, coverage, organ, license, status, language |
| **Community Health** | CONTRIBUTING.md, SECURITY.md, CODE_OF_CONDUCT.md at org level; CHANGELOG.md per repo |
| **README** | 4,500+ words, 95+/100 rubric score, standardized badge row |
| **Architecture** | 2-5 ADRs in `docs/adr/` documenting key design decisions |
| **API Docs** | TypeDoc (TS) or Sphinx (Python) config for auto-generated documentation |
| **Changelog** | Keep a Changelog format in CHANGELOG.md |
| **Registry** | New `implementation_status` field + `ci_workflow` field |

---

## Execution Plan (5 Waves)

### Wave 0: Infrastructure & Templates (~15 min)

**Scope:** Create reusable templates, deploy org-level health files

1. **Deploy community health files to ORGAN-I and ORGAN-II** — these are the only two orgs missing them (Gold Sprint deployed to III-VII + meta)
   - Files: CONTRIBUTING.md, SECURITY.md, CODE_OF_CONDUCT.md → `.github` repos
   - Source: existing templates at `.github/` in planning corpus

2. **Create 4 CI workflow templates** (stored locally, deployed per-repo):
   - `ci-python.yml` — pytest + coverage + ruff + mypy (graceful degradation)
   - `ci-typescript.yml` — npm/pnpm/yarn test + eslint + tsc (package manager detection)
   - `ci-mixed.yml` — parallel Python + TS jobs
   - `ci-minimal.yml` — universal (lint markdown, validate structure, always passes)

3. **Create badge template** — standardized 6-badge row per organ color scheme

4. **Create CHANGELOG.md template** — Keep a Changelog format with initial entry

5. **Create ADR template** — Numbered `docs/adr/001-*.md` format

**Files modified:** 2 org `.github` repos (ORGAN-I, ORGAN-II), local templates

---

### Wave 1: Flagships (8 repos, parallel agents)

The 8 flagship repos get the most attention. Deploy in parallel:

| # | Repo | Organ | Lang | CI Template | Notes |
|---|------|-------|------|-------------|-------|
| 1 | recursive-engine--generative-entity | I | Python | ci-python | 1,254 tests, 85% coverage |
| 2 | metasystem-master | II | TS+Python | ci-mixed | Monorepo, `master` branch |
| 3 | public-record-data-scrapper | III | TS | ci-typescript | 2,055 tests, Vercel deploy |
| 4 | orchestration-start-here | IV | Python | ci-python | 3 validation scripts |
| 5 | agentic-titan | IV | Python | ci-python | 1,095 tests |
| 6 | public-process | V | Jekyll | ci-minimal | Jekyll site + essays |
| 7 | a-mavs-olevm | II | JS | ci-typescript | Portfolio site |
| 8 | organvm-corpvs-testamentvm | META | Python | ci-python | Validation scripts |

**Per flagship:**
- Deploy CI workflow → `.github/workflows/ci.yml`
- Upgrade README → 4,500+ words with 6+ badges
- Add CHANGELOG.md
- Add 3-5 ADRs in `docs/adr/`
- Update registry entry

---

### Wave 2: ORGAN-I Standard Code Repos (8 repos, parallel)

| # | Repo | Size | CI Template |
|---|------|------|-------------|
| 1 | organon-noumenon--ontogenetic-morphe | 919K Python | ci-python |
| 2 | auto-revision-epistemic-engine | 108K Python | ci-python |
| 3 | narratological-algorithmic-lenses | 511K Python | ci-python |
| 4 | call-function--ontological | minimal | ci-minimal |
| 5 | sema-metra--alchemica-mundi | 384K TS | ci-typescript |
| 6 | cognitive-archaelogy-tribunal | 129K Python | ci-python |
| 7 | a-recursive-root | 37K mixed | ci-python |
| 8 | radix-recursiva-solve-coagula-redi | 212K Python | ci-python |
| 9 | reverse-engine-recursive-run | 22K Python | ci-python |
| 10 | linguistic-atomization-framework | 955K Python | ci-python |
| 11 | my-knowledge-base | 1.7M TS | ci-typescript |

Plus ORGAN-I skeletons:
| 12 | system-governance-framework | shell only | ci-minimal |
| 13 | cog-init-1-0- | empty | ci-minimal |
| 14 | collective-persona-operations | empty | ci-minimal |
| 15 | 4-ivi374-F0Rivi4 | empty branch | ci-minimal |

**Per repo:** CI workflow + badge row upgrade + CHANGELOG + 2 ADRs + README expansion to 4,500+

---

### Wave 3: ORGAN-II + ORGAN-III + ORGAN-IV Code Repos (parallel)

**ORGAN-II (4 code + 6 skeleton):**
| Repo | CI Template |
|------|-------------|
| a-i-council--coliseum | ci-python |
| example-generative-music | ci-typescript |
| client-sdk | ci-minimal |
| artist-toolkit-and-templates | ci-minimal |
| example-choreographic-interface | ci-minimal |
| example-theatre-dialogue | ci-minimal |
| audio-synthesis-bridge | ci-minimal |
| academic-publication | ci-minimal |
| showcase-portfolio | ci-minimal |
| archive-past-works | ci-minimal |
| case-studies-methodology | ci-minimal |
| learning-resources | ci-minimal |
| example-interactive-installation | ci-minimal |
| example-ai-collaboration | ci-minimal |

**ORGAN-III (15 code + 3 skeleton):**
| Repo | CI Template |
|------|-------------|
| classroom-rpg-aetheria | ci-typescript |
| gamified-coach-interface | ci-typescript |
| trade-perpetual-future | ci-mixed |
| fetch-familiar-friends | ci-typescript |
| sovereign-ecosystem--real-estate-luxury | ci-typescript |
| search-local--happy-hour | ci-typescript |
| multi-camera--livestream--framework | ci-minimal |
| universal-mail--automation | ci-python |
| mirror-mirror | ci-typescript |
| the-invisible-ledger | ci-typescript |
| enterprise-plugin | ci-minimal |
| virgil-training-overlay | ci-minimal (Swift) |
| tab-bookmark-manager | ci-typescript |
| a-i-chat--exporter | ci-typescript |
| the-actual-news | ci-typescript |
| your-fit-tailored | ci-minimal |
| my-block-warfare | ci-typescript |
| life-my--midst--in | ci-typescript |
| my--father-mother | ci-python |

**ORGAN-IV (2 remaining code repos):**
| Repo | CI Template |
|------|-------------|
| agent--claude-smith | ci-typescript |
| a-i--skills | ci-python |
| petasum-super-petasum | ci-minimal |
| universal-node-network | ci-minimal |

**Per repo:** CI workflow + badge row + CHANGELOG + 2 ADRs + README to 4,500+

---

### Wave 4: ORGAN-V Essays + ORGAN-VI/VII Badge Polish

**New essays for ORGAN-V public-process** (5 new, bringing total to 10):
1. "Testing the Meta-System: CI/CD Across Eight Organs"
2. "The Documentation-Implementation Gap: Honest Accounting"
3. "From Bronze to Platinum: Quality Ladders for Creative Infrastructure"
4. "AI-Conductor Methodology: Directing 270,000 Words of Documentation"
5. "Uniform Quality at Scale: How Every Repo Earns Its Badges"

**ORGAN-VI/VII polish** (docs-only repos, not full Platinum but badge/CHANGELOG upgrade):
- Add CHANGELOG.md to all 7 repos
- Standardize badge rows

---

### Wave 5: Registry + Validation

1. **Registry schema update** — add to every repo entry:
   ```json
   "implementation_status": "PRODUCTION" | "PROTOTYPE" | "SKELETON" | "DESIGN_ONLY",
   "ci_workflow": "ci-python.yml" | "ci-typescript.yml" | "ci-mixed.yml" | "ci-minimal.yml" | null,
   "platinum_status": true | false
   ```

2. **Update summary counts and launch_metrics**

3. **Run full validation suite:**
   - V3: Registry reconciliation (expect 80 entries, 78 on GitHub)
   - V4: Dependency validation (0 violations)
   - V5/V6: Constitution + organ checks
   - NEW: CI workflow audit (all 38+ repos have workflows)
   - NEW: Badge audit (all repos have 6+ badges)
   - NEW: CHANGELOG audit (all repos have CHANGELOG.md)

4. **Commit updated registry + validation scripts to corpvs-testamentvm**

---

## Parallel Execution Strategy

Given 16GB RAM constraint, run max 4-5 parallel agents:

```
Wave 0 (sequential, ~15 min)
  → Wave 1: 4 agents × 2 flagships each (~30 min)
  → Wave 2: 3 agents × 5 repos each (~30 min)
  → Wave 3: 5 agents × 7-8 repos each (~45 min)
  → Wave 4: 2 agents (essays + badge polish) (~20 min)
  → Wave 5: 1 agent (registry + validation) (~15 min)
```

---

## CI Template Reference

4 workflow templates designed with graceful degradation (see `/Users/4jp/.claude/plans/temporal-petting-kurzweil-agent-aa2155b.md` for full YAML):

- **ci-python.yml**: pytest + coverage + ruff + mypy. Auto-detects pyproject.toml/requirements.txt/setup.py. Passes if no tests exist.
- **ci-typescript.yml**: npm/pnpm/yarn detection, test + eslint + tsc + build. Multi-node-version matrix (18/20/22).
- **ci-mixed.yml**: Parallel Python + TS jobs with independent coverage.
- **ci-minimal.yml**: Universal. Markdown lint + structure validation. Always passes green.

---

## Files Modified

| Category | Count | Details |
|----------|-------|---------|
| CI workflows on GitHub | ~52 | `.github/workflows/ci.yml` per repo |
| CHANGELOG.md on GitHub | ~52 | Initial version per repo |
| README.md upgrades on GitHub | ~38 | Badge rows + content expansion |
| ADR files on GitHub | ~100-150 | `docs/adr/001-*.md` per repo |
| Org .github repos | 2 | ORGAN-I + II community health files |
| ORGAN-V essays | 5 | New essays in public-process |
| registry-v2.json | 1 | Schema update + all repo entries |
| Validation scripts | 1-2 | New Platinum audit script |

## Verification

- [ ] All ~38 code repos have CI workflows deployed and green (or green-with-notices for skeletons)
- [ ] All repos have 6+ standardized badges in README
- [ ] All repos have CHANGELOG.md
- [ ] All repos have 2-5 ADRs in `docs/adr/`
- [ ] ORGAN-I and II have community health files at org level
- [ ] ORGAN-V has 10 published essays
- [ ] Registry has `implementation_status`, `ci_workflow`, `platinum_status` fields
- [ ] Full validation suite passes (V3-V6 + Platinum checks)
- [ ] ~52 repos across 8 orgs touched, zero broken links, zero dependency violations
