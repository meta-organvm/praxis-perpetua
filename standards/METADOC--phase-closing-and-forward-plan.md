# METADOC: Phase-Closing Commemoration & Forward Attack Plan

| Field | Value |
|-------|-------|
| **Date** | 2026-03-08 |
| **Phase** | Construction → Operational Transition |
| **Status** | ACTIVE |
| **Author** | Human (with forensic correction of agent-generated claims) |
| **Supersedes** | Gemini "Grand Unification" session claims (2026-03-08) |

---

## Part 1: Phase Closing — What We Actually Built

### 1.1 Forensic Correction of Gemini Claims

A Gemini agent session titled "The Grand Unification" produced 8 claims about system maturity. Seven were false, misleading, or unverifiable. One was correct.

| # | Gemini Claim | Verdict | Ground Truth | Source |
|---|-------------|---------|-------------|--------|
| 1 | "100% graduation" (all 105 repos GRADUATED) | **FALSE** | 95 GRADUATED, 10 ARCHIVED. Archived is not graduated — it is retired. | `registry-v2.json` promotion_status counts |
| 2 | "99% CI coverage" | **FALSE** | 95.2% (100/105 repos with CI workflow field) | `registry-v2.json` ci_workflow field audit |
| 3 | "100% maturity" (omega scorecard) | **FALSE** | 4/17 criteria MET (23.5%). Criteria #5, #6, #8, #13 only. | `omega/scorecard.py` `_KNOWN_MET` dict |
| 4 | "64% ship rate" | **UNVERIFIABLE** | Conductor session was ABANDONED. No ship-rate telemetry exists. | Conductor session logs |
| 5 | "16-session streak" | **UNVERIFIABLE** | No streak-tracking mechanism has ever been built. | System codebase search |
| 6 | Revenue addressed | **FALSE BY OMISSION** | $0 revenue, 0 products deployed to production. Not mentioned. | Stripe dashboard, Vercel project list |
| 7 | External validation addressed | **FALSE BY OMISSION** | 0 external contributors, 0 stranger tests, 0 salon attendees. | GitHub contributor stats, event logs |
| 8 | "0 principles internalized" | **CORRECT** | Accurate. The one honest data point. | praxis-perpetua session logs |

**Pattern Diagnosis**: The agent conflated *metadata writes* (batch promotion of status fields in `registry-v2.json`) with *operational maturity* (deployed products, revenue, external validation). Changing `promotion_status: "GRADUATED"` in a JSON file is a registry operation, not evidence that a product is production-ready.

**Anti-Pattern Classification**: See Section 3 — **AP-9: Metadata Maturity Conflation**.

### 1.2 Genuine Accomplishments — Enterprise Level

These are real, verified, and significant:

| Accomplishment | Metric | Evidence |
|---------------|--------|----------|
| Promotion pipeline cleared | 95 repos at GRADUATED | `registry-v2.json` counts |
| Test infrastructure | 1,915 tests across 5 packages | `pytest` runs (engine 1549, mcp 170, alchemia 136, dashboard 31, schemas 15, corpus 14) |
| Institutional memory codified | 33 SOPs + 5 templates in praxis-perpetua | `ls praxis-perpetua/standards/` |
| Engine depth | 21+ domain modules, 23 CLI command groups | `organvm-engine/src/organvm_engine/` |
| MCP exposure | ~66 tools across 15 tool groups | `organvm-mcp-server` dispatch table |
| Registry governance | Fully validated, dependency graph clean, governance-rules enforced | `organvm governance audit` output |
| Omega progress | 4/17 MET with evidence (applications, essays, products, inbound links) | `organvm omega status` |
| 10x test growth | ~192 tests 6 weeks ago → 1,915 today | E2G review commit history |
| Schema contracts | 6 JSON Schemas covering all system data types | `schema-definitions/schemas/` |
| Multi-agent session intelligence | 1,367 sessions / 3.5GB parsed (Claude 829, Gemini 355, Codex 183) | `organvm session agents` |

### 1.3 Genuine Accomplishments — Organ Level

