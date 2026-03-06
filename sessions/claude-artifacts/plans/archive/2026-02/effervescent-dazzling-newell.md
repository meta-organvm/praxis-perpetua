# Plan: Phase 4 — The Green Wall Sprint

## Context

Phase 3 (completed 2026-02-12) validated 5 priority repos, fixed their CI, and updated the registry. But the system-wide picture reveals a much larger problem:

- **CI pass rate is 56%** — 33 passing vs 26 failing across 62 active repos
- **ORGAN-I is 94% red** — 15/16 repos with CI runs are failing
- **3 pending promotion obligations** remain undischarged from the Phase 4 state machine exercise
- **25 active repos** have DEPLOYED documentation but SKELETON/DESIGN_ONLY implementation

The Green Wall Sprint turns the GitHub Actions dashboard from a wall of red into a wall of green, converts 5 more SKELETON repos into working prototypes, discharges all promotion obligations, and standardizes community health across all 8 orgs. Doc 11 is explicit: *"The next artifact should be working code, not another evaluation document."*

**Target outcome:** CI pass rate from 56% → 95%+, 5 SKELETON→PROTOTYPE conversions, 3 promotion obligations discharged, issue templates across all 8 orgs, clean validation.

---

## Workstream A: CI Green Wall (26 Failing Workflows → Green)

### A.1 — Close Stale Dependency Bot PRs (15 min, TRIVIAL)
**Repos:** `mirror-mirror`, `public-record-data-scrapper`, `sovereign-ecosystem--real-estate-luxury`, `the-invisible-ledger` (all ORGAN-III)
**Action:** Close all open Dependabot/Renovate PRs that are failing CI:
```bash
gh pr list --repo organvm-iii-ergon/REPO --state open --json number --jq '.[].number' | xargs -I {} gh pr close {} --repo organvm-iii-ergon/REPO
```
**Also:** Fix `system-governance-framework` stale issue bot config (ORGAN-I).

### A.2 — Downgrade SKELETON Repos to Minimal CI (30 min, TRIVIAL)
**Repos with "Python CI" or "TypeScript CI" but no real code to test:**
- `a-recursive-root` (ORGAN-I) — replace ci-python.yml → ci-minimal.yml
- `cognitive-archaelogy-tribunal` (ORGAN-I) — same
- `example-generative-music` (ORGAN-II) — replace ci-typescript.yml → ci-minimal.yml

**Also investigate:** `cog-init-1-0-` and `collective-persona-operations` (ORGAN-I) — these run "Minimal CI" but still fail. Read their workflow logs to diagnose.

**ci-minimal.yml template:** Use the proven template from repos where Minimal CI passes (e.g., `example-choreographic-interface`).

**Deploy:** `gh api repos/ORG/REPO/contents/.github/workflows/ci.yml --method PUT`

### A.3 — Fix Flagship CI (1 hour, MODERATE)
Fix the 5 highest-visibility repos first:

| Repo | Org | Failing Workflow | Approach |
|------|-----|-----------------|----------|
| `recursive-engine--generative-entity` | organvm-i-theoria | Python CI | Read logs → fix deps/versions/SHA-pins |
| `agentic-titan` | organvm-iv-taxis | Python CI | Read logs → likely complex dep tree (Ray, etc.) |
| `metasystem-master` | organvm-ii-poiesis | Monorepo CI | Mixed Python+TS; fix both dep chains |
| `orchestration-start-here` | organvm-iv-taxis | Python CI | Read logs → script dep issue |
| `organvm-corpvs-testamentvm` | meta-organvm | Python CI | Read logs → path or dep issue |

**Pattern for each:**
1. `gh run list --repo ORG/REPO --limit 1 --json databaseId` → get run ID
2. `gh run view ID --repo ORG/REPO --log-failed` → read error
3. Diagnose (common: SHA-pin actions, wrong Python version, missing requirements.txt)
4. Fix workflow file or add missing dependency files
5. Deploy via `gh api` → verify CI re-runs green

### A.4 — Fix Remaining PRODUCTION/PROTOTYPE CI (1.5 hours, MODERATE)
Remaining repos with actual code but broken CI:

| Repo | Org | Status | CI Type |
|------|-----|--------|---------|
| `organon-noumenon--ontogenetic-morphe` | organvm-i-theoria | PRODUCTION | Python CI |
| `narratological-algorithmic-lenses` | organvm-i-theoria | PRODUCTION | Python CI |
| `linguistic-atomization-framework` | organvm-i-theoria | PRODUCTION | Python CI |
| `my-knowledge-base` | organvm-i-theoria | PRODUCTION | CI |
| `sema-metra--alchemica-mundi` | organvm-i-theoria | PRODUCTION | TypeScript CI |
| `radix-recursiva-solve-coagula-redi` | organvm-i-theoria | PRODUCTION | Semgrep |
| `reverse-engine-recursive-run` | organvm-i-theoria | PROTOTYPE | Python CI |
| `auto-revision-epistemic-engine` | organvm-i-theoria | PROTOTYPE | Python CI |
| `a-i-council--coliseum` | organvm-ii-poiesis | PROTOTYPE | Python CI |
| `life-my--midst--in` | organvm-iii-ergon | PRODUCTION | Performance Tests |
| `my--father-mother` | organvm-iii-ergon | PROTOTYPE | Python CI |

