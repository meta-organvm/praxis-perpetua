# B2B — Enterprise Sales Department Templates

**Persona:** styx-sales
**Linked Skills:** `freelance-client-ops`, `networking-outreach`

---

## Auto-Pull (all artifacts)

- From `seed.yaml`: product name, organ, tier, produces/consumes edges
- From `registry-v2.json`: revenue_model, revenue_status, description
- From `docs/planning/prd.md` (P1): features, success metrics
- From `docs/planning/user-personas.md` (P2): personas (adapt for enterprise buyers)
- From `docs/finance/pricing-strategy.md` (F2): tier design, enterprise pricing
- From `docs/marketing/gtm-strategy.md` (G1): competitive landscape, positioning
- From `docs/legal/compliance-guardrails.md` (L1): compliance certifications, data handling
- From `docs/operations/incident-response.md` (O1): SLA and uptime data
- From `docs/architecture/overview.md` (E2): architecture, security posture

## Questions (ask once, shared across B1-B6)

1. Are you selling B2B, B2C, or B2B2C?
2. What is the average deal size you're targeting? (< $1K / $1-10K / $10K+ / month)

---

## B1: Ideal Customer Profile (ICP)

**Phase:** hardening
**Governing SOP:** `SOP--market-gap-analysis.md`
**Output:** `docs/enterprise/icp.md`

### Generation Instructions

1. Read user personas (P2) — translate consumer persona to enterprise buyer
2. Read competitive landscape (G1)
3. Read revenue model — what kind of company would pay for this?
4. Define ICP across firmographic, technographic, and behavioral dimensions

### Template

```markdown
# Ideal Customer Profile — {product_name}

## Firmographic Criteria

| Dimension | Ideal | Acceptable | Disqualifying |
|-----------|-------|------------|---------------|
| Company size | {employees} | {range} | {too small/large} |
| Industry | {target vertical} | {adjacent} | {regulated/incompatible} |
| Revenue | {range} | {range} | {below threshold} |
| Geography | {from LEG jurisdictions} | {adjacent} | {unsupported} |

## Technographic Criteria

| Dimension | Ideal | Notes |
|-----------|-------|-------|
| Tech stack | {compatible stack from E2} | ... |
| Current solution | {competitor or manual process} | ... |
| Integration needs | {from seed.yaml edges} | ... |

## Behavioral Criteria

- **Pain signal:** {what indicates they need this product}
- **Buying signal:** {what indicates they're ready to buy}
- **Champion profile:** {who inside the company would advocate}
- **Decision maker:** {who signs the check}

## Disqualification Criteria

- {Cannot integrate with required systems}
- {Below minimum viable deal size}
- {In a regulated vertical we don't support}
```

---

## B2: Outreach Sequence Templates

**Phase:** hardening
**Governing SOP:** T1 skill `networking-outreach`
**Output:** `docs/enterprise/outreach-sequences.md`

### Template

```markdown
# Outreach Sequences — {product_name}

## Sequence 1: Cold Outreach (ICP Match)

### Email 1 (Day 0)
**Subject:** {pain point} at {company_name}?
**Body:**
Hi {name},

I noticed {company_name} {specific observation — from LinkedIn, news, job posting}.

We built {product_name} to {one-line value prop}. {Specific relevance to their situation}.

Would a 15-minute call next week make sense?

### Email 2 (Day 3) — Follow-up
**Subject:** Re: {original subject}
**Body:** Quick follow-up — {add a case study or data point}. Worth a conversation?

### Email 3 (Day 7) — Value add
**Subject:** {Resource relevant to their pain point}
**Body:** {Share a blog post, guide, or insight — no ask, just value.}

### Email 4 (Day 14) — Breakup
**Subject:** Should I close the loop?
**Body:** {Acknowledge they're busy. Leave door open. Offer to reconnect in N months.}

## Sequence 2: Warm Introduction

{Shorter — mutual connection context, single email + follow-up.}

## Sequence 3: Inbound Qualification

{For enterprise leads who reach out — qualification questions + demo scheduling.}
```

---

## B3: Security Questionnaire (Pre-filled)

**Phase:** hardening
**Governing SOP:** `SOP--security-and-accessibility-audit.md`
**Output:** `docs/enterprise/security-questionnaire.md`

### Generation Instructions

1. Read E2 architecture overview — hosting, data flow, encryption
2. Read L1 compliance guardrails — certifications, data handling
3. Read O1 incident response — breach notification procedures
4. Pre-fill standard security questionnaire fields

### Template

