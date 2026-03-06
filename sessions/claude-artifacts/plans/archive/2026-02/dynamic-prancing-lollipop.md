# PROPULSIO MAXIMA: Multi-Front Forward Sprint

## Context

The ORGANVM system is at **1/17 omega criteria MET**, with 3 IN_PROGRESS (time-gated soak tests at day 9/30). The pitch deck generator (Phase 1) just shipped. 62 repos are LOCAL, 16 are CANDIDATE, 12 PUBLIC_PROCESS, 4 GRADUATED (all ORGAN-VII). All ORGAN-III products are pre-launch with $0 MRR. The system needs simultaneous forward pressure on multiple fronts to break out of infrastructure-building mode into occupation mode.

**Goal:** Maximize omega criteria movement + promotion pipeline throughput via engineering work across 5 parallel fronts.

## Omega Criteria Triage

| # | Criterion | Status | Flippable by Engineering? | Action |
|---|-----------|--------|--------------------------|--------|
| 1 | 30-day soak (≤3 incidents) | IN_PROGRESS 9/30 | Auto (time) | Wait |
| 3 | Engagement baseline (30 days) | IN_PROGRESS 9/30 | Auto (time) | Wait |
| 17 | 30+ days autonomous | IN_PROGRESS 9/30 | Auto (time) | Wait |
| **8** | **≥1 ORGAN-III product live** | NOT_MET | **YES** | **Deploy public-record-data-scrapper** |
| **9** | **revenue_status: live** | NOT_MET | **YES** | **Flip registry after deploy** |
| **5** | **≥1 application submitted** | NOT_MET | **YES** | **Submit from application-pipeline** |
| **15** | **Portfolio updated w/ validation** | NOT_MET | **YES** | **Update portfolio site with system data** |
| 2,4,7,11,12,13,14,16 | External participants | NOT_MET | No (needs people) | Out of scope |