**Same pattern as A.3.** Parallelize by launching subagents per batch of 3-4 repos.

### A.5 — Document Expected Failures (5 min, TRIVIAL)
`tab-bookmark-manager` CI/CD pipeline fails on Docker auth — this is expected (no secrets configured). The TS unit tests already pass. No action needed beyond documenting.

**Workstream A verification:** `gh run list --repo ORG/REPO --limit 1 --json conclusion` returns `success` for all 62 active repos.

---

## Workstream B: SKELETON → PROTOTYPE Conversions (5 Repos)

Selected by cross-referencing portfolio relevance, organ representation, and dependency relationships. These 5 have the highest impact-per-effort:

### B.1 — `system-governance-framework` (ORGAN-I, CRITICAL relevance)
**Why:** Foundational governance repo; other repos depend on its concepts. Theory organ should have executable code.
**Implementation:**
```
src/__init__.py, rules.py, validator.py, promotion.py, audit.py
data/governance-rules.json
tests/test_rules.py, test_validator.py, test_promotion.py
pyproject.toml
.github/workflows/ci.yml (upgrade from ci-minimal to ci-python)
```
**Registry:** SKELETON → PROTOTYPE

### B.2 — `showcase-portfolio` (ORGAN-II, CRITICAL relevance)
**Why:** A portfolio aggregation repo that is itself SKELETON is the epitome of the P1 credibility gap. First thing a grant reviewer sees in ORGAN-II.
**Implementation:**
```
src/__init__.py, gallery.py, collector.py, renderer.py
data/works.json
templates/index.html
tests/test_gallery.py, test_collector.py
pyproject.toml
.github/workflows/ci.yml (upgrade to ci-python)
```
**Registry:** SKELETON → PROTOTYPE

### B.3 — `case-studies-methodology` (ORGAN-II, CRITICAL relevance)
**Why:** Case studies are the evidence layer grant reviewers need.
**Implementation:**
```
case-studies/template.md, 01-interactive-installation.md
src/__init__.py, parser.py, cross_reference.py, export.py
tests/test_parser.py, test_export.py
pyproject.toml
.github/workflows/ci.yml (upgrade to ci-python)
```
**Registry:** SKELETON → PROTOTYPE

### B.4 — `petasum-super-petasum` (ORGAN-IV, HIGH relevance)
**Why:** Cross-org governance tooling. ORGAN-IV should have executable infrastructure.
**Implementation:**
```
src/__init__.py, tracker.py, governance.py, report.py
tests/test_tracker.py, test_governance.py
pyproject.toml
.github/workflows/ci.yml (upgrade to ci-python)
```
**Registry:** SKELETON → PROTOTYPE

### B.5 — `artist-toolkit-and-templates` (ORGAN-II, HIGH relevance)
**Why:** Practical creative infrastructure. Supports the artist-as-system narrative.
**Implementation:**
```
templates/grant-application/template.md, project-proposal/template.md
src/__init__.py, template_engine.py, prospector.py
tests/test_template_engine.py
pyproject.toml
.github/workflows/ci.yml (upgrade to ci-python)
```
**Registry:** SKELETON → PROTOTYPE

**Workstream B verification:** Each repo has ≥10 passing tests, CI green, `implementation_status` updated in registry.

---

## Workstream C: Structural Improvements

### C.1 — Discharge 3 Promotion Obligations (P5)

From `docs/implementation/phase-4-state-machine-log.md`:

| Obligation | Type | Target Org | Action |
|-----------|------|-----------|--------|
| `art-from--narratological-algorithmic-lenses` | repo creation | organvm-ii-poiesis | Create repo, README, ci-minimal.yml, LICENSE |
| `art-from--auto-revision-epistemic-engine` | repo creation | organvm-ii-poiesis | Create repo, README, ci-minimal.yml, LICENSE |
| "Why AI Function Calling Needs Ontological Grounding" | essay (~3K words) | organvm-v-logos | Write essay, deploy to `public-process/essays/subsidiary/17-ontological-function-calling.md` |

**For repo creations:**
1. `gh repo create organvm-ii-poiesis/REPO_NAME --public --description "DESCRIPTION"`
2. Deploy README, LICENSE, .gitignore, ci-minimal.yml via `gh api`
3. Set topics via `gh api repos/ORG/REPO/topics --method PUT`
4. Add to `registry-v2.json` (SKELETON, DEPLOYED)
5. Update `total_repos` (81→83), ORGAN-II `repository_count` (27→29)

**For essay:** Follow the 6-point outline in phase-4-state-machine-log.md lines 49-54. Deploy via `gh api`.

### C.2 — Deploy Issue Templates to 7 Orgs (1 hour, TRIVIAL)
**Target orgs:** organvm-i-theoria, organvm-iii-ergon, organvm-iv-taxis, organvm-v-logos, organvm-vi-koinonia, organvm-vii-kerygma, meta-organvm

