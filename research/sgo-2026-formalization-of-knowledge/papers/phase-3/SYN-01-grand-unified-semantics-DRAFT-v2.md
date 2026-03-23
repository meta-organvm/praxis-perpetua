---
sgo_id: SGO-2026-SYN-001
title: "The Architecture of Compositional Formal Meaning"
tier: Dissertation (synthesis)
status: LOCAL (revised draft v2)
target_venues: [Journal of Philosophical Logic, Mathematical Structures in Computer Science, arXiv cs.LO]
dependencies: [RP-01, RP-06]
bridges: [Adventure 1, Adventure 6]
date: 2026-03-21
revision_notes: |
  v2 revised in response to Triadic Review Protocol (TRP-SYN-01, 2026-03-20).
  Aggregate TRP verdict: Revise and re-review (2 of 3 POVs).
  Key changes in v2:
    1. Title and scope narrowed from "grand unified semantics" to "unified architecture
       of compositional formal meaning." Pragmatics, embodied meaning, and non-compositional
       phenomena explicitly placed outside scope.
    2. New Section 1.3 on philosophy of unification: engages Kitcher (1981) on explanatory
       unification, Morrison (2000) on theoretical vs. reductive vs. structural unification,
       and Klein's Erlangen Programme (1872) as the precedent for structural unification.
       Result positioned honestly as structural unification, not scientific unification.
    3. DisCoCat sections revised with honest empirical assessment: scaling failure
       acknowledged; DisCoCat reframed as categorical proof of concept, not practical bridge.
       Transformer success confronted directly without dismissal.
    4. Categorical claims tightened: fibred/indexed category treatment for the family of
       semantic functors; symmetric vs. non-symmetric compact closure distinction addressed;
       worked topos-theoretic example (anaphora resolution via presheaves); ASCII commutative
       diagram for the five-way correspondence.
    5. "Almost tautological" concession reframed as evidence of naturality: if functorial
       compositionality is the right framework, its apparent tautological character reflects
       that the concept was already latent in all three traditions -- the architecture
       makes explicit what was implicit.
    6. ORGANVM application section removed (per TRP recommendation: trivial application
       undermined theoretical claims).
    7. Testable predictions section added: specific hypotheses about transformer behaviour
       derivable from the categorical architecture.
---

# The Architecture of Compositional Formal Meaning: A Categorical Framework for Structural Unification of Grammar, Semantics, and Computation

**Studium Generale ORGANVM -- Cross-Adventure Synthesis SYN-01**

**Synthesis of RP-01 (The Semantics Bridge) and RP-06 (Chomsky to Computation)**

---

## Abstract

This dissertation synthesises two prior investigations conducted under the Studium Generale ORGANVM research programme: RP-01, which identified eight structural bridges connecting three traditions of formal semantics (logical, computational, and natural language), and RP-06, which established a fourfold correspondence among grammars, types, proofs, and categories descending from Chomsky's 1956--1959 formalization of the linguistic hierarchy. The present work asks whether these two results can be unified into a single categorical architecture of compositional formal meaning. The central claim is that meaning, in its compositional and type-driven core, is the functorial passage from a syntactic category to a semantic category, and that this passage exhibits the same categorical structure whether the syntax in question is linguistic, logical, or computational. Crucially, this claim is one of *structural unification* in the sense of Klein's Erlangen Programme -- the identification of a common mathematical schema across independently developed traditions -- not *scientific unification* in the sense of Maxwell or Darwin, which would require novel empirical predictions or ontological identification. The argument proceeds through five stages. First, the results of RP-01 and RP-06 are recapitulated and their overlap and divergence mapped. Second, a philosophy of unification is developed, engaging with Kitcher's (1981) account of explanatory unification, Morrison's (2000) taxonomy of unification types, and the Erlangen Programme as a precedent for structural unification via shared mathematical architecture. Third, the categorical architecture is constructed: compositionality is formalised as functoriality; the semantic categories are treated as a fibred family parametrised by interpretive tradition; the Lambek calculus is exhibited as the syntactic category; Montague's rule-to-rule correspondence is characterised as a natural transformation; the DisCoCat framework is assessed with an honest account of its empirical limitations; compact closed categories are situated with careful attention to the symmetric/non-symmetric distinction; and the topos-theoretic perspective is developed with a worked example of anaphora resolution via presheaves. Fourth, the unification claim is stated precisely as a five-way correspondence among derivation, proof, programme, morphism, and meaning-composition, supported by a commutative diagram, and evaluated against both supporting and countervailing evidence. Fifth, the distributional challenge is addressed: DisCoCat is reframed as a categorical proof of concept rather than a practical bridge; the empirical success of transformers is confronted directly; and testable predictions derivable from the categorical architecture are identified. The dissertation concludes that the classical, compositional, typed core of all three semantic traditions admits genuine *structural* unification under a single functorial architecture, while acknowledging that this achievement is weaker than scientific unification and that pragmatics, non-compositionality, embodied meaning, and neural mechanisms fall outside the architecture's scope.

**Keywords:** category theory, formal semantics, compositionality, functoriality, Curry-Howard-Lambek correspondence, Lambek calculus, Montague grammar, DisCoCat, pregroup grammar, compact closed category, topos, natural transformation, distributional semantics, type theory, Erlangen Programme, structural unification, fibred categories

---

## 1. Introduction

### 1.1 Two Convergent Investigations

The Studium Generale ORGANVM research programme has produced, in its second phase, two investigations that approach the formal structure of meaning from complementary directions. RP-01, *Toward a Grand Unified Semantics*, surveyed the three traditions of formal semantics -- logical semantics (Tarski 1936; Kripke 1959, 1963), programming language semantics (Scott and Strachey 1971; Plotkin 1981; Hoare 1969), and natural language semantics (Montague 1973; Heim and Kratzer 1998) -- and identified eight structural bridges connecting them: compositionality, lambda calculus, the Curry-Howard-Lambek correspondence, type theory, model theory, game semantics, dynamic semantics, and proof-theoretic semantics. Each bridge was assessed on a four-point scale of structural strength (isomorphism, homomorphism, analogy, metaphor), and the central finding was that the classical, compositional, typed fragment of each tradition admits genuine structural unification, with category theory providing the most perspicuous unifying metalanguage.

RP-06, *Grammars, Types, Proofs, and Categories*, approached the same territory from the side of formal language theory. Beginning with Chomsky's 1956--1959 formalization of the grammar hierarchy, RP-06 traced three threads from that origin: the "machines" thread (formal language theory and automata), the "engineering" thread (programming language syntax and compilers), and the "logic" thread (type theory, categorial grammar, and the Curry-Howard-Lambek correspondence). The central finding was a fourfold correspondence: at each level of the Chomsky hierarchy, grammars correspond to automata (the classical result), but they also correspond to regimes of type-theoretic expressiveness, and the convergence of all three threads reveals that grammars, types, proofs, and categories are structurally isomorphic. The Curry-Howard-Lambek correspondence, extended through categorial grammar to include linguistic derivation, renders this isomorphism precise: parsing IS type-checking IS proof construction IS composition of morphisms.

### 1.2 The Question of Unification

The present dissertation asks whether these two results can be unified into a single categorical architecture of meaning. RP-01 identified bridges between traditions of semantics; RP-06 identified correspondences between formal structures. The overlap is substantial: both investigations converge on the Curry-Howard-Lambek correspondence, on categorial grammar, on lambda calculus, and on the compositional, type-driven approach to meaning. Yet the investigations also diverge: RP-01 encompasses dynamic semantics and game semantics, which RP-06 does not address; RP-06 encompasses automata theory and the fine structure of the Chomsky hierarchy, which RP-01 treats only tangentially.

The unification question can be stated with precision. RP-01 established that meaning, across three traditions, is characterised by a compositional, structure-preserving map from syntax to semantics. RP-06 established that syntax, across four formal frameworks (grammars, types, proofs, categories), is characterised by a single abstract structure. If meaning is a map from syntax to semantics, and if syntax has a unified categorical structure, then meaning itself must have a unified categorical structure -- the structure of a functor from the syntactic category to the semantic category.

But what kind of unification is this? Before stating the central claim, it is necessary to be precise about what "unification" means in this context -- and, equally important, what it does not mean.

### 1.3 What Kind of Unification? Kitcher, Morrison, and the Erlangen Precedent

The word "unification" carries different weight in different intellectual traditions. The history of science offers paradigm cases of *scientific unification*: Maxwell's unification of electricity and magnetism, the Weinberg-Salam electroweak unification, Darwin's unification of biogeography and paleontology under natural selection. These unifications share distinctive features that must be examined honestly before any claim of "unification" is advanced.

**Kitcher's account of explanatory unification.** Philip Kitcher (1981) argued that unification is a matter of reducing the number of independent explanatory patterns: a unified theory explains many phenomena using few argument patterns, while a disunified collection uses many. On Kitcher's criterion, the categorical architecture achieves a modest degree of explanatory unification. The functorial pattern -- meaning as structure-preserving map from syntax to semantics -- replaces multiple independent descriptions of compositionality across traditions with a single argument pattern. But the degree of unification is limited: the functorial pattern was already implicit in the Curry-Howard-Lambek correspondence; the present work's contribution is to make it explicit across all three semantic traditions and to add the semantic dimension to RP-06's syntactic fourfold. This is genuine unification by Kitcher's lights -- reducing the number of explanatory patterns -- but it is incremental rather than revolutionary.

