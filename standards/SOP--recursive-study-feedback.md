# SOP: Recursive Study & Feedback Loop (The Ouroboros)

## 1. Ontological Purpose

This SOP closes the open loop between the Research Pipeline and the Study Suite. Without it, research flows linearly (intake → synthesis → specification) and studies observe passively (read → report). Neither feeds the other.

A recursive system is one where **study outputs become research inputs**, and **research outputs trigger new studies**. The system studies itself, learns from what it finds, refines its own processes, and studies the refinements. This is the autopoietic promise made concrete: the system that regenerates its own knowledge-producing apparatus.

**Constraint:** The human conductor remains the gate between observation and action. Studies propose; the conductor decides. This SOP governs the *routing*, not the *authority*.

**Upstream:** `METADOC--research-standards.md` (research pipeline), Study Suite founding spec (`research/2026-03-08-ontological-topology-of-organvm.md`, §IV).
**Downstream:** All SOPs in the research cluster + all Study Suite agents.

---

## 2. The Feedback Cycle

```
                    ┌─────────────────────────────────────┐
                    │                                     │
                    ▼                                     │
            ┌──────────────┐                              │
            │   RESEARCH   │  37 docs, 81 sources,        │
            │   CORPUS     │  22 principles, 29 SOPs      │
            └──────┬───────┘                              │
                   │                                      │
                   │ triggers (new doc, new principle,     │
                   │ SOP change, session log)              │
                   ▼                                      │
            ┌──────────────┐                              │
            │  STUDY SUITE │  Reviewer, Experimenter,     │
            │  (observe)   │  Auditor                     │
            └──────┬───────┘                              │
                   │                                      │
                   │ produces (findings, hypotheses,       │
                   │ audit reports)                        │
                   ▼                                      │
            ┌──────────────┐                              │
            │   TRIAGE     │  Human conductor reviews     │
            │   (decide)   │  study output                │
            └──────┬───────┘                              │
                   │                                      │
                   │ routes to one of 5 actions:           │
                   ▼                                      │
        ┌──────────────────────────────────┐              │
        │  A. Refine (principles/SOPs)     │──────────────┤
        │  B. Investigate (new research)   │──────────────┤
        │  C. Correct (fix drift/errors)   │──────────────┤
        │  D. Deprecate (remove stale)     │──────────────┤
        │  E. Archive (acknowledge, defer) │              │
        └──────────────────────────────────┘              │
                                                          │
            Actions A-D modify the corpus ────────────────┘
            which triggers new studies
```

The cycle has no terminus. Each action that modifies the corpus triggers new study observations. Archive (E) is the only action that does NOT feed back — it acknowledges a finding without modifying anything.

---

## 3. Trigger Events

Studies are not run on a fixed schedule. They are triggered by events in the corpus.

| Event | Agents Triggered | Study Type |
|-------|-----------------|------------|
| New research document added to `research/` | Reviewer | Citation graph update, consilience check, terminology scan |
| New or modified derived principle in `lessons/` | Experimenter | Hypothesis formulation for the principle |
| New or modified SOP in `standards/` | Auditor | Cross-reference integrity, consistency check |
| Session log committed to `sessions/` | Reviewer + Auditor | Cross-session pattern analysis, agent risk update |
| Study output committed to `studies/` | Reviewer | Meta-study: does the finding contradict or reinforce existing findings? |
| Promotion event in registry | Auditor + Experimenter | Governance compliance check, hypothesis test (did promotion match predictions?) |
| Triage action taken (A-D) | All three | Verify the action didn't introduce new inconsistencies |

**The recursive trigger:** When a study output is committed to `studies/`, the Reviewer is triggered to check whether it contradicts or reinforces existing findings. This is the system studying its own studies — the Ouroboros bite.

---

## 4. Triage Protocol

When study output arrives, the conductor triages each finding:

### Step 1: Severity Classification

The study output already classifies severity (CRITICAL / WARNING / INFO per the Auditor, or consilience scores per the Reviewer, or confirmed/refuted per the Experimenter). The conductor validates the classification.

### Step 2: Route to Action

