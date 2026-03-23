---
sgo_id: SGO-2026-SYN-001
title: "The Architecture of Formal Meaning"
tier: Dissertation (synthesis)
status: LOCAL (first draft)
target_venues: [Journal of Philosophical Logic, Mathematical Structures in Computer Science, arXiv cs.LO]
dependencies: [RP-01, RP-06]
bridges: [Adventure 1, Adventure 6]
date: 2026-03-21
---

# The Architecture of Formal Meaning: A Categorical Framework for Unifying Grammar, Semantics, and Computation

**Studium Generale ORGANVM -- Cross-Adventure Synthesis SYN-01**

**Synthesis of RP-01 (The Semantics Bridge) and RP-06 (Chomsky to Computation)**

---

## Abstract

This dissertation undertakes the synthesis of two prior investigations conducted under the Studium Generale ORGANVM research programme: RP-01, which identified eight structural bridges connecting the three traditions of formal semantics (logical, computational, and natural language), and RP-06, which established a fourfold correspondence among grammars, types, proofs, and categories descending from Chomsky's 1956--1959 formalization of the linguistic hierarchy. The present work asks whether these two results -- the eight bridges and the fourfold correspondence -- can be unified into a single categorical architecture of meaning. The central claim is that meaning, in its most general formal characterisation, IS the functorial passage from a syntactic category to a semantic category, and that this passage exhibits the same categorical structure whether the syntax in question is linguistic, logical, or computational. The argument proceeds through five stages. First, the results of RP-01 and RP-06 are recapitulated and their regions of overlap and divergence identified. Second, the categorical architecture is constructed: compositionality is formalised as functoriality; the Lambek calculus is exhibited as the syntactic category; Montague's rule-to-rule correspondence is characterised as a natural transformation; the DisCoCat framework is shown to extend the architecture to distributional meaning; compact closed categories and pregroup grammars are situated within the framework; and the topos-theoretic perspective is developed for contextual meaning. Third, the unification claim is stated precisely: a five-way correspondence among derivation, proof, programme, morphism, and meaning-composition is proposed, and evidence both for and against the claim is marshalled. Fourth, the distributional challenge -- whether vector-space semantics can be categorified -- is addressed through the DisCoCat framework, the analysis of what transformers learn, and the identification of the reconciliation frontier. Fifth, implications for the ORGANVM system are drawn, interpreting schema contracts as syntactic categories and registry operations as functorial meaning-preserving transformations. The dissertation concludes that the classical, compositional, typed core of all three semantic traditions, together with the grammar-type-proof-category fourfold of RP-06, admits genuine categorical unification under a single functorial architecture, while the extensions beyond this core -- pragmatics, non-compositionality, neural representations, concurrency -- constitute the boundary conditions that delimit the architecture's scope and define the frontier of future research.

**Keywords:** category theory, formal semantics, compositionality, functoriality, Curry-Howard-Lambek correspondence, Lambek calculus, Montague grammar, DisCoCat, pregroup grammar, compact closed category, topos, natural transformation, distributional semantics, type theory, Chomsky hierarchy

---

## 1. Introduction

### 1.1 Two Convergent Investigations

The Studium Generale ORGANVM research programme has produced, in its second phase, two investigations that approach the formal structure of meaning from complementary directions. RP-01, *Toward a Grand Unified Semantics*, surveyed the three traditions of formal semantics -- logical semantics (Tarski 1936; Kripke 1959, 1963), programming language semantics (Scott and Strachey 1971; Plotkin 1981; Hoare 1969), and natural language semantics (Montague 1973; Heim and Kratzer 1998) -- and identified eight structural bridges connecting them: compositionality, lambda calculus, the Curry-Howard-Lambek correspondence, type theory, model theory, game semantics, dynamic semantics, and proof-theoretic semantics. Each bridge was assessed on a four-point scale of structural strength (isomorphism, homomorphism, analogy, metaphor), and the central finding was that the classical, compositional, typed fragment of each tradition admits genuine structural unification, with category theory providing the most perspicuous unifying metalanguage.

RP-06, *Grammars, Types, Proofs, and Categories*, approached the same territory from the side of formal language theory. Beginning with Chomsky's 1956--1959 formalization of the grammar hierarchy, RP-06 traced three threads from that origin: the "machines" thread (formal language theory and automata), the "engineering" thread (programming language syntax and compilers), and the "logic" thread (type theory, categorial grammar, and the Curry-Howard-Lambek correspondence). The central finding was a fourfold correspondence: at each level of the Chomsky hierarchy, grammars correspond to automata (the classical result), but they also correspond to regimes of type-theoretic expressiveness (regular grammars to finite types, context-free grammars to recursive algebraic types, context-sensitive grammars to parametric polymorphism, unrestricted grammars to full dependent types), and the convergence of all three threads reveals that grammars, types, proofs, and categories are structurally isomorphic. The Curry-Howard-Lambek correspondence, extended through categorial grammar to include linguistic derivation, renders this isomorphism precise: parsing IS type-checking IS proof construction IS composition of morphisms.

### 1.2 The Question of Unification

The present dissertation asks whether these two results can be unified into a single categorical architecture of meaning. RP-01 identified bridges between traditions of semantics; RP-06 identified correspondences between formal structures. The overlap is substantial: both investigations converge on the Curry-Howard-Lambek correspondence, on categorial grammar, on lambda calculus, and on the compositional, type-driven approach to meaning. Yet the investigations also diverge: RP-01 encompasses dynamic semantics and game semantics, which RP-06 does not address; RP-06 encompasses automata theory and the fine structure of the Chomsky hierarchy, which RP-01 treats only tangentially.

The unification question can be stated with precision. RP-01 established that meaning, across three traditions, is characterised by a compositional, structure-preserving map from syntax to semantics. RP-06 established that syntax, across four formal frameworks (grammars, types, proofs, categories), is characterised by a single abstract structure. If meaning is a map from syntax to semantics, and if syntax has a unified categorical structure, then meaning itself must have a unified categorical structure -- the structure of a functor from the syntactic category to the semantic category.

### 1.3 The Grand Claim

The grand claim of this dissertation is as follows:

**Meaning is the functorial passage from syntax to semantics, and this passage has the same categorical structure whether the syntax is linguistic, logical, or computational.**

More precisely: there exists a family of categories **Syn** (syntactic categories) and a family of categories **Sem** (semantic categories) such that, for each tradition of formal semantics, meaning assignment is a functor F: **Syn** -> **Sem**. The syntactic categories are the categories of grammatical derivations (in linguistics), proof trees (in logic), and typed lambda terms (in computation). The semantic categories are the categories of model-theoretic denotations (in logic), domain-theoretic values (in computation), and intensional meanings (in linguistics). The Curry-Howard-Lambek correspondence guarantees that the syntactic categories are equivalent; the eight bridges of RP-01 guarantee that the functorial passage from syntax to semantics has the same structural character in all three traditions. The architecture of formal meaning is the architecture of this functorial passage.

### 1.4 Scope and Method

The method of this dissertation is conceptual and formal analysis. The primary data are the results of RP-01 and RP-06, supplemented by the mathematical literature on category theory, categorial grammar, the Lambek calculus, pregroup grammars, compact closed categories, topos theory, and the DisCoCat framework. The dissertation does not present new mathematical theorems in the sense of original proof; rather, it synthesises existing results into a unified architectural picture and identifies the precise points at which the architecture succeeds, the points at which it requires extension, and the points at which it fails.

The scope is necessarily broad. A synthesis that spans formal language theory, type theory, proof theory, category theory, model-theoretic semantics, distributional semantics, and applied system design cannot achieve the depth of a monograph focused on any one of these fields. The compensating virtue is architectural: by assembling the components into a single structure, the dissertation reveals the shape of the whole in a way that is invisible from within any single component.

The remainder of the dissertation is organised as follows. Section 2 recapitulates the results of RP-01 and RP-06, identifying overlap and divergence. Section 3 constructs the categorical architecture. Section 4 states and evaluates the unification claim. Section 5 addresses the distributional challenge. Section 6 draws implications for the ORGANVM system. Section 7 offers discussion. Section 8 concludes.

---

## 2. Recapitulation: The Eight Bridges and the Fourfold

This section summarises the two prior investigations -- RP-01's taxonomy of cross-domain semantic bridges and RP-06's fourfold grammar-type-proof-category correspondence -- and maps their regions of overlap and divergence. The summary is necessarily compressed; the reader is referred to the full texts of RP-01 and RP-06 for detailed exposition and formal argument.

### 2.1 Summary of RP-01: The Bridge Taxonomy

RP-01 identified eight structural bridges connecting the three traditions of formal semantics. Each bridge was assessed for structural strength on a four-point scale:

1. **Compositionality** (Frege's Principle). In all three traditions, meaning is assigned by a structure-preserving map (homomorphism) from a syntactic algebra to a semantic algebra. The algebraic formulation is identical across traditions: the relationship between syntax and semantics is, in each case, the same mathematical concept instantiated in different domains. **Structural strength: isomorphism.**

2. **Lambda calculus**. Church's lambda calculus is, simultaneously and non-metaphorically, the foundation of functional programming, the notation of Montague grammar, and a proof-term calculus for intuitionistic logic. The lambda terms that appear in a Montague-grammar derivation are syntactically and semantically identical to those defining higher-order functions in Haskell and serving as proof terms in natural deduction. **Structural strength: isomorphism.**

3. **The Curry-Howard-Lambek correspondence**. The three-way equivalence of proofs, programmes, and categorical morphisms is an isomorphism in the strongest sense: precise, invertible translations exist between the three presentations, preserving composition, identity, and typing. The extension to natural language, via the type-logical tradition and combinatory categorial grammar, is a homomorphism: it captures the compositional, type-driven aspects of natural language meaning but does not extend to pragmatics, context-dependence, or distributional meaning. **Structural strength: isomorphism (three-way); homomorphism (extension to natural language).**

4. **Type theory**. Types classify meanings in all three traditions: they sort entities into kinds, constrain well-formedness, and drive composition. The role of types is structurally parallel, but the type systems differ in important respects (logical type systems emphasise paradox prevention; programming type systems emphasise error prevention; linguistic type systems emphasise semantic anomaly prevention). **Structural strength: homomorphism.**

5. **Model theory**. In all three traditions, a central approach to semantics proceeds by defining an interpretation: a mapping from syntactic expressions to elements of a mathematical structure (a model). For classical, compositional fragments, the model-theoretic approach is structurally identical across traditions. **Structural strength: isomorphism (for classical fragments).**

6. **Game semantics**. Independently and productively developed in all three traditions -- dialogical logic (Lorenzen, Lorenz), game-theoretical semantics for natural language (Hintikka), and game semantics for programming languages (Abramsky, Hyland, Ong) -- game semantics treats meaning as interactive strategy. The convergence of three independent traditions on a game-theoretic conception of meaning constitutes powerful evidence of deep structural kinship. **Structural strength: homomorphism.**

7. **Dynamic semantics**. The treatment of meaning as context-change potential (state transformation) is the default view in programming language semantics and was revolutionary in natural language semantics (Heim 1982; Kamp 1981; Groenendijk and Stokhof 1991). Both traditions use the same mathematical framework: functions on state spaces. **Structural strength: analogy tending toward homomorphism.**

8. **Proof-theoretic semantics**. Meaning located in inferential role rather than denotation: introduction and elimination rules in logic (Gentzen, Dummett, Prawitz), constructors and destructors in programming (Martin-Lof), inferential articulation in philosophy (Brandom). **Structural strength: homomorphism.**

The hierarchy of bridge strengths reveals a pattern: the bridges closest to the classical, compositional, typed core (compositionality, lambda calculus, model theory) achieve isomorphism; those that extend the core (type theory, game semantics, proof-theoretic semantics, the Curry-Howard-Lambek extension to natural language) achieve homomorphism; and those at the dynamic periphery (dynamic semantics) are analogies under active formalisation. No bridge was assessed as mere metaphor.

### 2.2 Summary of RP-06: The Fourfold Correspondence

RP-06 established a correspondence extending the classical Chomsky hierarchy into the type-theoretic domain. The central result is a table of correspondences:

| Level | Grammar | Automaton | Type System | Logic |
|-------|---------|-----------|-------------|-------|
| Type 3 | Regular | Finite automaton | Finite types, enumerations | Propositional (decidable fragment) |
| Type 2 | Context-free | Pushdown automaton | Recursive algebraic types | First-order (decidable fragment) |
| Type 1 | Context-sensitive | Linear bounded automaton | Parametric polymorphism, refinement types | Second-order logic |
| Type 0 | Unrestricted | Turing machine | Full dependent types | Higher-order logic (undecidable) |

Each level of the hierarchy admits a fourfold characterisation: grammar, automaton, type system, logic. The Curry-Howard-Lambek correspondence provides the formal mechanism relating the type-theoretic, logical, and categorical characterisations; the grammar-automaton correspondence provides the classical formal language theory; and categorial grammar provides the linguistic instantiation.

RP-06 further identified that the critical level for the grammar-computation connection is Type 2 (context-free), where Chomsky's phrase-structure grammars and Backus-Naur form independently discovered the same mathematical substrate. It proposed that natural language resides at a level between Type 2 and Type 1 -- the mildly context-sensitive languages -- and that the type-theoretic characterisation of this intermediate level is an open problem.

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

**The Curry-Howard-Lambek correspondence.** Both investigations identify this three-way (or four-way, with grammars included) correspondence as the deepest known structural bridge. RP-01 treats it as Bridge 3 and assesses it as an isomorphism for the three-way correspondence and a homomorphism for the extension to natural language. RP-06 treats it as the culmination of the fourfold and the mechanism that makes the grammar-type-proof-category identification precise. The treatments are mutually reinforcing: RP-01 provides the semantic dimension (the correspondence connects three traditions of *meaning*), while RP-06 provides the syntactic dimension (the correspondence connects four formal *structures*).

**Categorial grammar and the Lambek calculus.** Both investigations identify categorial grammar as the framework in which the grammar-logic-computation-category correspondence becomes linguistically concrete. RP-01 discusses it in the context of Bridge 3 (the extension of Curry-Howard-Lambek to natural language) and Bridge 4 (type theory in natural language semantics). RP-06 discusses it extensively as the formalism where "grammar IS typing" and traces its development from Ajdukiewicz (1935) through Bar-Hillel (1953), Lambek (1958), and Montague (1970s) to the modern type-logical tradition and combinatory categorial grammar (Steedman 2000).

**Lambda calculus as the shared formal system.** Both investigations identify lambda calculus as the formal system that is, non-metaphorically, the same in all three traditions. RP-01 assesses it as an isomorphic bridge. RP-06 traces its role from Church's original formulation through typed extensions (simply typed lambda calculus, System F, calculus of constructions) and shows that the Chomsky hierarchy of grammars corresponds to a hierarchy of typed lambda calculi.

**Compositionality as the structural principle.** RP-01 formalises compositionality as a homomorphism from syntactic algebras to semantic algebras and assesses it as isomorphic across traditions. RP-06 identifies compositionality as the consequence of the typed structure of categorial grammar: when syntax is typed and semantics is a type-preserving interpretation, compositionality follows as a theorem rather than an assumption.

### 2.4 Where They Diverge

The divergences between RP-01 and RP-06 are equally instructive, as they mark the boundaries of the unified architecture.

**Dynamic and game semantics (RP-01 only).** RP-01 devotes substantial attention to dynamic semantics (Bridge 7) and game semantics (Bridge 6), treating them as cross-domain bridges in their own right. RP-06 does not address these frameworks. The reason is structural: dynamic semantics and game semantics concern the *nature of meaning* (meaning as state transformation, meaning as interactive strategy) rather than the *structure of syntax* (grammars, types, proofs). RP-06's fourfold concerns the syntactic side; dynamic and game semantics concern the semantic side. The categorical architecture constructed in Section 3 must accommodate both.

**Automata theory (RP-06 only).** RP-06 devotes extensive attention to the grammar-automaton correspondence at each level of the Chomsky hierarchy. RP-01 does not address automata theory directly. The automaton perspective is important for the categorical architecture because automata provide the *operational* or *intensional* characterisation of syntactic complexity, complementing the *generative* or *extensional* characterisation provided by grammars and the *logical* characterisation provided by type systems.

**The mildly context-sensitive problem (RP-06 only).** RP-06 identifies the type-theoretic characterisation of mildly context-sensitive languages -- the conjectured complexity class of natural language -- as an open problem. RP-01 does not address this question, since its focus is on semantic bridges rather than syntactic complexity. The problem is significant for the categorical architecture because the characterisation of natural language's position in the hierarchy determines which categorical structures are needed to model linguistic syntax.

**Distributional semantics (treated differently).** RP-01 devotes a substantial section (Section 5.3) to the distributional and neural challenge, concluding that distributional semantics cannot be fully reconciled with formal traditions but that partial reconciliation is achievable through categorical frameworks (notably DisCoCat). RP-06 mentions DisCoCat and the question of whether transformers implicitly learn type-theoretic structure, but treats these as open questions rather than developed analyses. The present synthesis addresses the distributional challenge in Section 5.

---

## 3. The Categorical Architecture

This section constructs the categorical architecture of formal meaning. The architecture has seven components, developed in sequence: meaning as functor (Section 3.1), compositionality as functoriality (Section 3.2), the Lambek calculus as the syntactic category (Section 3.3), Montague's rule-to-rule correspondence as natural transformation (Section 3.4), the DisCoCat framework (Section 3.5), compact closed categories and pregroup grammars (Section 3.6), and the topos-theoretic perspective (Section 3.7).

### 3.1 Meaning as Functor

The central organising concept of the categorical architecture is the treatment of meaning as a functor. In category theory, a functor F: **C** -> **D** is a structure-preserving map between categories: it sends objects of **C** to objects of **D** and morphisms of **C** to morphisms of **D**, preserving composition and identity. That is, F(g . f) = F(g) . F(f) for any composable morphisms f and g, and F(id_A) = id_{F(A)} for any object A.

The claim that meaning is a functor asserts that there is a syntactic category **Syn** and a semantic category **Sem**, and that meaning assignment is a functor F: **Syn** -> **Sem**. This claim, once stated, is almost tautological -- it merely says that meaning is a structure-preserving map -- but its force lies in the identification of what the "structure" is that is being preserved.

In the syntactic category **Syn**, the objects are syntactic types (syntactic categories in linguistics, types in programming, propositions in logic) and the morphisms are derivations (grammatical derivations in linguistics, typed lambda terms in programming, proofs in logic). In the semantic category **Sem**, the objects are semantic domains (sets of denotations, model-theoretic structures, vector spaces) and the morphisms are meaning-preserving transformations (functions between denotation domains, model homomorphisms, linear maps).

The functorial requirement -- that F preserves composition and identity -- is precisely the requirement of compositionality: the meaning of a composite derivation (a derivation built from sub-derivations) is the composition of the meanings of the sub-derivations. This is why compositionality, assessed by RP-01 as an isomorphic bridge, is so fundamental: it is not merely one property of meaning among others, but the *defining structural property* of the functorial relationship that constitutes meaning assignment.

The functorial perspective unifies the three traditions as follows:

**In logical semantics.** The syntactic category is the category of formulae and proofs in a formal system (e.g., intuitionistic propositional logic, first-order predicate logic). The semantic category is the category of models and model homomorphisms (e.g., the category **Set** of sets and functions, or the category of Kripke frames and frame morphisms). The meaning functor assigns to each formula a semantic domain (its extension in a model) and to each proof a function between domains (the computational content of the proof, via the Curry-Howard correspondence). Tarskian satisfaction is the instantiation of this functor for first-order logic; Kripke semantics is its instantiation for modal logic.

**In programming language semantics.** The syntactic category is the category of types and typed terms (lambda terms, or more generally, terms in a typed programming language). The semantic category is the category of domains and continuous functions (in denotational semantics), or the category of configurations and transition relations (in operational semantics), or the category of specifications and refinement relations (in axiomatic semantics). The meaning functor assigns to each type a domain of values and to each programme a function from inputs to outputs. The compositionality of denotational semantics -- Scott and Strachey's foundational design decision -- is precisely the functoriality of this functor.

**In natural language semantics.** The syntactic category is the category of syntactic types and grammatical derivations (in a categorial grammar, such as the Lambek calculus or CCG). The semantic category is the category of semantic types and typed lambda terms operating on model-theoretic structures. The meaning functor assigns to each syntactic type a semantic type (e.g., NP maps to type *e*, S maps to type *t*, NP\S maps to type *e* -> *t*) and to each grammatical derivation a semantic derivation (a lambda term that computes the meaning of the derived expression from the meanings of its parts). Montague's rule-to-rule hypothesis is precisely the assertion that this functor exists: every syntactic rule is paired with a semantic rule, and the meaning of the whole is computed functorially from the meanings of the parts.

### 3.2 Compositionality as Functoriality

The identification of compositionality with functoriality is not new -- it has been observed by Janssen (1997), Hodges (2001), and others -- but its consequences for the architecture of meaning deserve explicit development.

Janssen's algebraic characterisation of Montague grammar treats the syntax of a language as a *many-sorted algebra* (an algebra with multiple sorts of elements and operations that may take elements of different sorts as arguments and return elements of a designated sort). The syntactic algebra **A**_syn has sorts corresponding to syntactic categories (NP, VP, S, etc.) and operations corresponding to syntactic rules (e.g., the rule that combines an NP and a VP to form an S). The semantic algebra **A**_sem has sorts corresponding to semantic types (entities, truth values, functions) and operations corresponding to semantic combination rules (e.g., function application, abstraction, intensionalisation). Montague's principle of compositionality asserts that there exists a homomorphism h: **A**_syn -> **A**_sem. This is precisely the assertion that meaning assignment is a functor, expressed in the language of universal algebra rather than category theory.

The categorical formulation has the advantage of generality. A many-sorted algebra is a special case of a category (an algebra with one object per sort); a homomorphism of algebras is a special case of a functor. By moving from algebras to categories, the framework accommodates structures that are more general than algebras: derivations with internal structure (not just derived objects), relations between derivations (not just between derived objects), and higher-order structure (functors between functor categories). This additional generality is needed to account for phenomena such as syntactic ambiguity (multiple derivations of the same string), scope ambiguity (multiple semantic readings arising from a single syntactic derivation), and discourse structure (meaning relations between sentences, not just within sentences).

The functorial formulation also makes precise the sense in which compositionality can *fail*. A failure of compositionality is a failure of the meaning map to be a functor: a case in which F(g . f) is not equal to F(g) . F(f). In natural language, idioms provide the canonical example: the meaning of "kick the bucket" (in its idiomatic reading) is not the composition of the meanings of "kick," "the," and "bucket." In the functorial framework, this failure can be diagnosed precisely: either the syntactic derivation of the idiomatic reading differs from the derivation of the literal reading (so that the functor *does* preserve composition, but operates on a different derivation), or the meaning map is not functorial for this fragment of the language (so that the idiomatic reading falls outside the scope of the compositional architecture). Both diagnoses have been pursued in the literature, and both are expressible in the categorical framework.

In programming language semantics, the compositionality failures identified by RP-01 -- exceptions, continuations, mutable state, concurrency -- correspond to cases in which the meaning functor must be extended from a simple functor F: **Syn** -> **Sem** to a functor into a richer semantic category. Moggi's (1991) monadic framework formalises this extension: the semantic category is not **Set** (or **Dom**, the category of domains) but the Kleisli category of a monad T on **Set** (or **Dom**). The meaning functor F: **Syn** -> **Kleisli**(T) preserves composition in the monadic sense: the meaning of a sequential composition is the Kleisli composition (monadic bind) of the meanings of the components. This is compositionality restored, not abandoned -- but restored at the cost of enriching the semantic category.

The parallel between monadic enrichment in programming language semantics and coercion/type-shifting in natural language semantics is striking and, as far as the present author is aware, underexplored. In both cases, compositionality is maintained by enriching the semantic framework: the objects of the semantic category become more structured (monadic values rather than plain values; coerced types rather than basic types), and the morphisms become more complex (Kleisli arrows rather than plain functions; type-shifting operations rather than simple applications). A systematic comparison of these enrichment strategies, framed categorically, would constitute a significant contribution to the architecture of meaning. The present dissertation notes the parallel and identifies it as a direction for future research.

### 3.3 The Lambek Calculus as the Syntactic Category

The Lambek calculus, introduced by Joachim Lambek in 1958, provides the canonical syntactic category for the categorical architecture of meaning. In the Lambek calculus, every word of a language is assigned a syntactic type (category), and the grammar has no phrase-structure rules -- only type assignments and the principle of function application. A word of type A/B combines with an adjacent word of type B on its right to produce a constituent of type A; a word of type B\A combines with an adjacent word of type B on its left to produce a constituent of type A. The forward slash and backward slash are the two implication connectives of a non-commutative logic.

The Lambek calculus is a *logic*: it has introduction and elimination rules for its connectives (/, \, and the product), and a derivation in the Lambek calculus is a proof in this logic. This is the linguistic incarnation of the Curry-Howard correspondence: syntactic categories are propositions, grammatical derivations are proofs, and the derivation of a sentence is the construction of a proof that the string of words reduces to the sentential type S.

As a category, the Lambek calculus forms the *free residuated monoid* (or, in its non-associative variant, the free residuated groupoid) generated by the basic syntactic types. The objects of this category are syntactic types; the morphisms are derivations (proofs). The residuation laws encode the relationship between the product (concatenation) and the implications (the slash connectives):

A . B -> C if and only if A -> C / B if and only if B -> A \ C

This adjunction between the product and the implications is the categorical expression of the relationship between syntactic combination and syntactic types. In categorical terms, the Lambek calculus is a *monoidal closed category* (specifically, a *biclosed monoidal category*, since it has both left and right residuals). The non-commutativity of the product reflects the fact that word order matters in natural language: "John loves Mary" and "Mary loves John" have different meanings because concatenation is non-commutative.

The significance of the Lambek calculus for the categorical architecture is threefold. First, it provides a *concrete* syntactic category: the category of syntactic types and grammatical derivations for a natural language (or a fragment thereof). Second, it connects the syntactic category to logic: the syntactic types are propositions in a substructural logic, and the derivations are proofs. Third, it connects the syntactic category to computation: via the Curry-Howard correspondence, the derivations (proofs) correspond to lambda terms, and the derivation of a sentence corresponds to the construction of a programme that computes the sentence's meaning.

The substructural character of the Lambek calculus deserves emphasis. The Lambek calculus lacks the structural rules of exchange (commutativity), weakening (discarding hypotheses), and contraction (duplicating hypotheses) that are present in classical and intuitionistic logic. The absence of exchange reflects word order; the absence of weakening reflects the fact that every word in a sentence must be "used" (contribute to the meaning); the absence of contraction reflects the fact that a word cannot be "used twice" in a single derivation. These absences connect the Lambek calculus to linear logic (Girard 1987), which similarly lacks weakening and contraction and treats propositions as *resources* that are consumed in proof. The connection between the Lambek calculus and linear logic has been extensively developed (Moortgat 1997; Morrill 2011) and provides an important link between linguistic structure and resource-sensitive computation.

From the perspective of RP-06's fourfold, the Lambek calculus sits at the Type 2 level of the Chomsky hierarchy (context-free grammars) in its basic form, since the Lambek calculus without product is weakly equivalent to context-free grammars. Extensions of the Lambek calculus -- with modalities, with controlled structural rules, with discontinuous operators -- can capture mildly context-sensitive phenomena, approaching the conjectured complexity class of natural language. The type-theoretic characterisation of these extended Lambek calculi -- the precise regime of type-theoretic expressiveness that corresponds to mildly context-sensitive grammars -- remains the open problem identified by RP-06.

### 3.4 Montague's Rule-to-Rule Correspondence as Natural Transformation

Montague grammar implements the meaning functor for natural language by pairing each syntactic rule with a corresponding semantic rule. This pairing -- the rule-to-rule hypothesis -- can be given a precise categorical formulation as a natural transformation.

In the categorical framework, consider two functors from the syntactic category **Syn** to the semantic category **Sem**: the *syntactic interpretation functor* S, which maps syntactic types to the formal objects manipulated by the grammar (strings, trees, phonological representations), and the *semantic interpretation functor* M, which maps syntactic types to semantic objects (intensions, truth conditions, denotations). A natural transformation eta: S => M is a family of morphisms eta_A: S(A) -> M(A), one for each syntactic type A, such that for every derivation f: A -> B in **Syn**, the following diagram commutes:

```
S(A) --eta_A--> M(A)
 |                |
S(f)             M(f)
 |                |
 v                v
S(B) --eta_B--> M(B)
```

The commutativity of this diagram is precisely the rule-to-rule hypothesis: the meaning of a derived expression (obtained by applying a syntactic rule and then interpreting semantically) is the same as the meaning obtained by first interpreting the parts semantically and then applying the corresponding semantic rule. The natural transformation eta is the *bridge* between syntax and semantics, and its naturality condition is the mathematical content of compositionality.

This formulation reveals that Montague's rule-to-rule correspondence is not merely a methodological convenience but a structural requirement: it is the condition that the syntactic and semantic interpretations are *coherent* -- that they form a commutative diagram. The naturality condition ensures that the meaning assignment is *uniform*: it does not depend on the particular derivation used to combine the parts, but only on the types of the parts and the rule of combination. This uniformity is what makes compositional semantics *systematic* -- the ability to understand novel sentences is a consequence of the naturality of the transformation from syntax to semantics.

The natural transformation formulation also provides a framework for analysing failures of the rule-to-rule correspondence. A failure of naturality -- a case in which the diagram does not commute -- corresponds to a case in which the meaning of a derived expression depends on the particular syntactic derivation, not just on the meanings of the parts. Scope ambiguity in natural language provides an example: the sentence "Every student read a book" has two readings (one in which every student read the same book, and one in which each student read a possibly different book), corresponding to two different derivations that produce the same surface string. The two derivations yield different semantic values under the meaning functor, reflecting the failure of the surface string to determine the meaning uniquely. In the categorical framework, this is diagnosed as a failure of the functor to be *faithful* (injective on morphisms): distinct derivations (morphisms) that produce the same derived object (surface string) may produce distinct semantic values.

The natural transformation perspective further illuminates the difference between *extensional* and *intensional* semantics. In Montague's intensional logic, the semantic interpretation assigns to each expression not an extension (a denotation in a single model) but an intension (a function from possible worlds to extensions). The intensional interpretation is a functor from **Syn** to the category of intensions, which is a functor category [**W**, **Sem**] where **W** is the (discrete) category of possible worlds. The move from extensional to intensional semantics is, categorically, the move from functors **Syn** -> **Sem** to functors **Syn** -> [**W**, **Sem**]. This move can be understood as a natural transformation between functor categories -- a "second-order" natural transformation -- and its coherence conditions encode the relationship between extensional and intensional meaning.

### 3.5 The DisCoCat Framework: Distributional Meaning in Categorical Form

The DisCoCat framework (Categorical Compositional Distributional semantics), introduced by Coecke, Sadrzadeh, and Clark (2010), is the most sustained attempt to bridge the formal-compositional and distributional-statistical traditions of semantics within a categorical framework. Its significance for the architecture of formal meaning is that it demonstrates the feasibility of incorporating distributional meaning -- meaning derived from patterns of co-occurrence in large corpora, represented as vectors in high-dimensional spaces -- into the functorial architecture.

The key observation underlying DisCoCat is that pregroup grammars (Lambek 1999, 2001) and the category of finite-dimensional vector spaces (**FdVect**) share a common mathematical structure: both are compact closed categories (more precisely, rigid categories, which are the non-symmetric variant). In a compact closed category, every object A has a dual A*, and there are unit and counit morphisms (eta: I -> A* . A and epsilon: A . A* -> I) satisfying the "yanking" equations. In **FdVect**, the dual of a vector space V is its dual space V*, and the unit and counit are the canonical bilinear pairing. In a pregroup grammar, the dual of a type p is its left adjoint p^l or right adjoint p^r, and the unit and counit are the adjunction maps.

DisCoCat exploits this shared structure to define meaning as a functor from grammar to vector spaces. Formally, a DisCoCat model is a strong monoidal functor:

F: **G** -> **FdVect**

where **G** is the free rigid category generated by the pregroup grammar. This functor assigns:

- To each basic syntactic type x, a finite-dimensional vector space F(x). For example, the noun type n might be assigned a 300-dimensional space whose basis elements correspond to features (semantic dimensions), and the sentence type s might be assigned a one-dimensional space (so that sentence meanings are scalars -- truth values or degrees of truth).

- To each word w with dictionary type t = t_1 ... t_n, a vector F(w) in the tensor product space F(t_1) tensor ... tensor F(t_n). A noun like "cat" is assigned a vector in F(n); a transitive verb like "loves" is assigned a tensor in F(n) tensor F(s) tensor F(n) (reflecting the type n^r . s . n^l).

- To each grammatical derivation f: w_1 ... w_n -> s, a linear map F(f): F(w_1) tensor ... tensor F(w_n) -> F(s), obtained by composing the cup maps (adjunction counits) according to the derivation. The meaning of a sentence is the scalar obtained by applying this linear map to the tensor product of the word vectors.

The functorial character of DisCoCat is essential: it ensures that the meaning of a sentence is computed *compositionally* from the meanings of its words, with the composition governed by the grammatical structure. The distributional hypothesis ("a word is characterised by the company it keeps") provides the lexical meanings (word vectors); the categorical framework provides the compositional structure; and the functor F provides the bridge.

DisCoCat resolves, or at least addresses, the fundamental tension between distributional and compositional semantics that RP-01 identified in Section 5.3. Distributional semantics provides rich, empirically grounded lexical meanings but lacks compositionality; formal semantics provides compositionality but lacks empirically grounded lexical meanings. DisCoCat provides *both*: the word vectors encode distributional meaning, and the functorial composition encodes compositional structure. The result is a framework in which the meaning of "dog bites man" differs from the meaning of "man bites dog" -- as it must -- because the different grammatical derivations (different morphisms in **G**) produce different linear maps in **FdVect**.

The limitations of DisCoCat are equally important for the architecture. First, the choice of **FdVect** as the semantic category is restrictive: it cannot directly represent logical operations (negation, quantification, modality) that are central to formal semantics. The meaning of "every dog bites some cat" requires quantificational machinery that is not naturally available in vector spaces. Extensions of DisCoCat to density matrices, to the category of relations (**Rel**), and to other semantic categories are active areas of research. Second, pregroup grammars are weakly equivalent to context-free grammars, which are insufficient for the full range of natural language phenomena; extensions to combinatory categorial grammar (CCG) and other mildly context-sensitive formalisms are being developed. Third, the empirical performance of DisCoCat models, while promising, has not yet matched the performance of neural language models on standard NLP benchmarks, though the frameworks address different questions (DisCoCat asks about the *structure* of compositional meaning; neural models ask about the *prediction* of linguistic behaviour).

### 3.6 Compact Closed Categories and Pregroup Grammars

The role of compact closed categories in the architecture of meaning warrants further development, as it represents the point at which the categorical structure of grammar and the categorical structure of distributional semantics meet most directly.

A compact closed category is a symmetric monoidal category in which every object has a dual satisfying certain coherence conditions (the unit-counit adjunction, or "snake equations"). The canonical example is **FdVect**: finite-dimensional vector spaces with tensor product as the monoidal structure. In **FdVect**, every vector space V has a dual V* = Hom(V, k) (where k is the base field), and the canonical evaluation map V* tensor V -> k and coevaluation map k -> V tensor V* witness the compact closure.

A pregroup, as defined by Lambek (1999, 2001), is a partially ordered monoid in which every element p has a left adjoint p^l and a right adjoint p^r satisfying:

p^l . p <= 1 <= p . p^l
p . p^r <= 1 <= p^r . p

A pregroup, viewed as a category (with elements as objects and the order relation as morphisms), is a rigid category -- a non-symmetric variant of a compact closed category. The adjunction maps p^l . p -> 1 and 1 -> p . p^l correspond to the counit and unit of the compact closure, respectively.

The significance of this shared structure is that it permits a functorial passage from grammar (modelled by a pregroup or a free rigid category) to semantics (modelled by **FdVect** or another compact closed category). The functor preserves the compact closed structure: duals in grammar (left and right adjoints) are mapped to duals in semantics (dual vector spaces), and the adjunction maps in grammar are mapped to the evaluation and coevaluation maps in semantics.

The compact closed structure also provides a diagrammatic calculus. In both pregroups and **FdVect**, morphisms can be represented as string diagrams -- graphs with nodes (representing operations) and edges (representing objects) -- and equality of morphisms can be verified by topological deformation of diagrams (the "yanking" equations). This diagrammatic calculus, imported from categorical quantum mechanics (Abramsky and Coecke 2004), provides an intuitive and computationally efficient method for reasoning about meaning composition. The meaning of a sentence is computed by drawing the string diagram corresponding to the grammatical derivation and "pulling" the word-meaning tensors through the diagram according to the diagrammatic rules. The result is a tensor contraction that yields the sentence meaning.

The connection between compact closed categories and quantum mechanics is not merely formal but conceptually suggestive. Quantum processes (state preparation, measurement, entanglement) and linguistic processes (word combination, predication, anaphoric reference) share the structure of compact closed categories. This observation, which motivated the development of DisCoCat, suggests that the architecture of meaning may be connected to the architecture of physical processes at a deeper level than is currently understood. The development of quantum natural language processing (QNLP), which implements DisCoCat models on quantum computers, represents one direction of investigation into this connection.

### 3.7 The Topos-Theoretic Perspective: Presheaf Semantics for Contextual Meaning

A topos is a category that behaves like a generalised universe of sets. The category **Set** of sets and functions is the simplest topos; presheaf categories (functor categories [**C**^op, **Set**] for a small category **C**) and sheaf categories (subcategories of presheaf categories satisfying a gluing condition) provide richer examples. Every topos has an internal logic that is intuitionistic (constructive) and higher-order, and every topos provides a model of intuitionistic higher-order logic.

The topos-theoretic perspective on semantics, as developed in programming language semantics and beginning to be explored in natural language semantics, provides a framework for modelling *contextual meaning* -- meaning that varies across contexts, perspectives, or information states.

In programming language semantics, presheaf categories have been used to model local state, name generation, and parametricity. A presheaf over a category of contexts **C** is a functor F: **C**^op -> **Set** that assigns to each context c a set F(c) of "elements in context c" and to each context morphism f: c -> c' (a context extension or context restriction) a function F(f): F(c') -> F(c) that translates elements across contexts. The presheaf semantics captures the *intensional* character of computation: the meaning of a programme depends on the context (the state, the environment, the continuation) in which it is evaluated.

