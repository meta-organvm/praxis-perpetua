---
sgo_id: SGO-2026-RP-007
title: "Measuring the Unmeasurable"
tier: Thesis
status: LOCAL (first draft)
target_venues: [Empirical Software Engineering, J. Systems and Software, arXiv cs.SE]
dependencies: [RP-02, RP-03]
date: 2026-03-21
---

# Measuring the Unmeasurable: Psychometric Validity Theory Applied to Automated Software Governance

---

## 1. Introduction

The software industry measures everything and validates nothing. Continuous integration pipelines compute code coverage percentages, linting tools count style violations, complexity analyzers assign numerical scores, and promotion gates aggregate these signals into composite readiness indicators that determine whether a software artifact advances through its lifecycle. These measurement activities are pervasive, consequential, and almost entirely unexamined through the lens of measurement theory. The numbers are produced with extraordinary precision and consumed with extraordinary credulity. No one asks whether the ruler is valid.

This silence is remarkable when contrasted with the maturity of measurement theory in adjacent fields. Psychometrics -- the science of psychological measurement -- has spent more than a century developing rigorous frameworks for answering a deceptively simple question: does a given measurement procedure actually measure what it claims to measure? From Spearman's (1904) formulation of classical test theory through Messick's (1989) unified validity framework to contemporary applications of item response theory in high-stakes educational assessment, the psychometric tradition has built an elaborate and empirically tested apparatus for evaluating the quality of measurements. This apparatus distinguishes between reliability (consistency) and validity (accuracy of inference), identifies multiple forms of validity evidence (content, criterion, construct), and provides formal statistical methods -- factor analysis, structural equation modeling, differential item functioning analysis -- for testing whether measurement instruments possess the properties their users assume they possess.

Software engineering has developed nothing comparable. The field has produced hundreds of metrics but no systematic theory of what makes a metric valid. Lines of code, cyclomatic complexity, code coverage, dependency counts, code smell frequencies, build stability indices -- each is proposed, adopted, and operationalized without the foundational work that psychometrics demands before a measurement instrument is trusted. The metric is the operational definition, the operational definition is the construct, and the construct is whatever the metric happens to capture. The circularity is complete, and it is invisible precisely because no one applies the vocabulary that would make it visible.

The consequences of this omission are not merely theoretical. When automated governance systems use composite quality scores to determine whether software artifacts may advance through promotion pipelines -- from local development to candidate status to public availability to graduated production readiness -- those scores function as high-stakes assessments. They determine resource allocation, deployment sequencing, and organizational attention. If the scores lack construct validity -- if they measure a proxy for quality rather than quality itself, or if they collapse multiple distinct constructs into a single number, or if they mean different things when applied to different technology stacks -- then the governance system built upon them is making consequential decisions on the basis of measurements whose inferential foundations have never been examined.

This thesis addresses three research questions that together constitute a program for applying psychometric validity theory to automated software governance:

**RQ1.** Can software quality be validly measured as a single latent variable, or does factor analysis of common code metrics (coverage, complexity, lint violations, build stability, dependency freshness) reveal multiple distinct constructs that should not be collapsed into a single score?

**RQ2.** Does the ORGANVM promotion state machine (LOCAL to CANDIDATE to PUBLIC_PROCESS to GRADUATED) empirically satisfy Guttman scale properties -- specifically, the assumption of cumulative attainment -- and what do violations reveal about the construct validity of the promotion construct?

**RQ3.** How should measurement invariance be established for code quality metrics applied across programming languages, technology stacks, and project types, and what psychometric methods (multi-group confirmatory factor analysis, differential item functioning analysis) are appropriate for this purpose?

The central thesis is straightforward: software quality assessment needs psychometric discipline. The tools exist. The theory is mature. The gap is one of application, not invention. What follows is an attempt to bridge that gap by importing the full machinery of psychometric validity theory into the domain of automated software governance, using the ORGANVM multi-organ software system as a concrete case study for demonstrating both the theoretical framework and its practical implications.

The structure of the argument proceeds as follows. Section 2 establishes the foundations of measurement theory, covering classical test theory, item response theory, the Rasch model, the unified validity framework, and measurement invariance. Section 3 surveys the current state of software measurement, identifying the validity questions that the field has failed to ask. Section 4 reframes software governance as a measurement instrument, analyzing promotion state machines as Guttman scales, configuration contracts as operational definitions, and automated checks as test items. Section 5 develops the application of item response theory to software governance in detail. Section 6 presents a case study of the ORGANVM promotion pipeline, applying the theoretical framework to a concrete system. Section 7 draws implications for automated governance design. Sections 8 and 9 discuss limitations and conclude.

---

## 2. Foundations of Measurement Theory

Measurement theory addresses a question that appears simple but resists easy answers: what does it mean to assign a number to an attribute? The question becomes especially difficult when the attribute in question is not directly observable -- when it is, in the language of psychometrics, a *latent construct*. Intelligence, depression, educational achievement, writing quality, and software quality all share this property: they are real in the sense that they have observable consequences, but they cannot be placed on a scale or read from a meter. They must be inferred from observable indicators through some form of mathematical modeling.

The psychometric tradition has developed two major theoretical frameworks for this inferential task -- classical test theory and item response theory -- along with a comprehensive validity framework for evaluating whether the inferences drawn from measurements are justified. This section presents each in turn.

### 2.1 Classical Test Theory

Classical test theory (CTT), codified by Novick (1966) and elaborated by Lord and Novick (1968), is the foundational framework for understanding measurement error. Its core model is elegant in its simplicity:

**X = T + E**

where X is the observed score, T is the true score (the score a person would receive if the measurement process were perfectly accurate), and E is the error of measurement. The model is "classical" both chronologically and in contrast to the more recent item response theory, which is sometimes designated the "modern" approach (Allen & Yen, 2002).

The assumptions of CTT are minimal. The expected value of error across repeated measurements is zero: E(E) = 0. Error is uncorrelated with the true score: rho(T, E) = 0. And errors on different measurements are uncorrelated with each other: rho(E_1, E_2) = 0. From these assumptions, a body of theory follows that addresses the central concern of CTT: the reliability of measurements.

Reliability, in the CTT framework, is the proportion of observed score variance attributable to true score variance: r_XX = sigma^2_T / sigma^2_X. It can equivalently be understood as the squared correlation between observed scores and true scores. A perfectly reliable instrument (r_XX = 1.00) contains no measurement error; all variation in observed scores reflects genuine variation in the construct being measured. A perfectly unreliable instrument (r_XX = 0.00) produces scores that are pure noise.

Several methods exist for estimating reliability. Test-retest reliability administers the same instrument on two occasions and correlates the scores. Parallel-forms reliability administers two equivalent versions of the instrument. Internal consistency methods, of which Cronbach's alpha (1951) is the most widely used, estimate reliability from a single administration by examining the correlations among items. The Spearman-Brown prophecy formula predicts how reliability changes as items are added to or removed from an instrument -- a result with direct implications for governance systems, since it tells us how the precision of a composite quality score changes as assessment criteria are added or removed.

CTT also provides the standard error of measurement (SEM), which quantifies the precision of individual scores: SEM = sigma_X * sqrt(1 - r_XX). This statistic defines a confidence interval around any observed score, making explicit that every measurement contains uncertainty. An observed quality score of 85 with an SEM of 5 means the true score lies approximately between 75 and 95 with 95% confidence. Governance systems that treat observed scores as exact values are implicitly assuming an SEM of zero -- an assumption that CTT reveals to be unjustifiable for any finite-reliability instrument.

The strengths of CTT are its mathematical simplicity, its minimal sample size requirements, and its applicability to any set of items that can be scored and summed. Its limitations are equally clear. Item parameters (difficulty, discrimination) and person parameters (true scores) are *sample-dependent*: the estimated difficulty of an item depends on who takes the test, and the estimated ability of a person depends on which items they encounter. CTT assumes that all items are essentially parallel -- equally difficult and equally discriminating -- which is rarely true in practice. And reliability is a property of the test as a whole, not of individual items, which means CTT cannot tell us which specific items contribute most to measurement precision.

In the software measurement context, CTT corresponds to the common practice of computing a quality score by averaging or summing multiple metric subscores, weighting them equally regardless of their difficulty or informativeness. A repository that achieves 80% code coverage, zero critical lint violations, and a passing build receives the same weight for each metric, even though some of these achievements may be far more difficult -- and far more informative about underlying quality -- than others.

