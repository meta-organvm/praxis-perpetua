# CHAPTER 4 | THE METHOD: PSYCHOMETRIC GOVERNANCE MECHANISMS

## 4.1 Introduction

This chapter formalizes the statistical apparatus that constitutes the evaluative authority's judicial mechanism. Three agreement measures — ICC(2,1), Cohen's kappa, and Fleiss' kappa — are specified with sufficient mathematical detail to serve as an implementation reference. The consensus computation, outlier detection, and composite scoring procedures are formalized. All methods are implementable in pure Python standard library without external statistical dependencies.

The chapter answers the methodological component of RQ2: *What statistical framework enables meaningful agreement measurement among persona-driven AI evaluators?*

## 4.2 Design Principles

### 4.2.1 Pure-Stdlib Implementation

The evaluative authority's statistical module requires no scipy, numpy, statsmodels, or other external packages. This is a deliberate architectural choice with three motivations:

1. **Self-containment**: The authority should be deployable as a single package without dependency chains that may conflict with host system requirements
2. **Auditability**: Any practitioner who can read Python arithmetic can verify the statistical computations. No opaque C extensions or Fortran subroutines stand between the specification and the implementation
3. **Portability**: The module runs on any Python ≥ 3.11 installation without compilation or binary dependencies

The cost is performance: pure-Python implementations are slower than optimized C/Fortran alternatives. For the authority's workload (matrices of 4-7 raters × 9 dimensions = 36-63 cells), this cost is negligible — computation completes in <1 millisecond.

### 4.2.2 Ratings Matrix Convention

All computations operate on a ratings matrix **R** of shape (n × k), where:
- n = number of subjects (rubric dimensions being evaluated)
- k = number of raters (panel members who provided scores)
- R[i][j] = rater j's score for dimension i

For the evaluative authority's typical configuration: n = 4 (subjective dimensions only, since IRA is meaningless for zero-variance objective dimensions) and k = 4 (panel members).

## 4.3 ICC(2,1): Intraclass Correlation Coefficient

### 4.3.1 Model Selection

ICC(2,1) is the "two-way random effects, single measures, absolute agreement" form from the Shrout & Fleiss (1979) taxonomy. The model treats both dimensions (rows) and raters (columns) as random effects — samples from larger populations of possible quality dimensions and possible evaluative personas, respectively.

Absolute agreement (rather than consistency) is chosen because we require that raters assign the same *score*, not merely the same *ranking*. A rater who consistently scores 2 points higher than all other raters has meaningful disagreement, even if the ranking is preserved. Absolute agreement captures this; consistency does not.

### 4.3.2 Computation

Given the ratings matrix R with n rows and k columns:

**Step 1: Compute means.**
- Grand mean: x̄ = (1/nk) · ΣᵢΣⱼ R[i][j]
- Row means: x̄ᵢ = (1/k) · Σⱼ R[i][j] for each dimension i
- Column means: x̄ⱼ = (1/n) · Σᵢ R[i][j] for each rater j

**Step 2: Compute sum of squares.**
- SS_between_subjects = k · Σᵢ (x̄ᵢ - x̄)²
- SS_between_judges = n · Σⱼ (x̄ⱼ - x̄)²
- SS_error = ΣᵢΣⱼ (R[i][j] - x̄ᵢ - x̄ⱼ + x̄)²
- SS_total = ΣᵢΣⱼ (R[i][j] - x̄)²

**Step 3: Compute mean squares.**
- BMS = SS_between_subjects / (n - 1)
- JMS = SS_between_judges / (k - 1)
- EMS = SS_error / ((n - 1)(k - 1))

**Step 4: Compute ICC(2,1).**

```
ICC(2,1) = (BMS - EMS) / (BMS + (k-1)·EMS + (k/n)·(JMS - EMS))
```

### 4.3.3 Interpretation

ICC values range from -1.0 to 1.0:
- 1.0: Perfect agreement (all raters assign identical scores)
- 0.0: Agreement equals chance
- Negative: Systematic disagreement (raters inversely correlated)

Interpretation follows configurable bands (default: Landis & Koch, 1977):

