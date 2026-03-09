---
sop: true
name: legal-compliance-matrix
scope: system
phase: foundation
triggers:
  - context:new-product
  - context:revenue-activation
  - context:jurisdiction-change
complements:
  - contract-risk-analyzer
  - gdpr-compliance-check
  - security-threat-modeler
overrides: null
---
# SOP: Legal & Compliance Matrix

**Version:** 1.0.0 | **Date:** March 8, 2026 | **Status:** Active
**Scope:** Jurisdiction-aware compliance checklist process — which legal artifacts are needed at each lifecycle phase, how to evaluate regulatory exposure, and when human legal counsel (H:LC) must be engaged vs. when AI agents can draft.

---

## 1. Ontological Purpose

Legal compliance is not a checkbox exercise performed at launch — it is a living guardrail system that activates progressively as a product organism matures. A genesis-phase product needs different legal protections than a graduated one handling payments and personal data. This SOP defines which legal artifacts are required at each lifecycle phase, maps them to jurisdictions, and establishes clear boundaries between what AI agents can draft and what requires human legal review.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 5: Planning & Design)
**Cross-reference:** `SOP--business-organism-design.md` (organism phases map to compliance phases), `SOP--product-deployment-and-revenue-activation.md` (deployment triggers compliance checks), `SOP--security-and-accessibility-audit.md` (security audit feeds compliance matrix)

---

## 2. Trigger

Execute this SOP when:
- A new commercial product (ORGAN-III) is being designed
- A product is transitioning to revenue activation (accepting payments)
- The product expands to a new jurisdiction or user base
- A regulatory change affects the product's domain (e.g., AI regulation, data privacy)
- Annual compliance review cycle (every 12 months for graduated products)

**Exception:** Internal tools, open-source libraries, and infrastructure repos without user-facing data handling do not require a full compliance matrix.

---

## 3. Phase I: Regulatory Exposure Assessment

**Goal:** Determine which regulatory domains apply to this product.

### Process

1. **Identify data types handled:**
   - Personal Identifiable Information (PII)
   - Financial data (payment info, bank details)
   - Health data (PHI under HIPAA)
   - Children's data (COPPA)
   - Behavioral/usage data (analytics, tracking)
   - AI-generated content (EU AI Act considerations)

2. **Identify jurisdictions:**
   - Where is the product hosted? (data residency)
   - Where are users located? (regulatory reach)
   - Where is the business entity incorporated?

3. **Map to regulatory frameworks:**

| Data Type | US | EU/UK | CA | AU |
|-----------|-----|-------|-----|-----|
| PII | State privacy laws (CCPA, etc.) | GDPR | PIPEDA | APPs |
| Financial | PCI-DSS, state MSB laws | PSD2, GDPR | PCMLTFA | AML/CTF Act |
| Health | HIPAA | GDPR Art. 9 | PHIPA | My Health Records Act |
| Children | COPPA | GDPR Art. 8 | PIPEDA | Privacy Act |
| AI Content | FTC guidance, state AI laws | EU AI Act | AIDA (proposed) | — |

4. **Score exposure level:**
   - **LOW** — no PII, no payments, no regulated domain
   - **MEDIUM** — collects PII (email, name), processes payments
   - **HIGH** — handles sensitive data (health, financial, children), multi-jurisdiction

### Output
A regulatory exposure assessment with data types, jurisdictions, and exposure level.

---

## 4. Phase II: Compliance Artifact Inventory

**Goal:** Determine which legal documents are needed and when.

### Artifact-to-Phase Matrix

| Artifact | Phase | Exposure Level | AI-Draftable? | H:LC Required? |
|----------|-------|---------------|---------------|----------------|
| IP Assignment & Open-Source Policy | genesis | ALL | Yes (template) | Review recommended |
| Founder/Contractor Agreement | genesis | ALL | Yes (template) | Review required for equity/IP |
| Compliance Guardrails Matrix | foundation | MEDIUM+ | Yes | No |
| Regulatory Risk Register | foundation | MEDIUM+ | Yes | Review for HIGH |
| Terms of Service (ToS) | hardening | ALL | Yes (draft) | Review required before publish |
| Privacy Policy | hardening | MEDIUM+ | Yes (draft) | Review required before publish |
| Cookie/Consent Banner | hardening | MEDIUM+ (EU users) | Yes | No |
| Data Processing Agreement (DPA) | graduation | HIGH | No — H:LC drafts | Yes |
| Subprocessor List | graduation | HIGH | Yes | Review required |
| DPIA (Data Protection Impact Assessment) | graduation | HIGH (GDPR) | Partial | Yes |
| Security Audit Report | graduation | MEDIUM+ | Yes (via SOP) | No |
| SOC 2 / ISO 27001 prep | graduation+ | HIGH (enterprise) | Partial | Yes (auditor) |

