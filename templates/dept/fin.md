# FIN — Finance & Revenue Department Templates

**Persona:** styx-finance
**Linked Skills:** `systemic-product-analyst` (partial coverage)

---

## Auto-Pull (all artifacts)

- From `seed.yaml`: product name, organ, tier
- From `registry-v2.json`: revenue_model, revenue_status, promotion_status
- From `package.json` / `pyproject.toml`: dependencies (detect payment processors — Stripe, LemonSqueezy, Paddle)
- From `docs/planning/prd.md` (P1): success metrics
- From `docs/marketing/gtm-strategy.md` (G1): launch phases, competitive landscape
- From `docs/operations/cost-management.md` (O5): infrastructure costs

## Questions (ask once, shared across F1-F6)

1. What is your pricing model? (flat / tiered / usage-based / freemium / one-time)
2. What is your target monthly revenue at steady state?
3. What is your current monthly burn rate (infrastructure + subscriptions)?

---

## F1: Unit Economics Model

**Phase:** genesis
**Governing SOP:** `SOP--business-organism-design.md`
**Output:** `docs/finance/unit-economics.md`

### Generation Instructions

1. Read revenue model from registry
2. Read dependencies for payment processing fees (Stripe = 2.9% + $0.30)
3. Read infrastructure costs from O5 if available, else estimate from provider + dependencies
4. Calculate per-unit margins

### Template

```markdown
# Unit Economics — {product_name}

**Revenue Model:** {from registry}
**Status:** {revenue_status from registry}

## Per-Unit Economics

| Metric | Value | Source |
|--------|-------|--------|
| Price per unit | {from Question 1 context} | Founder input |
| COGS per unit | {infrastructure per user + AI tokens per request} | Estimated |
| Payment processing | {2.9% + $0.30 if Stripe in deps} | Provider |
| Gross margin per unit | {calculated} | Derived |
| Gross margin % | {calculated} | Derived |

## Variable Costs

| Cost | Per | Amount | Notes |
|------|-----|--------|-------|
| AI API tokens | request | ${est.} | {from deps — OpenAI, Anthropic, etc.} |
| Database queries | user/mo | ${est.} | {from DB provider pricing} |
| Bandwidth | GB | ${est.} | {from hosting provider} |
| Payment processing | transaction | 2.9% + $0.30 | {Stripe / other} |

## Fixed Costs

| Cost | Monthly | Notes |
|------|---------|-------|
| Hosting | ${amount} | {from Question 3 or O5} |
| Domain | ${amount/12} | Annual prorated |
| SaaS tools | ${amount} | {monitoring, email, etc.} |
| **Total fixed** | **${total}** | |

## Break-Even Analysis

- **Fixed costs / gross margin per unit = break-even users:** {calculated}
- **At target revenue ({Question 2}): {calculated} units needed**

## LTV/CAC Projection

| Metric | Optimistic | Expected | Pessimistic |
|--------|-----------|----------|-------------|
| Monthly churn | 2% | 5% | 10% |
| Avg. lifetime (months) | 50 | 20 | 10 |
| LTV | ${calc} | ${calc} | ${calc} |
| Target CAC | < ${LTV/3} | < ${LTV/3} | < ${LTV/3} |
```

---

## F2: Pricing Strategy & Tier Design

**Phase:** foundation
**Governing SOP:** `SOP--business-organism-design.md`
**Output:** `docs/finance/pricing-strategy.md`

### Generation Instructions

1. Read revenue model and unit economics (F1)
2. Read competitive landscape from G1 if available
3. Design tier structure based on pricing model (Question 1)

### Template

```markdown
# Pricing Strategy — {product_name}

**Model:** {from Question 1}
**Competitive range:** {from G1 competitive landscape}

## Tier Design

| Tier | Price | Target User | Key Features | Limits |
|------|-------|-------------|-------------|--------|
| Free | $0 | {trial users} | {core features} | {usage limits} |
| Pro | ${price}/mo | {primary persona} | {all features} | {higher limits} |
| Enterprise | Custom | {B2B buyers} | {everything + SLA + support} | Unlimited |

## Pricing Rationale

- **Anchor:** {Pro tier is the default — priced for margin}
- **Free tier purpose:** {acquisition funnel — not sustainable long-term}
- **Enterprise:** {deployed only when B2B demand materializes}

## Billing Implementation

- **Provider:** {from deps — Stripe / LemonSqueezy / Paddle}
- **Billing cycle:** {monthly / annual with discount}
- **Trial period:** {7/14/30 days}

## Price Change Policy

{How price increases are communicated — grandfathering? Notice period?}
```

---

## F3: Financial Projections (3-Scenario)

**Phase:** foundation
**Governing SOP:** `SOP--business-organism-design.md` (Phase II)
**Output:** `docs/finance/financial-projections.md`

### Generation Instructions

1. Read unit economics (F1) for margin structure
2. Read GTM strategy (G1) for growth assumptions
3. Apply three-scenario model from SOP--business-organism-design.md §4
4. Project 12 months

### Template

