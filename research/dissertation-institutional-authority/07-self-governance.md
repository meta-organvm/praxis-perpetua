# CHAPTER 7 | SELF-GOVERNANCE: THE META-EVALUATIVE PROBLEM

## 7.1 Introduction

The evaluative authority detects degradation in host systems. But what detects degradation in the authority itself? If the rubric ossifies, if the personas converge, if the consensus mechanism produces artificially high scores — who raises the alarm?

This is the recursive governance problem. This chapter addresses RQ4: *Can the authority detect its own governance failures through self-monitoring mechanisms?*

## 7.2 Taxonomy of Authority Failure Modes

### 7.2.1 Agreeableness Collapse

**Definition**: All raters produce nearly identical scores despite different personas. ICC is high, but evaluative diversity is absent.

**Mechanism**: LLMs are trained to produce helpful, balanced responses. Without strong scoring bias instructions, the persona framing is insufficient to overcome this training prior. All raters converge to a "reasonable score" that reflects the model's default judgment rather than the persona's distinctive perspective.

**Detection metric**: Coefficient of variation (CV) across rater scores per dimension. CV = SD / mean. If CV < 0.05 for a dimension across 3+ consecutive assessments, the panel may be collapsing.

**Remediation**: (a) Strengthen scoring bias instructions — make the directional preference more extreme. (b) Increase temperature for the most moderate rater. (c) Replace the most agreeable rater with an adversarially generated persona.

### 7.2.2 Rubric Ossification

**Definition**: The rubric has not been amended despite significant evolution in the host system. New capabilities are not measured; deprecated capabilities retain full weight.

**Mechanism**: Rubric amendment requires operational failure as a trigger (Chapter 3, Section 3.3). If the host system is functioning well, no failures trigger amendments, and the rubric gradually loses alignment with the system's actual quality profile.

**Detection metric**: Evidence source validity check. For each dimension's evidence sources, verify: (a) commands still execute without error; (b) file paths still exist; (c) scoring guide anchor descriptions still describe achievable states. An evidence source failure rate > 10% indicates rubric drift.

**Remediation**: Quarterly rubric-to-reality reconciliation. Update stale evidence sources. Consider adding dimensions for capabilities that have emerged since the last rubric version.

### 7.2.3 Persona Monoculture

**Definition**: Despite nominally different personas, all raters evaluate from similar intellectual frameworks.

**Mechanism**: Persona authoring bias. If the author is a systems engineer, all personas implicitly value engineering qualities — even the "operator" and "auditor" personas are conceived from an engineering perspective.

**Detection metric**: Map each persona's scoring bias keywords to a quality taxonomy (e.g., ISO 25010 characteristics). Compute the centroid of the panel's coverage. If all personas cluster within 2 ISO characteristics, the panel has a monoculture.

**Remediation**: (a) Adversarial persona generation — ask an LLM to design a persona that maximally disagrees with the existing panel. (b) External persona sourcing — invite a domain outsider to define a persona. (c) Taxonomy gap analysis — identify ISO 25010 characteristics not covered by any persona and create a persona targeting that gap.

### 7.2.4 Feedback Loop Corruption

**Definition**: The authority's recommendations consistently worsen the host system.

**Mechanism**: Spurious correlation (small sample size) or overfitting (recommendations chase noise in outcome data).

**Detection metric**: Track host system performance (outcome rates) before and after implementing the authority's recommendations. If performance degrades after implementing recommendations from a specific feedback channel, that channel may be corrupt.

**Remediation**: (a) Increase minimum sample sizes for correlation-based recommendations. (b) Implement A/B testing: apply recommendations to half of entries and compare outcomes. (c) Pause the corrupt channel pending human review.

### 7.2.5 Archive Amnesia

**Definition**: Historical diagnostic data is lost, corrupted, or inaccessible.

**Mechanism**: Disk failure, accidental deletion, format migration, or simply not running the archival step.

**Detection metric**: At each assessment, verify: (a) previous assessment exists in archive; (b) date sequence is continuous (no gaps); (c) file checksums match (no silent corruption).

**Remediation**: Include the diagnostic archive in the host system's backup schedule. Store checksums. Flag any assessment that cannot find the previous cycle's archive.

## 7.3 The Three-Tier Meta-Evaluative Architecture

The recursive governance problem — what evaluates the evaluator? — is resolved through three tiers, each catching failure modes the previous tier cannot.

### 7.3.1 Tier 1: Statistical Self-Monitoring (Automated)

The IRA computation is its own first-level check. ICC measures whether raters agree; by definition, a drop in ICC indicates evaluative dysfunction. The re-rate threshold (ICC < 0.61) is the trigger.

**Catches**: Persona divergence beyond productive disagreement, evidence assembly failure, model degradation after updates, prompt injection or hallucination in rater outputs.

**Cannot catch**: Unanimous error (all raters agree on a wrong score — high ICC, invalid consensus), rubric obsolescence (high agreement on irrelevant dimensions), agreeableness collapse (high ICC, no evaluative diversity).

### 7.3.2 Tier 2: Meta-Diagnostic (Periodic)

A second rubric evaluates the authority itself. This meta-rubric has 6 dimensions (Chapter 3, Section 3.8.2): rubric currency, persona diversity, statistical robustness, feedback latency, archive integrity, and external validation coverage.

