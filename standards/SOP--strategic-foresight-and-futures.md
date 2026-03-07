# SOP: Strategic Foresight & Futures (The Telescope)

## 1. Ontological Purpose
This SOP defines the process for transitioning from historical synthesis to concrete future thinking without drifting into speculative fiction. It operationalizes Strategic Foresight and Prospective Theory — the academic discipline of studying the future as a measurable, manageable extension of the present.

We do not predict one future. We build multiple plausible futures, stress-test our Covenants against them, and backcast a roadmap from the desired Omega to the present.

**Applicable to:** All ORGANVM projects requiring forward planning, scenario modeling, or roadmap generation. Governed by `METADOC--research-standards.md` (Pillar III: Teleology).

**Upstream dependencies:** `SOP--typological-hermeneutic-analysis.md` (provides Covenants and pattern language), `SOP--source-evaluation-and-bibliography.md` (provides evaluated evidence base).

**Downstream consumer:** `SOP--research-to-implementation-pipeline.md` (Stage III-IV consumes scenarios and backcasted roadmaps).

---

## 2. Phase I: Environmental Scanning — STEEP Analysis

**Goal:** Map the external forces that will act upon the system. Do not guess — track observable signals.

### Process
1. **Scan across five STEEP dimensions:**
   - **Social:** Demographic shifts, cultural attitudes, behavioral trends, workforce patterns.
   - **Technological:** Emerging technologies, infrastructure changes, platform shifts, obsolescence vectors.
   - **Economic:** Market dynamics, capital flows, pricing models, labor economics.
   - **Environmental:** Resource constraints, climate impacts, regulatory responses, sustainability pressures.
   - **Political:** Regulatory trends, governance models, geopolitical shifts, policy directions.
2. **Classify each signal:**
   - **Megatrend:** Large-scale, long-duration movement already in motion (e.g., AI adoption, remote work normalization).
   - **Weak Signal:** Early indicator of potential change, not yet mainstream (e.g., post-quantum cryptography adoption, DAO governance experiments).
   - **Wild Card:** Low-probability, high-impact event (e.g., platform collapse, regulatory ban, paradigm-shifting paper).
3. **Map signals to time horizons:**
   - **Near-term (0-2 years):** Megatrends and strong signals that affect current operations.
   - **Medium-term (2-5 years):** Weak signals that may become megatrends.
   - **Long-term (5-15 years):** Wild cards and speculative but plausible developments.
4. **Build the STEEP matrix:**

   | Dimension | Signal | Classification | Time Horizon | Impact on Covenants |
   |-----------|--------|:---:|:---:|---------------------|
   | | | | | |

### Starter Research Questions
- What megatrends are already reshaping the competitive landscape in our domain?
- What weak signals have appeared in adjacent fields that could cross over?
- What wild card events, however unlikely, would invalidate our core assumptions?
- Which STEEP dimensions are most volatile for our specific system?
- Are there signals that reinforce each other across dimensions (e.g., a technological shift + regulatory response)?

---

## 3. Phase II: Scenario Planning

**Goal:** Build 3-4 plausible futures. Stress-test Covenants and products against each scenario to identify necessary Pivots (strategic shifts) and Dodges (risk mitigations).

### Process
1. **Identify the two most critical uncertainties** from the STEEP analysis — factors that are both high-impact and genuinely uncertain.
2. **Build a 2x2 scenario matrix:** Each axis is one critical uncertainty with its two extreme outcomes. The four quadrants yield four distinct, internally consistent futures.
3. **Name and narrate each scenario:**
   - Give each scenario an evocative name that captures its character.
   - Write a 500-word narrative: What does the world look like in this scenario? What happened to get here? What are the dominant behaviors and constraints?
4. **Stress-test Covenants:** For each scenario, evaluate:
   - Which Covenants survive intact?
   - Which Covenants need modification?
   - Which Covenants break entirely?
5. **Identify Pivots and Dodges:**
   - **Pivots:** Strategic shifts required if a specific scenario materializes. Pre-planned responses.
   - **Dodges:** Risk mitigations deployable regardless of scenario — actions that improve outcomes across all four futures.
6. **Stress-test products:** For each product or system, determine its viability in each scenario. Products that fail in >1 scenario need architectural redesign.

### Starter Research Questions
- What two uncertainties, if resolved differently, would most change the operating environment?
- Are the four scenarios genuinely distinct, or do they collapse into fewer futures?
- Which Covenants are robust across all scenarios (and are therefore high-confidence)?
- What Pivots can be pre-built as options (low cost to maintain, high value if needed)?
- Is there a scenario where the entire system becomes irrelevant? What would cause that?

---

## 4. Phase III: Causal Layered Analysis (CLA)

**Goal:** Analyze the future at four depths to ensure interventions address root causes, not symptoms. Changing the Myth changes the Future Form.

### Process
1. **Layer 1 — Litany (Surface):** What are the observable, surface-level trends? (The news, the metrics, the commonly cited data.)
2. **Layer 2 — Social Causes (Systemic):** What systemic structures produce the Litany? (Economic models, organizational structures, policy frameworks, incentive systems.)
3. **Layer 3 — Worldview (Cultural):** What deep-seated beliefs and cultural narratives support the systemic structures? (Assumptions about human nature, progress, value, authority.)
4. **Layer 4 — Myth/Metaphor (Unconscious):** What unconscious stories, metaphors, and archetypes underlie the worldview? (The "Alchemy" — the story a culture tells itself about what is possible.)
5. **Design interventions at each layer:**
   - Litany-level: Tactical responses (quick but shallow).
   - Social-level: Structural reforms (medium effort, medium depth).
   - Worldview-level: Narrative shifts (slow but deep).
   - Myth-level: Paradigm creation (the hardest, most transformative intervention).