```markdown
# Security Questionnaire — {product_name}

**Prepared for:** Enterprise prospects
**Last updated:** {today}

## Company Information

| Field | Response |
|-------|----------|
| Company name | {from seed.yaml org} |
| Product name | {product_name} |
| Year founded | {if available} |
| Number of employees | {founder + AI agents} |

## Data Handling

| Question | Response |
|----------|----------|
| What data do you collect? | {from L1 exposure assessment} |
| Where is data stored? | {from E2 — provider + region} |
| Is data encrypted at rest? | {from architecture} |
| Is data encrypted in transit? | {TLS — yes for all modern deployments} |
| Do you process PII? | {from L1} |
| Data retention policy? | {from L3 privacy policy} |

## Infrastructure

| Question | Response |
|----------|----------|
| Hosting provider | {from deployment config} |
| Multi-tenant or single-tenant? | {from architecture} |
| Backup frequency | {from O4} |
| Disaster recovery plan? | {from O4} |
| Uptime SLA | {from O1} |

## Access Control

| Question | Response |
|----------|----------|
| Authentication method | {from code — JWT, OAuth, etc.} |
| Role-based access control? | {from code} |
| MFA available? | {yes/no} |
| Audit logging? | {yes/no — from code} |

## Incident Response

| Question | Response |
|----------|----------|
| Incident response plan? | Yes — {reference O1} |
| Breach notification timeline | {from O1 + L1} |
| Post-incident review process? | Yes — {reference O1 postmortem} |

## Compliance

| Question | Response |
|----------|----------|
| GDPR compliant? | {from L1} |
| SOC 2 certified? | {status} |
| Penetration testing? | {last date or "planned"} |

## Additional Documentation

- Architecture overview: `docs/architecture/overview.md`
- Privacy policy: `docs/legal/privacy-policy.md`
- Incident response: `docs/operations/incident-response.md`
```

---

## B4: SLA Template

**Phase:** graduation
**Governing SOP:** T1 skill `contract-risk-analyzer`
**Output:** `docs/enterprise/sla-template.md`

### Template

```markdown
# Service Level Agreement — {product_name}

> **TEMPLATE — Requires review and customization per customer. H:LC review for binding agreements.**

## 1. Service Description
{From seed.yaml description.}

## 2. Availability

| Tier | Uptime Target | Measurement | Credits |
|------|--------------|-------------|---------|
| Standard | {99.9%} | Monthly | {5% per 0.1% below} |
| Enterprise | {99.99%} | Monthly | {10% per 0.01% below} |

**Excluded:** Scheduled maintenance (with 48h notice), force majeure, customer-caused issues.

## 3. Support Response Times

| Severity | Standard | Enterprise |
|----------|----------|------------|
| SEV-1 (service down) | < 4 hours | < 1 hour |
| SEV-2 (degraded) | < 8 hours | < 4 hours |
| SEV-3 (minor) | < 24 hours | < 8 hours |

## 4. Performance Targets

| Metric | Target |
|--------|--------|
| API response time (p95) | < 500ms |
| Error rate | < 0.1% |
| Data durability | 99.999% |

## 5. Reporting
{Monthly SLA report delivered via email/dashboard.}

## 6. Remedies
{Service credits for SLA violations — calculated as % of monthly fee.}
```

---

## B5: Demo Script & Walkthrough

**Phase:** graduation
**Governing SOP:** `SOP--pitch-deck-rollout.md`
**Output:** `docs/enterprise/demo-script.md`

### Template

```markdown
# Demo Script — {product_name}

**Duration:** 20 minutes (15 demo + 5 Q&A)
**Audience:** {ICP from B1 — decision maker + champion}

## Opening (2 min)

"Thanks for taking the time. I want to show you how {product_name} solves {pain point}."

{Personalize: reference their company, their specific challenge.}

## Problem Statement (2 min)

{From P1 — the problem in their language, not ours.}

"Most {persona} currently {painful status quo}. This costs {time/money/frustration}."

## Demo Flow (10 min)

### Scene 1: {Core Value} (4 min)
1. {Step-by-step walkthrough of primary feature}
2. {Show the "aha moment"}
3. {Highlight what would take them {X hours} manually}

### Scene 2: {Differentiator} (3 min)
1. {Show what competitors can't do}
2. {Highlight unique approach}

### Scene 3: {Enterprise Feature} (3 min)
1. {Admin controls / SSO / audit logs / API}
2. {Integration with their stack}

## Closing (1 min)

"Based on what you've seen, would {product_name} solve the {pain point} we discussed?"

## Q&A Preparation

| Likely Question | Answer |
|----------------|--------|
| "How does pricing work?" | {reference F2} |
| "What about security?" | {reference B3} |
| "Can you integrate with X?" | {reference E3 API spec} |
| "What's your uptime?" | {reference B4 SLA} |
```

---

## B6: Enterprise Pricing Proposal

**Phase:** graduation
**Governing SOP:** `SOP--business-organism-design.md`
**Output:** `docs/enterprise/pricing-proposal.md`

### Template

```markdown
# Enterprise Pricing Proposal — {product_name}

**Prepared for:** {company_name}
**Date:** {today}
**Valid until:** {today + 30 days}

## Solution Summary

{1 paragraph: what they get, tailored to their ICP profile.}

## Pricing

| Component | Description | Price |
|-----------|-------------|-------|
| {product_name} Enterprise | {N} seats, all features | ${amount}/mo |
| Onboarding | {setup, training, migration} | ${amount} one-time |
| Priority support | {SLA from B4} | Included |
| **Total Year 1** | | **${total}** |

## What's Included

- {All features from Pro tier}
- {Enterprise-specific features — SSO, audit, custom integrations}
- {SLA guarantees from B4}
- {Priority support from C3}
- {Quarterly business reviews}

## Implementation Timeline

| Phase | Duration | Deliverables |
|-------|----------|-------------|
| Onboarding | {weeks} | {setup, data migration} |
| Training | {days} | {admin + user training} |
| Go-live | Day {N} | Production deployment |

## Terms

{Reference ToS (L2), SLA (B4), DPA (L4 if applicable).}
```

---

*Generates 6 artifacts: B1 (ICP), B2 (outreach sequences), B3 (security questionnaire), B4 (SLA), B5 (demo script), B6 (pricing proposal)*
