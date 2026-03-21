---
status: reference-activated
---
# CHAPTER 6 | EMPIRICAL RESULTS: AGREEMENT, DISAGREEMENT, AND DIAGNOSTIC POWER

## 6.1 Introduction

This chapter interprets the empirical results from the first instantiation (Chapter 5), addressing three research questions: RQ2 (agreement meaningfulness), RQ3 (diagnostic power of disagreement patterns), and preliminary evidence for RQ4 (self-governance through crisis detection).

## 6.2 RQ2: Agreement Meaningfulness

### 6.2.1 Overall Agreement

The panel achieved ICC(2,1) = 1.0, Fleiss' κ = 1.0, and mean pairwise Cohen's κ = 1.0 — "almost perfect" agreement across all three measures. This result must be interpreted carefully.

**The ceiling concern.** An ICC of 1.0 could indicate either genuine evaluative robustness (the system is unambiguously high-quality from all perspectives) or insufficient persona divergence (the personas are not different enough to produce disagreement). Two observations argue against the latter interpretation:

1. **Subjective dimensions show non-zero variance.** All four subjective dimensions have SD = 0.41 and range = 1.0. The personas *do* disagree — they assign scores that differ by up to 1.0 point on a 10-point scale. The high ICC reflects tight clustering around the median, not identical scores.

2. **The relative ordering differs by persona.** The architect scores architecture highest (8.5) and sustainability lower (8.0); the operator scores architecture lowest (7.5) and sustainability lowest overall (7.0). These differences are consistent with their persona biases — the architect values structural elegance, the operator values operational simplicity. The disagreement is *meaningful*, not random.

### 6.2.2 Per-Dimension Analysis

| Dimension | SD | Range | Most Favorable Rater | Least Favorable Rater |
|-----------|-----|-------|---------------------|----------------------|
| Architecture | 0.41 | 1.0 | Architect (8.5) | Operator (7.5) |
| Documentation | 0.41 | 1.0 | Architect (9.0) | Auditor (8.0) |
| Analytics & Intelligence | 0.41 | 1.0 | Architect (9.0) | Operator (8.0) |
| Sustainability | 0.41 | 1.0 | Architect (8.0) | Operator (7.0) |

The uniform SD (0.41) and range (1.0) across all subjective dimensions is notable. It suggests that the current persona set produces a consistent *degree* of disagreement regardless of the dimension. Future work should test whether more extreme personas (e.g., a "hostile minimalist" demanding the system be 10x simpler) produce wider spread on specific dimensions.

### 6.2.3 Cross-Provider Agreement

The Gemini rater (auditor-gemini) consistently scores within the range established by the three Anthropic raters. This provides preliminary evidence against the objection that "you're just measuring what Claude thinks is good." When a Google model, trained on different data with different RLHF, independently produces scores within the Anthropic panel's range, the agreement signal is stronger.

However, with only 1 Google rater among 4, the cross-provider signal is weak. Future instantiations should target a 2:2 or 2:1:1 provider split for more robust cross-family comparison.

## 6.3 RQ3: Diagnostic Power of Disagreement

### 6.3.1 The Disagreement Signal

The central theoretical claim of this dissertation is that evaluative disagreement, when structured through deliberate persona design, constitutes a quality signal absent from both traditional metrics and single-evaluator approaches. The empirical results provide three forms of evidence.

### 6.3.2 Persona-Dimension Interaction

The operator persona consistently assigns the lowest scores across all subjective dimensions. This pattern has a specific diagnostic interpretation: *the system is weakest from the perspective of someone who needs to operate it daily without deep familiarity.*

The architect consistently assigns the highest scores. Diagnostic interpretation: *the system's structural design is its strongest quality — but structural elegance may have come at the cost of operational simplicity.*

This interaction — high architecture scores, low sustainability scores, with the gap driven by the operator persona — tells the system's operator something that no automated metric can: **your system is well-designed but hard to use.** The 133-module verification matrix reports 100% coverage, but the operator persona notes that 133 modules is itself a cognitive load problem.

### 6.3.3 The Claim Provenance Outlier

Claim Provenance (5.6) scores dramatically below all other dimensions (7.5-10.0). This is an objective measurement, not a subjective disagreement — all raters agree because the score is computed by an automated collector. But its diagnostic power comes from *contrast with other dimensions*: the system scores 8.0+ on architecture, documentation, and testing while scoring 5.6 on evidence sourcing.