### AI Agent Boundaries

**AI agents (styx-legal persona) MAY:**
- Draft initial versions of ToS, Privacy Policy, IP Assignment using templates
- Maintain the Compliance Guardrails Matrix
- Track regulatory changes and flag exposure
- Generate the Regulatory Risk Register
- Prepare DPA templates from standard frameworks

**AI agents MUST NOT:**
- Provide legal advice or render legal opinions
- Finalize documents that create binding legal obligations without H:LC review
- Assess novel regulatory questions without flagging for human review
- Sign or authorize any legal document

**H:LC (Human Legal Counsel) MUST:**
- Review all documents before they are published or signed
- Make final determinations on regulatory exposure classification for HIGH-exposure products
- Draft or substantially modify DPAs, SLAs, and equity agreements
- Advise on jurisdiction-specific compliance for multi-national products

---

## 5. Phase III: Guardrails Matrix Construction

**Goal:** Build the living compliance guardrails document for the product.

### Process

1. Create `docs/legal/compliance-guardrails.md` with this structure:

```markdown
# Compliance Guardrails — {Product Name}

## Exposure Assessment
- **Level:** LOW | MEDIUM | HIGH
- **Data types:** {list}
- **Jurisdictions:** {list}
- **Regulatory frameworks:** {list}

## Required Artifacts

| Artifact | Phase | Status | Owner | Last Reviewed |
|----------|-------|--------|-------|---------------|
| ... | ... | Draft / Reviewed / Published / N/A | ... | YYYY-MM-DD |

## Guardrails (Active)

| # | Rule | Source | Enforcement |
|---|------|--------|-------------|
| 1 | No PII stored without encryption at rest | GDPR Art. 32 | Code review + CI check |
| 2 | Payment processing via PCI-compliant provider only | PCI-DSS | Architecture ADR |
| ... | ... | ... | ... |

## Open Questions (for H:LC)

| # | Question | Context | Priority |
|---|----------|---------|----------|
| 1 | ... | ... | HIGH/MEDIUM/LOW |
```

2. Link each guardrail to an enforcement mechanism (code check, CI, architecture constraint, or manual review).

3. Review and update quarterly for graduated products.

### Output
A compliance guardrails matrix document with artifact inventory, active guardrails, and open questions.

---

## 6. Regulatory Risk Register

**Goal:** Track known and emerging regulatory risks.

### Format

```markdown
# Regulatory Risk Register — {Product Name}

| # | Risk | Framework | Likelihood | Impact | Mitigation | Status | Owner |
|---|------|-----------|------------|--------|------------|--------|-------|
| 1 | EU user data stored outside EU | GDPR | Medium | High | Evaluate EU hosting option | Open | styx-legal |
| 2 | AI-generated content liability | EU AI Act | Low | Medium | Add disclosure labels | Mitigated | styx-legal |
```

---

## 7. Output Artifacts

- Regulatory exposure assessment
- Compliance artifact inventory (per-phase matrix)
- Compliance guardrails matrix (`docs/legal/compliance-guardrails.md`)
- Regulatory risk register (`docs/legal/regulatory-risk-register.md`)
- Open questions list for H:LC review

---

## 8. Verification

- [ ] Exposure level assessed (LOW/MEDIUM/HIGH) with data types and jurisdictions
- [ ] All required artifacts for the current lifecycle phase identified
- [ ] AI vs. H:LC boundaries clearly marked for each artifact
- [ ] Guardrails matrix links each rule to an enforcement mechanism
- [ ] Risk register has no unowned risks
- [ ] Documents flagged for H:LC review are not published without sign-off

---

## 9. Starter Research Questions

- What data does this product collect, process, or store?
- In which countries/states are your users located?
- Does the product use AI/ML in any user-facing capacity?
- Are there industry-specific regulations (fintech, healthtech, edtech)?
- What third-party services process user data on your behalf?
- Does the product target or could it attract users under 13/16?

---

*Version: 1.0.0 | System-Wide Directive | ORGANVM*
