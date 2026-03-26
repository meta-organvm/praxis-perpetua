---
status: reference-activated
---
# Adventure 7: Measurement Theory

## Central Question

What makes a measurement valid, and how does this apply to automated assessment?

This adventure traces a line from the philosophical foundations of measurement -- what does it mean to assign a number to an attribute? -- through the psychometric machinery that validates tests and scales, and into the territory where automated systems (AI graders, code quality scores, promotion gates) attempt to measure things that resist easy quantification. The core tension: measurement theory was built for human judges measuring human traits. What breaks when the judge becomes a machine?

---

## Seed Articles

### Scale (social sciences)
Scaling is the process of measuring or ordering entities with respect to quantitative attributes or traits. It covers everything from estimating individuals' levels of extraversion to the perceived quality of products. Some techniques permit estimation of magnitudes on a continuum; others provide only for relative ordering. The critical distinction: a *scale* (an instrument emerging from collective responses to multiple items) is not the same as an *index* (a composite measure), though the terms are frequently conflated.

**Connection:** Every automated scoring system implicitly constructs a scale. The question is whether that scale has the properties needed for the inferences drawn from it.

### Sorting
Ordering data by some criterion, or categorizing items with similar properties. Ordering is the combination of categorizing based on equivalent order and then ordering the categories. A deceptively simple concept that becomes the foundation of all measurement: before you can measure, you must be able to sort.

**Connection:** Sorting is the pre-measurement operation. Academic grading, code quality tiers, and promotion state machines all begin with sorting -- but whether the sorting reflects a valid underlying dimension is the deeper question.

### Academic Grading in the United States
The familiar A-through-F system, typically five to seven letter grades. Numeric-to-letter conversions vary across systems and disciplines. The system is so pervasive that its arbitrariness becomes invisible: why five grades? Why not seven? Why letter buckets at all?

**Connection:** Grading is measurement in its most institutionalized form. The gap between a student's "true" ability and their letter grade is exactly the measurement error that psychometrics was built to understand.

### Test Validity (2 visits, Validation process section)
The extent to which a test accurately measures what it is supposed to measure. Classical models divided validity into content, criterion, and construct varieties; the modern (Messick-era) view treats validity as a *single unitary construct* -- a unified evaluative judgment about the adequacy and appropriateness of inferences drawn from test scores. Validity is not a property of the test itself but of the *interpretation* of its scores for a specific purpose.

Key insight: reliability (consistency) is necessary but not sufficient for validity. A perfectly consistent measure can consistently measure the wrong thing.

**Connection:** This is the theoretical center of the entire adventure. Every automated metric is a test; every threshold or gate is an interpretation. The validity question applies to all of them.

### Model Context Protocol
An open standard introduced by Anthropic (November 2024) for standardizing how AI systems integrate with external tools, systems, and data sources. Provides a universal interface for reading files, executing functions, and handling contextual prompts. Adopted by OpenAI and Google DeepMind.

**Connection:** MCP is infrastructure for automated systems that *consume* measurements. When an AI agent reads a code quality score or a repo readiness metric through MCP, the validity of that measurement determines whether the agent's downstream actions are well-founded.

---

## Expansion Articles

### Psychometrics
The field concerned with the theory and technique of psychological measurement. Focuses on the objective measurement of *latent constructs* -- things that cannot be directly observed (intelligence, personality traits, educational achievement). Individual levels on these unobservable variables are inferred through mathematical modeling based on observed responses to test items. The field houses two major theoretical traditions: classical test theory and item response theory.

### Item Response Theory (IRT)
A paradigm for test design, analysis, and scoring based on the relationship between individual performance on a test item and the test taker's level of the underlying ability. Unlike classical test theory, IRT does *not* assume all items are equally difficult. Each item has its own characteristic curve described by parameters: difficulty (location), discrimination (slope), and pseudo-guessing (lower asymptote). IRT is the preferred method for high-stakes assessments (GRE, GMAT) precisely because it handles differential item difficulty.

### Classical Test Theory (CTT)
The foundational framework: observed score = true score + error. The aim is to understand and improve reliability. CTT is "classical" both chronologically and in contrast to IRT's "modern" approach. Its simplicity is both its strength (easy to apply) and its limitation (assumes all items are equivalent replications of each other).

