---
trp_id: TRP-SYN-01
venture: SGO-2026-SYN-001
title: "The Architecture of Formal Meaning"
venture_type: Paper (Dissertation synthesis)
venture_status: LOCAL (first draft)
domain_signature: [category theory, formal semantics, NLP]
date: 2026-03-20
triad:
  pov_1:
    field: category theory
    role: Theorist
    discipline: Category theory / abstract algebra
    stance: sympathetic
  pov_2:
    field: NLP
    role: Practitioner / Empiricist
    discipline: Distributional semantics / computational linguistics
    stance: adversarial
  pov_3:
    field: philosophy of science
    role: Critic
    discipline: Philosophy of science / epistemology
    stance: orthogonal
---

# Triadic Review Protocol: SYN-01 -- The Architecture of Formal Meaning

**Venture:** SGO-2026-SYN-001 -- *The Architecture of Formal Meaning: A Categorical Framework for Unifying Grammar, Semantics, and Computation*

**Domain Signature:** `[category theory, formal semantics, NLP]`

**Dependencies:** RP-01 (The Semantics Bridge), RP-06 (Chomsky to Computation)

---

## POV 1 Review: Theorist / Category Theory / Sympathetic

### Summary Assessment

This is an ambitious and largely well-executed synthesis that correctly identifies the functorial perspective as the natural language for unifying compositional semantics across traditions. The mathematical instincts are sound -- meaning-as-functor, compositionality-as-functoriality, the naturality of rule-to-rule correspondence -- and the paper succeeds in assembling a coherent architectural picture from disparate sources. Where the work needs strengthening is in the precision of its categorical claims: several constructions are sketched at a level that invites challenge from specialists, and the central five-way correspondence table needs formal underpinning to distinguish it from an extended analogy.

### Primary Mode: Amendment

The categorical framework is on the right track, but several claims need tightening to withstand scrutiny from the category theory community.

**1. The functor F: Syn -> Sem needs a more careful type-theoretic specification.** The paper treats "the syntactic category" and "the semantic category" as if each tradition provides a single, canonical category. In practice, the choice of category is not unique and carries significant consequences. For logical semantics, is **Sem** the category **Set** (classical), the effective topos (constructive), or the category of Kripke presheaves (modal)? For programming language semantics, is it **Dom** (domains with continuous functions), **CPO** (complete partial orders), or the Kleisli category of an appropriate monad? The paper acknowledges this multiplicity in passing (Section 3.1, where three choices are listed for PL semantics) but does not confront its implications for the unification claim. If the semantic category is not canonical, then the "unified functorial passage" is actually a *family* of functorial passages, and the unification claim must be restated: the claim is that there is a *schema* of functors F: Syn -> Sem, parametrised by the choice of semantic category, and that this schema has a uniform categorical description. This reformulation is stronger, not weaker, than the current claim, but it requires the machinery of indexed categories or fibred categories to make precise. I recommend the paper adopt this fibrational perspective explicitly.

**2. The compact closed structure deserves more careful handling.** The paper correctly identifies that pregroup grammars and **FdVect** are both compact closed (or rather, rigid) categories, and that DisCoCat exploits this shared structure. But the paper elides a subtle point: pregroup grammars form *rigid* categories (non-symmetric compact closed), while **FdVect** is *symmetric* compact closed. The DisCoCat functor therefore maps from a non-symmetric structure to a symmetric one, which means it cannot be fully faithful -- it must collapse some distinctions that the grammar makes (specifically, the distinction between left and right adjoints, which are identified in a symmetric setting). This is not a fatal objection, but it should be acknowledged and discussed: the "loss of word-order information" in DisCoCat models of sentences like "dog bites man" vs. "man bites dog" is preserved only because the word *tensors* (not the types) differ. The structural preservation is weaker than the paper suggests.

**3. The topos-theoretic section is the most promising and the least developed.** The presheaf perspective on contextual meaning is genuinely novel in the context of a unified architecture, and the connection between sheaf gluing and discourse coherence is beautiful. But the section remains entirely programmatic. I would like to see at least one worked example: take a specific discourse phenomenon (say, anaphora resolution across sentences, or presupposition accommodation), specify the category of contexts C, define the presheaf, and show that the sheaf condition captures the desired coherence property. Without such an example, the topos-theoretic component is a promissory note rather than a contribution.

