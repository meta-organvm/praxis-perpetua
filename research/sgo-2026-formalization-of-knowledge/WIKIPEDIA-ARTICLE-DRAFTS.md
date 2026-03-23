# Wikipedia Article Drafts -- SGO Research Program Novel Concepts

**Prepared for:** Apadavano Wikipedia account
**Date:** 2026-03-20
**Source material:** SGO-2026-SYN-002 (Governance Impossibility Thesis), SGO-2026-SYN-003 (Names That Hold), SGO-2026-SOP-001 (Triadic Review Protocol)
**Wikipedia verification:** Searches conducted 2026-03-20 confirming no existing articles for these concepts.

---

## Article 1: Governance Trilemma

### Verification

Searched Wikipedia for "Governance trilemma" and "Trilemma of governance" on 2026-03-20. No article exists. The general [[Trilemma]] article lists several named trilemmas (Munchhausen trilemma, impossible trinity, Epicurean trilemma) but does not include a governance trilemma. The concept is novel to the SGO research program (SYN-02).

### Proposed article title

**Governance trilemma**

### Wikitext content

```wikitext
{{Short description|Structural constraint on self-governing systems}}
{{More citations needed|date=March 2026}}

The '''governance trilemma''' is a proposed structural constraint on [[self-governance|self-governing systems]], stating that no such system can simultaneously achieve three desirable properties: '''completeness''' (the system governs all of itself), '''consistency''' (its governance rules do not contradict each other), and '''measurability''' (governance outcomes can be validly assessed). Any two of these properties can be approximated, but attaining two forces the sacrifice of the third.<ref name="sgo-syn02">{{Cite thesis |last=<!-- Author --> |title=The Governance Impossibility Thesis: Formal Limits of Self-Describing, Self-Measuring, Self-Organizing Systems |date=2026 |type=Working paper |series=Studium Generale ORGANVM Research Program, SYN-02}}</ref>

The trilemma synthesizes [[impossibility theorem|impossibility results]] from three independent intellectual traditions: [[mathematical logic]] ([[Gödel's incompleteness theorems]], [[Tarski's undefinability theorem]], [[Rice's theorem]]), [[social choice theory]] ([[Arrow's impossibility theorem]], [[Gibbard–Satterthwaite theorem]]), and [[measurement theory]] ([[Goodhart's law]], [[Campbell's law]], [[construct validity]]). It applies to organizations, platforms, software architectures, and AI-augmented institutions that attempt to describe their own structure, measure their own performance, and organize their own coordination.

The governance trilemma does not claim to be a formal [[theorem]] in the sense of [[Gödel's incompleteness theorems|Godel's result]]; it is presented as a design constraint that exhibits the same structural signature -- the impossibility of simultaneously satisfying three desiderata within a closed system -- grounded in established formal results and robust empirical regularities.

== Background ==

=== Impossibility results in mathematics and social science ===

Several twentieth-century results established fundamental limits on what systems can achieve when their evaluative apparatus is applied to themselves:

* '''[[Gödel's incompleteness theorems]]''' (1931): Any consistent [[formal system]] capable of encoding basic [[arithmetic]] contains true statements it cannot prove, and cannot prove its own consistency.<ref>{{Cite journal |last=Gödel |first=Kurt |date=1931 |title=Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I |journal=Monatshefte für Mathematik und Physik |volume=38 |pages=173–198 |doi=10.1007/BF01700692}}</ref> This establishes that complete self-description is impossible for sufficiently expressive systems.

* '''[[Tarski's undefinability theorem]]''' (1933): [[Truth]] for a sufficiently strong formal system cannot be defined by a formula within the system itself; a [[metalanguage]] hierarchy is required.<ref>{{Cite book |last=Tarski |first=Alfred |date=1933 |title=Pojęcie prawdy w językach nauk dedukcyjnych |trans-title=The Concept of Truth in Formalized Languages |location=Warsaw}}</ref>

* '''[[Rice's theorem]]''' (1953): Every non-trivial [[semantic]] property of [[Computer program|programs]] is [[Undecidable problem|undecidable]].<ref>{{Cite journal |last=Rice |first=H. G. |date=1953 |title=Classes of recursively enumerable sets and their decision problems |journal=Transactions of the American Mathematical Society |volume=74 |issue=2 |pages=358–366 |doi=10.2307/1990888}}</ref> This draws a boundary between [[Syntax (programming languages)|syntactic]] properties (which can be automatically verified) and semantic properties (which cannot).

* '''[[Arrow's impossibility theorem]]''' (1950): No [[ranked voting]] aggregation procedure can simultaneously satisfy a minimal set of rationality axioms.<ref>{{Cite journal |last=Arrow |first=Kenneth J. |date=1950 |title=A Difficulty in the Concept of Social Welfare |journal=Journal of Political Economy |volume=58 |issue=4 |pages=328–346 |doi=10.1086/256963}}</ref>

* '''[[Goodhart's law]]''' (1975): "When a measure becomes a target, it ceases to be a good measure."<ref>{{Cite journal |last=Goodhart |first=Charles |date=1975 |title=Problems of Monetary Management: The U.K. Experience |journal=Papers in Monetary Economics |volume=1 |publisher=Reserve Bank of Australia}}</ref> '''[[Campbell's law]]''' (1979) generalises this: quantitative social indicators used for decision-making are subject to corruption pressures that distort the processes they monitor.<ref>{{Cite journal |last=Campbell |first=Donald T. |date=1979 |title=Assessing the Impact of Planned Social Change |journal=Evaluation and Program Planning |volume=2 |issue=1 |pages=67–90 |doi=10.1016/0149-7189(79)90048-X}}</ref>

These traditions developed in relative isolation. The governance trilemma proposes that they converge on a single structural pattern when applied to systems that govern themselves.

== The three trade-offs ==

The trilemma identifies three possible two-property combinations, each requiring the sacrifice of the third property.

=== Complete and consistent, but unmeasurable ===

A governance system that governs all aspects of itself (completeness) with non-contradictory rules (consistency) creates maximal conditions for [[Goodhart's law|Goodhart corruption]]. The comprehensiveness of the governance framework means that every component is assessed by governance metrics, and the consistency of the framework means those metrics produce determinate verdicts. Actors within the system face a comprehensive, determinate set of metrics and can optimise for those metrics rather than for the underlying constructs. The reflexive feedback loop identified by [[Campbell's law]] -- comprehensive measurement creating comprehensive optimisation pressure that corrupts the measurements -- becomes maximal. The system governs everything consistently but can no longer validly assess whether its governance is achieving its intended outcomes.

=== Complete and measurable, but inconsistent ===

A governance system that governs all aspects of itself (completeness) with valid metrics (measurability) encounters the [[Undecidable problem|undecidability]] results of mathematical logic. [[Rice's theorem]] guarantees that the semantic properties governance cares about -- "does this component do what it should?" -- are undecidable in the general case. The system encounters cases where its governance processes, applied to different aspects of the same component through different evaluation paths, produce contradictory outputs. [[Gödel's incompleteness theorems|Godel's second incompleteness theorem]] sharpens this: the system cannot prove its own consistency. The result is not formal logical contradiction but operational inconsistency -- a persistent stream of boundary cases where the governance apparatus produces conflicting guidance.

=== Consistent and measurable, but incomplete ===

A governance system preserves non-contradictory rules (consistency) and valid measurement (measurability) by restricting its jurisdiction -- leaving some domains ungoverned. This is described as the most practically viable combination and the position that well-designed governance systems typically adopt, whether explicitly or implicitly. [[Legal system]]s maintain consistency and measurability by declaring some disputes non-justiciable. Software governance systems restrict automated assessment to [[Syntax (programming languages)|syntactic]] properties (where Rice's theorem does not apply) and delegate [[semantic]] assessment to human review.

== Design responses ==

The trilemma does not counsel abandoning governance but rather designing systems that work within their structural limits. Proposed responses include:

* '''Staged governance''': Validating a system's ''previous'' state using its ''current'' state, converting circular self-reference into sequential cross-reference. This addresses the [[Gödel's incompleteness theorems|Godelian]] impossibility by ensuring the governance system is never asked to verify itself at the present moment.<ref name="sgo-syn02" />
* '''Hybrid topology''': Combining [[Hierarchy|hierarchical]] structure where coordination failure is costly with flat, [[Rhizome (philosophy)|rhizomatic]] connectivity where innovation requires unexpected combinations.<ref>{{Cite book |last=Scott |first=James C. |date=1998 |title=Seeing Like a State |publisher=Yale University Press |isbn=0-300-07016-0}}</ref>
* '''Psychometrically calibrated measurement''': Applying [[psychometrics|psychometric]] [[construct validity|validity theory]] -- [[factor analysis]], [[item response theory]], [[measurement invariance]] testing -- to governance metrics to detect and mitigate measurement corruption.<ref>{{Cite book |last=Messick |first=Samuel |date=1989 |title=Validity |work=Educational Measurement |edition=3rd |editor-last=Linn |editor-first=R. L. |publisher=Macmillan |pages=13–103}}</ref>
* '''Human-in-the-loop''': Placing human judgement at the points where formal governance fails, functioning as a [[metalanguage]] -- the "Tarskian escape" -- that provides evaluative resources richer than the governance system's own formal rules.
* '''Dynamic trilemma navigation''': Treating the trilemma as a navigable design space, shifting the system's position across its lifecycle (e.g., accepting inconsistency during early exploratory phases, then migrating toward consistency-plus-measurability as the system scales).

== Relationship to other trilemmas ==

The governance trilemma is structurally analogous to several established trilemmas:

* The '''[[impossible trinity]]''' (Mundell-Fleming trilemma) in [[international economics]]: a country cannot simultaneously maintain a fixed [[exchange rate]], free [[capital movement]], and independent [[monetary policy]].<ref>{{Cite journal |last=Mundell |first=Robert A. |date=1963 |title=Capital Mobility and Stabilization Policy under Fixed and Flexible Exchange Rates |journal=Canadian Journal of Economics and Political Science |volume=29 |issue=4 |pages=475–485 |doi=10.2307/139336}}</ref>
* The '''[[CAP theorem]]''' in [[distributed computing]]: a distributed data store cannot simultaneously provide [[Consistency (database systems)|consistency]], [[Availability|availability]], and [[Network partition|partition tolerance]].<ref>{{Cite conference |last=Brewer |first=Eric |date=2000 |title=Towards Robust Distributed Systems |conference=ACM Symposium on Principles of Distributed Computing}}</ref>
* The '''blockchain scalability trilemma''' attributed to [[Vitalik Buterin]]: a blockchain cannot simultaneously achieve [[decentralisation]], [[Computer security|security]], and [[scalability]].
* '''[[Holmström's theorem]]''' in [[economics]]: no incentive system for a team can simultaneously achieve [[budget balance]], [[Pareto efficiency]], and [[Individual rationality|individual rationality]].

All share the structural pattern of three desirable properties, only two of which can be jointly achieved. The governance trilemma extends this pattern to the domain of [[self-governance]], drawing on formal impossibility results from logic, social choice, and measurement theory rather than from economics or computer science alone.

== Relationship to the viable system model ==

The governance trilemma has been mapped to [[Stafford Beer]]'s [[viable system model]] (VSM).<ref>{{Cite book |last=Beer |first=Stafford |date=1972 |title=Brain of the Firm |publisher=Allen Lane |isbn=0-471-94839-X}}</ref> In this mapping:
* '''System 3''' (control) manages consistency across operational units
* '''System 3*''' (sporadic audit) manages measurability by providing an independent measurement channel resistant to Goodhart corruption
* '''System 4''' (intelligence) manages the completeness boundary, identifying ungoverned domains and proposing governance extensions
* '''System 5''' (policy) resolves trilemma conflicts, functioning as the locus of normative judgement where the governance system's trilemma position is chosen
* The '''System 3-4 homeostat''' provides dynamic trilemma navigation, balancing present-focused control (consistency and measurability) with future-focused intelligence (completeness and adaptation)

== Criticisms and limitations ==

The governance trilemma has been presented as a structural design constraint rather than a formally proven [[theorem]].<ref name="sgo-syn02" /> A full formalisation would require a precise mathematical definition of "governance system" and formal proofs that the three properties are jointly unsatisfiable under specified conditions. Critics may object that:

* Existing governance systems function adequately without impossibility awareness. The response is that these systems are already implicitly choosing which trilemma vertex to sacrifice; the trilemma makes this choice explicit.
* [[Mechanism design]] theory has produced environments (such as [[Vickrey–Clarke–Groves mechanism|VCG mechanisms]] and [[scoring rule|proper scoring rules]]) where measurement and incentive alignment are maintained by design. The response is that these solutions are domain-specific and do not eliminate the systemic Goodhart dynamics that arise from governance as an ongoing, multi-metric process.
* The analogies to [[Gödel's incompleteness theorems]] are suggestive but not formally rigorous. The structural parallel depends on the claim that governance systems are "sufficiently expressive" in a sense analogous to formal systems capable of encoding arithmetic, which requires further formalisation.

== See also ==

* [[Trilemma]]
* [[Impossible trinity]]
* [[CAP theorem]]
* [[Gödel's incompleteness theorems]]
* [[Arrow's impossibility theorem]]
* [[Goodhart's law]]
* [[Campbell's law]]
* [[Rice's theorem]]
* [[Tarski's undefinability theorem]]
* [[Viable system model]]
* [[Self-governance]]
* [[Construct validity]]
* [[Holmström's theorem]]

== References ==
{{Reflist}}

{{DEFAULTSORT:Governance trilemma}}
[[Category:Trilemmas]]
[[Category:Governance]]
[[Category:Impossibility theorems]]
[[Category:Systems theory]]
[[Category:Cybernetics]]
[[Category:Social choice theory]]
[[Category:Measurement]]
```

