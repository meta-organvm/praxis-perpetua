---
sop: true
name: project-board-taxonomy
scope: system
phase: genesis
triggers:
  - context:new-product
  - context:project-board-creation
  - context:board-audit
complements:
  - planning-and-roadmapping
  - business-organism-design
  - agent-seeding-and-workforce-planning
overrides: null
---
# SOP: Project Board Taxonomy & Review Pipeline

**Version:** 1.0.0 | **Date:** March 8, 2026 | **Status:** Active
**Scope:** Standardized field taxonomy, classification logic, review pipeline, and sub-issue decomposition for GitHub Projects V2 boards across all ORGANVM products.

---

## 1. Ontological Purpose

A project board is the nerve system of a product organism. Without standardized fields, items become opaque — their ownership, cost, phase position, and review status are invisible. This SOP defines the canonical field set, the inference rules that populate them, and the cross-disciplinary review pipeline that ensures every work unit passes through both a domain expert and a critical shadow before approval.

The core insight: **effort is measured in tokens, not hours**. Calendar time is an illusion for AI-conductor systems. What matters is the objective cost of generation — the token expenditure. Dates exist only to render phase gates on a roadmap view.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 3: Execution & Delivery)
**Cross-reference:** `SOP--planning-and-roadmapping.md` (plans feed boards), `SOP--business-organism-design.md` (departments map to board taxonomy), `SOP--agent-seeding-and-workforce-planning.md` (personas map to board ownership)

---

## 2. Trigger

Execute this SOP when:
- Creating a new GitHub Projects V2 board for any ORGAN-III product
- Auditing an existing board for field coverage gaps
- Onboarding a new product into the ORGANVM orchestration layer
- Adding new departments or personas to an existing organism

**Exception:** Internal infrastructure boards (CI, tooling) may use a reduced field set — but Department, Persona, and Phase Energy are always required.

---

## 3. Canonical Field Set (21 Fields)

Every product board carries exactly 21 fields. No blanks permitted on populatable fields.

### 3.1 Core Fields (built-in or original)

| Field | Type | Source | Notes |
|-------|------|--------|-------|
| Title | text | manual | Issue title |
| Status | single-select | manual | `Todo`, `In Progress`, `Done` |
| Labels | built-in | manual | Free-form tagging |
| Repository | built-in | auto | Hosting repo |
| Category | single-select | manual/inherited | Plan source category |
| Source Plan | single-select | manual/inherited | Which plan generated this item |
| Priority | single-select | manual/inherited | `P0-blocker`, `P1-high`, `P2-medium`, `P3-backlog` |
| Effort | single-select | manual/inherited | `XS`, `S`, `M`, `L`, `XL` (human-readable) |
| Target Date | date | computed | Phase gate date (see §6) |
| Milestone | built-in | computed | Phase milestone (see §6) |
| Assignees | built-in | rule-based | Always `{founder}` — the human steward of all work |

### 3.2 Organism Fields (new, product-specific)

| Field | Type | Source | Notes |
|-------|------|--------|-------|
| Department | single-select | inferred | Business department (see §4) |
| Persona | single-select | inferred | Primary AI/human owner (see §5) |
| Token Budget | number | computed | Objective effort in tokens (see §7) |
| Phase Energy | number (0-100) | computed | Position in Alpha→Omega lifecycle (see §6) |

### 3.3 Review Pipeline Fields

| Field | Type | Source | Notes |
|-------|------|--------|-------|
| Review Persona | single-select | matrix | Cross-disciplinary shadow reviewer (see §8) |
| Review Stage | single-select | workflow | `1-Draft`, `2-Cross-Review`, `3-Revision`, `4-Approved` |

### 3.4 Structural Fields (auto-populate)

| Field | Type | Source | Notes |
|-------|------|--------|-------|
| Issue Types | built-in | inferred | `Task`, `Feature`, `Bug` |
| Parent Issue | built-in | linked | Phase root or epic parent |
| Sub-issues Progress | built-in | auto | Renders from parent/child relationships |
| Linked PRs | built-in | auto | Populates when PRs reference issues |
| Reviewers | built-in | auto | Populates from PR review requests |

---

## 4. Department Taxonomy