In natural language semantics, presheaf semantics has a natural interpretation. The category of contexts **C** can be taken to be the category of discourse states (as in DRT), or the category of possible worlds (as in Kripke semantics), or the category of information states (as in dynamic semantics). A presheaf over **C** assigns to each context a set of possible meanings, and to each context extension (the introduction of new discourse referents, the arrival of new information) a function that updates the meanings. The presheaf condition -- that the updates are functorial (respect composition and identity) -- is the formal expression of the *coherence* of contextual meaning: meaning in an extended context must be consistent with meaning in the original context.

The sheaf condition adds a further requirement: *gluing*. If the meaning in each of several overlapping contexts is specified, and the specifications agree on the overlaps, then there is a unique meaning in the joint context that restricts to the given meanings. In linguistic terms, the sheaf condition says that if the meaning of a sentence is determined in several partial contexts (e.g., in the context of the first paragraph, in the context of the second paragraph, and in the context where both paragraphs are present), and the determinations agree where the contexts overlap, then there is a unique meaning in the full discourse context. This is a formal version of the discourse coherence principle: a coherent discourse is one in which the meanings of its parts can be "glued together" into a meaning for the whole.

The topos-theoretic perspective connects to the categorical architecture in several ways. First, a topos is a cartesian closed category, and therefore has an internal language that is a typed lambda calculus. This means that the compositional, type-driven approach to meaning -- the approach that RP-01 identified as the core of the unified semantics -- is available *within* any topos. The topos provides both the contextual structure (the presheaf/sheaf structure) and the compositional structure (the CCC structure), integrated into a single framework.