**4. The five-way correspondence table (Section 4.2) should be accompanied by a commutative diagram.** The table is suggestive but static. A diagram showing the functors between the five columns -- and especially the natural transformations that mediate between different semantic interpretations of the same syntactic structure -- would make the architecture visually precise. I have in mind something like a pentagonal diagram with Syn at the top and four semantic categories (model-theoretic, domain-theoretic, distributional, proof-theoretic) at the vertices of the base, with functors connecting them and natural transformations witnessing their coherence. This diagram would be the paper's central visual contribution.

**5. Adjunctions are underused.** The paper mentions adjunctions (the residuation in the Lambek calculus, the unit-counit of compact closure) but does not systematically exploit the adjunction concept. Many of the "bridges" in RP-01 can be characterised as adjunctions: the relationship between syntax and semantics is often not just a functor but a pair of adjoint functors (a "free" construction going from semantics to syntax, and a "forgetful" functor going from syntax to semantics, or vice versa). The adequacy and full abstraction results in denotational semantics, for example, can be formulated as conditions on the adjunction between syntactic and semantic categories. A systematic treatment of adjunctions would elevate the architecture from "functors between categories" to "adjunctions between categories," which is a significantly richer structure.

### Secondary Observations

**Expansion.** The paper's treatment of monadic enrichment for compositionality failures (Section 3.2, on Moggi's monads for exceptions, state, etc.) is suggestive but could be extended in a direction the author may not have considered: *graded monads* (Katsumata 2014) provide a framework for tracking the *degree* of non-compositionality. A graded monad T indexed by a monoid M assigns to each "grade" m in M a transformation T_m, and composition of graded effects follows the monoid structure. Applied to the semantic architecture, this would allow a formal quantification of how far a given construction departs from pure compositionality -- precisely the kind of metric that would address the "where does the architecture fail?" question with mathematical precision rather than hand-waving.

**Expansion.** The connection to categorical quantum mechanics (Section 3.6) could be pushed further by noting that the ZX-calculus (Coecke and Duncan 2011), which provides a complete diagrammatic language for qubit quantum mechanics, has been adapted to natural language processing in the lambeq framework. This suggests a *tricategorical* perspective: grammar, meaning, and quantum computation form a triangle of compact closed categories with functors between them, and the question of whether this triangle "commutes" is a concrete, testable prediction of the architecture.

### Verdict

- [ ] Advance as-is
- [x] Advance with amendments (listed above)
- [ ] Revise and re-review
- [ ] Fork: alternative path recommended

### Inter-POV Questions

**To POV 2 (Distributional Semanticist):** The paper claims that DisCoCat "resolves, or at least addresses" the tension between distributional and compositional semantics. From your empirical perspective, does the DisCoCat resolution actually *work* on real NLP tasks, or is it a mathematically elegant framework that fails to compete with architectures (transformers) that ignore categorical structure entirely? What would constitute adequate empirical evidence that the functorial perspective captures something real about language, rather than merely redescribing compositional intuitions in categorical notation?

**To POV 3 (Philosopher of Science):** My amendments aim to make the categorical claims more precise. But does increased precision address the "redescription vs. genuine unification" concern, or does it merely make the redescription more rigorous? Is there a principled criterion that distinguishes a genuinely unifying theory from a merely encompassing notation?

---

## POV 2 Review: Practitioner-Empiricist / Distributional Semantics & NLP / Adversarial

### Summary Assessment

The paper constructs an impressive theoretical edifice, but from the standpoint of someone who builds systems that process language at scale, the edifice floats above its empirical foundations. The central claim -- that meaning is functorial passage from syntax to semantics -- is either trivially true (any structure-preserving map is a functor, so what have we learned?) or substantively false (real language processing does not decompose into the clean syntactic-category-to-semantic-category pipeline the paper describes). The paper's treatment of distributional semantics and transformers, while more informed than most formal-semantics papers, still fundamentally mischaracterises the state of the art and understates the severity of the challenge that neural methods pose to the entire categorical programme.

### Primary Mode: Critique

**1. DisCoCat has not scaled. Period.** The paper treats DisCoCat as the key bridge between categorical and distributional semantics, but it avoids confronting the empirical record honestly. DisCoCat models have been tested on small-scale sentence similarity tasks (Grefenstette and Sadrzadeh 2011; Kartsaklis et al. 2012) and compositional tasks involving simple transitive sentences. On these restricted benchmarks, DisCoCat sometimes matches or slightly outperforms additive baselines. But these are toy benchmarks by the standards of modern NLP. DisCoCat has not been demonstrated on tasks like:

- Machine translation at scale (WMT benchmarks)
- Open-domain question answering (Natural Questions, TriviaQA)
- Summarisation (CNN/DailyMail, XSum)
- Dialogue (MultiWOZ, PersonaChat)
- Any task requiring reasoning over paragraphs, not just single sentences

The paper's claim that DisCoCat "demonstrates that reconciliation is *feasible*" is misleading. It demonstrates that reconciliation is feasible for two-word or three-word phrases consisting of subject-verb-object triples. That is not reconciliation; that is a proof of concept that has not progressed beyond the concept stage in over fifteen years.

**2. The paper mischaracterises what transformers learn.** Section 5.3 says transformers "do not directly implement compositional semantics" and frames this as a limitation of transformers. But from the NLP perspective, this is backwards: it is a limitation of the *theory of compositionality*. If a system can translate between languages, answer questions about complex texts, generate coherent multi-paragraph prose, and do zero-shot reasoning -- all without implementing the categorical architecture -- then the burden of proof falls on the architecture to explain what it adds, not on the system to explain why it does not implement the architecture.

The probing studies the paper cites (Hewitt and Manning 2019; Clark et al. 2019) show that transformers *do* encode syntactic structure, but in a distributed, continuous, contextual form that looks nothing like the discrete types and derivations of categorial grammar. The paper treats this as evidence that transformers are "compatible" with the categorical framework. A more honest reading is that transformers have found a *different* way to capture the same underlying regularities -- a way that is more flexible, more robust, and more empirically successful than the categorical way. The question is not whether transformers can be forced into a categorical mould, but whether the categorical mould captures anything that transformers do not already capture better.

**3. The "structure vs. mechanism" distinction is a dodge.** Section 5.3 concludes that "the categorical architecture describes the *structure* of meaning; transformers implement a *mechanism* for computing meaning," and presents this as a complementary relationship. But this distinction only holds if the "structure" described by the architecture is actually the structure of the phenomenon, rather than the structure of a particular theoretical tradition's way of describing the phenomenon. If transformers can compute meaning without implementing categorical structure, then categorical structure is a property of certain *theories* of meaning, not a property of meaning itself. The paper needs to address this possibility directly rather than defining it away.

**4. The paper ignores the multimodal revolution.** Modern language models are increasingly multimodal: they process images, audio, video, and text jointly. CLIP, Flamingo, GPT-4V, Gemini -- these systems ground language in perception in ways that the categorical architecture does not address. Section 5.4 mentions "grounded meaning" briefly, but the treatment is perfunctory. The multimodal challenge is severe for the categorical programme: if meaning is grounded in perception and action, then the "semantic category" is not **Set** or **FdVect** but something much richer -- a category of sensorimotor representations, perhaps -- and the functorial passage from syntax to this category has not been defined, let alone shown to be uniform across traditions.

**5. The ORGANVM application section (Section 6) undermines the paper's claims.** The paper applies the categorical architecture to a specific software system (ORGANVM), interpreting schema contracts as syntactic categories and registry operations as functors. This is presented as a practical vindication of the architecture. But the application is *trivial*: any structured data transformation system can be described in categorical terms (categories are, after all, just a general theory of structured transformations). The fact that ORGANVM's governance rules can be described as functors does not validate the claim that meaning is functorial; it validates only the claim that category theory is a general-purpose mathematical language -- which is not in dispute, but is also not interesting.

**6. Where are the novel empirical predictions?** A unifying theory should generate predictions that the component theories do not generate individually. The paper identifies the five-way correspondence (Section 4.2) as going beyond RP-01 and RP-06, but the five-way table adds a "semantics" column to the existing four-way table without generating predictions that could be tested. What experiment would *falsify* the five-way correspondence? What linguistic phenomenon would, if observed, show that the categorical architecture is wrong rather than merely incomplete? Without falsifiable predictions, the architecture is unfalsifiable -- and an unfalsifiable theory, no matter how elegant, contributes nothing to empirical science.

### Secondary Observations

