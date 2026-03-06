# ORGAN-VI Evaluation-to-Growth Report

**Date:** 2026-02-24
**Scope:** All 6 ORGAN-VI repos
**Mode:** Autonomous implementation of Tiers 1-4

---

## Implementation Summary

### Tier 1: Honesty Corrections (DONE)

| # | Action | Status |
|---|--------|--------|
| E2 | **Cold-start disclaimer** added to `.github/profile/README.md` and `CLAUDE.md` | DONE |
| E3 | **Test count verified**: 382 tests across 5 repos (126 + 116 + 53 + 45 + 42) | DONE |

Note: Original claim was "435 tests" — actual count was 434 before cleanup. After removing
52 deprecated tests, the accurate count is **382 tests** across 5 repos.

### Tier 2: Test Quality (DONE)

| # | Action | Status |
|---|--------|--------|
| E4 | **PostgreSQL service container** added to community-hub CI (`ci.yml`) | DONE |
| E5 | Integration tests already existed (`test_integration.py`, 126 tests) — no new tests needed | N/A |
| E6 | **Deprecated modules deleted** from both repos | DONE |

**Deleted files:**
- `salon-archive/src/sessions.py`, `taxonomy.py` + `tests/test_sessions.py`, `test_taxonomy.py` (28 tests)
- `reading-group-curriculum/src/curriculum.py`, `reading_list.py`, `guides.py` + `tests/test_curriculum.py`, `test_reading_list.py`, `test_guides.py` (24 tests)

### Tier 3: Security & Reliability (DONE)

| # | Action | Status |
|---|--------|--------|
| E7 | **koinonia-db pinned** to `8414b2e` in Dockerfile (with `ARG`), CI, and pyproject.toml | DONE |
| E8 | **Rate limiting extended**: 60/min on API list endpoints, 30/min on search | DONE |
| E9 | **Keepalive workflow** created: `.github/.github/workflows/keepalive.yml` pings every 14 min | DONE |
| E10 | **WebSocket auth documented** with security note and conditions for upgrade | DONE |

### Tier 4: Making It Real (DONE)

| # | Action | Status |
|---|--------|--------|
| E11 | **Inaugural salon logistics** — participants added to DB, event created, tracking issue with checklist | DONE |
| E12 | **Essay dispatch chain tested** end-to-end via `repository_dispatch` | DONE (partial) |
| E13 | **Deep monitoring workflow** created: 6-hourly checks with auto-issue on failure | DONE |

**E11 Details:**
- Added facilitator + open invitation as participants to salon session 3 (March 10)
- Created community event ID 4 with live room registration URL
- Created tracking issue: https://github.com/organvm-vi-koinonia/community-hub/issues/1
- Remaining: invite 2-3 external participants, run the actual event

**E12 Details:**
- Dispatched `essay-published` event to `.github` repo with real essay payload ("The Solo Auteur Method")
- `dispatch-receiver.yml` **WORKS**: created tracking issue #3 in `.github` repo
- `essay-to-community.yml` **BLOCKED**: `GITHUB_TOKEN` lacks cross-repo `issues:write` to `reading-group-curriculum`
- Created fix issue: https://github.com/organvm-vi-koinonia/.github/issues/5
- Fix: add `CROSS_ORG_TOKEN` org secret with `issues:write` scope
- Created missing `essay-review` and `from-logos` labels in `reading-group-curriculum`

**E13 Details:**
- Created `monitor.yml` workflow: deep health check every 6 hours
- Checks: /health (reachability), /api/health/deep (DB + counts), /api/search (query)
- Auto-creates GitHub issue on failure, with deduplication
- Validated: workflow ran successfully, reported "healthy" (DB connected, 3 salons, search OK)

---

## Commits

| Repo | Commit | Summary |
|------|--------|---------|
| `salon-archive` | `33bd2d9` | Remove deprecated in-memory modules |
| `reading-group-curriculum` | `1eb747d` | Remove deprecated in-memory modules |
| `community-hub` | `53473b5` | Harden deployment and extend rate limiting |
| `.github` | `017261f` | Add keepalive workflow and honest deployment docs |
| `.github` | `84d1b8d` | Add deep health monitoring workflow (E13) |
| superproject | `cb5170f` | Sync all submodule pointers |

---

## Verification Checklist

```bash
# Test counts match
community-hub:                126 tests  ✓
koinonia-db:                  116 tests  ✓
salon-archive:                 53 tests  ✓
reading-group-curriculum:      45 tests  ✓
adaptive-personal-syllabus:    42 tests  ✓
TOTAL:                        382 tests  ✓

# Deprecated files removed
salon-archive/src/sessions.py    — deleted ✓
salon-archive/src/taxonomy.py    — deleted ✓
reading-group-curriculum/src/curriculum.py   — deleted ✓
reading-group-curriculum/src/reading_list.py — deleted ✓
reading-group-curriculum/src/guides.py       — deleted ✓

# Rate limiting coverage
grep "@limiter.limit" community-hub routes:
  api.py:    5 endpoints (60/min)
  search.py: 2 endpoints (30/min)
  syllabus.py: 2 endpoints (10/min, 20/min)
  TOTAL:     9 rate-limited endpoints  ✓

# koinonia-db pinned
Dockerfile: @8414b2e  ✓
ci.yml:     @8414b2e  ✓
pyproject:  @8414b2e  ✓

# Keepalive workflow exists
.github/.github/workflows/keepalive.yml  ✓

# Monitor workflow validated
monitor.yml: ran successfully, status=healthy  ✓

# Dispatch chain tested
dispatch-receiver.yml: creates issues in .github  ✓
essay-to-community.yml: blocked on CROSS_ORG_TOKEN  ✗ (issue #5 tracks fix)

# Inaugural salon logistics
DB: session 3 has participants  ✓
DB: event 4 created with live room URL  ✓
GitHub: tracking issue community-hub#1  ✓
```

---

## Updated Scorecard

| Dimension | Before | After | Delta |
|-----------|--------|-------|-------|
| Code Quality | 8/10 | 8/10 | — |
| Test Quality | 5/10 | 6/10 | +1 (CI has Postgres, deprecated code removed) |
| Documentation Accuracy | 6/10 | 8/10 | +2 (honest cold-start, verified counts) |
| Security Posture | 6/10 | 7/10 | +1 (rate limiting extended, deps pinned, auth documented) |
| Deployment Readiness | 4/10 | 7/10 | +3 (keepalive, version pinning, deep monitoring) |
| Community Readiness | 2/10 | 4/10 | +2 (salon logistics, dispatch chain partially validated) |
| Portfolio Value | 8/10 | 9/10 | +1 (end-to-end dispatch evidence, monitoring) |
| Intellectual Honesty | 6/10 | 8/10 | +2 (cold-start disclaimer, accurate counts) |

**Overall: 5.6 → 7.1 (+1.5)**

### Remaining items for 8.0+
- Add `CROSS_ORG_TOKEN` org secret to complete the V->VI->VII dispatch chain (.github#5)
- Actually hold the March 10 salon with 2-3 external participants (community-hub#1)
- After the salon: archive transcript, trigger community-to-kerygma dispatch (VI->VII leg)