### Rasch Model
A psychometric model for analyzing categorical data as a function of the trade-off between respondent ability and item difficulty. A special case of IRT mathematically, but philosophically distinct: Rasch proponents insist on *specific objectivity* -- the requirement that item comparisons be independent of the sample of respondents and vice versa. This makes the Rasch model a prescriptive standard for what measurement *should* look like, not just a descriptive model of data.

### Construct Validity
How well a set of indicators represents a concept that is not directly measurable. Modern validity theory defines construct validity as the *overarching* concern, subsuming content and criterion validity. Messick's unified view: "an integrated evaluative judgment of the degree to which empirical evidence and theoretical rationales support the adequacy and appropriateness of inferences and actions based on test scores." Borsboom et al. (2004) counter with a more empiricist definition emphasizing statistical and causal reasoning.

### Content Validity
The extent to which a measure represents *all facets* of a given construct. A depression scale that only measures affect but ignores behavior lacks content validity. Inherently subjective -- requires agreement on what the construct actually encompasses.

### Criterion Validity
The extent to which a test relates to or predicts a theoretically related behavior or outcome. Splits into concurrent validity (measured at the same time as the criterion) and predictive validity (measured before the criterion). Assessed by comparison with a "gold standard" test.

### Reliability (statistics)
The overall consistency of a measure. Produces similar results under consistent conditions. Expressed as coefficients from 0.00 (much error) to 1.00 (no error). A prerequisite of validity but not a guarantee of it.

### Inter-rater Reliability
The degree of agreement among independent observers rating the same phenomenon. Assessment tools that rely on ratings *must* exhibit good inter-rater reliability, otherwise they are not valid. Measured by Cohen's kappa, Fleiss' kappa, intraclass correlation, Krippendorff's alpha, and others.

### Measurement Invariance
A statistical property indicating that the same construct is being measured across specified groups. Tested via multiple-group confirmatory factor analysis. Violations preclude meaningful cross-group comparisons. If your measurement isn't invariant across groups, you may not be measuring the same thing for different populations.

### Rubric (academic)
A scoring guide containing evaluative criteria, quality definitions for levels of achievement, and a scoring strategy. Serves both as a grading tool and a planning tool. The operational bridge between abstract constructs ("writing quality") and concrete assessments.

### Likert Scale
The most widely used approach to scaling survey responses. Respondents indicate agreement/disagreement on a symmetric scale. Assumes equal distances between choices. Items are expected to be highly correlated (high internal consistency) while collectively capturing the full domain. IRT treats item difficulty as information to incorporate; Likert scaling assumes items are parallel instruments.

### Thurstone Scale
The first formal technique for measuring attitudes (1928). Statements about an issue are pre-rated by judges for favorability; respondents endorse statements they agree with; scores are averaged. The key innovation: the scale values are established *before* administration, by a separate panel.

### Guttman Scale
A unidimensional ordinal scale from which original observations can be reproduced. Not limited to dichotomous variables. A hypothesis about data structure: if the scale holds, a person who endorses a "harder" item must endorse all "easier" items. The discovery of a Guttman scale depends on data conforming to a particular cumulative structure.

### Representational Theory of Measurement / Theory of Conjoint Measurement
A formal theory of continuous quantity (Debreu 1960; Luce & Tukey 1964). Addresses situations where at least two natural attributes non-interactively relate to a third. Establishes that psychological attributes *can* in principle be quantified like physical quantities. The Rasch model has been argued (controversially) to be a stochastic variant of conjoint measurement. Limited practical application due to high mathematical complexity and difficulty handling noisy empirical data.

### Operational Definition
A concrete, replicable procedure designed to represent a construct. Stevens (1935): "An operation is the performance which we execute in order to make known a concept." The bridge between the abstract (the construct) and the observable (the measurement procedure).

### Latent Variable
A variable that can only be inferred indirectly through a mathematical model from observable variables. Used across disciplines from psychology to machine learning. Latent variables reduce data dimensionality -- many observables can be aggregated to represent an underlying concept. They serve a function analogous to scientific theories: making the unobservable tractable.

