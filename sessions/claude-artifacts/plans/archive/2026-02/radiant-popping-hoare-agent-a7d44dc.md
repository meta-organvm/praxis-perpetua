# Orchestration Workflow Diagnosis — orchestration-start-here

## Summary of Findings

All five workflows investigated. Root causes identified for each. Three of the four "failing" workflows have already been resolved by recent pushes. The Python CI workflow was replaced entirely.

---

## 1. essay-monitor.yml — 6/6 FAILING

### What it does
Runs daily at 09:00 UTC (+ manual dispatch). Fetches `_posts/` from `organvm-v-logos/public-process` via `gh api`, parses essay filenames for dates, creates GitHub issues (labeled `essay-detected`) for any essays published in the last 7 days that don't already have tracking issues.

### Root cause: NOT a real failure — GitHub Actions phantom runs
All 6 "failures" show the workflow name as `.github/workflows/essay-monitor.yml` (the raw file path) instead of "Essay Monitor" (the friendly name). They have **0 jobs** and **no logs**. This is a GitHub Actions quirk:

- The workflow triggers are `schedule` and `workflow_dispatch` only — there is NO `push:` trigger
- When the workflow YAML file is modified in a push, GitHub creates a "run" record for it anyway
- Since `push` doesn't match any `on:` trigger, GitHub marks it as `failure` with no jobs executed
- All 6 failures correspond to push events on dates when the file was modified (2026-02-13 and 2026-02-16)

### Evidence
- The most recent **actual** run (workflow_dispatch on 2026-02-16T15:07:05Z, ID 22067838986) **succeeded**
- The 6 "failures" all have `event: "push"` and `name: ".github/workflows/essay-monitor.yml"`
- Job count for all failures: `total_count: 0`

### Fix approach
**No code fix needed.** These are cosmetic phantom failures. To prevent them going forward:
- Option A (recommended): Ignore them — they don't affect actual workflow execution
- Option B: Add a `push:` trigger with a path filter that will never match, e.g.:
  ```yaml
  on:
    push:
      paths: ['__never_match__']
    schedule:
      - cron: '0 9 * * *'
    workflow_dispatch:
  ```
  This would prevent the phantom run from being created. However, this is a hack.

### Minor issue in the script
Line 75: `now = datetime.now(timezone.utc).replace(tzinfo=None)` — this strips timezone info after getting UTC time. Not a bug per se, but `replace(tzinfo=None)` is unnecessary and confusing. The `datetime.utcnow()` deprecation warning also appears in the validate-dependencies workflow.

---

## 2. publish-process.yml — 6/6 FAILING

### What it does
Triggered by `issue_comment` events. When someone comments `@orchestration create essay` on an issue with the `publish-process` label, it:
1. Extracts README/CHANGELOG from the current repo
2. Generates a draft essay markdown file
3. If `ORCHESTRATION_PAT` secret exists, creates a PR in `organvm-v-logos/public-process`
4. Comments status on the issue

### Root cause: Same phantom run problem as essay-monitor
All 6 "failures" show `name: ".github/workflows/publish-process.yml"` (raw path), triggered by `push` events. The workflow's only trigger is `issue_comment`. Same GitHub Actions quirk.

### Evidence
- All 6 failures: `event: "push"`, `total_count: 0` jobs
- No actual `issue_comment`-triggered runs exist (the workflow has never been organically triggered)
- The YAML parses correctly — the structure is valid

### Fix approach
**No code fix needed for the failures.** Same phantom run situation.

However, there are real functional concerns with this workflow if it were actually triggered:
1. **Missing `ORCHESTRATION_PAT` secret**: The `HAS_PAT` env var check (`secrets.ORCHESTRATION_PAT != ''`) will evaluate to `false` on the runner since the secret comparison happens at the YAML level but the result gets passed as a string. The `if: env.HAS_PAT == 'true'` step will be skipped unless the secret is configured.
2. **Cross-org PR creation**: Even with a PAT, the `gh repo clone` + `git push` + `gh pr create` flow needs the PAT to have `repo` scope for `organvm-v-logos/public-process`.
3. **The workflow comments status regardless** (the `Comment Status` step runs with `if: always()`), so even without the PAT it will post a helpful message.

---

## 3. ci.yml (was "Python CI", now "Minimal CI") — 5/5 FAILING

### What it does
**At the time of failures (commit 68cf4af):** The file was named `ci.yml` but had `name: Python CI`. It ran a full Python CI matrix (3.11 + 3.12) with pip caching, dependency detection, ruff, mypy, and pytest.

**Current version:** Replaced with `name: Minimal CI` — just checks for README.md and LICENSE files. All runs now succeed.

### Root cause: `setup-python` with `cache: 'pip'` but no `requirements.txt` or `pyproject.toml`
The exact error from the logs:
```
No file in /home/runner/work/orchestration-start-here/orchestration-start-here
matched to [**/requirements.txt or **/pyproject.toml],
make sure you have checked out the target repository
```

The `setup-python@v5` action with `cache: 'pip'` **requires** a pip dependency file to hash for the cache key. The repo has no `requirements.txt`, `pyproject.toml`, or `setup.py`. The action treats this as a hard error and fails the job.

### Evidence
- 5/5 failures, all on push events between 2026-02-10 and 2026-02-11
- Job `test (3.12)` failed; `test (3.11)` was cancelled (matrix fail-fast)
- Error: "No file matched to [**/requirements.txt or **/pyproject.toml]"
- The workflow was subsequently replaced with the current Minimal CI on/around 2026-02-12