**Amendment.** If the paper wants to engage seriously with the NLP community, it should include a concrete experimental proposal. For example: take a set of compositional phenomena that DisCoCat handles well (subject-verb-object composition, adjective-noun modification) and a set that it handles poorly (negation, quantification, long-distance dependencies), and compare DisCoCat models, transformer models, and hybrid models on each. Report accuracy, scalability (how performance changes with vocabulary size and sentence length), and interpretability (can you extract the categorical structure from the trained model?). This would transform the paper from a philosophical argument into an empirical research programme.

**Amendment.** The paper should acknowledge more directly that the "reconciliation frontier" (Section 5.4) is not a frontier at all from the NLP perspective -- it is the entire landscape. The formal-categorical tradition occupies a small, well-understood corner; the neural-distributional tradition occupies everything else. A paper claiming unification should not describe the neural tradition as a "challenge" to the formal tradition; it should describe the formal tradition as a "special case" of whatever the neural tradition is converging toward.

**Expansion.** One genuinely interesting direction the paper does not pursue: can we use the categorical framework to *improve* transformers? If the functorial structure captures real regularities, then architectures that explicitly encode this structure (e.g., transformers with type-driven attention patterns, or architectures where composition follows grammatical derivation) should outperform standard transformers on tasks requiring compositional generalisation (COGS, SCAN, gSCAN). There is some evidence for this (Lake and Baroni 2018; Kim and Linzen 2020), and connecting it to the categorical framework would be a genuine contribution.

### Verdict

- [ ] Advance as-is
- [ ] Advance with amendments (listed above)
- [x] Revise and re-review
- [ ] Fork: alternative path recommended

### Inter-POV Questions

**To POV 1 (Category Theorist):** You recommend making the categorical claims more precise with fibred categories, graded monads, and commutative diagrams. But will increased mathematical sophistication address the fundamental objection -- that the architecture has no empirical purchase? Is there a version of the categorical framework that makes *different* predictions from those a competent linguist would make without categories?

**To POV 3 (Philosopher of Science):** My core concern is falsifiability. Is there a reading of this paper under which it makes falsifiable claims? Or is the functorial perspective inherently unfalsifiable -- a framework rather than a theory -- in which case, what are the criteria for evaluating frameworks (as distinct from theories)?

---

## POV 3 Review: Critic / Philosophy of Science / Orthogonal

### Summary Assessment

This dissertation undertakes what it calls a "unification" of three traditions of formal semantics under a categorical framework. The mathematical craftsmanship is competent, and the synthesis of RP-01 and RP-06 is genuinely useful as a map of the intellectual landscape. But the central question -- whether this constitutes *genuine unification* or merely *redescription at a higher level of abstraction* -- is the question the paper most urgently needs to answer, and it is the question it least adequately addresses. The paper acknowledges the concern (Section 7, "abstraction cost") but treats it as a worry to be noted rather than an objection to be met. This review argues that the unification-vs-redescription question is not a peripheral concern but the load-bearing issue, and that the paper's failure to resolve it undermines the central claim.

### Primary Mode: Critique

**1. The paper does not provide an adequate criterion for genuine unification.**

The history of science offers clear cases of genuine unification: Maxwell's unification of electricity and magnetism, the Weinberg-Salam unification of electromagnetism and the weak force, Darwin's unification of biogeography and paleontology under natural selection. Each of these unifications has distinctive features:

- **Novel predictions.** Maxwell's equations predicted electromagnetic waves before they were observed. The electroweak theory predicted the W and Z bosons. A genuine unification generates predictions that neither component theory generates alone.

- **Explanatory deepening.** After unification, phenomena that were previously brute facts become explained. Electricity and magnetism are not merely *described* by the same equations; they are *explained* as aspects of a single field. Biogeographic patterns are not merely *catalogued* but *explained* by common descent and selection.

- **Ontological reduction (or identification).** Genuine unification typically involves identifying entities: electromagnetic waves *are* light; genes *are* segments of DNA. The identification is not merely notational but substantive -- it tells us something about the world, not just about our descriptions.

Now measure the paper's "categorical unification" against these criteria:

- **Novel predictions.** The paper does not identify a single prediction generated by the categorical framework that is not already generated by one of the component traditions. The five-way correspondence (Section 4.2) is a *restatement* of known correspondences (Curry-Howard-Lambek + Montague) in tabular form, not a derivation of new results. The paper's own candidate for a novel prediction -- that DisCoCat can bridge distributional and formal semantics -- predates the paper and is borrowed from Coecke et al. (2010), not derived from the unification.

