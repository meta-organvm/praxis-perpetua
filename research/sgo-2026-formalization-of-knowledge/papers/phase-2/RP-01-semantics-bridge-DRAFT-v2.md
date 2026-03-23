---
sgo_id: SGO-2026-RP-001
title: "Toward a Unified Compositional Formal Semantics"
tier: Dissertation
status: LOCAL (revised draft)
target_venues: [Journal of Philosophical Logic, Linguistics and Philosophy, arXiv cs.LO]
dependencies: [RP-06]
date: 2026-03-21
revision_date: 2026-03-20
version: v2
revision_notes: |
  TRP review required revise-and-re-review (1/3 advance, 1/3 revise, 1/3 fork).
  Key amendments incorporated:
  - Narrowed scope explicitly to "compositional formal semantics" per SYN-01 v2 recalibration.
    Title changed from "Grand Unified Semantics" to "Unified Compositional Formal Semantics."
  - Added Section 6: Embodied and Enactive Cognition -- acknowledges this as outside scope
    but not irrelevant, documents the fork as future work.
  - Substantially expanded distributional semantics treatment (Section 5.3 -> Section 5);
    engages seriously with the scaling hypothesis.
  - Specified which NL fragment the unification covers (Section 4.4).
  - Tightened epistemic claims: "the bridges connect formal traditions" not "the bridges
    unify meaning."
---

# Toward a Unified Compositional Formal Semantics: Structural Bridges Across Logic, Computation, and Natural Language

**Studium Generale ORGANVM -- Research Program RP-01**

---

## Abstract

The word "semantics" names three distinct academic traditions: logical semantics, in which meaning is truth-in-a-structure (Tarski, Kripke); programming language semantics, in which meaning is mathematical denotation, operational behaviour, or axiomatic specification (Scott, Strachey, Hoare); and formal natural language semantics, in which meaning is truth-conditional content compositionally assigned to syntactic structures (Montague, Heim, Kratzer). Each tradition claims to study "meaning," yet each operates with different formalisms, different standards of adequacy, and different philosophical presuppositions. This dissertation investigates whether the *compositional formal core* of these three traditions is unified by deep structural bridges or whether they merely share a homonymous label. Through systematic analysis of eight identified bridge structures -- compositionality, lambda calculus, the Curry-Howard-Lambek correspondence, type theory, model theory, game semantics, dynamic semantics, and proof-theoretic semantics -- we argue that the classical, compositional, typed fragment of each tradition admits genuine structural unification, with category theory providing the most perspicuous unifying metalanguage. For each bridge, we assess whether the cross-domain parallel constitutes genuine isomorphism, homomorphism, or mere analogy. We identify the precise points at which unification breaks down and argue that these breakdowns define the boundary of compositional formal tractability. The scope of this paper is explicitly limited to *compositional formal semantics*; the embodied, enactive, and phenomenological dimensions of meaning -- which constitute a genuine and important alternative paradigm -- are acknowledged as outside this scope but are documented as a fork for future work.

**Keywords:** formal semantics, compositionality, lambda calculus, Curry-Howard correspondence, type theory, category theory, game semantics, dynamic semantics, model theory, proof-theoretic semantics, distributional semantics, Montague grammar

---

## 1. Introduction

### 1.1 The Homonymy Problem

The term "semantics" appears, with apparently equal legitimacy, in at least three distinct disciplinary contexts. In mathematical logic, semantics is the study of truth, validity, and logical consequence relative to mathematical structures (Tarski 1936). In computer science, semantics is the rigorous mathematical study of the meaning of programming languages (Scott and Strachey 1971; Plotkin 1981; Hoare 1969). In linguistics and the philosophy of language, semantics is the study of the meaning of natural language expressions through truth-conditional, compositional, type-theoretic methods (Montague 1973; Heim and Kratzer 1998).

This terminological convergence raises a question that is at once philosophical, mathematical, and practical: do these three traditions study the same thing?

### 1.2 Scope Delimitation

A critical clarification is necessary at the outset. This paper investigates the structural unity of *compositional formal semantics* -- the core of each tradition that deals with meaning as compositional, typed, structure-preserving passage from syntax to semantic interpretation. This scope excludes several important dimensions of meaning:

- **Embodied and enactive meaning.** The tradition from Lakoff and Johnson (1980) through Varela, Thompson, and Rosch (1991) to Barsalou (2008) argues that meaning is grounded in sensorimotor experience. This paper does not engage with this tradition except to acknowledge its existence and identify the boundary between what compositional formal semantics captures and what it misses (Section 6).