```markdown
# Financial Projections — {product_name}

**Period:** Month 1-12
**Base date:** {today}

## Assumptions

| Parameter | Optimistic | Expected | Pessimistic |
|-----------|-----------|----------|-------------|
| Monthly user growth | 30% | 15% | 5% |
| Conversion rate | 8% | 4% | 2% |
| Monthly churn | 2% | 5% | 10% |
| ARPU | ${high} | ${mid} | ${low} |

## 12-Month Projection

| Month | Users (Opt) | MRR (Opt) | Users (Exp) | MRR (Exp) | Users (Pes) | MRR (Pes) |
|-------|------------|-----------|------------|-----------|------------|-----------|
| 1 | ... | ... | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... | ... | ... |
| 6 | ... | ... | ... | ... | ... | ... |
| 12 | ... | ... | ... | ... | ... | ... |

## Break-Even Timeline

| Scenario | Break-even month | Monthly burn until then |
|----------|-----------------|----------------------|
| Optimistic | {month} | ${burn from Question 3} |
| Expected | {month} | ${burn} |
| Pessimistic | {month or "not within 12 months"} | ${burn} |

## Decision Points

- **Month 3:** If actual growth < pessimistic, evaluate pivot or sunset
- **Month 6:** If not on expected trajectory, reduce burn or seek funding
- **Month 12:** Annual review — adjust all assumptions with actuals
```

---

## F4: Revenue Reconciliation Procedure

**Phase:** graduation
**Governing SOP:** `SOP--product-deployment-and-revenue-activation.md`
**Output:** `docs/finance/revenue-reconciliation.md`

### Template

```markdown
# Revenue Reconciliation — {product_name}

**Billing provider:** {from deps}
**Cadence:** Monthly

## Monthly Checklist

- [ ] Download billing provider report for the period
- [ ] Match transactions to user accounts
- [ ] Identify and investigate discrepancies
- [ ] Record refunds and chargebacks
- [ ] Update MRR/ARR tracking
- [ ] Compare actual vs. projected (F3)
- [ ] File for tax purposes

## Key Metrics to Track

| Metric | How to Calculate | Where |
|--------|-----------------|-------|
| MRR | Sum of active subscriptions | Billing dashboard |
| ARR | MRR × 12 | Calculated |
| Churn rate | Lost subs / total subs | Billing dashboard |
| Net revenue retention | (MRR + expansion - churn) / previous MRR | Calculated |

## Tax Obligations

{Based on Question 1 (jurisdictions from LEG) — sales tax, VAT, income tax.}
```

---

## F5: Runway & Burn Rate Tracker

**Phase:** foundation
**Governing SOP:** references F1 (unit economics)
**Output:** `docs/finance/runway-tracker.md`

### Template

```markdown
# Runway & Burn Rate — {product_name}

**Last updated:** {today}

## Current State

| Metric | Value |
|--------|-------|
| Monthly burn | ${from Question 3} |
| Monthly revenue | ${current or 0} |
| Net burn | ${burn - revenue} |
| Cash on hand | ${ask if not inferrable} |
| Runway | {cash / net_burn} months |

## Monthly Tracking

| Month | Revenue | Expenses | Net | Runway Remaining |
|-------|---------|----------|-----|-----------------|
| {month 1} | ... | ... | ... | ... |

## Burn Reduction Levers

| Action | Savings | Impact |
|--------|---------|--------|
| {Downgrade hosting} | ${amount}/mo | {tradeoff} |
| {Remove paid service X} | ${amount}/mo | {tradeoff} |

## Funding Triggers

- **< 6 months runway:** Begin fundraising or revenue push
- **< 3 months runway:** Emergency burn reduction
- **< 1 month runway:** Evaluate shutdown vs. pivot
```

---

## F6: Grant/Funding Application Template

**Phase:** any
**Governing SOP:** T1 skill `grant-proposal-writer`
**Output:** `docs/finance/funding-application.md`

### Template

```markdown
# Funding Application Template — {product_name}

## Project Summary
{One paragraph: what, why, who, how.}

## Problem Statement
{The problem this product addresses — from P1 if available.}

## Proposed Solution
{How the product solves it — technical and user-facing.}

## Impact
{Who benefits and how — quantified where possible.}

## Budget

| Category | Amount | Justification |
|----------|--------|---------------|
| Infrastructure | ${amount} | {hosting, APIs, databases} |
| Development | ${amount} | {labor or AI token costs} |
| Marketing | ${amount} | {launch, content, outreach} |
| Legal | ${amount} | {incorporation, compliance} |
| **Total** | **${total}** | |

## Timeline

| Phase | Duration | Deliverables |
|-------|----------|-------------|
| {phase 1} | {months} | {what will be delivered} |

## Team
{Founder background, AI agent workforce model, advisory.}

## Sustainability
{How the project sustains itself after grant period — revenue model.}
```

---

*Generates 6 artifacts: F1 (unit economics), F2 (pricing), F3 (projections), F4 (reconciliation), F5 (runway), F6 (funding application)*
