# MEMORIA Sprint: Stale Data Audit Report

**Target state:** 97 repos, 90 ACTIVE, 7 ARCHIVED, 0 DESIGN_ONLY, 0 SKELETON
**Org counts:** I=20, II=30, III=27, IV=7, V=2, VI=4, VII=4, Meta=3

**Excluded from scope:** `docs/archive/*`, `registry-v2.json`, `scripts/*`, `docs/genesis/*`, essays (historical snapshots), `_posts/*`

---

## FINDINGS BY FILE (Active Documents Only)

### 1. `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/CLAUDE.md`

| Line | Current Text | Should Be | Category |
|------|-------------|-----------|----------|
| 7 | "coordinates 88 GitHub repositories" | "coordinates 97 GitHub repositories" | Stale repo count (88) |
| 12 | "~363K words across 88 repos" | "~386K+ words across 97 repos" | Stale repo count (88) + word count |
| 20 | `\| I \| ... \| 19 \|` | `\| I \| ... \| 20 \|` | ORGAN-I count |
| 21 | `\| II \| ... \| 26 \|` | `\| II \| ... \| 30 \|` | ORGAN-II count |
| 22 | `\| III \| ... \| 24 \|` | `\| III \| ... \| 27 \|` | ORGAN-III count |
| 27 | `\| VIII \| ... \| 2 \|` | `\| VIII \| ... \| 3 \|` | Meta count |

### 2. `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/README.md`

| Line | Current Text | Should Be | Category |
|------|-------------|-----------|----------|
| 14 | `Repos-91` (badge) | `Repos-97` | Stale repo count (91) |
| 17 | "coordinating 91 GitHub repositories" | "coordinating 97 GitHub repositories" | Stale repo count (91) |
| 19 | "91 repositories, ~386K+ words" | "97 repositories, ~386K+ words" | Stale repo count (91) |
| 107 | `\| Repos on GitHub \| 77 \| 91 \|` | `\| Repos on GitHub \| 77 \| 97 \|` | Stale repo count (91) |
| 112 | `\| ACTIVE status repos \| -- \| 84 (92.3%) \|` | `\| ACTIVE status repos \| -- \| 90 (92.8%) \|` | Stale ACTIVE count (84) |
| 125 | `\| I \| ... \| 19 \|` | `\| I \| ... \| 20 \|` | ORGAN-I count |
| 126 | `\| II \| ... \| 28 \|` (already partially updated) | `\| II \| ... \| 30 \|` | ORGAN-II count (28 is stale too) |
| 127 | `\| III \| ... \| 24 \|` | `\| III \| ... \| 27 \|` | ORGAN-III count |
| 172 | "bringing the total to 84 ACTIVE repos (92.3%)" | Historical sprint description -- consider adding note or updating to "which later grew to 90 ACTIVE" | Stale ACTIVE count in sprint narrative |
| 248 | "see all 91 repos" | "see all 97 repos" | Stale repo count (91) |
| 276 | "across 91 repos" | "across 97 repos" | Stale repo count (91) |

### 3. `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/strategy/there+back-again.md`

| Line | Current Text | Should Be | Category |
|------|-------------|-----------|----------|
| 96 | `\| Repos on GitHub \| 91 \|` | `\| Repos on GitHub \| 97 \|` | Stale repo count (91) |
| 97 | `\| Active repos \| 84 (92.3%) \|` | `\| Active repos \| 90 (92.8%) \|` | Stale ACTIVE count (84) |
| 99 | `\| Design-only repos \| 2 \|` | `\| Design-only repos \| 0 \|` | Stale DESIGN_ONLY count |
| 104 | "115 edges across 91 repos" | "115 edges across 97 repos" | Stale repo count (91) |
| 440 | "91 repos, 8 orgs" | "97 repos, 8 orgs" | Stale repo count (91) |
| 450 | "91 repos, 8 organizations" | "97 repos, 8 organizations" | Stale repo count (91) |
| 590 | "~386K+ words across 91 repositories" | "~386K+ words across 97 repositories" | Stale repo count (91) |

### 4. `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/strategy/sprint-catalog.md`

| Line | Current Text | Should Be | Category |
|------|-------------|-----------|----------|
| 52 | `\| Registry entries \| 91 (84 ACTIVE, 7 ARCHIVED) \|` | `\| Registry entries \| 97 (90 ACTIVE, 7 ARCHIVED) \|` | Stale repo + ACTIVE count |
| 107 | "MEMORY.md says '82 ACTIVE, 2 DESIGN_ONLY' -- registry shows 84 ACTIVE, 0 DESIGN_ONLY" | Update to reflect current truth: 90 ACTIVE, 0 DESIGN_ONLY | Sprint-catalog's own stale correction note is itself stale |
| 108 | "operational-cadence.md references '5 ORGAN-II SKELETON repos' -- registry shows 0 SKELETON" | Still valid as a note, but should confirm it has been fixed | Meta-stale reference |
| 109 | "Omega roadmap says 'Design-only repos: 2' -- now 0" | Still valid as a note to confirm fixe | Meta-stale reference |

### 5. `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/operations/operational-cadence.md`