- **Explanatory deepening.** Does the categorical framework *explain* why compositionality holds across traditions, or does it merely *describe* the fact that it does? The paper asserts that "compositionality *is* functoriality" (Section 3.2), but this identification runs in the wrong direction for explanation. Functoriality is a mathematical property of structure-preserving maps between categories. To say that compositionality is functoriality is to say that the property we already knew about (compositionality) has a name in category theory (functoriality). This is *translation*, not *explanation*. An explanation would answer the question: *why* is meaning compositional? The categorical framework does not answer this question; it merely provides an elegant mathematical language for *stating* that meaning is compositional.

- **Ontological identification.** The paper does not claim that proofs *are* programmes *are* morphisms in any substantive ontological sense; it claims that they *correspond* to each other via structure-preserving maps. But correspondence and identity are different things. Maxwell's unification claims that light *is* an electromagnetic wave -- not that there exists a structure-preserving map from optics to electrodynamics. The Curry-Howard *correspondence* is named correctly: it is a correspondence, not an identification. And a correspondence, no matter how tight, is not a unification in the scientific sense unless it underwrites novel predictions or explanatory deepening.

**2. The "almost tautological" concession is devastating.**

The paper makes a revealing concession in Section 3.1: "The claim that meaning is a functor asserts that there is a syntactic category **Syn** and a semantic category **Sem**, and that meaning assignment is a functor F: **Syn** -> **Sem**. This claim, once stated, is almost tautological -- it merely says that meaning is a structure-preserving map."

The paper tries to rescue the claim from tautology by saying "its force lies in the identification of what the 'structure' is that is being preserved." But this rescue is insufficient. The identification of the relevant structure is precisely what RP-01 and RP-06 already accomplished: RP-01 identified eight structural bridges; RP-06 identified the fourfold correspondence. The categorical architecture *packages* these identifications in categorical language but does not *extend* them. The "force" of the claim is the force of the prior results, dressed in new notation.

This is precisely what philosophers of science call **Procrustean unification**: forcing disparate phenomena into a common framework by describing them in sufficiently abstract terms, without thereby gaining explanatory or predictive power. Category theory, by virtue of being the most abstract branch of mathematics, is especially susceptible to Procrustean deployment. Any two mathematical structures can be related by a functor (at minimum, a constant functor); any two functors can be related by a natural transformation. The question is always: does the categorical description add something beyond what was already known in the domain-specific terms?

**3. The paper conflates mathematical generality with scientific unification.**

There is a fundamental distinction between:

(a) **Scientific unification:** discovering that two apparently different phenomena are manifestations of the same underlying process, and

(b) **Mathematical generalisation:** finding a mathematical framework sufficiently abstract to encompass two different formalisms as instances.

The paper pursues (b) and presents it as (a). Category theory provides the mathematical generalisation: all three traditions of semantics instantiate the pattern "functor from syntactic category to semantic category." But this is generalisation, not unification. Unification would require showing that the three traditions are manifestations of the *same underlying process* -- that there is a single phenomenon called "meaning" whose behaviour is described by the categorical architecture. The paper asserts this ("the three traditions are three perspectives on a single subject") but the assertion is not supported by the evidence marshalled. The evidence shows that the three traditions share mathematical structure; it does not show that they share subject matter.

Consider an analogy. Groups appear in crystallography, particle physics, and music theory. One could construct a "categorical unification" of these three domains by noting that each involves a group acting on a set, and that the action functor from the group (viewed as a one-object category) to **Set** captures the shared structure. Would this constitute a genuine unification of crystallography, particle physics, and music? Obviously not. The shared mathematical structure (groups acting on sets) is a reflection of the *mathematics*, not of the *phenomena*. Crystallography, particle physics, and music share no underlying process; they merely share a mathematical pattern.

The paper needs to argue -- and the argument would be difficult -- that the case of formal semantics is *different* from the group-theory analogy. It needs to argue that the three traditions of semantics are not merely three domains that happen to use similar mathematics, but three investigations of a *single phenomenon* (meaning) that the categorical architecture reveals to be unified. This argument would require engaging with the philosophy of meaning in a way the paper currently does not: it would require a substantive account of what meaning *is*, beyond the formal characterisation as "functorial passage."