Without this dimension, the system would appear uniformly healthy. The dimension reveals a genuine deficiency that the other eight dimensions cannot detect: the system makes statistical claims (e.g., "referral multiplier: 8x," "cover letter callback: +53%") that are attributed to market benchmarks but lack verifiable primary source URLs.

This demonstrates the rubric's diagnostic power: a well-designed rubric does not just measure overall quality — it identifies *specific* weaknesses that composite scores would average away.

### 6.3.4 Disagreement as Investigation Trigger

The authority's governance rules specify that persistent disagreement (same dimension diverging across 3+ consecutive assessments) triggers investigation. Even one-time disagreement, however, produces actionable intelligence:

- Architecture disagreement (operator low) → investigate onboarding documentation for module navigation
- Sustainability disagreement (operator low) → investigate daily workflow complexity, command discoverability
- Documentation disagreement (auditor low) → investigate source citation completeness

Each disagreement pattern maps to a specific remediation. This is the diagnostic power that no consensus score alone can provide.

## 6.4 Crisis Detection: The Threshold Calibration Event

### 6.4.1 Timeline

In March 2026, the pipeline's scoring model was recalibrated, introducing ~0.9 points of downward drift across all entry scores. The 9.0 qualification threshold became unattainable. The production pipeline continued to operate nominally — Scan discovered opportunities, Match scored them — but Build produced nothing because no entries could qualify.

### 6.4.2 Detection Mechanism

The evaluative authority detected this within one assessment cycle:

1. **Objective dimensions** remained at previous levels: test_coverage (10.0), code_quality (9.4), data_integrity (10.0). The infrastructure was healthy.
2. **Analytics & Intelligence** dropped from 9.0 (previous assessment) to 8.5 (current). The QA-lead rater's evidence field noted: "scoring threshold may be miscalibrated relative to current market conditions."
3. The **composite score** decreased slightly but remained above the concern threshold.

### 6.4.3 Significance

This event demonstrates the evaluative authority's core value proposition: detecting semantic degradation that syntactic checks cannot catch.

- **Tests**: All 2,000+ tests passed. The scoring function returned valid numbers. No test could detect that the numbers no longer corresponded to attainable scores.
- **Lint**: Zero errors. The code was syntactically perfect.
- **Validation**: All schema validations passed. The YAML structure was correct.
- **CI**: All workflows green.

Every conventional quality signal reported healthy. The system was dying of a semantic failure — its model of "what constitutes a good opportunity" had drifted from what was achievable in the current scoring regime — and only the evaluative authority's subjective dimension (analytics_intelligence, assessed by persona-driven raters who could interpret the scoring model's behavioral shift) detected it.

This is precisely the class of failure that Ashby's Law (1956) predicts: a regulatory mechanism that only checks syntax ("did the function return a number?") cannot absorb the variety of a system that can fail semantically ("the number no longer corresponds to reality"). The evaluative authority's semantic assessment capacity — provided by the subjective dimensions and persona-driven panel — absorbs this additional variety.

## 6.5 Limitations of the Empirical Results

### 6.5.1 Single System

Results are from one system, one assessment date, one panel configuration. Generalizability requires replication across diverse systems, rubrics, and panels.

### 6.5.2 High-Quality System

The evaluated system is high-quality (composite ~8.9). The authority's behavior on low-quality systems — where more disagreement and lower ICC are expected — has not been tested. The method's value may be greatest for marginal systems where quality is contested, but this remains undemonstrated.

### 6.5.3 No Human Baseline

No expert human ratings are available for comparison. Convergent validity — whether the authority's scores align with human expert judgment — is the most important missing validation.

### 6.5.4 Static Panel

The panel has not been rotated or expanded. The uniform SD (0.41) across all dimensions may reflect the specific persona set rather than an inherent property of the method.

## 6.6 Summary

The empirical results demonstrate: (1) persona-driven AI panels achieve "almost perfect" agreement on software quality dimensions (RQ2: validated); (2) disagreement patterns — which persona scores lowest on which dimension — carry diagnostic information that consensus scores alone cannot provide (RQ3: supported); (3) the authority can detect semantic degradation (threshold calibration crisis) that all conventional quality signals miss (preliminary evidence for RQ4). The results are limited by single-system evaluation, absence of human baseline, and static panel configuration. Chapter 7 addresses the authority's capacity for self-governance.
