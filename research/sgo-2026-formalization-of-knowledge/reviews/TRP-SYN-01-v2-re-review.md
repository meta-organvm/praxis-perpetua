---
trp_id: TRP-SYN-01-v2
venture: SGO-2026-SYN-001
title: "The Architecture of Compositional Formal Meaning"
venture_type: Paper (Dissertation synthesis)
venture_status: LOCAL (revised draft v2)
domain_signature: [category theory, formal semantics, NLP]
date: 2026-03-21
round: 2 (re-review of v2, following "Revise and re-review" verdict on v1)
prior_review: TRP-SYN-01 (2026-03-20)
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
status: reference-activated
---
# Triadic Review Protocol (Round 2): SYN-01 v2 -- The Architecture of Compositional Formal Meaning

**Venture:** SGO-2026-SYN-001 -- *The Architecture of Compositional Formal Meaning: A Categorical Framework for Structural Unification of Grammar, Semantics, and Computation*

**Domain Signature:** `[category theory, formal semantics, NLP]`

**Dependencies:** RP-01 (The Semantics Bridge), RP-06 (Chomsky to Computation)

**Review context:** This is a Round 2 re-review. The v1 draft received an aggregate verdict of "Revise and re-review" (POV 1: advance with amendments; POV 2: revise and re-review; POV 3: revise and re-review). Seven revision priorities were issued. This review evaluates whether the v2 revision adequately addresses those priorities.

---

## Revision Priority Tracker

Before the individual POV reviews, a summary of how each original revision priority was addressed:

| # | Priority | Status | Assessment |
|---|----------|--------|------------|
| 1 | **[Critical -- POV 3]** Philosophy of unification section; engage Kitcher, Morrison, Erlangen | **Addressed** | New Section 1.3 engages all three substantively. Erlangen framing adopted as central organising metaphor. |
| 2 | **[Critical -- All]** Narrow scope claim | **Addressed** | Title changed; abstract rewritten; scope limitations made explicit in Section 1.5; "compositional formal meaning" used throughout. |
| 3 | **[Critical -- POV 2]** Honest DisCoCat assessment | **Addressed** | Section 3.5 now acknowledges scaling failure directly, lists undemonstrated benchmarks, reframes as proof of concept. |
| 4 | **[Important -- POV 1]** Tighten categorical claims | **Largely addressed** | Fibred categories introduced (Section 3.1); symmetric/non-symmetric distinction treated (Section 3.6); ASCII diagram provided (Section 4.2); worked topos example (Section 3.7). Some residual issues noted below. |
| 5 | **[Important -- POV 2]** Testable predictions | **Addressed** | Section 5.3 provides four specific, testable predictions. Quality varies; see POV 2 assessment. |
| 6 | **[Desirable -- POV 1]** Graded monads for non-compositionality | **Not addressed** | Moggi's monads are discussed but graded monads (Katsumata 2014) are not mentioned. Acceptable as "desirable" priority. |
| 7 | **[Desirable -- POV 3]** Remove or strengthen ORGANVM section | **Addressed** | Section removed entirely. |

---

## POV 1 Review: Theorist / Category Theory / Sympathetic

### Summary Assessment

The v2 revision has substantially improved the mathematical precision of the paper. The fibred category formulation is the single most important structural improvement: it transforms the central claim from an impressionistic gesture ("meaning is a functor") into a precisely stated mathematical proposition about a parametrised family of functors with coherent reindexing. The worked topos example, while still elementary, demonstrates that the author can move from programmatic to concrete. The symmetric/non-symmetric distinction is now honestly treated. The paper is significantly closer to publication-quality from a category-theoretic standpoint.

### Primary Mode: Amendment

The critical amendments from Round 1 have been addressed. What remains are refinements -- important for a dissertation, but not blocking for advancement.

