# The Self-Governing Institution of Checks: Architecture of a Recursive Evaluative System

**Document D** — The grading facility as its own institutional subject
**Date:** 2026-03-15
**Author:** Anthony James Padavano
**Cross-references:** Document A (statistical method), Document B (organism context), Document C (thesis integration)

---

## Abstract

Documents A-C describe a multi-model inter-rater agreement (IRA) facility in service of a career application pipeline — the facility as *tool*. This document inverts the frame. It describes the facility as its own *institution*: a self-governing system of checks with its own constitution (the rubric), its own deliberative body (the rater panel), its own judicial mechanism (consensus and outlier detection), its own amendment process (recalibration), its own archival memory (diagnostic history), and its own failure modes. The central question is not "how does the facility evaluate the pipeline?" but "how does the facility govern itself, and what prevents the evaluator from degrading?" This is the institutional theory of the grading facility — the governance layer beneath the statistical layer.

---

## 1. The Institution, Not the Tool

A hammer does not need governance. It does not drift, degrade, or develop blind spots. A statistical function — ICC, kappa, median — is a hammer: it computes the same output for the same input every time.

But the system that *decides what to compute, who computes it, and what the computation means* is not a hammer. It is an institution. Institutions require governance because their components interact, drift, and conflict in ways that cannot be resolved by the components themselves.

The IRA facility is an institution in this precise sense. It comprises:

- A **constitution** (the rubric) that defines what is measured and how
- A **deliberative body** (the rater panel) that produces evaluative judgments
- A **judicial mechanism** (consensus computation) that resolves disagreements
- A **legislative process** (rubric amendment) that evolves the constitution over time
- An **archival memory** (diagnostic history) that accumulates precedent
- An **executive function** (feedback channels) that translates evaluative findings into operational changes

Each of these components requires its own governance — rules about how it operates, changes, and is held accountable. Without that governance, the evaluative institution degrades just as surely as the productive system it evaluates.

The irony is structural: a system designed to detect degradation in other systems can itself degrade, and its degradation is *harder to detect* because there is nothing above it to notice. This is the recursive governance problem, and it is the subject of this document.

---

## 2. The Constitution: Rubric Governance

### 2.1 The Rubric as Living Document

The grading rubric (`system-grading-rubric.yaml`, currently v1.1) is not a static specification. It is a constitutional document — the highest-level normative artifact in the evaluative institution. Everything downstream (which dimensions are measured, how they are weighted, what the raters are asked to evaluate) derives from it.

Like any constitution, the rubric must be both *stable enough to provide continuity* and *flexible enough to accommodate change*. These demands are in tension. A rubric that changes with every assessment cycle provides no longitudinal comparability — you cannot say "the system improved from 7.2 to 8.5" if the rubric changed between measurements. A rubric that never changes cannot accommodate new quality concerns (Claim Provenance did not exist in v1.0 and would still be invisible without the v1.0→v1.1 amendment).

### 2.2 Amendment Process

The rubric's amendment history establishes precedent:

| Version | Date | Change | Rationale |
|---------|------|--------|-----------|
| 1.0 | 2026-03-05 | Initial: 8 dimensions | Bootstrap the evaluative capacity |
| 1.1 | 2026-03-13 | Add claim_provenance (9th), rebalance weights | Discovery of unsourced statistical claims — a quality gap invisible to the original 8 dimensions |

The v1.0→v1.1 transition reveals the amendment logic: a new dimension is added when *operational experience reveals a quality concern that existing dimensions cannot detect*. The trigger is not theoretical completeness ("we should measure everything") but operational failure ("we found a problem and had no dimension for it").

This is conservative constitutional design: amend only when reality forces amendment, not when theory suggests incompleteness. The benefit is that every dimension in the rubric has an operational justification — it was added because something went wrong that the existing rubric couldn't detect.

### 2.3 Amendment Governance Rules

Proposed governance protocol (not yet formalized in code, but implied by practice):