The meta-diagnostic runs on a slower cadence (quarterly, or triggered by anomalous primary results). Its output answers: "Is the evaluative institution itself functioning properly?"

**Catches**: Rubric ossification (stale evidence sources), persona monoculture (low CV across raters), archive integrity loss, feedback latency degradation.

**Cannot catch**: The meta-rubric's own blind spots. If a critical meta-quality dimension is absent from the meta-rubric, the meta-diagnostic cannot detect the gap.

### 7.3.3 Tier 3: Human Epistemic Audit (Quarterly)

The recursion terminates with the human asking: *"What might the system be missing?"*

This question cannot be automated. It requires the capacity to recognize unknown unknowns — to notice that a question has not been asked. The human reads the rubric, reads the most recent diagnostic output, and asks whether the rubric's dimensions still capture what matters. Any concern that survives scrutiny becomes a candidate for rubric amendment.

**Catches**: Unknown unknowns — quality properties that no existing rubric dimension captures. New stakeholder perspectives not represented by any persona. Ethical concerns that emerge from operational context rather than from the rubric's quality taxonomy.

**Cannot catch**: Nothing beyond the human's own cognitive horizon. The human is the ground floor; there is no tier 4.

## 7.4 Formal Properties of the Three-Tier Architecture

### 7.4.1 Completeness

The three tiers are *asymptotically complete* in the following sense: any failure mode that produces observable consequences will eventually be detected by one of the three tiers, provided:

1. Statistical self-monitoring runs with every assessment (catches rate-level failures)
2. Meta-diagnostic runs periodically (catches institutional-level failures)
3. Human epistemic audit runs periodically (catches conceptual-level failures)

Failure modes that produce *no observable consequences* — silent degradation with no effect on any measurable outcome — are undetectable by any mechanism, including human observation. This is a fundamental limit, not a design deficiency.

### 7.4.2 Non-Redundancy

Each tier catches failure modes the others cannot:

| Failure Mode | Tier 1 | Tier 2 | Tier 3 |
|-------------|--------|--------|--------|
| Rater divergence | ✓ | | |
| Evidence assembly failure | ✓ | | |
| Rubric ossification | | ✓ | |
| Persona monoculture | | ✓ | |
| Archive integrity loss | | ✓ | |
| Agreeableness collapse | ✓* | ✓ | |
| Feedback loop corruption | | ✓ | |
| Unknown unknowns | | | ✓ |
| Conceptual blind spots | | | ✓ |

*Tier 1 detects agreeableness collapse only if it produces *low* ICC (raters collapsing to identical scores on some dimensions but not others). If all raters converge uniformly, ICC remains high and Tier 1 misses it; Tier 2's CV check catches it.

### 7.4.3 Termination

The recursion terminates at Tier 3. We do not propose a meta-meta-diagnostic for three reasons:

1. **Diminishing returns**: Each meta-level adds complexity but catches increasingly rare failure modes
2. **Human ground**: The human's epistemic audit is inherently non-recursive — the human does not need a meta-meta-audit to question their own assumptions (though they can, and should, seek external perspectives)
3. **Practical tractability**: Three tiers are implementable, auditable, and sustainable. Four or more tiers would exceed the governance budget of a one-person institution

## 7.5 Governance Budget

Self-governance has costs. The authority's meta-evaluative operations require:

| Activity | Frequency | Time | Cost |
|----------|-----------|------|------|
| Tier 1 (statistical check) | Every assessment | 0 sec (computed automatically) | $0 |
| Tier 2 (meta-diagnostic) | Quarterly | 15 min (automated + review) | ~$0.10 (API calls) |
| Tier 3 (human audit) | Quarterly | 1-2 hours (human reading + thinking) | Operator time |
| Rubric amendment | As triggered | 1-4 hours (design + validation) | Operator time |
| Panel rotation | Quarterly | 30 min (configure new persona, test) | ~$0.10 |

Total annual governance budget: ~8-12 hours of human time + ~$1 in API costs. This is dramatically less than the cost of the governance failures it prevents (the threshold calibration crisis, undetected, would have cost weeks of lost applications).

## 7.6 Answering RQ4

*Can the authority detect its own governance failures through self-monitoring mechanisms?*

**Answer**: Partially, with caveats. The three-tier architecture provides detection mechanisms for the five identified failure modes (agreeableness collapse, rubric ossification, persona monoculture, feedback corruption, archive amnesia). Tier 1 (statistical) and Tier 2 (meta-diagnostic) are automated and catch 4 of 5 modes. Tier 3 (human audit) catches the remaining mode (unknown unknowns) and provides the terminating ground for the recursive governance problem.

The authority cannot detect failure modes that produce no observable consequences, and cannot transcend the epistemic horizon of its rubric + the human's imagination. These are fundamental limits shared by all governance systems, including human institutional governance.

## 7.7 Summary

The self-governance problem — what evaluates the evaluator? — is resolved through a three-tier architecture: statistical self-monitoring (automated, every assessment), meta-diagnostic (periodic, quarterly), and human epistemic audit (periodic, quarterly). Five failure modes are identified, each with detection metrics and remediation strategies. The architecture is non-redundant (each tier catches modes the others miss), asymptotically complete (any observable failure will eventually be detected), and terminable (recursion stops at the human). Annual governance budget: ~8-12 hours + ~$1.