**1. The fibred formulation is sound but could be more precise.** The paper introduces the category **T** of interpretive traditions and defines the fibration p: **Sem** -> **T**. This is the right move. However, the treatment remains somewhat informal. The paper says the objects of **T** are "the various choices of semantic domain (Set, Dom, FdVect, Kripke presheaves, etc.)" and the morphisms are "functors between them that preserve the relevant structure." For a dissertation, the morphisms of **T** need sharper characterisation. Which functors between Set and Dom count as morphisms in **T**? The forgetful functor from Dom to Set? The free domain functor? Both? The answer matters because the reindexing functors of the fibration -- which are the formal expression of "translating meaning across traditions" -- are determined by the morphisms of **T**. I recommend adding a paragraph that gives at least two concrete morphisms in **T** (e.g., the forgetful functor **Dom** -> **Set** that forgets the domain structure and retains only the underlying sets, and the inclusion **Set** -> [**W**, **Set**] that embeds extensional semantics into intensional semantics via constant functions on worlds) and shows how the reindexing along these morphisms produces the expected relationship between the corresponding meaning functors. This would move the fibred formulation from "correctly schematic" to "concretely instantiated."

**2. The commutative diagram is a good start but the natural transformations need content.** The ASCII diagram in Section 4.2 is a welcome addition. The labels U_LD, U_DV, U_VP are introduced as "natural transformations witnessing coherence," but the paper does not specify what these natural transformations *are*. For U_LD (the transformation between the logical and domain-theoretic meaning functors), the content is well-known: it is the denotational semantics of logic, the functor that maps each logical formula to its denotation in a domain model. For U_DV (domain-theoretic to distributional), the content is much less clear -- this is arguably the least understood edge in the diagram. The paper should either specify these transformations concretely (at least for the well-understood edges) or explicitly state which edges are established and which are conjectural. A pentagonal diagram with some edges marked "established" and others marked "conjectural" would be more honest and more useful than a diagram that implies all edges are on the same footing.

**3. The worked topos example is adequate but could be strengthened.** The anaphora resolution example (Section 3.7) successfully demonstrates the presheaf-as-context mechanism and the sheaf condition as coherence. The example is clear and pedagogically effective. Two suggestions for strengthening it:

(a) The category of contexts **C** is defined as a poset of discourse states ordered by inclusion of referent sets. This is natural but minimal. A richer **C** -- one that includes morphisms for *forgetting* referents (modelling the decay of discourse salience) or for *splitting* contexts (modelling garden-path ambiguity) -- would show the presheaf machinery doing more work. This is a suggestion for future development, not a blocking amendment.

(b) The example does not exhibit the *subobject classifier* of the presheaf topos, which is one of the advertised connections to non-classical truth values. A brief remark showing that the truth value of "he refers to the farmer" in the presheaf topos is not {true, false} but a sieve on **C** -- a set of contexts in which the proposition holds -- would connect the example to the topos-theoretic claims more concretely.

**4. Adjunctions remain underexploited.** This was a secondary observation in Round 1 and remains relevant. The paper mentions the residuation in the Lambek calculus as an adjunction and the unit-counit of compact closure, but does not develop a systematic adjunction-based perspective. The relationship between syntax and semantics in several of the traditions is not merely functorial but *adjoint*: the "free" construction (from semantic types to syntactic types) and the "forgetful" construction (from syntax to underlying semantic structure) form adjoint pairs. Adequacy and full abstraction results can be formulated as conditions on these adjunctions. This remains a direction for future development rather than a blocking concern, but the paper could at minimum note the adjunction perspective as a natural extension of the fibred formulation.

### Secondary Observations

**Expansion.** The fibred formulation opens a direction the paper does not pursue: *descent theory*. In algebraic geometry, descent theory studies when local data (meaning in individual semantic traditions) can be assembled into global data (meaning in a "universal" semantic category). The question "does the fibration p: **Sem** -> **T** satisfy effective descent?" is a precise formulation of "is there a universal semantic category that all traditions are fragments of?" This is a deep question that the paper need not answer, but it should be identified as the mathematical formulation of the "grand unification" aspiration the paper explicitly defers.