| ICC Range | Interpretation |
|-----------|---------------|
| < 0.00 | Poor |
| 0.00–0.20 | Slight |
| 0.21–0.40 | Fair |
| 0.41–0.60 | Moderate |
| 0.61–0.80 | Substantial |
| 0.81–1.00 | Almost perfect |

### 4.3.4 Boundary Cases

- **k = 1**: ICC is undefined (requires ≥ 2 raters)
- **n = 1**: ICC reduces to comparing a single dimension across raters (low statistical power)
- **BMS = EMS**: ICC = 0 (no systematic between-dimension variance)
- **All scores identical**: BMS = JMS = EMS = 0; ICC is defined as 1.0 by convention

## 4.4 Cohen's Kappa

### 4.4.1 Purpose

Cohen's kappa (Cohen, 1960) measures chance-corrected agreement between exactly two raters on categorical data. The evaluative authority computes it for all (k choose 2) rater pairs, producing a pairwise agreement matrix.

### 4.4.2 Score Categorization

Continuous scores must be binned into categories for kappa computation. The default binning:

| Category | Score Range | Label |
|----------|------------|-------|
| 1 | [1.0, 3.5) | Low |
| 2 | [3.5, 6.5) | Medium |
| 3 | [6.5, 9.5) | High |
| 4 | [9.5, 10.0] | Maximum |

The binning is configurable. Finer bins increase sensitivity but require larger n for stable estimates.

### 4.4.3 Computation

For two raters A and B evaluating n dimensions:

1. Construct the k×k confusion matrix C, where C[a][b] = count of dimensions where rater A assigned category a and rater B assigned category b
2. Compute observed agreement: p_o = (1/n) · Σᵢ C[i][i] (sum of diagonal)
3. Compute expected agreement: p_e = (1/n²) · Σᵢ (row_sum_i · col_sum_i)
4. Kappa: κ = (p_o - p_e) / (1 - p_e)

### 4.4.4 Interpretation

Same scale as ICC. κ = 1 indicates perfect agreement beyond chance; κ = 0 indicates agreement at chance level; κ < 0 indicates agreement below chance (systematic disagreement).

## 4.5 Fleiss' Kappa

### 4.5.1 Purpose

Fleiss' kappa (Fleiss, 1971) generalizes to multiple raters simultaneously. Unlike Cohen's kappa (which is pairwise), Fleiss' kappa computes agreement across the entire panel at once.

### 4.5.2 Computation

For n subjects (dimensions) rated by k raters into c categories:

1. For each dimension i and category j, let n_ij = count of raters who assigned category j to dimension i
2. Compute proportion per category: p_j = (1/nk) · Σᵢ n_ij
3. Compute per-dimension agreement: P_i = (1/(k(k-1))) · (Σⱼ n_ij² - k)
4. Compute overall observed agreement: P̄ = (1/n) · Σᵢ P_i
5. Compute expected agreement: P̄_e = Σⱼ p_j²
6. Fleiss' kappa: κ = (P̄ - P̄_e) / (1 - P̄_e)

### 4.5.3 Relationship to Cohen's Kappa