### Fix approach
**Already fixed.** The workflow was replaced with `name: Minimal CI` which doesn't use Python setup at all. All 31+ Minimal CI runs since then show `conclusion: "success"`.

If you ever want to restore Python CI, either:
- Remove `cache: 'pip'` from the setup-python step, OR
- Add a minimal `requirements.txt` (even empty) to the repo root

---

## 4. validate-dependencies.yml — 4/6 FAILING (intermittent)

### What it does
Validates the organ system's dependency graph from `registry.json`. Checks for:
1. Cycles (circular dependencies)
2. Back-edges (forbidden cross-organ direction: e.g., ORGAN-III depending on ORGAN-I)
3. Transitive depth (chains > 4 levels)
4. Dangling references (deps pointing to repos not in registry)

Runs on: registry file pushes, weekly schedule (Mon 06:30 UTC), manual dispatch.

### Root cause: Two ORGAN-III repos had back-edge dependencies on ORGAN-I
The exact error from all 4 failure logs:
```
Back-edge: organvm-iii-ergon/tab-bookmark-manager depends on
  organvm-i-theoria/my-knowledge-base (ORGAN-III cannot depend on ORGAN-I)
Back-edge: organvm-iii-ergon/my--father-mother depends on
  organvm-i-theoria/my-knowledge-base (ORGAN-III cannot depend on ORGAN-I)
```

These back-edges violated the governance rule that ORGAN-III (Commerce) cannot depend on ORGAN-I (Theory). The `dependencies` arrays for these two repos had `organvm-i-theoria/my-knowledge-base` listed.

### Timeline
- **2026-02-13 through 2026-02-16T07:35** — failures (4 runs: 2 push, 1 schedule, 1 manual dispatch)
- **2026-02-12T12:31** — success (before the back-edges were introduced)
- **2026-02-16T15:04** — success (after the registry was fixed, back-edges removed)

### Current state: RESOLVED
The remote `registry.json` now shows `"dependencies": []` for both `tab-bookmark-manager` and `my--father-mother`. The most recent run passed.

### Secondary issue: deprecation warning
Line in the inline script uses `datetime.datetime.utcnow()` (deprecated since Python 3.12). Should be `datetime.datetime.now(datetime.UTC)`. This is a warning, not a failure cause.

### Fix approach
**Already fixed** in the registry. The deprecation warning can be cleaned up by changing the inline Python from:
```python
now = datetime.now(timezone.utc).isoformat()
```
(This is actually already correct in the current code — the deprecation warning might be from an older version that was running at the time, or from a different code path.)

---

## 5. distribute-content.yml — 29/29 SKIPPED

### What it does
POSSE distribution automation. Triggered when the `ready-to-distribute` label is applied to an issue. Posts to Mastodon, Discord, LinkedIn, and Ghost newsletter.

### Root cause: The `if:` condition correctly filters non-matching events
The workflow trigger is:
```yaml
on:
  issues:
    types: [labeled]
```

And the job has:
```yaml
if: contains(github.event.label.name, 'ready-to-distribute')
```

All 29 runs were triggered by the `essay-monitor` workflow creating issues with the `essay-detected` label — **not** the `ready-to-distribute` label. GitHub fires the `issues.labeled` event for every label application. The `if:` condition correctly evaluates to `false` and the job is skipped.

### Evidence
- All 29 runs: `event: "issues"`, `conclusion: "skipped"`
- The 29 issues created (e.g., "Essay Detected: Why Ai Function Calling Needs Ontological Grounding") all have the `essay-detected` label only
- The `distribute` job shows `conclusion: "skipped"` — the `if` condition worked as designed
- The display titles match the essay-monitor issue titles

### This is correct behavior
The workflow is working exactly as intended. The `essay-detected` issues are meant to be triaged first (review essay, prepare social excerpt), then manually labeled `ready-to-distribute` to trigger actual distribution. The 29 skips are the system correctly waiting for human approval before distributing.

### No fix needed
This is the expected flow. If you want to reduce noise in the Actions tab, you could add a concurrency group or use a more specific trigger. But the current design is intentional.

---

## Summary Table

| Workflow | Failures | Root Cause | Current State | Action Needed |
|----------|----------|------------|---------------|---------------|
| essay-monitor.yml | 6/6 | Phantom push runs (no `push:` trigger) | PASSING (latest dispatch succeeded) | None (cosmetic) |
| publish-process.yml | 6/6 | Phantom push runs (no `push:` trigger) | Never organically triggered | None (cosmetic) |
| ci.yml (Python CI) | 5/5 | `cache: 'pip'` with no requirements file | REPLACED with Minimal CI — all passing | Already fixed |
| validate-dependencies.yml | 4/6 | Back-edge violations in registry | FIXED — latest run passed | Already fixed |
| distribute-content.yml | 29/29 skipped | Correct `if:` filtering on label name | Working as designed | None |

## Optional Cleanup Items
1. **Deprecation warning**: Update inline Python in validate-dependencies.yml to use `datetime.now(datetime.UTC)` instead of any `utcnow()` calls
2. **Phantom runs**: Could add dummy `push: paths: ['__never__']` to essay-monitor and publish-process to prevent phantom entries, but this is purely cosmetic
3. **CROSS_ORG_TOKEN**: The essay-monitor uses `secrets.CROSS_ORG_TOKEN || secrets.GITHUB_TOKEN` — verify that `CROSS_ORG_TOKEN` is set in the repo secrets for reliable cross-org API calls (the recent successful run suggests it is)
4. **ORCHESTRATION_PAT**: The publish-process workflow needs this secret configured to actually create cross-org PRs