Eight departments map to the business organism's functional anatomy. Every item belongs to exactly one.

| Code | Department | Domain |
|------|-----------|--------|
| ENG | Engineering | Code, tests, CI, schemas, APIs |
| LEG | Legal & Compliance | Regulatory, KYC, licensing, counsel |
| PRD | Product & Design | UX, A/B testing, user research |
| OPS | Operations & Infrastructure | Deploy, monitoring, scaling, incident response |
| GRO | Growth & Marketing | SEO, content, acquisition, referral |
| FIN | Finance & Revenue | Billing, pricing, unit economics, reconciliation |
| CXS | Customer Success | FAQ, onboarding, churn detection, support |
| B2B | Enterprise Sales | ICP, outreach, demos, partnerships |

### 4.1 Inference Rules (priority order)

Classification follows a waterfall — first match wins:

1. **LEG:** Label `legal` / `owner:legal-compliance` / title contains `F-LEGAL-*`, `compliance`, `KYC`, `CFTC`, `AML`, `regulatory`, `sanctions`, `money transmit`
2. **B2B:** Label `enterprise` / `b2b` / `owner:business-development` / title contains `F-B2B-*`, `HR dashboard`, `enterprise`, `institutional`, `white-label`
3. **FIN:** Label `finance` / title contains `billing`, `revenue`, `Stripe`, `merchant`, `settlement`, `pricing`, `subscription`, `payment`, `treasury`, `fee`, `unit economics`
4. **GRO:** Label `marketing` / title contains `growth`, `SEO`, `content calendar`, `GTM`, `go-to-market`, `viral`, `referral`, `waitlist`, `launch market`
5. **CXS:** Label `support` / title contains `FAQ`, `onboarding`, `churn`, `customer success`, `support ticket`, `NPS`, `help center`
6. **OPS:** Label `ops` / `devops` / title contains `CI/CD`, `Terraform`, `deploy`, `Docker`, `monitoring`, `incident`, `infrastructure`, `runbook`, `scaling`, `load test`, `uptime`, `CDN`, `DNS`
7. **PRD:** Label `product` / title contains `UX`, `A/B test`, `user research`, `design system`, `wireframe`, `prototype`, `accessibility`
8. **ENG:** Default — anything not caught above

### 4.2 Extending

To add a department:
1. Add the option to the project field
2. Add an inference rule at the appropriate priority position
3. Create a corresponding AI persona (§5)
4. Add a review pair (§8)
5. Update the department tracker epic template

---

## 5. Persona Taxonomy

14 personas: 8 AI agent personas and 6 human-required roles.

### 5.1 AI Agent Personas

| Persona | Department | Capability |
|---------|-----------|------------|
| styx-eng | ENG | Writes code, tests, APIs, schemas |
| styx-legal | LEG | Drafts compliance docs, checklists, policy |
| styx-product | PRD | UX audits, A/B test design, user research |
| styx-ops | OPS | Runbooks, monitoring config, scaling plans |
| styx-growth | GRO | SEO, content strategy, acquisition funnels |
| styx-finance | FIN | Unit economics, pricing models, reconciliation |
| styx-support | CXS | FAQs, onboarding sequences, churn analysis |
| styx-enterprise | B2B | ICP definition, outreach templates, demo environments |

### 5.2 Human-Required Personas

| Persona | Role | Why Human |
|---------|------|-----------|
| H:MN | Mobile Native (Swift/Kotlin) | Physical device APIs, Xcode/Android Studio |
| H:LC | Legal Counsel | Signed opinions, bar-certified review |
| H:BD | Business Development | Vendor relationships, in-person partnerships |
| H:RO | Release Ops | App Store submission, TestFlight, DNS |
| H:CR | Cryptography | ZK proofs, EVM, C2PA — requires mathematical verification |
| H:FO | Founders | Strategic go/no-go gates, hiring, fundraising |

### 5.3 Inference Rules (priority order)