For k = 2, Fleiss' kappa reduces to Scott's pi (not Cohen's kappa — the difference is in the expected agreement computation). Fleiss' kappa assumes random rater assignment per subject; Cohen's assumes fixed raters. For the evaluative authority, where the same panel evaluates all dimensions, both are computed for complementary perspectives.

## 4.6 Consensus Computation

### 4.6.1 Method Selection

The evaluative authority uses **median** as its consensus method. The choice between mean, median, and trimmed mean is a governance decision with institutional implications (see Document D, Section 4.1):

- **Mean**: Sensitive to outliers. A single extreme score shifts the consensus.
- **Median**: Robust to outliers. The majority perspective prevails.
- **Trimmed mean**: Intermediate. Requires defining "outlier" — a secondary governance decision.

Median is the default because it embodies the governance principle: *the majority evaluative perspective should prevail, but minority perspectives should be recorded and investigated, not averaged away*.

### 4.6.2 Procedure

For each dimension d:

1. Collect all rater scores: S_d = {s_d1, s_d2, ..., s_dk}
2. Sort S_d
3. If k is odd: consensus = S_d[(k+1)/2]
4. If k is even: consensus = (S_d[k/2] + S_d[k/2 + 1]) / 2
5. Compute Q1, Q3, IQR = Q3 - Q1
6. Define outlier bounds: [Q1 - f·IQR, Q3 + f·IQR] where f is the configurable outlier threshold (default 1.5)
7. Flag any score outside the bounds as an outlier
8. Record: {consensus, median, q1, q3, iqr, outliers: [...]}

### 4.6.3 Outlier Policy

Flagged outliers are:
- **Recorded** in the consensus output (with rater ID)
- **Preserved** in the archive (for longitudinal analysis)
- **Not removed** from the consensus computation (median is already robust)
- **Flagged** for human review if they recur across 3+ consecutive assessments (indicating a persistent perspective gap, not a one-time anomaly)

### 4.6.4 Composite Score

The weighted composite is computed over all dimensions (both objective and subjective):

```
Composite = Σ_d (weight_d × consensus_d)
```

where weight_d is the dimension's rubric weight and consensus_d is:
- For objective dimensions: the automated collector's score (deterministic)
- For subjective dimensions: the panel's median score

## 4.7 The Re-Rate Protocol

### 4.7.1 Trigger

If overall ICC (computed over subjective dimensions only) falls below the re-rate threshold (configurable, default 0.61 — lower bound of "substantial" agreement):

- The assessment is flagged as **governance crisis**
- The composite score is computed but marked as **unreliable**
- The re-rate investigation protocol is triggered

### 4.7.2 Investigation Steps

1. **Per-dimension ICC**: Compute ICC for each subjective dimension individually. Identify which dimension(s) drive the low overall ICC.
2. **Pairwise kappa inspection**: Examine all (k choose 2) pairwise kappas. Identify which rater pair(s) disagree most.
3. **Evidence review**: Check whether the evidence assembly was complete for the low-agreement dimension. Incomplete evidence → fix evidence pipeline and re-rate.
4. **Scoring guide review**: Check whether the scoring guide for the low-agreement dimension is ambiguous. Ambiguity → revise guide and re-rate.
5. **Persona conflict check**: Determine whether two personas have contradictory biases that produce irreconcilable scores on this dimension. Contradiction → either reconcile biases, split the dimension, or accept disagreement as inherent and lower the threshold for that dimension.
6. **Escalation**: If steps 1-5 do not resolve the crisis, escalate to human operator (System 5) for judgment.

## 4.8 Validity Framework

### 4.8.1 Construct Validity

Do the rubric dimensions measure "system quality"? Established by grounding dimensions in McCall et al. (1977) and ISO/IEC 25010:2023 where mappings exist, and by operational justification for domain-specific dimensions. Future work: convergent validity against expert human ratings.

### 4.8.2 Content Validity

Do the dimensions cover the relevant quality space? Established iteratively through operational experience: dimensions are added when quality gaps are discovered (e.g., claim_provenance added in v1.1 after unsourced claims were identified). Content validity improves over time as operational experience accumulates.

### 4.8.3 Criterion Validity

Do high scores predict good outcomes? Requires longitudinal outcome data: systems that score higher should exhibit fewer defects, higher acceptance rates, and lower maintenance costs. Preliminary: the threshold calibration crisis (Chapter 6) was detected by the authority before it caused operational failure, suggesting predictive utility.

### 4.8.4 Internal Consistency

Cronbach's alpha across dimensions would measure whether dimensions covary as expected. Computed separately for subjective dimensions (excluding zero-variance objective dimensions that would inflate alpha). Not yet reported pending sufficient longitudinal assessment data.

## 4.9 Summary

The statistical apparatus comprises three agreement measures (ICC(2,1), Cohen's κ, Fleiss' κ), a consensus mechanism (median with IQR outlier detection), a composite scoring procedure (weighted sum over objective collectors + subjective consensus), and a re-rate protocol triggered by ICC below threshold. All methods are implemented in pure Python standard library, are mathematically specified to implementation level, and are interpretable via configurable benchmark frameworks. The apparatus is domain-agnostic — the same computations apply regardless of what the rubric dimensions measure or who the raters are.
