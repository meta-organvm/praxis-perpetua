# ORGANVM: Complete Organ Interaction Implementation + Hierarchical Git Strategy

## Context

The ORGANVM eight-organ system has a well-designed interaction model (6 edges, quality gates, event dispatch, seed.yaml contracts) and ~99 independent git repos — but the interactions are mostly unimplemented (9 of 10 agents in DESIGN_PHASE) and there is zero git coordination between repos. The `~/world` root was decommissioned; env vars are stale. Two registries have diverged. This plan completes the implementation end-to-end and adds a three-level hierarchical git tracking system.

**Two deliverables:**
1. **Organ interaction implementation** — make all 6 edges work with real GitHub Actions workflows, quality gates, and fallback polling
2. **Hierarchical git tracking** — per-organ superprojects with submodules + workspace manifest + `organvm git` CLI

---

## PART A: ORGAN INTERACTION IMPLEMENTATION

### A1. Registry Consolidation (blocks everything)

**Problem:** `orchestration-start-here/registry.json` (91 repos) vs `organvm-corpvs-testamentvm/registry-v2.json` (100 repos). All ORGAN-IV workflows fetch the stale copy.

**Actions:**
- Replace `orchestration-start-here/registry.json` with a redirect stub (`{"_redirect": "Use registry-v2.json in organvm-corpvs-testamentvm"}`)
- Create `orchestration-start-here/scripts/fetch-registry.sh` — fetches from `meta-organvm/organvm-corpvs-testamentvm/main/registry-v2.json` with retry and stub detection
- Update all 5 ORGAN-IV workflows to use `fetch-registry.sh` + `registry-v2.json`
- Add `registry-sync-check.yml` (Monday 05:00 UTC) to detect future drift

**Files to modify:**
- `~/Workspace/organvm-iv-taxis/orchestration-start-here/registry.json` (replace with stub)
- `~/Workspace/organvm-iv-taxis/orchestration-start-here/.github/workflows/registry-health-audit.yml`
- `~/Workspace/organvm-iv-taxis/orchestration-start-here/.github/workflows/orchestrator-agent.yml`
- `~/Workspace/organvm-iv-taxis/orchestration-start-here/.github/workflows/promote-repo.yml`
- `~/Workspace/organvm-iv-taxis/orchestration-start-here/.github/workflows/publish-process.yml`
- `~/Workspace/organvm-iv-taxis/orchestration-start-here/.github/workflows/promotion-recommender.yml`

**New files:**
- `~/Workspace/organvm-iv-taxis/orchestration-start-here/scripts/fetch-registry.sh`
- `~/Workspace/organvm-iv-taxis/orchestration-start-here/.github/workflows/registry-sync-check.yml`

### A2. Event Catalog

Create `orchestration-start-here/docs/event-catalog.yaml` — canonical list of all 10 event types:

| Event | Edge | Producer | Consumer |
|-------|------|----------|----------|
| `theory.candidate` | I→II | registry push watcher | promote-repo.yml |
| `art.ready-commercialize` | II→III | ORGAN-II issue label | promote-repo.yml |
| `commerce.publish-requested` | III→V | ORGAN-III issue label | publish-process.yml |
| `essay.published` | V→VI, V→VII | essay-monitor.yml | ORGAN-VI receiver, ORGAN-VII RSS |
| `community.milestone` | VI→VII | ORGAN-VI issue label | dispatch-receiver.yml |
| `marketing.quarterly-signals` | VII→I | quarterly cron | theory-input-handler.yml |
| `governance.updated` | cross-cutting | registry push | all organs |
| `health-audit.completed` | cross-cutting | weekly audit | all organs |
| `promotion.completed` | cross-cutting | promote-repo.yml | ORGAN-V, ORGAN-VII |
| `distribution.completed` | cross-cutting | dispatch-receiver.yml | ORGAN-IV logging |