**Morrison's taxonomy of unification types.** Margaret Morrison (2000) distinguishes *theoretical unification* (what Maxwell achieved -- a single set of equations governing both electricity and magnetism), *reductive unification* (what Weinberg-Salam achieved -- deriving previously distinct forces from a single gauge symmetry), and what might be called *structural unification* -- showing that disparate domains share a common mathematical architecture without claiming that they share a cause or a substrate. Morrison's analysis is crucial for honest self-assessment: the present work achieves structural unification, not theoretical or reductive unification. The three traditions of formal semantics share a mathematical architecture (the functorial passage from syntax to semantics). But the architecture does not *explain* why compositionality holds across traditions, as Maxwell's equations explain why light is electromagnetic. It does not *reduce* the three traditions to a single substrate, as the electroweak theory reduces electromagnetism and the weak force to a single gauge field. It reveals shared structure -- and argues that the shared structure is deep enough to be illuminating -- but it does not claim more than that.

**The Erlangen Programme as precedent.** The most apt precedent for the present work is not Maxwell or Darwin but Felix Klein's Erlangen Programme (1872). Klein "unified" the many geometries that had proliferated in the nineteenth century -- Euclidean, affine, projective, hyperbolic -- by characterising each as the study of invariants under a specific transformation group. This unification is widely regarded as a genuine and lasting intellectual achievement, yet it is precisely the kind of structural unification at issue here. Klein did not claim that Euclidean geometry and projective geometry are "the same subject" in the way that electricity and magnetism are the same field. He showed that they share a common *schema* -- a group acting on a space -- and that the relationships between geometries correspond to inclusion relationships between their symmetry groups. The schema illuminated the structure of geometry without collapsing its diversity.

As Eilenberg and Mac Lane noted in their seminal 1945 paper introducing categories, the categorical perspective "may be regarded as a continuation of the Klein Erlanger Programm, in the sense that a geometrical space with its group of transformations is generalized to a category with its algebra of mappings." The present work takes this genealogy seriously: it proposes an Erlangen Programme for the formal study of meaning, in which each tradition of semantics is characterised by its functorial passage from syntax to semantics, and the relationships between traditions correspond to relationships between their categorical structures.

This positioning has consequences for what the dissertation claims and does not claim:

- **Claimed:** The three traditions of compositional formal semantics share a common categorical architecture -- the functorial passage from a syntactic category to a semantic category -- and this architecture is deep enough to generate productive insights, concrete mathematical results, and a framework for comparing traditions.
- **Not claimed:** That the three traditions are "really the same subject," that the categorical architecture generates novel empirical predictions about language or cognition, or that the architecture captures the full range of meaning (including pragmatics, embodied meaning, and non-compositional phenomena).
- **Not claimed:** Scientific unification in the sense of Maxwell or Darwin. The evidence supports shared mathematical structure, not shared underlying process.

### 1.4 The Central Claim (Recalibrated)

With this philosophical framing in place, the central claim can be stated:

**The compositional, type-driven core of formal meaning -- across the logical, computational, and linguistic traditions -- admits structural unification under a single categorical architecture: the functorial passage from a syntactic category to a semantic category.**

More precisely: there exists a family of categories **Syn** (syntactic categories) and a *fibred family* of categories **Sem** (semantic categories, parametrised by the choice of interpretive tradition and semantic domain) such that, for each tradition of formal semantics, meaning assignment is a functor F: **Syn** -> **Sem**. The syntactic categories are the categories of grammatical derivations (in linguistics), proof trees (in logic), and typed lambda terms (in computation). The semantic categories are the categories of model-theoretic denotations (in logic), domain-theoretic values (in computation), and intensional or distributional meanings (in linguistics). The Curry-Howard-Lambek correspondence guarantees that the syntactic categories are equivalent; the eight bridges of RP-01 guarantee that the functorial passage from syntax to semantics has the same structural character in all three traditions.

The architecture of compositional formal meaning is the architecture of this functorial passage. Its value lies not in collapsing distinctions but in making the shared structure explicit -- as the Erlangen Programme made the shared structure of geometries explicit -- so that insights from one tradition can be systematically transported to others.

### 1.5 Scope and Limitations

The scope of this dissertation is necessarily circumscribed. A synthesis that spans formal language theory, type theory, proof theory, category theory, model-theoretic semantics, distributional semantics, and the philosophy of unification cannot achieve the depth of a monograph focused on any one of these fields. The compensating virtue is architectural: by assembling the components into a single structure, the dissertation reveals the shape of the whole in a way that is invisible from within any single component.

**What falls outside scope.** The following are explicitly acknowledged as outside the architecture's reach:

- *Pragmatics.* Conversational implicature (Grice 1975), speech acts (Austin 1962; Searle 1969), presupposition, and discourse-level meaning beyond compositional sentence semantics.
- *Embodied and grounded meaning.* The embodied cognition tradition (Lakoff and Johnson 1980; Varela, Thompson, and Rosch 1991) and grounded semantics (Harnad 1990; Barsalou 1999).
- *Non-compositional phenomena.* Idioms, metaphor, co-predication, and other constructions that resist compositional analysis.
- *Dynamic meaning in its full generality.* Dynamic semantics (Heim 1982; Kamp 1981; Groenendijk and Stokhof 1991) is partially addressed through the topos-theoretic perspective but not fully incorporated.
- *Game-theoretic and inferential meaning.* Game semantics (Hintikka 1996; Abramsky 1997) and inferential semantics (Brandom 1994; Prawitz 2006) are touched on but not systematically integrated.
- *Probabilistic and Bayesian meaning.* The rational speech act framework (Frank and Goodman 2012) and probabilistic semantics.

The title has been revised from "The Architecture of Formal Meaning" to "The Architecture of Compositional Formal Meaning" to reflect this scope. The claim is about the compositional, typed core -- not about meaning in its full range.

The remainder of the dissertation is organised as follows. Section 2 recapitulates the results of RP-01 and RP-06, identifying overlap and divergence. Section 3 constructs the categorical architecture with the tightened categorical claims. Section 4 states and evaluates the unification claim. Section 5 addresses the distributional challenge with an honest assessment of DisCoCat and transformers. Section 6 offers discussion. Section 7 concludes.

---

## 2. Recapitulation: The Eight Bridges and the Fourfold

This section summarises the two prior investigations -- RP-01's taxonomy of cross-domain semantic bridges and RP-06's fourfold grammar-type-proof-category correspondence -- and maps their regions of overlap and divergence. The summary is necessarily compressed; the reader is referred to the full texts of RP-01 and RP-06 for detailed exposition and formal argument.

### 2.1 Summary of RP-01: The Bridge Taxonomy

RP-01 identified eight structural bridges connecting the three traditions of formal semantics. Each bridge was assessed for structural strength on a four-point scale:

1. **Compositionality** (Frege's Principle). In all three traditions, meaning is assigned by a structure-preserving map (homomorphism) from a syntactic algebra to a semantic algebra. The algebraic formulation is identical across traditions: the relationship between syntax and semantics is, in each case, the same mathematical concept instantiated in different domains. **Structural strength: isomorphism.**

2. **Lambda calculus**. Church's lambda calculus is, simultaneously and non-metaphorically, the foundation of functional programming, the notation of Montague grammar, and a proof-term calculus for intuitionistic logic. **Structural strength: isomorphism.**

3. **The Curry-Howard-Lambek correspondence**. The three-way equivalence of proofs, programmes, and categorical morphisms is an isomorphism in the strongest sense: precise, invertible translations exist between the three presentations, preserving composition, identity, and typing. The extension to natural language, via the type-logical tradition and combinatory categorial grammar, is a homomorphism: it captures the compositional, type-driven aspects but does not extend to pragmatics, context-dependence, or distributional meaning. **Structural strength: isomorphism (three-way); homomorphism (extension to natural language).**

4. **Type theory**. Types classify meanings in all three traditions: they sort entities into kinds, constrain well-formedness, and drive composition. The role of types is structurally parallel, but the type systems differ in important respects. **Structural strength: homomorphism.**

5. **Model theory**. In all three traditions, a central approach to semantics proceeds by defining an interpretation: a mapping from syntactic expressions to elements of a mathematical structure (a model). **Structural strength: isomorphism (for classical fragments).**

6. **Game semantics**. Independently developed in all three traditions -- dialogical logic (Lorenzen, Lorenz), game-theoretical semantics for natural language (Hintikka), and game semantics for programming languages (Abramsky, Hyland, Ong). **Structural strength: homomorphism.**

7. **Dynamic semantics**. The treatment of meaning as context-change potential (state transformation), the default view in programming language semantics and revolutionary in natural language semantics (Heim 1982; Kamp 1981). **Structural strength: analogy tending toward homomorphism.**

8. **Proof-theoretic semantics**. Meaning located in inferential role rather than denotation: introduction and elimination rules in logic, constructors and destructors in programming, inferential articulation in philosophy. **Structural strength: homomorphism.**

The hierarchy of bridge strengths reveals a pattern: the bridges closest to the classical, compositional, typed core achieve isomorphism; those that extend the core achieve homomorphism; and those at the dynamic periphery are analogies under active formalisation.

### 2.2 Summary of RP-06: The Fourfold Correspondence

RP-06 established a correspondence extending the classical Chomsky hierarchy into the type-theoretic domain:

| Level | Grammar | Automaton | Type System | Logic |
|-------|---------|-----------|-------------|-------|
| Type 3 | Regular | Finite automaton | Finite types, enumerations | Propositional (decidable fragment) |
| Type 2 | Context-free | Pushdown automaton | Recursive algebraic types | First-order (decidable fragment) |
| Type 1 | Context-sensitive | Linear bounded automaton | Parametric polymorphism, refinement types | Second-order logic |
| Type 0 | Unrestricted | Turing machine | Full dependent types | Higher-order logic (undecidable) |

The fourfold was rendered fully explicit in the Curry-Howard-Lambek triangle extended to include grammars:

| Grammar | Logic | Computation | Category |
|---------|-------|-------------|----------|
| Syntactic category | Proposition | Type | Object |
| Grammatical derivation | Proof | Programme | Morphism |
| Category A/B | Implication | Function type | Exponential |
| Sentence formation | Modus ponens | Application | Evaluation |
| Lexicon | Axioms | Constants | Generators |

### 2.3 Where They Overlap

RP-01 and RP-06 converge on three critical structures:

**The Curry-Howard-Lambek correspondence.** Both investigations identify this three-way (or four-way, with grammars included) correspondence as the deepest known structural bridge. The treatments are mutually reinforcing: RP-01 provides the semantic dimension (the correspondence connects three traditions of *meaning*), while RP-06 provides the syntactic dimension (the correspondence connects four formal *structures*).

**Categorial grammar and the Lambek calculus.** Both investigations identify categorial grammar as the framework in which the grammar-logic-computation-category correspondence becomes linguistically concrete.

**Lambda calculus as the shared formal system.** Both investigations identify lambda calculus as the formal system that is, non-metaphorically, the same in all three traditions.

**Compositionality as the structural principle.** RP-01 formalises compositionality as a homomorphism from syntactic algebras to semantic algebras. RP-06 identifies compositionality as the consequence of the typed structure of categorial grammar: when syntax is typed and semantics is a type-preserving interpretation, compositionality follows as a theorem rather than an assumption.

### 2.4 Where They Diverge

The divergences between RP-01 and RP-06 mark the boundaries of the unified architecture.

**Dynamic and game semantics (RP-01 only).** These concern the *nature of meaning* (meaning as state transformation, meaning as interactive strategy) rather than the *structure of syntax*. The categorical architecture must accommodate both, but these phenomena lie closer to the architecture's boundary than to its core.

**Automata theory (RP-06 only).** The grammar-automaton correspondence provides the *operational* or *intensional* characterisation of syntactic complexity, complementing the *generative* and *logical* characterisations.

**The mildly context-sensitive problem (RP-06 only).** The type-theoretic characterisation of mildly context-sensitive languages -- the conjectured complexity class of natural language -- remains an open problem that the categorical architecture must eventually address.

**Distributional semantics (treated differently).** RP-01 devotes substantial attention to the distributional and neural challenge. RP-06 mentions it as an open question. The present synthesis addresses the distributional challenge in Section 5 with greater empirical honesty than either prior work.

---

## 3. The Categorical Architecture

This section constructs the categorical architecture of compositional formal meaning. The architecture has seven components, developed in sequence: meaning as functor (Section 3.1), compositionality as functoriality (Section 3.2), the Lambek calculus as the syntactic category (Section 3.3), Montague's rule-to-rule correspondence as natural transformation (Section 3.4), the DisCoCat framework (Section 3.5), compact closed categories and pregroup grammars (Section 3.6), and the topos-theoretic perspective with a worked example (Section 3.7).

### 3.1 Meaning as Functor: The Fibred Perspective

The central organising concept of the categorical architecture is the treatment of meaning as a functor. In category theory, a functor F: **C** -> **D** is a structure-preserving map between categories: it sends objects of **C** to objects of **D** and morphisms of **C** to morphisms of **D**, preserving composition and identity. That is, F(g . f) = F(g) . F(f) for any composable morphisms f and g, and F(id_A) = id_{F(A)} for any object A.

The claim that meaning is a functor asserts that there is a syntactic category **Syn** and a semantic category **Sem**, and that meaning assignment is a functor F: **Syn** -> **Sem**. The force of this claim lies not in the abstract assertion -- which, once category theory is adopted as the metalanguage, is the *natural* way to express structure-preservation -- but in the identification of what the "structure" is that is being preserved, and in the consequences that flow from taking the identification seriously across multiple traditions.

**Why "almost tautological" is a feature, not a bug.** The first draft of this paper conceded that the claim "meaning is a functor" is "almost tautological -- it merely says that meaning is a structure-preserving map." The TRP review rightly identified this concession as problematic. On reflection, the apparent tautological character of the claim is better understood as evidence of its *naturality* -- in both the ordinary and the categorical sense. That the functorial perspective arises independently in logical semantics (Tarskian interpretation), programming language semantics (denotational semantics), and natural language semantics (Montague's rule-to-rule hypothesis) is not evidence of vacuity but evidence that the concept of structure-preserving meaning assignment was already latent in all three traditions before it was made explicit in categorical terms. The Erlangen Programme was similarly "tautological" in the sense that geometers had always studied invariants under transformations; Klein's contribution was to make the schema explicit and thereby reveal the hierarchy of geometries. Analogously, semanticists in all three traditions had always been constructing functors from syntax to semantics; the present work's contribution is to make this schema explicit and thereby reveal the architecture of formal meaning.

The more substantive issue, raised by TRP POV 1, is that the paper treated "the syntactic category" and "the semantic category" as if each tradition provides a single, canonical category. In practice, the choice of semantic category is not unique and carries significant consequences:

- For logical semantics, **Sem** may be the category **Set** (classical model theory), the effective topos (constructive semantics), or the category of Kripke presheaves (modal semantics).
- For programming language semantics, **Sem** may be **Dom** (Scott domains with continuous functions), **CPO** (complete partial orders), or the Kleisli category of an appropriate monad (for effectful computation).
- For natural language semantics, **Sem** may be **Set** (extensional Montague semantics), a functor category [**W**, **Set**] (intensional semantics over possible worlds), or **FdVect** (distributional semantics).

This multiplicity means that the "unified functorial passage" is not a single functor but a *family* of functors, parametrised by the choice of semantic category. The correct framework for making this precise is that of *indexed* or *fibred* categories (Grothendieck 1971; Jacobs 1999).

**The fibred formulation.** Let **T** be the category of *interpretive traditions* -- a category whose objects are the various choices of semantic domain (Set, Dom, FdVect, Kripke presheaves, etc.) and whose morphisms are functors between them that preserve the relevant structure (forgetful functors, change-of-base functors, adjunctions). The semantic categories form a *fibration* p: **Sem** -> **T**, where the fibre over each tradition t in **T** is the semantic category **Sem**_t appropriate to that tradition. The meaning functor is then a *section* of this fibration: a family of functors F_t: **Syn** -> **Sem**_t, one for each tradition, that are coherent with respect to the morphisms in **T**.

This fibred formulation is *stronger* than the single-functor claim, not weaker. It says that there is not merely a single functor but a *parametrised family* of functors with a uniform categorical description, and that the relationships between different semantic traditions (the morphisms in **T**) are themselves functorial. The fibration captures both the unity (all traditions share the same schema: functor from syntax to semantics) and the diversity (different traditions use different semantic categories, and these differences are systematically related).

The functorial perspective unifies the three traditions as follows:

**In logical semantics.** The syntactic category is the category of formulae and proofs in a formal system. The semantic category is the category of models and model homomorphisms (**Set** for classical logic, Kripke presheaves for modal logic, the effective topos for constructive logic). The meaning functor assigns to each formula a semantic domain and to each proof a function between domains. Tarskian satisfaction is the instantiation of this functor for first-order logic; Kripke semantics is its instantiation for modal logic.

**In programming language semantics.** The syntactic category is the category of types and typed terms. The semantic category is the category of domains and continuous functions (denotational semantics), or configurations and transition relations (operational semantics), or specifications and refinement relations (axiomatic semantics). The compositionality of denotational semantics -- Scott and Strachey's foundational design decision -- is precisely the functoriality of this functor.

**In natural language semantics.** The syntactic category is the category of syntactic types and grammatical derivations (in a categorial grammar). The semantic category is the category of semantic types and typed lambda terms operating on model-theoretic structures. Montague's rule-to-rule hypothesis is precisely the assertion that this functor exists.

### 3.2 Compositionality as Functoriality

The identification of compositionality with functoriality is not new -- it has been observed by Janssen (1997), Hodges (2001), and others -- but its consequences for the architecture of meaning deserve explicit development.

Janssen's algebraic characterisation of Montague grammar treats the syntax of a language as a *many-sorted algebra*. The syntactic algebra **A**_syn has sorts corresponding to syntactic categories and operations corresponding to syntactic rules. The semantic algebra **A**_sem has sorts corresponding to semantic types and operations corresponding to semantic combination rules. Montague's principle of compositionality asserts that there exists a homomorphism h: **A**_syn -> **A**_sem. This is precisely the assertion that meaning assignment is a functor, expressed in the language of universal algebra rather than category theory.

The categorical formulation has the advantage of generality. A many-sorted algebra is a special case of a category (an algebra with one object per sort); a homomorphism of algebras is a special case of a functor. By moving from algebras to categories, the framework accommodates structures that are more general than algebras: derivations with internal structure, relations between derivations, and higher-order structure. This additional generality is needed to account for phenomena such as syntactic ambiguity, scope ambiguity, and discourse structure.

The functorial formulation also makes precise the sense in which compositionality can *fail*. A failure of compositionality is a failure of the meaning map to be a functor: a case in which F(g . f) is not equal to F(g) . F(f). Idioms provide the canonical example. In the functorial framework, this failure can be diagnosed precisely: either the syntactic derivation of the idiomatic reading differs from that of the literal reading, or the meaning map is not functorial for this fragment. Both diagnoses have been pursued in the literature.

In programming language semantics, the compositionality failures identified by RP-01 -- exceptions, continuations, mutable state, concurrency -- correspond to cases in which the meaning functor must be extended from a simple functor F: **Syn** -> **Sem** to a functor into a richer semantic category. Moggi's (1991) monadic framework formalises this extension: the semantic category becomes the Kleisli category of a monad T. The meaning functor F: **Syn** -> **Kleisli**(T) preserves composition in the monadic sense. This is compositionality restored, not abandoned -- but restored at the cost of enriching the semantic category.

The parallel between monadic enrichment in programming language semantics and coercion/type-shifting in natural language semantics is striking and underexplored. In both cases, compositionality is maintained by enriching the semantic framework. A systematic comparison of these enrichment strategies, framed categorically, would constitute a significant contribution. The present dissertation identifies the parallel and marks it as a direction for future research.

### 3.3 The Lambek Calculus as the Syntactic Category

The Lambek calculus, introduced by Joachim Lambek in 1958, provides the canonical syntactic category for the categorical architecture. In the Lambek calculus, every word of a language is assigned a syntactic type (category), and the grammar has no phrase-structure rules -- only type assignments and the principle of function application. A word of type A/B combines with an adjacent word of type B on its right to produce a constituent of type A; a word of type B\A combines with an adjacent word of type B on its left to produce a constituent of type A.

The Lambek calculus is a *logic*: it has introduction and elimination rules for its connectives, and a derivation is a proof. This is the linguistic incarnation of the Curry-Howard correspondence: syntactic categories are propositions, grammatical derivations are proofs.

As a category, the Lambek calculus forms the *free residuated monoid* generated by the basic syntactic types. The residuation laws encode the adjunction:

A . B -> C if and only if A -> C / B if and only if B -> A \ C

In categorical terms, the Lambek calculus is a *biclosed monoidal category*. The non-commutativity of the product reflects word order.

The significance of the Lambek calculus for the architecture is threefold. First, it provides a *concrete* syntactic category. Second, it connects to logic: syntactic types are propositions in a substructural logic. Third, it connects to computation: via the Curry-Howard correspondence, derivations correspond to lambda terms.

The substructural character deserves emphasis. The Lambek calculus lacks exchange (commutativity), weakening, and contraction. These absences connect it to linear logic (Girard 1987), establishing a link between linguistic structure and resource-sensitive computation.

From RP-06's perspective, the Lambek calculus sits at the Type 2 level of the Chomsky hierarchy in its basic form, since the Lambek calculus without product is weakly equivalent to context-free grammars. Extensions with modalities and controlled structural rules can capture mildly context-sensitive phenomena.

### 3.4 Montague's Rule-to-Rule Correspondence as Natural Transformation

Montague grammar implements the meaning functor for natural language by pairing each syntactic rule with a corresponding semantic rule. This pairing -- the rule-to-rule hypothesis -- can be given a precise categorical formulation as a natural transformation.

Consider two functors from the syntactic category **Syn** to the semantic category **Sem**: the *syntactic interpretation functor* S and the *semantic interpretation functor* M. A natural transformation eta: S => M is a family of morphisms eta_A: S(A) -> M(A), one for each syntactic type A, such that for every derivation f: A -> B in **Syn**, the following diagram commutes:

```
S(A) --eta_A--> M(A)
 |                |
S(f)             M(f)
 |                |
 v                v
S(B) --eta_B--> M(B)
```

The commutativity of this diagram is precisely the rule-to-rule hypothesis: the meaning of a derived expression (obtained by applying a syntactic rule and then interpreting semantically) is the same as the meaning obtained by first interpreting the parts semantically and then applying the corresponding semantic rule. The naturality condition ensures that meaning assignment is *uniform* and *systematic*.

The natural transformation formulation also provides a framework for analysing failures of the rule-to-rule correspondence. Scope ambiguity provides an example: the sentence "Every student read a book" has two readings corresponding to two different derivations that produce the same surface string. In the categorical framework, this is diagnosed as a failure of the meaning functor to be *faithful* (injective on morphisms).

The intensional dimension adds further structure. Montague's intensional logic assigns to each expression not an extension but an intension (a function from possible worlds to extensions). Categorically, the move from extensional to intensional semantics is the move from functors **Syn** -> **Sem** to functors **Syn** -> [**W**, **Sem**], where **W** is the (discrete) category of possible worlds. This move is itself natural in the fibred framework of Section 3.1: the change from extensional to intensional semantics is a morphism in the base category **T** of interpretive traditions, and the corresponding change in the meaning functor is the reindexing along this morphism in the fibration.

### 3.5 The DisCoCat Framework: Promise, Proof of Concept, and Empirical Limits

The DisCoCat framework (Categorical Compositional Distributional semantics), introduced by Coecke, Sadrzadeh, and Clark (2010), is the most sustained attempt to bridge the formal-compositional and distributional-statistical traditions of semantics within a categorical framework. Its significance for the architecture is that it demonstrates the *in-principle feasibility* of incorporating distributional meaning into the functorial architecture. Its limitation -- which must be stated with equal force -- is that this feasibility has been demonstrated only at the scale of toy examples, and the framework has not progressed beyond proof-of-concept stage in over fifteen years.

**The theoretical contribution.** The key observation underlying DisCoCat is that pregroup grammars (Lambek 1999, 2001) and the category of finite-dimensional vector spaces (**FdVect**) share a common categorical structure: both are compact closed categories (with the important caveat discussed in Section 3.6). DisCoCat exploits this shared structure to define meaning as a functor from grammar to vector spaces. Formally, a DisCoCat model is a strong monoidal functor:

F: **G** -> **FdVect**

where **G** is the free rigid category generated by the pregroup grammar. This functor assigns vector spaces to basic types and tensors to words. The meaning of a sentence is computed by applying the linear map determined by the grammatical derivation to the tensor product of the word vectors.

The functorial character ensures that meaning is computed *compositionally* from the meanings of words, with composition governed by grammatical structure. The distributional hypothesis provides lexical meanings (word vectors); the categorical framework provides compositional structure; the functor provides the bridge. The result is a framework in which "dog bites man" differs from "man bites dog" because different grammatical derivations produce different linear maps.

**The empirical record: an honest assessment.** DisCoCat models have been tested on small-scale sentence similarity tasks (Grefenstette and Sadrzadeh 2011; Kartsaklis et al. 2012) and compositional tasks involving simple transitive sentences. On these restricted benchmarks, DisCoCat sometimes matches or slightly outperforms additive baselines. But these are toy benchmarks by the standards of modern NLP. DisCoCat has not been demonstrated on:

- Machine translation at scale (WMT benchmarks)
- Open-domain question answering (Natural Questions, TriviaQA)
- Summarisation (CNN/DailyMail, XSum)
- Dialogue systems (MultiWOZ, PersonaChat)
- Any task requiring reasoning over paragraphs rather than single sentences

The claim in the first draft of this paper -- that DisCoCat "demonstrates that reconciliation is *feasible*" -- was misleading. DisCoCat demonstrates that reconciliation is feasible *in principle*, for sentences of two or three words consisting of subject-verb-object triples. It is a proof of *categorical concept*: it shows that a strong monoidal functor from a pregroup grammar to **FdVect** can be defined, and that this functor captures word-order-sensitive composition. It does not show that this approach scales to real language processing, and after more than fifteen years of development, the scaling gap remains open.

This honest assessment does not diminish DisCoCat's theoretical contribution to the architecture. The proof of categorical concept is genuine: it establishes that the compositional-distributional divide is not an in-principle barrier but a practical challenge. The divide can, in principle, be bridged by a functor. That the bridge has not yet been engineered to carry real traffic is a statement about the current state of the art, not about the mathematical possibility.

**Limitations.** Beyond scalability, DisCoCat faces three structural limitations. First, **FdVect** cannot directly represent logical operations (negation, quantification, modality) that are central to formal semantics. Extensions to density matrices and the category of relations (**Rel**) are being explored. Second, pregroup grammars are weakly equivalent to context-free grammars, which are insufficient for the full range of natural language phenomena. Third, the tensor representations of words grow exponentially with the arity of the word's type, creating practical difficulties for relational words with complex type structures.

### 3.6 Compact Closed Categories and the Symmetric/Non-Symmetric Distinction

The role of compact closed categories in the architecture warrants careful treatment, particularly regarding a subtlety that the first draft of this paper elided.

A compact closed category is a symmetric monoidal category in which every object has a dual satisfying the unit-counit adjunction (the "snake equations"). The canonical example is **FdVect**. A pregroup, viewed as a category, is a *rigid* category -- a *non-symmetric* variant of a compact closed category.

**The subtlety.** Pregroup grammars form rigid categories (non-symmetric compact closed), while **FdVect** is *symmetric* compact closed. The DisCoCat functor therefore maps from a non-symmetric structure to a symmetric one. This has a concrete consequence: the functor cannot be fully faithful, because it must collapse the distinction between left and right adjoints (which are identified in a symmetric setting but distinct in a rigid setting). In linguistic terms, the distinction between subject and object -- encoded in pregroup grammars through left versus right adjoints -- is preserved in DisCoCat models only because the word *tensors* (not the types) differ. The structural preservation is weaker than a naive reading of "meaning is a functor" would suggest.

This is not a fatal objection. The word tensors do carry the information that the types alone do not, so the model correctly distinguishes "dog bites man" from "man bites dog." But it means that the functorial bridge between grammar and distributional semantics involves a *lossy* compression of grammatical information at the type level, compensated by richer structure at the morphism level. Acknowledging this subtlety makes the architecture more honest and the DisCoCat contribution more precisely characterised.

The compact closed structure also provides a diagrammatic calculus: morphisms in both pregroups and **FdVect** can be represented as string diagrams, and equality of morphisms can be verified by topological deformation. This diagrammatic calculus, imported from categorical quantum mechanics (Abramsky and Coecke 2004), provides an intuitive method for reasoning about meaning composition. The connection to quantum mechanics is not merely formal but has led to the development of quantum natural language processing (QNLP), which implements DisCoCat models on quantum computers via the lambeq framework (Kartsaklis et al. 2021).

### 3.7 The Topos-Theoretic Perspective: Presheaf Semantics for Contextual Meaning

A topos is a category that behaves like a generalised universe of sets. Every topos has an internal logic that is intuitionistic and higher-order, and every topos provides a model of intuitionistic higher-order logic. The topos-theoretic perspective provides a framework for modelling *contextual meaning* -- meaning that varies across contexts, perspectives, or information states.

**The general framework.** A presheaf over a category of contexts **C** is a functor F: **C**^op -> **Set** that assigns to each context c a set F(c) of "elements in context c" and to each context morphism f: c -> c' a function F(f): F(c') -> F(c) that translates elements across contexts. The presheaf condition -- that the translations are functorial -- is the formal expression of the *coherence* of contextual meaning.

The sheaf condition adds a *gluing* requirement: if the meaning in each of several overlapping contexts is specified, and the specifications agree on the overlaps, then there is a unique meaning in the joint context. In linguistic terms, the sheaf condition formalises discourse coherence.

**Worked example: anaphora resolution as a sheaf condition.** To move beyond the programmatic, consider the concrete phenomenon of anaphora resolution -- the process by which a pronoun is linked to its antecedent across sentences.

Let the category of contexts **C** be the category of *discourse states*, where an object is a set of available discourse referents and a morphism i: D -> D' (where D is a subset of D') is an *extension* that introduces new referents. This gives **C** the structure of a poset category (ordered by inclusion of referent sets).