| Finding Type | Typical Action | Resulting Modification |
|-------------|---------------|----------------------|
| Contradiction between principles | **A. Refine** | Update `derived-principles.md` to resolve or document the tension |
| Unoperationalized research insight | **B. Investigate** | New research document or SOP draft |
| Terminology drift | **A. Refine** | Glossary update, SOP language alignment |
| Governance rule violation | **C. Correct** | Registry/seed fix, governance rule update |
| Confirmed hypothesis | **A. Refine** | Strengthen principle's consilience score, embed in SOP |
| Refuted hypothesis | **D. Deprecate** | Weaken or remove the principle, update dependents |
| Orphan document (zero citations) | **B. Investigate** or **E. Archive** | Integrate into corpus or acknowledge as dead end |
| SOP cross-reference error | **C. Correct** | Fix the reference |
| Agent behavioral risk update | **A. Refine** | Update `agent-behavioral-risks.md` |
| Meta-study contradiction | **B. Investigate** | Deeper study to resolve |

### Step 3: Record the Decision

Every triage decision is logged in `studies/triage-log.md` (append-only):

```markdown
## YYYY-MM-DD | {finding-id}

**Source:** {study-file}
**Finding:** {one-line summary}
**Severity:** {CRITICAL/WARNING/INFO}
**Action:** {A/B/C/D/E} — {description}
**Resulting change:** {file modified or "none (archived)"}
**Re-study trigger:** {yes/no — does this action require re-observation?}
```

---

## 5. The Five Lenses

Every study applies one or more analytical lenses from the research standards. These are not optional — they ensure recursive depth, not recursive shallowness.

| Lens | Source SOP | What It Sees | Study Suite Role |
|------|-----------|-------------|-----------------|
| **Historiographic** | `SOP--typological-hermeneutic-analysis.md` | How did this idea/pattern evolve over time? What historical forms does it echo? | Reviewer: trace concept genealogy across dated documents |
| **Ontological** | `METADOC--research-standards.md` §6 | What IS the current state? What lifecycle phase is this finding relevant to? | Auditor: compare declared state vs. actual state |
| **Teleological** | `SOP--strategic-foresight-and-futures.md` | Where does this finding point? What futures does it enable or foreclose? | Experimenter: design scenarios from confirmed hypotheses |
| **Autopoietic** | `SOP--autopoietic-systems-diagnostics.md` | Can the system regenerate this capability? Is the feedback loop healthy? | Auditor: assess whether the recursive cycle itself is functioning |
| **Consilient** | `METADOC--research-standards.md` §1 | Do independent lines of evidence converge? | Reviewer: score convergence across documents, sessions, and studies |

### Lens Application Rules

- **Single-finding studies** (e.g., fixing a cross-reference error): minimum 1 lens (Ontological).
- **Pattern-level studies** (e.g., terminology drift): minimum 3 lenses (Historiographic + Ontological + Consilient).
- **System-level studies** (e.g., governance drift audit): all 5 lenses mandatory.
- **Meta-studies** (studying study outputs): Autopoietic lens is mandatory — you are studying the study system itself.

---

## 6. Recursive Depth Controls

Unbounded recursion produces noise, not knowledge. These controls prevent the Ouroboros from choking on its own tail.

### 6.1 Depth Limit

A study can trigger at most **3 levels of re-study** before requiring human intervention:

```
Level 0: Original study (e.g., R1: Consilience Index)
Level 1: Meta-study triggered by Level 0 output
Level 2: Meta-meta-study triggered by Level 1 output
Level 3: HALT — human reviews the chain before any further recursion
```

### 6.2 Diminishing Returns Gate

If a re-study produces findings that are ≥80% identical to the study that triggered it, the cycle halts with a "convergence report." The system has stabilized — further recursion adds no new knowledge.

### 6.3 Token Budget Cap

No single recursive chain (Level 0 through Level 3) may exceed **500K tokens** total. If the budget is exhausted, the chain halts and surfaces what it has.

### 6.4 Staleness Window

Study outputs older than 90 days without re-validation are marked STALE. Stale studies do not trigger re-study — they trigger a fresh study from Level 0.

---

## 7. Integration with Existing SOPs

This SOP does not replace existing research SOPs. It wires them into the feedback loop.

### 7.1 Research Pipeline → Study Suite (Forward Arc)

When any research SOP produces output:

| SOP | Output | Study Trigger |
|-----|--------|--------------|
| Source Evaluation | Annotated bibliography | Reviewer: check for orphan sources, citation coverage |
| Typological Analysis | Covenants, pattern language | Experimenter: formulate testable hypotheses from covenants |
| Market Gap Analysis | Competitor matrix, gap register | Reviewer: cross-reference against existing research for consilience |
| Research-to-Implementation | Technical specs, backlog items | Auditor: verify specs reference their research lineage |
| Strategic Foresight | Scenarios, backcasted roadmaps | Experimenter: test scenario predictions against actual outcomes |
| Autopoietic Diagnostics | Diagnostic table, regenerative score | Auditor: compare diagnostic findings against study findings |

### 7.2 Study Suite → Research Pipeline (Return Arc)

When study output requires action A (Refine) or B (Investigate):

| Study Finding | Research SOP Invoked | Purpose |
|--------------|---------------------|---------|
| Unoperationalized insight | Research-to-Implementation (Stage IV) | Transform insight into specification |
| Terminology drift | Source Evaluation (Phase IV: Gap) | Standardize terminology, update glossary |
| Refuted principle | Typological Analysis (Phase V: Reconstruction) | Re-derive the principle from first principles |
| Governance violation | Autopoietic Diagnostics (Phase II) | Diagnose why the violation occurred |
| Convergent evidence | Strategic Foresight (Phase IV: Backcasting) | Use confirmed patterns to refine roadmap |
| New agent risk | Source Evaluation (Phase I: Discovery) | Research the risk pattern in academic literature |

### 7.3 Study Suite → Study Suite (Meta Arc)

When study output contradicts a previous study:

1. Reviewer compares the two findings and produces a **contradiction report** in `findings/`.
2. Experimenter designs a **resolution hypothesis** — which finding is more likely correct, and why?
3. Auditor checks whether either finding was based on **stale or invalid data**.
4. The three outputs are bundled as a **meta-study package** for triage.

This is Level 1 recursion. It answers: "Our studies disagree with each other — which one is right?"

---

## 8. Output Schema

All recursive study outputs use a standard frontmatter:

```yaml
---
study_id: "{agent}-{YYYY-MM-DD}-{slug}"
agent: reviewer | experimenter | auditor
level: 0 | 1 | 2 | 3
triggered_by: "{event type}: {source file or event}"
lenses_applied: [historiographic, ontological, teleological, autopoietic, consilient]
token_budget_used: {number}
token_budget_remaining: {number}  # within the recursive chain
findings_count: {number}
actions_proposed: {number}
convergence_score: {0-100}  # 100 = fully converged with prior studies
---
```

Body follows the agent-specific format (findings journal for Reviewer, hypothesis registry for Experimenter, audit report for Auditor).

---

## 9. Bootstrap Sequence

To activate the recursive loop for the first time:

### Phase 1: Seed Studies (Level 0)
Run the P0 studies from `STUDY-PROMPTS.md`:
- R1: Consilience Index (Reviewer)
- G1: Governance Rule Drift (Auditor)
- X1: Governance-as-Soil Hypothesis (Experimenter)

These establish the baseline that all subsequent recursion builds on.

### Phase 2: First Triage
Conductor reviews Phase 1 outputs. Routes each finding to an action (A-E). Records decisions in `triage-log.md`.

### Phase 3: Forward Arc
Actions A-D modify the corpus. These modifications are the first real recursion triggers — they cause the system to re-observe itself.

### Phase 4: First Re-Study (Level 1)
Triggered studies observe what changed. The Reviewer checks whether the modifications introduced consilience or contradiction. The Auditor checks whether the modifications are consistent with governance. The Experimenter checks whether any new testable predictions emerged.

### Phase 5: Steady State
The system is now in continuous operation. Events trigger studies. Studies trigger triage. Triage triggers actions. Actions trigger re-studies. The conductor governs the pace by controlling how quickly triage decisions are made.

---

## 10. Verification

The recursive system is healthy when:

- [ ] Every triage decision has a logged entry in `triage-log.md`
- [ ] No study output is older than 90 days without re-validation or STALE marking
- [ ] The depth limit (Level 3) has never been exceeded without human review
- [ ] The token budget cap (500K per chain) has never been silently exceeded
- [ ] The convergence gate has fired at least once (proving the system can stabilize)
- [ ] At least one Level 1 meta-study exists (proving the system can study its own studies)
- [ ] The triage log shows all 5 action types used at least once (proving the full routing vocabulary is exercised)
- [ ] No study finding has been ignored for more than 30 days without an explicit Archive (E) decision

---

*Version: 1.0.0 | System-Wide Directive | ORGANVM*
