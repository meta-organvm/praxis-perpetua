---
trp_id: TRP-RP-06
venture: SGO-2026-RP-006
title: "The Fourfold Correspondence: Grammar, Automaton, Type, and Proof from Chomsky to Curry-Howard-Lambek"
domain_signature: [formal languages, type theory, linguistics]
triad:
  pov_1:
    field: type theory
    role: Theorist
    discipline: Type theory / Curry-Howard
    stance: sympathetic
  pov_2:
    field: linguistics
    role: Empiricist
    discipline: Corpus linguistics
    stance: adversarial
  pov_3:
    field: HCI / developer experience
    role: Practitioner
    discipline: HCI / Programming language design
    stance: orthogonal
date: 2026-03-20
stage: "COMPOSITION (Stage 2 TRP Gate)"
---

# Triadic Review Protocol: RP-06 -- The Fourfold Correspondence

---

## POV 1 Review: Type Theorist / Curry-Howard Specialist / Sympathetic

### Summary Assessment

This paper makes a genuinely ambitious structural claim -- that the Chomsky hierarchy admits a fourfold extension through types and proofs -- and substantiates it with carefully assembled formal parallels. The context-free / recursive algebraic type level is precise and convincing. The weaker levels of the correspondence, however, need tighter formal scaffolding: the paper currently oscillates between claiming an isomorphism and claiming an analogy, and the distinction matters enormously for the contribution's durability.

### Primary Mode: Amendment

The central thesis -- that grammars, automata, types, and proofs are four projections of a single mathematical structure -- is well-motivated and the paper marshals the right technical traditions (Lambek calculus, Curry-Howard, DisCoCat) to support it. But as a sympathetic reader who knows these formalisms, I have specific amendments that would strengthen the formal claims substantially.

**1. The grammar-type correspondence needs stratified precision claims.** The paper repeatedly asserts that the fourfold correspondence "holds" at each level, but the nature of the correspondence varies dramatically. At Type 2, we have a genuine constructive isomorphism: BNF grammars and recursive algebraic types are the same mathematical object. At Type 1, we have a structural analogy between context-sensitivity in rewriting and context-dependency in typing (System F, refinement types). At Type 0, we have a correspondence between two forms of undecidability. These are not the same kind of relationship. The paper acknowledges this in Section 4.5 and Section 8, but the acknowledgment comes too late and is too soft. I recommend that the paper introduce, early in Section 1, an explicit three-tier classification of correspondence strength -- *isomorphism*, *structural embedding*, and *analogy* -- and classify each level's correspondence accordingly. This would preempt the most damaging objection (that the paper conflates proof with suggestion) while preserving the bold thesis.

**2. The Type 1 / parametric polymorphism mapping requires a sharper formal argument.** The claim that context-sensitive grammars correspond to System F is the weakest link in the chain. Context-sensitivity means that the applicability of a rewriting rule depends on the surrounding string; parametric polymorphism means that a term's type depends on how its type variables are instantiated. These are both "context-dependent" in a loose sense, but the precise connection is not established. Does every CSG have a natural encoding as a System F typing problem? Can type-checking in System F be reduced to CSG membership? The paper gestures toward these questions but does not attempt even a sketch proof. A concrete worked example -- encoding the language {a^n b^n c^n} as a System F typing problem -- would dramatically strengthen this section.

**3. The mildly context-sensitive gap deserves a conjecture.** The paper identifies the MCS gap as the central open problem but stops short of proposing a candidate type system. Given the paper's own observation that CCG corresponds to combinatory logic, and that MCS languages correspond to embedded pushdown automata, I would expect the paper to conjecture that the corresponding type system is something like a *restricted second-order system* -- perhaps a fragment of System F with bounded polymorphism, or a linear type system with controlled structural rules. The paper has the technical sophistication to propose such a conjecture; its absence is a missed opportunity. Even a wrong conjecture would advance the field more than a correct identification of the gap.