1. Label `owner:mobile-native` or title matches Swift/Kotlin/Xcode/TestFlight/iOS/Android → `H:MN`
2. Label `owner:legal-compliance` or title matches signed opinion/attorney/retainer → `H:LC`
3. Label `owner:business-development` or title matches vendor/partnership → `H:BD`
4. Label `owner:release-ops` or title matches App Store submit/TestFlight setup → `H:RO`
5. Label `owner:cryptography` or title matches ZK proof/EVM/C2PA/Solidity → `H:CR`
6. Title matches `hiring:` / `milestone:` / founder gate → `H:FO`
7. Default → department's AI agent (`styx-{dept-lowercase}`)

### 5.4 Assignee Rule

- Items with `H:*` persona → assign `{founder_github_handle}` (human-required work needs founder attention)
- Items with AI persona → assign `{founder_github_handle}` (founder steers all work in solo-founder mode)
- When team scales → AI persona items get no assignee; human personas get the specific human

---

## 6. Phase Lifecycle & Energy Model

### 6.1 Phase Gates

| Phase | Energy Range | Gate Boundary | Milestone Due | Meaning |
|-------|-------------|---------------|---------------|---------|
| Alpha | 0–20 | 20 | (completed) | Foundation, architecture, scaffolding |
| Beta | 21–40 | 40 | Q1 end | Market-safe money enablement |
| Gamma | 41–60 | 60 | Q2 end | Proof integrity at scale |
| Delta | 61–80 | 80 | Q3 end | Retention + network effects |
| Omega | 81–100 | 100 | Q4 end | Enterprise expansion |

### 6.2 Energy Placement

Within each phase, items receive granular energy based on:

- **Priority**: P0-blockers get energy near the gate ceiling (e.g., Beta P0 = 38-40)
- **Dependencies**: Items that block others get +2-3 energy (closer to gate)
- **Optionality**: Nice-to-have items get -5 energy (further from gate)
- **Base placement**: Phase midpoint is the default (e.g., Beta = 30, Gamma = 50)

### 6.3 Target Date Derivation

Target Date is a derived field, not an independent input:

| Phase | Target Date |
|-------|-------------|
| Beta | End of Q1 (e.g., 2026-04-30) |
| Gamma | End of Q2 (e.g., 2026-06-30) |
| Delta | End of Q3 (e.g., 2026-09-30) |
| Omega | End of Q4 (e.g., 2026-12-31) |

This ensures the Roadmap view renders meaningful phase swim lanes.

### 6.4 Phase Root Parents

Four phase-root issues sit at the top of the hierarchy:
- `🏛 Phase Beta — {product phase description}`
- `🏛 Phase Gamma — {product phase description}`
- `🏛 Phase Delta — {product phase description}`
- `🏛 Phase Omega — {product phase description}`

All top-level items without an existing parent are linked as sub-issues of their phase root. Items that are sub-issues of an epic retain their epic parent. The hierarchy is:

```
🏛 Phase Root
  ├── Epic (XL item with sub-issues)
  │   ├── Sub-issue
  │   └── Sub-issue
  ├── Standalone item (M/S, no children)
  └── Standalone item
```

### 6.5 Phase Inference Rules

1. Label `P0-beta-blocker` or P0 priority → Beta (energy 36-40)
2. Label `P1-beta-enhancer` → Beta (energy 25-34)
3. Specific ticket patterns (TKT-P1-007/008/013/014/015, F-CORE-09) → Gamma (energy 41-55)
4. Specific ticket patterns (TKT-P1-005/006/010/012/016/017/018) → Delta (energy 61-75)
5. Enterprise features or TKT-P1-019 → Omega (energy 85-95)
6. Checklist gates: TestFlight=Beta, Real-money=Gamma, App Store=Delta, Enterprise=Omega
7. Department epics → Omega (energy 95)
8. Brainstorm/audit/archive items → Omega (energy 90-100)
9. P1-high + core/schema/api/auth keywords → Beta (energy 32)
10. P2-medium → Delta (energy 65)
11. Remaining → Omega (energy 85)

---

## 7. Token Budget Model

Token Budget is the objective effort companion to the human-readable Effort field.

| Effort | Token Budget | Rationale |
|--------|-------------|-----------|
| XS | 5,000 | Config change, single-file edit |
| S | 25,000 | Small feature, test addition, sub-issue |
| M | 100,000 | Multi-file feature, module-level |
| L | 500,000 | Cross-workspace: schema + API + UI + tests |
| XL | 2,000,000 | Epic-level, multi-session |