### Factor Analysis
A statistical method describing variability among observed, correlated variables in terms of fewer unobserved factors. Factor loadings indicate how strongly each variable relates to each factor. Commonly used in psychometrics to identify the latent structure underlying a set of test items.

### Structural Equation Modeling (SEM)
A family of methods for testing hypotheses about causal relationships among latent and observed variables. Subsumes confirmatory factor analysis, path analysis, and multi-group modeling. Allows simultaneous estimation of all model coefficients using all available information. The primary tool for testing measurement invariance and validating the factor structure of assessment instruments.

### Automated Essay Scoring (AES)
Computer programs that assign grades to essays. A classification problem: map textual entities to discrete grade categories. Driven by cost pressure, accountability demands, and NLP advances. Significant backlash: opponents argue computers cannot grade writing accurately and that AES promotes teaching to the test. The validity question is acute here -- does the automated score reflect the same construct as a human-assigned score?

---

## The Validity Framework

Validity is not a property of a test. It is a property of the *inferences drawn from test scores for a specific purpose*. This distinction is the most important idea in measurement theory.

### The Classical Trinity (and its unification)

The classical model identified three "types" of validity:

1. **Content validity** -- Does the test sample the full domain of the construct? A code quality metric that only checks line count and ignores logic correctness, security, or maintainability lacks content validity. Establishing content validity requires agreement on what the construct encompasses -- which means you need a theory of the construct first.

2. **Criterion validity** -- Does the test predict or correlate with an external criterion? Subdivides into:
   - *Concurrent validity*: Does the score correlate with a current gold-standard measure?
   - *Predictive validity*: Does the score predict a future outcome?
   A repo readiness score has predictive validity if repos that score higher actually succeed more often after promotion to production.

3. **Construct validity** -- Does the test measure the theoretical construct it claims to measure? This is the deepest form. It requires:
   - *Convergent validity*: The measure correlates with other measures of the same construct.
   - *Discriminant validity*: The measure does NOT correlate with measures of different constructs.
   - A *nomological network*: The measure behaves as theory predicts it should within a web of related constructs.

The modern (Messick 1989) unification treats construct validity as the master concept. Content and criterion evidence are *types of evidence* supporting construct validity, not separate "validities." This matters because it prevents cherry-picking: you cannot claim a test is "content valid" and stop there. You must demonstrate that the *inferences* drawn from scores are justified across all relevant evidence types.

### The Reliability-Validity Relationship

Reliability is necessary but not sufficient. A speedometer that always reads 10 mph too high is perfectly reliable but not valid for measuring speed. The formula: validity <= sqrt(reliability). This sets a ceiling: an unreliable test *cannot* be valid.

### Measurement Invariance as a Validity Constraint

If a measure means different things to different groups, it cannot support valid cross-group inferences. Testing measurement invariance via multi-group CFA is increasingly standard. Levels of invariance:
- **Configural**: Same factor structure across groups
- **Metric**: Same factor loadings across groups
- **Scalar**: Same intercepts across groups (required for mean comparisons)
- **Strict**: Same residual variances across groups

For automated systems, the "groups" might be programming languages, project sizes, team configurations, or time periods.

---

## Classical vs. Modern Test Theory

### Classical Test Theory (CTT)

**Core model:** X = T + E (observed = true + error)

**Assumptions:**
- The expected value of error is zero
- Error is uncorrelated with true score
- Errors on different tests are uncorrelated

