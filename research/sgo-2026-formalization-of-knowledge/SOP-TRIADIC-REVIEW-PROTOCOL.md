---
sgo_id: SGO-2026-SOP-001
title: "Triadic Review Protocol (TRP)"
type: Standard Operating Procedure
status: CANDIDATE
applies_to: All SGO ventures (papers, implementations, publications, governance changes)
date: 2026-03-21
---

# Triadic Review Protocol (TRP)

> *"A liquid takes the shape of its container."*
>
> Every venture that advances through the ORGANVM system must be evaluated by three perspectives — non-redundant, generative, and venture-shaped.

---

## 1. Core Principle

No work advances with fewer than three points of view. Not one POV agreeing with itself. Not two POVs in binary agreement or disagreement. Three POVs creating a harmonious system of critique, expansion, amendment, and divergence.

**Why three:**
- One POV produces echo
- Two POVs produce debate (thesis/antithesis without synthesis)
- Three POVs produce triangulation — structural integrity through non-redundant coverage

This is consistent with:
- Peirce's triadic sign model (sign, object, interpretant)
- The psychometric requirement for inter-rater agreement (minimum 3 raters for reliable ICC)
- The Governance Trilemma (completeness, consistency, measurability — three axes of evaluation)
- Beer's Viable System Model (System 3, 3*, and 4 as three governance perspectives)

---

## 2. Venture Classification

Every venture declares its **domain signature** before review begins.

### 2.1 Domain Signature

A domain signature is a set of 2-5 fields the venture touches. Examples:

| Venture | Domain Signature |
|---------|-----------------|
| RP-04 (Naming Problem) | `[philosophy of language, information science, software engineering]` |
| SYN-02 (Governance Impossibility) | `[mathematical logic, organizational theory, psychometrics, STS]` |
| RP-05 (Latour/ANT) | `[science & technology studies, AI systems, philosophy]` |
| Governance redesign task | `[systems architecture, measurement, policy design]` |
| arXiv submission | `[academic publishing, disciplinary norms, audience analysis]` |
| Wikipedia contribution | `[encyclopedic standards, domain expertise, source verification]` |

### 2.2 Venture Types

| Type | Advancement Path | TRP Gate |
|------|-----------------|----------|
| **Paper** (SGO) | LOCAL → CANDIDATE → PUBLIC_PROCESS → GRADUATED | TRP at each transition |
| **Implementation** (ORGANVM) | Design → Build → Verify → Deploy | TRP at Design and Verify |
| **Publication** (External) | Draft → Format → Submit → Revise | TRP at Draft and Revise |
| **Governance Change** | Propose → Review → Implement → Audit | TRP at Review |

---

## 3. Triad Constitution

### 3.1 The Amorphous Principle

The three POVs are not fixed roles. They are **constituted per-venture** based on the domain signature. The container shapes the liquid.

### 3.2 POV Dimensions

Each POV is constituted from three orthogonal dimensions:

| Dimension | Options |
|-----------|---------|
| **Role** | Architect, Critic, Practitioner, Historian, Empiricist, Theorist, Operator, Auditor |
| **Discipline** | Formal logic, Philosophy, Linguistics, CS/PL theory, Organizational science, STS, Psychometrics, Art/Design, Systems theory, Rhetoric |
| **Stance** | Sympathetic (steelman), Adversarial (where does this break?), Orthogonal (what adjacent field does this ignore?) |

### 3.3 Selection Algorithm

1. Take the venture's domain signature (2-5 fields)
2. If > 3 fields: select the 3 most **tension-bearing** — the fields most likely to produce non-redundant critique
3. For each selected field, constitute a POV by choosing:
   - A **role** appropriate to that field
   - The **discipline** matching that field
   - A **stance**: one sympathetic, one adversarial, one orthogonal (always this distribution)
4. Verify **non-redundancy**: no two POVs share the same role AND discipline
5. If implemented with AI models: distribute across models (e.g., Claude, Gemini, ChatGPT) to prevent model-specific bias

### 3.4 Triad Template

```yaml
venture: <venture ID>
domain_signature: [field_1, field_2, field_3]
triad:
  pov_1:
    field: <field_1>
    role: <role>
    discipline: <discipline>
    stance: sympathetic
    model: <model_1>  # if AI-implemented
  pov_2:
    field: <field_2>
    role: <role>
    discipline: <discipline>
    stance: adversarial
    model: <model_2>
  pov_3:
    field: <field_3>
    role: <role>
    discipline: <discipline>
    stance: orthogonal
    model: <model_3>
```

---

## 4. Review Execution

### 4.1 Output Modes

Each POV must produce at least one of four output modes:

| Mode | Description | Required Output |
|------|-------------|----------------|
| **Critique** | Where does this break? What assumptions are unexamined? | Specific failure point + evidence |
| **Expansion** | What does this enable that the author didn't see? | Concrete extension + rationale |
| **Amendment** | Agreement with modification | Specific change + justification |
| **Fork** | Disagreement with alternative path | Alternative formulation + argument for why it's preferable |

**No bare approval.** A review that says only "this is good" is invalid. Every POV must produce substantive output in at least one mode.

### 4.2 Review Structure

Each POV produces a structured review:

```markdown
## POV Review: [Role] / [Discipline] / [Stance]

### Summary Assessment
[2-3 sentences: what this work does well and where it needs work]

### Primary Mode: [Critique | Expansion | Amendment | Fork]
[Substantive output in the primary mode — 300-500 words]

### Secondary Observations
[Additional notes in other modes — 200-300 words]

### Verdict
- [ ] Advance as-is
- [ ] Advance with amendments (listed above)
- [ ] Revise and re-review
- [ ] Fork: alternative path recommended

### Inter-POV Questions
[Questions directed at the other two POVs — what do you see that I might be missing?]
```

### 4.3 Synthesis Round

After all three POVs produce reviews:

1. **Agreement map:** Where do all three agree? (These findings are high-confidence)
2. **Disagreement map:** Where do POVs conflict? (These are the most valuable signals)
3. **Expansion inventory:** What new directions did the reviews surface?
4. **Fork analysis:** If any POV recommended a fork, the venture author must address it explicitly — accept the fork, reject with justification, or integrate as a branch

### 4.4 Resolution Protocol

| Pattern | Resolution |
|---------|-----------|
| 3/3 advance | Advance to next stage |
| 2/3 advance, 1 amend | Advance with amendments incorporated |
| 2/3 advance, 1 fork | Advance, but fork is documented as future work |
| 1/3 advance, 2 revise | Revise and re-review (new triad may be constituted) |
| 0/3 advance | Major revision; venture returns to previous stage |
| Any POV raises ethical/integrity concern | Escalate to human review regardless of other verdicts |

---

## 5. The Research-to-Publication-to-Implementation Pipeline

### 5.1 Pipeline Stages

Every research venture follows this pipeline. Each stage has a TRP gate.

```
STAGE 1: GENESIS
├── Browser history / reading / conversation → Research Atlas
├── Atlas → Research Adventures (domain expansion via Wikipedia API)
├── Adventures → Research Program Prospectus (formal RQs, methodology, venues)
└── TRP Gate: Domain signature + triad constituted for the research program

STAGE 2: COMPOSITION
├── Prospectus → Academic paper/thesis/dissertation (first draft)
├── Draft → Self-review (author identifies weaknesses)
└── TRP Gate: Three-POV review of draft

STAGE 3: REFINEMENT
├── TRP feedback incorporated → Revised draft
├── Cross-reference with prior works in the program
├── Citation audit (verify all references, add missing sources)
└── TRP Gate: Re-review of revised draft (may use same or new triad)

STAGE 4: DUAL PUBLICATION
├── INTERNAL: Advance through SGO pipeline (LOCAL → CANDIDATE → PUBLIC_PROCESS)
│   ├── IRA panel defense (the TRP IS the defense)
│   └── Archive in meta-organvm/praxis-perpetua/research/
├── EXTERNAL: Format for target venue
│   ├── arXiv preprint (immediate visibility)
│   ├── Journal/conference submission
│   └── Wikipedia contribution (novel concepts become encyclopedia entries)
└── TRP Gate: Publication-readiness review

STAGE 5: IMPLEMENTATION
├── Extract design principles / recommendations from the paper
├── Identify ORGANVM components affected (from ORGANVM Connection field)
├── Create implementation tasks (code changes, governance updates, tool builds)
├── Build → Test → Deploy
└── TRP Gate: Implementation review (does the code match the theory?)

STAGE 6: FEEDBACK
├── Implementation produces empirical data
├── Data feeds back into the research (case studies, validation, refutation)
├── Updated findings may trigger paper revision or new paper
└── The spiral continues
```

### 5.2 The Dual-Track Principle

Publication and implementation are not sequential — they are **simultaneous**:

- Every paper that publishes also produces implementation tasks
- Every implementation that ships also produces a case study for the next paper
- The Wikipedia user page is updated with each publication
- The SGO corpus grows with each cycle

### 5.3 Batch Operations

For the current corpus of 13 works:

**Batch 1: Integrate into SGO**
- Move all 13 papers from `intake/research-adventures-2026-03/papers/` to `meta-organvm/praxis-perpetua/research/` with proper dated naming
- Update the SGO research corpus index
- Advance all works from LOCAL to CANDIDATE status