### 2.2 Item Response Theory

Item response theory (IRT) addresses the limitations of CTT by modeling the relationship between individual item performance and the underlying latent trait. Where CTT models test-level behavior (total scores), IRT models item-level behavior (the probability of a correct response to each item as a function of the respondent's ability). This shift from test-level to item-level analysis has profound consequences for measurement precision, test design, and the detection of measurement bias.

The general IRT model specifies the probability of a correct response as a mathematical function of person and item parameters:

**P(X_ij = 1 | theta_j, a_i, b_i, c_i) = c_i + (1 - c_i) / (1 + exp(-a_i(theta_j - b_i)))**

where theta_j is the ability of person j (the latent trait), b_i is the difficulty of item i (the point on the ability scale where the probability of a correct response is 0.5, after adjusting for guessing), a_i is the discrimination of item i (the slope of the item characteristic curve at the point of inflection, indicating how steeply the probability of a correct response changes with ability), and c_i is the pseudo-guessing parameter (the lower asymptote, representing the probability that even the least able person will respond correctly by chance).

This general form is the three-parameter logistic (3PL) model. Simplifications yield the two-parameter (2PL) model (c_i = 0, no guessing) and the one-parameter (1PL) model (c_i = 0, a_i = constant for all items), of which the Rasch model is the most prominent instance.

The item characteristic curve (ICC) is the graphical representation of the IRT model for a single item: a sigmoid function plotting the probability of a correct response against the latent trait. The ICC encodes three kinds of information. Its location on the horizontal axis (determined by b_i) indicates difficulty -- items further to the right require higher ability for a 0.5 probability of success. Its slope at the inflection point (determined by a_i) indicates discrimination -- steeper curves distinguish more sharply between respondents of different abilities. And its lower asymptote (determined by c_i) indicates the guessing floor.

The item information function, derived from the ICC, quantifies how much information a given item provides at each point on the ability scale. An item provides maximal information at the ability level corresponding to its difficulty parameter and provides diminishing information as ability moves away from that level. The test information function -- the sum of all item information functions -- describes the overall precision of the instrument across the ability continuum. This is a major advantage over CTT, which provides only a single reliability estimate for the entire test: IRT reveals exactly where the instrument measures precisely and where it measures poorly.

The assumptions of IRT are more demanding than those of CTT. Unidimensionality requires that a single latent trait dominates responses to all items. Local independence requires that responses to different items are statistically independent after conditioning on the latent trait. And the parametric form of the ICC must hold. When these assumptions are met, IRT offers two properties that CTT cannot: item parameters are *sample-independent* (the estimated difficulty of an item does not depend on the ability distribution of the sample, given adequate model fit) and person parameters are *item-independent* (the estimated ability of a person does not depend on which specific items they encounter, given adequate model fit). These properties are collectively known as *specific objectivity* in the Rasch tradition and are considered essential for genuine measurement.

For software governance, IRT offers a fundamentally different approach to quality assessment. Rather than treating all assessment criteria as interchangeable (the CTT assumption), IRT would model each criterion -- each CI check, each quality gate, each promotion requirement -- as an item with its own difficulty and discrimination parameters. A repository that passes a difficult check (such as comprehensive integration test coverage across multiple environments) provides more evidence of quality than one that passes an easy check (such as the presence of a README file). IRT would weight these contributions accordingly, producing ability estimates (quality scores) that reflect the informational content of each criterion rather than treating all criteria as equal units.

Furthermore, IRT enables adaptive assessment: if a repository passes several easy checks, the system can skip to harder checks, reducing evaluation burden while maintaining or even improving measurement precision. This is the principle underlying computerized adaptive testing (CAT) in educational assessment, where the GRE, GMAT, and other high-stakes examinations select items in real time based on the test-taker's estimated ability. An analogous adaptive governance assessment would evaluate repositories with criteria selected based on estimated maturity, concentrating measurement effort where it provides the most information.

### 2.3 The Validity Framework

If reliability concerns the consistency of measurement, validity concerns its meaning. A measurement can be perfectly reliable -- perfectly consistent across occasions, raters, and contexts -- and still be invalid if it measures the wrong thing. A speedometer that consistently reads ten miles per hour too fast is perfectly reliable but not valid for measuring speed. The foundational insight of validity theory is that reliability is necessary but not sufficient: validity is bounded above by the square root of reliability (r_XV <= sqrt(r_XX)), establishing a ceiling that unreliable measures cannot exceed, but reliability alone cannot guarantee that a measure captures its intended construct.

The history of validity theory is one of progressive unification. The classical model identified three distinct "types" of validity -- content, criterion, and construct -- and treated them as independent evaluative standards. A test could be "content valid" without being "criterion valid," and the assessment of each type proceeded by different methods. Messick's (1989) landmark contribution was to argue that these are not separate validities but rather different *types of evidence* bearing on a single, overarching evaluative judgment: construct validity. In Messick's unified framework, construct validity is "an integrated evaluative judgment of the degree to which empirical evidence and theoretical rationales support the adequacy and appropriateness of inferences and actions based on test scores."

This unification has a critical consequence: it prevents cherry-picking. One cannot claim that a measure is "content valid" and stop there, because content evidence is only one component of the overall validity argument. Nor can one demonstrate high correlation with an external criterion and declare the measure "valid," because criterion evidence alone does not establish that the measure captures the intended construct rather than a correlated proxy. The unified framework demands that all relevant types of evidence be gathered and integrated into a comprehensive validity argument.

**Content validity** addresses the question of domain sampling: does the measurement procedure sample the full domain of the construct? A depression scale that assesses only affective symptoms (sadness, hopelessness) but ignores behavioral symptoms (sleep disturbance, appetite changes, social withdrawal) lacks content validity because it does not represent the full construct of depression. Establishing content validity requires, first, a clear theoretical definition of the construct and its dimensions, and second, a demonstration that the measurement procedure covers those dimensions adequately. Content validity is inherently judgmental -- it requires expert agreement on what the construct encompasses -- which means it cannot be reduced to a statistical test. In software measurement, content validity asks: does the quality metric sample all facets of software quality, or does it systematically omit dimensions that matter (security, usability, maintainability, performance, accessibility)?

**Criterion validity** addresses the question of prediction: does the measurement procedure relate to or predict a theoretically relevant outcome? Criterion validity subdivides into concurrent validity (the measure correlates with a currently available criterion) and predictive validity (the measure predicts a future outcome). It is assessed by comparing the measure under evaluation with a "gold standard" -- an established criterion that is accepted as a valid indicator of the construct. In educational testing, the gold standard for a college admissions test is subsequent academic performance; SAT scores are validated partly by their correlation with first-year grade point averages. In software governance, criterion validity would ask: do repositories with higher quality scores actually deploy more successfully, experience fewer production incidents, receive more favorable peer review assessments, or demonstrate greater longevity? Without criterion validation, a quality score is an internally consistent number with no demonstrated connection to the outcomes it is meant to predict.

**Construct validity** is, in the unified framework, the master concept that subsumes all others. It asks the deepest question: does the measure actually tap into the theoretical construct it claims to measure? Construct validity requires multiple lines of evidence:

*Convergent validity* demands that the measure correlate positively with other measures of the same construct. If an automated code quality score measures the same construct as expert human assessment, the two should be substantially correlated.

*Discriminant validity* demands that the measure *not* correlate with measures of different constructs. A code quality score should not correlate too highly with repository age, team size, or programming language popularity -- those are different constructs, and high correlations would suggest that the quality score is confounded with extraneous variables.

*The nomological network*, introduced by Cronbach and Meehl (1955), is the web of theoretical relationships in which a construct is embedded. A valid measure of software quality should behave as theory predicts: it should correlate positively with developer experience, negatively with defect density, and show no relationship with variables theoretically unrelated to quality. The nomological network provides the interpretive framework within which individual validity coefficients acquire meaning.

*Factor structure* -- examined through exploratory and confirmatory factor analysis -- reveals whether the indicators used to measure a construct actually load onto a single latent factor (supporting unidimensionality) or onto multiple distinct factors (suggesting that what was assumed to be one construct is actually several). This is the empirical test of the latent variable assumption that underlies any composite score.

### 2.4 Measurement Invariance

Measurement invariance -- also called measurement equivalence or factorial invariance -- is a statistical property indicating that the same construct is being measured in the same way across specified groups (Meredith, 1993; Vandenberg & Lance, 2000). If a measurement instrument functions differently for different populations -- if, for example, a depression scale measures a somewhat different construct for men than for women, or if an intelligence test has different psychometric properties for different cultural groups -- then cross-group comparisons using that instrument are uninterpretable. Violations of measurement invariance preclude meaningful comparison of scores across groups and therefore undermine the validity of any inference that depends on such comparisons.

Measurement invariance is typically tested within the framework of multiple-group confirmatory factor analysis (CFA), proceeding through a hierarchy of increasingly restrictive tests:

**Configural invariance** requires that the same factor structure holds across groups -- the same items load onto the same factors in each group. This is the weakest form of invariance: it establishes that the same constructs exist in each group but does not require that they are measured with the same precision or on the same scale.

**Metric invariance** (also called weak invariance) requires that the factor loadings -- the relationships between observed indicators and latent factors -- are equal across groups. This establishes that a one-unit change in the latent construct produces the same change in the observed indicators in each group. Metric invariance is necessary for meaningful comparison of relationships (correlations, regression slopes) across groups.

**Scalar invariance** (also called strong invariance) requires, in addition to equal factor loadings, that the intercepts of the observed indicators are equal across groups. This is the level of invariance required for meaningful comparison of latent factor *means* across groups. Without scalar invariance, observed differences in mean scores may reflect differences in how the instrument functions for different groups rather than genuine differences in the underlying construct.

**Strict invariance** requires, in addition to all of the above, that the residual variances of the observed indicators are equal across groups. This is rarely achieved in practice and is not generally considered necessary for most research purposes.

For automated software governance, measurement invariance is not an abstract concern but an operational necessity. If the same quality metrics are applied across repositories written in different programming languages (Python, TypeScript, Rust, Go), targeting different platforms (web applications, CLI tools, embedded systems, infrastructure), maintained by different organizational units, or evaluated at different points in time, then measurement invariance must be established before cross-context comparisons are meaningful. A test coverage threshold of 80% may represent substantially different levels of engineering diligence depending on the language (achieving 80% coverage in a dynamically typed language with complex runtime behavior may be more difficult than in a statically typed language with well-defined control flow), the application domain (80% coverage of a mathematical library is qualitatively different from 80% coverage of a web application with extensive UI interaction), and the testing conventions of the team. If invariance is violated, then a quality score of 85 for a Python CLI tool and a quality score of 85 for a TypeScript web application may not reflect the same level of underlying quality, and any governance decision that treats them as comparable is built on a measurement error.

---

## 3. The State of Software Measurement

### 3.1 Current Software Metrics Landscape

Software engineering has produced a substantial inventory of metrics, each proposed as a quantitative indicator of some property of software systems. The most commonly employed include:

**Lines of code (LOC).** The oldest and simplest software metric, counting the number of lines in a source file or codebase. Variants include source lines of code (SLOC, excluding blank lines and comments), logical lines of code (counting statements rather than physical lines), and various normalization schemes. LOC has been used as a predictor of development effort, defect density, and maintenance cost, despite well-documented limitations: it is language-dependent (the same functionality requires vastly different line counts in different languages), it conflates size with complexity, and it penalizes concise, well-abstracted code.

**Cyclomatic complexity.** Introduced by McCabe (1976), cyclomatic complexity measures the number of linearly independent paths through a program's control-flow graph. It is computed as M = E - N + 2P, where E is the number of edges, N is the number of nodes, and P is the number of connected components. Higher cyclomatic complexity indicates more decision points and, by hypothesis, greater difficulty in understanding, testing, and maintaining the code. McCabe proposed that functions with cyclomatic complexity exceeding 10 should be considered suspect. The metric is well-defined and efficiently computable, but its validity as a measure of "complexity" in any broader sense has been questioned: it captures control-flow branching but ignores data complexity, algorithmic complexity, architectural complexity, and cognitive complexity.

**Code coverage.** The percentage of code that is executed during automated test runs. Variants include statement coverage, branch coverage, condition coverage, path coverage, and modified condition/decision coverage (MC/DC). Higher coverage is generally interpreted as indicating more thorough testing. The metric is widely used as a quality gate -- repositories must achieve a minimum coverage threshold to pass CI checks. However, code coverage measures the *extent* of testing, not its *effectiveness*: 100% statement coverage can be achieved with tests that execute every line but assert nothing meaningful. The metric captures a necessary condition for thorough testing (untested code cannot be known to work) but is not sufficient (tested code may be tested poorly).

**Code smells.** Characteristics of source code that suggest deeper structural problems, a term popularized by Fowler (1999). Code smell detection tools identify patterns such as long methods, large classes, feature envy, shotgun surgery, and duplicated code. The concept is inherently subjective -- what constitutes a "smell" varies by language, paradigm, and development methodology -- and the relationship between code smells and actual defects or maintenance costs is empirically contested. Beck and Fowler explicitly characterized smells as heuristics requiring human judgment, but automated tools have transformed them into quantitative metrics, counting smell instances and using the counts as quality indicators.

**Build stability.** The frequency with which a project's continuous integration builds succeed or fail. Typically expressed as a success rate over a time window (e.g., 95% of builds passed in the last 30 days). Build stability is a direct indicator of integration quality but may be confounded with build infrastructure quality, test flakiness, dependency stability, and development workflow (projects with aggressive CI pipelines that run on every commit will show different stability profiles than those with periodic builds).

**Dependency metrics.** Counts and analyses of third-party dependencies, including the number of direct and transitive dependencies, the currency of dependencies (how far behind the latest version), the presence of known security vulnerabilities (via databases such as the National Vulnerability Database), and licensing compatibility. These metrics address a real concern -- supply chain risk -- but their relationship to software quality is indirect and mediated by numerous confounds.

### 3.2 What Is Missing: The Validity Question

What is conspicuously absent from the software metrics literature is any sustained engagement with the question of validity. Each metric is proposed with face validity -- it *looks like* it measures something relevant to software quality -- and is adopted on the basis of pragmatic availability (it can be computed automatically) and social consensus (other organizations use it). But the psychometric apparatus for rigorously evaluating whether a metric measures what it claims to measure is almost entirely missing.

Consider the validity questions that psychometrics would demand before trusting any of these metrics:

*Content validity.* Does the set of metrics currently used to assess software quality sample the full domain of the "software quality" construct? The answer is clearly no. Standard metric suites emphasize structural properties of source code (complexity, style conformance, coverage) but systematically underrepresent functional correctness, usability, performance, security, documentation quality, architectural coherence, and developer experience. The content validity gap is enormous, and it is invisible precisely because no one has performed the domain-mapping exercise that content validity requires.

*Criterion validity.* Do the metrics predict outcomes that matter? Does higher code coverage predict fewer production incidents? Does lower cyclomatic complexity predict faster time-to-resolution for bugs? Does a higher composite quality score predict more successful deployments? These are empirical questions, and the answers are less clear than the metrics' widespread adoption would suggest. The software engineering literature contains studies showing positive, negative, and null relationships between individual metrics and various outcomes, depending on context, methodology, and confounds. No metric has been validated against a clearly defined criterion with the rigor that psychometrics demands.

*Construct validity.* Is "software quality" -- the construct that all these metrics implicitly claim to measure -- even a single construct? Or is it a label applied to a heterogeneous collection of properties (reliability, maintainability, security, performance, usability) that may be empirically independent? Factor analysis could answer this question, but it has rarely been applied to software metrics in the psychometric sense. If factor analysis reveals multiple distinct factors underlying common quality metrics, then collapsing those metrics into a single "quality score" is a construct validity violation -- the score pretends to measure one thing while actually conflating several.

*Measurement invariance.* Do the metrics mean the same thing across contexts? An 80% coverage score in Python, TypeScript, Rust, and Go -- does it indicate the same underlying level of testing diligence? A cyclomatic complexity of 15 in a mathematical computation module, a web request handler, and a state machine implementation -- does it indicate the same underlying level of structural complexity? Without measurement invariance testing, cross-context comparisons are uninterpretable, yet such comparisons are precisely what automated governance systems perform when they apply uniform thresholds across heterogeneous repositories.

### 3.3 Multi-Metric Scoring Systems and the Latent Variable Assumption

When multiple metrics are combined into a composite quality score -- as occurs in any multi-criteria governance system -- the combination implicitly invokes a latent variable model. The composite score is treated as an estimate of an underlying quality construct that manifests through the observable indicators (the individual metrics). This is precisely the model that psychometrics calls a reflective measurement model: the latent variable "causes" the observed indicators, and the indicators are correlated because they share a common cause.

This model carries testable assumptions. The indicators should be positively correlated (if they all reflect the same construct). The correlations should be explainable by a single latent factor (unidimensionality) or by a small number of factors (a known factor structure). The factor loadings should be positive and substantial (each indicator should be a reasonable reflection of the construct). And the model should fit the observed data adequately (the predicted covariance matrix should match the observed covariance matrix).

If these assumptions are violated -- if some metrics are uncorrelated with others, or if the metrics load onto multiple distinct factors -- then the composite score is not a valid estimate of any single construct. It is an arbitrary combination of incommensurable quantities, like averaging temperature and pressure and calling the result "weather quality." The number exists, but the inference from number to construct is unjustified.

Structural equation modeling (SEM) provides the statistical framework for testing these assumptions. SEM allows the researcher to specify a hypothesized model (e.g., a single latent factor "software quality" with observed indicators "coverage," "complexity," "lint score," "build stability"), estimate the model parameters, and evaluate the model's fit to observed data. Confirmatory factor analysis (CFA), a special case of SEM, tests whether a hypothesized factor structure is consistent with the observed correlations among indicators. Multi-group CFA extends this to test measurement invariance across groups (technology stacks, project types, organizational units). These methods are mature, well-understood, and widely available in statistical software -- but they have been almost entirely absent from the software metrics literature.

### 3.4 The Dimensionality Problem: Is "Quality" One Thing or Many?

The question of dimensionality is the most consequential unresolved question in software measurement. If software quality is unidimensional -- if a single latent factor adequately explains the correlations among common quality metrics -- then composite quality scores are defensible (though they may still lack content validity, criterion validity, or measurement invariance). But if software quality is multidimensional -- if the metrics partition into multiple distinct clusters corresponding to distinct constructs such as reliability, maintainability, security, and performance -- then any single composite score is fundamentally misleading.

The ISO/IEC 25010 standard for software product quality identifies eight quality characteristics (functional suitability, performance efficiency, compatibility, usability, reliability, security, maintainability, portability), each decomposed into sub-characteristics. This taxonomy suggests multidimensionality, but taxonomies are not factor analyses. The empirical question is whether the metrics commonly used to assess these characteristics actually load onto distinct factors corresponding to the ISO categories, or whether the empirical factor structure differs from the theoretical taxonomy.

Preliminary evidence, though sparse, suggests multidimensionality. Studies that have applied factor analysis to sets of software metrics (Oman & Hagemeister, 1992; Bansiya & Davis, 2002) have typically found two to four distinct factors, not one. If this finding generalizes, it implies that the widespread practice of computing a single quality score from multiple metrics conflates distinct constructs -- a fundamental violation of construct validity that no amount of threshold-tuning or weight-adjusting can remedy. The solution is not a better composite score but a multidimensional quality profile.

---

## 4. Software Governance as Measurement Instrument

This section develops the central theoretical contribution of the thesis: the reframing of automated software governance systems as measurement instruments, subject to the same validity requirements as any psychometric instrument. A promotion state machine is a scale. A configuration contract is an operational definition. An automated check is a test item. A composite readiness score is a latent variable estimate. Once this reframing is established, the full apparatus of psychometric validity theory applies, and the strengths and weaknesses of governance systems become visible in a new light.

### 4.1 The Promotion State Machine as Guttman Scale

A Guttman scale (Guttman, 1944) is a unidimensional ordinal scale with a specific structural property: the items form a cumulative hierarchy such that endorsement of a "harder" item implies endorsement of all "easier" items. If the scale holds, the total score perfectly determines the response pattern. A person who endorses item 4 (the hardest) must also endorse items 3, 2, and 1. A person who endorses only items 1 and 2 must not endorse items 3 or 4. The Guttman scale is not merely an ordering of items by difficulty but a hypothesis about the cumulative structure of the attribute being measured.

The discovery of a Guttman scale in empirical data depends on the data conforming to this cumulative structure. Guttman's coefficient of reproducibility (CR) measures how well the observed response patterns match the patterns predicted by a perfect cumulative scale. A CR of 0.90 or higher is traditionally considered evidence that the scale holds. Scalogram analysis -- the systematic examination of response patterns for conformity to the Guttman model -- is the diagnostic procedure for evaluating whether data support the cumulative assumption.

The promotion state machine in a multi-state software governance system has precisely the structure of a Guttman scale. Consider the ORGANVM promotion chain:

**LOCAL** (initial development) -> **CANDIDATE** (ready for evaluation) -> **PUBLIC_PROCESS** (undergoing public scrutiny) -> **GRADUATED** (production-ready) -> **ARCHIVED** (end-of-life)

The cumulative assumption is explicit: a GRADUATED repository is presumed to possess all properties required at LOCAL, CANDIDATE, and PUBLIC_PROCESS, plus additional properties specific to the GRADUATED state. A CANDIDATE repository possesses all LOCAL-state properties plus the candidate-specific requirements. The promotion pipeline assumes that maturity is a cumulative, unidimensional attribute that increases monotonically through the state sequence.

This assumption is testable. For each pair of adjacent states, one can verify whether repositories in the higher state consistently exhibit the properties required at the lower state. Violations -- GRADUATED repositories that lack properties possessed by CANDIDATE repositories -- indicate that the scale is broken: the promotion state does not validly indicate the underlying construct of repository maturity.

Several types of violation are diagnostically informative:

*Hard violations* occur when a repository in a higher state fails a criterion that is explicitly required at a lower state. For example, a GRADUATED repository that lacks CI/CD configuration that is required for CANDIDATE status. These violations indicate either that the promotion criteria are not enforced (a governance failure) or that the criteria have changed over time without retroactive enforcement (a measurement drift problem).

*Soft violations* occur when a repository in a higher state exhibits lower quality on a continuous metric than repositories in a lower state. For example, a GRADUATED repository with lower test coverage than the median CANDIDATE repository. These violations may indicate that the continuous metric is not part of the construct being measured by the promotion state machine (a content validity issue) or that the relationship between the metric and the promotion state is nonlinear.

*Structural violations* occur when the ordering of items (promotion criteria) does not conform to a consistent difficulty hierarchy. If some CANDIDATE criteria are harder to achieve than some GRADUATED criteria, the cumulative assumption is violated and the scale is not unidimensional.

Scalogram analysis of the promotion pipeline would reveal the coefficient of reproducibility -- how well the observed patterns of criteria achievement match the patterns predicted by a perfect Guttman scale. A CR below 0.90 would suggest that the promotion construct is either not unidimensional (maturity is not one thing) or that the criteria are not ordered correctly (the difficulty hierarchy is misspecified).

### 4.2 seed.yaml as Operational Definition

An operational definition specifies the concrete, replicable procedures designed to represent a construct (Stevens, 1935). In the ORGANVM system, the `seed.yaml` configuration contract serves as the operational definition of repository membership, tier, implementation status, and inter-repository relationships. Each repository's `seed.yaml` declares its organ affiliation, promotion state, produces/consumes edges, and event subscriptions. This contract is the operational bridge between the abstract construct of "repository maturity" or "governance compliance" and the concrete assessment procedures that determine a repository's promotion state.

The content validity of the seed.yaml contract depends on how comprehensively it covers the domain of the construct it claims to operationalize. If "repository readiness" encompasses documentation quality, test coverage, dependency health, API stability, accessibility compliance, performance benchmarks, and security posture, then the seed.yaml must include indicators for each of these dimensions. Any dimension omitted from the contract represents a content validity gap -- an aspect of the construct that is not measured and therefore cannot influence governance decisions.

Content validity assessment for seed.yaml would proceed through the following steps: (1) convene a panel of expert judges (experienced software engineers, governance architects, security specialists) to define the full domain of "repository readiness"; (2) map each domain facet to the corresponding seed.yaml field or automated check; (3) identify facets with no corresponding measurement procedure; (4) evaluate whether the unmeasured facets are consequential for the governance decisions that depend on the readiness assessment. This is precisely the procedure that psychometrics uses to evaluate the content validity of a new test, adapted to the software governance context.

The operational definition problem is particularly acute for automated systems because the operational definition *is* the algorithm. When "code quality" is defined as the output of a specific linting tool plus a specific test coverage calculation plus a specific complexity analyzer, that operationalization becomes the de facto construct. Developers optimize for the operational definition -- they write code that satisfies the linter, achieves the coverage threshold, and keeps complexity below the cutoff -- whether or not these operational targets actually correspond to the intended construct of "quality." This is the software instantiation of teaching-to-the-test, and it is a validity threat that arises from the collapse of construct into operationalization.

### 4.3 Automated Checks as Items

Each automated check in a CI/CD pipeline functions as a test item in the psychometric sense: it evaluates the repository against a specific criterion and produces a dichotomous (pass/fail) or graded response. From an IRT perspective, each check has item parameters:

**Difficulty (b_i).** How hard is the check to pass? A check that requires the presence of a README file is easy (low b); a check that requires 90% branch coverage with mutation testing is hard (high b). Difficulty is empirically estimable from the proportion of repositories that pass the check: the fewer that pass, the harder the check.

**Discrimination (a_i).** How well does the check distinguish between high-quality and low-quality repositories? A check with high discrimination cleanly separates repositories with genuine quality from those without; a check with low discrimination is passed (or failed) by repositories of all quality levels roughly equally. Discrimination is estimated from the slope of the item characteristic curve -- the rate at which the probability of passing increases with the underlying quality level.

**Information.** Each check provides maximal information at the point on the quality continuum corresponding to its difficulty level and provides diminishing information at points further away. A check calibrated at the CANDIDATE-GRADUATED boundary provides little information about whether a repository is ready for LOCAL-CANDIDATE promotion and vice versa.

The test information function -- the sum of the information functions of all checks in the governance battery -- describes the overall precision of the governance assessment across the quality continuum. If the checks are all calibrated at similar difficulty levels (all easy, or all hard), the information function will be peaked: the assessment will be precise for repositories near that difficulty level but imprecise for repositories at other levels. A well-designed governance assessment would distribute check difficulties across the quality continuum, providing adequate information at every promotion boundary.

This analysis immediately suggests diagnostic questions for existing governance systems: What is the difficulty distribution of the current checks? Are they clustered at one point on the quality continuum, leaving other regions unmeasured? Which checks have the highest discrimination -- which are the most informative about underlying quality? Are there checks with near-zero discrimination that contribute noise rather than signal and should be removed or redesigned?

### 4.4 Human Review as Criterion

In the validity framework, criterion validity requires comparison with a "gold standard" -- an external measure accepted as a valid indicator of the construct. For automated software governance, the most natural gold standard is expert human judgment. When experienced engineers assess a repository's quality, readiness, or maturity, their assessment reflects a rich, contextual understanding of the construct that no automated system currently replicates. Human review serves as the criterion against which automated scores can be validated.

Criterion validity for an automated governance system would be established by correlating automated quality scores with independent human assessments. Concurrent validity would compare automated scores with human assessments made at the same time: do the numbers agree? Predictive validity would compare automated scores with future outcomes: do repositories that score higher experience fewer production incidents, shorter time-to-resolution, higher user satisfaction, or greater longevity?

The inter-rater reliability of human reviewers sets a ceiling on criterion validity. If expert humans agree with each other at a level of kappa = 0.70, then we cannot reasonably expect an automated system to agree with any single human at a higher level. Cohen's kappa, Fleiss' kappa (for multiple raters), the intraclass correlation coefficient (ICC), and Krippendorff's alpha are the standard statistics for quantifying inter-rater agreement, each appropriate for different measurement scales and rating designs.

For automated governance systems, the inter-rater reliability question extends to the AI reviewers themselves. When LLM-based code review tools assess repository quality, the "raters" are model runs that may vary due to temperature settings, prompt variations, context window contents, and model version updates. The reliability of these assessments -- their consistency across runs, prompts, and model versions -- must be established before their validity can even be meaningfully assessed. An unreliable automated rater cannot be valid, just as an unreliable human rater cannot be valid.

The standard benchmark for automated assessment systems in education is whether the machine agrees with humans as well as humans agree with each other. This benchmark, while reasonable, addresses only consistency (reliability), not validity. Two raters -- human or machine -- can consistently agree while both measuring the wrong thing. High inter-rater agreement between an automated system and human reviewers is necessary but not sufficient evidence that the automated system is measuring the intended construct.

---

## 5. Applying IRT to Software Governance

### 5.1 Repositories as Examinees, Governance Checks as Items

The formal analogy between psychometric assessment and software governance assessment maps cleanly onto the IRT framework. Repositories are the "examinees" -- the entities whose ability (quality, maturity, readiness) is being estimated. Governance checks are the "items" -- the assessment criteria applied to each examinee. The promotion state is the "score" -- the categorical summary of the assessment outcome. And the latent construct -- "repository quality" or "repository maturity" -- is the unobservable attribute that the assessment procedure attempts to measure.

In IRT terms, each repository j has an ability parameter theta_j representing its position on the latent quality continuum. This parameter is not directly observable; it is inferred from the repository's pattern of pass/fail responses to the governance checks. Repositories with higher theta values are expected to pass more checks, and specifically to pass harder checks, than repositories with lower theta values.

Each governance check i has item parameters: difficulty b_i (the quality level at which the check has a 50% pass rate), discrimination a_i (how sharply the check distinguishes between repositories of different quality levels), and potentially a pseudo-guessing parameter c_i (the probability that a low-quality repository passes the check by accident -- for example, a test coverage check that can be gamed by writing trivial assertions that execute all lines without testing meaningful behavior).

The IRT model then specifies the probability of repository j passing check i as a function of these parameters:

P(pass | theta_j, a_i, b_i, c_i) = c_i + (1 - c_i) / (1 + exp(-a_i(theta_j - b_i)))

This model has several immediate applications to governance design.

### 5.2 Item Characteristic Curves for CI/CD Checks

Each governance check can be characterized by its item characteristic curve (ICC) -- the sigmoid function plotting the probability of passing against the latent quality dimension. Estimating the ICC for each check requires fitting the IRT model to a matrix of pass/fail data across a population of repositories.

Consider a hypothetical set of governance checks and their estimated ICC parameters:

| Check | Difficulty (b) | Discrimination (a) | Interpretation |
|-------|----------------|---------------------|----------------|
| Has README | -2.0 | 0.8 | Very easy, low discrimination |
| Has CI config | -1.0 | 1.2 | Easy, moderate discrimination |
| Passes linting | 0.0 | 1.5 | Medium, good discrimination |
| 80% test coverage | 0.5 | 2.0 | Medium-hard, high discrimination |
| Passes security scan | 1.0 | 1.8 | Hard, high discrimination |
| Integration tests pass | 1.5 | 2.2 | Hard, very high discrimination |
| Load testing passes | 2.0 | 1.0 | Very hard, moderate discrimination |
| Mutation testing > 70% | 2.5 | 1.5 | Very hard, moderate discrimination |

The ICC parameters tell us several things that are invisible in a flat pass/fail checklist. First, difficulty ordering: the checks are not equally hard, and their ordering by difficulty may not match the ordering assumed by the governance designers. If mutation testing (b = 2.5) is treated as a CANDIDATE-level requirement while security scanning (b = 1.0) is treated as a GRADUATED-level requirement, the difficulty ordering of the checks contradicts the difficulty ordering assumed by the promotion states, which is evidence that the promotion construct is misspecified.

Second, discrimination values identify the most informative checks. The integration test check (a = 2.2) discriminates most sharply between high-quality and low-quality repositories. The README check (a = 0.8) discriminates poorly -- nearly all repositories pass it regardless of quality. A governance system that weights all checks equally wastes information: it gives the same weight to a highly discriminating check and a poorly discriminating one.

Third, the combination of difficulty and discrimination reveals the *information* each check provides. A check with high difficulty but low discrimination (load testing: b = 2.0, a = 1.0) provides moderate information only for high-quality repositories. A check with moderate difficulty and high discrimination (test coverage: b = 0.5, a = 2.0) provides substantial information precisely at the quality level where most governance decisions are made -- the CANDIDATE-GRADUATED boundary.

### 5.3 Difficulty Ordering: Which Checks Discriminate Best?

The difficulty ordering of governance checks is an empirical question that is rarely investigated empirically. Governance systems typically assign checks to promotion states based on face validity -- "this seems like a GRADUATED-level requirement" -- rather than on empirical difficulty data. IRT provides a principled alternative: estimate the difficulty of each check from the proportion of repositories that pass it (adjusted for the ability distribution of the repository population), and assign checks to promotion states based on their empirical difficulty.

If the empirically estimated difficulty ordering of checks does not match the intended ordering, several implications follow:

1. *Checks assigned to lower states may be harder than checks assigned to higher states.* This violates the cumulative assumption of the Guttman scale model and means that the promotion state does not reliably indicate a monotonically increasing level of the underlying construct.

2. *Checks at the same promotion level may have widely different difficulties.* This means that two repositories at the same promotion state may have achieved very different things, undermining the interpretability of the promotion state as a quality indicator.

3. *Some checks may have near-zero discrimination.* These checks do not distinguish between repositories of different quality levels and contribute only noise to the assessment. They should be removed, redesigned, or replaced with more discriminating alternatives.

The IRT framework provides a principled procedure for check calibration: estimate item parameters from data, assign checks to promotion levels based on their empirical difficulty, weight checks by their discrimination, and drop checks that fail to discriminate. This is the standard procedure for test calibration in psychometrics, and there is no principled reason it should not apply to governance assessments.

### 5.4 The Information Function: Where Does the Instrument Measure Best?

The test information function I(theta) is the sum of the item information functions across all checks:

I(theta) = sum_i I_i(theta)

where the item information function for the 2PL model is:

I_i(theta) = a_i^2 * P_i(theta) * (1 - P_i(theta))

This function tells us how precisely the governance assessment measures at each point on the quality continuum. The standard error of the ability estimate at any point is SE(theta) = 1 / sqrt(I(theta)).

If all checks are calibrated at similar difficulty levels, the information function will be peaked at that level and will decline rapidly at other levels. The governance system will measure precisely at the difficulty level of the checks and imprecisely everywhere else. This means that the system can distinguish reliably between repositories near the check difficulty level but cannot distinguish reliably between repositories that are much higher or much lower.

A well-designed governance assessment should have adequate information at every promotion decision boundary. If the CANDIDATE-GRADUATED boundary corresponds to theta = 1.0 on the quality continuum, there should be sufficient information at theta = 1.0 to distinguish reliably between repositories that are ready for GRADUATED status and those that are not. If the information function at that boundary is low (because few checks are calibrated near that difficulty level), then the governance decision is being made with high uncertainty -- the measurement is imprecise precisely where precision matters most.

The information function also reveals redundancy. If two checks have similar difficulty and discrimination parameters, they provide overlapping information. The second check adds little beyond what the first already provides. In a governance system with many checks, identifying and eliminating redundant checks can reduce evaluation burden without meaningful loss of measurement precision -- a parallel to the psychometric practice of shortening tests while maintaining reliability by retaining only the most informative items.

### 5.5 Measurement Invariance Across Technology Stacks and Organs

The application of IRT to software governance must confront the problem of measurement invariance: do the governance checks function the same way across different populations of repositories? In psychometric terms, this is the question of differential item functioning (DIF): does an item (check) have different difficulty or discrimination parameters for different groups (technology stacks, organizational units, project types), after controlling for the overall ability level?

If a governance check functions differently across groups -- if, for example, the "80% test coverage" check is much harder for embedded systems repositories than for web application repositories, even among repositories of the same underlying quality -- then the check exhibits DIF and the governance assessment is biased. The bias operates in a specific direction: embedded systems repositories will receive systematically lower quality estimates than web application repositories of the same true quality, because the test coverage check is harder for them in a way that does not reflect a genuine quality difference.

DIF analysis is the standard IRT method for detecting measurement bias. The procedure involves fitting the IRT model separately for each group, comparing the estimated item parameters, and testing whether the differences exceed what would be expected by chance. Items that exhibit significant DIF can be flagged for review: either the item should be revised to function equivalently across groups, or separate scoring should be implemented for different groups (acknowledging that the "same" check measures different things in different contexts).

In the ORGANVM multi-organ system, the "groups" for invariance testing include: organs (ORGAN-I repositories are predominantly theoretical Python projects; ORGAN-III repositories are predominantly commercial TypeScript products; ORGAN-IV repositories are orchestration infrastructure), programming languages (Python, TypeScript, Go, Rust), project types (libraries, CLI tools, web applications, infrastructure), and project ages (new repositories versus mature ones). Each of these groupings represents a potential source of DIF, and each requires separate invariance testing.

The practical consequence is that a single set of governance thresholds -- applied uniformly across all repositories regardless of organ, language, type, or age -- is valid only if measurement invariance holds across all of these groupings. If it does not hold (and it almost certainly does not, given the heterogeneity of the repository population), then the governance system must either (a) establish separate norms and thresholds for different groups, (b) adjust scores for group-level differences, or (c) redesign checks to achieve invariance. Each option has trade-offs, but ignoring the problem is not a valid option -- it simply embeds systematic measurement bias into the governance system.

---

## 6. Case Study: ORGANVM Promotion Pipeline

### 6.1 The Current Scoring Methodology

The ORGANVM system implements a multi-organ governance framework spanning approximately 117 repositories across eight organizational organs. Each repository is governed by a seed.yaml contract that declares its organ membership, tier, implementation status, and inter-repository dependencies. The promotion state machine defines five states: LOCAL, CANDIDATE, PUBLIC_PROCESS, GRADUATED, and ARCHIVED, with transitions governed by a combination of automated checks and human review.

The current assessment methodology employs an omega scorecard -- a composite evaluation framework that aggregates multiple assessment dimensions into a holistic readiness indicator. The scorecard evaluates repositories against criteria that include: presence and completeness of seed.yaml, CI/CD configuration, test coverage metrics, linting compliance, documentation completeness, dependency health, security posture, and architectural conformance with organ-level conventions. Individual criteria are assessed as present/absent or as continuous scores, and the results are combined into a composite readiness score.

This methodology exemplifies the measurement practices that the psychometric framework calls into question. The scorecard combines heterogeneous indicators -- binary presence checks, continuous metric scores, and categorical assessments -- into a single number. The combination assumes that the indicators reflect a single underlying construct (repository readiness) and that the combining procedure (whether weighted or unweighted summation) appropriately maps indicator patterns to construct levels. Neither assumption has been empirically tested.

### 6.2 Factor Analysis: Is the Omega Scorecard Unidimensional?

The most consequential empirical question about the omega scorecard is whether the indicators it combines actually reflect a single latent construct or multiple distinct constructs. This is the question that factor analysis is designed to answer.

An exploratory factor analysis (EFA) of the scorecard indicators across the full repository population would proceed as follows: (1) compute the correlation matrix among all scorecard indicators across all repositories with available data; (2) determine the number of factors to extract using parallel analysis, the Kaiser criterion, or scree plot inspection; (3) extract factors using principal axis factoring or maximum likelihood estimation; (4) rotate the factor solution using oblique rotation (promax or oblimin) to allow correlated factors; (5) interpret the factor structure by examining which indicators load most strongly onto each factor.

Several factor structures are plausible a priori:

*Unidimensional.* All indicators load onto a single factor, supporting the interpretation that the scorecard measures a single construct ("repository readiness"). This would validate the composite scoring approach, though it would not address content validity or criterion validity concerns.

*Two-factor.* Indicators partition into "process maturity" (CI/CD, seed.yaml, documentation) and "code quality" (test coverage, linting, complexity). This would suggest that the scorecard conflates two distinct constructs and that a single composite score is misleading.

*Three-factor.* Indicators partition into "structural completeness" (seed.yaml, README, CI config), "code quality" (coverage, linting, complexity), and "operational readiness" (build stability, dependency health, security). This would suggest an even more differentiated picture of repository maturity.

*Multidimensional with cross-loadings.* Some indicators load onto multiple factors, suggesting complex relationships between constructs that a simple composite score cannot represent.

Confirmatory factor analysis (CFA) would then test whether the empirically derived factor structure fits the data adequately, using fit indices such as the comparative fit index (CFI), the Tucker-Lewis index (TLI), the root mean square error of approximation (RMSEA), and the standardized root mean square residual (SRMR). Conventional cutoffs (CFI > 0.95, RMSEA < 0.06, SRMR < 0.08; Hu & Bentler, 1999) provide benchmarks for acceptable fit, though these cutoffs are approximate and context-dependent.

If the unidimensional model fits poorly -- if the data reject the hypothesis that a single factor underlies the scorecard indicators -- then the composite scoring approach is not merely imprecise but fundamentally invalid. The score does not measure any single construct, and governance decisions based on it are not psychometrically defensible. The appropriate response would be to replace the single score with a multidimensional profile, reporting separate scores for each empirically identified factor.

### 6.3 Proposed Psychometric Calibration

Based on the theoretical framework developed in the preceding sections, a psychometric calibration of the ORGANVM governance system would proceed through the following stages:

**Stage 1: Item analysis.** For each governance check, compute the pass rate across the repository population and the point-biserial correlation between the check result and the total score (excluding that check). Checks with very high or very low pass rates contribute little information. Checks with low point-biserial correlations do not discriminate between high-scoring and low-scoring repositories and may be measuring a different construct.

**Stage 2: Factor analysis.** Conduct EFA on the full set of governance indicators to determine the empirical factor structure. Follow with CFA to test the identified structure. If the factor structure is multidimensional, compute separate subscores for each factor rather than a single composite.

**Stage 3: IRT calibration.** Fit an IRT model (initially a 2PL model) to the pass/fail data for all governance checks. Estimate difficulty and discrimination parameters for each check. Compute the test information function and identify regions of the quality continuum where measurement precision is inadequate.

**Stage 4: Measurement invariance testing.** Conduct multi-group CFA across organs, programming languages, and project types to test whether the factor structure and factor loadings are invariant. Conduct DIF analysis on individual checks to identify checks that function differently across groups.

**Stage 5: Criterion validation.** Correlate governance scores with external criteria: production incident rates, peer review assessments, deployment success rates, time-to-resolution for reported issues, and other outcomes that the governance system is implicitly designed to predict. Compute concurrent and predictive validity coefficients.

**Stage 6: Iterative refinement.** Based on the results of Stages 1-5, revise the governance instrument: remove non-discriminating checks, add checks for under-measured regions of the quality continuum, adjust promotion-state assignments to match empirical difficulty ordering, and implement group-specific norms where invariance is violated.

### 6.4 Where the Current System Violates Measurement Principles

Even without empirical data, the theoretical framework identifies several points where the current ORGANVM governance system likely violates psychometric measurement principles:

**Uniform weighting.** All governance checks contribute equally to the composite score, regardless of their difficulty or discrimination. This is the CTT assumption of parallel items, which IRT demonstrates to be unrealistic. Checks that are very easy (nearly all repositories pass them) or very hard (nearly none pass them) contribute minimal information to the quality estimate and should receive less weight.

**Single composite score.** The omega scorecard produces a single readiness number from multiple heterogeneous indicators. Without factor-analytic evidence of unidimensionality, this composite score is psychometrically indefensible. If the indicators measure multiple distinct constructs, the composite conflates them in a way that obscures both the individual construct levels and the relationships between constructs.

**Uniform thresholds across contexts.** The same governance thresholds are applied across organs with different technology stacks, project types, and maturity levels. Without measurement invariance testing, this practice may introduce systematic bias -- penalizing repositories in contexts where the checks are harder and favoring repositories in contexts where the checks are easier, independent of true quality differences.

**No criterion validation.** The governance scores have not been validated against external criteria. There is no evidence that repositories with higher scores actually perform better in production, receive better peer assessments, or achieve other outcomes that the governance system is designed to promote. Without criterion validation, the governance system is internally consistent but externally unanchored.

**No error quantification.** Governance scores are reported without confidence intervals, standard errors, or any other indication of measurement uncertainty. Every score is treated as exact, implying perfect reliability. CTT demonstrates that this assumption is untenable for any finite-reliability instrument, and the practical consequence is that governance decisions near promotion thresholds are being made with unquantified uncertainty.

**Construct-operationalization collapse.** The governance system defines "readiness" as whatever the governance checks measure. This circular definition precludes validity assessment: if the construct *is* the operational definition, there is no independent standard against which to evaluate whether the operational definition captures the construct. Breaking this circularity requires an independent theoretical definition of readiness -- one that can be used to evaluate whether the governance checks adequately operationalize the intended construct.

---

## 7. Implications for Automated Governance Design

The psychometric framework developed in this thesis has concrete implications for the design of automated governance systems, whether in the ORGANVM context or in software organizations more broadly.

**First, governance systems should be designed as measurement instruments, with explicit attention to reliability, validity, and measurement invariance from the outset.** This means defining the construct to be measured (repository readiness, software quality, deployment fitness) independently of the measurement procedure, evaluating the measurement procedure against that independent definition, and iterating until the procedure demonstrably captures the construct. The design process should follow the psychometric test development lifecycle: construct definition, item writing, pilot testing, item analysis, calibration, and validation.

**Second, composite scores should be used only when factor-analytic evidence supports unidimensionality.** If the governance indicators load onto multiple distinct factors, separate subscores should be reported for each factor. Governance decisions can still depend on multiple subscores -- a repository might need to achieve minimum levels on each factor -- but the decision rule should acknowledge the multidimensionality of the construct rather than hiding it behind a single number.

**Third, IRT-based scoring should replace uniform weighting.** Each governance check should be characterized by its difficulty and discrimination parameters, estimated from empirical data. Checks should be weighted by their information content rather than treated as equal units. This is standard practice in educational assessment and is feasible for any governance system with a sufficient population of assessed repositories.

**Fourth, measurement invariance should be tested before cross-context comparisons are made.** If governance scores are used to compare repositories across technology stacks, organs, or project types, invariance must be established. Where invariance is violated, separate norms, adjusted thresholds, or redesigned checks are necessary to ensure fair and interpretable comparison.

**Fifth, criterion validation should be an ongoing activity.** Governance scores should be periodically correlated with external outcomes (production incidents, deployment success, peer assessments, user satisfaction) to verify that the scores predict the outcomes they are intended to predict. Criterion validity is not a one-time demonstration but a continuing obligation, because both the governance system and the external environment change over time.

**Sixth, adaptive assessment deserves exploration.** IRT enables adaptive testing -- selecting items based on the examinee's estimated ability. An adaptive governance system would evaluate repositories with checks selected based on estimated quality, concentrating measurement effort on the checks most informative for each repository's quality level. This would reduce evaluation burden for repositories whose quality level is clearly above or below a promotion threshold while maintaining precision for repositories near the boundary where the decision matters most.

**Seventh, consequential validity must be monitored.** Messick (1989) argued that the social consequences of score use are part of the validity argument. In the governance context, consequential validity asks whether the governance system produces desirable organizational outcomes or whether it induces pathological behaviors -- Goodhart's Law (when a measure becomes a target, it ceases to be a good measure) and Campbell's Law (the more a quantitative indicator is used for social decision-making, the more subject it will be to corruption pressures and the more apt it will be to distort and corrupt the social processes it was intended to monitor). If developers optimize for governance scores rather than for the quality constructs the scores are meant to reflect -- writing trivial tests to inflate coverage numbers, suppressing lint warnings rather than fixing the underlying issues, adding boilerplate documentation that satisfies presence checks without conveying useful information -- then the governance system is undermining its own purpose. Monitoring for these pathological optimization patterns is a validity obligation.

---

## 8. Discussion and Limitations

This thesis has argued that automated software governance systems are measurement instruments and should be evaluated as such, using the validity frameworks developed by a century of psychometric research. The argument is conceptual and theoretical: it imports an established framework from one domain (psychological measurement) into another (software engineering) and demonstrates the fit. Several limitations of this approach warrant discussion.

**The analogy has limits.** Psychometric measurement theory was developed for measuring latent attributes of *persons* -- intelligence, personality, knowledge, attitudes. Software repositories are not persons, and "software quality" may not behave like a psychological construct. Psychological constructs are assumed to be relatively stable attributes of individuals that generate consistent patterns of behavior across situations. Software quality, by contrast, may be highly context-dependent (the same code may be high quality for a prototype and low quality for a production system), rapidly changing (a single commit can dramatically alter quality), and multiply realized (quality can be achieved through very different architectural and engineering approaches). The extent to which psychometric models developed for person measurement apply to artifact measurement is an open empirical question.

**Sample sizes may be inadequate.** IRT parameter estimation requires substantial sample sizes -- typically 200 or more respondents for 2PL models and 500 or more for 3PL models. Many software organizations do not have enough repositories to support stable IRT parameter estimation. The ORGANVM system, with approximately 117 repositories, approaches the minimum for 2PL estimation but may not support more complex models. Creative solutions -- treating repositories at different points in time as different "respondents," pooling across organizations, or using Bayesian estimation methods with informative priors -- may be necessary.

**The "gold standard" problem.** Criterion validity requires a criterion, and there is no universally accepted gold standard for software quality. Human expert judgment is the most natural candidate, but human judgments are themselves variable, subjective, and potentially biased. Production outcomes (incident rates, deployment success) are contaminated by factors unrelated to code quality (traffic patterns, infrastructure stability, operational practices). The choice of criterion influences what the governance system optimizes for, and no criterion is perfect.

**Causal inference is difficult.** The framework identifies correlational relationships between governance scores and external outcomes but does not establish causation. A positive correlation between governance scores and deployment success does not prove that high governance scores *cause* successful deployments -- both may be caused by a third factor (organizational maturity, team experience, management attention). Causal inference in observational settings requires careful control of confounds, which is challenging in the messy reality of software development.

**The framework is resource-intensive.** Full psychometric calibration -- factor analysis, IRT estimation, invariance testing, criterion validation -- requires substantial data collection and analysis. For organizations with small repository populations or limited measurement infrastructure, the full framework may be impractical. However, even partial application -- asking the validity questions without formal statistical testing -- represents an improvement over the current state of no validity assessment at all.

**Dynamic constructs pose challenges.** Software quality is not static; it changes with every commit, dependency update, and infrastructure modification. Psychometric models were developed for constructs that are assumed to be stable during the measurement occasion. Applying these models to rapidly changing artifacts requires either (a) treating each snapshot as a separate measurement occasion and tracking measurement properties over time, or (b) developing dynamic extensions of psychometric models that accommodate temporal variation. This is a frontier area with limited existing theory.

---

## 9. Conclusion

Software engineering has accumulated an impressive arsenal of metrics and an almost complete absence of measurement theory. This thesis has argued that the gap is consequential: automated governance systems that use composite quality scores to make high-stakes decisions about software promotion, deployment, and lifecycle management are operating without the psychometric foundations that adjacent fields consider essential for any measurement-based decision system. The tools for closing this gap exist -- classical test theory, item response theory, the unified validity framework, factor analysis, structural equation modeling, measurement invariance testing, differential item functioning analysis -- and they are mature, well-documented, and computationally tractable. What is missing is not the technology but the will to apply it.

The three research questions posed in this thesis -- whether software quality is unidimensional, whether promotion state machines satisfy Guttman scale properties, and how measurement invariance should be established across technology stacks -- are all empirically answerable with existing methods and data. Answering them would transform software governance from an engineering heuristic into a measurement-theoretic practice: a practice that defines its constructs independently of its measurement procedures, estimates the precision and bias of those procedures, validates them against external criteria, tests their invariance across contexts, and monitors their consequential effects on the systems they are intended to govern.

The Rasch tradition offers a particularly apt aspiration for software governance: specific objectivity -- the requirement that the comparison of any two repositories be independent of which specific checks are used to evaluate them, and that the comparison of any two checks be independent of which specific repositories they are applied to. This is a demanding standard, and it may not be fully achievable in the software domain. But it is the standard that genuine measurement demands, and even partial progress toward it would represent a significant advance over the current practice of treating every number produced by an automated system as a valid measurement simply because it was produced consistently.

The title of this thesis invokes the unmeasurable, but the argument it makes is that software quality is not unmeasurable -- it is unmeasured. The distinction matters. Unmeasurable implies impossibility; unmeasured implies only that the work has not yet been done. Psychometrics provides the blueprint. The construction remains.

---

## References

Allen, M. J., & Yen, W. M. (2002). *Introduction to measurement theory*. Waveland Press.

Bansiya, J., & Davis, C. G. (2002). A hierarchical model for object-oriented design quality assessment. *IEEE Transactions on Software Engineering*, 28(1), 4-17.

Beck, K. (2000). *Extreme programming explained: Embrace change*. Addison-Wesley.

Borsboom, D., Mellenbergh, G. J., & van Heerden, J. (2004). The concept of validity. *Psychological Review*, 111(4), 1061-1071.

Campbell, D. T. (1979). Assessing the impact of planned social change. *Evaluation and Program Planning*, 2(1), 67-90.

Campbell, D. T., & Fiske, D. W. (1959). Convergent and discriminant validation by the multitrait-multimethod matrix. *Psychological Bulletin*, 56(2), 81-105.

Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika*, 16(3), 297-334.

Cronbach, L. J., & Meehl, P. E. (1955). Construct validity in psychological tests. *Psychological Bulletin*, 52(4), 281-302.

de Ayala, R. J. (2009). *The theory and practice of item response theory*. Guilford Press.

Embretson, S. E., & Reise, S. P. (2000). *Item response theory for psychologists*. Lawrence Erlbaum.

Fenton, N. E., & Bieman, J. (2014). *Software metrics: A rigorous and practical approach* (3rd ed.). CRC Press.

Fowler, M. (1999). *Refactoring: Improving the design of existing code*. Addison-Wesley.

Goodhart, C. A. E. (1984). Problems of monetary management: The UK experience. In C. A. E. Goodhart (Ed.), *Monetary theory and practice* (pp. 91-121). Macmillan.

Guttman, L. (1944). A basis for scaling qualitative data. *American Sociological Review*, 9(2), 139-150.

Guttman, L. (1950). The basis for scalogram analysis. In S. A. Stouffer et al. (Eds.), *Measurement and prediction* (pp. 60-90). Princeton University Press.

Hu, L., & Bentler, P. M. (1999). Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives. *Structural Equation Modeling*, 6(1), 1-55.

ISO/IEC 25010:2011. *Systems and software engineering -- Systems and software Quality Requirements and Evaluation (SQuaRE) -- System and software quality models*. International Organization for Standardization.

Kan, S. H. (2003). *Metrics and models in software quality engineering* (2nd ed.). Addison-Wesley.

Likert, R. (1932). A technique for the measurement of attitudes. *Archives of Psychology*, 22(140), 1-55.

Lord, F. M., & Novick, M. R. (1968). *Statistical theories of mental test scores*. Addison-Wesley.

McCabe, T. J. (1976). A complexity measure. *IEEE Transactions on Software Engineering*, SE-2(4), 308-320.

Meredith, W. (1993). Measurement invariance, factor analysis and factorial invariance. *Psychometrika*, 58(4), 525-543.

Messick, S. (1989). Validity. In R. L. Linn (Ed.), *Educational measurement* (3rd ed., pp. 13-103). Macmillan.

Messick, S. (1995). Validity of psychological assessment: Validation of inferences from persons' responses and performances as scientific inquiry into score meaning. *American Psychologist*, 50(9), 741-749.

Novick, M. R. (1966). The axioms and principal results of classical test theory. *Journal of Mathematical Psychology*, 3(1), 1-18.

Oman, P. W., & Hagemeister, J. (1992). Metrics for assessing a software system's maintainability. In *Proceedings of the International Conference on Software Maintenance* (pp. 337-344). IEEE.

Rasch, G. (1960). *Probabilistic models for some intelligence and attainment tests*. Danish Institute for Educational Research.

Spearman, C. (1904). The proof and measurement of association between two things. *American Journal of Psychology*, 15(1), 72-101.

Stevens, S. S. (1935). The operational definition of psychological concepts. *Psychological Review*, 42(6), 517-527.

Stevens, S. S. (1946). On the theory of scales of measurement. *Science*, 103(2684), 677-680.

Strathern, M. (1997). "Improving ratings": Audit in the British university system. *European Review*, 5(3), 305-321.

Thurstone, L. L. (1928). Attitudes can be measured. *American Journal of Sociology*, 33(4), 529-554.

Vandenberg, R. J., & Lance, C. E. (2000). A review and synthesis of the measurement invariance literature: Suggestions, practices, and recommendations for organizational research. *Organizational Research Methods*, 3(1), 4-70.

Wright, B. D., & Stone, M. H. (1979). *Best test design: Rasch measurement*. MESA Press.