**Strengths:**
- Mathematically simple
- Easy to compute reliability (Cronbach's alpha, split-half)
- Minimal sample size requirements
- Works well for homogeneous item sets

**Limitations:**
- Item and person parameters are *sample-dependent* -- item difficulty depends on who takes the test
- Assumes all items are parallel (equally difficult, equally discriminating)
- Reliability is a property of the test as a whole, not individual items
- Cannot handle adaptive testing

**Software analogy:** Measuring code quality by averaging all metric subscores equally, regardless of whether some metrics are harder to achieve than others.

### Item Response Theory (IRT)

**Core model:** P(correct | theta, b, a, c) = c + (1-c) / (1 + exp(-a(theta - b)))

Where theta = ability, b = difficulty, a = discrimination, c = pseudo-guessing.

**Assumptions:**
- Unidimensionality (one latent trait dominates)
- Local independence (responses to different items are independent given theta)
- The item characteristic curve (ICC) follows a specific mathematical function

**Strengths:**
- Item parameters are *sample-independent* (given model fit)
- Person parameters are *item-independent* (given model fit)
- Enables adaptive testing (select items based on estimated ability)
- Provides item-level information (where on the ability scale each item is most informative)
- Can detect differential item functioning (bias)

**Limitations:**
- Requires larger samples (typically 200+ for 2PL, 500+ for 3PL)
- Assumes a parametric form for the ICC
- Unidimensionality assumption is often violated in practice
- More complex to implement and interpret

**Software analogy:** Weighting code quality checks by their difficulty and informativeness. A repo that passes a hard check (e.g., comprehensive integration test coverage) provides more evidence of quality than one passing an easy check (e.g., has a README).

### The Rasch Model as a Middle Path

The Rasch model is mathematically a 1-parameter IRT model (only difficulty varies), but its proponents treat it as a *prescriptive* standard rather than a descriptive model. The Rasch philosophy: if data don't fit the model, the *items* need revision, not the model. This implies specific objectivity -- the comparison of any two persons should be independent of which items they respond to, and vice versa.

**Software analogy:** Insisting that a promotion rubric be calibrated so that the relative readiness of any two repos can be assessed regardless of which specific criteria are evaluated. If a criterion fails to discriminate consistently, it should be redesigned or dropped.

---

## Scale Construction

### How to Build a Valid Measurement Instrument

The choice of scaling method embeds assumptions about the construct being measured.

### Likert Scales (Summative)

**Method:** Present a set of statements; respondents rate agreement on a symmetric scale (e.g., 1-5). Sum or average the ratings.

**Assumption:** Equal intervals between response categories. All items are parallel replications.

**Best for:** Measuring attitudes, opinions, or satisfaction where the construct is relatively homogeneous.

**Weakness:** The equal-interval assumption is often violated. Averaging ordinal data as if it were interval data is statistically questionable.

**Software application:** A developer satisfaction survey. A rubric where reviewers rate each dimension 1-5. The typical PR review checklist.

### Thurstone Scales (Equal-Appearing Intervals)

**Method:** A panel of judges pre-rates statements for favorability. Statements with high judge agreement and even spacing are selected. Respondents endorse statements they agree with. Score = average of endorsed statement values.

**Advantage:** Scale values are established by expert consensus before administration.

**Weakness:** Time-consuming to construct. Judge panel may not be representative.

**Software application:** Expert-calibrated code quality standards, where a panel of senior engineers rates the severity/importance of different quality indicators before those indicators are used to score repos.

### Guttman Scales (Cumulative)

**Method:** Items form a cumulative hierarchy. Endorsing a "harder" item implies endorsement of all "easier" items.

**Advantage:** If the scale holds, the total score perfectly reproduces the response pattern. Powerful test of unidimensionality.

**Weakness:** Rarely achieved in practice. Real data usually only approximate the Guttman pattern.

**Software application:** Promotion state machines (LOCAL -> CANDIDATE -> PUBLIC -> GRADUATED -> ARCHIVED). The assumption is cumulative: a GRADUATED repo has passed all criteria required for CANDIDATE and PUBLIC. If this is violated -- if a GRADUATED repo lacks something a CANDIDATE has -- the "scale" is broken.

### Rasch Measurement

**Method:** Model the probability of a response as a function of person ability minus item difficulty. Estimate both on the same interval scale.

**Advantage:** Specific objectivity. Item-free person measurement. Person-free item calibration.

**Weakness:** Strict assumptions. Data must fit the model, or items must be revised.

**Software application:** Calibrating assessment criteria so that the relative readiness of repos is comparable regardless of which specific criteria are evaluated. The most rigorous approach to building a promotion rubric.

---

## Automated Assessment

### What Measurement Theory Says About Machine Scoring

Automated essay scoring (AES) is the most studied case, and its lessons generalize to any automated assessment system.

### The Core Validity Challenge

AES systems are typically validated by comparing machine scores to human scores. If the correlation is high, the system is declared "valid." But this conflates criterion validity (correlation with an external standard) with construct validity (does the machine measure the same thing a human measures?).

**The construct problem:** An AES system might achieve high agreement with human raters by exploiting surface features (essay length, vocabulary sophistication, sentence complexity) that correlate with quality but are not themselves the construct "writing quality." A student who games these features can score well without actually writing well. The system measures a *proxy*, not the *construct*.

This is the fundamental challenge for all automated assessment: correlation with human judgment is necessary but not sufficient. You must also show that the automated system is sensitive to the same *reasons* that drive human judgment.

### Inter-rater Reliability as a Benchmark

The standard benchmark for AES: does the machine agree with humans as well as humans agree with each other? This sets a reasonable ceiling -- you cannot demand the machine be more consistent than expert humans. But inter-rater reliability only addresses *consistency*, not *validity*. Two raters can consistently agree while both measuring the wrong thing.

### Measurement Invariance in Automated Systems

Does the automated system measure the same construct for different populations? An AES system trained on essays by native English speakers may not measure writing quality invariantly for ESL students. A code quality metric calibrated on web applications may not transfer to embedded systems.

Differential item functioning (DIF) from IRT provides a formal framework: if an item (or in this case, a scoring criterion) functions differently for different groups *after controlling for ability*, that criterion is biased.

### The Operational Definition Problem

For automated systems, the operational definition *is* the algorithm. When you define "code quality" as the output of a linting tool plus test coverage plus cyclomatic complexity, that operationalization becomes the construct. If the operationalization is incomplete -- if it misses dimensions of quality that matter -- no amount of reliability improvement will fix the validity problem.

---

## Implications for Software Quality Metrics

### Applying Psychometric Validity to Code Quality Scores, Repo Readiness, and Promotion Gates

This is where measurement theory meets the ORGANVM system directly.

### Your Promotion State Machine Is a Guttman Scale

The promotion chain LOCAL -> CANDIDATE -> PUBLIC_PROCESS -> GRADUATED -> ARCHIVED assumes cumulative attainment. A GRADUATED repo should possess everything a CANDIDATE has, plus more. If this cumulative structure is violated in practice, the scale is invalid -- the "score" (promotion state) does not reliably indicate the underlying construct (repo maturity).

**Test:** For each pair of adjacent states, verify that repos in the higher state consistently exhibit the properties required at the lower state. Any violations indicate the scale needs recalibration.

### seed.yaml as Operational Definition

Each repo's `seed.yaml` operationalizes membership, tier, and status. The operational definition determines what is measured and what is not. If seed.yaml omits a dimension of repo maturity that matters (e.g., documentation quality, dependency health, user adoption), then the promotion system has a content validity gap.

### Code Quality Metrics Are Latent Variable Models

When you compute a "quality score" from multiple metrics (test coverage, linting results, type safety, build stability), you are implicitly positing a latent variable -- "code quality" -- that manifests through these observable indicators. Factor analysis can tell you whether these indicators actually load onto a single factor, or whether "code quality" is really multiple distinct constructs (reliability, maintainability, security, performance) that should not be collapsed into one score.

### Measurement Invariance Across Organs

If the same quality metrics are applied across organs with different technological profiles (Python CLI tools in ORGAN-I vs. TypeScript web apps in ORGAN-III vs. orchestration infrastructure in ORGAN-IV), measurement invariance must be tested. A test coverage threshold of 80% may represent different levels of diligence depending on the technology stack, codebase architecture, and testing conventions.

### The Construct Validity Test for Any Automated Metric

For any automated assessment in the system, ask:

1. **Content validity:** Does the metric sample the full domain of the construct? What aspects of "quality" or "readiness" does it miss?

2. **Criterion validity:** Does the metric predict outcomes that matter? Do repos with higher scores actually deploy more successfully, have fewer bugs in production, or receive better reviews?

3. **Construct validity (convergent):** Does the metric correlate with other measures of the same thing? Does a high code quality score correlate with positive peer review assessments?

4. **Construct validity (discriminant):** Does the metric discriminate from different constructs? A code quality score should not correlate too highly with repo age or team size -- those are different constructs.

5. **Measurement invariance:** Does the metric mean the same thing across different contexts (organs, tech stacks, project sizes)?

6. **Reliability:** Does the metric produce consistent results? If you run the same analysis twice on the same codebase, do you get the same score? (For automated tools this is usually trivially satisfied, which is why validity -- not reliability -- is the harder problem.)

### The Inter-rater Problem for AI Judges

When an AI system (e.g., an LLM-based code reviewer) provides assessments, inter-rater reliability takes on new meaning. The "raters" are model runs that may vary due to temperature, prompt variation, or context window contents. Establishing that the AI reviewer produces consistent, valid assessments requires the same psychometric rigor as establishing that human raters agree.

---

## Conceptual Map

```
MEASUREMENT THEORY
|
+-- Foundations
|   +-- Levels of measurement (Stevens: nominal/ordinal/interval/ratio)
|   +-- Operational definition (construct -> observable procedure)
|   +-- Representational theory / conjoint measurement (Luce & Tukey)
|   +-- Latent variables (unobserved constructs inferred from observables)
|
+-- Classical Test Theory
|   +-- X = T + E
|   +-- Reliability (Cronbach's alpha, split-half)
|   +-- Standard error of measurement
|   +-- Spearman-Brown prophecy formula
|
+-- Item Response Theory
|   +-- 1PL / Rasch model (difficulty only)
|   +-- 2PL (difficulty + discrimination)
|   +-- 3PL (+ pseudo-guessing)
|   +-- Item characteristic curves
|   +-- Item information functions
|   +-- Differential item functioning
|   +-- Computerized adaptive testing
|
+-- Scale Construction
|   +-- Likert (summative, equal intervals assumed)
|   +-- Thurstone (equal-appearing intervals, judge-calibrated)
|   +-- Guttman (cumulative, hierarchical)
|   +-- Rasch (prescriptive measurement model)
|
+-- Validity Framework (unified, Messick 1989)
|   +-- Content evidence (domain sampling)
|   +-- Criterion evidence (concurrent / predictive)
|   +-- Construct evidence
|   |   +-- Convergent validity
|   |   +-- Discriminant validity
|   |   +-- Nomological network
|   |   +-- Factor structure
|   +-- Measurement invariance (configural / metric / scalar / strict)
|   +-- Consequential validity (social consequences of score use)
|
+-- Statistical Infrastructure
|   +-- Factor analysis (exploratory / confirmatory)
|   +-- Structural equation modeling
|   +-- Multi-group CFA
|   +-- Inter-rater reliability (Cohen's kappa, ICC, Krippendorff's alpha)
|
+-- Applied Domains
    +-- Educational testing (SAT, GRE, GMAT)
    +-- Automated essay scoring
    +-- Computational psychometrics
    +-- Software quality metrics  <-- THIS IS WHERE YOU ARE
    +-- AI-based assessment systems
```

---

## Open Questions

1. **Can software quality be validly measured as a single latent variable?** Factor analysis of common code metrics (coverage, complexity, lint violations, build stability, dependency freshness) might reveal multiple distinct factors. If so, collapsing them into a single "quality score" is a construct validity violation.

2. **What is the "gold standard" for repo readiness?** Criterion validity requires a criterion. Is it production success rate? Time-to-incident? User/developer satisfaction? The choice of criterion shapes what the metric optimizes for.

3. **Does the Rasch model's specific objectivity requirement apply to promotion rubrics?** If the relative readiness of two repos depends on *which* criteria you happen to evaluate, the rubric lacks the measurement properties the Rasch tradition demands.

4. **How do you establish measurement invariance for code quality across programming languages?** The same metric (e.g., test coverage) may have different psychometric properties in Python vs. TypeScript vs. Rust. Formal invariance testing is needed.

5. **What is the consequential validity of automated assessment?** Messick included the social consequences of score use as part of validity. If automated metrics cause teams to optimize for the metric rather than the construct (Goodhart's Law / Campbell's Law), the measurement system is self-undermining.

6. **Can IRT-based adaptive assessment be applied to repos?** Instead of a fixed rubric, evaluate repos with criteria selected based on estimated maturity -- harder criteria for repos that pass easy ones. This would reduce evaluation burden while maintaining measurement precision.

7. **What does inter-rater reliability look like for LLM-based code reviewers?** Temperature, prompt engineering, and context window contents all introduce variance. Is this variance random error (reliability problem) or systematic bias (validity problem)?

8. **Is the ORGANVM promotion state machine empirically cumulative?** The Guttman model predicts that passing higher-state criteria implies passing all lower-state criteria. This is testable with existing repo data.

---

## Frontier Articles

These articles appeared in the link graphs of Psychometrics and Construct validity and represent natural next-step reading:

- **Computational psychometrics** -- The direct bridge between psychometrics and AI/ML assessment systems
- **Standards for Educational and Psychological Testing** -- "The Bible" of testing industry professionals; operational best practices
- **Nomological network** -- The formal framework for construct validity evidence
- **Convergent validity / Discriminant validity** -- The twin requirements for construct evidence
- **Multitrait-multimethod matrix** -- Campbell & Fiske's method for simultaneous convergent/discriminant assessment
- **Levels of measurement** -- Stevens' nominal/ordinal/interval/ratio framework; foundational for understanding what operations are legitimate on what kinds of data
- **Theory of conjoint measurement** -- The formal mathematical foundation for psychological measurement as true quantity
- **Differential item functioning** -- How to detect when an item (or criterion) is biased across groups
- **Computerized adaptive testing** -- The applied consequence of IRT: tests that adapt in real time to the test-taker
- **Cronbach's alpha** -- The workhorse reliability coefficient; its assumptions and limitations
- **Spearman-Brown prediction formula** -- How reliability changes as you add items (or criteria)
- **Jingle-jangle fallacies** -- When different names refer to the same construct (jangle) or the same name refers to different constructs (jingle)
- **Campbell's Law** -- "The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures"
- **Goodhart's Law** -- "When a measure becomes a target, it ceases to be a good measure"

---

## Sources

All summaries sourced from English Wikipedia via MCP Wikipedia tools, 2026-03-20.

### Seed Articles
| Article | Wikipedia Title |
|---------|---------------|
| Scale (social sciences) | Scale (social sciences) |
| Sorting | Sorting |
| Academic grading in the US | Academic grading in the United States |
| Test validity | Test validity |
| Model Context Protocol | Model Context Protocol |

### Expansion Articles
| Article | Wikipedia Title |
|---------|---------------|
| Psychometrics | Psychometrics |
| Item response theory | Item response theory |
| Classical test theory | Classical test theory |
| Rasch model | Rasch model |
| Construct validity | Construct validity |
| Content validity | Content validity |
| Criterion validity | Criterion validity |
| Reliability | Reliability (statistics) |
| Inter-rater reliability | Inter-rater reliability |
| Measurement invariance | Measurement invariance |
| Rubric | Rubric (academic) |
| Likert scale | Likert scale |
| Thurstone scale | Thurstone scale |
| Guttman scale | Guttman scale |
| Conjoint measurement | Theory of conjoint measurement |
| Operational definition | Operational definition |
| Latent variable | Latent variable |
| Factor analysis | Factor analysis |
| Structural equation modeling | Structural equation modeling |
| Automated essay scoring | Automated essay scoring |

### Additional Articles (from link graph exploration)
| Article | Wikipedia Title |
|---------|---------------|
| Nomological network | Nomological network |
| Convergent validity | Convergent validity |
| Levels of measurement | Levels of measurement |
| Computational psychometrics | Computational psychometrics |
| Standards for testing | Standards for Educational and Psychological Testing |

### Query-Targeted Summaries
Focused summaries were generated for the query "validity of automated measurement and assessment systems" for: Test validity, Psychometrics, Construct validity, Item response theory, Automated essay scoring, Rasch model, Measurement invariance, Rubric (academic), Reliability (statistics), Inter-rater reliability.

### Link Graphs Explored
- Psychometrics (500+ outgoing links)
- Construct validity (54 outgoing links)