**4. The boundary conditions reveal the limits of the "unification."**

The paper is commendably honest about the boundary conditions of the architecture: pragmatics, non-compositionality, neural representations, concurrency, and embodied meaning all fall outside its scope (Section 4.4). But the paper does not confront the implication of these boundary conditions for the unification claim.

If the architecture applies only to "the classical, compositional, typed core" of each tradition, then what has been unified is not "meaning" but "the compositional fragment of meaning." This is significant, but it is not the grand unification advertised. The title says "The Architecture of Formal Meaning" -- but formal meaning *includes* dynamic meaning (Heim, Kamp, Groenendijk and Stokhof), game-theoretic meaning (Hintikka, Abramsky), inferential meaning (Brandom, Prawitz), and probabilistic meaning (Goodman and Frank). These are formal, mathematically rigorous approaches to meaning that fall outside or at the boundary of the architecture. The paper should either broaden its claim to include these approaches (which would require substantial additional work) or narrow its title and thesis to match the actual scope of the result.

I would suggest a title like "The Architecture of Compositional Meaning" or "The Functorial Core of Formal Semantics" -- something that signals that the result concerns the compositional fragment, not meaning in its full range.

**5. What would genuine unification look like?**

If the paper's approach falls short of genuine unification, what would genuine unification look like? I submit that genuine unification of the three semantic traditions would require at least one of the following:

(a) **A novel phenomenon predicted by the unified framework.** For example: if the categorical architecture predicts that a certain compositional pattern must exist in natural language because it exists in programming language semantics and the functor requires it, and this prediction is then *confirmed* by linguistic data, that would be strong evidence of genuine unification.

(b) **An impossibility result derivable only from the unified framework.** For example: if the categorical architecture proves that a certain kind of semantic system is impossible -- that you cannot have property X and property Y simultaneously -- and this impossibility is confirmed across all three traditions, that would show the framework has predictive power beyond any single tradition.

(c) **A practical consequence.** If the categorical architecture enables the construction of a system that *works better* than systems built without the categorical perspective -- better NLP, better programming language design, better logical reasoning -- that would be evidence that the architecture captures something real.

The paper should explicitly address what would count as evidence of genuine unification, and should acknowledge that its current evidence -- the structural parallels documented in RP-01 and RP-06 -- constitutes evidence of *shared mathematical structure* but not yet evidence of *genuine unification* in the philosophy-of-science sense.

### Secondary Observations

**Amendment.** The paper should engage with Kitcher's (1981) account of explanatory unification ("Explanatory Unification," *Philosophy of Science*). Kitcher argues that unification is a matter of reducing the number of independent explanatory patterns: a unified theory explains many phenomena using few argument patterns, while a disunified collection uses many. By Kitcher's criterion, the paper's architecture achieves some unification (the functorial pattern replaces multiple independent descriptions of compositionality), but the degree of unification is modest (the pattern was already implicit in the Curry-Howard-Lambek correspondence; the paper's contribution is to make it explicit and add the semantic column).

**Amendment.** The paper should also engage with Morrison's (2000) *Unifying Scientific Theories* and her distinction between *theoretical unification* (what Maxwell achieved) and *reductive unification* (what Weinberg-Salam achieved). The paper's categorical architecture is arguably a case of *structural unification* -- a third kind, in which the unifying element is a mathematical structure rather than a theoretical principle or an ontological reduction. Structural unification is legitimate but weaker than theoretical or reductive unification: it shows that the domains share a pattern, not that they share a cause or a substrate. Making this distinction explicit would strengthen the paper by replacing an overblown claim ("genuine unification") with a precise and defensible one ("structural unification via shared categorical architecture").

**Expansion.** There is an interesting parallel with the Erlangen Programme (Klein 1872), which "unified" geometries by characterising each as the study of invariants under a specific transformation group. This is widely regarded as a genuine (if partial) unification, yet it is precisely the kind of "structural unification" the paper pursues: it shows that different geometries share a common mathematical schema (group action on a space) without claiming that Euclidean geometry and hyperbolic geometry are "the same subject." The paper could strengthen its claims by positioning itself relative to the Erlangen Programme and arguing for the value of structural unification as a legitimate (if not maximal) form of theoretical achievement.

### Verdict