Second, the subobject classifier of a topos -- the analogue of the set {true, false} in **Set** -- is not, in general, a two-element set. In a presheaf topos, the subobject classifier assigns to each context a set of "truth values in that context," which may include intermediate values (neither fully true nor fully false). This provides a natural framework for modelling the *graded* truth values that appear in vague language ("tall," "bald," "heap"), in probabilistic reasoning, and in the graded similarity judgments that distributional semantics captures.

Third, the internal logic of a topos is intuitionistic, which connects the topos-theoretic perspective to the constructive tradition in logic and to the Curry-Howard-Lambek correspondence. In a topos, every proof has computational content (a programme that computes a witness); there are no non-constructive existence proofs. This constructive character aligns with the computational perspective on meaning: meaning is not merely truth-in-a-model but *constructive evidence* for truth, which is to say, a programme.

The topos-theoretic unification remains, however, largely programmatic. While presheaf models have been applied to specific phenomena in programming language semantics and specific phenomena in natural language semantics, a comprehensive topos-theoretic natural language semantics does not yet exist. The challenges include the intuitionistic restriction (natural language semantics typically assumes classical logic), the difficulty of specifying the category of contexts for natural language discourse, and the computational complexity of reasoning in presheaf toposes. Nevertheless, the topos-theoretic perspective provides the most general categorical framework for contextual meaning, and its development represents one of the most promising frontiers of the categorical architecture.