**4. The Curry-Howard table in Section 5.1 should be extended to the fourfold case.** The paper presents the standard Curry-Howard dictionary (logic/computation) and the Lambek extension (computation/category theory), then separately introduces the grammatical column. A single consolidated four-column table at this point -- showing the correspondence across all four dimensions at each of the four Chomsky levels -- would be the paper's signature contribution. This table exists in embryonic form in Section 2.6 but does not include the proof-theoretic column. Completing it would make the contribution immediately legible.

**5. The proof-theoretic dimension is underdeveloped.** The paper's title promises "Grammar, Automaton, Type, and Proof," but the proof-theoretic column receives substantially less attention than the other three. Which proof calculus corresponds to each Chomsky level? Propositional logic to Type 3? First-order logic to Type 2? Second-order logic to Type 1? Higher-order logic to Type 0? The paper implies this mapping but does not develop it. Since the Curry-Howard correspondence relates types and proofs bijectively, the proof-theoretic column should be derivable from the type-theoretic column -- but this derivation should be made explicit rather than left to the reader.

### Secondary Observations

**Expansion.** The paper's treatment of HoTT (Section 6.1) is brief but tantalizing. If types are spaces and proofs are paths, then the fourfold correspondence gains a topological dimension: grammatical derivations would correspond to paths in a space of types. This could connect to the "higher-dimensional grammar" programme of Mellies/Burroni. I encourage developing this into a full subsection or flagging it as a concrete future direction rather than a parenthetical aside.

**Amendment.** The discussion of decidability preservation (Section 1, final paragraph of the introduction) claims that decidability properties are "preserved across all four dimensions." This claim needs qualification: type-checking in System F is decidable, but type *inference* in System F is undecidable (Wells, 1999, which the paper cites in Section 7.1). The decidability landscape is more nuanced than "preserved across all four dimensions" suggests.

**Critique.** The paper treats the Lambek calculus as generating context-free languages, which is correct for the product-free calculus (Pentus, 1997 -- notably absent from the references). But the full Lambek calculus with product generates a larger class. This distinction matters for the fourfold mapping and should be addressed.

### Verdict

- [ ] Advance as-is
- [x] Advance with amendments (listed above)
- [ ] Revise and re-review
- [ ] Fork: alternative path recommended

### Inter-POV Questions

**To POV 2 (Corpus Linguist):** The paper's linguistic examples (Swiss German cross-serial dependencies, Turkish vowel harmony, English phrase structure) are all well-known textbook cases. From your empirical perspective, do these examples adequately represent the *range* of natural language phenomena, or are they cherry-picked to fit the hierarchy cleanly? Are there well-documented phenomena that would actively *resist* placement in the fourfold correspondence?

**To POV 3 (HCI Researcher):** The paper argues that the grammar-type parallel has implications for programming language design (Section 7.1). From a practitioner's standpoint, do language designers actually think in terms of Chomsky levels when making type-system decisions? Is the fourfold correspondence producing *new* design insights, or is it a post-hoc rationalisation of decisions made on other grounds?

---

## POV 2 Review: Corpus Linguist / Empiricist / Adversarial

### Summary Assessment

This paper constructs an impressive formal architecture, but its linguistic foundations are built on a dangerously narrow empirical base. The natural language examples are drawn almost exclusively from English, German, and a handful of well-worn non-English cases (Swiss German cross-serial dependencies, Turkish vowel harmony, Bambara reduplication). For a paper claiming to illuminate the structural essence of natural language, the absence of typological breadth is a serious weakness. Furthermore, the paper's treatment of natural language implicitly adopts a generativist framing that corpus linguistics has long challenged on empirical grounds.

### Primary Mode: Critique

The paper's central move -- extending the Chomsky hierarchy with type-theoretic and proof-theoretic columns -- rests on a premise that the Chomsky hierarchy is itself an adequate model of natural language complexity. I challenge this premise on several empirical grounds.

**1. The Chomsky hierarchy is a poor empirical fit for natural language.** The paper acknowledges (Section 2.5) that natural language is "mildly context-sensitive," occupying an interstitial position between Type 2 and Type 1. But it does not grapple with the more fundamental critique: the Chomsky hierarchy classifies languages by the *form of their rewriting rules*, a criterion that privileges constituency structure over other structural dimensions (dependency, construction, information structure, discourse) that are equally or more important for characterizing natural language. Construction Grammar (Goldberg, 1995, 2006 -- not cited), Cognitive Grammar (Langacker, 1987, 2008 -- not cited), and usage-based approaches (Bybee, 2010 -- not cited) reject the premise that natural language structure is best described by formal grammars at all. The paper's entire architecture stands on generativist assumptions that are contested within linguistics itself.

