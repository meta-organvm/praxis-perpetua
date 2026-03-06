# Plan: Update ORGAN-VI `.github` Repo

## Context

The org profile README at `.github/profile/README.md` is stale — written during the CONSOLIDATION-II sprint when ORGAN-VI only had 2 skeleton repos. Since then, 3 repos were added (community-hub, koinonia-db, adaptive-personal-syllabus) and all repos advanced to PRODUCTION status. Visitors to `github.com/organvm-vi-koinonia` see outdated information.

Additionally, the `.github` repo has no CLAUDE.md, which means future Claude Code sessions opened from that directory lack context.

## Step 1: Update `profile/README.md`

**File:** `~/Workspace/organvm-vi-koinonia/.github/profile/README.md`

Changes needed:
- Update badge/count line from "3 repositories · 2 SKELETON · 1 DESIGN_ONLY" to "5 repositories · 4 PRODUCTION · 1 PROTOTYPE"
- Replace the 2-repo list with a full 5-repo table:
  | Repo | Role | Status |
  |------|------|--------|
  | `community-hub` | FastAPI portal — salon archive, curricula browser, stats dashboard | PRODUCTION (flagship) |
  | `koinonia-db` | Shared SQLAlchemy models, Alembic migrations, seed data | PRODUCTION |
  | `salon-archive` | Transcription pipeline, taxonomy, session archival | PRODUCTION |
  | `reading-group-curriculum` | Multi-week reading programs with discussion guides | PRODUCTION |
  | `adaptive-personal-syllabus` | AI-personalized learning paths across organ domains | PROTOTYPE |
- Update "Current Status" section from "early development" / skeleton language to reflect the actual state (DB layer built, seed data loaded, CI pipelines running, FastAPI flagship operational)
- Keep the Philosophy, Planned Initiatives, and Connection sections intact — they're still accurate and well-written
- Update the sprint tag at the bottom

## Step 2: Add `CLAUDE.md` to `.github` repo

**File:** `~/Workspace/organvm-vi-koinonia/.github/CLAUDE.md`

Brief file covering:
- What this repo is (org profile + community health files, not application code)
- Key files: `profile/README.md` (what visitors see on the org page), community health files (CODE_OF_CONDUCT, CONTRIBUTING, SECURITY), issue/PR templates in `.github/`
- That this is infrastructure — changes here affect the org-wide GitHub presence
- Org-level context: 5 sibling repos, dependency graph (koinonia-db → everything → community-hub)

## Step 3: Commit and push

Single commit to the `.github` repo with both files.

## Files to modify
- `~/Workspace/organvm-vi-koinonia/.github/profile/README.md` — update stale content
- `~/Workspace/organvm-vi-koinonia/.github/CLAUDE.md` — new file

## Verification
1. `git -C ~/Workspace/organvm-vi-koinonia/.github diff` — review changes before commit
2. `git -C ~/Workspace/organvm-vi-koinonia/.github status` — clean after push
3. Profile README renders correctly on `github.com/organvm-vi-koinonia` (check via `gh` or browser)