**Deploy to each org's `.github` repo:**
```
.github/ISSUE_TEMPLATE/bug_report.md
.github/ISSUE_TEMPLATE/feature_request.md
.github/ISSUE_TEMPLATE/documentation.md
.github/ISSUE_TEMPLATE/config.yml
.github/PULL_REQUEST_TEMPLATE.md
```

### C.3 — Enhance Sustainability Checklist (15 min, TRIVIAL)
**File:** `docs/governance/quarterly-sustainability-checklist.md`
**Add:** CI health query across all orgs (the command pattern from our CI survey), implementation status drift comparison formula.

---

## Workstream D: Registry & Validation

### D.1 — Update `registry-v2.json`
- 5 repos: SKELETON → PROTOTYPE (Workstream B)
- 2 new repos added (Workstream C.1)
- Update `total_repos`: 81 → 83
- Update `total_repos_note`
- Update ORGAN-II `repository_count`: 27 → 29
- Recalculate `implementation_status_distribution`: PRODUCTION 32, PROTOTYPE **15** (+5), SKELETON **14** (-5), DESIGN_ONLY 20, plus 2 new SKELETON = SKELETON **16**
- Add `promotion_obligations` tracking to relevant entries
- Update `last_validated` dates

### D.2 — Re-run All Validation Scripts
```bash
python scripts/v1-v2-link-tbd-audit.py
python scripts/v3-registry-reconciliation.py
python scripts/v4-dependency-validation.py
python scripts/v5-v6-constitution-organ-checks.py
```
All should pass. Fix v1-v2 pass logic if needed (exclude confirmed false-positive TBD markers).

### D.3 — Commit All Local Changes
Stage and commit changes to this repo (registry, sustainability checklist, any script fixes).

---

## Execution Sequence

```
Phase 1: Quick Wins (2 hours)
  A.1  Close stale Dependabot PRs              15 min
  A.2  Downgrade SKELETON repos to ci-minimal  30 min
  C.2  Deploy issue templates to 7 orgs        1 hour

Phase 2: CI Fixes — Flagships (2.5 hours)
  A.3  Fix 5 flagship CI workflows             1 hour
  A.4  Fix remaining 11 PRODUCTION/PROTOTYPE   1.5 hours

Phase 3: SKELETON Conversions (6-8 hours)
  B.1  system-governance-framework             1.5 hours
  B.2  showcase-portfolio                      1.5 hours
  B.3  case-studies-methodology                1.5 hours
  B.4  petasum-super-petasum                   1.5 hours
  B.5  artist-toolkit-and-templates            1 hour

Phase 4: Promotion Obligations (3 hours)
  C.1a Create art-from--narratological-*       45 min
  C.1b Create art-from--auto-revision-*        45 min
  C.1c Write ontological function calling essay 1.5 hours

Phase 5: Registry & Validation (2 hours)
  C.3  Enhance sustainability checklist        15 min
  D.1  Update registry-v2.json                 45 min
  D.2  Re-run validation scripts               30 min
  D.3  Commit local changes                    15 min
```

Each phase produces independently valuable results. After Phase 2 alone, the CI dashboard transforms from 56% green to ~95%+ green.

---

## Expected Outcomes

| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| CI passing | 33/62 (53%) | ~60/62 (97%) | +27 |
| PROTOTYPE repos | 10 | 15 | +5 |
| SKELETON repos | 19 | 16 | -3 |
| Total repos | 81 | 83 | +2 |
| Promotion obligations pending | 3 | 0 | -3 |
| Orgs with issue templates | 1 | 8 | +7 |
| Validation scripts passing | 3/5 | 5/5 | +2 |

---

## Critical Files

| File | Action |
|------|--------|
| `registry-v2.json` | UPDATE — 5 status changes, 2 new repos, distribution recalc |
| `docs/governance/quarterly-sustainability-checklist.md` | UPDATE — add CI health section |
| Remote: ~26 CI workflow files across 8 orgs | FIX/REPLACE via `gh api` |
| Remote: 5 repos' `src/`, `tests/`, `pyproject.toml` | CREATE via `gh api` (Workstream B) |
| Remote: 2 new repos in organvm-ii-poiesis | CREATE via `gh repo create` + `gh api` |
| Remote: 1 essay in organvm-v-logos/public-process | CREATE via `gh api` |
| Remote: 7 orgs' .github repos issue templates | CREATE via `gh api` |

## Deployment Pattern
All remote changes use `gh api repos/ORG/REPO/contents/PATH --method PUT` with base64-encoded content (SSH passphrase constraint). Use `gh repo create` for new repos.

## Verification
1. Every CI-fixed repo shows green badge: `gh run list --repo ORG/REPO --limit 1 --json conclusion`
2. All 5 converted repos have ≥10 passing pytest tests
3. All validation scripts pass with 0 errors
4. Registry counts match actual GitHub state
5. Issue templates visible when clicking "New Issue" in any org's repos