**Engineering can flip 4 omega criteria (#5, #8, #9, #15) and 3 more auto-complete with time (#1, #3, #17).** That's 7/17 → potentially 8/17 within 30 days (up from 1/17).

---

## Front 1: Deploy public-record-data-scrapper (Omega #8, #9)

**Why:** Flagship ORGAN-III product. Already at PUBLIC_PROCESS. Has `vercel.json`, `Dockerfile`, `docker-compose.yml`, 2,055 tests, Terraform AWS infra. Described as "50-state UCC public records aggregation platform" with "tiered B2B subscriptions." This is the single highest-leverage move — flips 2 omega criteria.

### Steps

1. **Audit deployment readiness**
   - Read `vercel.json`, `docker-compose.yml`, `Dockerfile`, `package.json`
   - Check what's actually deployed vs. what needs setup
   - Identify any env vars, API keys, or infra needed
   - `organvm-iii-ergon/public-record-data-scrapper/`

2. **Deploy to Vercel (or validate existing deployment)**
   - Wire up production config
   - Ensure at least the landing page + one functional route is live

3. **Enable Stripe subscription tier**
   - The registry says `revenue_model: "subscription"` — check if Stripe integration exists
   - If exists: configure production keys, enable at least 1 tier
   - If not: create minimal Stripe Checkout integration

4. **Update registry-v2.json**
   - `revenue_status: "pre-launch"` → `"live"`
   - `promotion_status: "PUBLIC_PROCESS"` → leave (GRADUATED needs more)
   - Update `last_validated` and `note`

### Files
- `organvm-iii-ergon/public-record-data-scrapper/vercel.json`
- `organvm-iii-ergon/public-record-data-scrapper/Dockerfile`
- `organvm-iii-ergon/public-record-data-scrapper/package.json`
- `organvm-corpvs-testamentvm/registry-v2.json`

---

## Front 2: Pitch Deck Phase 2 — First Rollout

**Why:** The generator shipped but no decks have actually been generated yet. Generating 15-20 decks across 3 organs is high-visibility, low-risk work that immediately improves system presentation.

### Steps

1. **Generate decks for ORGAN-I** (~16 eligible repos)
   ```
   organvm pitch sync --organ ORGAN-I
   ```

2. **Generate decks for ORGAN-II** (~20 eligible repos)
   ```
   organvm pitch sync --organ ORGAN-II
   ```

3. **Generate decks for ORGAN-III** (~15 eligible repos, skip bespoke)
   ```
   organvm pitch sync --organ ORGAN-III
   ```

4. **Spot-check** — open 3-4 decks in browser, verify theming + content

5. **Commit generated decks** per-repo (one commit per repo with deck)

6. **Create `pitch.yaml` for 3-4 flagships** — enriched content for:
   - `recursive-engine--generative-entity` (ORGAN-I flagship)
   - `public-record-data-scrapper` (ORGAN-III flagship)
   - `organvm-engine` (META flagship)

### Files
- `organvm-engine/src/organvm_engine/pitchdeck/sync.py` (already built)
- Each generated `docs/pitch/index.html` across repos

---

## Front 3: Promotion Pipeline Cascade

**Why:** 62 LOCAL repos is a massive backlog. ORGAN-VII graduated all 4 repos — proving the pipeline works. Promoting repos en masse demonstrates system maturity and is a prerequisite for many omega criteria.

### Steps

1. **Promote organvm-engine LOCAL → CANDIDATE**
   - It's flagship, 192+ tests, full CI — far beyond CANDIDATE requirements
   - Update `promotion_status`, `last_validated`, `note` in registry

2. **Promote other META repos**
   - `system-dashboard`: LOCAL → CANDIDATE (has CI, tests)
   - `alchemia-ingestvm`: stays CANDIDATE (already there)
   - `schema-definitions`: stays CANDIDATE (already there)

3. **Batch promote eligible ORGAN-I repos LOCAL → CANDIDATE**
   - Any with `ci_workflow` + `platinum_status: true` + ACTIVE status
   - Registry scan needed to identify full list

4. **Batch promote eligible ORGAN-III repos LOCAL → CANDIDATE**
   - Same criteria: CI + platinum + ACTIVE

5. **Update registry metadata**
   - Fix stale counts (organvm-engine registry says 41 tests, actually 192+)
   - Update `total_repos` in summary (now 103, registry says 101)

### Files
- `organvm-corpvs-testamentvm/registry-v2.json`

---

## Front 4: Engine Hardening

**Why:** organvm-engine is the crown jewel infrastructure but registry metadata is stale and platinum status isn't set. Hardening it demonstrates the system can maintain itself.

### Steps

1. **Set platinum_status: true** in registry for organvm-engine
   - It has CI, CHANGELOG, CLAUDE.md, tests, README — exceeds platinum

2. **Update engine registry entry**
   - Fix test count: 41 → 192+
   - Add note about pitchdeck module, omega scorecard, contextmd sync
   - Update `last_validated` to today

3. **Update organvm-mcp-server registry entry**
   - Note the new `organvm_pitch_status` tool (15 tools total now)
   - Update test count if needed

4. **Run `organvm context sync`** to refresh all auto-generated CLAUDE.md sections
   - Ensures edge data, sibling lists, and organ info are current

### Files
- `organvm-corpvs-testamentvm/registry-v2.json`
- `organvm-engine/src/organvm_engine/contextmd/sync.py` (run only)

---

## Front 5: Portfolio + Application Readiness (Omega #5, #15)

**Why:** Omega #5 requires ≥1 application submitted. #15 requires portfolio updated with validation data. Both are engineering-actionable.

### Steps

1. **Update portfolio site** (`4444J99/portfolio/`) with current system data
   - 103 repos, 192+ engine tests, 8 organs operational
   - Add omega scorecard data as validation evidence
   - This flips omega #15

2. **Prepare application submission** from `4444J99/application-pipeline/`
   - Check which applications are staged and closest to submission
   - Identify the one needing least additional work
   - Complete and submit → flips omega #5

### Files
- `4444J99/portfolio/` (Astro site)
- `4444J99/application-pipeline/`
- `organvm-corpvs-testamentvm/docs/applications/`

---

## Implementation Order

| Priority | Front | Effort | Omega Impact |
|----------|-------|--------|--------------|
| 1 | **Front 1**: Deploy ORGAN-III product | High | #8 + #9 (2 criteria) |
| 2 | **Front 3**: Promotion cascade | Medium | Pipeline movement (prerequisite for many criteria) |
| 3 | **Front 2**: Pitch deck rollout | Low | Visibility + system presentation |
| 4 | **Front 4**: Engine hardening | Low | Registry accuracy + platinum |
| 5 | **Front 5**: Portfolio + applications | Medium | #5 + #15 (2 criteria) |

Fronts 2-4 can run in parallel. Front 1 is the critical path. Front 5 depends on some context from Fronts 3-4.

## Verification

1. `organvm omega` — scorecard should show movement on #8, #9, #15, #5
2. `organvm registry list --status CANDIDATE` — should show 30+ repos (up from 16)
3. `organvm pitch sync --dry-run` — should show 50+ decks generated
4. Visit deployed product URL — live with at least landing page
5. `pytest organvm-engine/tests/ -v` — all tests still pass
6. `pytest organvm-mcp-server/tests/ -v` — all tests still pass
7. `organvm registry validate` — zero warnings on promoted repos

## Key Reference Files

- `organvm-engine/src/organvm_engine/omega/scorecard.py` — 17 criteria definitions
- `organvm-engine/src/organvm_engine/governance/state_machine.py` — promotion transitions
- `organvm-engine/src/organvm_engine/pitchdeck/sync.py` — pitch deck workspace sync
- `organvm-corpvs-testamentvm/registry-v2.json` — single source of truth
- `organvm-iii-ergon/public-record-data-scrapper/` — deployment target
- `organvm-vi-koinonia/community-hub/` — Dockerfile + render.yaml (ready for deploy, future front)