**New file:** `~/Workspace/organvm-iv-taxis/orchestration-start-here/docs/event-catalog.yaml`

### A3. Edge 1: ORGAN-I → ORGAN-II (theory.candidate)

**Current:** 2 promotions manually fulfilled. `promote-repo.yml` exists but only fires on `issue_comment`.

**Changes:**
- Add `repository_dispatch` trigger to `promote-repo.yml` for `theory.candidate` and `art.ready-commercialize` event types
- Create `handle-dispatch-promotion.py` — processes dispatch payloads, checks gates (documentation-complete, promotion-status, no-back-edges), opens tracking issue or executes promotion
- Create `theory-to-art-watcher.yml` in `organvm-corpvs-testamentvm` — fires on registry-v2.json push + Tuesday 10:00 UTC fallback; scans for ORGAN-I CANDIDATE repos and dispatches to ORGAN-IV
- Extend `promotion-recommender.yml` with unfulfilled I→II check

**New files:**
- `~/Workspace/organvm-iv-taxis/orchestration-start-here/scripts/handle-dispatch-promotion.py`
- `~/Workspace/meta-organvm/organvm-corpvs-testamentvm/.github/workflows/theory-to-art-watcher.yml`

**Modify:** `promote-repo.yml`, `promotion-recommender.yml`

### A4. Edge 2: ORGAN-II → ORGAN-III (art.ready-commercialize)

**Trigger:** Issue labeled `ready-for-commercialization` in ORGAN-II repos.

**New file:** `art-to-commerce.yml` workflow template — added to ORGAN-II flagships (`metasystem-master`, `a-mavs-olevm`). Checks gates (documentation-complete, security-review label), dispatches to ORGAN-IV. Falls back to issue comment if PAT missing.

**Receiver:** Already handled by A3's `handle-dispatch-promotion.py` (shared script for both Edge 1 and Edge 2).

### A5. Edge 3: ORGAN-III → ORGAN-V (commerce.publish-requested)

**Current:** `publish-process.yml` works when `@orchestration create essay` is typed on a labeled issue. Missing: automated trigger from ORGAN-III.

**New file:** `commerce-to-logos.yml` template for ORGAN-III flagships — creates orchestration issue in ORGAN-IV when `publish-process` label is applied.

**Modify:** `publish-process.yml` — add `audit-clean` gate (checks latest health audit conclusion) and `synthesis-approved` label gate.

### A6. Edge 4: ORGAN-V → ORGAN-VI (essay.published)

**Current:** `essay-monitor.yml` detects essays and creates `ready-to-distribute` issues but only targets ORGAN-VII. ORGAN-VI receives nothing.

**Changes:**
- Modify `essay-monitor.yml` to also dispatch `essay.published` to ORGAN-VI
- Create `essay-to-community.yml` in `organvm-vi-koinonia/.github` — receives dispatch + daily 11:00 UTC fallback poll; creates tracking issues in `reading-group-curriculum` for curator review

**New file:** `~/Workspace/organvm-vi-koinonia/.github/.github/workflows/essay-to-community.yml`
**Modify:** `~/Workspace/organvm-iv-taxis/orchestration-start-here/.github/workflows/essay-monitor.yml`

### A7. Edge 5: ORGAN-VI → ORGAN-VII (community.milestone)

**Trigger:** `community-approved` label on an issue that has been open 7+ days (RFC gate).

**New files:**
- `community-to-kerygma.yml` in `organvm-vi-koinonia/.github` — validates RFC gate (7-day age) + quality-threshold label, dispatches to ORGAN-VII
- `community-milestone.md` template in `organvm-vii-kerygma/announcement-templates/templates/community/`

**Modify:** ORGAN-VII `dispatch-receiver.yml` — add `community.milestone` to event types list

### A8. Edge 6: ORGAN-VII → ORGAN-I (marketing.quarterly-signals)