Define a presheaf R: **C**^op -> **Set** that assigns to each discourse state D the set R(D) of *possible referent assignments* -- functions from the pronouns in the current sentence to the available referents in D. For a context extension i: D -> D', the restriction map R(i): R(D') -> R(D) restricts assignments to the smaller set of referents.

Now consider a two-sentence discourse:

(1) "A farmer owns a donkey."
(2) "He beats it."

After sentence (1), the discourse state is D_1 = {farmer, donkey}. Sentence (2) introduces pronouns "he" and "it" that must be resolved against D_1. The presheaf R assigns to D_1 the set of possible assignments: {he -> farmer, it -> donkey} (plus other combinatorial possibilities).

The *sheaf condition* enters when we consider the discourse as a whole. Suppose we have two overlapping "contexts" for interpreting sentence (2): one in which "he" is resolved (the context of the subject), and one in which "it" is resolved (the context of the object). Each partial context provides a partial assignment. The sheaf condition says: if the partial assignments are *compatible* (they do not contradict each other on the overlap), then there is a unique *total* assignment that extends both. This is precisely the condition for successful anaphora resolution: the pronouns must be resolvable in a way that is coherent across all positions in the sentence.

When the sheaf condition *fails* -- when the partial assignments are incompatible -- we get the formal diagnosis of an anaphoric failure: a discourse in which the pronouns cannot be consistently resolved. The classic "donkey sentences" of dynamic semantics (Kamp 1981; Heim 1982) can be analysed in this framework: the challenge they pose is precisely that the standard compositional semantics does not generate the right presheaf (the right set of available referents at each discourse state), and the dynamic semantic accounts of Kamp and Heim can be understood as constructing a different presheaf that does.

