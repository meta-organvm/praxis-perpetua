# Study Suite — AI Handoff Prompts

Queued studies for the three Study Suite agents. Each prompt is a self-contained handoff: an AI agent should be able to execute it with no additional context beyond the files referenced.

**Founding spec:** [The Ontological Topology of ORGANVM](../research/2026-03-08-ontological-topology-of-organvm.md), Section IV.

**Output rules:**
- All output goes to the appropriate subdirectory (`findings/`, `hypotheses/`, `audits/`)
- All files are dated: `YYYY-MM-DD--{slug}.md`
- Append-only — never overwrite an existing study output
- Observers, not actors — studies propose changes but never modify production files

---

## Reviewer Studies (findings/)

### R1: Consilience Index for Derived Principles

**Agent:** Reviewer
**Priority:** P0 — foundational for all subsequent studies
**Estimated tokens:** 100K

**Prompt:**

> Read all 37 research documents in `praxis-perpetua/research/` and the 22 derived principles in `praxis-perpetua/lessons/derived-principles.md`.
>
> For each derived principle (S1-S5, C1-C4, A1-A4, Y1-Y7, E1-E2), produce a **consilience score** (0-5):
> - **0**: Principle appears only in its source document
> - **1**: One additional document touches the same idea without naming it
> - **2**: 2-3 documents independently arrive at the same conclusion
> - **3**: 4-6 documents converge, or the principle is operationalized in an SOP
> - **4**: 7+ documents converge AND the principle is embedded in running infrastructure
> - **5**: The principle is so deeply embedded that violating it would break the system
>
> For each score, cite the specific documents and passages that provide evidence.
>
> Output format: `findings/YYYY-MM-DD--consilience-index-v1.md` with a summary table (Principle | Score | Key Evidence | Gap Notes) followed by detailed evidence sections.
>
> Flag any principles that contradict each other. Flag any research documents that articulate ideas not yet captured as principles.

---

### R2: Citation & Cross-Reference Graph

**Agent:** Reviewer
**Priority:** P1
**Estimated tokens:** 75K

**Prompt:**

> Read all 37 research documents in `praxis-perpetua/research/`. Build a citation graph:
>
> 1. **Internal references:** Which documents explicitly reference other documents in the corpus? (Look for markdown links, title mentions, concept citations.)
> 2. **Conceptual clusters:** Group documents by shared themes. Identify at least 5 clusters. For each cluster: name, member documents, core thesis, and the strongest/weakest document.
> 3. **Orphan detection:** Which documents have zero inbound references (nothing cites them)? These are potential dead ends or undiscovered gems.
> 4. **Bridge documents:** Which documents connect multiple clusters? These are the most structurally important in the corpus.
> 5. **Temporal evolution:** How do the clusters' ideas evolve from May 2025 → March 2026? Where did ideas shift, deepen, or get abandoned?
>
> Also read the 4 session logs in `praxis-perpetua/sessions/` and note which research documents they produced or referenced.
>
> Output: `findings/YYYY-MM-DD--citation-graph-v1.md` with a mermaid diagram, cluster analysis, and orphan/bridge lists.

---

### R3: SOP Coverage Audit — Theory vs. Practice

**Agent:** Reviewer
**Priority:** P1
**Estimated tokens:** 100K

**Prompt:**

> Read all 29 SOPs in `praxis-perpetua/standards/` (including the METADOC ecosystem inventory). Read the 37 research documents in `praxis-perpetua/research/`.
>
> Answer these questions:
>
> 1. **Which research insights have been operationalized into SOPs?** For each SOP, identify the research documents whose ideas it codifies.
> 2. **Which research insights have NOT been operationalized?** List research documents or specific sections that articulate actionable methodology but have no corresponding SOP.
> 3. **Which SOPs have no research backing?** Are there SOPs that were created from operational necessity without any theoretical grounding in the research corpus?
> 4. **Quality assessment:** For each SOP, rate on a 3-point scale:
>    - **Grounded**: Has explicit research backing and cites it
>    - **Implied**: Implicitly draws on research themes but doesn't cite them
>    - **Orphaned**: No traceable connection to the research corpus
>
> Output: `findings/YYYY-MM-DD--sop-coverage-audit-v1.md` with a mapping table (SOP → Research Source → Grounding Level) and a gap analysis section proposing SOPs that should be written based on unoperationalized research.

---

