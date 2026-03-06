# Plan: Update Rolling TODO with Outstanding Tasks

## Context

The rolling-todo.md was created during the AUTOMATA sprint (2026-02-17) and is 96% current. Since its creation, essays #34/#35 were deployed, and the Render deployment was attempted but hit free-tier limitations (worker type not available, Redis IP allow list required). The render.yaml was fixed and pushed, but the actual deployment hasn't completed — the old blueprint needs deletion and a fresh deploy.

## Changes

### File: `docs/operations/rolling-todo.md`

#### 1. Mark E4 as COMPLETED (line 42-43 → move to COMPLETED section)
- Essays #34 and #35 deployed to public-process on 2026-02-16
- Move from READY section to COMPLETED section with date

#### 2. Update X2 with current status (line 58-61)
- Add note: `render.yaml` fixed for free tier (removed worker + Redis), old Render blueprint needs deletion, then fresh deploy from updated yaml
- Keep in NEEDS TIME — This Week section

#### 3. Reclassify G2 from NEEDS INCOME to READY (lines 119-121)
- Render free tier costs $0 (no credit card needed)
- The deploy hook secret is free once the service exists
- Move from NEEDS INCOME to READY section
- Update description to note that service must be deployed first (depends on X2)

#### 4. Update totals (line 180)
- Adjust counts: READY goes from 2→2 (remove E4, add G2), COMPLETED goes from 1→2, INCOME goes from 4→3
- New total: 23 items (2 READY, 13 TIME, 3 INCOME, 3 EXTERNAL, 2 COMPLETED)

## Verification
- `grep -c '\[ \]' docs/operations/rolling-todo.md` should show 20 open items
- `grep -c '\[x\]' docs/operations/rolling-todo.md` should show 2 completed items
- E4 appears only in COMPLETED section
- G2 appears in READY section, not NEEDS INCOME