This example is deliberately simple, but it illustrates the topos-theoretic perspective concretely. The presheaf captures context-dependence; the sheaf condition captures coherence; and the failure of the sheaf condition diagnoses incoherence. A fuller development would address more complex phenomena (presupposition accommodation, modal subordination, temporal anaphora), but the basic mechanism -- presheaves over discourse states, with the sheaf condition enforcing coherence -- is the same.

**Connections to the architecture.** The topos-theoretic perspective connects to the categorical architecture in three ways. First, a topos is a cartesian closed category, so compositional, type-driven semantics is available *within* any topos. Second, the subobject classifier of a topos provides non-classical truth values, suitable for modelling vagueness and graded truth. Third, the internal logic of a topos is intuitionistic, connecting to the constructive tradition and the Curry-Howard-Lambek correspondence.

---

## 4. The Unification Claim

### 4.1 What Is Unified (and What Is Not)

The categorical architecture constructed in Section 3 structurally unifies the *compositional, type-driven core* of four formally distinct domains:

1. **Grammar.** The structure of well-formed expressions, captured by categorial grammars and the Lambek calculus.
2. **Logic.** The structure of valid inference, captured by proof systems.
3. **Computation.** The structure of typed programmes, captured by typed lambda calculi.
4. **Natural language semantics.** The structure of compositional linguistic meaning, captured by Montague grammar and its extensions.

These four domains share a common categorical skeleton:

- Objects (syntactic types, propositions, programme types, semantic types).
- Morphisms (derivations, proofs, programmes, meaning-compositions).
- Composition of morphisms.
- Identity for each object.
- Functors between the syntactic and semantic aspects.
- Natural transformations between functors (coherence conditions).

The claim is that this shared skeleton reflects a genuine structural identity: the four domains instantiate the same mathematical schema, and the schema is deep enough to support systematic transfer of results. This is *structural unification* in the Erlangen sense -- not scientific unification in the Maxwell sense.

**What is not unified.** The architecture does not unify:
- Pragmatic meaning with compositional meaning.
- Distributional meaning with truth-conditional meaning (though DisCoCat shows the bridge is categorically possible).
- The formal structure of meaning with the neural mechanism of meaning processing.
- Compositional semantics with embodied, grounded, or enactive approaches to meaning.

These limitations are not merely boundary conditions to be noted in passing. They define the actual scope of the result. The architecture captures the compositional core -- and the compositional core is substantial, encompassing the Curry-Howard-Lambek correspondence, Montague semantics, denotational semantics, and their categorical generalisations. But it is a core, not the whole.

### 4.2 The Five-Way Correspondence

The unification claim can be stated as a five-way correspondence:

| Grammar | Logic | Computation | Category | Semantics |
|---------|-------|-------------|----------|-----------|
| Syntactic type | Proposition | Type | Object | Semantic type |
| Derivation | Proof | Programme | Morphism | Meaning-composition |
| Concatenation | Conjunction | Product type | Categorical product | Conjunction of meanings |
| Slash type (A/B) | Implication (A => B) | Function type (A -> B) | Exponential object | Functional meaning |
| Sentence derivation | Theorem proof | Well-typed term | Composed morphism | Sentence meaning |
| Lexicon | Axioms | Constants/primitives | Generators | Lexical meanings |
| Grammaticality | Provability | Well-typedness | Existence of morphism | Meaningfulness |
| Ambiguity | Multiple proofs | Multiple terms | Multiple morphisms | Multiple readings |
| Meaning assignment | Soundness/completeness | Adequacy/full abstraction | Functorial image | Semantic evaluation |
| Compositionality | Cut elimination | Beta-reduction | Composition law | Frege's principle |

This five-way table extends RP-06's four-way table by adding a fifth column for semantics, drawn from RP-01. The addition of the semantic column is the distinctive contribution of the present synthesis.

**The correspondence as a commutative diagram.** The five-way correspondence can be represented as a diagram with **Syn** at the apex and four semantic categories at the base, connected by functors and related by natural transformations:

```
                          Syn
                        / | \ \
                       /  |  \ \
                      /   |   \ \
                     v    v    v  v
                F_L  F_D  F_V  F_P
                 |    |    |    |
                 v    v    v    v
               Sem_L Sem_D Sem_V Sem_P
                 \    |    |   /
                  \   |    |  /
              U_LD \ U_DV  | / U_VP
                    v v    v v
                  (natural transformations
                   witnessing coherence)
```

where:
- **Syn** = the syntactic category (Lambek calculus / categorial grammar)
- F_L = the logical meaning functor (Syn -> **Sem_L** = **Set** or Kripke presheaves)
- F_D = the domain-theoretic meaning functor (Syn -> **Sem_D** = **Dom** or **CPO**)
- F_V = the distributional meaning functor (Syn -> **Sem_V** = **FdVect**, via DisCoCat)
- F_P = the proof-theoretic meaning functor (Syn -> **Sem_P** = proof-relevant interpretations)
- U_LD, U_DV, U_VP = natural transformations between the functors, witnessing that the different semantic interpretations of the same syntactic structure are coherently related.

The natural transformations U at the base are the formal expression of the "bridges" identified by RP-01. The commutativity conditions they must satisfy -- that the semantic interpretation obtained by composing functors through one path equals that obtained through another -- are the precise mathematical content of the unification claim. Where the conditions hold, the architecture succeeds; where they fail, the architecture encounters its boundary conditions.