---

## 4. The Unification Claim

### 4.1 What Is Unified

The categorical architecture constructed in Section 3 unifies four formally distinct domains:

1. **Grammar.** The structure of well-formed expressions in a language (natural or formal), as captured by formal grammars, particularly categorial grammars and the Lambek calculus.

2. **Logic.** The structure of valid inference, as captured by proof systems, particularly natural deduction and sequent calculus.

3. **Computation.** The structure of typed programmes, as captured by typed lambda calculi and their extensions.

4. **Natural language semantics.** The structure of linguistic meaning, as captured by Montague grammar, dynamic semantics, and distributional semantics.

These four domains share a common categorical skeleton. In each domain:

- There are *objects* (syntactic types, propositions, programme types, semantic types).
- There are *morphisms* between objects (grammatical derivations, proofs, programmes, meaning-composition operations).
- There is *composition* of morphisms (combining derivations, concatenating proofs, composing programmes, composing meanings).
- There is *identity* for each object (the trivial derivation, the identity proof, the identity programme, the trivial meaning).
- There are *functors* between the syntactic and semantic aspects (meaning assignment, semantic interpretation, denotational semantics, model-theoretic evaluation).
- There are *natural transformations* between functors (the coherence conditions on meaning assignment, the rule-to-rule hypothesis, adequacy and full abstraction results).

The claim is that this shared skeleton is not accidental but reflects a genuine structural identity: the four domains are four perspectives on a single mathematical structure. The Curry-Howard-Lambek correspondence provides the formal mechanism of identification for the syntactic side (grammars = types = proofs = objects/morphisms in categories); the eight bridges of RP-01 provide the evidence of identification for the semantic side (meaning assignment has the same structural character in all traditions).

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

This five-way table extends RP-06's four-way table (grammar, logic, computation, category) by adding a fifth column for semantics, drawn from RP-01's analysis of the eight bridges. The addition of the semantic column is the distinctive contribution of the present synthesis: it shows that the structural unification identified by RP-06 on the syntactic side is mirrored by a structural unification on the semantic side, and that the two are connected by the functorial passage from syntax to semantics.

The five-way correspondence is strongest at the centre of each domain -- the classical, compositional, typed core -- and weakens toward the periphery. At the centre, the correspondence is an isomorphism: there are precise, invertible translations between the five presentations. At the periphery, the correspondence degrades:

- Pragmatic meaning (implicature, presupposition, speech acts) has no counterpart in the logic, computation, or category columns.
- Concurrent computation has no satisfactory counterpart in the grammar or logic columns (linear logic provides a partial account, but the full Curry-Howard for concurrency remains open).
- Distributional meaning (vector-space representations, learned embeddings) does not directly correspond to proofs or programmes (though DisCoCat provides a categorical bridge to compact closed categories).
- Non-compositional meaning (idioms, coercion, co-predication) requires enrichment of the functorial architecture (type-shifting, monadic effects, or lexical stipulation).

### 4.3 Evidence for the Claim

The evidence for the five-way correspondence is of three kinds:

**Formal evidence.** Mathematical theorems establish precise correspondences between pairs of columns. The Curry-Howard correspondence establishes the logic-computation correspondence (propositions = types, proofs = programmes). Lambek's theorem establishes the computation-category correspondence (typed lambda calculi = cartesian closed categories). The weak equivalence of the Lambek calculus with context-free grammars establishes a grammar-logic correspondence. Montague's rule-to-rule hypothesis, formalised as a functorial semantics, establishes a grammar-semantics correspondence. The adequacy and full abstraction results for denotational semantics establish a computation-semantics correspondence. Each of these formal results has been proven rigorously and published in the mathematical literature.

**Structural evidence.** The eight bridges of RP-01 provide structural evidence that the same mathematical concepts (compositionality, lambda calculus, types, models, games, dynamics, inferential role) appear with the same structural character across traditions. The fourfold of RP-06 provides structural evidence that the same hierarchy of complexity (regular, context-free, context-sensitive, unrestricted) appears in grammars, automata, type systems, and logics. The coincidence of these parallel structures across independently developed traditions is strong evidence of underlying unity.

**Historical evidence.** The historical development of the relevant theories exhibits a pattern of convergent discovery. Chomsky and Backus independently discovered context-free grammars; Curry and Howard independently discovered the proofs-as-programmes correspondence; Lambek extended this to categories and, independently, to linguistic grammar; Montague developed his formal semantics in close intellectual proximity to Scott's domain theory (both were at UCLA in the late 1960s); game semantics was independently developed in logic (Lorenzen), natural language (Hintikka), and computer science (Abramsky, Hyland, Ong). This pattern of convergent discovery -- the same structures being found by researchers working in different fields with different motivations -- is the hallmark of a genuine structural unity rather than a projection of one discipline's concepts onto another.

### 4.4 Evidence Against: Where the Correspondence Fails

Intellectual honesty requires that the evidence against the unification claim be given equal weight. The failures are of four kinds:

**Pragmatics and non-compositionality.** Natural language meaning is pervasively context-dependent in ways that have no natural counterpart in logic or computation. Conversational implicature, speech acts, presupposition, and discourse structure all contribute to the meaning of an utterance in ways that go beyond the compositional, type-driven framework. Idioms, metaphor, and coercion resist compositional treatment. These phenomena do not refute the compositional core of the architecture, but they do show that the architecture captures only a *fragment* of natural language meaning -- the compositional, truth-conditional fragment -- and that a substantial portion of meaning falls outside its scope.

**Neural representations and opacity.** Modern neural language models (transformers, large language models) achieve remarkable performance on a wide range of linguistic tasks, yet their internal representations do not obviously correspond to the typed, compositional structures of the categorical architecture. Probing studies show that transformers encode some syntactic and semantic structure implicitly, but the representations are distributed, continuous, and opaque -- not the discrete, algebraic, transparent structures of categorial grammar or typed lambda calculus. The question of whether neural representations *can be* categorified -- whether there exists a categorical framework that captures what transformers learn -- is open. DisCoCat provides one answer (functors into **FdVect**), but current DisCoCat models are far simpler than transformer architectures and do not capture the full range of phenomena that transformers handle.