**Amendment (minor).** The reference to Grothendieck (1971) for fibred categories is correct but the more accessible reference for a semantics audience would be Jacobs (1999), which the paper does cite but only in passing. I recommend making Jacobs the primary reference for the fibred category framework and Grothendieck the historical credit.

### Verdict

- [x] Advance with amendments (listed above)
- [ ] Advance as-is
- [ ] Revise and re-review
- [ ] Fork: alternative path recommended

The paper has met the standard for advancement. The amendments above are refinements appropriate for the revision cycle between CANDIDATE and PUBLIC_PROCESS, not grounds for another full revision.

### Inter-POV Questions

**To POV 2:** The fibred formulation and the testable predictions in Section 5.3 are the paper's main concessions to your Round 1 concerns. Prediction 2 (categorical structure improves compositional generalisation) and Prediction 4 (tensor rank and compositional complexity) are the most empirically concrete. Do you find these genuine enough to constitute a research programme, or are they still too theory-driven to engage the NLP community?

**To POV 3:** The Erlangen framing is now central. Does the paper succeed in positioning structural unification as a legitimate and precisely characterised achievement? Or does the analogy with the Erlangen Programme do too much work -- is there a disanalogy between Klein's situation (many geometries, one schema) and this paper's situation (three semantic traditions, one schema) that the paper does not confront?

---

## POV 2 Review: Practitioner-Empiricist / Distributional Semantics & NLP / Adversarial

### Summary Assessment

The v2 revision represents a significant improvement in intellectual honesty. The paper now acknowledges, without hedging, that DisCoCat has not scaled; that transformers compute meaning without implementing the categorical architecture; and that the burden of proof falls on the architecture to explain what it adds. The removal of the ORGANVM section was correct. The testable predictions section is a genuine attempt to provide empirical traction. However, the predictions remain closer to "hypotheses a sympathetic theorist would find interesting" than to "experiments an NLP researcher would run," and the paper still does not fully reckon with the depth of the challenge that neural methods pose to the categorical programme. The revision moves from "Revise and re-review" territory to "Advance with amendments" -- but only just.

### Primary Mode: Amendment

**Assessment of how Round 1 critiques were addressed:**

**1. DisCoCat honesty -- ADEQUATELY ADDRESSED.** Section 3.5 now contains the most honest assessment of DisCoCat I have seen in a paper sympathetic to the categorical programme. The explicit list of undemonstrated benchmarks (WMT, Natural Questions, CNN/DailyMail, MultiWOZ), the acknowledgment that fifteen years of development have not closed the scaling gap, and the reframing as "proof of categorical concept" are all correct. The sentence "it demonstrates that reconciliation is feasible *in principle*, for sentences of two or three words consisting of subject-verb-object triples" is exactly right. This is a marked improvement.

**2. Transformer engagement -- PARTIALLY ADDRESSED.** Section 5.2 is significantly better than the v1 treatment. The paper now says plainly: "If meaning can be computed (or at least closely approximated) without the functorial passage from syntax to semantics, then the burden of proof falls on the architecture to explain what it adds." This is the right framing. The paper's answer -- structural transparency, guaranteed compositionality, and a framework for comparison -- is reasonable but still underweights the transformer challenge. The claim that comparing the architecture with transformers "on NLP benchmarks is a category error" is a hedge that should be removed or qualified. If the architecture makes predictions about compositional generalisation (Prediction 2), then those predictions *are* testable on benchmarks, and the comparison is not a category error but a direct empirical test. The paper cannot simultaneously claim testable predictions and claim that benchmark comparison is a category error.

**3. Testable predictions -- ADDRESSED BUT UNEVEN.** Section 5.3 provides four predictions. Their quality varies:

- **Prediction 1 (compositional vs. non-compositional processing):** This is testable in principle but faces a severe confound: compositional constructions and non-compositional constructions differ in many ways beyond compositionality (frequency, length, familiarity, register). A probing study comparing attention patterns would need to control for these confounds, and the prediction as stated does not specify how. The prediction needs operationalisation: which specific constructions, which specific probing method, what constitutes "more systematic, structure-sensitive behaviour"?