### R4: Terminology Drift Analysis

**Agent:** Reviewer
**Priority:** P2
**Estimated tokens:** 75K

**Prompt:**

> Read all 37 research documents in `praxis-perpetua/research/` in chronological order (May 2025 → March 2026). Track how the following core concepts evolve in terminology:
>
> - The relationship between human and AI (conductor/director/orchestrator/manager/pilot?)
> - The organizational unit (organ/department/domain/module/workspace?)
> - The lifecycle model (promotion/maturity/graduation/growth?)
> - The creative process (poiesis/generation/production/composition?)
> - The governance model (constitution/rules/guardrails/constraints?)
> - The revenue model (monetization/commercialization/activation/deployment?)
>
> For each concept: (a) list every variant term used, with document + passage reference, (b) identify the "winning" term (most recent, most consistent), (c) flag documents still using deprecated terms, (d) assess whether the terminological drift reflects genuine conceptual evolution or just inconsistency.
>
> Output: `findings/YYYY-MM-DD--terminology-drift-v1.md` with a term evolution timeline and a recommended glossary for consistency going forward.

---

## Experimenter Studies (hypotheses/)

### X1: Governance-as-Soil Hypothesis Test

**Agent:** Experimenter
**Priority:** P0 — tests the most foundational systemic principle (Y2)
**Estimated tokens:** 150K

**Prompt:**