| Line | Current Text | Should Be | Category |
|------|-------------|-----------|----------|
| 377 | "across 91 repositories" | "across 97 repositories" | Stale repo count (91) |
| 472 | "ORGAN-II SKELETON repos (5 repos: example-generative-music, ...)" | Remove or note these are now ACTIVE (0 SKELETON remain) | Stale SKELETON references |
| 475 | "91 repos is enough; don't add more" | "97 repos is enough; don't add more" | Stale repo count (91) |
| 525-536 | Section "### 5. The ORGAN-II SKELETON Repos Are a Trap" (entire section) | Rewrite or remove -- no SKELETON repos remain | Stale SKELETON section |
| 601 | "91 repositories is enough" | "97 repositories is enough" | Stale repo count (91) |

### 6. `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/operations/minimum-viable-operations.md`

| Line | Current Text | Should Be | Category |
|------|-------------|-----------|----------|
| 11 | "spanning 91 repositories" | "spanning 97 repositories" | Stale repo count (91) |

### 7. `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/operations/emergency-procedures.md`

| Line | Current Text | Should Be | Category |
|------|-------------|-----------|----------|
| 134 | "19 repos" (in ORGAN-I billing calculation) | "20 repos" | ORGAN-I count stale |

### 8. `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/evaluation/e2g-full-system-review.md`

| Line | Current Text | Should Be | Category |
|------|-------------|-----------|----------|
| 35 | "89 repos across 8 orgs" | "97 repos across 8 orgs" | Stale repo count (89) |
| 69 | "70 of 89 repos" | Update both numbers | Stale repo count (89) |
| 112 | "82 PRODUCTION, 7 ARCHIVED" | "90 ACTIVE, 7 ARCHIVED" | Stale count + PRODUCTION terminology |
| 132 | "PRODUCTION\|PROTOTYPE\|SKELETON\|DESIGN_ONLY\|ARCHIVED" | Note: PRODUCTION renamed to ACTIVE | PRODUCTION terminology |
| 145 | "89 repos, ~386K words" | "97 repos, ~386K+ words" | Stale repo count (89) |
| 171 | "8 orgs, 89 repos" | "8 orgs, 97 repos" | Stale repo count (89) |
| 177 | "77/89 repos" | Update ratio | Stale repo count (89) |
| 199 | "89 PRODUCTION repositories" / "89 repositories (82 actively maintained, 7 archived)" | Update to 97 repos (90 ACTIVE, 7 ARCHIVED) | Stale counts + PRODUCTION terminology |
| 321 | "89 repos, 82 PRODUCTION, 7 ARCHIVED" | "97 repos, 90 ACTIVE, 7 ARCHIVED" | Stale counts + PRODUCTION terminology |

### 9. `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/evaluation/e2g-action-items.md`

| Line | Current Text | Should Be | Category |
|------|-------------|-----------|----------|
| 24 | "all 24 ORGAN-III repos" | "all 27 ORGAN-III repos" | ORGAN-III count stale |
| 65 | "all 24 ORGAN-III repos" | "all 27 ORGAN-III repos" | ORGAN-III count stale |

### 10. `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/governance/quarterly-sustainability-checklist.md`

| Line | Current Text | Should Be | Category |
|------|-------------|-----------|----------|
| 83 | `baseline = {'PRODUCTION': 32, 'PROTOTYPE': 15, 'SKELETON': 16, 'DESIGN_ONLY': 20}` | Update baseline to reflect current state: `{'ACTIVE': 90, 'ARCHIVED': 7}` | Stale baseline + PRODUCTION terminology |
| 93 | "Verify SKELETON + DESIGN_ONLY count has decreased" | Update -- both are now 0 | Stale SKELETON/DESIGN_ONLY reference |
| 94 | "PRODUCTION repos degraded" | "ACTIVE repos degraded" | PRODUCTION terminology |
| 95 | "5 highest-portfolio-relevance SKELETON repos" | Remove or update -- 0 SKELETON | Stale SKELETON reference |

### 11. `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/applications/shared/metrics-snapshot.md`

| Line | Current Text | Should Be | Category |
|------|-------------|-----------|----------|
| 7 | `\| Total repositories \| 89 \|` | `\| Total repositories \| 97 \|` | Stale repo count (89) |
| 8 | `\| Production status \| 82 \|` | `\| Active status \| 90 \|` | Stale count + PRODUCTION terminology |
| 20 | "ORGAN-I: 19 repos" | "ORGAN-I: 20 repos" | ORGAN-I count |
| 21 | "ORGAN-II: 26 repos" | "ORGAN-II: 30 repos" | ORGAN-II count |
| 22 | "ORGAN-III: 24 repos" | "ORGAN-III: 27 repos" | ORGAN-III count |

### 12. `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/applications/shared/system-overview.md`

| Line | Current Text | Should Be | Category |
|------|-------------|-----------|----------|
| 5 | "coordinating 89 repositories" | "coordinating 97 repositories" | Stale repo count (89) |
| 9 | "89 repositories across 8 organizations" | "97 repositories across 8 organizations" | Stale repo count (89) |
| 10 | "82 production-grade repos" | "90 active repos" | Stale count + PRODUCTION terminology |
| 14 | "10 sprints completed" | Update sprint count (now 16+) | Stale sprint count |
| 18 | "validate 89 repositories" | "validate 97 repositories" | Stale repo count (89) |