1. **Trigger**: An operational event reveals a quality concern not captured by existing dimensions
2. **Proposal**: A new dimension is drafted with type, weight, scoring guide, and evidence sources
3. **Weight rebalancing**: Existing weights are adjusted to sum to 1.0 after adding the new weight. No dimension's weight may decrease by more than 0.03 in a single amendment to prevent destabilizing existing longitudinal tracking
4. **Versioning**: The rubric version is incremented (minor version for additions, major version for restructuring). Previous versions are archived, never deleted
5. **Re-baseline**: The first assessment under the new rubric version establishes a new baseline. Longitudinal comparisons acknowledge the version boundary
6. **Sunset provision**: Dimensions that have scored at maximum (10.0) for 5 consecutive assessments are candidates for removal or weight reduction — they have become *structural guarantees* rather than *variable quality indicators* and consume evaluative attention without producing signal

### 2.4 Dimension Retirement vs. Preservation

Should a dimension ever be removed? The tension:

- **For removal**: A dimension at permanent 10.0 (e.g., test_coverage after reaching 2,000+ tests with 100% matrix coverage) no longer differentiates quality states. It consumes weight that could increase the sensitivity of variable dimensions.
- **Against removal**: A dimension at 10.0 today might drop to 7.0 tomorrow if the system degrades. Removing it removes the capacity to detect that degradation. It also destroys longitudinal comparability — a composite score computed without test_coverage is not comparable to one computed with it.

Resolution: *weight reduction, not removal*. A dimension at sustained maximum can have its weight reduced to 0.02 (signal floor) — enough to detect catastrophic regression but not enough to dominate the composite. This preserves the dimension's watchdog function while reallocating most of its weight to dimensions that still vary.

---

## 3. The Deliberative Body: Panel Governance

### 3.1 Panel Composition as Institutional Design

The rater panel is not a random collection of models. It is a deliberately composed deliberative body whose composition embodies assumptions about *what evaluative perspectives matter*. These assumptions are institutional choices that require governance.

Current composition: 4 raters, 3 Anthropic + 1 Google, 4 distinct personas.

The composition encodes several implicit decisions:

- **Panel size (4)**: The minimum for meaningful IRA computation with outlier detection. Shrout & Fleiss (1979) note that ICC confidence intervals narrow significantly between 3 and 5 raters and modestly thereafter. The rubric specifies `min_raters: 3, max_raters: 7`, establishing a governance band.
- **Provider mix (3:1 Anthropic:Google)**: Provides cross-family diversity but is Anthropic-heavy. A 2:2 split would be more balanced but would sacrifice the capability gradient (Opus → Sonnet → Haiku) that tests whether model capability affects evaluative judgment.
- **Persona set (architect, QA, operator, auditor)**: Models four functional roles in a software organization. Does not include: user advocate, security specialist, business analyst, ethicist. Each omission is an institutional choice about whose perspective is *not* represented.

### 3.2 Panel Evolution Rules

Proposed governance:

1. **Addition threshold**: A new rater is added when a quality concern arises that no existing persona can evaluate (e.g., adding a security auditor after a vulnerability is discovered). Maximum 7 raters (rubric `max_raters`) to prevent ICC dilution.
2. **Removal threshold**: A rater is removed if it consistently produces scores within 0.2 of another rater across 5+ consecutive assessments — the two perspectives have converged and no longer provide independent signal. Minimum 3 raters.
3. **Rotation policy**: At least once per quarter, one rater should be replaced with a new persona to prevent institutional calcification. The archived rater's historical scores remain in the longitudinal record.
4. **Model updates**: When a model receives a major version update (e.g., Opus 4.6 → Opus 5.0), the rater is treated as a *new rater* for IRA purposes. Agreement between the pre-update and post-update versions is itself a diagnostic datum — if the new model produces dramatically different scores under the same persona, the persona definition may need recalibration.
5. **Cross-provider minimum**: At least one rater must use a non-majority provider. If 3 raters use Anthropic, at least 1 must use Google, Meta, Mistral, or another provider. This is a constitutional requirement, not a preference.

### 3.3 Persona Authoring as Institutional Act

Every persona is authored by a human. This makes persona authoring the most consequential institutional act in the evaluative system — more consequential than rubric amendment, because the rubric defines *what is measured* while the personas define *how it is interpreted*.

A persona that penalizes complexity will never emerge from an author who does not recognize complexity as a problem. A panel that lacks a security perspective cannot detect security issues. The evaluative institution's blind spots are the persona author's blind spots.

Three mitigation strategies:

