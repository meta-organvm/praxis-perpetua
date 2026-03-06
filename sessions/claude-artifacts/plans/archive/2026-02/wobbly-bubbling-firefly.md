# Plan: ERUPTIO Commit Fix + Pipeline Prep

## Context

The ERUPTIO governance doc updates are done but currently say "completed 2026-02-18" — the user hasn't actually submitted anything yet. These are **staged materials to be completed**, not completed actions. Need to:

1. Fix the language in all 4 governance docs (completed → staged)
2. Commit with honest framing
3. Ensure the full "needle" pipeline (next 30 days) has all submission scripts ready
4. Write missing scripts for gaps

## Step 1: Fix Governance Doc Language

### Files to modify (4 files, ~25 edits total):

**`docs/operations/rolling-todo.md`** — 9 items currently marked `[x]` "completed":
- Change all 9 items from `[x]` back to `[ ]`
- Change "completed 2026-02-18" to "STAGED 2026-02-18 — materials ready, awaiting submission"
- In COMPLETED section: move the 10 new ERUPTIO entries back out (or reframe as "STAGED")
- Fix "Last reviewed" line from "completed" to "staged"
- Fix totals: 21 COMPLETED → revert to reflect actual state
- Fix provenance note: "9 items completed" → "9 items staged"

**`docs/applications/04-application-tracker.md`** — 8 status changes:
- Change "**SUBMITTED** — 2026-02-18" to "**STAGED** — materials ready 2026-02-18"
- Change "**ACTIVATED** — 2026-02-18" to "**STAGED** — setup guide ready 2026-02-18"
- Fix priority queue: "**SUBMITTED** 2026-02-18" → "**STAGED** — script ready"
- Fix summary table counts: 7 submitted → 0 submitted, 7 staged (or keep under "Ready")
- Fix header line

**`docs/strategy/there+back-again.md`** — omega scorecard:
- #5: Change `**MET**` back to `STAGED` or `NOT MET` with note "7 scripts ready, awaiting submission"
- #8: Change `**MET**` back to `NOT MET` with note "deploy script + Neon DB ready"
- #9: Change `**IN PROGRESS**` back to `NOT MET` with note "Sponsors setup guide ready"
- Fix score line back to: "1/17 MET, 3/17 IN PROGRESS, 13/17 NOT MET"
- Fix ERUPTIO note to "staged, awaiting execution"

**`docs/applications/eruptio-execution-guide.md`**:
- Change "Status: COMPLETED" → "Status: STAGED — all materials ready, awaiting execution"
- Fix post-action section from "COMPLETED" to "TO BE COMPLETED after execution"

## Step 2: Commit

Stage all 4 files and commit with honest message:
```
feat: ERUPTIO — stage all submission materials, prep governance docs for 7 applications + deploy + Sponsors

Materials staged (not yet submitted):
- 7 submission scripts clipboard-ready (Watermill, CL5, Artadia, Doris Duke, Prix Ars, S+T+ARTS, PEN America)
- Deploy guide ready (life-my--midst--in → Render)
- GitHub Sponsors setup guide ready
- Omega scorecard, rolling-todo, application-tracker pre-staged for execution
```

## Step 3: Audit Pipeline Coverage

**Full "needle" pipeline — script status:**

| Item | Deadline | Script | Status |
|------|----------|--------|--------|
| F24 Watermill | TODAY | `watermill.md` | READY |
| X1 Google CL5 | Rolling | `google-cl5.md` | READY |
| F12 PEN America | Rolling | `pen-america.md` | READY |
| F3 Artadia NYC | Mar 1 | `artadia-nyc.md` | READY |
| F22 Doris Duke | Mar 2 | `doris-duke.md` | READY |
| F10+F11 Prix Ars | Mar 4 | `prix-ars-starts.md` | READY |
| F1 GitHub Sponsors | ASAP | `infrastructure-setup.md` | READY |
| F2 Fractured Atlas | ASAP | `infrastructure-setup.md` | READY |
| F13 Awesome Foundation | Monthly | `awesome-foundation.md` | READY |
| F4 NEH Summer Programs | Mar 6 | **MISSING** | NEEDS SCRIPT |
| F14 Bread Loaf | Mar 15 | **MISSING** | NEEDS SCRIPT |
| W1 Noema Magazine | Rolling | `noema-pitch.md` | READY |
| W2 Gay & Lesbian Review | Rolling | `glr-pitch.md` | READY |
| E3 Google Fellowship | Mar 18 | `google-fellowship.md` | READY |
| X3 Together AI | Rolling | cover letter exists | READY (no script needed — direct apply) |
| X3 HuggingFace | Rolling | cover letter exists | READY (no script needed — direct apply) |

**Gaps requiring new scripts: 2**
- `neh.md` (F4, deadline Mar 6)
- `bread-loaf.md` (F14, deadline Mar 15)

**Already covered: 14 of 16 items have scripts or cover letters.**

## Step 4: Write Missing Scripts

Write 2 new submission scripts:

### `docs/applications/submission-scripts/neh.md` (F4)
- NEH Summer Programs
- Research the specific program and eligibility
- Educator identity position (11 years teaching, 100+ courses)
- Brief script — NEH Summer Programs are typically course-based, not application-heavy

### `docs/applications/submission-scripts/bread-loaf.md` (F14)
- Bread Loaf Writers' Conference scholarship
- Writer identity position (MFA, 42 essays, 134K words)
- Nonfiction track
- Application typically requires: writing sample, statement of purpose, brief bio

## Step 5: Second Commit

Commit the 2 new scripts:
```
feat: add submission scripts for NEH Summer Programs and Bread Loaf Conference
```

## Verification

After both commits:
- [ ] `git status` clean
- [ ] All 4 governance docs use "STAGED" not "completed" language
- [ ] Omega scorecard still shows 1/17 MET (honest)
- [ ] 16/16 "needle" pipeline items have scripts or cover letters
- [ ] Both commits pushed (or ready to push)
- [ ] Rolling-todo totals are accurate

## Files Modified

| File | Action |
|------|--------|
| `docs/operations/rolling-todo.md` | Fix completed → staged (9 items) |
| `docs/applications/04-application-tracker.md` | Fix submitted → staged (8 items) |
| `docs/strategy/there+back-again.md` | Fix omega scorecard back to honest state |
| `docs/applications/eruptio-execution-guide.md` | Fix status to STAGED |
| `docs/applications/submission-scripts/neh.md` | NEW — F4 script |
| `docs/applications/submission-scripts/bread-loaf.md` | NEW — F14 script |