**Concurrency and interaction.** The Curry-Howard-Lambek correspondence, as currently formulated, applies to *sequential* computation. Concurrent computation -- multiple interacting processes executing simultaneously -- disrupts the correspondence. Linear logic (Girard 1987) provides a partial account of concurrency through its resource-sensitive connectives, and session types provide a type-theoretic account of communication protocols, but a full "Curry-Howard for concurrency" -- a precise correspondence between concurrent proofs, concurrent programmes, and morphisms in an appropriate category -- remains an open problem. Since natural language discourse is inherently interactive (multi-party, turn-taking, jointly constructed), the absence of a satisfactory categorical account of concurrency limits the architecture's applicability to discourse-level meaning.

**The gap between formal adequacy and empirical coverage.** The categorical architecture, like the formal semantic traditions from which it derives, prioritises *structural elegance* and *mathematical precision* over *empirical coverage* and *psychological plausibility*. The architecture explains how meaning *could* be structured, given the formal properties of grammars, types, proofs, and categories. It does not explain how meaning *is* processed by human cognition, or how meaning *is* learned from experience, or how meaning *is* represented in neural tissue. The gap between formal adequacy and empirical coverage is not a refutation of the architecture, but it is a significant limitation: the architecture describes the *logical space* of meaning, not the *actual mechanism* of meaning.

---

## 5. The Distributional Challenge

### 5.1 Can Vector-Space Semantics Be Categorified?

The distributional tradition in semantics, rooted in the distributional hypothesis of Zellig Harris (1954) and John Rupert Firth (1957), represents the meaning of a word as a point in a high-dimensional vector space, where the dimensions correspond to contextual features and the position of the point encodes the statistical distribution of the word's occurrences across contexts. Modern incarnations of this approach -- word2vec (Mikolov et al. 2013), GloVe (Pennington et al. 2014), and the contextual embeddings of BERT (Devlin et al. 2019) and GPT (Radford et al. 2018, 2019; Brown et al. 2020) -- have demonstrated that vector-space representations capture rich semantic information: synonymy (nearby vectors), analogy (vector arithmetic), selectional preferences (clustering), and even aspects of logical structure (entailment direction).

The question for the categorical architecture is whether this vector-space approach can be *categorified* -- whether the distributional tradition can be incorporated into the functorial framework as a particular choice of semantic category, rather than standing as an alternative to formal semantics.

The answer involves distinguishing between *lexical* and *compositional* distributional semantics. At the lexical level, the distributional approach assigns meanings to individual words. This is straightforwardly categorifiable: the meaning of a word is a vector (an object in the semantic category **FdVect**), and the distributional hypothesis provides the empirical method for determining which vector. At the compositional level, the question is how to compute the meaning of a phrase or sentence from the meanings of its words. This is where the distributional tradition has historically been weakest and where the categorical framework provides its greatest contribution.

Naive approaches to compositional distributional semantics -- additive models (the meaning of a phrase is the sum of its word vectors) and multiplicative models (the meaning is the component-wise product) -- violate compositionality in the functorial sense: the "composition" is not governed by syntactic structure, and the meaning of "dog bites man" is the same as the meaning of "man bites dog." The categorical architecture, via DisCoCat, resolves this by making the composition *structure-dependent*: the grammatical derivation determines the linear map that combines the word vectors, so that different syntactic structures produce different meanings.

### 5.2 The DisCoCat Answer

DisCoCat's categorical answer to the distributional challenge, as detailed in Section 3.5, proceeds through three moves.

**First move: choose the right categories.** The syntactic category is a pregroup grammar (or, more precisely, the free rigid category generated by a pregroup grammar). The semantic category is **FdVect** (finite-dimensional vector spaces and linear maps). Both are compact closed categories, so they share the structural features needed for the functorial passage.

**Second move: define the functor.** The DisCoCat functor F: **G** -> **FdVect** assigns vector spaces to basic types and tensors to words. The meaning of a sentence is computed by applying the linear map determined by the grammatical derivation to the tensor product of the word vectors. This computation can be represented as a tensor network contraction and can be carried out efficiently.

**Third move: learn the parameters.** The word vectors and the tensors assigned to relational words (verbs, adjectives, prepositions) are learned from corpus data using distributional methods. The grammatical structure is provided by a parser (typically a CCG parser, though pregroup parsers have also been developed). The result is a model in which the *structure* is provided by the categorical framework and the *content* is provided by distributional learning.

DisCoCat thus provides a principled answer to the question of whether vector-space semantics can be categorified: yes, via compact closed categories and strong monoidal functors. The answer is not complete -- the limitations identified in Section 3.5 remain -- but it demonstrates that the distributional and formal traditions are not irreconcilable. They occupy different semantic categories (truth-conditional semantics lives in **Set** or a topos; distributional semantics lives in **FdVect**), and the relationship between these categories (the forgetful functor from **Set** to **FdVect** and its adjoints) provides the formal basis for their comparison.

### 5.3 What Transformers Learn vs. What Categorical Semantics Describes

The rise of transformer-based language models -- beginning with the "Attention Is All You Need" architecture (Vaswani et al. 2017) and culminating in large language models (LLMs) -- has transformed the empirical landscape of distributional semantics. Transformers learn contextual representations that capture syntactic structure, semantic relations, and even aspects of pragmatic reasoning, achieving state-of-the-art performance on a wide range of NLP benchmarks.

The relationship between what transformers learn and what the categorical architecture describes is subtle and contested. Several observations bear on this relationship:

**Transformers implicitly encode syntactic structure.** Probing studies (Hewitt and Manning 2019; Clark et al. 2019; Jawahar et al. 2019) have shown that transformer attention patterns encode syntactic dependency relations, that specific attention heads specialise in specific syntactic relations (e.g., subject-verb agreement, relative clause attachment), and that syntactic information is distributed across layers in a roughly hierarchical fashion (lower layers encode local syntactic relations, higher layers encode longer-distance relations). This suggests that transformers, despite lacking explicit grammatical structure, learn representations that are *compatible* with the syntactic categories of categorial grammar.

**Transformers do not directly implement compositional semantics.** Despite encoding syntactic structure, transformers do not compute meaning compositionally in the sense of the categorical architecture. The meaning of a sentence in a transformer is not computed by applying type-driven combination rules to the meanings of the words; rather, it is computed by a learned function (a sequence of attention and feed-forward layers) that takes the entire sequence as input and produces a contextual representation for each token. This function may be *approximately* compositional -- the representations of compound expressions may be *approximately* determined by the representations of their parts -- but the approximation is not exact, and the degree of compositionality varies across constructions and model architectures.

**The categorical architecture describes the *structure* of meaning; transformers implement a *mechanism* for computing meaning.** The two are not competitors but address different questions. The categorical architecture asks: what is the mathematical structure of the relationship between syntax and semantics? Transformers ask: what computation, when trained on large corpora, produces representations that support accurate prediction of linguistic behaviour? The categorical architecture provides the *what*; transformers provide the *how*. A reconciliation of the two would require showing that the computation transformers perform *implements* (or approximates) a functorial passage from a syntactic category to a semantic category. This is an open research question, and its resolution would constitute a major advance in our understanding of both categorical semantics and neural language processing.

**The attention mechanism has a categorical interpretation.** Recent work (notably by Gavranovic et al. 2024 and related efforts) has explored categorical interpretations of the attention mechanism, treating multi-head attention as a family of natural transformations between representation functors. While this work is preliminary, it suggests that the categorical architecture may be extensible to transformer-based models, with the attention mechanism playing the role of the natural transformation that mediates between syntactic and semantic interpretations.

### 5.4 The Reconciliation Frontier

The reconciliation of distributional/neural semantics with categorical/formal semantics defines one of the most important frontiers in the study of meaning. The present synthesis identifies three dimensions of this frontier:

**Grounded meaning.** The categorical architecture, like the formal semantic traditions it synthesises, treats meaning as a relationship between linguistic expressions and mathematical structures (models, types, categories). It does not, by itself, address the question of how meaning is *grounded* in perception, action, and embodied experience. Grounded semantics approaches (Harnad 1990; Barsalou 1999; Roy 2005) seek to connect linguistic representations to sensory-motor representations, and recent work on multimodal neural models (CLIP, Flamingo, Gemini) provides computational instantiations of this connection. The categorical architecture could, in principle, incorporate grounding by enriching the semantic category: instead of **FdVect** (vector spaces of word co-occurrences), the semantic category could be a category of multimodal representations that include perceptual and motor features. The formal development of such a grounded categorical semantics remains a task for future research.

**Embodied cognition.** The embodied cognition tradition (Lakoff and Johnson 1980, 1999; Varela, Thompson, and Rosch 1991) challenges the computational view of meaning by arguing that meaning is constituted by bodily experience, not by formal manipulation of abstract symbols. If meaning is fundamentally embodied, then the categorical architecture -- which is, by construction, a theory of *formal* meaning -- captures at best the surface structure of meaning and misses its experiential core. The tension between formal and embodied approaches to meaning is not resolved by the present synthesis; it is identified as a fundamental boundary condition on the architecture's scope.

**Hybrid architectures.** The most promising near-term direction is the development of *hybrid architectures* that combine categorical structure with neural computation. The lambeq framework (Kartsaklis et al. 2021), which implements DisCoCat models as parameterised quantum circuits, represents one such hybrid: the categorical structure provides the compositional skeleton, and the quantum (or classical) parameters are learned from data. The development of hybrid architectures that combine the structural transparency of categorical semantics with the empirical power of neural models is, the present author submits, the central challenge for the next decade of research on the formal architecture of meaning.

---

## 6. Implications for the ORGANVM System