Sub-issues default to `S` (25,000 tokens) regardless of parent effort, since decomposition makes each unit small.

---

## 8. Cross-Disciplinary Review Pipeline

### 8.1 Pipeline Stages

Every item progresses through four stages:

```
1-Draft         Persona executes the work
    ↓
2-Cross-Review  Review Persona provides critical/theoretical check
    ↓
3-Revision      Persona incorporates feedback, addresses concerns
    ↓
4-Approved      Ready for merge, deployment, or handoff
```

### 8.2 Review Pairing Matrix

Each primary Persona has a designated shadow reviewer from a complementary discipline:

| Primary Persona | Review Persona | Review Lens |
|----------------|---------------|-------------|
| styx-eng | styx-ops | Reliability — will this survive production? |
| styx-ops | styx-eng | Correctness — is the automation logic sound? |
| styx-legal | styx-finance | Commercial viability — does compliance kill the business model? |
| styx-finance | styx-legal | Compliance — does the pricing model create regulatory exposure? |
| styx-product | styx-support | User empathy — will real users understand this? |
| styx-support | styx-product | Consistency — does this align with the product vision? |
| styx-growth | styx-enterprise | Market fit — does acquisition align with enterprise needs? |
| styx-enterprise | styx-growth | Acquisition lens — can we market what we're selling? |
| H:MN | styx-eng | Architecture — does the native code fit the system design? |
| H:LC | H:FO | Strategic alignment — does the legal opinion serve the mission? |
| H:BD | styx-enterprise | ICP fit — do partnerships match the ideal customer profile? |
| H:RO | styx-ops | Automation — can we automate this release step? |
| H:CR | styx-legal | Regulatory lens — does the cryptographic approach create legal risk? |
| H:FO | styx-legal | Risk check — does the strategic decision have legal exposure? |

### 8.3 Design Rationale

The pairing matrix creates natural tension:
- **Technical pairs** (eng↔ops): production reality checks theory
- **Money pairs** (legal↔finance): compliance and commerce balance each other
- **User pairs** (product↔support): design intent meets user reality
- **Market pairs** (growth↔enterprise): acquisition strategy meets enterprise needs
- **Human-to-AI bridge**: every human persona gets an AI shadow that checks for automatable or AI-assistable components

No persona reviews itself. Every deliverable passes through a lens that is structurally different from the one that created it.

### 8.4 Extending

When adding a new persona:
1. Add to both Persona and Review Persona field options
2. Choose a cross-disciplinary review partner (different department preferred)
3. Add both directions to the pairing matrix
4. Document the review lens (what specific perspective the reviewer brings)

---

## 9. Sub-Issue Decomposition

### 9.1 Tier System

| Tier | Criteria | Sub-issues | Pattern |
|------|----------|------------|---------|
| Tier 1 | XL effort, epic trackers, department trackers | 3-7 per parent | Checklist items → individual issues |
| Tier 2 | L effort with clear API/Schema/UI/Tests breakdown | 2-4 per parent | Standard decomposition pattern |
| Tier 3 | M effort, multi-step descriptions | 2 per parent | Implementation + Verification |
| Atomic | S/XS effort | 0 | Already atomic, no decomposition |

### 9.2 Standard Decomposition Patterns

**Feature (Tier 2):**
```
Parent: feat: {description}
  ├── Schema + API — data model + endpoints
  ├── UI — user-facing components
  └── Tests — unit + integration coverage
```

**Legal/Compliance (Tier 2):**
```
Parent: legal: {description}
  ├── Draft — AI-generated document
  ├── Legal review — counsel sign-off
  └── Release gate — automated compliance check
```

**Department Epic (Tier 1):**
```
Parent: {Department} Department — Task Tracker
  ├── Beta phase task 1
  ├── Beta phase task 2
  ├── Gamma phase task 1
  ├── ...
  └── Omega phase task N
```

### 9.3 Inheritance Rules