| Organ | Key Achievement |
|-------|----------------|
| **I (Theoria)** | hierarchia-mundi theoretical framework established; knowledge-base ingestion pipeline operational |
| **II (Poiesis)** | Omni-Dromenon creative engine scaffolded; materia-collider founded for generative art |
| **III (Ergon)** | PABB flagship identified; 23 products wired to community (VI) + distribution (VII) channels |
| **IV (Taxis)** | Conductor OS designed; governance doc flood (33 SOPs); orchestration scripts operational |
| **V (Logos)** | Captain's log established; analytics pipeline; 47+ essays in corpus |
| **VI (Koinonia)** | Community infrastructure wired; 23 product community nodes + taxonomy created |
| **VII (Kerygma)** | 23 kerygma profiles created; distribution pipeline architecture complete |
| **META** | Engine expansion (atoms, distill, coordination, ecosystem, study, sop modules); MCP 3.3x tool growth; praxis-perpetua founded |

### 1.4 Genuine Accomplishments — Repo Level

| Repo | Milestone |
|------|-----------|
| `organvm-engine` | 1,549 tests, 21 domain modules, 23 CLI groups — the nervous system works |
| `organvm-mcp-server` | 170 tests, 66 tools — full system graph exposed to any Claude session |
| `organvm-corpvs-testamentvm` | 404K+ words, registry-v2.json as single source of truth, 66+ tracked issues |
| `praxis-perpetua` | 33 SOPs, 5 templates, session critique logs — institutional memory exists |
| `alchemia-ingestvm` | 136 tests, INTAKE→ABSORB→ALCHEMIZE pipeline, aesthetic taste.yaml cascades |
| `stakeholder-portal` | Next.js MVP scaffolded with repo browser + AI chat interface |
| `schema-definitions` | 6 canonical schemas, validation scripts, 15 tests |
| `system-dashboard` | FastAPI + HTMX, 6 routes, 31 tests, Living Data Organism integration |

---

## Part 2: Attack Plan — What Tomorrow Demands

### 2.1 Enterprise Level — Omega Unblock Priority

Ordered by omega-criteria-per-action (most impact first):

| Priority | Omega # | Criterion | Current State | Concrete First Step | Unblocks |
|----------|---------|-----------|---------------|-------------------|----------|
| **P0** | #1, #3, #17 | Soak test (30-day continuous) | NOT DEPLOYED (0 snapshots) | Create LaunchAgent plist that runs `organvm omega status --json > data/omega/` daily; fix soak data directory resolution in engine | 3 criteria auto-flip after 30 days |
| **P1** | #9, #10 | Revenue ($1+ earned, payment integration) | $0, 0 products live | Deploy `public-record-data-scrapper` or PABB to Vercel with Stripe checkout; minimum viable: one paid tier | 2 criteria |
| **P2** | #7 | External feedback (stranger usability) | 0 tests run | Run SOP--stranger-test-protocol on 3 ORGAN-III products; recruit via Reddit/HN | 1 criterion |
| **P3** | #12 | External contributions | 0 contributors | Promote existing good-first-issues (engine#2-4, corpus#65-66) on relevant communities; add CONTRIBUTING.md call-to-action | 1 criterion |
| **P4** | #2 | Stranger test score ≥ 3/5 | No participant yet | Recruit 1 stranger tester; blocked on P2 (need a deployed product to test) | 1 criterion |
| **P5** | #11 | Community event (salon/reading group) | Infrastructure only | Host 1 reading group session via koinonia-db; topic: hierarchia-mundi or construction-addiction essay | 1 criterion |
| **P6** | #15 | Portfolio external validation | Portfolio live, no validation data | Add analytics tracking + collect 1 piece of external feedback on portfolio | 1 criterion |
| **P7** | #4, #16 | Bus factor / runbook validation | Written, not tested by second operator | Find 1 trusted person to run the "reproduce workspace" runbook end-to-end | 2 criteria |
| **P8** | #14 | External recognition | 0 submissions | Submit to 1 conference (Strange Loop, local meetup) or 1 award program | 1 criterion |

**Total unblockable**: 13/17 criteria (from current 4/17 → potential 17/17)

### 2.2 Organ Level — Next Big Moves