### Suggested categories

- [[Category:Trilemmas]]
- [[Category:Governance]]
- [[Category:Impossibility theorems]]
- [[Category:Systems theory]]
- [[Category:Cybernetics]]
- [[Category:Social choice theory]]
- [[Category:Measurement]]

### Existing Wikipedia articles to link to/from

**Link to (from this article):**
- [[Trilemma]] -- add governance trilemma to the list of named trilemmas
- [[Godel's incompleteness theorems]]
- [[Arrow's impossibility theorem]]
- [[Goodhart's law]]
- [[Campbell's law]]
- [[Rice's theorem]]
- [[Tarski's undefinability theorem]]
- [[Impossible trinity]]
- [[CAP theorem]]
- [[Viable system model]]
- [[Stafford Beer]]
- [[Construct validity]]
- [[Holmstrom's theorem]]
- [[Self-governance]]
- [[Mechanism design]]
- [[Gibbard-Satterthwaite theorem]]

**Link from (add links in these articles pointing to governance trilemma):**
- [[Trilemma]] -- add to list of examples
- [[Self-governance]] -- add to "See also" or "Limitations" section
- [[Goodhart's law]] -- mention in "Applications" as part of a formal trilemma framework

### Notability assessment

**Moderate risk of deletion for lack of notability.** The concept is novel and originates from a working paper, not yet published in a peer-reviewed venue. Wikipedia's [[WP:GNG]] (General Notability Guideline) requires "significant coverage in reliable, independent sources." To survive:

1. The underlying paper (SYN-02) must be published -- ideally in a peer-reviewed journal (Philosophy and Technology, ACM Computing Surveys) or at minimum on arXiv with subsequent citations.
2. The article's strength is that it synthesizes entirely from *existing* Wikipedia-notable concepts (Godel, Arrow, Goodhart, Beer). The synthesis itself is what needs sourcing.
3. **Recommended strategy:** Publish the paper on arXiv first, submit to a journal, then create the Wikipedia article once there is at least one citable published source. In the interim, the concept could be added as a brief mention in the [[Trilemma]] article's list of examples, which has a lower notability bar.
4. Secondary coverage by independent sources (e.g., a blog post by a governance researcher, a citation in another paper) would substantially strengthen the case.

**Risk level:** HIGH if created before publication. MODERATE if created after arXiv publication. LOW if created after peer-reviewed publication and at least one independent citation.

---

## Article 2: Syntactic-semantic boundary (governance)

### Verification

Searched Wikipedia for "syntactic semantic boundary governance" on 2026-03-20. No article exists for this specific concept. The [[Rice's theorem]] article discusses the syntactic/semantic distinction for program properties. The [[George Lakoff]] article mentions debate over whether there is a boundary separating syntax and semantics in natural language. No article addresses the governance application of this distinction.

### Proposed article title

**Syntactic-semantic boundary (governance)**

### Wikitext content

```wikitext
{{Short description|Distinction between automatically verifiable and human-judgment-requiring governance rules}}
{{More citations needed|date=March 2026}}

In the context of [[governance]] and [[automated]] systems, the '''syntactic-semantic boundary''' is the distinction between governance rules whose compliance can be [[Decidability (logic)|automatically verified]] (syntactic rules) and those whose assessment requires [[human]] [[Judgment (decision making)|judgement]] (semantic rules). The boundary is drawn with [[mathematical]] precision by [[Rice's theorem]], which establishes that all non-trivial [[Semantics|semantic]] properties of [[Computer program|programs]] are [[Undecidable problem|undecidable]], while [[Syntax (programming languages)|syntactic]] properties -- those concerning a program's textual structure rather than its behaviour -- remain decidable.<ref>{{Cite journal |last=Rice |first=H. G. |date=1953 |title=Classes of recursively enumerable sets and their decision problems |journal=Transactions of the American Mathematical Society |volume=74 |issue=2 |pages=358–366 |doi=10.2307/1990888}}</ref>

The concept has applications in [[software governance]], [[regulatory compliance]], [[automated auditing]], and [[AI governance]], where it determines what can and cannot be delegated to automated assessment.

== Theoretical foundations ==

=== Rice's theorem ===

[[Rice's theorem]] (1953) states that every non-trivial semantic property of programs is undecidable. A '''semantic property''' concerns the program's [[behaviour]] -- its input-output function, [[Termination analysis|termination characteristics]], [[Side effect (computer science)|side effects]] -- as opposed to a '''syntactic property''', which concerns the program's textual structure. The theorem is a generalisation of the [[undecidable problem|undecidability]] of the [[halting problem]].<ref>{{Cite web |title=Rice's theorem |url=https://en.wikipedia.org/wiki/Rice%27s_theorem |access-date=2026-03-20}}</ref>

For governance, Rice's theorem establishes that the fundamental governance question -- "does this component do what it should?" -- is [[algorithm]]ically undecidable in the general case. No automated system can correctly determine, for all possible inputs, whether a given component satisfies a non-trivial behavioural specification.

=== Tarski's undefinability theorem ===

[[Tarski's undefinability theorem]] (1933) shows that [[truth]] for a sufficiently strong [[formal system]] cannot be defined within the system itself. The resolution requires a hierarchy of [[metalanguage]]s: truth for language ''L'' can be defined only in a richer metalanguage ''L''&prime; that contains ''L'' as a proper part.<ref>{{Cite book |last=Tarski |first=Alfred |date=1933 |title=Pojęcie prawdy w językach nauk dedukcyjnych |trans-title=The Concept of Truth in Formalized Languages |location=Warsaw}}</ref>

Applied to governance, Tarski's theorem implies that a governance layer that evaluates other components cannot fully evaluate itself using the same evaluative framework. Evaluation of the evaluator requires a higher-order perspective.

=== The halting problem ===

The [[halting problem]], proved undecidable by [[Alan Turing]] in 1936, is the foundational result underlying Rice's theorem. It establishes that no general algorithm can determine whether an arbitrary program will eventually halt or run forever.<ref>{{Cite journal |last=Turing |first=A. M. |date=1936 |title=On Computable Numbers, with an Application to the Entscheidungsproblem |journal=Proceedings of the London Mathematical Society |series=2 |volume=42 |pages=230–265 |doi=10.1112/plms/s2-42.1.230}}</ref> The governance implication is that [[termination analysis|termination]] -- a basic behavioural property -- cannot be verified automatically for arbitrary components.

== The boundary in practice ==

=== Syntactic properties (automatically verifiable) ===

Properties that lie on the syntactic (decidable) side of the boundary include:

* '''Naming convention compliance''' -- whether identifiers follow a specified pattern (e.g., [[Naming convention (programming)|camelCase]], specific prefix conventions)
* '''Schema conformance''' -- whether a configuration file conforms to a [[JSON Schema]] or [[XML schema]]
* '''Dependency acyclicity''' -- whether the [[dependency graph]] among components is [[Directed acyclic graph|acyclic]]
* '''Type checking''' -- whether a program satisfies the rules of its [[type system]] (in [[statically typed]] languages)
* '''[[Lint (software)|Linting]]''' -- whether source code satisfies a set of structural style rules
* '''Structural completeness''' -- whether required files, fields, or sections are present

These properties concern the ''structure'' of governance artifacts, not their ''behaviour'' or ''purpose''.

=== Semantic properties (requiring human judgement) ===

Properties that lie on the semantic (undecidable) side include:

* '''Fitness for purpose''' -- whether a component actually achieves its intended goal
* '''Architectural coherence''' -- whether a component's design is appropriate within the larger system
* '''Correctness''' -- whether a program produces the right output for all inputs (a non-trivial semantic property per Rice's theorem)
* '''Ethical alignment''' -- whether a system's behaviour is consistent with specified values
* '''Quality''' -- whether code, documentation, or governance artifacts meet qualitative standards beyond structural conformance
* '''Security''' (in the general case) -- whether a system is free of all [[Vulnerability (computing)|vulnerabilities]] (equivalent to proving behavioural properties)

These properties concern ''behaviour'', ''purpose'', and ''value'' -- domains where [[automated reasoning]] confronts fundamental limits.

== Applications ==

=== Software governance ===

In [[software engineering]], the syntactic-semantic boundary determines the scope of [[continuous integration|automated CI/CD checks]]. [[Static program analysis|Static analysis]] tools, [[Lint (software)|linters]], [[Type system|type checkers]], and schema validators operate on the syntactic side. [[Code review]], [[Design review|architectural review]], and [[fitness function]]s that require human interpretation operate on the semantic side. The boundary explains why fully automated [[software quality]] assessment is impossible in principle: the most important quality properties (correctness, fitness for purpose) are semantic and therefore undecidable.

=== Regulatory compliance ===

In [[regulatory compliance]], the boundary distinguishes between rules that can be checked by [[audit software]] (e.g., "does the annual report contain the required sections?") and rules that require [[auditing|human auditors]] (e.g., "do the financial statements present a true and fair view?"). The observation that regulatory frameworks persistently require human auditors despite advances in automation reflects the mathematical impossibility identified by Rice's theorem, not merely a technological limitation.

=== AI governance ===

In [[AI governance]], the boundary has particular significance because [[artificial intelligence|AI systems]] may exhibit [[Opacity (software)|constitutive opacity]] -- behaviour that is not fully explainable even by their designers. The boundary implies that governance of AI systems can automate the verification of syntactic properties (model architecture compliance, data format conformance, documentation completeness) but cannot automate the verification of semantic properties (fairness, [[explainability]], alignment with human values).

== Relationship to approximate methods ==

The syntactic-semantic boundary is absolute in the theoretical sense established by Rice's theorem: no algorithm can correctly decide any non-trivial semantic property for all programs. However, practical [[static analysis]] and [[formal verification]] techniques provide useful ''approximations'':

* [[Abstract interpretation]] computes [[conservative approximation]]s of semantic properties (always overestimating or always underestimating).
* [[Model checking]] verifies semantic properties for finite-state systems or bounded executions.
* [[Testing]] provides empirical evidence about semantic properties without guaranteeing coverage.
* [[Formal verification]] proves semantic properties for specific programs under specific conditions, without contradicting Rice's theorem (which concerns decidability for ''all'' programs).

These approximations do not cross the syntactic-semantic boundary; they provide useful but incomplete information about properties that remain fundamentally undecidable in the general case.

== See also ==

* [[Rice's theorem]]
* [[Halting problem]]
* [[Tarski's undefinability theorem]]
* [[Static program analysis]]
* [[Decidability (logic)]]
* [[Semantics]]
* [[Syntax (programming languages)]]
* [[Formal verification]]
* [[Automated auditing]]
* [[Goodhart's law]]

== References ==
{{Reflist}}

{{DEFAULTSORT:Syntactic-semantic boundary (governance)}}
[[Category:Theory of computation]]
[[Category:Governance]]
[[Category:Software engineering]]
[[Category:Computability theory]]
[[Category:Automated auditing]]
```

### Suggested categories

- [[Category:Theory of computation]]
- [[Category:Governance]]
- [[Category:Software engineering]]
- [[Category:Computability theory]]
- [[Category:Automated auditing]]

### Existing Wikipedia articles to link to/from

**Link to (from this article):**
- [[Rice's theorem]]
- [[Halting problem]]
- [[Tarski's undefinability theorem]]
- [[Static program analysis]]
- [[Formal verification]]
- [[Abstract interpretation]]
- [[Model checking]]
- [[Decidability (logic)]]
- [[Lint (software)]]
- [[Type system]]
- [[Continuous integration]]
- [[Code review]]
- [[AI governance]]
- [[Regulatory compliance]]

**Link from (add links in these articles pointing to this article):**
- [[Rice's theorem]] -- add to "Applications" or "See also"
- [[Static program analysis]] -- mention the boundary concept in context
- [[Goodhart's law]] -- the boundary concept explains *where* Goodhart effects are strongest (semantic side)

### Notability assessment

**Lower risk than Article 1, but still moderate.** The syntactic-semantic distinction as applied to program properties is well-established (Rice's theorem has its own Wikipedia article). The novel contribution here is the explicit framing as a *governance* boundary -- the claim that this computability-theoretic result has direct implications for organizational governance design.

1. The article draws heavily on existing notable concepts and could be seen as an applied-context expansion of [[Rice's theorem]].
2. **Alternative strategy:** Rather than a standalone article, this content could be proposed as a new section ("Applications to governance") in the existing [[Rice's theorem]] article or as an expansion of the [[Static program analysis]] article's discussion of fundamental limits. This would face a much lower notability bar.
3. If published as a standalone article, it would benefit from citations to the software engineering literature on the limits of automated analysis (e.g., papers on the limits of static analysis tools, the irreducible need for human code review).
4. The connection to AI governance provides timeliness -- the question of what can and cannot be automated in AI governance is an active policy discussion.

**Risk level:** MODERATE as standalone. LOW if framed as a section addition to [[Rice's theorem]] or [[Static program analysis]].

---

## Article 3: Triadic Review Protocol (proposed section for existing articles)

### Verification

Searched Wikipedia for "triadic review protocol" on 2026-03-20. No article or section exists. The concept is novel to the SGO research program (SOP-001). Related existing articles:
- [[Peer review]] -- well-developed article on the general concept
- [[Inter-rater reliability]] -- statistical requirements for agreement among raters
- [[Triangulation (social science)]] -- combining multiple methods/observers for validity

### Proposed addition

This is better suited as a **proposed section addition** to the [[Peer review]] or [[Triangulation (social science)]] article rather than a standalone article. The concept is too niche for its own article and would likely be tagged for deletion under [[WP:NOTABILITY]].

### Option A: Section for [[Peer review]] article

**Proposed section title:** "Minimum reviewer count and structural integrity"

```wikitext
=== Minimum reviewer count and structural integrity ===

Research in [[inter-rater reliability]] establishes that a minimum of three independent raters is required for reliable [[intraclass correlation coefficient|intraclass correlation]] (ICC) estimates.<ref>{{Cite book |last1=Shrout |first1=Patrick E. |last2=Fleiss |first2=Joseph L. |date=1979 |title=Intraclass Correlations: Uses in Assessing Rater Reliability |journal=Psychological Bulletin |volume=86 |issue=2 |pages=420–428 |doi=10.1037/0033-2909.86.2.420}}</ref> This psychometric minimum has structural implications for peer review design: review by a single reviewer produces potential [[confirmation bias|echo]], review by two reviewers produces binary agreement or disagreement (thesis and antithesis without [[Thesis, antithesis, synthesis|synthesis]]), while review by three or more reviewers enables [[Triangulation (social science)|triangulation]] -- structural integrity through non-redundant coverage of the subject matter.

The distinction parallels findings in [[social science]] methodology, where [[Triangulation (social science)|triangulation]] -- the combination of multiple observers, theories, or methods to study the same phenomenon -- is used to overcome the weaknesses inherent in single-method, single-observer studies.<ref>{{Cite book |last=Denzin |first=Norman K. |date=1978 |title=The Research Act: A Theoretical Introduction to Sociological Methods |edition=2nd |publisher=McGraw-Hill |isbn=0-07-016365-5}}</ref> In review contexts, three perspectives create a minimum viable [[triangulation]] structure: areas of agreement across all three reviewers indicate high-confidence findings, areas of disagreement indicate the most valuable signals for revision, and areas where reviewers surface new directions indicate opportunities for expansion.

This three-reviewer minimum is reflected in the practices of many [[Academic journal|academic journals]], [[grant review]] panels, and [[dissertation committee]]s, which typically require three or more reviewers for substantive assessments. The structural rationale -- that three perspectives provide the minimum for non-redundant triangulation -- complements the [[Statistical power|statistical]] rationale from inter-rater reliability research.

When constituting review panels, the effectiveness of the three-reviewer structure depends on '''non-redundancy''': the reviewers should bring distinct disciplinary perspectives, methodological expertise, or evaluative stances. Three reviewers from the same discipline applying the same criteria provide redundancy rather than triangulation. Effective panel constitution assigns complementary roles -- for example, one reviewer sympathetic to the work's aims (identifying what it does well and how to strengthen it), one adversarial (identifying where and how it fails), and one orthogonal (identifying what adjacent considerations the work overlooks).<ref name="sgo-sop001">{{Cite thesis |last=<!-- Author --> |title=Triadic Review Protocol |date=2026 |type=Standard Operating Procedure |series=Studium Generale ORGANVM Research Program, SOP-001}}</ref>

This stance-distribution approach draws on [[Charles Sanders Peirce|Peirce]]'s [[Semiotic theory of Charles Sanders Peirce#Triadic structure|triadic sign model]] (sign, object, interpretant) and the broader epistemological argument that knowledge claims are most robustly tested when subjected to perspectives that are not merely different in degree but different in kind.<ref>{{Cite book |last=Peirce |first=Charles Sanders |date=1903 |title=Collected Papers |volume=2 |chapter=Speculative Grammar}}</ref>
```

### Option B: Section for [[Triangulation (social science)]] article

**Proposed section title:** "Triangulation in review and evaluation"

```wikitext
=== Triangulation in review and evaluation ===

The triangulation principle extends from research methodology to [[peer review]] and evaluation practices. Just as combining multiple research methods overcomes the weaknesses of single-method studies, combining multiple reviewer perspectives overcomes the weaknesses of single-reviewer assessment.

The minimum structure for triangulation in review contexts requires three non-redundant perspectives. Two perspectives create a binary dynamic -- agreement or disagreement -- that maps onto debate (thesis versus antithesis) rather than triangulation. The addition of a third perspective transforms the dynamic: areas of three-way agreement indicate robust findings, two-against-one patterns indicate areas requiring further examination, and novel directions surfaced by any single reviewer become candidates for expansion rather than dismissal.

This structural observation is supported by the [[inter-rater reliability]] literature, which establishes that a minimum of three independent raters is needed for reliable [[intraclass correlation coefficient|intraclass correlation]] estimates.<ref>{{Cite journal |last1=Shrout |first1=Patrick E. |last2=Fleiss |first2=Joseph L. |date=1979 |title=Intraclass Correlations: Uses in Assessing Rater Reliability |journal=Psychological Bulletin |volume=86 |issue=2 |pages=420–428 |doi=10.1037/0033-2909.86.2.420}}</ref> The effectiveness of the three-reviewer minimum depends on selecting reviewers whose expertise, disciplinary background, or evaluative stance provides genuine non-redundancy, rather than redundant application of identical criteria.
```

### Suggested categories (if standalone, which is not recommended)

- [[Category:Peer review]]
- [[Category:Research methodology]]
- [[Category:Psychometrics]]

### Existing Wikipedia articles to link to/from

**Link to (from proposed sections):**
- [[Inter-rater reliability]]
- [[Triangulation (social science)]]
- [[Intraclass correlation coefficient]]
- [[Peer review]]
- [[Confirmation bias]]
- [[Charles Sanders Peirce]]
- [[Statistical power]]

**Link from (if section additions are accepted):**
- The sections themselves create the links. No external articles need to be modified.

### Notability assessment

**Not notable as a standalone article.** The Triadic Review Protocol is a specific methodological procedure from a single research programme. It would not survive [[WP:NOTABILITY]] as a standalone Wikipedia article.

However, the *underlying principle* -- that three non-redundant perspectives provide a minimum structural integrity threshold for review, grounded in inter-rater reliability requirements and triangulation theory -- is well-supported by existing literature and is a legitimate contribution to the [[Peer review]] or [[Triangulation (social science)]] articles.

**Recommended strategy:**
1. Do NOT create a standalone "Triadic Review Protocol" article. It will be flagged for deletion.
2. Propose the section addition to [[Peer review]] (Option A) or [[Triangulation (social science)]] (Option B) via the article's Talk page.
3. Frame the addition around the well-sourced psychometric and methodological literature (Shrout & Fleiss, Denzin, ICC requirements), not around the SGO programme's specific protocol.
4. The SGO-specific protocol can be cited as one example of the principle in practice, but the section should stand on the broader methodological literature.

**Risk level:** LOW for section additions grounded in existing literature. HIGH for standalone article.

---

## Summary of publication strategy

| Article | Format | Risk | Prerequisites |
|---------|--------|------|---------------|
| Governance trilemma | Standalone article | HIGH before publication; MODERATE after arXiv | Publish SYN-02 on arXiv; ideally obtain one independent citation |
| Syntactic-semantic boundary | Standalone or section addition | MODERATE standalone; LOW as section | Cite existing software engineering literature on static analysis limits |
| Triadic Review Protocol | Section addition only | LOW as section | Frame around Shrout & Fleiss, Denzin, ICC literature |

**Recommended sequence:**
1. Publish SYN-02 on arXiv (provides citable source for governance trilemma).
2. Add brief mention of governance trilemma to [[Trilemma]] article's examples list (low bar, gets the concept indexed).
3. Propose section addition for triadic review to [[Peer review]] Talk page (well-sourced, low risk).
4. Propose section addition for syntactic-semantic boundary to [[Rice's theorem]] or [[Static program analysis]] (well-sourced, low risk).
5. After SYN-02 receives at least one independent citation, create the standalone governance trilemma article.
