# CXS — Customer Success Department Templates

**Persona:** styx-cx
**Linked Skills:** (none dedicated — adapts `incident-response-commander`, `data-storytelling-analyst`)

---

## Auto-Pull (all artifacts)

- From `seed.yaml`: product name, organ, tier
- From `registry-v2.json`: revenue_model, promotion_status
- From `README.md`: product description, getting started guide
- From `docs/planning/prd.md` (P1): user personas, core features
- From `docs/planning/user-personas.md` (P2): primary persona pain points
- From `docs/operations/incident-response.md` (O1): severity levels, escalation
- From `docs/finance/pricing-strategy.md` (F2): tier structure

## Questions (ask once, shared across C1-C5)

1. What are your support channels? (email / chat / forum / in-app / GitHub Issues)
2. What is your expected response time for support requests? (< 1h / < 4h / < 24h / best effort)

---

## C1: FAQ / Help Center Articles

**Phase:** hardening
**Governing SOP:** `SOP--readme-and-documentation.md`
**Output:** `docs/customer-success/faq.md`

### Generation Instructions

1. Read README getting started guide — extract common setup steps
2. Read API spec (E3) — identify complex endpoints users ask about
3. Read product features — anticipate "how do I..." questions
4. Scan GitHub Issues (if public) for recurring questions
5. Generate 10-20 Q&A pairs grouped by category

### Template

```markdown
# FAQ — {product_name}

## Getting Started

### How do I sign up?
{From README or onboarding flow.}

### How do I {core action}?
{From primary user flow.}

### What are the system requirements?
{From README / docs.}

## Features

### How does {feature X} work?
{From feature documentation.}

### Can I {common request}?
{Yes/no with explanation.}

## Billing & Plans

### What plans are available?
{From F2 pricing strategy.}

### How do I upgrade/downgrade?
{Process description.}

### What is your refund policy?
{State policy.}

## Troubleshooting

### I'm getting error {common error}
{Diagnosis + fix.}

### {Common issue}
{Solution.}

## Contact

For questions not covered here: {from Question 1 — support channels}.
```

---

## C2: Onboarding Email Sequence

**Phase:** hardening
**Governing SOP:** `SOP--product-deployment-and-revenue-activation.md`
**Output:** `docs/customer-success/onboarding-sequence.md`

### Generation Instructions

1. Read user personas (P2) — what do they need to succeed?
2. Read core features — what's the "aha moment"?
3. Read pricing tiers — when does conversion make sense?
4. Design 5-email sequence over 14 days

### Template

```markdown
# Onboarding Email Sequence — {product_name}

**Trigger:** New user signup
**Duration:** 14 days, 5 emails
**Goal:** Get user to {aha moment} within 7 days

## Email 1: Welcome (Day 0)

**Subject:** Welcome to {product_name} — here's how to get started
**Content:**
- Thank you for signing up
- {1-2 sentence value reminder}
- Quick start: {3 steps to first value}
- Link to getting started guide

## Email 2: First Value (Day 2)

**Subject:** Did you try {core feature}?
**Content:**
- Highlight the #1 feature
- Step-by-step walkthrough
- Link to help docs

## Email 3: Deeper Engagement (Day 5)

**Subject:** {N}% of users love {feature} — have you tried it?
**Content:**
- Social proof or usage stat
- Second most valuable feature
- Tip or shortcut

## Email 4: Check-in (Day 9)

**Subject:** How's it going with {product_name}?
**Content:**
- Ask if they have questions
- Link to FAQ
- Invite to {community / feedback channel}

## Email 5: Conversion (Day 14)

**Subject:** Ready to unlock more?
**Content:**
- Summary of what they've accomplished
- What Pro/paid tier adds
- CTA to upgrade (if freemium model)
- Or: feedback request (if no freemium)
```

---

## C3: Support Playbook & Escalation

**Phase:** graduation
**Governing SOP:** T1 skill `incident-response-commander` (adapted for CX)
**Output:** `docs/customer-success/support-playbook.md`

### Generation Instructions

