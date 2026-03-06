# Plan: Redesign 6 Disabled Workflows for Useful Operation

## Context

Six workflows were disabled because they created branches and PRs on every run with no one merging them, accumulating 96 orphaned branches and 61 stale PRs. Rather than leaving them disabled, this plan redesigns each to work properly.

**Root cause fix across all 6:** Replace the branch+PR pattern with direct-to-main commits using `[skip ci]`. This is an established pattern already used by `workflow-metrics.yml`, `safeguard-7-staggered-scheduling.yml`, and others in this repo.

**Common direct-to-main commit block** (used in every workflow):
```yaml
git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"
git add <specific files>
if git diff --staged --quiet; then
  echo "No changes to commit"
else
  git commit -m "<type>(<scope>): <message> [skip ci]"
  git push
fi
```

---

## Workflow 1: `reset-quotas.yml` (simplest)

**File:** `.github/workflows/reset-quotas.yml.disabled` → `.github/workflows/reset-quotas.yml`

**What it does:** Runs `quota_manager.py reset_quotas` to reset daily/monthly API subscription usage counters in `.github/subscriptions.json`.

**Changes:**
- Remove branch creation + PR creation (lines 33-49)
- Replace with direct-to-main commit of `.github/subscriptions.json` only (drop unused `task_queue.json` staging)
- Change concurrency group from `${{ github.workflow }}` to explicit `reset-quotas`
- Keep: daily midnight UTC schedule, manual trigger, quota_manager.py call

**Result:** ~25-line workflow. Quotas reset daily, committed directly.

---

## Workflow 2: `badge-management.yml`

**File:** `.github/workflows/badge-management.yml.disabled` → `.github/workflows/badge-management.yml`

**What it does:** Detects repo languages/features, generates shields.io badges, updates README between `<!-- BADGES:START -->` / `<!-- BADGES:END -->` markers.

**Changes:**
- Remove `pull_request` trigger and `master` branch references
- Remove BOTH PR creation mechanisms (gh CLI step at lines 336-375 AND peter-evans action at lines 377-407)
- Remove `pull-requests: write` and `issues: read` permissions
- Replace with direct-to-main commit of `README.md`
- Keep: config loading from `.github/badge-config.yml`, language/feature detection, badge generation, sed-based README update, `workflow_call` trigger, `workflow_dispatch` with `force_update`

**Result:** Same detection + badge generation, committed directly. No duplicate PR mechanisms.

---

## Workflow 3: `metrics-collection.yml`

**File:** `.github/workflows/metrics-collection.yml.disabled` → `.github/workflows/metrics-collection.yml`

**What it does:** Queries GitHub API for workflow run statistics, writes metrics JSON and markdown summary.

**Changes:**
- Reduce schedule from every 6 hours to daily (`30 5 * * *`)
- Remove peter-evans/create-pull-request action
- Remove broken cache hit analysis (N^3 API calls for unreliable data)
- Remove `python-dateutil` dependency (unused)
- Fix Python version from 3.11 to 3.12 (consistency)
- Rewrite inline Python to support historical data: load existing `metrics/workflow-metrics.json` as timestamped array, append new snapshot, prune entries >30 days old
- Fix broken `metrics-summary.md` generation (move into Python script)
- Add `mkdir -p metrics` before writing
- Replace PR with direct-to-main commit of `metrics/`

**Result:** Daily metrics collection with 30-day trend history, committed directly.

---

## Workflow 4: `daily-orchestrator.yml`

**File:** `.github/workflows/daily-orchestrator.yml.disabled` → `.github/workflows/daily-orchestrator.yml`

**What it does:** Reads `orchestration_tasks.json` for cron-scheduled tasks, deduplicates via `task_deduplicator.py`, dispatches target workflows per subscription config.

**Changes:**
- Remove 3 broken jobs: `process-task-queue` (dispatches nonexistent `process-queue.yml`), `consolidate-prs` (30-min sleep + nonexistent `daily-pr-consolidator.yml`), separate `cleanup` job
- Simplify from 6 jobs → 3 jobs: `check` → `orchestrate` → `summary`
- Fold cleanup (`task_deduplicator.py cleanup 7`) into `orchestrate` job as a final step
- Remove both separate PR creation steps (orchestration state + cleanup)
- Replace with single direct-to-main commit of `.github/task_state.json`
- Remove `pull-requests: write`, `issues: write` permissions
- Remove `wait_time_minutes` input (no longer waiting)
- Keep: `check-if-should-run` logic, `get_daily_tasks.py`, `task_deduplicator.py`, `force_run` input, croniter dependency