**Batch 2: Constitute Triads**
- Generate domain signatures for all 13 works
- Constitute review triads for each
- Execute TRP reviews (can be parallelized — 13 ventures × 3 POVs = 39 reviews)

**Batch 3: Dual-Track Execution**
- Prepare arXiv submissions for the 3 strongest papers (SYN-02, RP-06, SYN-01)
- Extract implementation tasks from all papers
- Begin Wikipedia contribution planning (Governance Trilemma, Naming as Infrastructure)

**Batch 4: Implementation Sprint**
- Apply SYN-02's governance trilemma to ORGANVM redesign
- Implement RP-07's psychometric calibration of promotion pipeline
- Audit naming conventions against RP-04/SYN-03 principles
- Build citation network / knowledge graph from 591 citations

---

## 6. Quality Metrics

### 6.1 Inter-POV Agreement

After each TRP cycle, compute:
- **Agreement rate:** proportion of assessment items where all 3 POVs converge
- **Productive disagreement rate:** proportion of items generating forks or amendments
- **Expansion rate:** proportion of reviews that surface new directions

Healthy targets:
- Agreement: 40-60% (too high = insufficient diversity; too low = incoherent)
- Productive disagreement: 20-40%
- Expansion: 20-30%

### 6.2 Pipeline Velocity

Track per-venture:
- Time from GENESIS to first COMPOSITION draft
- Time from COMPOSITION to TRP-cleared REFINEMENT
- Time from REFINEMENT to DUAL PUBLICATION
- Time from PUBLICATION to IMPLEMENTATION
- Time from IMPLEMENTATION to FEEDBACK (spiral completion)

### 6.3 Spiral Depth

Count how many times a venture has completed the full pipeline spiral. Each pass deepens the work. The capstone dissertation should spiral at least twice before GRADUATED status.

---

## 7. Appendix: Triad Configurations for Current Corpus

| Work | Domain Signature | POV 1 (Sympathetic) | POV 2 (Adversarial) | POV 3 (Orthogonal) |
|------|-----------------|---------------------|---------------------|---------------------|
| RP-04 | `[phil. of language, info science, software eng.]` | Philosopher / Naming theory | Software architect / "Does this actually help name things?" | Linguist / "What about non-Western naming?" |
| RP-02 | `[math logic, computability, governance]` | Logician / Gödel specialist | Systems engineer / "Can you actually build with these constraints?" | Biologist / "How does autopoiesis really work?" |
| RP-07 | `[psychometrics, software eng., measurement theory]` | Psychometrician / IRT specialist | Software practitioner / "These metrics are already good enough" | Sociologist / "Measurement is political" |
| RP-03 | `[org theory, philosophy, network science]` | Systems theorist / Complexity | Political scientist / "Hierarchy exists for reasons" | Ecologist / "Natural systems do this differently" |
| RP-05 | `[STS, AI systems, philosophy]` | STS scholar / ANT specialist | AI safety researcher / "Symmetry is dangerous" | Pragmatist / "What does this change in practice?" |
| RP-01 | `[formal semantics, PL theory, linguistics]` | Logician / Model theory | NLP engineer / "Transformers don't care about compositionality" | Cognitive scientist / "Meaning is embodied" |
| RP-06 | `[formal languages, type theory, linguistics]` | Type theorist / Curry-Howard | Corpus linguist / "Natural language is messier than this" | HCI researcher / "What about the programmer's experience?" |
| SYN-01 | `[category theory, formal semantics, NLP]` | Category theorist | Distributional semanticist / "Vectors work without categories" | Philosopher of science / "Is this genuine unification or redescription?" |
| SYN-02 | `[math logic, org theory, psychometrics, STS]` | Governance designer / Sympathetic | Decision theorist / "Arrow's theorem doesn't generalize this way" | Practitioner / "We govern systems fine without this" |
| SYN-03 | `[naming, org theory, STS]` | Infrastructure scholar / Star & Bowker | Software architect / "Naming conventions are bikeshedding" | Anthropologist / "How do non-Western orgs name?" |
| SYN-04 | `[STS, psychometrics, philosophy]` | Barad scholar / Agential realism | Psychometrician / "You can't just dissolve latent variables" | Software engineer / "Give me a number I can use" |
| SYN-05 | `[philosophy, formal semantics, computability, naming]` | Philosopher of language | Formal semanticist / "This architecture is too loose" | Artist / "Where is aesthetic meaning in this?" |
| CAP | `[all fields]` | Intellectual historian / "Does this hold together?" | Methodologist / "Is the evidence adequate?" | Outsider / "Would a stranger understand this?" |

---

*This SOP is itself subject to the Triadic Review Protocol. Its domain signature is `[governance, methodology, epistemology]`.*
