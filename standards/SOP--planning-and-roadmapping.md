---
sop: true
name: planning-and-roadmapping
scope: system
phase: genesis
triggers:
  - context:new-project
  - context:quarterly-review
  - context:scope-expansion
complements:
  - repo-onboarding-and-habitat-creation
  - structural-integrity-audit
overrides: null
---
# SOP: Planning and Roadmapping

**Version:** 1.0.0 | **Date:** March 8, 2026 | **Status:** Active
**Scope:** Any initiative requiring phased execution — from single-repo feature sets to cross-organ system milestones.

---

## 1. Ontological Purpose

A plan is a contract between the present self and the future self. Without formalized planning, work becomes reactive — driven by the most urgent prompt rather than the most important trajectory. This SOP codifies the "there-and-back-again" methodology: start at the destination (omega), decompose backward to the present (alpha), then execute forward through milestones.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 2: Research & Analysis)
**Cross-reference:** `SOP--repo-onboarding-and-habitat-creation.md` (plans precede repos), `SOP--structural-integrity-audit.md` (plans are audited for completeness)

---

## 2. Trigger

Execute this SOP when:
- Starting a new project or major feature set
- A repo has accumulated >10 untracked ideas without a roadmap
- Quarterly review reveals drift between work and goals
- Scope expansion requires re-planning (new organ, new product, new market)

**Exception:** Tactical single-session tasks (bug fixes, config changes) do not require formal planning.

---

## 3. Phase I: Omega Definition

**Goal:** Define the destination before plotting the route.

### Process

1. **State the omega condition** — what does "done" look like? Be concrete:
   - What artifacts exist?
   - What capabilities are operational?
   - What metrics are met?
   - Who can use the system and how?

2. **Set the time horizon:**
   - Sprint-scale (1-2 weeks): single feature or repo milestone
   - Quarter-scale (1-3 months): product launch, organ maturity gate
   - Epoch-scale (6-12 months): system-wide transformation

3. **Identify hard constraints:**
   - Dependencies on external systems or people
   - Resource limits (token budget, compute, time)
   - Governance gates (promotion requirements, review cycles)

### Output
A 1-paragraph omega statement with measurable criteria.

---

## 4. Phase II: Macro Decomposition

**Goal:** Break the omega into major phases (3-7 milestones).

### Process

1. **Work backward from omega.** What is the last milestone before omega? What precedes that?
2. **Name each milestone** with a descriptive slug (e.g., `core-engine`, `ci-pipeline`, `public-launch`)
3. **Assign dependencies** between milestones. Draw the critical path.
4. **Estimate effort class** per milestone:
   - `S` — single session, <2 hours
   - `M` — 2-5 sessions, 1-3 days
   - `L` — 5-15 sessions, 1-2 weeks
   - `XL` — 15+ sessions, requires sub-planning

### Output
A milestone table: `ID | Name | Depends On | Effort | Status`

---

## 5. Phase III: Micro Decomposition

**Goal:** Break each milestone into atomic tasks.

### Process

1. **For each milestone**, list every concrete task needed to complete it
2. **Tag each task** with:
   - File references (what files are created or modified)
   - Test requirements (what verification proves it's done)
   - Agent suitability (can this be delegated to a parallel agent?)
3. **Identify blockers** — tasks that require human input, external APIs, or information not yet available
4. **Group tasks** into parallelizable workstreams where dependencies allow

### Output
An atomized task list per milestone, suitable for `organvm plans atomize` ingestion.

---

## 6. Phase IV: Plan Persistence

**Goal:** Write the plan to a durable, discoverable location.

### Process

1. **Write the plan file** to `<project>/.claude/plans/YYYY-MM-DD-{descriptive-slug}.md`
2. **Include in the plan file:**
   - Omega statement
   - Milestone table
   - Task decomposition per milestone
   - Known blockers and risks
   - Cross-references to related plans
3. **Never overwrite** an existing plan. Revisions get `-v2.md`, `-v3.md` suffixes.
4. **Run `organvm plans index`** to update the plan index after writing.

### Output
A dated plan file in the project's plans directory.

---

## 7. Phase V: Execution Tracking

**Goal:** Keep the plan alive as work progresses.

### Process

1. **Mark task status** in the plan file as work completes: `[ ]` → `[x]`
2. **Run `organvm atoms pipeline --write`** periodically to reconcile plans against git history
3. **Re-plan when scope changes.** Create a new versioned plan file rather than modifying the original.
4. **At milestone completion**, run `SOP--session-self-critique.md` Phase III to audit deliverables.

---

## 8. Starter Research Questions

- What is the smallest omega that delivers meaningful value?
- Are there existing plans in `.claude/plans/` that overlap with this scope?
- Which milestones can be parallelized across agents?
- What is the critical path — which milestone, if delayed, delays everything?

---

## 9. Output Artifacts

- `YYYY-MM-DD-{slug}.md` — plan file in project plans directory
- Milestone table (embedded in plan or as standalone tracking)
- Atomized task list (JSONL via `organvm plans atomize`)
- Updated plan index (via `organvm plans index`)

---

## 10. Verification

- [ ] Omega condition is stated with measurable criteria
- [ ] Milestones decompose the full path from alpha to omega
- [ ] Every milestone has at least one concrete task
- [ ] Plan file is persisted with date prefix and descriptive slug
- [ ] Plan file is discoverable by `organvm plans index`
- [ ] No existing plan was overwritten

---

## 11. Prompt Examples

Representative prompts from clipboard history that trigger this pattern:

### Example 1

> devise extensive & exhaustive alpha through omega, <macro<>micro<>macro>, plan ['there+back-again.md'];

### Example 2

> devise extensive & exhaustive <macro<>micro<>macro> plan ['there+back-again.md'] to get us to omega and the milestones along the way

### Example 3

> let's defer that for now (pin in it). for now, devise an exhaustive/extensive plan to complete this whole project