**Design:** Weak/dashed edge. Quarterly cron collects signals; human writes synthesis; `synthesis-complete` label triggers dispatch.

**New files:**
- `quarterly-feedback.yml` in ORGAN-VII — quarterly cron (1st Mon of Jan/Apr/Jul/Oct), collects distribution reports + analytics, creates synthesis-needed issue
- `quarterly-synthesis-dispatch.yml` in ORGAN-VII — fires on `synthesis-complete` label, dispatches to ORGAN-IV
- `theory-input-handler.yml` in `orchestration-start-here` — receives `marketing.quarterly-signals`, opens theory-input issue in ORGAN-I

---

## PART B: HIERARCHICAL GIT TRACKING

### B1. Fix Stale Environment

**Modify `~/.zshenv` via chezmoi (`~/dotfiles/dot_zshenv`):**
- Remove: `WORLD_ROOT`, `AUDIT_ROOT`, `REALMS`, `ORG_POLICY`, `DEFAULT_ORG_UNIT`
- Fix: `ORG_I` through `ORG_VII` → actual GitHub org names (`organvm-i-theoria`, etc.)
- Add: `ORG_META=meta-organvm`, `ORGANVM_WORKSPACE_DIR=$HOME/Workspace`, `ORGANVM_CORPUS_DIR=$ORGANVM_WORKSPACE_DIR/meta-organvm/organvm-corpvs-testamentvm`

### B2. Initialize Stub Repos

5 non-git directories need `git init` + `gh repo create` before becoming submodules:
- `organvm-i-theoria/scalable-lore-expert`
- `organvm-ii-poiesis/life-betterment-simulation`
- `organvm-ii-poiesis/shared-remembrance-gateway`
- `organvm-ii-poiesis/universal-waveform-explorer`
- `organvm-iii-ergon/card-trade-social`

For each: `git init -b main`, `git add seed.yaml`, initial commit, `gh repo create --private --push`.

### B3. Three-Level Hierarchy Design

```
~/Workspace/                              Level 0: workspace-manifest.json (NOT a git repo)
  organvm-i-theoria/                      Level 1: organ superproject (git repo)
    .git/ .gitmodules .gitignore
    CLAUDE.md (committed)
    recursive-engine--generative-entity/  Level 2: individual repos (submodules)
    auto-revision-epistemic-engine/
    ...
  organvm-ii-poiesis/                     Level 1: organ superproject
  ...
```

**Key decisions:**
- Workspace root is NOT a git repo (avoids 100-submodule pathological status)
- Organ superprojects track only `.gitmodules`, `.gitignore`, `CLAUDE.md`, `README-superproject.md`
- Superproject commits are rare and meaningful (sprint snapshots, promotions) — NOT triggered by every child repo push
- No feature branches on superprojects; direct push to `main` only
- `git submodule update --remote` is NOT default; pointer advancement is deliberate via `organvm git sync-organ`

### B4. Create Superproject GitHub Repos

9 new private repos (one per organ + 4444J99):
- `organvm-i-theoria/organvm-i-theoria--superproject`
- `organvm-ii-poiesis/organvm-ii-poiesis--superproject`
- `organvm-iii-ergon/organvm-iii-ergon--superproject`
- `organvm-iv-taxis/organvm-iv-taxis--superproject`
- `organvm-v-logos/organvm-v-logos--superproject`
- `organvm-vi-koinonia/organvm-vi-koinonia--superproject`
- `organvm-vii-kerygma/organvm-vii-kerygma--superproject`
- `meta-organvm/meta-organvm--superproject`
- `4444j99/workspace--superproject`

### B5. Organ Superproject Initialization (per organ)

For each organ directory:

1. `git init -b main` (doesn't affect existing sub-repos)
2. Write `.gitmodules` registering all child repos as submodules
3. Write `.gitignore` (`*` with allowlist for `.gitmodules`, `.gitignore`, `CLAUDE.md`, `README-superproject.md`)
4. Register each repo in `.git/config` + `git add <repo>` to stage gitlinks
5. `git add .gitmodules .gitignore CLAUDE.md`, commit, set remote, push

**Submodule registration for existing repos** (no clone needed):
```bash
git config --file .git/config "submodule.<name>.url" "<url>"
git config --file .git/config "submodule.<name>.active" "true"
git add <repo-dir>  # stages gitlink (mode 160000)
```

**Initialization order:** META (5 repos) → IV (6) → V, VI, VII (4-5 each) → I (19) → III (25) → II (30)

### B6. Workspace Manifest

`~/Workspace/workspace-manifest.json` — static JSON listing all organ superproject remotes, non-organ dirs, and pending stubs. Also committed into `organvm-corpvs-testamentvm/` as a governed artifact.

### B7. `organvm git` CLI Module

New module: `meta-organvm/organvm-engine/src/organvm_engine/git/`

```
git/
  __init__.py
  superproject.py   ← init_superproject(), add_submodule(), sync_organ()
  reproduce.py      ← reproduce_workspace(), clone_organ()
  status.py         ← show_drift(), diff_pinned()
```

**New CLI commands:**
```
organvm git init-superproject --organ {I|II|III|IV|V|VI|VII|META}
organvm git add-submodule --organ X --repo <name>
organvm git sync-organ --organ X [--message "Sprint XXXX"]
organvm git sync-all [--dry-run]
organvm git status [--organ X]
organvm git reproduce-workspace [--organ X] [--shallow] [--manifest <path>]
organvm git diff-pinned [--organ X]
```

Reads organ membership from `registry-v2.json`. Reuses `ORGAN_ORGS` list from `seed/discover.py`.

**Add to:** `meta-organvm/organvm-engine/src/organvm_engine/cli.py` (extend dispatch table with `("git", "init-superproject")`, etc.)

### B8. CI for Superprojects

Each superproject gets `validate-submodules.yml` — verifies all submodule remote URLs are reachable on push to main. Lightweight; does not clone child repos.

---

## EXECUTION SEQUENCE

### Phase 1: Foundation
1. Fix `~/.zshenv` via chezmoi
2. Retire `orchestration-start-here/registry.json` with stub
3. Create `fetch-registry.sh`
4. Update 5 ORGAN-IV workflows to use `registry-v2.json`
5. Create `registry-sync-check.yml`
6. Create `event-catalog.yaml`
7. **Verify:** All ORGAN-IV workflows report 100 repos. Sync check finds no drift.

### Phase 2: Stubs + Superproject Tooling
1. `git init` + `gh repo create` for 5 stub directories
2. `gh repo create` 9 superproject remotes
3. Implement `organvm_engine/git/` module (superproject.py, reproduce.py, status.py)
4. Add `git` command group to `cli.py`
5. Write tests for git module
6. **Verify:** `organvm git init-superproject --organ META` works end-to-end.

### Phase 3: Initialize All Superprojects
1. Run `organvm git init-superproject` for each organ (META → IV → V,VI,VII → I → III → II)
2. Push each to its GitHub remote
3. Create `workspace-manifest.json`
4. Add `validate-submodules.yml` to each superproject
5. **Verify:** `git submodule status` in each organ dir shows all repos with SHAs. `organvm git status` shows no drift.

### Phase 4: Edge 1 + Edge 3 (build on existing workflows)
1. Extend `promote-repo.yml` with `repository_dispatch` trigger
2. Create `handle-dispatch-promotion.py`
3. Create `theory-to-art-watcher.yml`
4. Create `commerce-to-logos.yml` template
5. Extend `publish-process.yml` with new gates
6. Extend `promotion-recommender.yml` with unfulfilled checks
7. **Verify:** Push an ORGAN-I repo to CANDIDATE in registry → tracking issue appears. Apply `publish-process` label in ORGAN-III → orchestration issue created.

### Phase 5: Edges 2, 4, 5
1. Create `art-to-commerce.yml` for ORGAN-II flagships
2. Modify `essay-monitor.yml` to dispatch to ORGAN-VI
3. Create `essay-to-community.yml` for ORGAN-VI
4. Create `community-to-kerygma.yml` for ORGAN-VI
5. Add `community.milestone` to ORGAN-VII dispatch-receiver
6. Create community milestone template
7. **Verify:** Apply labels and confirm dispatches reach intended receivers; fallback polls create issues.

### Phase 6: Edge 6 (Feedback Loop)
1. Create `quarterly-feedback.yml` in ORGAN-VII
2. Create `quarterly-synthesis-dispatch.yml` in ORGAN-VII
3. Create `theory-input-handler.yml` in ORGAN-IV
4. **Verify:** Manual `workflow_dispatch` of quarterly-feedback creates issue. Adding `synthesis-complete` dispatches to ORGAN-IV.

### Phase 7: Cross-Organ Integration Testing
1. Run `organvm governance audit` — should pass
2. Run `organvm seed validate` — all seeds valid
3. Run `organvm git status` — all organs tracked
4. Run `organvm git sync-all --dry-run` — shows what would be committed
5. End-to-end: promote an ORGAN-I repo to CANDIDATE → art-from-- repo created in ORGAN-II → ORGAN-II superproject updated with new submodule

---

## ERROR HANDLING DESIGN

| Failure Mode | Response |
|---|---|
| Gate fails (automated check) | Comment on issue listing failed gates. Do not execute. Human re-triggers. |
| Event missed (dispatch not received) | Fallback scheduled workflow catches within 24-48h. Creates same tracking issue. |
| Dispatch API error (GitHub outage) | Create local issue in source repo via `GITHUB_TOKEN`. Body includes error + retry instructions. |
| PAT missing for cross-org dispatch | Degrade to in-repo issue creation with manual instructions. |
| Submodule SHA drift | `organvm git status` reports drift. `organvm git sync-organ` advances pointers. |

**Idempotency:** All dispatch workflows check for existing tracking issues before creating new ones (search by label + title prefix).

---

## FULL FILE INVENTORY

### New files to create (Part A — Interactions)

| File | Repo |
|------|------|
| `scripts/fetch-registry.sh` | `orchestration-start-here` |
| `scripts/handle-dispatch-promotion.py` | `orchestration-start-here` |
| `.github/workflows/registry-sync-check.yml` | `orchestration-start-here` |
| `.github/workflows/theory-input-handler.yml` | `orchestration-start-here` |
| `docs/event-catalog.yaml` | `orchestration-start-here` |
| `.github/workflows/theory-to-art-watcher.yml` | `organvm-corpvs-testamentvm` |
| `.github/workflows/art-to-commerce.yml` | `organvm-ii-poiesis/metasystem-master` + `a-mavs-olevm` |
| `.github/workflows/commerce-to-logos.yml` | `organvm-iii-ergon/public-record-data-scrapper` |
| `.github/workflows/essay-to-community.yml` | `organvm-vi-koinonia/.github` |
| `.github/workflows/community-to-kerygma.yml` | `organvm-vi-koinonia/.github` |
| `.github/workflows/quarterly-feedback.yml` | `organvm-vii-kerygma/.github` |
| `.github/workflows/quarterly-synthesis-dispatch.yml` | `organvm-vii-kerygma/.github` |
| `templates/community/community-milestone.md` | `organvm-vii-kerygma/announcement-templates` |

### New files to create (Part B — Git)

| File | Location |
|------|----------|
| `.git/`, `.gitmodules`, `.gitignore`, `README-superproject.md` | Each of 9 organ directories |
| `workspace-manifest.json` | `~/Workspace/` + `organvm-corpvs-testamentvm/` |
| `src/organvm_engine/git/__init__.py` | `organvm-engine` |
| `src/organvm_engine/git/superproject.py` | `organvm-engine` |
| `src/organvm_engine/git/reproduce.py` | `organvm-engine` |
| `src/organvm_engine/git/status.py` | `organvm-engine` |
| `.github/workflows/validate-submodules.yml` | Each superproject GitHub repo |

### Files to modify

| File | Change |
|------|--------|
| `~/dotfiles/dot_zshenv` | Remove stale WORLD_ROOT; fix ORG vars; add ORGANVM_WORKSPACE_DIR |
| `orchestration-start-here/registry.json` | Replace with redirect stub |
| `orchestration-start-here/.github/workflows/promote-repo.yml` | Add `repository_dispatch` trigger |
| `orchestration-start-here/.github/workflows/publish-process.yml` | Add audit-clean + synthesis gates |
| `orchestration-start-here/.github/workflows/essay-monitor.yml` | Add ORGAN-VI dispatch |
| `orchestration-start-here/.github/workflows/registry-health-audit.yml` | Use fetch-registry.sh |
| `orchestration-start-here/.github/workflows/orchestrator-agent.yml` | Use fetch-registry.sh |
| `orchestration-start-here/.github/workflows/promotion-recommender.yml` | Use fetch-registry.sh + unfulfilled checks |
| `organvm-vii-kerygma/.github/workflows/dispatch-receiver.yml` | Add community.milestone type |
| `organvm-engine/src/organvm_engine/cli.py` | Add git command group |
| `organvm-engine/pyproject.toml` | (optional) Add gitpython dependency |
| `organvm-corpvs-testamentvm/registry-v2.json` | Add superproject_remote field per organ |

### New GitHub repos (9 superprojects + up to 5 stubs)

All private. Created via `gh repo create`.

---

## KEY EXISTING CODE TO REUSE

- `organvm_engine/dispatch/payload.py` — `create_payload()` for constructing dispatch events (all new workflows should use this instead of hand-rolling JSON)
- `organvm_engine/governance/dependency_graph.py` — `validate_dependencies()` for the no-back-edges gate
- `organvm_engine/governance/state_machine.py` — `check_transition()` for promotion validation
- `organvm_engine/seed/discover.py` — `ORGAN_ORGS` list + `DEFAULT_WORKSPACE` + traversal pattern (reuse in git module)
- `organvm_engine/dispatch/cascade.py` — BFS ordering for `organvm git sync-all` (topological sync order)
- `organvm_engine/registry/loader.py` — `load_registry()` + `DEFAULT_REGISTRY_PATH`
- `orchestration-start-here/scripts/validate-deps.py` — already deployed, called by gate checks

---

## VERIFICATION PLAN

After each phase, run these checks:

| Phase | Verification |
|-------|-------------|
| 1 (Foundation) | `organvm registry list` shows 100 repos. `registry-sync-check.yml` passes. |
| 2 (Tooling) | `organvm git init-superproject --organ META` completes. `git submodule status` in META shows 5-6 repos. |
| 3 (Superprojects) | `organvm git status` reports all 9 organs tracked. `workspace-manifest.json` lists all remotes. `organvm git reproduce-workspace --organ META --shallow` works on a fresh directory. |
| 4 (Edges 1+3) | Push CANDIDATE to registry → dispatch fires → tracking issue in ORGAN-IV. Apply `publish-process` label → orchestration issue created. |
| 5 (Edges 2+4+5) | Apply labels → dispatches reach receivers. Fallback polls fire on schedule. |
| 6 (Edge 6) | Manual workflow_dispatch → quarterly issue created. `synthesis-complete` label → dispatch to ORGAN-IV → theory-input issue in ORGAN-I. |
| 7 (Integration) | `organvm governance audit` passes. `organvm seed validate` passes. Full promotion flow: ORGAN-I CANDIDATE → ORGAN-II art-from-- repo → superproject updated. |