**Adversarial persona generation.** Ask an LLM: "Given these existing personas, design a persona that would maximally disagree with all of them on at least 2 dimensions." The generated persona represents a perspective the author did not consider — by construction, it challenges the existing panel's consensus.

**Stakeholder audit.** For each rubric dimension, ask: "Who in a traditional organization would care most about this dimension?" If the answer is a role not represented in the panel, the panel has a gap. Example: no current persona represents a *user* of the system (as opposed to a developer, operator, or auditor). If usability were a dimension, this gap would matter.

**External persona sourcing.** Invite a colleague, mentor, or collaborator to define a persona based on their own evaluative priorities, without seeing the existing personas. Their independent perspective breaks the author's frame.

---

## 4. The Judicial Mechanism: Consensus Governance

### 4.1 Median as Political Choice

The consensus score is computed as the median of all rater scores for each dimension. This is not a neutral mathematical choice — it is a *political* choice with institutional implications.

**Mean** treats all raters equally and is sensitive to outliers. A single rater scoring 2.0 while three score 8.0 produces a mean of 6.5 — substantially lower than any majority view.

**Median** protects against outlier distortion. The same distribution produces a median of 8.0 — the majority view prevails.

**Trimmed mean** (excluding outliers, then averaging) would combine both properties but requires defining "outlier" — introducing a governance decision about what constitutes an extreme view.

The choice of median encodes a principle: *the majority evaluative perspective should prevail, but minority perspectives should be recorded and flagged, not silenced*. This is the institutional analog of a court's majority opinion with documented dissent. The dissenting rater's score is preserved in the ratings archive, available for longitudinal analysis, but does not drag the consensus toward an extreme that most perspectives reject.

### 4.2 Outlier Detection as Minority Protection

The IQR-based outlier detection (scores outside [Q1 - 1.5×IQR, Q3 + 1.5×IQR]) serves a dual function:

1. **Quality control**: Catching scores that result from model errors, prompt misunderstanding, or hallucination
2. **Minority protection**: Flagging scores that represent legitimate minority perspectives deserving investigation

The system *flags* outliers but does *not remove* them from the consensus computation (the median is already robust to outliers). This design choice embeds a governance principle: **no evaluative perspective should be silently discarded**. An outlier score means either "something went wrong with this rater" (investigate the rater) or "this rater sees something the others don't" (investigate the dimension). Both are valuable signals.

### 4.3 The Re-Rate Threshold as Constitutional Crisis Provision

When overall ICC drops below 0.61 (the lower bound of "substantial" agreement per Landis & Koch, 1977), the system triggers a re-rate recommendation. This is the evaluative institution's equivalent of a constitutional crisis — the raters disagree so fundamentally that the consensus has no legitimacy.

The re-rate threshold does not specify *what* to do — it specifies that *something must be done*. Resolution options:

1. **Investigate rubric ambiguity**: Do the scoring guides leave room for conflicting interpretations? Clarify.
2. **Investigate persona conflict**: Have two personas been authored with contradictory bias instructions? Reconcile or acknowledge as deliberate.
3. **Investigate evidence quality**: Did the evidence assembly fail, providing incomplete information to some raters? Fix the evidence pipeline.
4. **Split the dimension**: A dimension that consistently provokes disagreement may be measuring two distinct things. Split it into sub-dimensions that can be independently assessed.
5. **Convene human review**: If automated investigation cannot resolve the crisis, the human operator (Beer's System 5) must intervene.

The threshold is configurable (`re_rate_threshold: 0.61` in the rubric YAML). Domains where evaluative disagreement is expected (e.g., art quality assessment) should lower it. Domains where agreement is critical (e.g., safety assessment) should raise it.

---

## 5. The Archival Memory: Diagnostic History as Institutional Precedent

### 5.1 What Gets Archived

Every assessment cycle produces:

- **Individual rating files** (`ratings/*.json`): Each rater's scores, confidence levels, evidence citations, strengths, and weaknesses per dimension
- **Consensus file** (`ratings/consensus-YYYY-MM-DD.json`): Overall ICC/kappa, per-dimension scores, means, SDs, outlier flags
- **Diagnostic history** (`signals/diagnostic-history/consensus-YYYY-MM-DD.json`): Archival copy with timestamp

Previous rating files are moved to `ratings/archive/YYYY-MM-DD/` before each new session.

### 5.2 Longitudinal Analysis

The archive enables analyses impossible from a single assessment:

**Trend detection**: Is the system improving, degrading, or holding steady? 7-day, 30-day, and 90-day deltas over consensus scores reveal trajectories. Linear regression slopes detect monotonic trends. Inflection point detection (change in slope sign) catches reversals early.

**Dimension stability**: Which dimensions vary assessment-to-assessment? High-stability dimensions may have become structural guarantees (see Section 2.4 on dimension retirement). Low-stability dimensions may indicate genuine quality fluctuation or rubric ambiguity.

**Rater drift**: Does a specific rater's scoring pattern change over time? If the architect-opus rater consistently scored architecture at 8.0 but now scores it at 6.5 after a model update, the rater has drifted. This may reflect genuine system degradation (the new model detects problems the old model missed) or model-version bias (the new model has different evaluative priors). The archive enables the investigation.

**Agreement evolution**: Does ICC change over time? Increasing ICC suggests the system is becoming more robustly good (or the personas are converging — both should be investigated). Decreasing ICC suggests the system is developing quality inconsistencies that different perspectives detect differently.

### 5.3 The Archive as Institutional Memory

In human institutions, judicial precedent constrains future decisions — a court cannot easily reach a conclusion that contradicts its prior rulings without acknowledging and addressing the contradiction. The diagnostic archive functions similarly:

- If the system scores 10.0 on data_integrity for six consecutive assessments and then drops to 7.0, the archive *demands explanation*. The drop cannot be ignored or normalized — the historical record establishes an expectation.
- If a rubric amendment changes a dimension's definition, the archive preserves the old definition's scoring history. Future analysts can understand that the 2026-Q1 scores were under v1.0's definition while Q2 scores are under v1.1's — the archive prevents false longitudinal comparisons.
- If a rater is removed from the panel, their archived ratings remain. Future analysts can reconstruct what the panel's consensus *would have been* with the removed rater included, testing whether the removal changed the institution's evaluative character.

---

## 6. The Executive Function: Feedback Channel Governance

### 6.1 The Four Channels

The evaluative institution translates its findings into operational changes through four feedback channels:

| Channel | Mechanism | Latency | Risk |
|---------|-----------|---------|------|
| Threshold calibration | Detect when scoring thresholds no longer align with attainable scores | Hours | Over-correction (relaxing thresholds too aggressively) |
| Block-outcome correlation | Classify narrative blocks as golden/toxic based on outcome patterns | Weeks-months | Spurious correlation (small sample sizes) |
| External validation | Compare internal assumptions against external market data | Hours | API dependency, data staleness |
| Longitudinal tracking | Detect trends, inflections, and drift over time | Weeks-months | Trend extrapolation past structural breaks |

### 6.2 Feedback Integrity

Each channel has a failure mode that could corrupt the productive system:

**Threshold over-correction**: If the facility detects a threshold problem and relaxes the threshold too aggressively, the production system begins producing low-quality output. Governance: threshold adjustments are capped (no more than 0.5 points per assessment cycle) and require human confirmation above that cap.

**Spurious block correlation**: With small sample sizes (e.g., a block used in only 3 submissions), golden/toxic classification is unreliable. Governance: minimum 5 submissions before a block receives a classification. Below that threshold, the block is classified as "insufficient data."

**External data staleness**: BLS OES data updates annually; Remotive data updates in real-time but may be incomplete. The external validator stores fetch timestamps in its cache and flags data older than 90 days as stale. Governance: stale external data triggers a warning, not a recalibration — the system should not adjust internal parameters based on outdated external signals.

**Trend extrapolation failure**: A 30-day upward trend extrapolated through a structural break (e.g., a major refactoring that temporarily degrades all dimensions) produces a false optimism signal. Governance: trend analysis flags structural breaks (>2 SD change in a single assessment) and restarts trend computation from the new baseline.

### 6.3 The Separation of Powers

A critical governance principle: **the evaluative institution should not be able to modify the productive system's parameters without human authorization** — except in narrowly defined, pre-authorized circumstances.

Current implementation:
- Threshold calibration: *proposes* adjustments, requires `--apply --yes` to execute
- Block correlation: *classifies* blocks, does not automatically modify block selection weights
- External validation: *reports* discrepancies, does not automatically adjust scoring inputs
- Recalibration: *proposes* weight adjustments, requires `--apply --yes` to execute

This separation of powers prevents the evaluative institution from becoming an *autonomous governor* — a system that both evaluates and acts without human oversight. The human retains veto power over all operational changes. The facility has the *right to speak* (produce scores, flag problems, propose adjustments) but not the *right to act* (modify parameters, change thresholds, adjust weights).

This is Beer's System 5 in practice: the policy function (human operator) adjudicates between System 3* (the evaluative institution's findings) and System 3 (the production system's operational needs). Neither subsystem has unilateral authority.

---

## 7. The Meta-Evaluative Problem: What Evaluates the Evaluator?

### 7.1 The Recursive Governance Challenge

The evaluative institution can detect degradation in the productive system. But what detects degradation in the evaluative institution itself? If the rubric ossifies, if the personas converge, if the consensus mechanism begins producing artificially high scores — who raises the alarm?

This is the recursive governance problem. Every system of checks requires its own checks, which require their own checks, creating an infinite regress that can only be terminated by:

1. **Accepting an unmonitored ground floor** (the buck stops somewhere)
2. **Closing the loop** (the system monitors itself recursively)
3. **Invoking an external authority** (a human or external system provides the ground truth)

The conductor methodology uses all three, layered:

### 7.2 Ground Floor: Statistical Self-Monitoring

The IRA computation is its own first-level check. ICC, by definition, measures whether the raters agree. If ICC drops below 0.61, the system flags itself — "my raters disagree too much for my consensus to be meaningful." This is the evaluative institution detecting its own failure mode through the statistical properties of its own output.

This catches:
- Persona divergence (raters with contradictory biases producing irreconcilable scores)
- Evidence assembly failure (some raters received incomplete information)
- Model degradation (a model update changed a rater's evaluative behavior)

This does not catch:
- Unanimous error (all raters agree on a wrong score — high ICC, invalid consensus)
- Rubric obsolescence (the rubric no longer measures what matters — high ICC on irrelevant dimensions)
- Agreeableness collapse (all raters converge to the same scores despite different personas — high ICC but no evaluative diversity)

### 7.3 Recursive Loop: The Meta-Diagnostic

The meta-conductor concept (introduced in Chapter 10, Section 10.6.5) can be partially implemented:

**Define a meta-rubric** with dimensions that evaluate the evaluative institution itself:

| Meta-Dimension | Type | What It Measures |
|---------------|------|------------------|
| Rubric completeness | subjective | Do the 9 dimensions cover the relevant quality space? |
| Persona diversity | objective | How different are the rater scores? (measure: coefficient of variation across raters) |
| Statistical robustness | objective | Are ICC confidence intervals narrow enough for reliable interpretation? |
| Feedback loop latency | objective | How long between detection and correction? |
| Archive integrity | objective | Are all historical assessments preserved with proper versioning? |
| External validation coverage | mixed | What fraction of internal assumptions have external ground truth? |

**Run the meta-diagnostic** periodically (quarterly, or triggered by anomalous primary diagnostic results). The meta-diagnostic answers: "Is the evaluative institution itself functioning properly?"

The recursion terminates here — we do not propose a meta-meta-diagnostic. At this level, the human operator's epistemic audit (Section 7.4) provides the ground truth.

### 7.4 External Authority: The Human Epistemic Audit

The recursive regress terminates with the human asking: **"What might the system be missing?"**

This question cannot be formalized, automated, or delegated. It requires the capacity to recognize unknown unknowns — the epistemically generative act of noticing that a question has not been asked. The evaluative institution can measure along its rubric's dimensions; it cannot measure dimensions that do not exist in the rubric. The human's irreducible contribution is *rubric imagination* — the capacity to conceive of quality properties that the current rubric does not capture.

The operational practice:

1. **Quarterly rubric review**: The human reads the rubric, reads the most recent diagnostic output, and asks: "What quality concerns do I have that this rubric cannot express?" Any concern that survives scrutiny becomes a candidate for rubric amendment (Section 2.3).
2. **Annual persona audit**: The human reviews the persona definitions and asks: "Whose perspective is missing? What kind of evaluator would challenge my current panel's consensus most productively?" The answer becomes a candidate for panel addition (Section 3.2).
3. **External feedback integration**: The human solicits feedback from colleagues, mentors, or users about the system's quality — feedback that arrives through channels entirely outside the evaluative institution's perimeter. Any recurring theme not captured by the rubric reveals a blind spot.

---

## 8. Failure Modes of the Evaluative Institution

### 8.1 Agreeableness Collapse

**Symptom**: All raters produce nearly identical scores despite different personas. ICC is high, but evaluative diversity is absent.

**Mechanism**: LLMs are trained to be helpful and agreeable. Without strong persona bias instructions, raters converge to a "reasonable score" that reflects the model's default judgment rather than the persona's distinct perspective. The scoring bias instruction mitigates this, but model updates can weaken the instruction's effectiveness.

**Detection**: Monitor the coefficient of variation (CV) across raters per dimension. If CV drops below 0.05 for 3+ consecutive assessments, the panel may be collapsing toward consensus.

**Remediation**: Strengthen scoring bias instructions. Increase temperature for the most moderate rater. Replace the most agreeable rater with an adversarially generated persona (Section 3.3).

### 8.2 Rubric Ossification

**Symptom**: The rubric has not been amended in 6+ months despite ongoing system evolution. New capabilities are not measured; deprecated capabilities retain full weight.

**Mechanism**: Rubric amendment requires operational failure as a trigger (Section 2.2). If the system is functioning well, no failures trigger amendments, and the rubric gradually loses relevance as the system evolves beyond it.

**Detection**: Compare the rubric's evidence sources against the actual codebase. If evidence sources reference files, scripts, or commands that no longer exist, the rubric has drifted from reality.

**Remediation**: Schedule quarterly rubric-to-reality reconciliation. For each dimension, verify that its evidence sources are still operational and its scoring guide anchors still describe achievable states.

### 8.3 Persona Monoculture

**Symptom**: Despite nominally different personas, all raters evaluate from similar intellectual frameworks (e.g., all value technical quality, none value user experience or ethical implications).

**Mechanism**: Persona authoring bias — the author's blind spots become the panel's blind spots. If the author is a systems engineer, all personas will implicitly value systems engineering qualities.

**Detection**: Map each persona's scoring bias to a quality taxonomy (e.g., ISO 25010's characteristics). If all personas cluster in the same region of the taxonomy (e.g., Maintainability + Reliability), the panel has a monoculture.

**Remediation**: Use adversarial persona generation (Section 3.3). Commission personas from evaluators in different disciplines. Explicitly target underrepresented regions of the quality taxonomy.

### 8.4 Feedback Loop Corruption

**Symptom**: The evaluative institution's recommendations consistently make the productive system worse, not better.

**Mechanism**: If block-outcome correlation produces spurious classifications (golden blocks that actually reduce quality), and these classifications feed into block selection, the feedback loop amplifies error rather than correcting it.

**Detection**: Track outcome rates before and after feedback-driven changes. If acceptance rates decline after implementing the evaluative institution's recommendations, the feedback loop is corrupt.

**Remediation**: Increase minimum sample sizes for correlation-based recommendations. Implement A/B testing: apply recommendations to half of entries and compare outcomes. Require human confirmation for all recommendations until the feedback loop's integrity is re-established.

### 8.5 Archive Amnesia

**Symptom**: Historical diagnostic data is lost, corrupted, or inaccessible, destroying the institution's longitudinal memory.

**Mechanism**: Disk failures, accidental deletion, format migration, or simply not running the archival step.

**Detection**: The diagnostic script should verify archive integrity at each run: count archived files, verify date continuity, check for gaps.

**Remediation**: Backup the diagnostic archive alongside the pipeline's own backup schedule. Store archive checksums. Flag any assessment cycle that cannot find the previous cycle's archive.

---

## 9. The Evaluative Institution in Organizational Theory

### 9.1 Parallels to Human Institutions

The evaluative institution described here has structural parallels to governance mechanisms in human organizations:

| Evaluative Component | Institutional Parallel |
|---------------------|----------------------|
| Rubric | Constitution or charter |
| Rubric amendment | Constitutional amendment process |
| Rater panel | Board of directors or review committee |
| Panel composition rules | Board nomination and diversity requirements |
| Persona scoring biases | Fiduciary duties and domain expertise requirements |
| Consensus mechanism | Board voting procedure |
| Outlier flagging | Minority opinion / dissent preservation |
| Re-rate threshold | Constitutional crisis provision / quorum failure |
| Diagnostic archive | Corporate minutes and judicial precedent |
| Feedback channels | Executive directives and regulatory compliance |
| Human epistemic audit | Shareholder oversight / external audit |
| Meta-diagnostic | Governance committee reviewing its own effectiveness |

These parallels are not metaphorical — they reflect genuine structural isomorphisms between the governance problems faced by human organizations and AI-augmented institutions. Both must balance stability with adaptability, majority rule with minority protection, operational autonomy with oversight, and institutional memory with evolutionary capacity.

### 9.2 Novel Contributions

What the evaluative institution *adds* beyond human institutional parallels:

1. **Deterministic record-keeping**: Every rating, every consensus, every outlier flag is preserved in machine-readable format. Human institutions rely on meeting minutes that are partial, interpreted, and sometimes contested. The evaluative archive is complete and unambiguous.

2. **Reproducible deliberation**: Given the same system state and the same rubric version, the rater panel will produce *approximately* (temperature notwithstanding) the same scores. Human deliberative bodies produce dramatically different outcomes depending on mood, fatigue, interpersonal dynamics, and who speaks first.

3. **Scalable evaluation**: The 4-rater panel evaluates 9 dimensions in the time it takes to make 4 API calls (~60 seconds). A human review board evaluating the same scope would require hours of preparation, meeting, deliberation, and documentation.

4. **Explicit bias**: The rater personas declare their biases openly. Human evaluators have biases too, but rarely declare them. The evaluative institution's biases are inspectable, auditable, and adjustable — a transparency advantage that no human institution can match.

---

## 10. Conclusion

The self-governing institution of checks is more than an IRA computation with a YAML configuration. It is a recursive governance system with constitutional, deliberative, judicial, legislative, executive, and meta-evaluative layers. Each layer has its own failure modes, its own governance rules, and its own evolutionary dynamics.

The central tension — who evaluates the evaluator? — is resolved through a three-tier architecture:

1. **Statistical self-monitoring** (ICC as internal consistency check)
2. **Recursive meta-diagnostic** (the evaluative institution evaluating itself on meta-dimensions)
3. **Human epistemic audit** (the irreducible capacity to notice what the system cannot notice about itself)

No tier is sufficient alone. The statistical floor catches rater disagreement but misses unanimous error. The meta-diagnostic catches institutional degradation but cannot transcend its own rubric. The human catches unknown unknowns but cannot operate at the frequency and granularity of automated assessment.

Together, they constitute a governance architecture capable of sustaining evaluative integrity over time — not perfectly, not permanently, but with enough self-corrective capacity to detect and address its own degradation before that degradation corrupts the productive system it governs.

This is the institution. Not the tool, not the function, not the pipeline feature. The institution — with its own constitution, its own deliberative body, its own judicial mechanism, its own failure modes, and its own capacity for self-correction. Documenting it as such is necessary because tools are adopted; institutions are built. And building requires understanding governance, not just computation.

---

## References

Beer, S. (1972). *Brain of the Firm*. Allen Lane/Penguin.

Beer, S. (1979). *The Heart of Enterprise*. John Wiley & Sons.

Beer, S. (1985). *Diagnosing the System for Organizations*. John Wiley & Sons.

Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37–46.

Fleiss, J. L. (1971). Measuring nominal scale agreement among many raters. *Psychological Bulletin*, 76(5), 378–382.

ISO/IEC. (2023). *ISO/IEC 25010:2023 — Systems and software engineering — Product quality model*.

Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174.

Luhmann, N. (1995). *Social Systems*. Stanford University Press.

Maturana, H. R., & Varela, F. J. (1980). *Autopoiesis and Cognition*. D. Reidel.

Shrout, P. E., & Fleiss, J. L. (1979). Intraclass correlations: Uses in assessing rater reliability. *Psychological Bulletin*, 86(2), 420–428.

Zheng, L., et al. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. *NeurIPS 2023*.