The categorical architecture of formal meaning, while developed in the context of logic, linguistics, and computer science, has practical implications for the design of multi-representational systems -- systems that must manage multiple representations of the same entities and ensure consistency across representations. The ORGANVM system, as a multi-organ creative-institutional architecture comprising over one hundred repositories organised into eight functional organs, is precisely such a system. This section draws four implications.

### 6.1 Multi-Representational Systems as Multi-Syntactic Domains

The ORGANVM system maintains multiple representations of each entity (repository, organ, event, schema). A repository is represented in the registry (registry-v2.json) as a JSON object with fields for name, organ, tier, status, and dependencies. The same repository is represented in its seed contract (seed.yaml) as a YAML document declaring organ membership, produces/consumes edges, and event subscriptions. It is represented on GitHub as a repository with metadata (description, topics, visibility). It is represented in the dashboard as a visual element with colour, position, and status indicators.

In the categorical framework, each of these representations is a *semantic interpretation* of the repository entity -- a functor from the syntactic category of entity descriptions to a semantic category of representational objects. The registry functor F_reg maps entities to JSON objects; the seed functor F_seed maps entities to YAML documents; the GitHub functor F_gh maps entities to API objects; the dashboard functor F_dash maps entities to visual elements. The consistency requirement -- that the same entity has compatible representations across all four systems -- is the requirement that these functors are related by natural transformations: for each entity A, the registry representation F_reg(A), the seed representation F_seed(A), the GitHub representation F_gh(A), and the dashboard representation F_dash(A) must be coherently related, and changes to one representation must propagate coherently to the others.

### 6.2 Schema Contracts as Syntactic Categories

The seed.yaml contracts that define each repository's interface -- its organ membership, its produces/consumes edges, its event subscriptions -- can be understood as syntactic types in a categorial grammar of the ORGANVM system. Each contract declares what a repository *is* (its type) and what it *does* (the types of its inputs and outputs). The grammar of seed.yaml is, in effect, a type system for the ORGANVM architecture: a well-formed seed.yaml is a well-typed term, and the validation of seed.yaml contracts is type-checking.

The Chomsky hierarchy, as characterised by RP-06, provides a framework for classifying the complexity of this type-checking. Simple syntactic validation (checking that required fields are present, that values have the correct type) is a regular or context-free operation. Cross-repository validation (checking that dependency edges are acyclic, that produces/consumes edges match, that organ membership is consistent) is a context-sensitive operation. The governance rules that determine promotion eligibility (LOCAL -> CANDIDATE -> PUBLIC_PROCESS -> GRADUATED) require checking properties that may depend on the entire system state, potentially approaching the limits of decidability.

The architectural implication is that governance rules should be stratified by complexity: regular rules (naming conventions, field presence) should be checked first and automatically; context-free rules (schema structure, type-level consistency) should be checked next; context-sensitive rules (cross-repository dependencies, system-wide invariants) should be checked last and may require human judgment for boundary cases. This stratification mirrors the Chomsky hierarchy and reflects the increasing difficulty of validation at each level.

### 6.3 Registry Operations as Functorial Transformations

Registry operations -- adding a repository, updating its status, promoting it through the state machine, archiving it -- are transformations of the system's state. In the categorical framework, these transformations should be *functorial*: they should preserve the compositional structure of the system. Adding a repository should not break existing dependency edges; promoting a repository should not violate the dependency flow constraints; archiving a repository should not leave dangling references.

The functoriality requirement provides a design principle: every registry operation should be implemented as a *structure-preserving map* from the current system state to the new system state. The composition of two operations should be the same as the single operation that produces the combined effect. The identity operation (no change) should leave the system state unchanged. These are the functor laws, applied to system administration.

The natural transformation perspective provides a further design principle: when the representation of an entity changes (e.g., when a seed.yaml contract is updated to declare a new produces edge), the change should propagate *naturally* -- coherently and automatically -- to all other representations (the registry, the dashboard, the GitHub metadata). The naturality condition ensures that the propagation is consistent regardless of the order in which representations are updated.

### 6.4 Where the Categorical Framework Informs System Design

The categorical architecture of meaning informs ORGANVM system design at three levels:

**At the naming level.** The double-hyphen naming convention (single hyphen separates words within a function or descriptor; double hyphen separates function from descriptor) can be understood as a type-forming operation: the function and descriptor are typed components, and the double hyphen is the type constructor that combines them into a compound type. The naming convention thus implements a simple categorial grammar for repository names, and the well-formedness of a name is a type-checking operation.

**At the schema level.** The seed.yaml contracts implement a type system for the ORGANVM architecture. The governance-rules.json implements the typing constraints (dependency flow, promotion prerequisites). The validate-deps.py script implements the type-checker. This stack -- type assignments (seed.yaml), type constraints (governance-rules.json), type-checker (validate-deps.py) -- is an instance of the categorical architecture: the syntactic category is the grammar of seed.yaml contracts, the semantic category is the domain of system states, and the validation functor maps well-typed contracts to valid system states.

**At the governance level.** The promotion state machine (LOCAL -> CANDIDATE -> PUBLIC_PROCESS -> GRADUATED -> ARCHIVED) can be understood as a morphism in the category of system states. The promotion of a repository from LOCAL to CANDIDATE is a morphism that transforms the system state, subject to the constraint that the promotion is *valid* -- that the pre-conditions are met and the post-conditions are satisfied. This is precisely the structure of Hoare logic (axiomatic semantics), which RP-01 identified as one of the three approaches to programming language semantics. The categorical architecture thus provides a unified perspective on system governance: promotion rules are Hoare triples, validation is type-checking, and the system's evolution is a sequence of valid state transformations -- a programme in the language of system administration.

---

## 7. Discussion

The categorical architecture constructed in this dissertation is both a *synthesis* and a *proposal*. As a synthesis, it combines the results of RP-01 (the eight bridges) and RP-06 (the fourfold correspondence) into a single framework, showing that the bridges and the fourfold are two aspects of a single mathematical structure: the functorial passage from syntax to semantics. As a proposal, it claims that this functorial passage constitutes the *architecture* of formal meaning -- the deep structure that is common to all compositional, type-driven, formally rigorous approaches to meaning, whether the domain is logic, computation, or natural language.

The strengths of the architecture may be summarised as follows:

**Unifying power.** The architecture provides a single framework in which the results of RP-01 and RP-06 are not merely listed but *connected*. The eight bridges of RP-01 are not eight separate observations but eight manifestations of a single functorial structure. The fourfold of RP-06 is not a mere table of analogies but the structural characterisation of the syntactic side of the functor. The five-way correspondence of Section 4.2 is the explicit connection between the two.

**Precision.** The categorical formulation replaces informal notions of "analogy," "parallel," and "correspondence" with precise mathematical concepts: functor, natural transformation, adjunction, equivalence. Each of these concepts has a rigorous definition and a body of established theory. The claims of the dissertation can, in principle, be verified or refuted by checking whether the claimed categorical structures actually exist and satisfy the claimed properties.

**Productivity.** The categorical architecture generates predictions that go beyond the observations on which it is based. The naturality of Montague's rule-to-rule correspondence, the compact closed structure shared by pregroup grammars and vector spaces, the presheaf-theoretic account of contextual meaning, and the interpretation of schema contracts as syntactic categories are all consequences of the architecture that are not obvious from RP-01 or RP-06 considered separately.

The weaknesses of the architecture are equally significant:

**Scope limitation.** The architecture applies to the *classical, compositional, typed* core of each tradition and does not extend to the periphery. Pragmatics, non-compositionality, neural representations, concurrency, and embodied meaning all fall outside the architecture's scope (or at best are accommodated by enrichments that stretch the framework). This means that the architecture captures the structure of *formal* meaning but not the full range of *human* meaning.

**Abstraction cost.** Category theory, by virtue of its extreme generality, can describe virtually any mathematical structure. The concern raised in RP-01 (Section 4.2) that categorical unification may be "mere redescription" at a higher level of abstraction has not been fully resolved. The present dissertation has attempted to address this concern by identifying *productive* uses of the categorical framework (DisCoCat, presheaf semantics, the naturality of rule-to-rule correspondences), but the possibility remains that some of the categorical reformulations add complexity without adding insight.

**Empirical gap.** The architecture is a *formal* construction, not an *empirical* theory. It describes how meaning *could be* structured, not how meaning *is* processed, learned, or represented in human cognition. The gap between the categorical architecture and empirical reality is bridged only partially by DisCoCat (which provides a testable model for compositional distributional semantics) and by the probing paradigm (which investigates whether neural models learn categorical structure). The full reconciliation of formal architecture and empirical mechanism is a task for future research.

The relationship between the categorical architecture and the existing literature deserves comment. The idea that meaning is functorial is not new: it is implicit in Montague's work, explicit in Janssen's algebraic formulations, and central to the DisCoCat framework. The contributions of the present synthesis are: (a) the *systematic* connection of this idea to the full range of bridges identified by RP-01 and the full range of correspondences identified by RP-06; (b) the explicit formulation of the *five-way correspondence* that extends the grammar-type-proof-category fourfold to include semantics; (c) the identification of the topos-theoretic perspective as a framework for contextual meaning within the architecture; and (d) the application of the architecture to the design of multi-representational systems.

---

## 8. Conclusion

This dissertation has undertaken the synthesis of RP-01 (*Toward a Grand Unified Semantics*) and RP-06 (*Grammars, Types, Proofs, and Categories*) into a single categorical architecture of formal meaning. The synthesis proceeds from a simple observation: RP-01 established that meaning, across three traditions, is a structure-preserving map from syntax to semantics; RP-06 established that syntax, across four formal frameworks, has a unified categorical structure. Combining these results, meaning itself has a unified categorical structure: it is the *functorial passage from a syntactic category to a semantic category*.