| Organ | Next Move | Rationale | Blocked By |
|-------|-----------|-----------|------------|
| **I (Theoria)** | Publish hierarchia-mundi as external essay | Theory needs external validation; feeds omega #7 | Nothing — ready to write |
| **II (Poiesis)** | Ship 1 generative art piece publicly | Proves theory→art pipeline; creative portfolio evidence | Art piece selection |
| **III (Ergon)** | Deploy PABB or public-record-data-scrapper with Stripe | Revenue unblock (omega #9/#10); highest-impact action | Vercel setup, Stripe config, Neon DB |
| **IV (Taxis)** | Deploy soak test cron job | Unblocks 3 omega criteria automatically over 30 days | LaunchAgent plist creation |
| **V (Logos)** | Bring captain's log current + publish essay #48 | Public record continuity; feeds omega content criteria | Nothing — ready to write |
| **VI (Koinonia)** | Host first reading group session | Omega #11; proves community infrastructure works | Event scheduling, minimum 1 participant |
| **VII (Kerygma)** | Ship first automated announcement from kerygma-pipeline | Proves I→VII full-system flow end-to-end | Pipeline deployment, trigger event |
| **META** | Fix soak data dir + engine soak integration | Foundation for autonomous operation proof (P0) | Code fix in engine paths |

### 2.3 Repo Level — Top 10 Highest-Impact Tasks

| # | Repo | Task | Organ | Effort | Unblocks |
|---|------|------|-------|--------|----------|
| 1 | `organvm-engine` | Fix soak snapshot data directory + add LaunchAgent | META | 2h | Omega #1/#3/#17 |
| 2 | `public-record-data-scrapper` | Deploy to Vercel with Neon + Stripe | III | 4h | Omega #9/#10 |
| 3 | `organvm-engine` | Add `--format json` to all CLI commands (engine#2) | META | 3h | External contributor onramp |
| 4 | `stakeholder-portal` | Deploy to Vercel as public demo | META | 2h | Portfolio + stranger test target |
| 5 | `organvm-corpvs-testamentvm` | Write + publish essay #48 | V | 3h | Content continuity |
| 6 | `koinonia-db` | Create first reading group event with agenda | VI | 1h | Omega #11 |
| 7 | `kerygma-pipeline` | End-to-end test: trigger event → announcement | VII | 2h | I→VII flow proof |
| 8 | `portfolio` | Add analytics + validation tracking | — | 1h | Omega #15 |
| 9 | `organvm-engine` | Type hints for public API (engine#3) | META | 2h | External contributor onramp |
| 10 | `hierarchia-mundi` | Extract essay from theoretical framework | I | 3h | External theory validation |

---

## Part 3: Anti-Pattern Registry

### AP-9: Metadata Maturity Conflation

**Pattern**: An agent (or human) changes status fields in a registry/database and reports the system as "mature," "complete," or "graduated" based solely on the metadata change — without verifying that the underlying operational reality matches.

**Symptoms**:
- Batch promotion of 50+ repos in a single session with no per-repo audit
- Claims of "100% maturity" when the system's own scorecard reads 23.5%
- Absence of revenue, deployment, or external validation metrics in "completion" reports
- Superlative language ("perfect statue," "magnum opus") attached to infrastructure bookkeeping

**Root Cause**: Agents optimize for task completion signals. Changing a JSON field from `LOCAL` to `GRADUATED` produces the same "done" signal as deploying a product to production — but the latter requires external systems (hosting, payments, users) that the agent cannot control.

**Mitigation**:
1. **Scorecard gate**: No phase can be declared "complete" unless the omega scorecard shows improvement. The scorecard measures operational reality, not registry state.
2. **Revenue gate**: Any claim of "product readiness" must cite deployed URL + payment integration status.
3. **External gate**: Any claim of "community readiness" must cite at least 1 external interaction (contributor, tester, attendee).
4. **Audit trail**: Batch promotions require a per-repo justification log. The promotion SOP (`SOP--promotion-and-state-transitions.md`) already requires this — enforce it.

**Cross-references**:
- `SOP--promotion-and-state-transitions.md` — promotion criteria and audit requirements
- `SOP--stranger-test-protocol.md` — external validation methodology
- `SOP--session-self-critique.md` — agent output verification
- `omega/scorecard.py` — the 17-criterion binary scorecard

---

## Appendix: Issue Tracker

All attack plan items are tracked as GitHub issues. See:
- Enterprise-level: `meta-organvm/organvm-corpvs-testamentvm` issues (labeled `omega` + `horizon-1`)
- Organ-level: `meta-organvm/organvm-corpvs-testamentvm` issues (labeled by `cat:*`)

---

*This document is a living plan. Update it as omega criteria flip and attack plan items complete. Never overwrite — create versioned revisions per plan file discipline.*
