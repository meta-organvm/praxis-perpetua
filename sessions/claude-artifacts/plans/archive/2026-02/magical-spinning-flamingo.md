# Silver Sprint: Document All Remaining Repos

## Context

Bronze Sprint is **COMPLETE** (2026-02-10). 7 flagship READMEs deployed, 34/34 validation passed. The user wants **all repos documented to the same standard of exploration** before deciding what to pin. Pinning is deferred until every repo has been explored and given a proper README.

**Scope:** 64 repos need work (79 total - 7 Bronze flagships - 8 .github infra repos already done).

---

## Work Order: 4 Waves, Organ-by-Organ

### Wave 1: ORGAN-I Theory (16 repos)
Goes first because it's the theoretical foundation — other organs cross-reference it.

| # | Repo | Tier | Action |
|---|------|------|--------|
| 1-12 | 12 public standard repos (organon-noumenon, auto-revision-epistemic-engine, narratological-algorithmic-lenses, call-function--ontological, sema-metra--alchemica-mundi, nexus--babel-alexandria-, reverse-engine-recursive-run, 4-ivi374-F0Rivi4, linguistic-atomization-framework, my-knowledge-base, a-recursive-root, radix-recursiva-solve-coagula-redi) | standard | EXPLORE + WRITE 1,000+ words |
| 13-14 | 2 private repos (system-governance-framework, cognitive-archaelogy-tribunal) | standard | EXPLORE + WRITE governance README |
| 15-16 | 2 stubs (cog-init-1-0-, collective-persona-operations) | stub | WRITE 200+ words |

**Batches:** 5 batches of 3 repos each + 1 batch of 1.

### Wave 2A: ORGAN-III Commerce (19 repos) — parallel with Wave 2B
Revenue-generating products = highest portfolio impact after flagships.

| # | Repo | Tier | Action |
|---|------|------|--------|
| 1-10 | 10 public standard repos (classroom-rpg-aetheria, gamified-coach-interface, fetch-familiar-friends, multi-camera--livestream--framework, universal-mail--automation, tab-bookmark-manager, the-actual-news, my-block-warfare, life-my--midst--in, my--father-mother) | standard | EXPLORE + WRITE 1,000+ words |
| 11 | a-i-chat--exporter (fork) | standard | WRITE (lighter, ~50K TE) |
| 12-13 | 2 private standard (trade-perpetual-future, sovereign-ecosystem--real-estate-luxury) | standard | WRITE governance README |
| 14-16 | 3 public stubs (search-local--happy-hour, virgil-training-overlay, your-fit-tailored) | stub | WRITE 200+ words |
| 17-18 | 2 private stubs (mirror-mirror, the-invisible-ledger) | stub | WRITE governance stub |
| 19 | enterprise-plugin | archive | Archive notice |

### Wave 2B: ORGAN-II Art (20 repos) — parallel with Wave 2A
Most complex organ: mix of active code, NOT_CREATED, archives, duplicates.

| # | Repo | Tier | On GH? | Action |
|---|------|------|--------|--------|
| 1-3 | a-mavs-olevm, a-i-council--coliseum, artist-toolkit-and-templates | standard | yes | EXPLORE + WRITE |
| 4 | client-sdk | standard | yes | WRITE API docs |
| 5-9 | 5 skeleton/stub repos on GH (example-theatre-dialogue, example-generative-music, example-choreographic-interface, audio-synthesis-bridge, academic-publication) | stub | yes | WRITE 200+ words |
| 10-13 | 4 archive repos (core-engine, performance-sdk, example-generative-visual, docs) | archive | yes | Archive notice → metasystem-master |
| 14 | artist-toolkits-templates (empty duplicate) | DELETE | yes | Delete repo |
| 15-20 | 6 NOT_CREATED repos (showcase-portfolio, archive-past-works, case-studies-methodology, learning-resources, example-interactive-installation, example-ai-collaboration) | stub | **no** | CREATE repo + WRITE stub |