### 13. `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/applications/00-portfolio-brief.md`

| Line | Current Text | Should Be | Category |
|------|-------------|-----------|----------|
| 19 | `\| Total repositories \| 81 \|` | `\| Total repositories \| 97 \|` | Stale repo count (81) |
| 21 | "~335,000 words" | "~386K+ words" | Stale word count |
| 24 | "20 published (~84K words)" | "29 published (~111K words)" | Stale essay count |
| 28 | "66 PRODUCTION, 1 PROTOTYPE, 2 SKELETON, 12 DESIGN_ONLY" | "90 ACTIVE, 0 PROTOTYPE, 0 SKELETON, 0 DESIGN_ONLY" (or "90 ACTIVE, 7 ARCHIVED") | Multiple stale counts + PRODUCTION terminology |
| 36 | `\| I \| Theoria \| ... \| 18 \|` | `\| I \| Theoria \| ... \| 20 \|` | ORGAN-I count (18, very old) |
| 37 | `\| II \| Poiesis \| ... \| 23 \|` | `\| II \| Poiesis \| ... \| 30 \|` | ORGAN-II count (23, very old) |
| 38 | `\| III \| Ergon \| ... \| 22 \|` | `\| III \| Ergon \| ... \| 27 \|` | ORGAN-III count (22, very old) |
| 41 | `\| VI \| Koinonia \| ... \| 3 \|` | `\| VI \| Koinonia \| ... \| 4 \|` | ORGAN-VI count |
| 43 | `\| VIII \| Meta \| ... \| 2 \|` | `\| VIII \| Meta \| ... \| 3 \|` | Meta count |

### 14. `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/operations/key-workflows.md`

| Line | Current Text | Should Be | Category |
|------|-------------|-----------|----------|
| 53 | `implementation_status: ACTIVE \| PROTOTYPE \| SKELETON \| DESIGN_ONLY \| ARCHIVED` | Still valid as schema definition (these are valid enum values) | OK -- schema reference, not a count |

### 15. `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/implementation/orchestration-system-v2.md`

| Line | Current Text | Should Be | Category |
|------|-------------|-----------|----------|
| 220 | `\| SKELETON \| Repo exists with minimal structure \|` | Still valid as tier definition | OK -- tier definition, not a count |

### 16. `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/docs/applications/02-track-grants.md`

| Line | Current Text | Should Be | Category |
|------|-------------|-----------|----------|
| 43 | "3-5 SKELETON -> PROTOTYPE elevations per quarter" | Update -- no SKELETON repos remain; rephrase as future maintenance | Stale SKELETON reference |

---

## SUMMARY BY CATEGORY

| Category | Count of Stale References |
|----------|--------------------------|
| "91 repos" -> 97 | ~15 instances |
| "89 repos" -> 97 | ~10 instances |
| "88 repos" -> 97 | ~3 instances |
| "81 repos" -> 97 | ~2 instances |
| "84 ACTIVE" -> 90 | ~5 instances |
| "82 ACTIVE/PRODUCTION" -> 90 | ~5 instances |
| ORGAN-I 19 -> 20 | ~4 instances |
| ORGAN-II 26/28 -> 30 | ~4 instances |
| ORGAN-III 24 -> 27 | ~5 instances |
| ORGAN-VI 3 -> 4 | ~1 instance |
| Meta 2 -> 3 | ~2 instances |
| "2 DESIGN_ONLY" -> 0 | ~2 instances |
| "5 ORGAN-II SKELETON" -> 0 | ~3 instances |
| PRODUCTION terminology -> ACTIVE | ~10 instances |
| Very old counts (66, 18, 23, 22, 81, 335K) | ~6 instances (00-portfolio-brief.md) |

**Total stale references needing correction: ~77 across 15 active files**

### Priority Order for Fixes

1. **CLAUDE.md** -- agents read this first; stale counts here propagate errors
2. **README.md** -- public-facing; first thing external visitors see
3. **applications/shared/metrics-snapshot.md** -- feeds all application bundles
4. **applications/shared/system-overview.md** -- feeds all application bundles
5. **docs/applications/00-portfolio-brief.md** -- most severely stale (81 repos, 335K words)
6. **docs/strategy/there+back-again.md** -- omega roadmap, operational reference
7. **docs/strategy/sprint-catalog.md** -- meta-stale (its own correction notes are now outdated)
8. **docs/operations/operational-cadence.md** -- daily reference doc
9. **docs/operations/minimum-viable-operations.md** -- operator reference
10. **docs/operations/emergency-procedures.md** -- minor (billing calc)
11. **docs/governance/quarterly-sustainability-checklist.md** -- quarterly reference
12. **docs/evaluation/e2g-full-system-review.md** -- evaluation doc (many stale refs)
13. **docs/evaluation/e2g-action-items.md** -- minor (ORGAN-III count)