- **Prediction 2 (categorical structure improves compositional generalisation):** This is the strongest prediction. It is specific (COGS, SCAN, gSCAN), directional (improvement greatest on functor-application constructions), and connected to existing literature (Lake and Baroni 2018; Kim and Linzen 2020). However, the prediction is essentially that structured models outperform unstructured models on structured tasks -- which is already known. The distinctive contribution of the *categorical* architecture, as opposed to any structure-encoding approach, needs to be sharpened. What does the category-theoretic framework predict that, say, a tree-structured recursive neural network does not?

- **Prediction 3 (cross-tradition transfer):** This is interesting but not empirical in the NLP sense. It is a prediction about formal systems, testable by mathematical analysis, not by experiment. It belongs in the theoretical contributions section, not among empirical predictions.

- **Prediction 4 (tensor rank and compositional complexity):** This is specific and testable. The prediction that higher-arity grammatical types require higher-rank tensors, and that this is reflected in learning difficulty, could be tested with existing DisCoCat implementations. This is the most novel prediction in the section.

**Remaining concerns:**

**4. The multimodal challenge is still unaddressed.** Round 1 noted that the paper ignores multimodal language models (CLIP, Flamingo, GPT-4V, Gemini). v2 does not address this. The multimodal revolution is directly relevant because it challenges the assumption that "the semantic category" is a category of linguistic/logical denotations. If meaning is grounded in visual and embodied perception, then the semantic category must include perceptual representations, and the functorial passage from syntax to this richer semantic category has not been defined. The paper's scope limitation to "compositional formal meaning" provides partial cover, but a sentence acknowledging the multimodal challenge -- even to say it falls outside scope -- would be appropriate.

**5. The "honest framing" of Section 5.2 does not follow through.** The paper says: "the categorical architecture and transformers may be describing the same phenomena at different levels of abstraction, or they may be describing *different* phenomena that happen to co-occur in language. The question of which is the case is empirical." This is exactly right. But the paper then proceeds as if the first option is obviously correct (the architecture describes structure, transformers implement it). The possibility that they describe genuinely different phenomena -- that the compositional structure described by the architecture is an artefact of a particular theoretical tradition rather than a feature of language -- deserves at least a paragraph of direct engagement. This was POV 3's central concern in Round 1, and while the Erlangen framing addresses it philosophically, it does not address it empirically.

### Secondary Observations

**Amendment (minor).** The paper should cite Gavranovic et al. (2024) more substantively. The reference appears in the bibliography but is not discussed in the text. This paper on categorical deep learning is directly relevant to the question of whether category theory can inform neural architecture design, which is the most promising direction for giving the categorical programme empirical traction.

**Expansion.** One direction that would strengthen the paper's empirical relevance: the categorical architecture predicts specific *failure modes* for compositional generalisation. If compositional generalisation is functorial, then failures should be *systematic* -- they should occur at the boundary of the functorial core, not randomly. Analysing the error patterns on COGS and SCAN through the lens of the categorical architecture (which errors correspond to failures of functoriality? which correspond to phenomena outside the compositional core?) would be a concrete, achievable empirical contribution.

### Verdict

- [x] Advance with amendments (listed above)
- [ ] Advance as-is
- [ ] Revise and re-review
- [ ] Fork: alternative path recommended

This is a borderline verdict. The v2 revision addressed the most severe honesty problems from v1. The remaining concerns -- prediction operationalisation, multimodal silence, and the unresolved "different phenomena" possibility -- are addressable in the next revision cycle without requiring a full re-review. The paper has earned conditional advancement.

### Inter-POV Questions

**To POV 1:** The fibred formulation is mathematically elegant, but does it generate *different* predictions from the simpler claim that "each tradition has its own functor from syntax to semantics"? If the fibration is merely a way of organising the family of functors, rather than a structure that constrains them, then its empirical content is zero. Is there a consequence of the fibration axioms that is not a consequence of the individual functors considered separately?