**2. The linguistic examples are cherry-picked for formal tractability.** Every linguistic example in the paper is chosen because it maps cleanly onto a Chomsky level: phonotactic constraints are regular, phrase structure is context-free, Swiss German cross-serial dependencies are context-sensitive. But natural language is full of phenomena that resist clean classification:

- *Gradience in acceptability.* Grammaticality is not binary. Corpus data consistently shows gradient acceptability judgments (Bresnan, 2007; Lau et al., 2017). The sentence "Who did you wonder whether saw Mary?" is degraded but not flatly ungrammatical. Type systems are binary (well-typed or not); grammaticality is gradient. This is not a peripheral problem -- it undermines the entire parsing-as-type-checking metaphor.

- *Frequency effects.* High-frequency constructions are processed differently from low-frequency constructions, even when they have identical formal structure (Bybee, 2006). The corpus frequency of a construction affects its acceptability, productivity, and processing cost. No type system has a notion of "type frequency" that would capture this.

- *Constructional idioms.* Constructions like "the X-er, the Y-er" ("The bigger they are, the harder they fall") have idiosyncratic syntax that is productive but not derivable from general phrase-structure rules (Fillmore, Kay, and O'Connor, 1988). These are attested, frequent, and typologically widespread, but they do not fit any single Chomsky level. They are partially productive (unlike frozen idioms) but partially fixed (unlike fully compositional syntax).

- *Multiword expressions.* Corpus studies consistently find that a large proportion of natural language production consists of multiword expressions -- prefabricated chunks that are stored and retrieved holistically rather than generated compositionally (Wray, 2002). Estimates range from 30% to 80% of running text. If a third or more of natural language is non-compositional, then the compositionality assumption underlying the entire fourfold correspondence (Section 5.5) is not a minor caveat -- it is a gaping empirical hole.

**3. The cross-linguistic evidence is inadequate.** The paper's claim is universal -- it asserts a correspondence that should hold for *all* natural languages. But the linguistic evidence comes overwhelmingly from English and other well-studied European languages. Where is the evidence from:

- *Polysynthetic languages* (Mohawk, Inuktitut, Chukchi), where a single "word" can express what English requires an entire sentence for? The Chomsky hierarchy presupposes a distinction between words and sentences that polysynthetic morphology blurs.

- *Tonal languages* (Mandarin, Yoruba), where suprasegmental features carry lexical and grammatical information not captured by string rewriting?

- *Sign languages* (ASL, BSL), which have simultaneous rather than sequential structure -- multiple articulators operating in parallel -- that challenges the fundamental assumption that language is a string over a finite alphabet?

- *Free word-order languages* (Warlpiri, Latin, Japanese), where the linear order of constituents is largely independent of syntactic structure? The Lambek calculus and pregroup grammars are inherently order-sensitive (the directional slashes $/$, $\backslash$ encode word order). How does the fourfold correspondence work for languages where word order is pragmatically rather than syntactically determined?

**4. The treatment of Shieber (1985) is uncritical.** The paper treats Shieber's Swiss German result as a settled fact ("Shieber proved [this] is not context-free"), but the interpretation of this result is more contested than the paper acknowledges. Pullum and Gazdar (1982) had earlier argued that the evidence for non-context-freeness was weak, and subsequent work (Michaelis and Kracht, 1997) showed that the formal argument depends on specific assumptions about the analysis of Swiss German that are themselves debatable. This does not invalidate the MCS hypothesis, but it does illustrate the paper's tendency to treat contested linguistic claims as established facts when they support the formal architecture.

**5. The transformer probing results are over-interpreted.** Section 6.4 suggests that transformers may learn type-theoretic structure, citing probing studies (Hewitt and Manning, 2019; Goldberg, 2019). But the probing methodology has been challenged: probing classifiers may find structure in random representations simply because the probes themselves are powerful enough to learn the task (Hewitt and Liang, 2019 -- not cited; Pimentel et al., 2020 -- not cited). The paper should acknowledge the *control* problem in probing: the question is not whether a probe can extract syntactic information from a transformer, but whether the transformer *encodes* that information in a way that differs from chance.

### Secondary Observations

**Amendment.** If the paper retains its focus on formal rather than functional/cognitive approaches to language, it should at minimum acknowledge the existence of non-generativist alternatives and explain why the fourfold correspondence is framed within a generativist paradigm. A section on "scope and limitations" that addresses Construction Grammar, usage-based approaches, and the gradient/probabilistic nature of real grammaticality would significantly strengthen the paper's scholarly credibility.

**Expansion.** Interestingly, there is one domain where the paper's framework might actually gain empirical traction: *computational* languages (programming languages, formal specification languages, configuration formats). These are genuinely formal, genuinely compositional, genuinely binary in well-formedness, and genuinely hierarchically organized. The paper could strengthen its contribution by focusing more explicitly on the computational domain, where the fourfold correspondence is exact, rather than stretching it to cover natural language, where the fit is approximate at best.

### Verdict

- [ ] Advance as-is
- [ ] Advance with amendments (listed above)
- [x] Revise and re-review
- [ ] Fork: alternative path recommended

### Inter-POV Questions

**To POV 1 (Type Theorist):** You advocate for the fourfold correspondence. Can you point to a type-theoretic account of gradient grammaticality? If grammaticality is not binary but scalar, does the type-theoretic metaphor survive? Are there "almost well-typed" programs in a meaningful sense?

**To POV 3 (HCI Researcher):** From a developer-experience standpoint, do you find it plausible that programming language users would benefit from knowing that their type system corresponds to a level of the Chomsky hierarchy? Is this "nice to know" or "actionable"?

---

## POV 3 Review: HCI Researcher / Developer Experience Practitioner / Orthogonal

### Summary Assessment

This paper presents a theoretically rich architecture connecting four domains of formal structure, but never convincingly answers the practitioner's fundamental question: *so what should I do differently?* The implications section (Section 7) gestures at programming language design, NLP engineering, and governance system architecture, but offers heuristics rather than design methods. For a paper that claims practical consequences, the gap between theory and actionable guidance is the central weakness.

### Primary Mode: Expansion

My primary contribution is not a critique of what the paper says, but an identification of what it fails to develop: the design implications that would make the fourfold correspondence *useful* rather than merely *true* (or approximately true).

**1. The "design for the weakest sufficient level" principle needs operationalization.** Section 7.1 argues that language designers should choose the weakest type-system level that suffices, mirroring the principle that compilers stratify by Chomsky level. This is sound advice, but it is advice that every experienced language designer already follows intuitively. The paper needs to go further: *how do you determine what level suffices?* What features of a domain or problem push a type system from one level to the next? The paper should provide a decision procedure or at least a decision tree:

- Does your domain require recursive data structures? -> You need at least Type 2 (algebraic types).
- Does your domain require code reuse across types? -> You need at least Type 1 (polymorphism).
- Does your domain require types that depend on runtime values? -> You need Type 0 (dependent types), with the associated cost of potential non-termination.

A concrete taxonomy like this, derived from the fourfold correspondence, would be the paper's most cited contribution among practitioners.

**2. Error messages and the type-grammar correspondence.** One of the most impactful applications of the grammar-type parallel is in *error reporting*. When a parser encounters a syntax error, it can often provide a helpful message because the context-free grammar provides structural expectations ("expected ')' to close '('"). When a type-checker encounters a type error, the message is often opaque because the type system is more complex than a CFG. The grammar-type correspondence suggests a research direction: can we improve type error messages by exploiting the structural parallel with grammar errors? If type-checking is parsing in a type-level grammar, then parser error-recovery techniques (Burke and Fisher, 1987; Corchuelo et al., 2002) might be adaptable to type-error recovery. The paper does not explore this direction, but it is precisely the kind of practical payoff that would make the theoretical contribution matter to developers.

**3. The cognitive cost of type-system levels is unaddressed.** From an HCI perspective, the most important property of a type system is not its decidability or expressiveness but its *cognitive cost to the user*. Each level of the type-system hierarchy imposes different cognitive demands:

- Finite types (enumerations): trivial to understand. Cognitive cost is near-zero.
- Recursive algebraic types: require understanding recursion, which is a well-documented cognitive barrier (Kahney, 1983; Levy, 2001). But once understood, pattern matching provides a strong mental model.
- Parametric polymorphism: requires reasoning about type variables -- "for all types T" -- which adds a layer of abstraction. Studies of Java generics adoption (Parnin et al., 2013) show that many developers avoid generics or use them incorrectly.
- Dependent types: require reasoning about the *values* that types depend on, blurring the phase distinction between compile-time and run-time. The cognitive cost is high: even experienced functional programmers find dependent types challenging (Brady, 2013).

The fourfold correspondence would gain significant practical value if it incorporated cognitive complexity as a fifth dimension. The Chomsky hierarchy already has a complexity-theoretic dimension (O(n) to undecidable); adding a *human* complexity dimension would make it a genuine design tool rather than a taxonomic exercise.

**4. The governance application (Section 7.4) is the most actionable implication, but it is underdeveloped.** The observation that governance rules form a grammar and that their decidability depends on their Chomsky level is genuinely useful for system architects. But the section is only one page long and provides no concrete examples. A worked case study -- classifying the rules of a real governance system (Kubernetes RBAC, AWS IAM, or the paper's own ORGANVM system) by Chomsky level and demonstrating the decidability implications -- would transform this from an observation into a method.

**5. The paper ignores tooling.** A language's type system does not exist in isolation; it exists within an ecosystem of tools: IDEs, linters, language servers, refactoring tools, code generators. The fourfold correspondence predicts that the *quality of tooling* should correlate with the Chomsky level of the type system: languages with simpler type systems should admit more complete and more reliable tool support. Is this empirically true? Do languages with Type 2 type systems (ML, Haskell without extensions) have better IDE support than languages with Type 0 type systems (Haskell with type families, Agda, Lean)? A brief empirical survey would ground the theoretical claim in developer experience reality.

### Secondary Observations

**Amendment.** The paper's claim that "parsing is type-checking" (Section 4.2) is a compelling formal statement, but from a developer's perspective it obscures an important difference: parsing errors are typically *local* (you can point to the character where the parse fails), while type errors are often *non-local* (the error manifests far from the code that causes it). This locality difference has profound implications for developer experience and is not captured by the formal correspondence. The paper should acknowledge this.

**Critique.** The DisCoCat / quantum NLP material (Section 5.6) reads as a diversion from the paper's main argument. It is intellectually interesting, but the practical relevance of running NLP models on current quantum hardware is approximately zero. A practitioner reading this section will ask: "Is this useful for anything I will build in the next decade?" The honest answer is no. The section should be shortened or moved to an appendix.

### Verdict

- [ ] Advance as-is
- [x] Advance with amendments (listed above)
- [ ] Revise and re-review
- [ ] Fork: alternative path recommended

### Inter-POV Questions

**To POV 1 (Type Theorist):** You want the formal claims to be tighter. I want the practical implications to be more concrete. Is there a version of the fourfold correspondence that is both formally precise *and* actionable as a design tool? Or does formalizing it necessarily abstract away the features that matter for practice?

**To POV 2 (Corpus Linguist):** You challenge the paper's treatment of natural language. If we bracket natural language entirely and focus the paper on *formal/computational* languages, does the paper become stronger? Or does restricting the scope undermine the intellectual ambition that makes the contribution interesting?

---

# TRP Synthesis

## Agreement Map (High-Confidence Findings)

All three POVs agree on the following:

1. **The context-free / recursive algebraic type correspondence is the paper's strongest claim.** The isomorphism between BNF grammars and recursive algebraic types is constructive, precise, and well-established. All three reviewers regard this as solid and uncontested.

2. **The Type 1 (context-sensitive / parametric polymorphism) correspondence is the weakest link.** POV 1 identifies the lack of a formal argument connecting CSGs to System F. POV 2 notes that the linguistic evidence for context-sensitivity is more contested than the paper acknowledges. POV 3 observes that the cognitive jump from Type 2 to Type 1 is significant but unanalyzed.

3. **The mildly context-sensitive gap is genuinely important.** All three reviewers agree that identifying the type-theoretic characterization of MCS languages is a significant open problem. POV 1 urges a conjecture; POV 2 questions whether the Chomsky hierarchy is the right framework for natural language at all; POV 3 notes that MCS languages are the level where practical NLP operates.

4. **The paper's scope claim exceeds its evidence.** The paper claims relevance to natural language, programming languages, NLP, and governance systems. All three reviewers find the evidence adequate for the formal-languages / PL-theory core but thin for the extended applications (natural language, governance).

5. **Section 5.5 (where the correspondence breaks down) is the most intellectually honest section.** All reviewers appreciate that the paper identifies its own limitations, but all also argue that these limitations are more serious than the paper's framing suggests. Ambiguity, non-compositionality, and gradience are not peripheral issues -- they characterize the majority of natural language use.

## Disagreement Map (Most Valuable Signals)

| Issue | POV 1 (Sympathetic) | POV 2 (Adversarial) | POV 3 (Orthogonal) |
|-------|---------------------|---------------------|---------------------|
| **Is the generativist framing appropriate?** | Yes, with refinements. The Chomsky hierarchy is the right substrate for the formal investigation. | No. The hierarchy privileges constituency over other structural dimensions and is empirically inadequate for natural language. | Pragmatically acceptable for the PL-theory audience, but the paper should acknowledge alternatives. |
| **Should the paper cover natural language?** | Yes, but with more careful hedging about where the correspondence holds only approximately. | Only if it engages seriously with empirical linguistics (gradient acceptability, typological diversity, multiword expressions). Otherwise, restrict scope. | The paper would be stronger if it focused on formal/computational languages and treated natural language as a speculative extension. |
| **Is DisCoCat/quantum NLP relevant?** | Yes -- it is the most concrete modern realization of the categorical dimension. | Neutral -- it is formally interesting but linguistically untested on real corpora. | No -- it has no practical relevance and distracts from the actionable implications. |
| **Should the paper propose a conjecture for the MCS gap?** | Strongly yes. Even a wrong conjecture advances the field. | Only if it is grounded in linguistic evidence, not just formal elegance. | Only if the conjecture has practical implications for parser/type-checker design. |

## Expansion Inventory

New directions surfaced by the reviews:

1. **Type-theoretic gradient grammaticality** (POV 2 challenge to POV 1). Can fuzzy type theory, probabilistic type theory, or graded type systems model the gradient acceptability judgments attested in corpus data? This would bridge the gap between the binary well-typedness of formal type systems and the scalar grammaticality of natural language.

2. **Error message improvement via grammar-type parallel** (POV 3). Parser error-recovery techniques applied to type-error recovery, exploiting the structural correspondence between syntax errors and type errors.

3. **Cognitive complexity as a fifth dimension** (POV 3). A human-complexity hierarchy paralleling the computational-complexity hierarchy: O(trivial) for finite types, through significant cognitive overhead for parametric polymorphism, to the high barrier of dependent types.

4. **Governance rule classification** (POV 3). Worked case study of a real governance system (Kubernetes RBAC, AWS IAM, or ORGANVM) classified by Chomsky level with decidability implications made concrete.

5. **Topological extension via HoTT** (POV 1). If types are spaces and proofs are paths, then grammatical derivations are paths in a space of types, connecting to higher-dimensional grammar.

6. **Computational language focus** (POV 2 / POV 3 convergence). The paper would be strongest if its primary domain were formal/computational languages, with natural language treated as a conjectured extension rather than a settled application.

## Resolution

| Pattern | Assessment |
|---------|-----------|
| POV 1 (Sympathetic) | Advance with amendments |
| POV 2 (Adversarial) | Revise and re-review |
| POV 3 (Orthogonal) | Advance with amendments |

**Resolution per protocol (2/3 advance with amendments, 1 revise):** This falls between "2/3 advance, 1 amend" and "1/3 advance, 2 revise." The adversarial reviewer's concerns are serious but addressable within revision rather than requiring fundamental restructuring. The resolution is:

**Advance with amendments, incorporating POV 2's core critiques as revisions.**

The paper does not need to abandon its generativist framing or its natural-language ambitions, but it must:

1. Acknowledge and engage with non-generativist alternatives (Construction Grammar, usage-based approaches) rather than ignoring them.
2. Add typological breadth to the linguistic examples (polysynthetic languages, tonal languages, free word-order languages).
3. Explicitly address gradient grammaticality and the proportion of non-compositional language use as challenges to the correspondence rather than footnotes.
4. Qualify the cross-linguistic scope claims.

## Amendments Required

### Priority 1 (Must address before advancing to CANDIDATE)

| # | Amendment | Source POV | Section Affected |
|---|-----------|-----------|-----------------|
| A1 | Introduce explicit three-tier classification of correspondence strength (isomorphism / structural embedding / analogy) and classify each Chomsky level accordingly. | POV 1 | Section 1 (Introduction), Section 4.5 |
| A2 | Provide a concrete worked example encoding {a^n b^n c^n} as a System F typing problem, or explicitly acknowledge that this encoding is not known and that the Type 1 correspondence is conjectural. | POV 1 | Section 2.3, Section 4.5 |
| A3 | Add a scope-and-limitations section addressing gradient grammaticality, non-compositionality (citing multiword expression statistics), and the existence of non-generativist frameworks (Construction Grammar, usage-based linguistics). | POV 2 | New section or expanded Section 8 |
| A4 | Expand linguistic examples to include at least one polysynthetic language, one free word-order language, and one sign language, discussing how each challenges or supports the fourfold correspondence. | POV 2 | Sections 2.1--2.4 |
| A5 | Develop the proof-theoretic column explicitly: state which proof calculus corresponds to each Chomsky level and present the full four-column, four-row correspondence table. | POV 1 | Section 5, new consolidated table |

### Priority 2 (Should address; strengthens the paper significantly)

| # | Amendment | Source POV | Section Affected |
|---|-----------|-----------|-----------------|
| A6 | Propose a concrete conjecture for the type-theoretic characterization of MCS languages, even if speculative. | POV 1 | Section 4.5, Section 9 |
| A7 | Add a decision-tree or taxonomy for language designers: which domain requirements push a type system to which Chomsky level? | POV 3 | Section 7.1 |
| A8 | Acknowledge the locality difference between parse errors and type errors, and the implications for developer experience. | POV 3 | Section 7.1 or 7.2 |
| A9 | Add the Pentus (1997) result (Lambek calculus generates context-free languages) to the references and address it in the Lambek calculus discussion. | POV 1 | Section 4.1 |
| A10 | Acknowledge the probing methodology critique (Hewitt and Liang, 2019; Pimentel et al., 2020) in the transformer discussion. | POV 2 | Section 6.4 |

### Priority 3 (Optional; would enrich the contribution)

| # | Amendment | Source POV | Section Affected |
|---|-----------|-----------|-----------------|
| A11 | Expand the governance application (Section 7.4) with a worked case study of a real governance system. | POV 3 | Section 7.4 |
| A12 | Develop the HoTT connection to higher-dimensional grammar as a full subsection rather than a parenthetical. | POV 1 | Section 6.1 |
| A13 | Shorten or relocate the quantum NLP material to an appendix. | POV 3 | Section 5.6 |
| A14 | Add a brief discussion of cognitive complexity as a dimension parallel to computational complexity. | POV 3 | Section 7 (new subsection) |
| A15 | Address the missing citations: Construction Grammar (Goldberg 1995, 2006), Cognitive Grammar (Langacker 1987, 2008), usage-based approaches (Bybee 2006, 2010), probing controls (Hewitt & Liang 2019, Pimentel et al. 2020), Pentus (1997). | POV 2 / POV 1 | References, throughout |

---

*Review conducted under the Triadic Review Protocol (TRP), SOP SGO-2026-SOP-001.*
*Venture stage: COMPOSITION (Stage 2 TRP Gate).*
*Resolution: Advance with amendments. 15 amendments identified across 3 priority tiers.*