In the fibred formulation of Section 3.1, this diagram is the *total space* of the fibration p: **Sem** -> **T**, with **Syn** mapping into each fibre, and the U maps arising from the reindexing functors of the fibration.

### 4.3 Evidence for the Claim

The evidence for the five-way correspondence is of three kinds:

**Formal evidence.** Mathematical theorems establish precise correspondences between pairs of columns: Curry-Howard (logic-computation), Lambek's theorem (computation-category), the weak equivalence of the Lambek calculus with context-free grammars (grammar-logic), Montague's rule-to-rule hypothesis (grammar-semantics), and adequacy/full abstraction results (computation-semantics). Each has been proven rigorously.

**Structural evidence.** The eight bridges of RP-01 show that the same mathematical concepts appear with the same structural character across traditions. The fourfold of RP-06 shows that the same hierarchy of complexity appears in grammars, automata, type systems, and logics. The coincidence of these parallel structures across independently developed traditions is strong evidence of underlying structural unity.

**Historical evidence.** The pattern of convergent discovery -- Chomsky and Backus independently discovering context-free grammars; Curry and Howard independently discovering the proofs-as-programmes correspondence; game semantics independently developed in logic, natural language, and computer science -- is the hallmark of a genuine structural unity rather than a projection of one discipline's concepts onto another.

### 4.4 Evidence Against: Where the Correspondence Fails

**Pragmatics and non-compositionality.** Natural language meaning is pervasively context-dependent in ways that have no natural counterpart in logic or computation. These phenomena do not refute the compositional core but show that the architecture captures only a *fragment* of natural language meaning.

**Neural representations and opacity.** Modern neural language models achieve remarkable performance, yet their internal representations do not obviously correspond to the typed, compositional structures of the categorical architecture. The question of whether neural representations *can be* categorified is open. (This challenge is addressed in Section 5.)

**Concurrency and interaction.** The Curry-Howard-Lambek correspondence applies to *sequential* computation. A full "Curry-Howard for concurrency" remains an open problem. Since natural language discourse is inherently interactive, this limits the architecture's applicability to discourse-level meaning.

**The gap between formal adequacy and empirical coverage.** The architecture describes the *logical space* of meaning, not the *actual mechanism* of meaning. It explains how meaning *could* be structured, not how meaning *is* processed by human cognition.

---

## 5. The Distributional Challenge

### 5.1 Can Vector-Space Semantics Be Categorified?

The distributional tradition represents the meaning of a word as a point in a high-dimensional vector space. Modern incarnations -- word2vec, GloVe, and the contextual embeddings of BERT and GPT -- capture rich semantic information. The question for the categorical architecture is whether this approach can be incorporated as a particular choice of semantic category within the functorial framework.

The answer involves distinguishing *lexical* from *compositional* distributional semantics. At the lexical level, the distributional approach is straightforwardly categorifiable: word meanings are objects in **FdVect**. At the compositional level, naive approaches (additive and multiplicative models) violate functoriality because composition is not governed by syntactic structure. DisCoCat resolves this by making composition structure-dependent, as discussed in Section 3.5.

But the resolution is theoretical, not practical. The gap between DisCoCat's mathematical elegance and its empirical performance must be confronted directly.

### 5.2 Transformers: Confronting Success Without Categorical Structure

The rise of transformer-based language models has transformed the empirical landscape. Transformers learn contextual representations that capture syntactic structure, semantic relations, and aspects of pragmatic reasoning, achieving state-of-the-art performance on a wide range of benchmarks.

The relationship between what transformers learn and what the categorical architecture describes demands honest engagement, not defensive framing.

**What transformers demonstrate.** Transformers demonstrate that a system can translate between languages, answer questions about complex texts, generate coherent multi-paragraph prose, and perform zero-shot reasoning -- all without implementing the categorical architecture described in this paper. This is not a minor observation. If meaning can be computed (or at least closely approximated) without the functorial passage from syntax to semantics, then the burden of proof falls on the architecture to explain what it adds.

**What the architecture adds -- and what it does not.** The categorical architecture offers three things that transformers do not:

1. *Structural transparency.* The architecture makes the compositional structure of meaning explicit and inspectable. Transformers encode structure implicitly, in ways that require probing studies to uncover.

2. *Guaranteed compositionality.* The functorial framework guarantees that meaning composition respects syntactic structure. Transformers approximate this, but the approximation is not exact and fails on certain compositional generalisation tests (Lake and Baroni 2018; Kim and Linzen 2020; Keysers et al. 2020 on COGS).

3. *A framework for comparison.* The architecture provides a common language for comparing different semantic traditions. Transformers provide a single monolithic system that does not distinguish between semantic traditions.

What the architecture does *not* add: empirical performance, scalability, or a mechanism for learning meaning from data. The architecture describes *what* compositional meaning is; transformers provide *a way* to compute meaning (or a close proxy of it). The two are not competitors in the way the first draft of this paper implied. They address different questions. The architecture is a *theory of structure*; transformers are an *engineering achievement*. Comparing them on NLP benchmarks is a category error (no pun intended) -- but this observation does not exempt the architecture from the requirement to engage with the empirical evidence.

**Probing studies and partial compatibility.** Probing studies (Hewitt and Manning 2019; Clark et al. 2019; Jawahar et al. 2019) show that transformers encode syntactic dependency relations in their attention patterns and that syntactic information is distributed across layers in a roughly hierarchical fashion. This suggests that transformers, despite lacking explicit grammatical structure, learn representations that are *partially compatible* with categorial grammar. But "partially compatible" is a weak claim. The representations are distributed, continuous, and contextual -- not the discrete, algebraic structures of the Lambek calculus. The architecture describes the structure of meaning; transformers have found a *different* way to capture the same underlying regularities -- a way that is more flexible, more robust to noise, and empirically more powerful.

**The honest framing.** The first draft framed the relationship as "categorical architecture describes *structure*; transformers implement *mechanism*" and presented this as complementary. A more honest framing: the categorical architecture and transformers may be describing the same phenomena at different levels of abstraction, or they may be describing *different* phenomena that happen to co-occur in language. The question of which is the case is empirical, and the evidence is not yet decisive. What the categorical architecture offers is a *hypothesis* about the structure of meaning -- a hypothesis that can be tested by examining whether systems that explicitly encode categorical structure outperform systems that do not, on tasks that specifically require compositional generalisation.

### 5.3 Testable Predictions

A structural unification that generates no testable predictions risks being unfalsifiable. The following hypotheses are derivable from the categorical architecture and testable via existing experimental paradigms:

**Prediction 1: Compositional vs. non-compositional processing.** The architecture predicts that compositional phenomena (those within the functorial core) and non-compositional phenomena (those outside it) should be processed differently by neural systems. Specifically: transformers should show more systematic, structure-sensitive behaviour on compositional constructions (subject-verb-object composition, adjective-noun modification, relative clause attachment) than on non-compositional constructions (idioms, metaphor, coercion). This can be tested via probing studies that compare the degree to which attention patterns track syntactic derivation structure for compositional vs. non-compositional inputs.

**Prediction 2: Categorical structure improves compositional generalisation.** If the functorial structure captures real regularities, then architectures that explicitly encode categorical structure should outperform standard transformers on tasks requiring compositional generalisation -- tasks like COGS (Kim and Linzen 2020), SCAN (Lake and Baroni 2018), and gSCAN (Ruis et al. 2020), where the test set contains novel combinations of familiar components. The prediction is specific: the improvement should be greatest on constructions that correspond to functor application in the categorical framework and smallest on constructions that fall outside the compositional core.

**Prediction 3: Cross-tradition transfer.** The architecture predicts that compositional patterns identified in one tradition (e.g., type-shifting in natural language semantics) should have precise analogues in other traditions (e.g., monadic lifting in programming language semantics). This is testable by systematic comparison: identify a compositional phenomenon in one tradition, use the five-way correspondence to predict its analogue in another tradition, and verify whether the predicted analogue exists and has the predicted properties.

**Prediction 4: Tensor rank and compositional complexity.** In DisCoCat models, the tensor rank of a word's representation is determined by the complexity of its grammatical type. The architecture predicts that words with more complex grammatical types (higher-arity verbs, complex prepositions, sentential complement verbs) should require higher-rank tensors for adequate representation, and that this requirement should be reflected in the difficulty of learning these representations from corpus data.

These predictions are not revolutionary. They are modest, testable, and specific. They do not constitute the kind of novel prediction that would establish scientific unification in the Maxwell sense. But they provide empirical traction for the structural framework -- a way to move the architecture from philosophical argument to empirical research programme.

---

## 6. Discussion

### 6.1 What the Architecture Achieves

The categorical architecture is both a *synthesis* and a *proposal*. As a synthesis, it combines the results of RP-01 (the eight bridges) and RP-06 (the fourfold correspondence) into a single framework, showing that the bridges and the fourfold are two aspects of a single mathematical structure: the functorial passage from syntax to semantics. As a proposal, it claims that this functorial passage constitutes the *architecture* of compositional formal meaning -- the deep structure common to all compositional, type-driven, formally rigorous approaches to meaning.

The achievements are real but must be stated without inflation:

**Structural transparency.** The architecture provides a single framework in which the results of RP-01 and RP-06 are not merely listed but *connected*. The eight bridges are manifestations of a single functorial structure. The fourfold is the structural characterisation of the syntactic side. The five-way correspondence is the explicit connection between the two.

**Precision.** The categorical formulation replaces informal notions of "analogy" and "correspondence" with precise mathematical concepts: functor, natural transformation, adjunction, fibration. The claims can, in principle, be verified or refuted.

**A framework for comparison.** The fibred formulation (Section 3.1) makes it possible to compare different semantic traditions systematically, by comparing their positions in the fibration over interpretive traditions. This is valuable independently of any claim about "unification."

### 6.2 What the Architecture Does Not Achieve

**It is not scientific unification.** The architecture does not predict novel phenomena, does not identify ontological reductions, and does not explain *why* compositionality holds across traditions. It describes *that* compositionality holds and provides a mathematical framework for stating this precisely. This is the Erlangen Programme level of achievement, not the Maxwell level.

**It does not compete with transformers.** The architecture describes the structure of compositional meaning; transformers compute approximations of meaning. These are different enterprises. The architecture becomes empirically relevant only when its structural predictions (Section 5.3) are tested.

**It does not capture the full range of meaning.** Pragmatics, embodied meaning, non-compositional phenomena, game-theoretic meaning, and probabilistic meaning all fall outside or at the boundary. The architecture captures the compositional core -- a significant but bounded territory.

### 6.3 The Value of Structural Unification

Is structural unification worth having, if it falls short of scientific unification? The precedent of the Erlangen Programme suggests yes. Klein's classification of geometries by their symmetry groups did not explain why Euclidean geometry is useful or predict new geometric theorems. But it provided an intellectual framework that organised the field, clarified relationships between subfields, and enabled systematic transfer of results. The Erlangen Programme is universally regarded as a major intellectual achievement, despite being "merely" structural.

The analogous claim for the present work: the functorial architecture organises the study of formal meaning, clarifies the relationships between logical, computational, and linguistic semantics, and enables systematic transfer (e.g., using monadic techniques from programming language semantics to handle non-compositionality in natural language, or using the Lambek calculus to provide type-theoretic structure for distributional semantics). Whether this is "merely structural" or "genuinely unifying" may be a matter of philosophical taste. What matters is whether the architecture is *productive* -- whether it generates insights, techniques, and results that would not have arisen without it. The evidence of DisCoCat, of the lambeq framework, of the categorical interpretation of attention mechanisms, and of the predictions in Section 5.3 suggests that it is.

### 6.4 Relationship to Existing Literature

The idea that meaning is functorial is not new: it is implicit in Montague's work, explicit in Janssen's algebraic formulations, and central to DisCoCat. The contributions of the present synthesis are: (a) the *systematic* connection of this idea to the full range of bridges identified by RP-01 and correspondences identified by RP-06; (b) the fibred formulation that treats the multiplicity of semantic categories as a feature rather than a problem; (c) the explicit five-way correspondence with its commutative diagram; (d) the worked topos-theoretic example of anaphora resolution; and (e) the honest positioning as structural rather than scientific unification, with testable predictions.

---

## 7. Conclusion

This dissertation has undertaken the synthesis of RP-01 (*Toward a Grand Unified Semantics*) and RP-06 (*Grammars, Types, Proofs, and Categories*) into a single categorical architecture of compositional formal meaning. The synthesis proceeds from a simple observation: RP-01 established that meaning, across three traditions, is a structure-preserving map from syntax to semantics; RP-06 established that syntax, across four formal frameworks, has a unified categorical structure. Combining these results, meaning itself has a unified categorical structure: the *functorial passage from a syntactic category to a fibred family of semantic categories*.

The architecture has been constructed through seven components: meaning as functor (in a fibred setting), compositionality as functoriality, the Lambek calculus as the syntactic category, Montague's rule-to-rule correspondence as natural transformation, DisCoCat (honestly assessed as a proof of categorical concept), compact closed categories (with the symmetric/non-symmetric distinction acknowledged), and presheaf semantics for contextual meaning (with a worked example of anaphora resolution).

The central claim -- the five-way correspondence among derivation, proof, programme, morphism, and meaning-composition -- has been stated precisely, represented as a commutative diagram in the fibred setting, and evaluated against supporting and countervailing evidence. The evidence supports the claim for the classical, compositional, typed core. The boundary conditions -- pragmatics, non-compositionality, embodied meaning, neural mechanisms, and concurrency -- have been honestly acknowledged as falling outside the architecture's scope.

The dissertation has been explicit about the *kind* of unification achieved. This is structural unification in the tradition of Klein's Erlangen Programme: the identification of a common mathematical schema across independently developed traditions. It is not scientific unification in the tradition of Maxwell or Darwin: the architecture does not predict novel phenomena, does not reduce the three traditions to a single substrate, and does not explain why compositionality holds. By Kitcher's criterion, it achieves a modest reduction of explanatory patterns; by Morrison's taxonomy, it achieves structural but not theoretical or reductive unification.

The distributional challenge has been addressed with greater empirical honesty than the first draft. DisCoCat is a proof of categorical concept, not a practical bridge. Transformers compute meaning (or a close approximation) without implementing the categorical architecture, and this success must be confronted rather than explained away. The architecture's empirical relevance depends on the testable predictions identified in Section 5.3 -- predictions about compositional generalisation, cross-tradition transfer, and the relationship between grammatical type complexity and representational requirements.

The prospect of a grand unified semantics -- a single framework encompassing truth-conditional, compositional, distributional, dynamic, interactive, inferential, and embodied meaning -- remains an aspiration beyond the reach of the present work. But the categorical architecture provides a *skeleton* for the compositional core: the functorial passage from syntax to semantics, instantiated across traditions, formalised by category theory, and grounded in the five-way correspondence. The three traditions of compositional formal semantics are three perspectives on a single mathematical structure. The functorial architecture makes this structure explicit. Whether making structure explicit constitutes "unification" depends on one's philosophy of unification. That it constitutes a productive intellectual achievement -- in the tradition of the Erlangen Programme -- the present author submits with confidence.

---

## References

Abramsky, S. (1997). Semantics of interaction: An introduction to game semantics. In A. M. Pitts and P. Dybjer (eds.), *Semantics and Logics of Computation*, pp. 1--31. Cambridge University Press.

Abramsky, S., and Coecke, B. (2004). A categorical semantics of quantum protocols. In *Proceedings of the 19th IEEE Symposium on Logic in Computer Science (LiCS)*, pp. 415--425. IEEE.

Abramsky, S., Jagadeesan, R., and Malacaria, P. (2000). Full abstraction for PCF. *Information and Computation*, 163(2), 409--470.

Ajdukiewicz, K. (1935). Die syntaktische Konnexitat. *Studia Philosophica*, 1, 1--27.

Austin, J. L. (1962). *How to Do Things with Words*. Oxford University Press.

Bar-Hillel, Y. (1953). A quasi-arithmetical notation for syntactic description. *Language*, 29(1), 47--58.

Baroni, M., Bernardi, R., and Zamparelli, R. (2014). Frege in space: A program for compositional distributional semantics. *Linguistic Issues in Language Technology*, 9(6), 5--110.

Barsalou, L. W. (1999). Perceptual symbol systems. *Behavioral and Brain Sciences*, 22(4), 577--660.

Brandom, R. B. (1994). *Making It Explicit: Reasoning, Representing, and Discursive Commitment*. Harvard University Press.

Carpenter, B. (1997). *Type-Logical Semantics*. MIT Press.

Chomsky, N. (1956). Three models for the description of language. *IRE Transactions on Information Theory*, 2(3), 113--124.

Chomsky, N. (1957). *Syntactic Structures*. Mouton.

Chomsky, N. (1959). On certain formal properties of grammars. *Information and Control*, 2(2), 137--167.

Church, A. (1936). An unsolvable problem of elementary number theory. *American Journal of Mathematics*, 58(2), 345--363.

Church, A. (1940). A formulation of the simple theory of types. *Journal of Symbolic Logic*, 5(2), 56--68.

Clark, K., Khandelwal, U., Levy, O., and Manning, C. D. (2019). What does BERT look at? An analysis of BERT's attention. In *Proceedings of the 2019 ACL Workshop BlackboxNLP*, pp. 276--286.

Coecke, B., Sadrzadeh, M., and Clark, S. (2010). Mathematical foundations for a compositional distributional model of meaning. *Linguistic Analysis*, 36(1--4), 345--384.

Coquand, T., and Huet, G. (1988). The calculus of constructions. *Information and Computation*, 76(2--3), 95--120.

Curry, H. B., and Feys, R. (1958). *Combinatory Logic*, Vol. I. North-Holland.

Davidson, D. (1967). Truth and meaning. *Synthese*, 17(1), 304--323.

Devlin, J., Chang, M.-W., Lee, K., and Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. In *Proceedings of NAACL-HLT 2019*, pp. 4171--4186.

Dummett, M. (1991). *The Logical Basis of Metaphysics*. Harvard University Press.

Eilenberg, S., and Mac Lane, S. (1945). General theory of natural equivalences. *Transactions of the American Mathematical Society*, 58(2), 231--294.

Firth, J. R. (1957). A synopsis of linguistic theory, 1930--1955. In *Studies in Linguistic Analysis*, pp. 1--32. Philological Society.

Floyd, R. W. (1967). Assigning meanings to programs. *Mathematical Aspects of Computer Science*, 19, 19--32.