6. **Map Covenants to CLA layers:** Each Covenant should address at least the Social Causes layer. Covenants that only address Litany are insufficient.

### Starter Research Questions
- What is the dominant Litany (surface narrative) about this domain?
- What systemic structures produce that Litany? Who benefits from them?
- What worldview makes those structures seem natural or inevitable?
- What myth or metaphor underlies the worldview? (e.g., "move fast and break things" = the myth of beneficial disruption)
- If we changed the Myth, what would the new Litany look like in 10 years?

---

## 5. Phase IV: Backcasting

**Goal:** Start with the Omega (desired future state) and work backward to the present, generating a high-fidelity roadmap with specific triggers for action.

### Process
1. **Define the Omega** — the desired future state in concrete, measurable terms. Not aspirational language; specific conditions that must be true.
2. **Work backward in milestones:**
   - What must be true 5 years before the Omega? (Milestone T-5)
   - What must be true 3 years before? (T-3)
   - What must be true 1 year before? (T-1)
   - What must be true today? (T-0 = present state)
3. **Identify the critical path:** Which milestones are sequential dependencies? Which can be parallelized?
4. **Map milestones to Covenants:** Each milestone should advance at least one Covenant. Milestones that advance no Covenant are scope creep.
5. **Generate the roadmap:** A backcast roadmap from Omega to T-0, with:
   - Milestone name, target date, success criteria.
   - Required infrastructure and Covenants at each stage.
   - Trigger conditions for Pivots (from Phase II).
6. **Validate against scenarios:** Does the roadmap survive all four scenario futures, or does it assume a single scenario? Build conditional branches for scenario-dependent milestones.

### Starter Research Questions
- Can the Omega be stated in falsifiable, measurable terms?
- What is the single hardest milestone on the critical path? (This is the bottleneck.)
- Which milestones are scenario-dependent? What are the conditional branches?
- If we started the backcast from a different Omega, would the early milestones change?
- What existing infrastructure (code, systems, relationships) maps to which milestones?

---

## 6. Phase V: Transition Design

**Goal:** Apply the Multi-Level Perspective (MLP) to position the system within its sociotechnical landscape and identify tipping point indicators for regime change.

### Process
1. **Map the three levels:**
   - **Niche (Innovation):** Where is the new system positioned? What protected space allows it to develop without being crushed by the regime?
   - **Regime (Status Quo):** What is the current dominant system? What are its strengths and lock-in mechanisms?
   - **Landscape (Macro-trends):** What large-scale forces are creating pressure on the regime? (From STEEP analysis.)
2. **Identify tipping point indicators:** What observable events would signal that the regime is destabilizing and the niche has an opening?
3. **Design intentional interventions:**
   - **Niche-level:** Shield the innovation. Build community. Demonstrate viability.
   - **Regime-level:** Exploit cracks. Offer switching incentives. Reduce lock-in.
   - **Landscape-level:** Align with macro-trends. Position for regime change.
4. **Map interventions to the backcast roadmap:** Each intervention should correspond to a milestone and a Covenant.

### Starter Research Questions
- What niche protections does the system currently have? (Community, funding, regulatory gaps?)
- What lock-in mechanisms sustain the current regime? (Network effects, switching costs, regulatory capture?)
- Which landscape pressures are creating regime instability right now?
- What tipping point indicators should we monitor? How frequently?
- If the regime destabilizes faster than expected, is the niche ready to scale?

---

## 7. Output Artifacts

1. **STEEP Matrix** — classified signals across five dimensions with time horizons and Covenant impact.
2. **Scenario Set** — four named, narrated scenarios with Covenant stress-test results, Pivots, and Dodges.
3. **CLA Depth Map** — four-layer analysis with interventions designed at each depth.
4. **Backcast Roadmap** — Omega-to-present milestone sequence with critical path, conditional branches, and Covenant alignment.
5. **MLP Position Map** — niche/regime/landscape analysis with tipping point indicators and intervention design.

---

## Appendix: Cross-References

- **Governing document:** `METADOC--research-standards.md` (v3.0.0, Pillar III: Teleology)
- **Upstream — Typology:** `SOP--typological-hermeneutic-analysis.md` (provides Covenants and pattern language)
- **Upstream — Sources:** `SOP--source-evaluation-and-bibliography.md` (provides evaluated evidence base)
- **Downstream — Pipeline:** `SOP--research-to-implementation-pipeline.md` (Stage III-IV consumes scenarios and backcasted roadmaps)
- **Adjacent — Market-Gap:** `SOP--market-gap-analysis.md` (Phase I STEEP analysis shared)
- **Adjacent — Autopoietic:** `SOP--autopoietic-systems-diagnostics.md` (feedback loop from diagnostics → revised scenarios)
- **Bibliography:** `APPENDIX--research-standards-bibliography.md` (Domain 5)

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