The architecture has been constructed through seven components: the treatment of meaning as functor, the identification of compositionality with functoriality, the exhibition of the Lambek calculus as the canonical syntactic category, the characterisation of Montague's rule-to-rule correspondence as natural transformation, the incorporation of distributional semantics via the DisCoCat framework, the exploitation of compact closed structure in pregroup grammars and vector spaces, and the development of presheaf semantics for contextual meaning within the topos-theoretic perspective.

The central claim -- the five-way correspondence among derivation, proof, programme, morphism, and meaning-composition -- has been stated precisely and evaluated against formal, structural, and historical evidence. The evidence supports the claim for the classical, compositional, typed core of each tradition. The evidence also reveals the boundary conditions: pragmatics, non-compositionality, neural representations, and concurrency fall outside the architecture's scope, defining the frontier of future research.

The distributional challenge -- the question of whether the statistical, geometric, data-driven approach to meaning can be reconciled with the formal, algebraic, structure-driven approach -- has been addressed through the DisCoCat framework, which demonstrates that reconciliation is *feasible* via compact closed categories and strong monoidal functors. The analysis of transformer-based language models suggests that the categorical architecture and neural computation address different aspects of the same phenomenon: the architecture describes the *structure* of meaning; neural models implement a *mechanism* for computing meaning. The reconciliation of structure and mechanism defines the central challenge for the next decade of research.

The implications for the ORGANVM system demonstrate that the categorical architecture is not merely theoretical: it provides design principles for multi-representational systems, interpreting schema contracts as syntactic categories, registry operations as functorial transformations, governance rules as Hoare triples, and naming conventions as type-forming operations. The architecture thus bridges the gap between foundational theory and applied system design, realising the ORGANVM mission of connecting theoretical understanding to practical infrastructure.

The prospect of a grand unified semantics -- a single formal framework encompassing truth-conditional meaning, compositional structure, distributional similarity, dynamic context change, interactive meaning, and inferential role -- remains an aspiration. But the categorical architecture constructed here provides its *skeleton*: the functorial passage from syntax to semantics, instantiated across traditions, formalised by category theory, and grounded by the five-way correspondence. The three traditions of semantics are not three different subjects sharing a homonymous label; they are three perspectives on a single subject -- the formal structure of meaning -- and the functorial architecture is the structure they share.

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

Barwise, J., and Perry, J. (1983). *Situations and Attitudes*. MIT Press.

Brandom, R. B. (1994). *Making It Explicit: Reasoning, Representing, and Discursive Commitment*. Harvard University Press.

Brandom, R. B. (2000). *Articulating Reasons: An Introduction to Inferentialism*. Harvard University Press.

Brown, T. B., et al. (2020). Language models are few-shot learners. In *Advances in Neural Information Processing Systems*, vol. 33, pp. 1877--1901.

Carpenter, B. (1997). *Type-Logical Semantics*. MIT Press.

Chomsky, N. (1956). Three models for the description of language. *IRE Transactions on Information Theory*, 2(3), 113--124.

Chomsky, N. (1957). *Syntactic Structures*. Mouton.

Chomsky, N. (1959). On certain formal properties of grammars. *Information and Control*, 2(2), 137--167.

Church, A. (1936). An unsolvable problem of elementary number theory. *American Journal of Mathematics*, 58(2), 345--363.

Church, A. (1940). A formulation of the simple theory of types. *Journal of Symbolic Logic*, 5(2), 56--68.

Clark, H. H. (1996). *Using Language*. Cambridge University Press.

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

Grice, H. P. (1975). Logic and conversation. In P. Cole and J. L. Morgan (eds.), *Syntax and Semantics*, Vol. 3, pp. 41--58. Academic Press.

Groenendijk, J., and Stokhof, M. (1991). Dynamic predicate logic. *Linguistics and Philosophy*, 14(1), 39--100.

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

Janssen, T. M. V. (1997). Compositionality. In J. van Benthem and A. ter Meulen (eds.), *Handbook of Logic and Language*, pp. 417--473. Elsevier.

Jawahar, G., Sagot, B., and Seddah, D. (2019). What does BERT learn about the structure of language? In *Proceedings of the 57th Annual Meeting of the ACL*, pp. 3651--3657.

Kamp, H. (1981). A theory of truth and semantic representation. In J. Groenendijk, T. Janssen, and M. Stokhof (eds.), *Formal Methods in the Study of Language*, pp. 277--322. Mathematisch Centrum.

Kartsaklis, D., Fan, I., Yeung, R., Pearson, A., Lorber, R., Toumi, A., de Felice, G., Meichanetzidis, K., Clark, S., and Coecke, B. (2021). lambeq: An efficient high-level Python library for quantum NLP. arXiv:2110.04236.

Kripke, S. (1959). A completeness theorem in modal logic. *Journal of Symbolic Logic*, 24(1), 1--14.

Kripke, S. (1963). Semantical considerations on modal logic. *Acta Philosophica Fennica*, 16, 83--94.

Lakoff, G., and Johnson, M. (1980). *Metaphors We Live By*. University of Chicago Press.

Lambek, J. (1958). The mathematics of sentence structure. *American Mathematical Monthly*, 65(3), 154--170.

Lambek, J. (1968). Deductive systems and categories I. *Mathematical Systems Theory*, 2, 287--318.

Lambek, J. (1972). Deductive systems and categories III. In F. W. Lawvere (ed.), *Toposes, Algebraic Geometry and Logic*, pp. 57--82. Springer.

Lambek, J. (1999). Type grammar revisited. In A. Lecomte, F. Lamarche, and G. Perrier (eds.), *Logical Aspects of Computational Linguistics*, pp. 1--27. Springer.

Lambek, J. (2001). Type grammars as pregroups. *Grammars*, 4(1), 21--39.

Lewis, D. (1969). *Convention: A Philosophical Study*. Harvard University Press.

Martin-Lof, P. (1984). *Intuitionistic Type Theory*. Bibliopolis.

Mikolov, T., Chen, K., Corrado, G., and Dean, J. (2013). Efficient estimation of word representations in vector space. In *Proceedings of the 1st International Conference on Learning Representations (ICLR)*.

Moggi, E. (1991). Notions of computation and monads. *Information and Computation*, 93(1), 55--92.

Montague, R. (1970a). English as a formal language. In B. Visentini et al. (eds.), *Linguaggi nella Societa e nella Tecnica*, pp. 189--224. Edizioni di Comunita.

Montague, R. (1970b). Universal grammar. *Theoria*, 36(3), 373--398.

Montague, R. (1973). The proper treatment of quantification in ordinary English. In J. Hintikka, J. Moravcsik, and P. Suppes (eds.), *Approaches to Natural Language*, pp. 221--242. Reidel.

Moortgat, M. (1997). Categorial type logics. In J. van Benthem and A. ter Meulen (eds.), *Handbook of Logic and Language*, pp. 93--177. Elsevier.

Morrill, G. (2011). *Categorial Grammar: Logical Syntax, Semantics, and Processing*. Oxford University Press.

Pennington, J., Socher, R., and Manning, C. D. (2014). GloVe: Global vectors for word representation. In *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pp. 1532--1543.

Plotkin, G. D. (1981). A structural approach to operational semantics. Technical Report DAIMI FN-19, University of Aarhus.

Plotkin, G. D., and Power, J. (2003). Algebraic operations and generic effects. *Applied Categorical Structures*, 11(1), 69--94.

Prawitz, D. (1965). *Natural Deduction: A Proof-Theoretical Study*. Almqvist and Wiksell.

Prawitz, D. (2006). Meaning approached via proofs. *Synthese*, 148(3), 507--524.

Radford, A., Narasimhan, K., Salimans, T., and Sutskever, I. (2018). Improving language understanding by generative pre-training. OpenAI Technical Report.

Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., and Sutskever, I. (2019). Language models are unsupervised multitask learners. OpenAI Technical Report.

Roy, D. (2005). Semiotic schemas: A framework for grounding language in action and perception. *Artificial Intelligence*, 167(1--2), 170--205.

Russell, B. (1908). Mathematical logic as based on the theory of types. *American Journal of Mathematics*, 30(3), 222--262.

Scott, D. S. (1970). Outline of a mathematical theory of computation. In *Proceedings of the Fourth Annual Princeton Conference on Information Sciences and Systems*, pp. 169--176.

Scott, D. S., and Strachey, C. (1971). Toward a mathematical semantics for computer languages. In J. Fox (ed.), *Proceedings of the Symposium on Computers and Automata*, pp. 19--46. Polytechnic Institute of Brooklyn Press.

Searle, J. R. (1969). *Speech Acts: An Essay in the Philosophy of Language*. Cambridge University Press.

Stabler, E. (1997). Derivational minimalism. In C. Retore (ed.), *Logical Aspects of Computational Linguistics*, pp. 68--95. Springer.

Steedman, M. (2000). *The Syntactic Process*. MIT Press.

Tarski, A. (1936). The concept of truth in formalized languages. In A. Tarski, *Logic, Semantics, Metamathematics*, 2nd ed. (1983), pp. 152--278. Hackett.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., and Polosukhin, I. (2017). Attention is all you need. In *Advances in Neural Information Processing Systems*, vol. 30, pp. 5998--6008.

Varela, F. J., Thompson, E., and Rosch, E. (1991). *The Embodied Mind: Cognitive Science and Human Experience*. MIT Press.

Veltman, F. (1996). Defaults in update semantics. *Journal of Philosophical Logic*, 25(3), 221--261.

---

*Studium Generale ORGANVM -- SGO-2026-SYN-001 -- DRAFT v1 -- 2026-03-21*

*Synthesis of RP-01 (The Semantics Bridge) and RP-06 (Chomsky to Computation)*