- **Pragmatic meaning.** What speakers communicate beyond literal content -- Gricean implicature, presupposition, speech acts -- resists compositional treatment.

- **Phenomenological meaning.** The felt, lived dimension of understanding -- what it is *like* to mean something -- falls outside formal analysis.

The decision to limit scope is not a judgment that these dimensions are unimportant. It is a recognition that a useful structural comparison requires commensurable objects, and the compositional formal core is where the three traditions are most directly commensurable. Section 6 documents the embodied/enactive alternative as a fork for future work.

### 1.3 Research Questions

Three research questions guide the investigation:

**RQ1.** To what extent does the Curry-Howard-Lambek correspondence provide a genuine structural unification of compositional formal semantics across logic, computation, and natural language, and where does this unification break down?

**RQ2.** Is dynamic semantics -- the treatment of meaning as context-change potential -- a more natural unifying principle than truth-conditional semantics for bridging the three traditions?

**RQ3.** Can distributional semantics -- the statistical and geometric theory of meaning underlying modern neural language processing -- be reconciled with the formal semantic traditions, or does it constitute an irreducibly different theory of meaning?

### 1.4 Contribution and Scope

The principal contribution of this dissertation is a systematic taxonomy of cross-domain semantic bridges, ranked by structural strength on a four-point scale: isomorphism, homomorphism, analogy, and metaphor. This taxonomy is grounded in precise mathematical characterizations of each bridge and explicit identification of the conditions under which each bridge holds and fails.

## 2. The Three Traditions

### 2.1 Logical Semantics

Logical semantics, in the tradition of Tarski (1936) and Kripke (1963), studies truth, validity, and logical consequence relative to mathematical structures -- models, in the technical sense. A model-theoretic semantics interprets expressions by mapping them to elements, relations, and functions in a mathematical structure, with truth defined as a relationship between a sentence and a structure.

### 2.2 Programming Language Semantics

Programming language semantics, developed by Scott and Strachey (1971), Plotkin (1981), and Hoare (1969), provides three complementary approaches to the meaning of programs. Denotational semantics maps programs to mathematical objects (functions, domains). Operational semantics specifies meaning through execution rules. Axiomatic semantics specifies meaning through logical assertions (preconditions, postconditions).

### 2.3 Natural Language Semantics

Formal natural language semantics, inaugurated by Montague's (1973) demonstration that natural language could be treated with the same formal rigor as logical languages, assigns truth-conditional meaning to natural language expressions through compositional, type-theoretic methods. The Montagovian program treats natural language semantics as an extension of logical semantics, with lambda calculus providing the compositional machinery.

## 3. The Eight Bridges

### 3.1 Compositionality (Isomorphism)

In all three traditions, meaning is assigned by a structure-preserving map from a syntactic algebra to a semantic algebra. This is Frege's compositionality principle: the meaning of a complex expression is determined by the meanings of its parts and the rules of combination. In category-theoretic terms, compositionality is a functor from a syntactic category to a semantic category. This bridge holds at the level of isomorphism for the typed, compositional core of each tradition.

### 3.2 Lambda Calculus (Isomorphism)

Church's lambda calculus is, simultaneously and non-metaphorically, the foundation of functional programming, the notation of Montague grammar, and a proof-term calculus for intuitionistic logic. This is not analogy but identity: the same mathematical object serves as the foundation of all three traditions.

### 3.3 The Curry-Howard-Lambek Correspondence (Isomorphism/Homomorphism)

The three-way equivalence of proofs, programmes, and categorical morphisms is an isomorphism in the strongest sense. The extension to natural language, via the type-logical tradition and combinatory categorial grammar (CCG), is a homomorphism -- the natural language bridge operates through *substructural* categories (Lambek calculi that may lack exchange, weakening, or contraction), making the bridge to classical logic and standard typed lambda calculus a *forgetful functor* rather than an equivalence. This distinction matters: the NL bridge loses information (specifically, the resource-sensitivity of natural language expressions) that the logic-computation bridge preserves.

### 3.4 Type Theory (Homomorphism)

Types classify meanings in all three traditions: they sort entities into kinds, constrain well-formedness, and drive composition. The bridge is a homomorphism because the type systems differ in expressiveness (simple types in basic Montague grammar, polymorphic types in ML, dependent types in proof assistants) and the translation between them is structure-preserving but not bijective.

### 3.5 Model Theory (Isomorphism for Classical Fragments)

Interpretation as mapping from syntactic expressions to elements of a mathematical structure. The bridge holds at isomorphism for the classical fragments and degrades for extensions involving intensionality, context-dependence, and dynamic phenomena.

### 3.6 Game Semantics (Homomorphism)

