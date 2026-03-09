# LEG — Legal & Compliance Department Templates

**Persona:** styx-legal
**Linked Skills:** `contract-risk-analyzer`, `gdpr-compliance-check`, `security-threat-modeler`

---

## Auto-Pull (all artifacts)

- From `seed.yaml`: product name, organ, tier, event subscriptions
- From `registry-v2.json`: revenue_model, revenue_status, promotion_status
- From `package.json` / `pyproject.toml`: dependencies (detect payment processors, analytics, auth providers)
- From `src/`: data models (detect PII fields), middleware (detect auth/consent mechanisms)
- From `docs/legal/`: existing legal documents (skip regeneration)
- From `.github/workflows/`: deployment targets (infer hosting jurisdiction)

## Questions (ask once, shared across L1-L7)

1. What jurisdictions do you operate in? (US-only / US+EU / Global)
2. Are you handling PII, financial data, or health data? (Confirm even if inferred from code)
3. Is there an existing business entity, or will one be formed? (LLC, C-Corp, sole prop)

---

## L1: Compliance Guardrails Matrix

**Phase:** foundation
**Governing SOP:** `SOP--legal-compliance-matrix.md`
**Output:** `docs/legal/compliance-guardrails.md`

### Generation Instructions

1. Run the regulatory exposure assessment from `SOP--legal-compliance-matrix.md` §3
2. Classify exposure level (LOW/MEDIUM/HIGH) based on data types + jurisdictions
3. Build the artifact inventory per the phase matrix in §4
4. Generate active guardrails tied to code-level enforcement

### Template

```markdown
# Compliance Guardrails — {product_name}

## Exposure Assessment

- **Level:** {LOW | MEDIUM | HIGH}
- **Data types:** {PII types from code inspection + Question 2}
- **Jurisdictions:** {from Question 1}
- **Regulatory frameworks:** {mapped per SOP §3 matrix}

## Required Artifacts (Current Phase: {phase})

| Artifact | Required Phase | Status | Owner | Last Reviewed |
|----------|---------------|--------|-------|---------------|
| IP Assignment | genesis | {Draft/N-A} | styx-legal | — |
| Founder Agreement | genesis | {Draft/N-A} | styx-legal + H:LC | — |
| Compliance Guardrails | foundation | Active | styx-legal | {today} |
| Regulatory Risk Register | foundation | Active | styx-legal | {today} |
| Terms of Service | hardening | Not yet required | styx-legal + H:LC | — |
| Privacy Policy | hardening | Not yet required | styx-legal + H:LC | — |
| DPA | graduation | Not yet required | H:LC | — |

## Active Guardrails

| # | Rule | Source | Enforcement |
|---|------|--------|-------------|
| 1 | {e.g., No PII stored unencrypted} | {GDPR Art. 32 / CCPA} | {Code review / CI check} |
| 2 | {e.g., Payment via PCI-compliant provider} | {PCI-DSS} | {Architecture ADR} |

## Open Questions for H:LC

| # | Question | Context | Priority |
|---|----------|---------|----------|
| 1 | {specific legal question} | {context} | {HIGH/MED/LOW} |
```

---

## L2: Terms of Service

**Phase:** hardening
**Governing SOP:** `SOP--legal-compliance-matrix.md`
**Output:** `docs/legal/terms-of-service.md`

### Generation Instructions

1. Read exposure assessment from L1
2. Read product description from `seed.yaml` + `README.md`
3. Read revenue model from `registry-v2.json`
4. Draft ToS covering: acceptance, service description, user obligations, IP, liability, termination, governing law
5. Flag all sections that MUST be reviewed by H:LC before publication

### Template

```markdown
# Terms of Service — {product_name}

**Effective Date:** {TBD — set upon H:LC review}
**Last Updated:** {today — DRAFT}

> **DRAFT — NOT LEGALLY BINDING. Requires H:LC review before publication.**

## 1. Acceptance of Terms
{Standard acceptance clause — by using the service, you agree.}

## 2. Description of Service
{From seed.yaml description + README — what the product does.}

## 3. User Accounts & Responsibilities
{If applicable — registration, accuracy of information, account security.}

## 4. Acceptable Use
{What users may and may not do. Infer from product domain.}

## 5. Intellectual Property
{Who owns what — the product's IP, user-generated content, AI-generated output.}

## 6. Payment Terms
{If revenue_model != 'none' — pricing, billing cycle, refunds. From registry.}

## 7. Limitation of Liability
{Standard limitation clause. **H:LC REVIEW REQUIRED.**}

## 8. Termination
{How either party can end the relationship.}

## 9. Governing Law
{From Question 1 — jurisdiction for disputes. **H:LC REVIEW REQUIRED.**}

## 10. Changes to Terms
{How updates are communicated.}

## 11. Contact
{Product operator contact information.}
```

---

## L3: Privacy Policy

**Phase:** hardening
**Governing SOP:** T1 skill `gdpr-compliance-check`
**Output:** `docs/legal/privacy-policy.md`

### Generation Instructions

1. Read data types from L1 exposure assessment
2. Scan `src/` for data collection points (forms, API endpoints accepting user data)
3. Identify third-party data processors from dependencies (Stripe, analytics, auth providers)
4. Generate GDPR/CCPA-compliant privacy policy

### Template