1. Read O1 incident response — adapt severity levels for support
2. Read FAQ (C1) — link to self-service answers
3. Define triage rules and escalation paths

### Template

```markdown
# Support Playbook — {product_name}

**Channels:** {from Question 1}
**Target response time:** {from Question 2}

## Triage Rules

| Category | Priority | Response | Resolution Target |
|----------|----------|----------|-------------------|
| Account access | High | {Question 2 time} | Same day |
| Billing issue | High | {time} | Same day |
| Bug report | Medium | {time} | 48 hours |
| Feature request | Low | {time} | Acknowledge only |
| General question | Low | {time} | Point to FAQ |

## Response Templates

### Account Issues
> Hi {name}, thanks for reaching out. I can help with your account. {resolution steps}...

### Bug Reports
> Thanks for reporting this. I've logged it as {issue link}. {workaround if available}...

### Feature Requests
> Great idea! I've added this to our feature tracker. {context on roadmap}...

## Escalation

| Level | Trigger | Action |
|-------|---------|--------|
| L1 | Standard support | FAQ + response templates |
| L2 | Technical issue | Escalate to styx-engineering |
| L3 | Data/security incident | Escalate per O1 incident response |

## Metrics

| Metric | Target |
|--------|--------|
| First response time | < {from Question 2} |
| Resolution time | < {2x response time} |
| CSAT | > 4.0/5.0 |
| Ticket volume trend | Decreasing (FAQ effectiveness) |
```

---

## C4: Churn Signal Detection Guide

**Phase:** graduation
**Governing SOP:** `SOP--strategic-foresight-and-futures.md`
**Output:** `docs/customer-success/churn-signals.md`

### Template

```markdown
# Churn Signal Detection — {product_name}

## Leading Indicators

| Signal | Detection Method | Risk Level | Intervention |
|--------|-----------------|------------|-------------|
| No login in 14 days | Usage analytics | High | Re-engagement email |
| Support ticket spike | Ticket volume | Medium | Proactive outreach |
| Downgrade request | Billing event | High | Retention conversation |
| Feature usage decline | Analytics | Medium | Usage tips email |
| Negative feedback | NPS/survey | High | Personal follow-up |

## Automated Alerts

| Trigger | Action | Owner |
|---------|--------|-------|
| {14 days inactive} | Send re-engagement email | Automated |
| {3+ tickets in 7 days} | Flag for manual review | styx-cx |
| {NPS < 7} | Schedule call or send survey | styx-cx |

## Retention Playbook

### For at-risk users
1. Identify the signal
2. Review their usage history
3. Reach out with specific, personalized help
4. Offer value (extended trial, feature unlock, onboarding session)
5. Document outcome
```

---

## C5: NPS Survey & Analysis Template

**Phase:** graduation
**Governing SOP:** T1 skill `data-storytelling-analyst`
**Output:** `docs/customer-success/nps-survey.md`

### Template

```markdown
# NPS Survey & Analysis — {product_name}

## Survey Design

**Question:** On a scale of 0-10, how likely are you to recommend {product_name} to a colleague?
**Follow-up:** What is the primary reason for your score?

**Distribution:** {in-app / email}
**Frequency:** {quarterly / after key milestones}
**Sample:** {all users / active users only}

## Analysis Framework

| Category | Score Range | Action |
|----------|-----------|--------|
| Promoters | 9-10 | Ask for testimonial/referral |
| Passives | 7-8 | Identify upgrade path |
| Detractors | 0-6 | Personal outreach, investigate pain |

## NPS Calculation

**NPS = % Promoters - % Detractors**

| Period | Responses | Promoters | Passives | Detractors | NPS |
|--------|-----------|-----------|----------|------------|-----|
| {Q1} | ... | ...% | ...% | ...% | ... |

## Action Items from Latest Survey

| Theme | Frequency | Action | Owner | Status |
|-------|-----------|--------|-------|--------|
| {common feedback} | {N mentions} | {planned response} | {persona} | {open/done} |
```

---

*Generates 5 artifacts: C1 (FAQ), C2 (onboarding emails), C3 (support playbook), C4 (churn signals), C5 (NPS survey)*