Sub-issues inherit from their parent:
- **Category** — same category as parent
- **Priority** — same priority as parent
- **Effort** — defaults to `S` (sub-issues are small by definition)
- **Source Plan** — same source plan as parent
- **Department** — inferred from sub-issue title/labels (may differ from parent)
- **Persona** — inferred from sub-issue title/labels (may differ from parent)
- **Milestone** — same phase milestone as parent
- **Target Date** — derived from milestone phase

Fields that are NOT inherited (always independent):
- **Phase Energy** — computed per-item
- **Token Budget** — always `S` (25,000) for sub-issues
- **Review Persona** — computed from sub-issue's own Persona
- **Review Stage** — always starts at `1-Draft`

---

## 10. Issue Type Classification

Three types, inferred from title and labels:

| Type | Signal | Frequency |
|------|--------|-----------|
| Bug | Label `bug`, title contains `fix`, `bugfix`, `regression`, `broken`, `crash` | ~2% |
| Feature | Title starts with `feat:`, label `enhancement`/`feature`, title contains `implement`, `add support` | ~35% |
| Task | Everything else — docs, audits, chores, governance, milestones, checklists, hiring | ~63% |

---

## 11. Implementation Protocol

### 11.1 Board Creation Sequence

When standing up a new product board:

1. **Create project** via `gh project create`
2. **Create fields** in order: Department → Persona → Token Budget → Phase Energy → Review Persona → Review Stage
3. **Create milestones**: Phase Beta, Phase Gamma, Phase Delta, Phase Omega (with due dates)
4. **Create phase root issues**: 4 issues with `🏛` prefix, labeled `epic`
5. **Create `epic` label** if not present
6. **Import items** from planning documents

### 11.2 Classification Sequence

For each item on the board:

1. Infer Department (§4.1 rules)
2. Infer Persona (§5.3 rules, depends on Department)
3. Compute Token Budget (§7, depends on Effort)
4. Infer Phase + Energy (§6.5 rules)
5. Derive Target Date (§6.3, depends on Phase)
6. Assign Milestone (depends on Phase)
7. Compute Review Persona (§8.2 matrix, depends on Persona)
8. Set Review Stage = `1-Draft`
9. Set Assignee = `{founder}`
10. Set Issue Type (§10 rules)
11. Link to phase root parent if orphan

### 11.3 Sub-Issue Creation Sequence

After top-level items are classified:

1. Identify Tier 1 parents (XL, epic trackers)
2. Parse checklist items from parent body
3. Create sub-issues with `--milestone` matching parent phase
4. Link via `addSubIssue` GraphQL mutation
5. Classify sub-issues (same rules as parents, with inheritance)
6. Repeat for Tier 2 (L-effort items)

### 11.4 Rate Limiting

GitHub API rate limits require pacing:
- GraphQL mutations: ~5 req/s to avoid secondary rate limits
- `gh issue create`: ~2 req/s (heavier operation)
- `gh issue edit`: ~3 req/s
- Batch operations: sleep 1s every 3-5 calls

---

## 12. Verification Checklist

After board population, verify:

- [ ] All items have Department set (0 blanks)
- [ ] All items have Persona set (0 blanks)
- [ ] All items have Token Budget > 0
- [ ] All items have Phase Energy in range 0-100
- [ ] All items have Review Persona set
- [ ] All items have Review Stage = `1-Draft`
- [ ] All items have a Milestone assigned
- [ ] All items have Target Date set to a phase gate
- [ ] All items have an Assignee
- [ ] All items have an Issue Type
- [ ] All top-level items have a Parent Issue (phase root or epic)
- [ ] Phase distribution is reasonable (not all piled in one phase)
- [ ] Department distribution matches product shape (~60% ENG for technical products)
- [ ] Token Budget total is plausible for the project scope
- [ ] Roadmap view shows items distributed across phase swim lanes

---

## 13. Prompt Examples

### Example 1: Full Board Setup

> stand up the project board for {product}. follow SOP--project-board-taxonomy. 21 fields, full classification, sub-issue decomposition, review pipeline.

### Example 2: Board Audit

> audit the {product} project board for field coverage gaps. every field, every item, no blanks. report what's missing.

### Example 3: Adding a Department

> add a new department {CODE} to the {product} board. update inference rules, create persona, assign review pair.