```markdown
# Privacy Policy — {product_name}

**Effective Date:** {TBD — DRAFT}

> **DRAFT — Requires H:LC review before publication.**

## 1. Information We Collect
{Categorized: information you provide, information collected automatically, information from third parties.}

## 2. How We Use Your Information
{Mapped to legal bases — consent, contract performance, legitimate interest.}

## 3. How We Share Your Information
{Third-party processors with purpose. Infer from dependencies.}

## 4. Data Retention
{How long data is kept and why.}

## 5. Your Rights
{GDPR: access, rectification, erasure, portability, objection. CCPA: know, delete, opt-out.}

## 6. Security
{Reference security measures. Link to security audit if available.}

## 7. International Transfers
{If multi-jurisdiction from Question 1.}

## 8. Children's Privacy
{COPPA/GDPR Art. 8 compliance if applicable.}

## 9. Changes to This Policy
{Notification mechanism.}

## 10. Contact
{DPO or privacy contact.}
```

---

## L4: Data Processing Agreement (DPA)

**Phase:** graduation
**Governing SOP:** T1 skill `gdpr-compliance-check`
**Output:** `docs/legal/dpa.md`

### Generation Instructions

1. Read L1 exposure — only generate if HIGH exposure
2. Identify all subprocessors from dependencies
3. Draft standard contractual clauses framework
4. **This document MUST be drafted or substantially reviewed by H:LC.**

### Template

```markdown
# Data Processing Agreement — {product_name}

> **This document MUST be reviewed and approved by qualified legal counsel before use.**

## 1. Definitions
{Controller, processor, data subject, personal data, processing.}

## 2. Scope of Processing
{What data, what purposes, what duration.}

## 3. Obligations of the Processor
{Security measures, confidentiality, subprocessor management, breach notification.}

## 4. Subprocessors

| Subprocessor | Purpose | Location | DPA in Place? |
|-------------|---------|----------|---------------|
| {e.g., Stripe} | Payment processing | US | Yes |
| {e.g., Neon} | Database hosting | US/EU | Yes |

## 5. Data Subject Rights
{How the processor assists the controller.}

## 6. Audit Rights
{Controller's right to audit processor compliance.}

## 7. Data Return & Deletion
{What happens at contract termination.}

## 8. Standard Contractual Clauses
{Reference to applicable SCCs for international transfers.}
```

---

## L5: Regulatory Risk Register

**Phase:** foundation
**Governing SOP:** `SOP--legal-compliance-matrix.md`
**Output:** `docs/legal/regulatory-risk-register.md`

### Generation Instructions

1. Read L1 exposure assessment
2. Identify risks per regulatory framework
3. Score likelihood × impact
4. Assign mitigation strategies and owners

### Template

```markdown
# Regulatory Risk Register — {product_name}

**Last Updated:** {today}
**Exposure Level:** {from L1}

| # | Risk | Framework | Likelihood | Impact | Mitigation | Status | Owner |
|---|------|-----------|------------|--------|------------|--------|-------|
| 1 | {risk description} | {GDPR/CCPA/PCI/etc.} | {Low/Med/High} | {Low/Med/High} | {action} | {Open/Mitigated/Accepted} | {persona} |
```

---

## L6: Founder/Contractor Agreement

**Phase:** genesis
**Governing SOP:** T1 skill `contract-risk-analyzer`
**Output:** `docs/legal/founder-agreement.md`

### Generation Instructions

1. Read business entity type from Question 3
2. Draft IP assignment and work-for-hire clauses
3. **H:LC review required for any equity, compensation, or IP assignment terms.**

### Template

```markdown
# Founder/Contractor Agreement — {product_name}

> **TEMPLATE — Requires H:LC review and customization before signing.**

## 1. Parties
{Entity from Question 3 + contractor/founder identity.}

## 2. Services & Scope
{What work is being performed.}

## 3. Intellectual Property Assignment
{All IP created in scope of engagement is assigned to the entity.}

## 4. Compensation
{Terms — equity, cash, or hybrid. **H:LC MUST review.**}

## 5. Confidentiality
{Mutual NDA provisions.}

## 6. Term & Termination
{Duration, termination triggers.}

## 7. Governing Law
{From Question 1.}
```

---

## L7: IP Assignment & Open-Source Policy

**Phase:** genesis
**Governing SOP:** `SOP--legal-compliance-matrix.md`
**Output:** `docs/legal/ip-assignment.md`

### Generation Instructions

1. Read LICENSE file if present
2. Read `package.json`/`pyproject.toml` for license field
3. Identify open-source dependencies and their licenses
4. Draft policy covering: IP ownership, OSS contribution rules, license compatibility

### Template

```markdown
# IP Assignment & Open-Source Policy — {product_name}

## 1. IP Ownership
{All original code and content is owned by {entity from Question 3}.}

## 2. License
{Current license: {from LICENSE file}. Rationale for choice.}

## 3. Open-Source Dependencies

| Dependency | License | Compatible? | Notes |
|-----------|---------|-------------|-------|
| {dep1} | {MIT/Apache/GPL} | {Yes/No/Review} | ... |

## 4. Contribution Policy
{Rules for accepting external contributions — CLA required? DCO?}

## 5. AI-Generated Code
{Policy on AI-generated code — disclosure, ownership, review requirements.}
```

---

*Generates 7 artifacts: L1 (guardrails matrix), L2 (ToS), L3 (privacy policy), L4 (DPA), L5 (risk register), L6 (founder agreement), L7 (IP/OSS policy)*
