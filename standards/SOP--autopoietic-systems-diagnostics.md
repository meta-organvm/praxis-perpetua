# SOP: Autopoietic Systems Diagnostics (The Mirror of Eternity)

## 1. Ontological Purpose
This SOP defines the process for diagnosing, improving, and ensuring the self-regenerative capacity of any ORGANVM system. It operationalizes Autopoietic Systems Theory and Second-Order Cybernetics — the study of systems that continuously recreate themselves.

We do not examine products (outputs). We examine the network of processes that produce the components. If the producer and product are no longer the same, the system is decaying.

**Applicable to:** All ORGANVM organs, projects, and the meta-system itself. Governed by `METADOC--research-standards.md` (Section 3: The Meta-Layer).

**Upstream dependencies:** `SOP--source-evaluation-and-bibliography.md` (provides evidence base), `SOP--strategic-foresight-and-futures.md` (provides scenario context).

**Feedback loop:** Diagnostic findings feed back to `SOP--source-evaluation-and-bibliography.md` as new research requirements and to `SOP--strategic-foresight-and-futures.md` as revised scenario inputs.

---

## 2. Phase I: Autopoietic Identity Check

**Goal:** Determine whether the system satisfies the Maturana-Varela criteria for autopoiesis — is it self-producing, operationally closed, and structurally coupled to its environment?

### Process
1. **Define the system boundary:** What is inside? What is outside? Where does the system end and the environment begin?
2. **Enumerate the system's components:** Every module, process, team, workflow, and artifact that constitutes the system.
3. **Map the production network:** For each component, identify:
   - What produces it? (Another internal component, or an external dependency?)
   - What does it produce? (Another internal component, or only an external output?)
4. **Apply the autopoietic criteria:**
   - **Self-production:** Do the system's internal interactions generate the very same network that created them?
   - **Operational closure:** Does the system's organization (the pattern of relationships) remain invariant even as specific components change?
   - **Structural coupling:** Does the system adapt to environmental perturbations without losing its identity?
5. **Component regeneration audit:** For each component, ask: "If this component were destroyed, could the remaining system regenerate it?" Components that cannot be regenerated are single points of failure.

### Starter Research Questions
- Can you draw the system boundary unambiguously? If not, the system may not have a clear identity.
- Which components are produced internally vs. imported from outside? (External dependencies weaken autopoiesis.)
- If the lead developer, primary maintainer, or key relationship were removed, what regenerates?
- Does the system's organization (not its components) remain stable over the last 6 months?
- Are there components that only consume but never produce? (Parasitic elements.)

---

## 3. Phase II: Second-Order Cybernetic Audit

**Goal:** Audit how the system observes and regulates itself. In second-order cybernetics, the observer is part of the system — the system must learn how to learn.

### Process
1. **Identify the observer position:** Who or what monitors the system? (Metrics dashboards, CI pipelines, human reviewers, AI agents.) Is the observer inside or outside the system?
2. **Map all feedback loops:**
   - **Negative feedback (stabilizing):** Error correction, test suites, linting, code review — mechanisms that reduce deviation from targets.
   - **Positive feedback (amplifying):** Growth loops, viral effects, compounding returns — mechanisms that amplify deviation.
3. **Assess loop health:**
   - Are negative loops fast enough? (A feedback loop that takes 6 months to detect a bug is functionally dead.)
   - Are positive loops bounded? (Unbounded positive feedback = explosion or collapse.)
   - Are there dead loops? (Metrics collected but never acted upon.)
4. **Echo chamber detection:** Does the system only receive confirming information? Are there mechanisms for disconfirming evidence to reach decision-makers?
5. **Meta-learning audit:** Does the system learn how to learn? (e.g., retrospectives that change process, not just fix symptoms. SOPs that update themselves based on outcomes.)
6. **Assess Covenant mutability:** Are the system's Covenants static rules, or are they feedback loops that allow the system to rewrite its own rules as the environment shifts?

### Starter Research Questions
- What is the fastest feedback loop in the system? The slowest?
- Are there metrics being collected that no one acts on? (Dead loops.)
- When was the last time a process was changed because of feedback, not because of a crisis?
- Is there a mechanism for external, disconfirming information to reach the system's core decision-making?
- Can the system rewrite its own Covenants, or are they immutable?

---

## 4. Phase III: Regenerative Capacity Assessment

**Goal:** Determine whether the system produces surplus vitality — not just "less bad" (efficiency) but actively restorative.

### Process
1. **Measure surplus health:**
   - Does the system produce more resources (knowledge, code, community, capital) than it consumes?
   - Is the surplus growing, stable, or declining?
   - Is the surplus distributed or concentrated?
2. **Assess evolutionary development:** Growth is not linear expansion (which kills the host) but increased complexity and capability.
   - Is the system growing in complexity (new capabilities, richer relationships)?
   - Or is it growing only in size (more of the same)?
3. **Identify leaks:** Where does the system lose vitality?
   - Technical debt that compounds faster than repayment.
   - Knowledge that exists in a single person's head.
   - Community energy that flows out (contributors leaving) faster than it flows in.
4. **Regenerative accounting:**

   | Resource | Production Rate | Consumption Rate | Net Surplus | Trend |
   |----------|:---:|:---:|:---:|:---:|
   | Code quality | | | | |
   | Knowledge base | | | | |
   | Community energy | | | | |
   | Financial runway | | | | |

5. **"Essence thinking" check:** Does every process produce a surplus of vitality, or are some processes pure cost centers with no regenerative output?