Independently developed in all three traditions -- dialogical logic (Lorenzen), game-theoretical semantics for natural language (Hintikka), game semantics for programming languages (Abramsky, Hyland, Ong) -- treating meaning as interactive strategy.

### 3.7 Dynamic Semantics (Analogy Tending Toward Homomorphism)

Meaning as context-change potential, developed independently in logic (Kamp's DRT), programming (state transformers), and natural language semantics (Heim's file change semantics, Groenendijk and Stokhof's dynamic predicate logic). The formal structures are suggestive but the correspondence is under active formalization.

### 3.8 Proof-Theoretic Semantics (Homomorphism)

Meaning located in inferential role rather than denotation, developed by Gentzen, Prawitz, and Dummett in logic, by Martin-Lof in type theory, and with programmatic counterparts in the Curry-Howard correspondence.

## 4. The Structural Picture

### 4.1 Hierarchy of Bridge Strengths

The hierarchy of bridge strengths reveals a pattern: the bridges closest to the classical, compositional, typed core (compositionality, lambda calculus, model theory) achieve isomorphism; those that extend the core (type theory, game semantics, proof-theoretic semantics) achieve homomorphism; and those at the dynamic periphery achieve analogy under active formalization. No bridge was assessed as mere metaphor.

### 4.2 The Categorical Perspective

The categorical perspective provides the most perspicuous view of the unification. Compositional semantics in all three traditions can be formalized as a functor from a syntactic category to a semantic category. The Curry-Howard-Lambek correspondence provides a three-way equivalence. The central claim: meaning, in its compositional formal core, *is* functorial passage from syntax to semantics. This characterization is a *framework choice*, not a discovery about the nature of meaning -- it is chosen for its unifying power, and an inferentialist like Brandom (1994) would deny that meaning is passage from syntax to semantics, grounding meaning instead in inferential relations among sentences.

### 4.3 Central Finding

The three traditions of compositional formal semantics are unified at their compositional, typed, structure-preserving core. The unification breaks down at concurrency, pragmatics, distributional meaning, and compositionality failures. The boundary of unification marks the boundary of compositional formal tractability.

### 4.4 The Fragment: What the Unification Covers

The unification holds for a specific fragment of natural language that must be precisely characterized. The relevant fragment is: the portion of English (or any natural language) that can be parsed by a type-logical grammar (Lambek calculus, CCG, or pregroup grammar) and interpreted in a Montague-style model-theoretic semantics. This is a non-trivial fragment. It includes:

- Quantification (including scope ambiguity)
- Relative clauses
- Basic anaphora (within a dynamic extension)
- Coordination
- Adjectival and adverbial modification
- Intensional verbs and propositional attitudes (with possible-worlds extension)

It excludes:

- Idioms and non-compositional multi-word expressions
- Metaphor and figurative language
- Conversational implicature and pragmatic inference
- Discourse structure beyond single sentences (partially addressed by dynamic extensions)
- Ellipsis and fragments
- Most phenomena involving prosody, gesture, and multimodal communication

The size of this fragment matters for the significance of the unification. The fragment is large enough to cover a substantial portion of formal reasoning, legal language, scientific prose, and software documentation. It is not large enough to cover casual conversation, poetry, persuasive rhetoric, or most of what makes natural language communication interesting to its users. The unification is genuine but bounded, and the bounds should be stated explicitly rather than left implicit.

## 5. The Distributional Challenge and the Scaling Hypothesis

### 5.1 The Elephant in the Room

The dominant paradigm in computational semantics as of 2026 is distributional: transformer-based language models achieve state-of-the-art performance on virtually every NLP benchmark, including tasks that were supposedly the stronghold of formal semantics -- entailment detection, semantic parsing, question answering, logical reasoning. They do this without compositionality in the classical sense (no explicit type-driven bottom-up construction), without model-theoretic interpretation, and without lambda calculus. They operate by learning statistical regularities in token sequences at massive scale, using attention mechanisms that are neither typed nor compositional in the formal sense.

This paper must confront this challenge directly rather than treating it as a footnote.

### 5.2 The Scaling Hypothesis

The *scaling hypothesis* -- the thesis that sufficiently large neural language models, trained on enough data, will develop all the linguistic competence that formal theories describe, without any explicit formal structure -- is not proven, but it is the dominant working assumption in NLP engineering. The hypothesis has strong empirical support: performance on formal reasoning benchmarks has improved dramatically with model scale, and emergent capabilities (chain-of-thought reasoning, in-context learning) appear at scale thresholds that no formal theory predicted.

This paper takes the following position on the scaling hypothesis: **if transformers succeed without explicit compositional structure, this tells us something important about the relationship between compositional formal semantics and language processing, but it does not refute compositional formal semantics as a theory of meaning.** The distinction is between a theory of *structure* (what structural relationships hold among semantic objects) and a theory of *processing* (how those objects are computed). The bridges identified in this paper are structural: they describe isomorphisms and homomorphisms between mathematical objects. A neural network that achieves equivalent input-output behavior without implementing these structures is analogous to a calculator that produces correct arithmetic results without implementing the Peano axioms -- the axioms describe the structure of arithmetic regardless of how any particular device computes with numbers.

However, this response has limits. If neural models achieve perfect semantic competence without compositional structure, the pragmatic significance of compositional formal semantics is diminished: it becomes a theory of meaning that no practical system needs to implement. The bridges would be real but irrelevant to engineering -- a possibility this paper acknowledges honestly.

### 5.3 DisCoCat and Neuro-Symbolic Reconciliation

The DisCoCat framework of Coecke, Sadrzadeh, and Clark provides the most promising bridge between formal and distributional semantics. By interpreting grammatical types as vector spaces and grammatical derivations as multilinear maps, DisCoCat provides a compositional semantics in which the meaning of a sentence is a tensor in a product space. The framework uses compact closed categories as the mathematical setting.

The reconciliation is partial. Current transformer models do not obviously implement the categorial structure that DisCoCat requires. The question of whether transformers *implicitly learn* type-theoretic structure remains open. Recent probing studies (Hewitt and Manning, 2019; Tenney et al., 2019) find that syntactic structure is encoded in transformer hidden states, but the evidence that this encoding is *used* for semantic processing (rather than being an epiphenomenal correlate of distributional learning) is inconclusive.

The emerging paradigm of *neuro-symbolic AI* -- systems that combine neural language processing with symbolic reasoning -- takes the bridges seriously by literally building systems with both neural and symbolic components. This paradigm represents the most practically productive engagement with the formal-distributional tension and deserves sustained attention as a test of whether the bridges identified in this paper can be made to carry engineering weight.

### 5.4 What Would Refute the Unification?

The bridges described in this paper would be refuted if:
- A natural language phenomenon within the specified fragment (Section 4.4) could be shown to lack compositional structure in any type-logical grammar.
- A programming language semantics could be shown to be incompatible with the Curry-Howard correspondence (some exist: languages with `goto`, unrestricted side effects, and non-termination require extensions that weaken the correspondence).
- The DisCoCat program failed to produce empirically adequate compositional-distributional models even for the restricted fragment, suggesting that the categorical framework does not accommodate distributional meaning even in principle.

None of these refutations has occurred, but stating them explicitly makes the paper's claims testable.

## 6. The Embodied/Enactive Alternative: Scope Boundary and Future Work

### 6.1 What Compositional Formal Semantics Does Not Capture

The embodied cognition research program -- developed by Lakoff and Johnson (1980, 1999), Varela, Thompson, and Rosch (1991), Clark (1997), Barsalou (2008, 2010), and others -- argues that human cognition, including language, is fundamentally shaped by the body's interactions with the physical and social environment. Meaning is not a mapping from symbols to abstract structures; it is a pattern of *sensorimotor engagement* with the world.

This perspective does not deny that formal structures exist in language. There are compositional patterns, type-like constraints, and model-theoretic truth conditions. But it denies that these formal structures *constitute* meaning. They are abstractions -- useful, powerful, systematizable abstractions -- but they miss what makes meaning meaningful: its grounding in embodied experience, its connection to action, its sensitivity to social context, and its perpetual openness to creative extension.

The empirical evidence for embodied grounding is substantial. Barsalou (2008) provides evidence that conceptual processing involves reactivation of sensorimotor neural patterns. When people read the word "kick," motor areas associated with leg movement are activated. This neural grounding is not captured by any of the eight bridges identified in this paper, because the bridges are all purely structural.

### 6.2 The Fork: Embodied Semantics as Future Work

This paper documents a fork: a companion investigation that would examine the *limits* of formal unification from the perspective of embodied, situated, and enactive theories of meaning. The fork would ask:

1. Is the relationship between formal semantic structures and embodied grounding one of *implementation* (the formal structures are realized in sensorimotor patterns), *abstraction* (the formal structures are idealizations that approximate embodied meaning), or *orthogonality* (the formal and embodied dimensions of meaning are genuinely independent)?

2. Could one define a "grounding functor" from a formal semantic category to a sensorimotor category? The category-theoretic framework is, in principle, compatible with any mathematical structure; the question is whether the mapping from formal meanings to sensorimotor patterns preserves enough structure to qualify as a functor.

3. Does the success of neural language models -- which learn from text alone, without embodiment -- refute embodied cognition, or does it show that text is a sufficient approximation of embodied experience for a large class of language tasks? The failure of current models on tasks requiring genuine physical understanding (spatial reasoning, causal reasoning about physical interactions) suggests that embodied grounding may be necessary for *full* semantic competence, even if text-based learning suffices for the fragment that compositional formal semantics describes.

This fork is not a criticism of the present paper but a natural extension. The bridges identified here describe the architecture of formal meaning. The fork would investigate the relationship between formal meaning and the larger field of lived meaning that formal meaning presupposes.

## 7. Conclusion

This paper has systematically analyzed eight structural bridges connecting three traditions of compositional formal semantics and assessed each on a four-point scale of structural strength. The central finding is that the classical, compositional, typed fragment of each tradition admits genuine structural unification, with category theory providing the most perspicuous unifying metalanguage.

The unification is bounded. It covers a substantial but not exhaustive fragment of natural language. It does not accommodate distributional semantics except through the partial DisCoCat reconciliation. It does not capture the embodied, enactive, phenomenological, or pragmatic dimensions of meaning. These boundaries are not failures of the project but constitutive features: they define what compositional formal semantics is and is not a theory of.

The paper has engaged seriously with two challenges. The scaling hypothesis -- that transformers succeed without formal structure -- is acknowledged as an important empirical challenge to the *engineering relevance* of formal semantics, though not to its *structural validity*. The embodied cognition alternative -- that meaning is grounded in sensorimotor experience -- is documented as a fork for future work, with specific research questions that would test the relationship between formal and embodied meaning.

The bridges are real. They connect the compositional formal cores of three traditions that developed independently. Whether these bridges extend beyond the formal core -- to distributional, embodied, and pragmatic meaning -- is the frontier.

## References

Abramsky, S. (1997). "Semantics of Interaction: An Introduction to Game Semantics." In *Semantics and Logics of Computation*, 1-31.

Barsalou, L.W. (2008). "Grounded Cognition." *Annual Review of Psychology*, 59, 617-645.

Brandom, R. (1994). *Making It Explicit*. Cambridge, MA: Harvard University Press.

Church, A. (1936). "An Unsolvable Problem of Elementary Number Theory." *American Journal of Mathematics*, 58(2), 345-363.

Clark, A. (1997). *Being There: Putting Brain, Body, and World Together Again*. MIT Press.

Coecke, B., Sadrzadeh, M., and Clark, S. (2010). "Mathematical Foundations for a Compositional Distributional Model of Meaning." *Lambek Festschrift, Linguistic Analysis*, 36, 345-384.

Curry, H.B. and Feys, R. (1958). *Combinatory Logic*. Amsterdam: North-Holland.

Heim, I. and Kratzer, A. (1998). *Semantics in Generative Grammar*. Oxford: Blackwell.

Hewitt, J. and Manning, C.D. (2019). "A Structural Probe for Finding Syntax in Word Representations." *NAACL-HLT*.

Hoare, C.A.R. (1969). "An Axiomatic Basis for Computer Programming." *Communications of the ACM*, 12(10), 576-580.

Howard, W.A. (1980). "The Formulae-as-Types Notion of Construction." In *To H.B. Curry: Essays on Combinatory Logic*, 479-490.

Kripke, S. (1963). "Semantical Considerations on Modal Logic." *Acta Philosophica Fennica*, 16, 83-94.

Lakoff, G. and Johnson, M. (1980). *Metaphors We Live By*. University of Chicago Press.

Lambek, J. (1958). "The Mathematics of Sentence Structure." *American Mathematical Monthly*, 65(3), 154-170.

Montague, R. (1973). "The Proper Treatment of Quantification in Ordinary English." In J. Hintikka et al. (eds.), *Approaches to Natural Language*, 221-242.

Plotkin, G.D. (1981). "A Structural Approach to Operational Semantics." DAIMI FN-19, Aarhus.

Scott, D.S. and Strachey, C. (1971). "Toward a Mathematical Semantics for Computer Languages." *Proceedings of the Symposium on Computers and Automata*, 19-46.

Tarski, A. (1936). "The Concept of Truth in Formalized Languages." In *Logic, Semantics, Metamathematics*, 152-278.

Tenney, I., Das, D., and Pavlick, E. (2019). "BERT Rediscovers the Classical NLP Pipeline." *Proceedings of ACL*.

Varela, F.J., Thompson, E., and Rosch, E. (1991). *The Embodied Mind*. MIT Press.