**Result:** Clean 3-job workflow. Dispatches tasks, updates state, summarizes — no sleeping, no fake consolidation, no missing workflow references.

---

## Workflow 5: `generate-pages-index.yml`

**File:** `.github/workflows/generate-pages-index.yml.disabled` → `.github/workflows/generate-pages-index.yml`

**What it does:** Queries GitHub API for all org repos, indexes walkthroughs/demos/deployments into `docs/_data/*.yml` for the GitHub Pages site.

**Changes:**
- Reduce schedule from every 6 hours to weekly (`0 6 * * 1` — Monday 6 AM UTC)
- Remove `yq` installation step — replace single usage with `python3 -c` for YAML parsing
- Remove `workflow_call` trigger (needs org-level API access, not useful as reusable)
- Remove branch+PR creation (lines 290-328)
- Remove downstream `build-pages-site.yml` trigger (Pages auto-rebuilds on main push)
- Add YAML string sanitization for repo descriptions (escape quotes)
- Replace with direct-to-main commit of `docs/_data/*.yml`
- Keep: org repo enumeration, walkthrough detection, demo link scanning, deployment config detection, `repository_dispatch` triggers, statistics file generation

**Result:** Weekly org catalog refresh, committed directly. Pages auto-deploys.

---

## Workflow 6: `demo-deployment.yml` (most change)

**File:** `.github/workflows/demo-deployment.yml.disabled` → `.github/workflows/demo-deployment.yml`
**New file:** `.github/workflows/reusable/demo-registration.yml`

**Current problem:** Entirely simulation — generates fake URLs, fake demo IDs, adds non-functional badges. No actual deployment.

**Redesign:** Convert to a **demo registration system**. Other org repos call the reusable workflow to register their live demos. The `.github` repo maintains the registry in `docs/_data/app-deployments.yml`.

**New reusable workflow** (`reusable/demo-registration.yml`):
- `workflow_call` inputs: `repository` (required), `demo_url` (required), `app_type` (optional, default 'auto'), `status` (optional, default 'active')
- Checks out the `.github` repo
- Upserts the entry in `docs/_data/app-deployments.yml` (update if repo exists, add if new, remove if status=removed)
- Direct-to-main commit

**Wrapper workflow** (`demo-deployment.yml`, replaces disabled file):
- `workflow_dispatch` only — manual trigger with inputs: repository, demo_url, app_type, status
- Calls the reusable workflow
- Keep app type detection logic as optional enrichment (run if `app_type=auto`)

**Remove:** All push triggers, all simulation code, README badge manipulation, peter-evans action, `issues: write` permission, most of `demo-config.yml` content

**Result:** Functional demo registry. Other repos can register demos; manual registration also available.

---

## Implementation Order

1. `reset-quotas.yml` — simplest, establishes pattern
2. `badge-management.yml` — straightforward PR removal
3. `metrics-collection.yml` — Python rewrite + new directory
4. `daily-orchestrator.yml` — structural simplification (6→3 jobs)
5. `generate-pages-index.yml` — moderate complexity, API optimization
6. `demo-deployment.yml` — architectural change (new reusable + wrapper)

Each workflow: `git mv` from `.yml.disabled` back to `.yml`, then edit in place.

## Verification

For each workflow after implementation:
1. Validate YAML syntax: `python -c "import yaml; yaml.safe_load(open('<file>'))"`
2. Check that no `gh pr create`, `peter-evans/create-pull-request`, or branch creation patterns remain
3. Verify `[skip ci]` is in every commit message
4. Verify idempotency guard (`git diff --staged --quiet`) is present
5. Push to main and confirm no auto-branches/PRs appear
6. Manually trigger each via `gh workflow run` and check the Actions tab for successful execution

**Single commit:** `refactor(ci): redesign 6 auto-PR workflows to commit directly to main`