- [ ] Advance as-is
- [ ] Advance with amendments (listed above)
- [x] Revise and re-review
- [ ] Fork: alternative path recommended

### Inter-POV Questions

**To POV 1 (Category Theorist):** You recommend several mathematical enrichments (fibred categories, graded monads, adjunctions). But do these enrichments bring the paper closer to genuine unification, or do they merely make the redescription more elaborate? Is there a mathematical result that *could* be proved within the categorical framework that would constitute a genuinely novel prediction -- something that would surprise a semanticist who does not know category theory?

**To POV 2 (Distributional Semanticist):** You argue that the paper needs empirical predictions. But is the right response to demand that the categorical framework compete with transformers on NLP benchmarks, or is there a different kind of empirical test -- perhaps a cognitive or psycholinguistic one -- that would be a fairer test of the claim that meaning has compositional structure? After all, the categorical architecture claims to describe the *structure* of meaning, not the *mechanism* of language processing, so perhaps the right tests are ones that probe structure rather than processing efficiency.

---

## TRP Synthesis

### Agreement Map (High-Confidence Findings)

All three POVs agree on the following:

1. **The synthesis of RP-01 and RP-06 is a genuine contribution.** The paper successfully maps the overlap and divergence between the two prior works and assembles them into a coherent picture. The literature survey and the historical narrative are solid.

2. **The mathematical craftsmanship is competent.** The paper handles the categorical concepts correctly (with caveats from POV 1 about the symmetric/non-symmetric distinction in compact closure and the need for more careful type specification of the semantic categories).

3. **The paper's greatest weakness is its failure to distinguish genuine unification from redescription.** All three POVs, from different angles, converge on this point. POV 1 notes that the categorical claims need formal strengthening. POV 2 notes that the framework makes no empirical predictions. POV 3 makes the philosophical case directly: the paper achieves structural generalisation, not scientific unification, and does not provide adequate criteria for distinguishing the two.

4. **The DisCoCat treatment is overoptimistic.** POV 1 notes the symmetric/non-symmetric subtlety. POV 2 notes the failure to scale. POV 3 notes that DisCoCat's existence as a bridge does not constitute evidence of genuine unification. All three agree the paper needs a more honest assessment of DisCoCat's empirical record and limitations.

5. **The boundary conditions (Section 4.4) are honestly stated but insufficiently integrated into the thesis.** The paper acknowledges that pragmatics, neural representations, concurrency, and embodied meaning fall outside the architecture, but continues to claim "the architecture of formal meaning" rather than "the architecture of compositional formal meaning." All three POVs agree the scope claim should be narrowed to match the actual scope of the result.

### Disagreement Map (Most Valuable Signals)

1. **On the value of increased mathematical precision (POV 1 vs. POV 2 and POV 3).** POV 1 recommends enriching the framework with fibred categories, graded monads, and adjunctions. POV 2 argues that increased mathematical sophistication misses the point: the framework needs empirical grounding, not more abstraction. POV 3 questions whether precision addresses or exacerbates the redescription concern. This is the central tension of the paper and cannot be resolved by the paper alone -- it reflects a genuine methodological disagreement between mathematical, empirical, and philosophical approaches to the study of meaning.

   **Resolution recommendation:** The paper should pursue both precision *and* empirical engagement, but with different timelines. The immediate revision should include the mathematical tightenings recommended by POV 1 (particularly the careful specification of the semantic category and the symmetric/non-symmetric issue) and the philosophical engagement recommended by POV 3 (particularly the criteria for genuine unification and the engagement with Kitcher and Morrison). The empirical programme recommended by POV 2 (benchmarking DisCoCat against transformers on compositional tasks) should be identified as the primary direction for future work -- it is too substantial to be incorporated into the present paper but should be framed as the essential next step.

2. **On the status of transformers (POV 2 vs. POV 1 and POV 3).** POV 2 treats the success of transformers as a challenge to the relevance of the entire categorical programme. POV 1 treats transformers as an interesting implementation detail. POV 3 treats them as one data point in the philosophy-of-science question. This disagreement is genuine and productive: the paper must address the transformer challenge more directly than it currently does, without either dismissing transformers (as the current draft tends to) or conceding that they render the categorical programme obsolete (as POV 2 implies).

   **Resolution recommendation:** The paper should adopt the framing that POV 2's expansion suggests: use the categorical framework to generate *hypotheses about transformer behaviour* that can be empirically tested. For example: the categorical architecture predicts that compositional and non-compositional phenomena should be processed differently by transformers (since only the former fall within the functorial framework). Probing studies could test this prediction. This would give the categorical framework empirical traction without requiring it to compete with transformers on NLP benchmarks.