### Wave 3: ORGAN-IV Orchestration (4 repos)
Goes after I/II/III so cross-references can be fully resolved.

| # | Repo | Tier | Action |
|---|------|------|--------|
| 1-3 | agent--claude-smith, a-i--skills, petasum-super-petasum | standard | EXPLORE + WRITE 1,000+ words |
| 4 | universal-node-network | stub | WRITE 200+ words |

Note: 3 dual-listed NOT_CREATED repos (orchestration-start-here, system-governance-framework, cognitive-archaelogy-tribunal) deferred to Phase 2 — needs canonical home decision.

### Wave 4: ORGAN-VI + VII (5 NOT_CREATED repos)
All private stubs. Lowest portfolio impact, go last.

| # | Repo | Organ | Action |
|---|------|-------|--------|
| 1-2 | salon-archive, reading-group-curriculum | VI | CREATE + WRITE stub |
| 3-5 | announcement-templates, social-automation, distribution-strategy | VII | CREATE + WRITE stub |

---

## Per-Repo Protocol

For each repo:

1. **Explore** — `gh api` to inspect repo tree, read existing README, read key files (package.json, entry points, etc.). Understand what the code actually does.
2. **Write** — Select organ template from `03-per-organ-readme-templates.md`. Standard: 1,000+ words, 8 sections, score >= 70. Stub: 200+ words, 4 sections. Archive: notice + redirect.
3. **Deploy** — `gh api` PUT README.md (base64-encoded). Create repo first if NOT_CREATED.
4. **Update Registry** — Set `documentation_status` → DEPLOYED, `last_validated` → today.

---

## Tier Standards

| Tier | Words | Sections | Score Target | Badge Requirement |
|------|-------|----------|-------------|-------------------|
| Standard | 1,000+ | 8 | >= 70/100 | 2+ (organ + 1 metadata) |
| Stub | 200+ | 4 | n/a | 1 (organ badge) |
| Archive | 50+ | 2 | n/a | 1 (organ badge) |

---

## TE Budget Estimate

| Wave | Repos | TE Estimate |
|------|-------|-------------|
| Wave 1 (ORGAN-I) | 16 | ~956K |
| Wave 2A (ORGAN-III) | 19 | ~998K |
| Wave 2B (ORGAN-II) | 20 | ~578K |
| Wave 3 (ORGAN-IV) | 4 | ~240K |
| Wave 4 (VI+VII) | 5 | ~140K |
| Cross-reference passes | — | ~100K |
| **Total** | **64** | **~3.0M TE** |

---

## Execution Approach

- **3 repos per batch**, same organ, similar tier
- Explore → Write → Deploy → Update registry for each batch
- Cross-reference resolution pass after each wave completes
- Wave 1 first (ORGAN-I), then Waves 2A+2B can run in parallel, then 3, then 4
- Final system-wide link check after all waves

---

## Validation (Silver Sprint Completion Criteria)

- [ ] All 64 repos have READMEs deployed at their tier level
- [ ] All standard-tier READMEs score >= 70/100
- [ ] 0 broken links across all 79 repos
- [ ] 0 TBD markers in any deployed README
- [ ] Registry updated for all 64 repos
- [ ] 15 NOT_CREATED repos created on GitHub
- [ ] 4 archive repos have archive notices
- [ ] No dependency back-edges in any cross-reference

---

## Key Files

| File | Role |
|------|------|
| `registry-v2.json` | Source of truth — update after every deployment |
| `docs/planning/03-per-organ-readme-templates.md` | Templates per organ type |
| `docs/standards/10-repository-standards.md` | Badge, hero, tier standards |
| `docs/planning/01-readme-audit-framework.md` | Scoring rubric |
| `docs/specs/bronze-sprint/flagships/*.md` | Reference quality from Bronze |

## Starting Point

Begin with **Wave 1, Batch I-A**: Explore and write READMEs for the first 3 ORGAN-I standard-tier repos. The first batch sets the quality standard for the entire sprint.
