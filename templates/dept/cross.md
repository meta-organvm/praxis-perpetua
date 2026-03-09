# CROSS — Cross-Cutting Department Templates

**Persona:** varies per artifact
**Covers:** checklists, planning, brainstorm, pitch, thesis, ADR, research

---

## Auto-Pull (all artifacts)

- From `seed.yaml`: product name, organ, tier, status, produces/consumes edges
- From `registry-v2.json`: promotion_status, implementation_status, revenue_model
- From `docs/`: all existing documents (to identify what's written vs. scaffolded)
- From `.github/workflows/`: CI status, test results
- From `CLAUDE.md`: tech stack, project context

---

## X1: Phase Gate Checklist

**Phase:** any
**Persona:** styx-ops (cross-cutting)
**Governing SOP:** `SOP--promotion-and-state-transitions.md`
**Output:** `docs/checklists/phase-gate-{phase}.md`

### Generation Instructions

1. Read current promotion_status from registry
2. Determine which phase gate is next (LOCAL→CANDIDATE, CANDIDATE→PUBLIC_PROCESS, etc.)
3. Read the promotion SOP for gate criteria
4. Cross-reference existing docs to check off requirements
5. Generate one checklist per relevant transition

### Template

```markdown
# Phase Gate Checklist — {product_name}

**Current status:** {promotion_status}
**Target:** {next_status}
**Date:** {today}

## Prerequisites

### Code Quality
- [ ] All tests passing
- [ ] Lint clean (ruff / eslint)
- [ ] No critical security vulnerabilities
- [ ] Test coverage ≥ {threshold}%

### Documentation
- [ ] README complete per `SOP--readme-and-documentation.md`
- [ ] CLAUDE.md present and current
- [ ] seed.yaml valid
- [ ] Architecture overview (E2) exists

### Governance
- [ ] Registry entry up to date
- [ ] CI workflow configured and green
- [ ] Pitch deck generated (`organvm pitch sync`)

### Phase-Specific

#### LOCAL → CANDIDATE
- [ ] Core features implemented
- [ ] Basic test suite exists
- [ ] Development docs present

#### CANDIDATE → PUBLIC_PROCESS
- [ ] Stranger test passed (P3)
- [ ] Security audit completed
- [ ] Legal docs reviewed (L1 at minimum)
- [ ] Deployment procedure documented (O2)

#### PUBLIC_PROCESS → GRADUATED
- [ ] Revenue activation (if commercial)
- [ ] Monitoring in place (O3)
- [ ] Support playbook exists (C3)
- [ ] 30-day soak test passed

## Sign-off

| Role | Name | Date | Approved? |
|------|------|------|-----------|
| Engineering | styx-engineering | ... | [ ] |
| Product | styx-product | ... | [ ] |
| Founder | H:FO | ... | [ ] |
```

---

## X2: Sprint/Phase Planning Document

**Phase:** any
**Persona:** styx-ops (cross-cutting)
**Governing SOP:** `SOP--planning-and-roadmapping.md`
**Output:** `docs/planning/phase-{N}-plan.md`

### Template

```markdown
# Phase {N} Plan — {product_name}

**Phase:** {genesis | foundation | hardening | graduation}
**Duration:** {estimated weeks}
**Start:** {date}
**End:** {target date}

## Objectives

1. {Primary objective — what must be true to exit this phase}
2. {Secondary objective}
3. {Stretch goal}

## Department Activation

| Department | Active? | Key Deliverables |
|-----------|---------|-----------------|
| ENG | Yes | {list} |
| LEG | {Yes/No} | {list or "—"} |
| PRD | {Yes/No} | {list or "—"} |
| OPS | {Yes/No} | {list or "—"} |
| GRO | {Yes/No} | {list or "—"} |
| FIN | {Yes/No} | {list or "—"} |
| CXS | {Yes/No} | {list or "—"} |
| B2B | {Yes/No} | {list or "—"} |

## Task Breakdown

| # | Task | Department | Persona | Priority | Effort | Status |
|---|------|-----------|---------|----------|--------|--------|
| 1 | ... | ENG | styx-engineering | P0 | ... | ... |

## Dependencies

{What must be completed before this phase can start/end?}

## Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| ... | ... | ... | ... |

## Exit Criteria

- [ ] {Criterion 1}
- [ ] {Criterion 2}
- [ ] Phase gate checklist (X1) passed
```

---

## X3: Monthly Calendar & Status

**Phase:** any
**Persona:** styx-ops (cross-cutting)
**Governing SOP:** `SOP--planning-and-roadmapping.md`
**Output:** `docs/planning/monthly-{YYYY-MM}.md`

### Template

```markdown
# Monthly Status — {product_name} — {YYYY-MM}

## Key Metrics

| Metric | Start of Month | End of Month | Change |
|--------|---------------|-------------|--------|
| Users | ... | ... | ... |
| Revenue (MRR) | ... | ... | ... |
| Test coverage | ... | ... | ... |
| Open issues | ... | ... | ... |

## Accomplishments

1. {What was shipped}
2. {What was resolved}

## In Progress

1. {Ongoing work — carry forward}

## Blocked

1. {What's stuck and why}

## Next Month Priorities

1. {Top priority}
2. {Second priority}
3. {Third priority}

## Lessons Learned

{One or two insights from this month's work.}
```

---

## X4: Brainstorm Transcript Scaffold

**Phase:** any
**Persona:** varies
**Governing SOP:** `SOP--session-self-critique.md`
**Output:** `docs/brainstorm/{date}-{topic}.md`

### Template

```markdown
# Brainstorm — {topic}

**Date:** {today}
**Participants:** {personas or humans involved}
**Duration:** {estimated}
**Status:** Raw | Refined | Archived

## Prompt / Question

{The original question or problem that triggered this brainstorm.}

## Ideas (unfiltered)

1. {idea}
2. {idea}
3. {idea}
...

## Clustering

### Theme A: {label}
- Ideas: {1, 3, ...}
- Feasibility: {high/med/low}

### Theme B: {label}
- Ideas: {2, ...}
- Feasibility: {high/med/low}

## Decision

{Which ideas advance to planning? Which are parked? Why?}

## Next Steps

- [ ] {Action item from selected ideas}
- [ ] {File ADR if architecture-relevant}
- [ ] {Create planning doc (X2) if scope-worthy}
```

---

## X5: Pitch Deck Content

**Phase:** hardening
**Persona:** styx-growth
**Governing SOP:** `SOP--pitch-deck-rollout.md`
**Output:** `docs/pitch/content.md`

### Generation Instructions

1. Read seed.yaml + registry for identity and status
2. Read PRD (P1) for problem/solution
3. Read user personas (P2) for target audience
4. Read unit economics (F1) for business viability
5. Read GTM (G1) for market strategy
6. Read competitive landscape (G1) for positioning
7. Structure as slide-by-slide content

### Template

```markdown
# Pitch Deck Content — {product_name}

## Slide 1: Title
- {product_name}
- {one-line tagline}

## Slide 2: Problem
{From P1 — the pain point in user's language.}

## Slide 3: Solution
{What {product_name} does — demo screenshot or key flow.}

## Slide 4: How It Works
{3-step process or architecture diagram.}

## Slide 5: Market
{From G1 — TAM/SAM/SOM or market size indicator.}

## Slide 6: Business Model
{From F2 — pricing tiers, revenue model.}

## Slide 7: Traction
{Current metrics — users, revenue, growth rate.}

## Slide 8: Competition
{From G1 — positioning matrix or comparison table.}

## Slide 9: Team
{Founder + AI agent workforce model.}

## Slide 10: Ask
{What you're seeking — users, funding, partnerships, feedback.}
```

---

## X6: Academic Thesis Structure

**Phase:** any
**Persona:** styx-research
**Governing SOP:** `METADOC--research-standards.md`
**Output:** `docs/thesis/` (multi-file — one per chapter)

### Note

Thesis structure already exists as a de facto standard in Styx's `docs/thesis/` with 8 chapter files. This template captures the convention for reuse. Refer to `METADOC--research-standards.md` for methodology requirements. Each chapter should apply at least 3 of the 11 research lenses.

---

## X7: Architecture Decision Record

**Phase:** foundation+
**Persona:** styx-engineering
**Governing SOP:** `SOP--architecture-decision-records.md`
**Output:** `docs/adr/adr-NNN-{slug}.md`

### Note

This is an alias for E1 — same template, same SOP. Listed here for cross-cutting visibility since ADRs are referenced by multiple departments (ENG, OPS, B2B).

See `eng.md` → E1 for the full generation instructions and template.

---

## X8: Research Document

**Phase:** any
**Persona:** styx-research
**Governing SOP:** `METADOC--research-standards.md`
**Output:** `docs/research/{date}-{topic}.md`

### Note

Research documents follow the METADOC format with 11 lenses. The format is already well-established across 42 research files in Styx. Each research document should:

1. Apply at least 3 research lenses (archaeological, typological, genealogical, etc.)
2. Include a bibliography per `SOP--source-evaluation-and-bibliography.md`
3. Identify actionable implications (not just analysis)
4. Cross-reference related ADRs and planning documents

Refer to `METADOC--research-standards.md` for the full lens inventory and methodology.

---

*Generates 8 artifact types: X1 (phase gate), X2 (phase plan), X3 (monthly status), X4 (brainstorm), X5 (pitch content), X6 (thesis), X7 (ADR alias), X8 (research alias)*