3. **On the ORGANVM application (POV 2 vs. POV 1).** POV 2 argues that the ORGANVM application is trivial and undermines the paper's claims. POV 1 does not address this section. The disagreement reflects different standards: POV 2 demands that applications demonstrate non-trivial predictive power; POV 1 is content with mathematical illustration. The ORGANVM section should either be removed (it is tangential to the theoretical argument) or substantially strengthened (with a concrete example where the categorical perspective reveals a system design error or suggests an improvement that would not have been obvious without the framework).

### Expansion Inventory

1. **Graded monads for quantifying non-compositionality** (POV 1). A genuinely novel direction that could generate testable predictions about the degree of compositionality in different linguistic constructions.

2. **The ZX-calculus / tricategorical perspective** (POV 1). Connects the architecture to quantum NLP and could generate experimental predictions testable on quantum hardware.

3. **Worked topos-theoretic example** (POV 1). A concrete application of presheaf semantics to discourse coherence would transform the topos section from programmatic to substantive.

4. **Hybrid categorical-neural architectures** (POV 2). Using the categorical framework to design improved neural architectures for compositional generalisation -- a concrete research programme with testable outcomes.

5. **Engagement with Kitcher and Morrison** (POV 3). Positioning the result as "structural unification" within the philosophy-of-science literature on unification would sharpen the claims and make them defensible.

6. **Erlangen Programme analogy** (POV 3). A powerful framing device that would help the paper articulate precisely what kind of unification it achieves.

### Fork Analysis

No POV recommended a fork. The project direction is sound; the concerns are about execution, precision, and intellectual honesty about the scope and nature of the achievement.

### Aggregate Verdict

| POV | Verdict | Condition |
|-----|---------|-----------|
| POV 1 (Category Theorist) | Advance with amendments | Tighten categorical claims, add diagrams, develop topos example |
| POV 2 (Distributional Semanticist) | Revise and re-review | Address empirical gap, reassess DisCoCat claims, engage transformers seriously |
| POV 3 (Philosopher of Science) | Revise and re-review | Resolve unification-vs-redescription with explicit criteria, narrow scope claim |

**Resolution per protocol (1 advance, 2 revise): Revise and re-review.**

The paper should return to COMPOSITION stage for targeted revision addressing these priorities:

### Revision Priorities (Ordered)

1. **[Critical -- POV 3]** Add a section (or substantially expand Section 7) explicitly engaging with the philosophy of unification. Provide criteria for genuine unification vs. redescription. Position the result as *structural unification* (akin to the Erlangen Programme) and argue for the value of this kind of achievement while being honest about its limitations relative to theoretical or reductive unification. Engage with Kitcher (1981) and Morrison (2000).

2. **[Critical -- All POVs]** Narrow the scope claim. The paper unifies the *compositional, typed core* of formal semantics -- not "formal meaning" in its full range. Adjust the title, abstract, and conclusion accordingly.

3. **[Critical -- POV 2]** Provide an honest assessment of DisCoCat's empirical record. Acknowledge the scaling failure. Reframe DisCoCat as a proof of *categorical concept* rather than a practical bridge between traditions.

4. **[Important -- POV 1]** Tighten the categorical claims: specify semantic categories carefully, address the symmetric/non-symmetric distinction, add the pentagonal diagram, develop at least one worked topos-theoretic example.

5. **[Important -- POV 2]** Frame testable predictions. Identify specific hypotheses about transformer behaviour that follow from the categorical architecture and could be tested via probing studies or compositional generalisation benchmarks.

6. **[Desirable -- POV 1]** Explore graded monads for quantifying non-compositionality. This is the most promising novel direction for extending the framework.

7. **[Desirable -- POV 3]** Either remove the ORGANVM application section or strengthen it with a non-trivial example where the categorical perspective reveals something that domain-specific analysis would miss.

---

*TRP executed 2026-03-20. Single-model review (Claude Opus 4.6). For full inter-model triangulation, re-execute POV 2 with an empirically-oriented model and POV 3 with a model trained on philosophy-of-science literature.*