> Read derived principle Y2 ("Governance is soil, not bureaucracy") in `praxis-perpetua/lessons/derived-principles.md`.
>
> Y2 predicts: repos with governance artifacts premature for their maturity stage should show SLOWER progress than peers at the same promotion level without premature governance.
>
> Design and execute a test:
>
> 1. Read `meta-organvm/organvm-corpvs-testamentvm/registry-v2.json` to get all repos and their promotion statuses.
> 2. For each CANDIDATE-status repo, check which governance artifacts exist: SECURITY.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md, issue templates, PR templates, CI workflows. (Use the filesystem to check each repo's directory if accessible, or infer from registry data.)
> 3. Define "premature governance" = has governance artifacts typically expected at PUBLIC_PROCESS or GRADUATED level while still at CANDIDATE.
> 4. Define "progress" = implementation_status, presence of tests, CI passing, code_files count (from registry or metrics).
> 5. Compare: do premature-governance CANDIDATEs have lower progress indicators than minimal-governance CANDIDATEs?
> 6. Control for: tier (flagship vs standard vs infrastructure), organ (some organs are more mature).
>
> Output: `hypotheses/YYYY-MM-DD--y2-governance-soil-test-v1.md` with: hypothesis statement, prediction, methodology, data, results, conclusion (confirmed/refuted/inconclusive), and limitations.

---

### X2: Context Degradation Hypothesis Test

**Agent:** Experimenter
**Priority:** P1
**Estimated tokens:** 100K

**Prompt:**

> Read derived principle A3 ("Later deliverables in long sessions are most likely to have gaps") in `praxis-perpetua/lessons/derived-principles.md`.
>
> A3 predicts: in multi-file agent sessions, the quality of output degrades as a function of position in the session (later files are lower quality than earlier files).
>
> Design and execute a test:
>
> 1. Read the Gemini session log `praxis-perpetua/sessions/2026-03-06--gemini-styx-research.md` which documents a session producing ~21 files.
> 2. Read the 10 research documents it produced (identifiable by filename patterns matching the session log's file list).
> 3. For each document, score on 3 axes (0-5 each):
>    - **Structural compliance**: Does it follow the declared METADOC format? (Headers, sections, cross-references)
>    - **Framework completeness**: Does it apply all frameworks listed in the research standards?
>    - **Citation quality**: Are sources real, relevant, and properly cited?
> 4. Plot score vs. session position (chronological order of creation).
> 5. Test: is there a statistically meaningful downward trend?
>
> Output: `hypotheses/YYYY-MM-DD--a3-context-degradation-test-v1.md` with hypothesis, methodology, per-document scores, trend analysis, and conclusion.

---

### X3: Revenue Imperative Compliance Test

**Agent:** Experimenter
**Priority:** P1
**Estimated tokens:** 100K

**Prompt:**

> Read derived principle E1 ("The Revenue Imperative") in `praxis-perpetua/lessons/derived-principles.md`.
>
> E1 declares 6 valid revenue pathways: direct-product, consulting-service, content-ip, grant-award, employment, infrastructure.
>
> Test: what percentage of active repos have a declared revenue pathway?
>
> 1. Read `meta-organvm/organvm-corpvs-testamentvm/registry-v2.json`. Extract all repos with promotion_status != ARCHIVED.
> 2. For each repo, check: does `revenue_model` or `revenue_status` exist in the registry? Does the repo's `seed.yaml` declare a revenue pathway?
> 3. Categorize each repo: (a) has declared revenue pathway, (b) has `infrastructure` pathway with stated payoff horizon, (c) has `infrastructure` with no horizon (violates E1), (d) has no revenue declaration at all.
> 4. Calculate system-wide compliance rate.
> 5. Identify the 10 most egregious violators (highest tier / most effort invested but no revenue path).
>
> Output: `hypotheses/YYYY-MM-DD--e1-revenue-imperative-test-v1.md` with compliance data, violator list, and recommendation for how to improve compliance.

---

### X4: Ontological Stratum Decision Audit

**Agent:** Experimenter
**Priority:** P2
**Estimated tokens:** 75K

**Prompt:**

> Read derived principle Y6 ("The system is ontologically stratified") in `praxis-perpetua/lessons/derived-principles.md` and Section I of `praxis-perpetua/research/2026-03-08-ontological-topology-of-organvm.md`.
>
> Y6 defines 4 strata: implementation-detail, architectural-pattern, governance-rule, philosophical-commitment.
>
> Test: are recent decisions being made at the correct stratum?
>
> 1. Read the 4 session logs in `praxis-perpetua/sessions/`. Extract every decision recorded (tool choice, naming convention, file location, governance rule, principle declaration).
> 2. Classify each decision by stratum.
> 3. Assess: was the decision mechanism appropriate for its stratum?
>    - Implementation details decided quickly with minimal deliberation → CORRECT
>    - Architectural patterns decided after analysis of alternatives → CORRECT
>    - Governance rules decided after testing/evidence → CORRECT
>    - Philosophical commitments decided after deep reflection and documented permanently → CORRECT
>    - Any mismatch (e.g., philosophical commitment made casually, implementation detail agonized over) → FLAG
> 4. Produce a "stratum hygiene score" for each session.
>
> Output: `hypotheses/YYYY-MM-DD--y6-stratum-decision-audit-v1.md` with decision inventory, stratum classification, and hygiene scores.

---

## Auditor Studies (audits/)

### G1: Governance Rule Drift Audit

**Agent:** Auditor
**Priority:** P0 — foundational system health check
**Estimated tokens:** 150K

**Prompt:**

> Read `meta-organvm/organvm-corpvs-testamentvm/governance-rules.json` and `meta-organvm/organvm-corpvs-testamentvm/registry-v2.json`.
>
> Perform a full governance compliance audit:
>
> 1. **Dependency validation:** For every `dependencies` edge declared in registry repos, verify it doesn't violate the unidirectional flow (I→II→III). Flag any back-edges.
> 2. **Promotion consistency:** For every repo at PUBLIC_PROCESS or GRADUATED, verify it has the governance artifacts required by its level (as defined in `SOP--promotion-and-state-transitions.md`). List repos that are promoted beyond their artifact maturity.
> 3. **Seed ↔ registry consistency:** For repos accessible on the filesystem, compare `seed.yaml` declarations against registry entries. Flag mismatches in: organ, tier, status, dependencies.
> 4. **Stale validation dates:** Flag repos whose `last_validated` date is more than 30 days old.
> 5. **Orphan detection:** Flag repos in the registry that don't exist on the filesystem and repos on the filesystem that aren't in the registry.
>
> Output: `audits/YYYY-MM-DD--governance-drift-audit-v1.md` with severity-classified findings (CRITICAL / WARNING / INFO), an executive summary, and proposed remediation actions.

---

### G2: SOP Self-Consistency Audit

**Agent:** Auditor
**Priority:** P1
**Estimated tokens:** 100K

**Prompt:**

> Read all 29 SOPs in `praxis-perpetua/standards/`.
>
> Audit for internal consistency:
>
> 1. **Cross-reference integrity:** Every SOP that references another SOP — verify the target exists and the reference is accurate (correct title, correct section).
> 2. **Terminology consistency:** Do SOPs use the same terms for the same concepts? (e.g., does one say "promotion" where another says "graduation" for the same process?)
> 3. **Contradictory instructions:** Do any SOPs give contradictory guidance? (e.g., SOP-A says "always do X before Y" while SOP-B says "Y can precede X")
> 4. **Completeness gaps:** Do any SOPs reference processes or artifacts that don't exist yet? (e.g., "run `organvm foo`" where `foo` isn't a real command)
> 5. **Scope overlap:** Do any SOPs cover the same territory? Are the boundaries clear or confused?
> 6. **METADOC ecosystem inventory accuracy:** Cross-check `METADOC--sop-ecosystem.md`'s inventory against actual files in `standards/`. Are any SOPs missing from the inventory? Are any inventory entries pointing to non-existent files?
>
> Output: `audits/YYYY-MM-DD--sop-consistency-audit-v1.md` with findings by category, severity ratings, and specific fix recommendations.

---

### G3: Agent Behavioral Risk Update

**Agent:** Auditor
**Priority:** P1
**Estimated tokens:** 75K

**Prompt:**

> Read `praxis-perpetua/lessons/agent-behavioral-risks.md` (current risk catalogue).
> Read all session logs in `praxis-perpetua/sessions/` and the session archives in `sessions/claude/`, `sessions/claude-artifacts/`, and `sessions/gemini/`.
>
> Audit:
>
> 1. **Coverage:** Are there agent sessions whose behavioral patterns are NOT captured in the risk catalogue? (e.g., new failure modes, new agents used)
> 2. **Severity recalibration:** Based on accumulated evidence, should any risk severity be upgraded or downgraded?
> 3. **Mitigation effectiveness:** For each documented risk, has the mitigation actually been applied in subsequent sessions? Was it effective?
> 4. **New patterns:** Identify any recurring behavioral patterns across sessions that aren't yet catalogued. Propose new risk entries with severity and mitigation.
> 5. **Codex gap:** The Codex agent (183 sessions in the system-wide archive) has no risk profile yet. If any Codex session data is accessible, propose a Codex risk profile.
>
> Output: `audits/YYYY-MM-DD--agent-risk-update-v1.md` with proposed additions/modifications to the risk catalogue, evidence citations, and a summary of mitigation effectiveness.

---

### G4: Derived Principles Provenance Audit

**Agent:** Auditor
**Priority:** P2
**Estimated tokens:** 75K

**Prompt:**

> Read `praxis-perpetua/lessons/derived-principles.md` (22 principles).
>
> For each principle, verify:
>
> 1. **Source traceability:** The cited source session/document — does it actually exist? Does the cited passage actually support the principle as stated?
> 2. **Accurate representation:** Does the principle faithfully represent the source material, or has it been subtly distorted during extraction?
> 3. **Operational status:** Is each principle actually being followed in practice? Check SOPs and recent session logs for evidence of adherence or violation.
> 4. **Redundancy:** Are any principles saying the same thing in different words? Should they be merged?
> 5. **Staleness:** Are any principles outdated — contradicted by more recent work or decisions?
>
> Output: `audits/YYYY-MM-DD--principles-provenance-audit-v1.md` with a per-principle assessment table (Principle | Source Verified | Faithful | Active | Redundant With | Stale?) and detailed findings for any flagged issues.

---

## Execution Order

Recommended sequence (dependencies shown):

```
Phase 1 (foundational — no dependencies):
  R1: Consilience Index         ← enables all subsequent studies to reference principle strength
  G1: Governance Rule Drift     ← establishes system health baseline

Phase 2 (builds on Phase 1):
  R2: Citation Graph            ← uses R1's principle-to-document mapping
  R3: SOP Coverage Audit        ← uses R1's consilience scores to weight gaps
  G2: SOP Self-Consistency      ← complements R3 (coverage vs. consistency)
  X1: Governance-as-Soil Test   ← uses G1's compliance data as input

Phase 3 (independent, can run in parallel):
  R4: Terminology Drift         ← standalone linguistic analysis
  X2: Context Degradation Test  ← standalone empirical test
  X3: Revenue Imperative Test   ← standalone registry analysis
  G3: Agent Risk Update         ← standalone session analysis
  G4: Principles Provenance     ← standalone verification

Phase 4 (synthesis — after all above):
  X4: Stratum Decision Audit    ← uses all findings to calibrate stratum assignments
```

---

*Created: 2026-03-08 | 11 studies across 3 agents | Est. total: ~1,075K tokens*
