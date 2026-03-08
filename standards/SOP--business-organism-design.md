---
sop: true
name: business-organism-design
scope: system
phase: genesis
triggers:
  - context:new-product
  - context:revenue-planning
  - context:organ-activation
complements:
  - product-deployment-and-revenue-activation
  - planning-and-roadmapping
  - market-gap-analysis
overrides: null
---
# SOP: Business Organism Design

**Version:** 1.0.0 | **Date:** March 8, 2026 | **Status:** Active
**Scope:** Designing business entities as living organisms with departmental anatomy, phased activation, and scenario-modeled viability.

---

## 1. Ontological Purpose

A business is not a static structure — it is an organism that germinates, grows, adapts, and either thrives or dies. The ORGANVM system models this literally: each commercial product (ORGAN-III) is an organism with departments (organs), metabolic processes (revenue flows), and growth phases (activation stages). This SOP codifies the process of designing a business organism from conception through phased activation.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 2: Research & Analysis)
**Cross-reference:** `SOP--product-deployment-and-revenue-activation.md` (activation follows design), `SOP--market-gap-analysis.md` (market research feeds organism design)

---

## 2. Trigger

Execute this SOP when:
- Designing a new commercial product or SaaS tool
- An existing project is transitioning from theory (ORGAN-I) to commerce (ORGAN-III)
- Revenue modeling is needed for a grant proposal or investor pitch
- A product needs departmental restructuring after pivot or scope change

**Exception:** Open-source tools and infrastructure repos without commercial intent do not require this SOP.

---

## 3. Phase I: Organism Anatomy

**Goal:** Define the organism's departmental structure.

### Process

1. **Identify core departments:**
   - **Product** — what the organism makes (features, capabilities, APIs)
   - **Growth** — how the organism acquires users (marketing, distribution, partnerships)
   - **Revenue** — how the organism sustains itself (pricing, tiers, payment processing)
   - **Operations** — how the organism maintains itself (CI/CD, monitoring, support)
   - **Intelligence** — how the organism learns (analytics, user feedback, market signals)

2. **Map each department to repos/modules:**
   - Which existing repos serve each department?
   - What new repos or modules are needed?
   - What is the data flow between departments?

3. **Define the organism's identity:**
   - Name (per `SOP--ontological-renaming.md`)
   - One-line mission
   - Target user persona
   - Primary value proposition

### Output
An organism anatomy diagram: departments, repos, data flows.

---

## 4. Phase II: Three-Scenario Modeling

**Goal:** Model viability under optimistic, expected, and pessimistic conditions.

### Process

1. **Define the three scenarios:**
   - **Optimistic** — viral adoption, strong market fit, minimal competition response
   - **Expected** — steady organic growth, moderate market fit, normal competition
   - **Pessimistic** — slow adoption, weak market fit, aggressive competition or regulation

2. **For each scenario, model:**
   - User acquisition curve (month 1, 3, 6, 12)
   - Revenue projection (MRR/ARR)
   - Cost structure (infrastructure, AI tokens, labor if any)
   - Break-even timeline
   - Key risks and mitigations

3. **Identify survival conditions:**
   - What is the minimum viable revenue to sustain the organism?
   - What is the maximum acceptable burn rate?
   - At what point does the pessimistic scenario trigger a pivot or shutdown?

### Output
A three-scenario table with projections and decision points.

---

## 5. Phase III: Phased Activation

**Goal:** Define the activation sequence — which departments come online in what order.

### Process

1. **Phase 0: Genesis** — Product department only. Build the core value.
2. **Phase 1: Foundation** — Product + Operations. Deploy, monitor, stabilize.
3. **Phase 2: Growth** — Product + Operations + Growth. Acquire first users.
4. **Phase 3: Revenue** — All departments. Enable paid tiers, process payments.
5. **Phase 4: Intelligence** — All departments + analytics. Learn from usage, iterate.

For each phase:
- Define entry criteria (what must be true to start this phase)
- Define exit criteria (what must be true to advance)
- Identify the repos/modules that activate in this phase
- Estimate duration and effort

### Output
An activation timeline with phase gates.

---

## 6. Phase IV: Documentation & Registration

**Goal:** Register the organism in the ORGANVM system.

### Process

1. **Create/update `seed.yaml`** for all repos in the organism
2. **Update `registry-v2.json`** with product metadata
3. **Write the organism's README** per `SOP--readme-and-documentation.md`
4. **Create a pitch deck** via `organvm pitch generate` or `SOP--pitch-deck-rollout.md`
5. **File the organism design** in `.claude/plans/` as a dated plan

### Output
A fully registered organism with documentation, pitch, and activation plan.

---

## 7. Starter Research Questions

- What existing market does this organism enter, and what is the gap?
- Who is the minimum viable user? What is their acute pain?
- What is the simplest pricing model that sustains the organism?
- Which department is the bottleneck — where does the organism die if it fails?
- Does this organism complement or compete with other ORGAN-III products?

---

## 8. Output Artifacts

- Organism anatomy diagram
- Three-scenario model (optimistic/expected/pessimistic)
- Phased activation timeline
- Updated `seed.yaml` and `registry-v2.json`
- Pitch deck
- Organism design plan file

---

## 9. Verification

- [ ] All five departments are identified with repo/module mappings
- [ ] Three-scenario model includes revenue projections and break-even
- [ ] Phased activation has entry/exit criteria for each phase
- [ ] Organism is registered in `registry-v2.json`
- [ ] Pitch deck generated and reviewed

---

## 10. Prompt Examples

Representative prompts from clipboard history that trigger this pattern:

### Example 1

> Think of it this way: same actor, many masks, and each mask plays differently
> depending on which stage and which moment of the life-run it appears on.

### Example 2

> I will give you a reusable schema you can drop into any future Claude Code agent
> to seed the context correctly for phased business activation.