**To POV 3:** The paper now claims "structural unification" rather than "scientific unification." My worry is that this retreat is *too* successful -- it positions the result where it cannot be challenged. If structural unification requires only shared mathematical schema, and category theory is general enough to provide a schema for anything, then "structural unification" is trivially achievable for any collection of formal systems. Does the Erlangen analogy have enough teeth to prevent this trivialisation?

---

## POV 3 Review: Critic / Philosophy of Science / Orthogonal

### Summary Assessment

The v2 revision is a substantially more honest and philosophically informed paper. Section 1.3 engages seriously with Kitcher, Morrison, and the Erlangen Programme, and the result is a paper that knows what it is and says so clearly. The retreat from "grand unified semantics" to "structural unification of compositional formal meaning" is not merely a change of title but a genuine recalibration of the intellectual claims. The paper is now positioned to make a defensible contribution. Whether it *succeeds* in this positioning -- whether the Erlangen analogy holds, whether "structural unification" is as productive as the paper claims, and whether the honest concessions leave enough substance for a dissertation -- are the questions this review addresses.

### Primary Mode: Amendment

**Assessment of how Round 1 critiques were addressed:**

**1. Philosophy of unification -- WELL ADDRESSED.** Section 1.3 is the most important addition to the paper. The engagement with Kitcher is correct: the paper achieves a modest reduction of explanatory patterns. The engagement with Morrison is correct: the result is structural, not theoretical or reductive. The Erlangen Programme analogy is well-chosen and well-developed. The Eilenberg-Mac Lane quotation connecting categories to the Erlangen Programme is a particularly effective rhetorical move.

However, the engagement could be deepened in one respect. Kitcher's account of explanatory unification is not the only account. Friedman (1974) argued that unification is a matter of reducing the number of *independently acceptable* laws or principles. On Friedman's stricter criterion, the paper's unification is more substantial than Kitcher would suggest: the functorial principle replaces multiple independent principles of compositionality (Montague's rule-to-rule hypothesis, Scott and Strachey's compositionality, the homomorphism condition in abstract model theory) with a single principle (functoriality). The paper would benefit from noting Friedman's account alongside Kitcher's, as it provides a more favourable assessment without sacrificing honesty.

**2. The "almost tautological" reframing -- ADEQUATELY ADDRESSED.** The v2 treatment of this issue (Section 3.1, "Why 'almost tautological' is a feature, not a bug") is significantly better than the v1 concession. The argument that the apparent tautological character reflects the *naturality* of the concept -- that the functorial perspective was already latent in all three traditions -- is philosophically sound. The analogy with the Erlangen Programme's "tautological" character is apt: Klein did not discover something geometers did not know; he made explicit a structure that was already operative. This is a legitimate form of intellectual contribution.

The risk, which the paper does not fully address, is that "making the implicit explicit" is valuable only if the explicit formulation enables something the implicit understanding did not. The paper gestures at this (the five-way table, the commutative diagram, the fibred formulation, the presheaf example) but does not make the case as forcefully as it could. A paragraph that lists specific insights or results that were *not available* without the categorical formulation -- not merely re-descriptions of known results, but genuinely new observations or connections -- would complete the argument.

**3. Scope narrowing -- WELL ADDRESSED.** The title change, the explicit scope limitations in Section 1.5, and the consistent use of "compositional formal meaning" throughout the paper represent a genuine narrowing, not a cosmetic one. The paper is now honest about its territory. The list of exclusions (pragmatics, embodied meaning, non-compositional phenomena, dynamic semantics in full generality, game-theoretic semantics, probabilistic semantics) is comprehensive and correctly placed.