### Starter Research Questions
- If the system stopped receiving external inputs tomorrow, how long would it survive on internal surplus?
- Is the system more capable today than 6 months ago? In what specific ways?
- Where is knowledge concentrated in a single person? (Bus factor assessment.)
- What is the ratio of creation (new work) to maintenance (keeping old work alive)?
- Are contributors gaining or losing energy from their participation?

---

## 5. Phase IV: Antifragility Stress Test

**Goal:** Classify each system component on Taleb's triad: fragile (harmed by volatility), robust (unchanged by volatility), or antifragile (improved by volatility). An autopoietic system must be at least robust; the goal is antifragile.

### Process
1. **Enumerate all components** (from Phase I) and classify each:

   | Component | Fragile | Robust | Antifragile | Evidence |
   |-----------|:---:|:---:|:---:|----------|
   | | | | | |

2. **Apply stress scenarios:** For each component, evaluate behavior under:
   - **Load stress:** 10x normal usage.
   - **Failure stress:** Key dependency becomes unavailable.
   - **Adversarial stress:** A hostile actor attempts to exploit the component.
   - **Change stress:** Requirements shift significantly.
3. **Identify fragile components** — these are priority targets for architectural improvement.
4. **Design antifragile upgrades:** For each fragile component, ask: "What would make this component *improve* from the stress rather than merely survive it?"
   - Example: A test suite that only detects known bugs is robust. A test suite with property-based testing that discovers new bugs from random stress is antifragile.
5. **Build "Pivots and Dodges" into architecture:** Ensure that volatility becomes fuel for the next iteration of the Form, not a threat to it.

### Starter Research Questions
- Which components have never been tested under abnormal conditions?
- What happened the last time something broke? Did the system improve or merely recover?
- Are there components that benefit from having more users, more data, or more stress?
- What is the system's relationship with randomness? Does it avoid it (fragile), tolerate it (robust), or seek it (antifragile)?
- If a competitor copied the entire system tomorrow, what would be antifragile enough to survive?

---

## 6. Phase V: Meta-Layer Diagnostic Table

**Goal:** Produce the summary diagnostic — a four-row assessment of the system's autopoietic health across Identity, Logic, Evolution, and Impact.

### Process
1. **Compile findings** from Phases I-IV into the diagnostic table:

   | Level | Focus | Academic Term | Assessment (G/Y/R) | Evidence | Recommended Action |
   |-------|-------|---------------|:---:|----------|-------------------|
   | **Identity** | How the system defines itself | Autopoietic Organization | | | |
   | **Logic** | How the system regulates itself | Cybernetic Regulation | | | |
   | **Evolution** | How the system changes its form | Morphogenesis | | | |
   | **Impact** | How the system heals its environment | Regenerative Design | | | |

2. **Rating criteria:**
   - **Green (G):** Criterion fully satisfied. Evidence is strong. No action needed.
   - **Yellow (Y):** Criterion partially satisfied. Specific gaps identified. Action planned.
   - **Red (R):** Criterion not satisfied. Systemic intervention required. Escalate.
3. **Write the diagnostic narrative:** A prose summary of the system's autopoietic health, referencing specific evidence from each phase.
4. **Generate action items:** Each Yellow or Red assessment produces at least one concrete, time-bound action item with an owner.
5. **Compare against prior diagnostics:** If previous diagnostic tables exist, track trajectory. Is the system improving, stable, or declining?

### Starter Research Questions
- Can all four levels be assessed, or are there data gaps that prevent rating?
- Are there levels where the assessment has changed since the last diagnostic?
- Is there a pattern across levels? (e.g., strong Identity but weak Evolution = a system that knows what it is but cannot change.)
- What is the minimum intervention that would move a Yellow to Green?
- Are there Red assessments that have been Red for multiple diagnostic cycles? (Chronic dysfunction.)

---

## 7. Execution Cadence

| Trigger | Scope |
|---------|-------|
| **Quarterly** | Full diagnostic (Phases I-V) on the meta-system or highest-risk organ |
| **Post-promotion** | Targeted diagnostic (Phases I + IV) on the promoted project |
| **Post-crisis** | Targeted diagnostic (Phases II + IV) on the affected subsystem |
| **Annually** | Per-organ full diagnostic; compare against prior year's diagnostic table |
| **On demand** | Triggered by Red assessment in any diagnostic or by external shock |

---

## 8. Output Artifacts

1. **Autopoietic Identity Map** — system boundary, component inventory, production network, single points of failure.
2. **Feedback Loop Atlas** — all feedback loops (negative, positive, dead) with speed and health assessments.
3. **Regenerative Accounting Table** — resource production/consumption with net surplus and trend.
4. **Antifragility Classification Matrix** — all components classified on Taleb's triad with stress test results.
5. **Meta-Layer Diagnostic Table** — G/Y/R assessment with evidence and action items.
6. **Diagnostic Narrative** — prose summary suitable for stakeholder communication.

---

## Appendix: Cross-References

- **Governing document:** `METADOC--research-standards.md` (v3.0.0, Section 3: The Meta-Layer)
- **Upstream — Sources:** `SOP--source-evaluation-and-bibliography.md` (provides evidence base)
- **Upstream — Foresight:** `SOP--strategic-foresight-and-futures.md` (provides scenario context for stress tests)
- **Adjacent — Structural Audit:** `SOP--structural-integrity-audit.md` (Phase IV antifragility complements structural audit Phase IV pathology checklist)
- **Feedback — Source Evaluation:** Diagnostic findings generate new research requirements → `SOP--source-evaluation-and-bibliography.md`
- **Feedback — Foresight:** Diagnostic findings revise scenario inputs → `SOP--strategic-foresight-and-futures.md`
- **Bibliography:** `APPENDIX--research-standards-bibliography.md` (Domain 6)

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
