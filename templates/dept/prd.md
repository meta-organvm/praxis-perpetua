# PRD — Product & Design Department Templates

**Persona:** styx-product
**Linked Skills:** `product-requirements-designer`, `systemic-product-analyst`, `responsive-design-patterns`, `accessibility-patterns`

---

## Auto-Pull (all artifacts)

- From `seed.yaml`: product name, organ, tier, produces/consumes edges, event subscriptions
- From `registry-v2.json`: revenue_model, implementation_status, promotion_status
- From `README.md`: product description, features, target audience
- From `docs/research/`: existing research (market analysis, user studies)
- From `docs/planning/`: existing roadmaps, sprint plans
- From `src/`: feature modules, UI components (infer feature set)

## Questions (ask once, shared across P1-P5)

1. What problem does this product solve in one sentence?
2. Who is your primary user? (1-2 sentences describing the person, not the segment)
3. What is the single most important metric for this product? (e.g., DAU, conversion rate, retention)

---

## P1: Product Requirements Document (PRD)

**Phase:** genesis
**Governing SOP:** T1 skill `product-requirements-designer`
**Output:** `docs/planning/prd.md`

### Generation Instructions

1. Read product description from `README.md` + `seed.yaml`
2. Read existing research docs for market context
3. Scan `src/` for feature modules — infer current capabilities
4. Structure requirements as user stories grouped by epic

### Template

```markdown
# Product Requirements Document — {product_name}

**Version:** {from manifest}
**Owner:** styx-product
**Status:** {Draft | Approved}

## 1. Problem Statement
{From Question 1 — the core problem in one sentence.}

## 2. Target User
{From Question 2 — specific person, not a demographic.}

## 3. Success Metrics
{From Question 3 — the north star metric + 2-3 supporting metrics.}

## 4. Requirements

### Epic 1: {Core Value}

| ID | User Story | Priority | Status | Notes |
|----|-----------|----------|--------|-------|
| US-001 | As a {user}, I want to {action} so that {outcome} | P0 | {Implemented/Planned} | {infer from src/} |

### Epic 2: {Supporting Feature}
{...}

## 5. Out of Scope
{What this version explicitly does NOT include.}

## 6. Dependencies
{From seed.yaml consumes edges — what external systems are required?}

## 7. Open Questions
{Unresolved product decisions.}
```

---

## P2: User Persona Profiles

**Phase:** genesis
**Governing SOP:** `SOP--market-gap-analysis.md`
**Output:** `docs/planning/user-personas.md`

### Generation Instructions

1. Use Question 2 as the primary persona seed
2. Read market research from `docs/research/` if available
3. Read `seed.yaml` event subscriptions — what user actions are modeled?
4. Generate 2-3 personas (primary, secondary, anti-persona)

### Template

```markdown
# User Persona Profiles — {product_name}

## Primary Persona: {Name}

**Role:** {job title / role}
**Demographics:** {age range, tech comfort, relevant context}
**Goals:**
- {What they are trying to accomplish}
**Pain Points:**
- {What frustrates them about current solutions}
**How {product_name} helps:**
- {Specific value delivered}

## Secondary Persona: {Name}
{Same structure — a different user segment.}

## Anti-Persona: {Name}
{Who this product is NOT for — and why. Prevents scope creep.}
```

---

## P3: UX Audit Report

**Phase:** hardening
**Governing SOP:** `SOP--stranger-test-protocol.md`
**Output:** `docs/planning/ux-audit.md`

### Generation Instructions

1. Run the stranger test protocol from the governing SOP
2. Walk through all user-facing interfaces
3. Check against accessibility patterns (T1 skill)
4. Score usability on a 5-point scale per category

### Template

```markdown
# UX Audit Report — {product_name}

**Date:** {today}
**Auditor:** styx-product
**Method:** Stranger Test Protocol + Accessibility Patterns

## Summary Score

| Category | Score (1-5) | Notes |
|----------|-------------|-------|
| First Impression (< 5s) | ... | ... |
| Navigation | ... | ... |
| Core Task Completion | ... | ... |
| Error Handling | ... | ... |
| Accessibility | ... | ... |
| **Overall** | ... | ... |

## Findings

### Critical (blocks graduation)
1. {finding}

### Major (should fix before launch)
1. {finding}

### Minor (nice to fix)
1. {finding}

## Recommendations
{Prioritized action items with effort estimates.}
```

---

## P4: Feature Prioritization Matrix

**Phase:** foundation
**Governing SOP:** `SOP--planning-and-roadmapping.md`
**Output:** `docs/planning/feature-matrix.md`

### Generation Instructions

1. Read PRD (P1) for full feature list
2. Score each feature on impact (1-5) and effort (1-5)
3. Calculate priority score = impact / effort
4. Sort by priority score descending

### Template

```markdown
# Feature Prioritization Matrix — {product_name}

**Method:** Impact/Effort scoring
**Date:** {today}

| # | Feature | Impact (1-5) | Effort (1-5) | Priority Score | Phase | Status |
|---|---------|-------------|-------------|----------------|-------|--------|
| 1 | {feature} | 5 | 2 | 2.5 | foundation | Implemented |
| 2 | {feature} | 4 | 4 | 1.0 | hardening | Planned |

## Quadrant View

### Quick Wins (High Impact, Low Effort)
- ...

### Strategic Bets (High Impact, High Effort)
- ...

### Fill-ins (Low Impact, Low Effort)
- ...

### Deprioritize (Low Impact, High Effort)
- ...
```

---

## P5: A/B Test Design & Results Log

**Phase:** graduation
**Governing SOP:** `SOP--strategic-foresight-and-futures.md`
**Output:** `docs/planning/ab-test-log.md`

### Generation Instructions

1. Read success metrics from P1
2. Identify testable hypotheses from feature matrix (P4)
3. Design test structure — control, variant, sample size, duration
4. Create logging template for results

### Template

```markdown
# A/B Test Log — {product_name}

## Test Index

| # | Name | Hypothesis | Status | Winner | Date |
|---|------|-----------|--------|--------|------|
| 1 | {name} | {hypothesis} | {Planned/Running/Complete} | {A/B/None} | ... |

## Test 1: {Name}

**Hypothesis:** {If we change X, then Y will improve by Z%}
**Metric:** {from P1 success metrics}
**Control (A):** {current behavior}
**Variant (B):** {proposed change}
**Sample size:** {calculated or estimated}
**Duration:** {days/weeks}

### Results
{When complete — metrics, statistical significance, decision.}
```

---

*Generates 5 artifacts: P1 (PRD), P2 (user personas), P3 (UX audit), P4 (feature matrix), P5 (A/B test log)*