One improvement: the paper should note that several of these exclusions (dynamic semantics, game-theoretic semantics) are *formally rigorous* approaches to meaning that happen to fall outside the compositional core. This matters because the paper could be read as claiming to unify "all rigorous approaches to meaning" when it actually unifies "all compositional, type-driven approaches to meaning." The exclusions make clear that rigour is necessary but not sufficient for inclusion in the architecture.

**4. Unification-vs-redescription -- LARGELY RESOLVED.** The Erlangen framing does resolve the central concern from Round 1, but it resolves it by changing the terms of the debate rather than by winning it. In Round 1, I asked whether the categorical architecture achieves genuine unification or mere redescription. The v2 answer is, in effect: "It achieves structural unification, which is a specific kind of result that falls between trivial redescription and scientific unification. This kind of result has a distinguished precedent (the Erlangen Programme) and is valuable when it is productive." This is an honest and defensible answer.

The question that remains is whether the answer is *sufficient* for a dissertation. The Erlangen Programme was valuable because it was *productive*: it generated new mathematics (invariant theory), clarified previously mysterious relationships (the hierarchy of geometries), and informed subsequent research (Lie groups, Cartan's classification). The paper needs to argue that its structural unification is similarly productive. The testable predictions in Section 5.3 are one form of productivity. The fibred formulation enabling systematic comparison of traditions is another. The presheaf example is a third. Together, these provide adequate evidence of productivity -- but the paper should make this argument explicitly rather than leaving the reader to assemble it.

**5. The group-theory analogy.** In Round 1, I argued that groups appear in crystallography, particle physics, and music theory, but this shared mathematical structure does not constitute a "unification" of those domains. The paper does not address this analogy directly, and it should. The response should be: the semantic traditions, unlike crystallography and music theory, *are studying the same phenomenon* (meaning) from different perspectives. The shared mathematical structure is evidence of shared subject matter, not a coincidence of mathematical tools. This argument requires defending the claim that the three traditions study "the same phenomenon," which is not trivial (a distributional semanticist and a model theorist might disagree about whether they are studying the same thing). But the argument is available, and the paper should make it.

### Secondary Observations

**Amendment.** The paper should engage, even briefly, with Cat's (2019) anti-unificationist position -- the view that the diversity of semantic frameworks is a feature, not a bug, and that forcing them into a single framework risks losing the distinctive insights of each. The paper's Erlangen framing provides the response (Klein unified geometries without collapsing their diversity), but the objection should be stated before the response is given.

**Amendment (minor).** The conclusion (Section 7) is well-calibrated but ends weakly: "Whether making structure explicit constitutes 'unification' depends on one's philosophy of unification. That it constitutes a productive intellectual achievement -- in the tradition of the Erlangen Programme -- the present author submits with confidence." This is hedging at the finish line. After seven sections of careful argument, the paper has earned the right to a more assertive conclusion. I suggest: state clearly that the paper achieves structural unification, that structural unification is a specific and valued form of intellectual achievement, and that the productivity of the result (the five-way correspondence, the fibred formulation, the testable predictions, the presheaf example) demonstrates that the achievement is substantive. Then acknowledge the limitations -- but do not end on a hedge.

**Expansion.** The paper could note an interesting reflexive property of its own position: the *philosophy of unification* section (Section 1.3) itself exemplifies structural unification -- it shows that Kitcher's, Morrison's, and Klein's accounts of unification share a common schema (multiple perspectives on a phenomenon, unified by a shared structure), just as the paper shows that the three semantic traditions share a common schema. This self-similar structure is characteristic of deep results and could be noted briefly without indulgence.

### Verdict

- [x] Advance with amendments (listed above)
- [ ] Advance as-is
- [ ] Revise and re-review
- [ ] Fork: alternative path recommended

The paper has met the standard for advancement. The philosophical positioning is now sound. The remaining amendments are refinements that sharpen the argument without requiring restructuring.

### Inter-POV Questions

**To POV 1:** The fibred formulation and the presheaf example are the paper's strongest new formal contributions. Do you see these as genuinely *enabled* by the categorical framework -- results that could not have been formulated without categories -- or as re-formulations of ideas that were already available in the domain-specific traditions? The answer to this question is the empirical test of whether the "making-explicit" move is productive.

**To POV 2:** You worry that structural unification is trivially achievable for any collection of formal systems. I share the concern in principle, but is it true in practice? Can you name a case where a "categorical unification" of formally unrelated domains has been proposed and found to be vacuous? If such cases exist, the paper needs to distinguish itself from them. If they do not, the concern may be theoretical rather than practical.

---

## TRP Synthesis

### Agreement Map (High-Confidence Findings)

All three POVs agree on the following:

1. **The v2 revision has substantially addressed the critical concerns from Round 1.** The scope narrowing, the philosophy of unification section, the honest DisCoCat assessment, the fibred formulation, the worked topos example, and the removal of the ORGANVM section are all genuine improvements. The paper is a different and significantly better paper than v1.

2. **The Erlangen Programme framing is the right move.** All three POVs regard the positioning as structural unification -- with the Erlangen precedent -- as honest, defensible, and productive. It resolves the central tension of v1 (unification-vs-redescription) by changing the terms to a position the paper can actually defend.

3. **The paper now knows what it is.** The v1 draft oscillated between claiming grand unification and conceding near-tautology. The v2 draft holds a consistent position: structural unification of the compositional core, productive but not revolutionary, in the tradition of Klein rather than Maxwell. This consistency is a major improvement in intellectual quality.

4. **The testable predictions are a step in the right direction but need sharpening.** All three POVs find the predictions section a genuine addition. POV 2 provides the most detailed assessment: Prediction 2 (compositional generalisation) and Prediction 4 (tensor rank) are the strongest; Prediction 1 needs operationalisation; Prediction 3 is theoretical rather than empirical.

5. **Residual issues are refinements, not structural problems.** The remaining amendments (sharper fibred morphisms, concrete natural transformations, multimodal acknowledgment, the group-theory analogy response, conclusion strengthening) are all addressable in the next revision cycle.

### Disagreement Map (Most Valuable Signals)

1. **On the empirical sufficiency of the predictions (POV 1 vs. POV 2).** POV 1 regards the predictions as appropriate for a theoretical paper. POV 2 regards them as necessary but insufficiently operationalised. This reflects a genuine disciplinary difference about what counts as a "testable prediction." POV 1 is content with predictions that are in-principle testable; POV 2 demands predictions with specified experimental protocols. The paper should err toward POV 2's standard: add a paragraph to Predictions 1 and 2 specifying at minimum which constructions, which baselines, and what success criteria would be used.

   **Resolution:** Address in next revision. Not blocking for advancement.

2. **On the trivialisation risk (POV 2 and POV 3).** POV 2 worries that structural unification is trivially achievable for any collection of formal systems, since category theory is general enough to provide a schema for anything. POV 3 shares this concern but considers it addressed by the Erlangen analogy. The disagreement is about whether the Erlangen analogy provides adequate protection against trivialisation. POV 2 wants an empirical guarantee (the unification must make predictions that pure category-theoretic abstraction would not); POV 3 wants a philosophical guarantee (the traditions must genuinely study the same phenomenon).

   **Resolution:** The paper should address both. Add a paragraph distinguishing the present unification from the vacuous case (groups in crystallography and music theory) by arguing that the three semantic traditions study the same phenomenon, and connect this argument to the empirical predictions that test whether the shared structure captures real regularities.

3. **On the "category error" claim in Section 5.2 (POV 2 vs. POV 1).** POV 2 correctly notes that the paper cannot simultaneously claim testable predictions about compositional generalisation and claim that benchmark comparison is a "category error." POV 1 does not address this tension. The paper should resolve it: either remove the "category error" remark or qualify it to say that comparison on *general-purpose* benchmarks is a category error but comparison on *compositional generalisation* benchmarks is a direct test.

   **Resolution:** Address in next revision. Minor but important for consistency.

### Expansion Inventory

1. **Descent theory as the formalisation of "grand unification"** (POV 1). Whether the fibration satisfies effective descent is the precise mathematical question of whether there exists a universal semantic category. Identify as future work.

2. **Categorical analysis of COGS/SCAN error patterns** (POV 2). Analyse existing compositional generalisation failures through the lens of the functorial architecture to determine which errors correspond to boundary conditions of the architecture. Achievable near-term research.

3. **Friedman's (1974) stricter unification criterion** (POV 3). Provides a more favourable assessment of the paper's achievement than Kitcher alone. Quick addition with high payoff.

4. **Anti-unificationist position** (POV 3). Engage with the view that framework diversity is valuable, and show that the Erlangen approach preserves diversity while revealing structure.

5. **Reflexive structure of the argument** (POV 3). The paper's own methodology (unifying accounts of unification) exemplifies its thesis. A brief note, not a section.

6. **Concrete morphisms in **T**** (POV 1). Specify at least two morphisms in the category of interpretive traditions and show how reindexing works concretely. Essential for a dissertation-quality fibred formulation.

### Fork Analysis

No POV recommended a fork in either Round 1 or Round 2. The project direction remains sound.

### Aggregate Verdict

| POV | Round 1 Verdict | Round 2 Verdict | Change |
|-----|-----------------|-----------------|--------|
| POV 1 (Category Theorist) | Advance with amendments | Advance with amendments | Sustained; new amendments are refinements |
| POV 2 (Distributional Semanticist) | Revise and re-review | Advance with amendments | Upgraded; critical honesty concerns resolved |
| POV 3 (Philosopher of Science) | Revise and re-review | Advance with amendments | Upgraded; unification-vs-redescription resolved by Erlangen framing |

**Resolution per protocol (3/3 advance with amendments): Advance with amendments incorporated.**

The paper advances from LOCAL to CANDIDATE status, contingent on the following amendments being incorporated in the next revision (v3):

### Amendment Priorities (Ordered)

1. **[Important -- POV 2]** Remove or qualify the "category error" remark in Section 5.2 to be consistent with the testable predictions in Section 5.3. If the architecture makes predictions about compositional generalisation benchmarks, then benchmark comparison is not a category error for those benchmarks.

2. **[Important -- POV 1]** Add concrete morphisms in the base category **T** (at least two examples) and show how reindexing along these morphisms produces the expected relationships between meaning functors. This moves the fibred formulation from schematic to instantiated.

3. **[Important -- POV 3]** Add a paragraph distinguishing the present structural unification from the trivially achievable case (the group-theory analogy). Argue that the three semantic traditions study the same phenomenon, not merely use the same mathematics, and connect this to the empirical predictions.

4. **[Important -- POV 2]** Operationalise Predictions 1 and 2 with at least a sketch of experimental design: which constructions, which baselines, what constitutes success. Prediction 3 should be moved from "testable predictions" to "theoretical consequences" or relabelled as a formal rather than empirical prediction.

5. **[Desirable -- POV 2]** Add a sentence or brief paragraph acknowledging the multimodal challenge (CLIP, GPT-4V, Gemini) as falling outside the current scope but relevant to future extensions of the architecture.

6. **[Desirable -- POV 3]** Cite Friedman (1974) alongside Kitcher (1981) in Section 1.3 for a more complete picture of the philosophy of unification.

7. **[Desirable -- POV 1]** Specify which edges in the commutative diagram (Section 4.2) represent established mathematical results and which represent conjectural or partial correspondences. Mark the diagram accordingly.

8. **[Desirable -- POV 3]** Strengthen the conclusion: after seven sections of careful argument, the paper has earned a more assertive final paragraph. State the achievement positively, then acknowledge limitations -- do not end on a hedge.

---

*TRP Round 2 executed 2026-03-21. Single-model review (Claude Opus 4.6, 1M context). Same triad as Round 1, evaluating whether v2 revisions addressed Round 1 concerns. For full inter-model triangulation, re-execute with empirically-oriented model for POV 2.*