Frank, M. C., and Goodman, N. D. (2012). Predicting pragmatic reasoning in language games. *Science*, 336(6084), 998.

Frege, G. (1879). *Begriffsschrift*. Halle: Louis Nebert.

Frege, G. (1892). Uber Sinn und Bedeutung. *Zeitschrift fur Philosophie und philosophische Kritik*, 100, 25--50.

Gavranovic, B., Lessard, P., Dudzik, A., von Glehn, T., Ao Borges, J., and Mikulik, V. (2024). Categorical deep learning: An algebraic theory of architectures. arXiv:2402.15332.

Girard, J.-Y. (1987). Linear logic. *Theoretical Computer Science*, 50(1), 1--101.

Grefenstette, E., and Sadrzadeh, M. (2011). Experimental support for a categorical compositional distributional model of meaning. In *Proceedings of the 2011 Conference on Empirical Methods in Natural Language Processing*, pp. 1394--1404.

Grice, H. P. (1975). Logic and conversation. In P. Cole and J. L. Morgan (eds.), *Syntax and Semantics*, Vol. 3, pp. 41--58. Academic Press.

Groenendijk, J., and Stokhof, M. (1991). Dynamic predicate logic. *Linguistics and Philosophy*, 14(1), 39--100.

Grothendieck, A. (1971). *Revetements etales et groupe fondamental* (SGA 1). Lecture Notes in Mathematics 224. Springer.

Harnad, S. (1990). The symbol grounding problem. *Physica D*, 42(1--3), 335--346.

Harris, Z. S. (1954). Distributional structure. *Word*, 10(2--3), 146--162.

Heim, I. (1982). *The Semantics of Definite and Indefinite Noun Phrases*. Ph.D. dissertation, University of Massachusetts, Amherst.

Heim, I., and Kratzer, A. (1998). *Semantics in Generative Grammar*. Blackwell.

Hewitt, J., and Manning, C. D. (2019). A structural probe for finding syntax in word representations. In *Proceedings of NAACL-HLT 2019*, pp. 4129--4138.

Hintikka, J. (1996). *The Principles of Mathematics Revisited*. Cambridge University Press.

Hoare, C. A. R. (1969). An axiomatic basis for computer programming. *Communications of the ACM*, 12(10), 576--580.

Hodges, W. (2001). Formal features of compositionality. *Journal of Logic, Language and Information*, 10(1), 7--28.

Howard, W. A. (1980). The formulae-as-types notion of construction. In J. P. Seldin and J. R. Hindley (eds.), *To H. B. Curry: Essays on Combinatory Logic, Lambda Calculus and Formalism*, pp. 479--490. Academic Press. (Original manuscript 1969.)

Hyland, J. M. E., and Ong, C.-H. L. (2000). On full abstraction for PCF. *Information and Computation*, 163(2), 285--408.

Jacobs, B. (1999). *Categorical Logic and Type Theory*. Elsevier.

Janssen, T. M. V. (1997). Compositionality. In J. van Benthem and A. ter Meulen (eds.), *Handbook of Logic and Language*, pp. 417--473. Elsevier.

Jawahar, G., Sagot, B., and Seddah, D. (2019). What does BERT learn about the structure of language? In *Proceedings of the 57th Annual Meeting of the ACL*, pp. 3651--3657.

Kamp, H. (1981). A theory of truth and semantic representation. In J. Groenendijk, T. Janssen, and M. Stokhof (eds.), *Formal Methods in the Study of Language*, pp. 277--322. Mathematisch Centrum.

Kartsaklis, D., et al. (2012). A unified sentence space for categorical distributional-compositional semantics: Theory and experiments. In *Proceedings of COLING 2012*, pp. 549--558.

Kartsaklis, D., Fan, I., Yeung, R., Pearson, A., Lorber, R., Toumi, A., de Felice, G., Meichanetzidis, K., Clark, S., and Coecke, B. (2021). lambeq: An efficient high-level Python library for quantum NLP. arXiv:2110.04236.

Keysers, D., Schärli, N., Scales, N., Buiber, H., Furber, D., Kasber, S., Momchev, N., Siber, D., Auer, L., Bachem, O., Bober, G., Chen, J., Cisber, E., Gesmundo, A., Micber, K., Piber, L., Osber, N., Rber, A., Zhu, X., and Sorber, A. (2020). Measuring compositional generalization: A comprehensive method on realistic data. In *Proceedings of ICLR 2020*.

Kim, N., and Linzen, T. (2020). COGS: A compositional generalization challenge based on semantic interpretation. In *Proceedings of EMNLP 2020*, pp. 9087--9105.

Kitcher, P. (1981). Explanatory unification. *Philosophy of Science*, 48(4), 507--531.

Klein, F. (1872). Vergleichende Betrachtungen uber neuere geometrische Forschungen. *Mathematische Annalen*, 43 (1893), 63--100. (English translation by M. W. Haskell, *Bulletin of the New York Mathematical Society*, 2, 1892--1893, 215--249.)

Kripke, S. (1959). A completeness theorem in modal logic. *Journal of Symbolic Logic*, 24(1), 1--14.

Kripke, S. (1963). Semantical considerations on modal logic. *Acta Philosophica Fennica*, 16, 83--94.

Lakoff, G., and Johnson, M. (1980). *Metaphors We Live By*. University of Chicago Press.

Lake, B. M., and Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. In *Proceedings of ICML 2018*, pp. 2873--2882.

Lambek, J. (1958). The mathematics of sentence structure. *American Mathematical Monthly*, 65(3), 154--170.

Lambek, J. (1968). Deductive systems and categories I. *Mathematical Systems Theory*, 2, 287--318.

Lambek, J. (1999). Type grammar revisited. In A. Lecomte, F. Lamarche, and G. Perrier (eds.), *Logical Aspects of Computational Linguistics*, pp. 1--27. Springer.

Lambek, J. (2001). Type grammars as pregroups. *Grammars*, 4(1), 21--39.

Martin-Lof, P. (1984). *Intuitionistic Type Theory*. Bibliopolis.

Mikolov, T., Chen, K., Corrado, G., and Dean, J. (2013). Efficient estimation of word representations in vector space. In *Proceedings of the 1st International Conference on Learning Representations (ICLR)*.

Moggi, E. (1991). Notions of computation and monads. *Information and Computation*, 93(1), 55--92.

Montague, R. (1970a). English as a formal language. In B. Visentini et al. (eds.), *Linguaggi nella Societa e nella Tecnica*, pp. 189--224. Edizioni di Comunita.

Montague, R. (1970b). Universal grammar. *Theoria*, 36(3), 373--398.

Montague, R. (1973). The proper treatment of quantification in ordinary English. In J. Hintikka, J. Moravcsik, and P. Suppes (eds.), *Approaches to Natural Language*, pp. 221--242. Reidel.

Moortgat, M. (1997). Categorial type logics. In J. van Benthem and A. ter Meulen (eds.), *Handbook of Logic and Language*, pp. 93--177. Elsevier.

Morrill, G. (2011). *Categorial Grammar: Logical Syntax, Semantics, and Processing*. Oxford University Press.

Morrison, M. (2000). *Unifying Scientific Theories: Physical Concepts and Mathematical Structures*. Cambridge University Press.

Pennington, J., Socher, R., and Manning, C. D. (2014). GloVe: Global vectors for word representation. In *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pp. 1532--1543.

Plotkin, G. D. (1981). A structural approach to operational semantics. Technical Report DAIMI FN-19, University of Aarhus.

Prawitz, D. (1965). *Natural Deduction: A Proof-Theoretical Study*. Almqvist and Wiksell.

Prawitz, D. (2006). Meaning approached via proofs. *Synthese*, 148(3), 507--524.

Radford, A., Narasimhan, K., Salimans, T., and Sutskever, I. (2018). Improving language understanding by generative pre-training. OpenAI Technical Report.

Ruis, L., Andreas, J., Baroni, M., Bouchacourt, D., and Lake, B. M. (2020). A benchmark for systematic generalization in grounded language understanding. In *Advances in Neural Information Processing Systems*, vol. 33.

Scott, D. S. (1970). Outline of a mathematical theory of computation. In *Proceedings of the Fourth Annual Princeton Conference on Information Sciences and Systems*, pp. 169--176.

Scott, D. S., and Strachey, C. (1971). Toward a mathematical semantics for computer languages. In J. Fox (ed.), *Proceedings of the Symposium on Computers and Automata*, pp. 19--46. Polytechnic Institute of Brooklyn Press.

Searle, J. R. (1969). *Speech Acts: An Essay in the Philosophy of Language*. Cambridge University Press.

Steedman, M. (2000). *The Syntactic Process*. MIT Press.

Tarski, A. (1936). The concept of truth in formalized languages. In A. Tarski, *Logic, Semantics, Metamathematics*, 2nd ed. (1983), pp. 152--278. Hackett.

Varela, F. J., Thompson, E., and Rosch, E. (1991). *The Embodied Mind: Cognitive Science and Human Experience*. MIT Press.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., and Polosukhin, I. (2017). Attention is all you need. In *Advances in Neural Information Processing Systems*, vol. 30, pp. 5998--6008.

---

*Studium Generale ORGANVM -- SGO-2026-SYN-001 -- DRAFT v2 -- 2026-03-21*

*Synthesis of RP-01 (The Semantics Bridge) and RP-06 (Chomsky to Computation)*

*Revised in response to Triadic Review Protocol TRP-SYN-01 (2026-03-20)*
