---
sgo_id: SGO-2026-SYN-005
title: "The Architecture of Meaning"
tier: Dissertation (synthesis)
status: LOCAL (first draft)
target_venues: [Synthese, Philosophy and Phenomenological Research, arXiv cs.AI]
dependencies: [RP-01, RP-02, RP-04, RP-06]
bridges: [Adventure 1, Adventure 2, Adventure 4, Adventure 6]
date: 2026-03-21
---

# The Architecture of Meaning: A Unified Account from Naming Through Formalization to the Limits of Self-Description

**Studium Generale ORGANVM -- Cross-Adventure Synthesis SYN-05**

**Synthesis of RP-01 (The Semantics Bridge), RP-02 (Self-Reference and Limits), RP-04 (The Naming Problem), and RP-06 (Chomsky to Computation)**

---

## Abstract

This dissertation undertakes the penultimate synthesis of the Studium Generale ORGANVM research programme, unifying four prior investigations into a single architectural account of meaning. RP-04 established that naming is compression with information loss, subject to five characteristic failure modes. RP-01 and SYN-01 established that meaning, in its formal core, is the functorial passage from a syntactic category to a semantic category, with compositionality as functoriality. RP-06 established a fourfold correspondence among grammars, automata, types, and proofs, situating natural language at the mildly context-sensitive level of a computational hierarchy. RP-02 established that self-describing systems encounter an impossibility landscape -- Godelian incompleteness, Tarskian undefinability, and Rice's theorem -- that draws a bright line between syntactic self-description (tractable) and semantic self-description (intractable). The present work asks what these four results, taken together, reveal about the nature of meaning itself. The central claim is that meaning is not a single phenomenon but a four-dimensional architecture, whose dimensions are Reference (how meaning attaches to the world), Structure (how meaning composes), Computation (how meaning is realized in processing), and Reflexivity (where meaning encounters its own limits). These four dimensions are not rival theories but orthogonal aspects of a single phenomenon, and they stand in a cyclic dependency -- Reference constrains Structure, Structure constrains Computation, Computation constrains Reflexivity, and Reflexivity constrains Reference -- that constitutes a generative strange loop rather than a vicious circle. The paper develops this architectural claim, compares it with existing frameworks (Frege's two-level semantics, Morris's tripartite semiotics, the Ogden-Richards triangle), argues that four dimensions are both necessary and sufficient for a formal account, examines what the architecture cannot capture (pragmatics, embodiment, phenomenal consciousness, the hermeneutic dimension), and draws implications for philosophy of language, artificial intelligence, and the design of self-governing computational systems. The ORGANVM system is presented as a concrete instantiation of the four-dimensional architecture: its seed.yaml contracts realize the referential dimension, its registry operations realize the structural dimension, its CI/CD pipeline realizes the computational dimension, and its IRA panel realizes the reflexive dimension.

**Keywords:** meaning, philosophy of language, compositionality, self-reference, naming, type theory, category theory, Curry-Howard-Lambek correspondence, incompleteness, hermeneutics, intentionality, architecture of meaning, functorial semantics, strange loop

---

## 1. Introduction

### 1.1 The Convergence of Four Investigations

The question of what meaning is has occupied philosophy since its inception. Plato's *Cratylus* debates whether names attach to things by nature or by convention. Aristotle's *De Interpretatione* proposes that spoken sounds are symbols of mental impressions, which are in turn likenesses of things. The medieval scholastics developed elaborate theories of *significatio* and *suppositio*. The modern analytic tradition, from Frege through Russell, Wittgenstein, Carnap, Quine, Kripke, and Davidson, has produced a constellation of theories -- referential, descriptivist, causal, use-theoretic, truth-conditional, inferential, dynamic -- each illuminating one facet of meaning while leaving others in shadow. The continental tradition, from Husserl through Heidegger, Gadamer, and Ricoeur, has pursued the question through phenomenological and hermeneutic methods, emphasizing the lived experience of understanding, the historicity of interpretation, and the irreducibility of meaning to formal structure. The computational tradition, from Church and Turing through Chomsky, Montague, and the architects of modern type theory, has asked how meaning can be formalized, computed, and mechanically processed.

The Studium Generale ORGANVM research programme has approached this ancient question through four independent investigations, each tracing a different thread of the problem. These four threads, it will be argued, converge on a single architectural insight that none of them, taken alone, could have produced.

RP-04, *The Deep Structure of Naming*, established the first thread by examining how meaning attaches to things in the first place. The paper surveyed three traditions of naming theory -- the philosophical (Frege, Russell, Kripke, Wittgenstein), the linguistic-scientific (Saussure, Peirce, Linnaean taxonomy, controlled vocabularies), and the computational (identifiers, namespaces, ontologies) -- and identified a structural unity beneath their diversity. All three traditions describe the same fundamental phenomenon: a reference relation between a sign and a referent, established and maintained by some combination of convention, causation, and use. The paper's central finding was that naming is compression: every name compresses a complex entity into a manipulable token, and this compression necessarily entails information loss. Five characteristic failure modes -- reference failure, namespace collision, semantic drift, abstraction mismatch, and governance failure -- recur across all three traditions because they are structural features of the compression operation itself.

RP-01, *Toward a Grand Unified Semantics*, and its synthesis SYN-01, *The Architecture of Formal Meaning*, established the second thread by examining how meaning composes. RP-01 surveyed three traditions of formal semantics -- logical (Tarski, Kripke), computational (Scott, Strachey, Hoare), and natural language (Montague, Heim, Kratzer) -- and identified eight structural bridges connecting them: compositionality, lambda calculus, the Curry-Howard-Lambek correspondence, type theory, model theory, game semantics, dynamic semantics, and proof-theoretic semantics. Each bridge was assessed on a four-point scale of structural strength (isomorphism, homomorphism, analogy, metaphor), and the central finding was that the classical, compositional, typed fragment of each tradition admits genuine structural unification, with category theory providing the most perspicuous unifying metalanguage. SYN-01 crystallized this into a single claim: meaning is the functorial passage from a syntactic category to a semantic category, and this passage has the same categorical structure whether the syntax is linguistic, logical, or computational.

RP-06, *The Fourfold Correspondence*, established the third thread by examining how meaning is computationally realized. Beginning with Chomsky's 1956 hierarchy, the paper traced a fourfold correspondence among grammars, automata, type systems, and proof calculi. At each level of the hierarchy, a grammar corresponds to an automaton (the classical result), but also to a regime of type-theoretic expressiveness (regular grammars to finite types, context-free grammars to recursive algebraic types, context-sensitive grammars to parametric polymorphism, unrestricted grammars to full dependent types) and a proof-theoretic regime. The central finding was that natural language occupies a specific computational niche -- the mildly context-sensitive level -- and that this niche has characteristic decidability and complexity properties that constrain how meaning can be processed.

RP-02, *The Impossibility Landscape*, established the fourth thread by examining where meaning encounters its own limits. The paper mapped the family of impossibility results -- Godel's incompleteness theorems, Tarski's undefinability of truth, the halting problem, Rice's theorem, Lob's theorem -- and the productive forms of self-reference that flourish alongside them (quines, reflection, bootstrapping, autopoiesis). The central finding was a bright line between syntactic self-description (tractable) and semantic self-description (intractable), with the consequence that no system capable of encoding arithmetic can fully describe its own semantics. Seven design principles for self-governing systems were derived, all predicated on the recognition that self-referential meaning is inherently incomplete.

### 1.2 The Question That Unifies Them

These four investigations were conducted independently, each addressing a different research question. Yet they converge on a single, deeper question: *what is meaning?*

RP-04 answered: meaning begins with reference -- the attachment of a sign to a thing. RP-01 and SYN-01 answered: meaning is constituted by composition -- the functorial passage from syntax to semantics. RP-06 answered: meaning is realized through computation -- the processing of structured expressions by automata of appropriate power. RP-02 answered: meaning is bounded by reflexivity -- the impossibility of complete self-description.

These are not four rival answers to the same question. They are four answers to four different aspects of the same question, and it is the thesis of this dissertation that these four aspects are dimensions of a single architecture. To ask "what is meaning?" is not to seek a definition that can be stated in a single sentence. It is to describe a structure -- an architecture -- that has reference, composition, computation, and reflexivity as its four orthogonal dimensions. The architecture of meaning is not a theory *of* meaning, in the sense of a set of necessary and sufficient conditions. It is a theory of meaning's *shape* -- a description of the space within which all theories of meaning operate, the dimensions along which they vary, and the constraints that bind those dimensions together.

### 1.3 Scope and Method

The method of this dissertation is synthetic and architectural. It does not present new formal results in logic, linguistics, or computer science, nor does it offer new philosophical arguments about the nature of reference or the limits of self-knowledge. Rather, it takes the results of four prior investigations and assembles them into a unified structure, asking what the assembled whole reveals that the parts, taken separately, do not.

The scope is necessarily broad. A synthesis that spans the philosophy of language, formal semantics, computability theory, and category theory cannot achieve the depth of a monograph in any one of these fields. The compensating virtue is perspicuity: by mapping the architecture of meaning across its four dimensions, the dissertation reveals structural relationships -- particularly the cyclic dependency among dimensions -- that are invisible from within any single theoretical tradition.

The paper draws on the full philosophical tradition from Frege to Brandom, on the formal results of Godel, Tarski, Turing, Chomsky, Lambek, Montague, and Curry-Howard, and on the phenomenological and hermeneutic traditions of Husserl, Heidegger, Gadamer, and Ricoeur, the last of these invoked not as formal apparatus but as a boundary condition that delimits what the formal architecture can and cannot capture.

The remainder of the dissertation proceeds as follows. Section 2 develops the four dimensions of meaning in detail. Section 3 presents the architectural claim -- that the four dimensions are orthogonal, interacting, and cyclically dependent. Section 4 examines the limits of the architecture. Section 5 draws implications. Section 6 offers discussion. Section 7 concludes.

---

## 2. Four Dimensions of Meaning

The argument of this section is that meaning, as revealed by the four prior investigations, exhibits four dimensions that are conceptually distinct, formally characterizable, and jointly necessary for a comprehensive account. Each dimension corresponds to a different aspect of what it is for something to mean something, and each is grounded in a specific body of philosophical and formal work.

### 2.1 The Referential Dimension (from RP-04)

#### 2.1.1 How Meaning Attaches: The Primacy of Naming

Before meaning can compose, compute, or reflect upon itself, it must first *attach*. Something must come to stand for something else. A sound must come to signify a concept; a written mark must come to denote an object; an identifier must come to point to a memory address. This primary attachment -- the establishment of a reference relation between a sign and a referent -- is the foundational act of meaning, and it is the subject of RP-04's investigation.

The referential dimension of meaning concerns the question: *how does a sign come to mean what it means?* This question has received four major answers in the philosophical tradition, each illuminating a different mechanism of attachment.

Frege's answer, articulated in his 1892 paper "Uber Sinn und Bedeutung," is that a sign attaches to its referent through a *sense* -- a mode of presentation, a cognitive route by which a thinker grasps the object. The morning star and the evening star present the same referent (Venus) under different aspects, and these different aspects are constitutive of meaning. Understanding a name is not merely knowing what it picks out but grasping the particular way it picks it out. This sense-mediated reference generates the fundamental puzzle of informative identity: "Hesperus is Phosphorus" is informative precisely because the two names, though co-referential, differ in sense.

Russell's answer, developed in "On Denoting" (1905) and elaborated by Searle's cluster theory, is that names are disguised definite descriptions. The reference of "Aristotle" is determined by whatever object uniquely satisfies the associated descriptions -- the teacher of Alexander, the author of the *Metaphysics*, the most famous student of Plato. On this view, the attachment of name to thing is mediated by descriptive content, and meaning is, at bottom, a matter of description-fitting.

Kripke's answer, delivered in the lectures published as *Naming and Necessity* (1980), overthrew the Frege-Russell consensus. Names are *rigid designators*: they denote the same object in every possible world where that object exists. The name "Aristotle" refers to Aristotle even in counterfactual scenarios where everything we believe about him is false. Reference is fixed not by description but by an *initial baptism* -- a naming event in which the name is attached to an object by ostension or stipulation -- and transmitted through a community via a *causal chain* of communication. The causal theory separates reference from description and grounds meaning in historical-social practice rather than in cognitive content.

Wittgenstein's answer, articulated in the *Philosophical Investigations* (1953), refuses the question's presupposition. The meaning of a word is not a thing (neither a referent, nor a sense, nor a description) but its *use in the language*. Words participate in *language games* -- practices in which language and action are interwoven -- and meaning is constituted by the role the word plays in those practices. There is no single "meaning" extractable from a name independently of its contexts of use.

#### 2.1.2 Naming as Compression with Information Loss

RP-04's contribution to the referential dimension was the identification of a structural principle that underlies all four philosophical positions: *naming is compression*. Every name compresses a complex entity -- an object with indefinitely many properties, relations, and aspects -- into a finite, manipulable token. The compression is necessarily lossy: the name "Aristotle" does not encode the full complexity of the historical individual. This information loss is not a defect of naming but a constitutive feature. Without compression, naming would be impossible: a name that encoded all the information about its referent would be as complex as the referent itself and would fail to serve the cognitive function for which names exist.

The compression thesis has formal consequences. The tradeoff between referential precision (how unambiguously a name picks out its referent), descriptive richness (how much the name reveals about the properties of the referent), and cognitive cost (the mental effort required to process the name) is a universal constraint on naming systems. Every naming convention -- from Linnaean binomials to camelCase identifiers to IUPAC chemical nomenclature -- occupies a point on this tradeoff surface. The tradeoff is not merely aesthetic; it has measurable consequences for communication accuracy, retrieval precision, and system maintainability.

#### 2.1.3 Five Failure Modes of Reference

The referential dimension is subject to five characteristic failure modes, identified by RP-04 as structural features of the name-thing relation itself:

*Reference failure* occurs when a name points to nothing. Frege's "the largest integer" has sense but no reference. In computing, the null pointer exception is reference failure made operational: the program presupposed that a name had a referent, but it did not.

*Namespace collision* occurs when a single name maps to multiple referents within a scope. Homonymy in natural language ("bank" as financial institution versus river edge) and name collision in package registries are structural analogues of the same problem.

*Semantic drift* occurs when a name's associated meaning changes over time while the name persists. "Nice" once meant "foolish"; a function called `getUser()` may now also initialize a cache. The causal theory of reference predicts this phenomenon: the causal chain transmits the name, but the descriptions evolve independently.

*Abstraction mismatch* occurs when the same entity is represented by different names in different contexts. Kripke's puzzle about belief -- Pierre who believes "Londres est jolie" and "London is not pretty" without realizing they name the same city -- has its computational analogue in integration failures between systems that cannot agree on what to call the same thing.

*Governance failure* occurs when there is no authoritative mechanism for resolving naming disputes. Biological nomenclature solved this through international commissions; computing has fragmented governance across ICANN, npm, PyPI, and organizational style guides.

These five failure modes are not domain-specific accidents. They recur across philosophy, linguistics, and computing because they are structural features of the compression operation that constitutes naming. Any system that compresses complex entities into finite tokens is susceptible to all five.

#### 2.1.4 Key Finding: Reference Is Necessary but Not Sufficient

The referential dimension establishes that meaning begins with attachment -- with the establishment of a sign-thing relation. But reference alone does not constitute meaning. A name that refers does not thereby mean; it must also participate in a system of composition, be processable by some computational mechanism, and be subject to the limits that arise when the system of meaning attempts to describe itself. The referential dimension is the ground floor of the architecture of meaning, but it is not the entire building.

### 2.2 The Structural Dimension (from RP-01 and SYN-01)

#### 2.2.1 How Meaning Composes: Compositionality as the Structural Principle

The structural dimension of meaning concerns the question: *how do complex meanings arise from simpler ones?* If the referential dimension asks how a single sign attaches to a single thing, the structural dimension asks how the meanings of parts combine to produce the meaning of a whole.

The answer, convergently discovered across three independent traditions, is compositionality. The principle of compositionality, attributed to Frege and formalized by subsequent workers, states that the meaning of a complex expression is determined by the meanings of its constituent expressions and the rules used to combine them. This principle is not a philosophical stipulation but a structural discovery: it appears, with the same mathematical form, in logical semantics (Tarski's recursive definition of satisfaction), programming language semantics (Scott and Strachey's denotational method), and natural language semantics (Montague's rule-to-rule hypothesis).

RP-01's central contribution was the demonstration that compositionality, far from being merely a shared desideratum, is a genuine structural bridge across traditions. In the algebraic formulation developed by Janssen and others, compositionality is a *homomorphism* from a syntactic algebra (whose elements are expressions and whose operations are syntactic combination rules) to a semantic algebra (whose elements are meanings and whose operations are semantic combination functions). This algebraic formulation is identical across traditions: it is the same mathematical concept -- a structure-preserving map between algebras -- instantiated in three different domains.

#### 2.2.2 The Eight Bridges and Their Structural Strength

RP-01 identified eight structural bridges connecting the three traditions of formal semantics:

1. **Compositionality** -- the structure-preserving map from syntax to semantics. Structural strength: *isomorphism*.
2. **Lambda calculus** -- the formal system for function abstraction and application, simultaneously the foundation of functional programming, the notation of Montague grammar, and a proof-term calculus for intuitionistic logic. Structural strength: *isomorphism*.
3. **The Curry-Howard-Lambek correspondence** -- the three-way identification of proofs, programs, and categorical morphisms. Structural strength: *isomorphism* (three-way); *homomorphism* (extension to natural language).
4. **Type theory** -- the classification of meanings by types. Structural strength: *homomorphism*.
5. **Model theory** -- interpretation in mathematical structures. Structural strength: *isomorphism* (for classical fragments).
6. **Game semantics** -- meaning as interactive strategy. Structural strength: *homomorphism*.
7. **Dynamic semantics** -- meaning as context-change potential. Structural strength: *analogy tending toward homomorphism*.
8. **Proof-theoretic semantics** -- meaning as inferential role. Structural strength: *homomorphism*.

The hierarchy of bridge strengths reveals a significant pattern: the bridges closest to the classical, compositional, typed core (compositionality, lambda calculus, model theory) achieve isomorphism; those that extend the core (type theory, game semantics, proof-theoretic semantics) achieve homomorphism; and those at the dynamic periphery (dynamic semantics) are analogies under active formalization.

#### 2.2.3 The Five-Way Correspondence

SYN-01 crystallized RP-01's findings into the grand claim that meaning is the functorial passage from a syntactic category to a semantic category. When combined with RP-06's fourfold correspondence (grammar-automaton-type-proof), this yields a five-way correspondence:

| Grammar | Logic | Computation | Category | Semantics |
|---------|-------|-------------|----------|-----------|
| Syntactic category | Proposition | Type | Object | Semantic domain |
| Grammatical derivation | Proof | Program | Morphism | Meaning-composition |
| Functor category A/B | Implication | Function type | Exponential | Semantic function |
| Sentence formation | Modus ponens | Application | Evaluation | Denotation |
| Lexicon | Axioms | Constants | Generators | Lexical meanings |

A string of words is grammatical if and only if there exists a proof in the relevant logic that the type assignment entails the sentential type, if and only if there exists a well-typed lambda term of the appropriate type, if and only if there exists a morphism in the corresponding category, if and only if the compositional semantics yields a well-defined meaning. These are not five different activities that happen to be analogous. They are the same activity described in five mathematical languages.

#### 2.2.4 Key Finding: Meaning Is the Functorial Passage

The structural dimension yields a precise characterization of how meaning composes: meaning is a functor from syntax to semantics. The functor preserves composition (the meaning of a compound derivation is the composite of the meanings of its sub-derivations) and identity (the meaning of the trivial derivation is the identity on the corresponding semantic domain). Compositionality is not merely a desideratum or a methodological preference; it is the *defining structural property* of the functorial relationship that constitutes meaning assignment.

This characterization achieves its full force only when combined with the referential dimension. The functor maps syntactic objects (which have been given referential content by the naming acts of the lexicon) to semantic objects (which represent the compositional meanings of complex expressions). The lexicon -- the base of the functor -- is the interface between the referential and structural dimensions: it is where individually attached meanings enter the compositional machinery.

### 2.3 The Computational Dimension (from RP-06)

#### 2.3.1 How Meaning Is Realized: The Chomsky Hierarchy as Computational Architecture

The computational dimension of meaning concerns the question: *what computational resources are required to process meaning?* If the referential dimension asks how meaning attaches and the structural dimension asks how meaning composes, the computational dimension asks how meaning is *realized* -- what kinds of machines, automata, or processors can implement the compositional operations that constitute meaning assignment.

RP-06 established that this question has a precise answer, structured by the Chomsky hierarchy. The hierarchy stratifies formal grammars into four types of increasing generative power -- regular (Type 3), context-free (Type 2), context-sensitive (Type 1), and unrestricted (Type 0) -- and each type corresponds to a class of abstract machines with characteristic computational properties: finite automata, pushdown automata, linear bounded automata, and Turing machines, respectively.

The fourfold correspondence extends this grammar-automaton pairing to include type systems and proof calculi:

| Level | Grammar | Automaton | Type System | Decidability |
|-------|---------|-----------|-------------|-------------|
| Type 3 | Regular | Finite automaton | Finite types | O(n) |
| Type 2 | Context-free | Pushdown automaton | Recursive algebraic types | O(n^3) |
| MCS | TAG/CCG | Embedded PDA | *(Open problem)* | O(n^6) |
| Type 1 | Context-sensitive | Linear bounded automaton | Parametric polymorphism | PSPACE-complete |
| Type 0 | Unrestricted | Turing machine | Full dependent types | Undecidable |

Each level imposes a specific regime of computational cost on the processing of meaning. Regular phenomena (phonotactics, morphological inflection) can be processed in linear time with finite memory. Context-free phenomena (phrase structure, recursive nesting) require a stack and cubic time. Context-sensitive phenomena (agreement, type checking, scope resolution) require space proportional to the input. Unrestricted computation (arbitrary reasoning, theorem-proving) is undecidable in the general case.

#### 2.3.2 Natural Language in the Computational Landscape

A landmark finding of formal linguistics, crystallized by Joshi (1985) and corroborated by Shieber (1985), is that natural language occupies a specific computational niche: the *mildly context-sensitive* level, intermediate between context-free and context-sensitive. This level is characterized by four properties: it generates all context-free languages; it can generate some context-sensitive languages (notably {a^n b^n c^n}); it has the constant growth property; and its recognition problem is solvable in polynomial time.

The mildly context-sensitive class is significant for the architecture of meaning because it imposes a specific constraint on the computational realization of natural language semantics. The formal systems that capture this class -- tree-adjoining grammars, combinatory categorial grammars, head grammars, linear indexed grammars -- have been shown to be weakly equivalent, generating the same class of string languages. This convergence suggests that the computational complexity of natural language is a robust natural property rather than an artifact of any particular formalism.

The identification of natural language's computational niche has direct consequences for the structural dimension. The compositional semantics of a language is constrained by the computational complexity of its syntax: a semantics that requires operations beyond the computational power of the language's syntactic processing mechanisms is unrealizable. The functor from syntax to semantics must be computable within the complexity class of the syntax. This constraint links the structural and computational dimensions: the compositional architecture of meaning is bounded by the computational architecture that realizes it.

#### 2.3.3 The Grammar-Type-Proof Equivalence in Practice

The practical import of the computational dimension is visible in the architecture of compilers and natural language processing systems, both of which reflect the Chomsky hierarchy in their internal structure. A compiler's front end stratifies its processing into a lexer (operating at the regular level), a parser (operating at the context-free level), and a semantic analyzer (operating at the context-sensitive level). This stratification is not an engineering convenience but a mathematical necessity: each phase operates at the most restrictive level that suffices for its task, minimizing computational cost.

In natural language processing, the fourfold correspondence has been operationalized through CCG-based semantic parsers that translate English sentences into typed logical forms -- lambda-calculus expressions with explicit types -- that can be evaluated against a knowledge base. In these systems, parsing constructs a grammatical derivation, which *is* a proof in a type-logical system, which *determines* a typed lambda term, which *is* a query. The fourfold operates in real time, demonstrating that the correspondence is not merely a theoretical elegance but a viable engineering architecture.

#### 2.3.4 Key Finding: Meaning Occupies a Computational Niche

The computational dimension reveals that meaning is not computationally arbitrary. Natural language meaning is realized at a specific level of the Chomsky hierarchy -- the mildly context-sensitive level -- with characteristic complexity and decidability properties. The computational resources required to process meaning are precisely constrained by the syntactic complexity of the language and the type-theoretic expressiveness of its compositional semantics. Meaning is not free-floating; it is anchored in a computational substrate that determines what compositional operations are tractable, what type-checking procedures are decidable, and what inferences are effectively computable.

### 2.4 The Reflexive Dimension (from RP-02)

#### 2.4.1 How Meaning Encounters Itself: Self-Reference and Its Consequences

The reflexive dimension of meaning concerns the question: *what happens when a system of meaning turns its descriptive apparatus upon itself?* If the referential dimension asks how meaning attaches, the structural dimension how it composes, and the computational dimension how it is realized, the reflexive dimension asks what occurs at the boundary where meaning attempts to describe its own operations.

RP-02 established that this boundary is drawn with mathematical precision. The family of impossibility results -- Godel's incompleteness theorems, Tarski's undefinability of truth, the halting problem, Rice's theorem, Lob's theorem -- collectively demonstrate that when a sufficiently expressive formal system turns its descriptive apparatus upon itself, the resulting self-reference generates objects that the system cannot consistently classify. The system is powerful enough to construct self-referential questions but not powerful enough to answer them all.

The impossibility results are not independent curiosities. They share a common proof technique -- the diagonal argument, originating in Cantor's 1891 proof -- and they express a single underlying structural fact: a system cannot serve as its own metalanguage without remainder. Every attempt to collapse the distance between object-level and meta-level generates objects that defeat the description.

The specific impossibilities include:

- *Complete self-proof is impossible* (Godel's first theorem): a consistent system cannot prove all truths about itself.
- *Self-certified consistency is impossible* (Godel's second theorem): a consistent system cannot prove that it is consistent.
- *Internal truth definition is impossible* (Tarski's theorem): a system cannot define a truth predicate for its own sentences.
- *Universal behavior prediction is impossible* (halting problem): no algorithm can predict the behavior of all programs, including itself.
- *General semantic inspection is impossible* (Rice's theorem): no algorithm can decide any non-trivial behavioral property of programs.
- *Provability-to-truth lifting is impossible except trivially* (Lob's theorem): a system cannot bootstrap truth from provability for statements not already provable.

#### 2.4.2 The Syntactic/Semantic Boundary

RP-02's most consequential finding for the architecture of meaning is the bright line between syntactic and semantic self-description. Syntactic properties of a system -- those that can be determined by inspecting the system's textual or structural representation without executing it or reasoning about its behavior -- are in general decidable. A linter can check whether code follows a naming convention; a schema validator can check whether a YAML file conforms to a schema; a dependency checker can verify the absence of circular imports. These are all syntactic operations, and Rice's theorem does not apply to them.

Semantic properties -- those that concern the system's behavior, purpose, correctness, or fitness -- are in general undecidable. Whether a program terminates, whether it computes a specific function, whether it is free from security vulnerabilities, whether it fulfills its intended purpose -- these are all semantic properties, and Rice's theorem guarantees that no algorithm can decide any of them in the general case.

This boundary has profound implications for meaning. Meaning itself is a semantic property: to ask "what does this expression mean?" is to ask about the behavior of the expression within a system of interpretation, and this behavior is precisely the kind of thing that Rice's theorem declares undecidable for sufficiently expressive systems. A system of meaning can describe the *syntax* of its own expressions exhaustively -- their form, their structure, their type-theoretic properties -- but it cannot decide the *semantics* of its own expressions in the general case. The system can talk about meaning, but it cannot fully determine meaning for itself.

#### 2.4.3 Productive Self-Reference: Quines, Reflection, and Fixed Points

The impossibility results prohibit *complete* self-description, not *any* self-description. RP-02 surveyed the productive forms of self-reference that remain available despite the impossibility walls.

*Quines* -- programs that output their own source code -- demonstrate that perfect syntactic self-description is achievable. A quine reproduces its syntax perfectly but knows nothing about its own semantics. It achieves self-description by remaining on the tractable side of the syntactic/semantic boundary.

*Reflection* in programming languages allows processes to examine and modify their own structure at runtime. Reflective programs can inspect their own types, methods, fields, and call stacks -- all syntactic properties. They cannot decide their own termination, correctness, or fitness -- all semantic properties.

*Bootstrapping* compilers demonstrate that self-reference becomes productive when it is staged temporally. A compiler at stage N is compiled by the compiler at stage N-1, breaking the circularity of simultaneous self-compilation into a well-ordered sequence of non-self-referential steps.

*Autopoietic* systems, as described by Maturana and Varela, maintain themselves through continuous self-production rather than formal self-verification. A living cell does not prove its own consistency; it detects deviations from operational norms and adjusts accordingly. This suggests that operational self-maintenance is achievable even when formal self-verification is not.

The fixed-point perspective unifies these productive forms of self-reference. Fixed-point theorems (Brouwer, Banach, Knaster-Tarski, the diagonal lemma) guarantee the existence of self-referential structures under specified conditions. The impossibility results arise when the fixed point generates a paradox (a sentence that is true if and only if it is not provable); the possibility results arise when the fixed point generates a stable, non-paradoxical structure (a program that outputs its own code). The difference lies not in the mechanism but in the property being self-referred to: self-reference is paradoxical for semantic properties and productive for syntactic properties.

#### 2.4.4 Key Finding: Meaning Cannot Fully Describe Its Own Semantics

The reflexive dimension establishes that meaning's encounter with itself produces a characteristic pattern: syntactic self-description succeeds; semantic self-description fails. A system of meaning can describe the forms, structures, and types of its own expressions -- their referential attachments, their compositional rules, their computational complexity -- but it cannot decide what its own expressions *mean* in the full, semantic sense. Meaning's self-knowledge is necessarily incomplete.

This incompleteness is not a defect of any particular formalism. It is a mathematical theorem that follows from the expressive power of the system. A system powerful enough to construct self-referential questions about its own semantics is a system that cannot answer them all. The reflexive dimension of meaning is the dimension of its own limitation.

---

## 3. The Architectural Claim

### 3.1 Meaning as Four-Dimensional Architecture

The central claim of this dissertation is that meaning is a four-dimensional architecture whose dimensions are:

1. **Reference** (attachment): how meaning connects signs to the world.
2. **Structure** (composition): how meanings of parts combine to produce meanings of wholes.
3. **Computation** (realization): what computational resources are required to process meaning.
4. **Reflexivity** (limits): where meaning encounters the boundaries of self-description.

These four dimensions are not rival theories of meaning. They are not competing answers to a single question. They are orthogonal aspects of a single, irreducibly complex phenomenon. A complete account of meaning must specify all four: how it attaches (reference), how it composes (structure), how it is processed (computation), and where it cannot go (reflexivity). An account that addresses fewer than four dimensions is incomplete; one that addresses all four captures the shape of meaning as a whole.

The analogy with physical architecture is deliberate. A building has height, width, depth, and structural integrity. None of these can be reduced to the others; none can be omitted without losing something essential. Height without width is a line, not a building. Structure without reference is a calculus that floats free of the world. Computation without composition is a machine without a language. Reflexivity without reference is self-reference without content.

The claim that meaning has exactly four dimensions requires both a positive argument (that these four are necessary) and a negative argument (that they are sufficient). The positive argument has been given by the four prior investigations: each addresses an aspect of meaning that none of the others captures. RP-04 addresses the question of how signs attach to things -- a question untouched by RP-01's analysis of composition, RP-06's analysis of computation, or RP-02's analysis of limits. RP-01 addresses the question of how meanings compose -- a question unaddressed by RP-04's analysis of naming, RP-06's analysis of the Chomsky hierarchy, or RP-02's analysis of impossibility. And so on for each dimension. No dimension is derivable from the others; each contributes something irreducible.

The negative argument -- that four dimensions suffice -- is more delicate and is addressed in Section 4, where candidate fifth dimensions (pragmatics, embodiment, affect, consciousness) are examined and argued to be either derivable from the existing four or genuinely beyond the scope of a formal architecture.

### 3.2 How the Dimensions Interact

The four dimensions are orthogonal -- no dimension can be reduced to another -- but they are not independent. Each constrains the others in specific, identifiable ways. The pattern of constraints forms a directed cycle:

**Reference constrains Structure.** What can be named constrains what can be composed. The lexicon -- the set of referentially grounded basic expressions -- is the input to the compositional machinery. If a concept cannot be named (if no sign can be attached to it), it cannot enter the compositional system and cannot participate in the construction of complex meanings. The five failure modes of reference (Section 2.1.3) propagate into the structural dimension: reference failure in the lexicon produces gaps in the compositional semantics (undefined base cases); namespace collision produces ambiguity; semantic drift produces compositionality violations (the meaning of the whole diverges from the meaning composed from the parts, because the parts have drifted). Frege's sense/reference distinction is itself a constraint of reference on structure: two names with the same reference but different senses produce different compositional results in intensional contexts.

**Structure constrains Computation.** The compositional requirements of a language's semantics constrain what computational mechanisms can implement it. The functorial passage from syntax to semantics must be computable, and the complexity of the computation is determined by the complexity of the syntactic and type-theoretic structures involved. A compositional semantics that requires operations beyond the computational power of the underlying automaton is unrealizable. The Chomsky hierarchy provides the precise calibration: a context-free compositional semantics can be processed by a pushdown automaton; a context-sensitive semantics requires a linear bounded automaton; a fully dependent-typed semantics requires the full power of a Turing machine. The structural dimension determines the computational dimension's requirements.

**Computation constrains Reflexivity.** The computational power of a system determines its capacity for self-description. A finite automaton cannot construct self-referential queries (it lacks the memory to encode its own states in a way that supports diagonalization). A pushdown automaton has limited self-referential capacity. A Turing machine has full self-referential capacity -- and this is precisely why it inherits the impossibility results. Godel's theorems apply to systems capable of encoding arithmetic (roughly, context-sensitive and above); weaker systems (Presburger arithmetic, finite automata) can achieve completeness and decidability because they lack the computational power to construct the diagonal sentences. The reflexive dimension's impossibility walls are calibrated to the computational dimension's power: more computational power yields more self-referential capacity yields more impossibility.

**Reflexivity constrains Reference.** The impossibility of complete semantic self-description limits what can be named about the system itself. Tarski's theorem establishes that a system cannot define a truth predicate for its own sentences -- which means that "the true sentences of this system" cannot be named within the system. Godel's theorem establishes that "the consistent sentences of this system" cannot be delimited from within. Rice's theorem establishes that no non-trivial semantic property of programs can be decided -- which means that names for semantic categories ("the terminating programs," "the correct implementations," "the secure modules") cannot be precisely extensionalized by the system itself. The reflexive dimension constrains the referential dimension by establishing that certain self-referential naming acts are impossible: the system cannot name its own truth, its own consistency, or its own semantic properties.

### 3.3 The Cyclic Dependency: A Strange Loop of Meaning

The four constraints form a directed cycle:

Reference --> Structure --> Computation --> Reflexivity --> Reference

This cyclic dependency invites two interpretations. On the *vicious circle* reading, the cycle is a defect -- a bootstrapping problem in which none of the dimensions can be established without the others, and therefore none can be established at all. On the *generative spiral* reading, the cycle is productive -- a self-reinforcing structure in which each dimension enables and constrains the next, producing an ascending spiral of increasingly articulated meaning.

The present dissertation argues for the generative-spiral interpretation. The argument draws on three sources.

First, the *hermeneutic circle* in the tradition of Schleiermacher, Heidegger, and Gadamer provides a philosophical precedent for productive circularity in the domain of meaning. Gadamer's hermeneutics holds that understanding is not a linear process from parts to whole or from whole to parts, but a circular movement in which one's understanding of the parts is informed by one's understanding of the whole, and vice versa. The circle is not vicious because it is not a logical deduction but a temporal process: understanding deepens with each iteration. Similarly, the cyclic dependency among the four dimensions of meaning is not a logical circularity but a structural description of how meaning is constituted through the interplay of its dimensions. Reference enables composition, which enables computation, which enables (and constrains) self-reference, which constrains what can be referred to -- and the next iteration operates on a richer basis than the first.

Second, Hofstadter's concept of the *strange loop* provides a formal metaphor for the cycle. A strange loop is a cyclic structure that traverses levels of a hierarchy such that, by moving only upwards or downwards, one returns to one's starting point. The four dimensions of meaning form a hierarchy -- Reference is the ground, Structure is built upon it, Computation realizes it, Reflexivity bounds it -- but the reflexive dimension's constraints on reference close the loop, returning to the ground level. This is precisely the structure of a strange loop. And Hofstadter's insight, developed in *Godel, Escher, Bach* and *I Am a Strange Loop*, is that strange loops are not pathological but generative: they are the mechanism by which self-referential systems produce emergent properties (consciousness, in Hofstadter's case; meaning, in ours).

Third, the *bootstrapping pattern* identified by RP-02 provides a constructive model for how the cycle operates. Bootstrapping resolves apparent circularity through temporal staging: a compiler at stage N is compiled by the compiler at stage N-1. Similarly, the meaning system at stage N operates with a referential vocabulary, compositional apparatus, computational implementation, and reflexive self-knowledge that were established at stage N-1. Each stage inherits the resources of the previous stage and extends them. The cycle is not traversed instantaneously (which would produce paradox) but iteratively (which produces progressive elaboration). This is why the impossibility results do not prevent the system from working: they prevent *instantaneous* complete self-description, but they do not prevent *staged* partial self-description that improves with each iteration.

The cyclic dependency is thus not a defect of the four-dimensional architecture but one of its most significant features. It explains why meaning is neither foundationally grounded (there is no first dimension from which the others can be derived) nor circularly defective (the cycle is productive rather than vicious). Meaning is a strange loop -- a self-reinforcing structure that generates its own conditions of possibility through iterative elaboration.

### 3.4 Comparison with Existing Architectures of Meaning

The four-dimensional architecture proposed here should be situated relative to the existing frameworks that have attempted to characterize the structure of meaning.

#### 3.4.1 Frege's Two-Level Semantics

Frege's sense/reference distinction partitions meaning into two levels: the sense (Sinn) -- the mode of presentation, the cognitive route to the referent -- and the reference (Bedeutung) -- the object denoted. This two-level architecture has been enormously influential, but it captures only a fragment of what the four-dimensional account describes. Frege's distinction operates entirely within the referential dimension: both sense and reference concern how a sign attaches to a thing (directly, by pointing to the object; or indirectly, by presenting the object under a particular aspect). The structural dimension (compositionality) appears in Frege's work as a principle but not as a dimension of the semantic architecture itself. The computational and reflexive dimensions are absent. Frege's two-level semantics is a theory of the internal structure of the referential dimension, not a theory of meaning as a whole.

#### 3.4.2 Morris's Three Dimensions: Syntax, Semantics, Pragmatics

Charles Morris (1938) proposed a tripartite division of semiotics into syntax (the formal relations among signs), semantics (the relations between signs and the objects they denote), and pragmatics (the relations between signs and their interpreters). This trichotomy has become the standard classification in linguistics and has been adopted by the philosophy of language.

Morris's three dimensions map partially onto the four-dimensional architecture. His syntax corresponds to aspects of both the structural and computational dimensions (formal relations among signs are constituted by compositional rules and realized by computational processes). His semantics corresponds to the referential dimension (the sign-object relation). His pragmatics has no direct counterpart in the four-dimensional architecture, a point discussed at length in Section 4.1. Morris's classification omits the reflexive dimension entirely: it provides no account of what happens when the semiotic system describes itself.

The four-dimensional architecture is therefore not a refinement of Morris's trichotomy but a reorientation. Morris classifies the *relations* in which signs participate (formal, denotational, interpretive). The four-dimensional architecture classifies the *aspects* of meaning that any adequate theory must address (attachment, composition, realization, self-limitation). The two classifications cross-cut rather than nest.

#### 3.4.3 The Ogden-Richards Triangle

Ogden and Richards (1923) proposed the "semiotic triangle" relating three elements: the *symbol* (the sign), the *thought or reference* (the mental concept), and the *referent* (the object in the world). The triangle asserts that the relation between symbol and referent is not direct but mediated by thought: the symbol evokes a thought, and the thought refers to the referent. The base of the triangle (symbol-referent) is indicated by a dashed line, signifying that the direct relation is merely "imputed" rather than real.

The semiotic triangle captures the internal structure of the referential dimension from a psychological perspective: it introduces the mind (the "thought or reference") as a mediating element in the sign-thing relation. But it has nothing to say about composition, computation, or reflexivity. Like Frege's two-level semantics, it is a theory of the referential dimension's internal structure, not a theory of meaning's overall architecture.

#### 3.4.4 Why Four Dimensions Are Necessary

None of the existing frameworks captures all four aspects of meaning. Frege and Ogden-Richards address reference. Morris addresses reference, partial structure, and pragmatics. None addresses computation in the precise, hierarchy-stratified sense of RP-06, and none addresses reflexivity in the impossibility-theoretic sense of RP-02. The four-dimensional architecture is necessary because the phenomena it describes -- the computational niche of natural language, the impossibility of semantic self-description, the five failure modes of naming, the functorial character of composition -- are real, formally established, and not captured by any existing framework.

The four dimensions are also sufficient for a *formal* account of meaning, in the following sense: every formally characterizable aspect of meaning falls within one of the four dimensions. The attachment of signs to things (reference), the combination of meanings into larger meanings (structure), the processing of meanings by computational mechanisms (computation), and the self-referential limits of meaning-systems (reflexivity) exhaust the space of formal possibilities. What the architecture cannot capture -- pragmatics, embodiment, phenomenal consciousness -- falls outside the formal domain, as argued in Section 4.

---

## 4. The Limits of the Architecture

The four-dimensional architecture claims to be necessary and sufficient for a formal account of meaning. This section examines what the architecture cannot capture and whether these lacunae constitute genuine limitations or merely mark the boundary between formal and non-formal aspects of meaning.

### 4.1 What the Architecture Cannot Capture: Pragmatics

The most conspicuous absence from the four-dimensional architecture is pragmatics -- the aspects of meaning that depend on the context of use rather than the form or structure of an expression. Indexicals ("I," "here," "now"), conversational implicature (Grice's maxims), presupposition, speech acts (Austin's performatives, Searle's illocutionary force), and discourse dynamics all contribute to the meaning of an utterance in ways that the four dimensions do not directly capture.

The referential dimension concerns how signs attach to things, not how the context of utterance determines which thing a sign attaches to on a particular occasion. The structural dimension concerns how meanings compose, not how contextual information modulates the composition. The computational dimension concerns what resources are required to process compositional meaning, not how contextual inference is computationally realized. The reflexive dimension concerns the limits of self-description, not the pragmatic norms that govern communicative interaction.

Does this omission vitiate the architecture? The answer depends on one's view of the relationship between semantics and pragmatics. On the *semantic minimalism* of Borg (2004) and Cappelen and Lepore (2005), the literal meaning of an expression -- its contribution to truth conditions -- is determined by its form and the conventional meanings of its parts, independently of context. On this view, pragmatics is not part of meaning proper but is a distinct cognitive process that operates on the output of the semantic system. The four-dimensional architecture captures semantic meaning; pragmatics falls outside it.

On the *contextualist* view of Travis (1997), Recanati (2004), and others, nearly all meaning is context-dependent: the contribution of an expression to truth conditions cannot be determined without reference to the context of utterance. On this view, the four-dimensional architecture captures only a skeletal notion of meaning, and the full phenomenon requires a fifth dimension -- the contextual or pragmatic dimension.

The present dissertation does not adjudicate this debate but notes that the four-dimensional architecture is *consistent* with either view. On the minimalist view, the architecture is complete for semantic meaning, and pragmatics is a distinct phenomenon. On the contextualist view, the architecture captures the formal core of meaning, and a fifth dimension (pragmatics) would be needed for a complete account. The architecture's self-described scope -- the formal architecture of meaning -- is preserved on either view.

It should be noted that certain formal frameworks have attempted to bring pragmatic phenomena within the scope of compositional analysis. Dynamic semantics treats meaning as context-change potential, effectively incorporating some pragmatic phenomena (anaphora resolution, presupposition accommodation) into the compositional machinery. Game-theoretic pragmatics (Lewis, Frank and Goodman) models speaker-hearer interaction as a game, providing a formal framework for implicature. These approaches suggest that the boundary between semantics and pragmatics is not fixed but can be progressively shifted by enriching the compositional and computational resources of the system. The four-dimensional architecture accommodates this shift: as pragmatic phenomena are formalized, they are absorbed into the structural and computational dimensions.

### 4.2 The Hard Problem of Meaning: Phenomenal Consciousness and Intentionality

A deeper limitation concerns the relationship between formal meaning and phenomenal consciousness. Husserl's phenomenology, founded on the concept of *intentionality* -- the directedness of mental acts toward objects -- holds that meaning is constituted not merely by formal structure but by the lived experience of a conscious subject. Every conscious act is *about* something: perception is perception *of* an object; belief is belief *that* something is the case; desire is desire *for* something. This "aboutness" -- intentionality -- is, for Husserl and the phenomenological tradition, the ground of all meaning.

The four-dimensional architecture has no account of intentionality in this phenomenological sense. The referential dimension describes how signs attach to things, but it does not explain how a *conscious subject* experiences the sign as meaning something. The structural dimension describes how meanings compose, but it does not explain how a subject *understands* a compositional meaning as a unified thought rather than a sequence of formal operations. The computational dimension describes how meaning is processed, but processing is not the same as understanding. The reflexive dimension describes where self-description fails, but it does not address the "hard problem" of consciousness -- why there is *something it is like* to mean.

This limitation is real and, on many philosophical views, insuperable for any formal theory. The "explanatory gap" between computational processing and phenomenal experience -- identified by Levine (1983) and given its sharpest formulation by Chalmers (1996) as the "hard problem of consciousness" -- applies with full force to the phenomenon of meaning. A system that processes language according to the compositional, type-theoretic, computationally realized, reflexively bounded architecture described in this paper may do everything that the architecture prescribes -- and yet there may be no fact of the matter about whether the system *means* anything, in the phenomenological sense, at all.

The present dissertation accepts this limitation. The four-dimensional architecture is a theory of meaning's formal shape, not a theory of meaning's experiential ground. It describes the structure within which meaning operates but does not explain why that structure gives rise to (or is accompanied by) conscious understanding. Whether this limitation is a temporary gap that future theoretical work might close, or a permanent boundary between the formal and the phenomenal, is an open question in philosophy of mind that the present work does not presume to settle.

### 4.3 The Distributional Challenge: Can Vector-Space Meaning Be Architectured?

Modern neural language models (transformers, large language models) represent meaning in a way that does not obviously fit the four-dimensional architecture. In these models, the meaning of a word is a vector in a high-dimensional space, derived from patterns of co-occurrence in large corpora. Sentence meanings are computed by attention-weighted combinations of word vectors. There are no explicit types, no explicit compositional rules, no explicit referential attachments. Yet these models produce outputs that, by many behavioral measures, exhibit sophisticated understanding.

Does the distributional/neural approach to meaning constitute a fifth dimension, or does it fall within the existing four?

The DisCoCat framework (Coecke, Sadrzadeh, and Clark, 2010), discussed at length in RP-06 and SYN-01, suggests that distributional meaning can be brought within the structural dimension. DisCoCat uses category theory to bridge the gap between compositional and distributional semantics: grammatical structure (represented by pregroup grammars) and vector-space semantics (represented by the category of finite-dimensional vector spaces) are both compact closed categories, and meaning assignment is a functor from the grammatical category to the vector-space category. Under this functor, sentence meaning is computed by tensor contraction determined by the grammatical structure, producing a vector that represents the sentence's meaning in a principled, compositional way.

The DisCoCat approach demonstrates that distributional meaning is not a separate dimension but a particular *instantiation* of the structural dimension -- one in which the semantic category is the category of vector spaces rather than the category of sets (as in model-theoretic semantics) or the category of domains (as in denotational semantics). The four-dimensional architecture accommodates distributional meaning by noting that the functorial passage from syntax to semantics can target different semantic categories, and vector spaces are one legitimate choice.

The question of whether transformer-based models implicitly learn the four-dimensional architecture remains open. Probing studies (Hewitt and Manning, 2019; Clark et al., 2019) demonstrate that transformers encode syntactic structure and track agreement phenomena, suggesting implicit competence at the context-free and context-sensitive levels. Whether they learn type-theoretic structure in the precise sense of categorial grammar has not been established. The present architecture predicts that any system that processes meaning -- whether explicitly designed or learned from data -- must instantiate some version of the four dimensions, though the instantiation may be implicit, approximate, or partial.

### 4.4 The Hermeneutic Dimension: Understanding as Fusion of Horizons

Gadamer's philosophical hermeneutics, developed in *Truth and Method* (1960), proposes that understanding is not the recovery of an author's original intention but a *fusion of horizons* (Horizontverschmelzung) -- the merging of the interpreter's horizon of understanding with the horizon of the text being interpreted. Every act of understanding is historically situated: the interpreter brings a *fore-understanding* (Vorverstandnis) shaped by tradition, experience, and prejudice, and the text brings its own historical context and tradition. Understanding occurs when these two horizons overlap and merge, producing a new understanding that is neither the author's original meaning nor the interpreter's pre-existing beliefs but something new -- a "third thing" that transcends both.

Ricoeur extended Gadamer's hermeneutics to include a structural moment: the interpretation of a text involves not only the fusion of horizons but also the *explanation* of the text's internal structure -- its syntax, its semantics, its compositional organization. Ricoeur's "hermeneutic arc" moves from a naive initial understanding, through structural analysis, to a deeper, reflective understanding that integrates structural insight with lived experience.

The hermeneutic tradition points to an aspect of meaning that the four-dimensional architecture acknowledges but does not formalize: the historicity and situatedness of understanding. The four dimensions describe the *structural conditions* of meaning -- what must be in place for something to mean something -- but they do not describe the *temporal process* of understanding, in which an interpreter, situated in a particular historical and cultural moment, comes to grasp a meaning that is itself historically situated. The hermeneutic circle -- the iterative movement between part and whole, between fore-understanding and text -- is a description of understanding *in time*, and the four-dimensional architecture is a description of meaning *in structure*. These are complementary rather than competing accounts, but the architecture, by its formal nature, cannot capture the temporal, historical, and experiential character of understanding.

The hermeneutic circle does, however, have a structural echo in the architecture: the cyclic dependency among the four dimensions (Section 3.3) is a formal analogue of the hermeneutic circle. The iterative movement from reference to structure to computation to reflexivity and back is the architectural counterpart of the iterative movement from part to whole and back. Just as the hermeneutic circle deepens understanding with each iteration, the cyclic dependency among the four dimensions enriches meaning with each traversal. The analogy is suggestive but should not be pressed too far: the hermeneutic circle involves a conscious subject in historical time, while the architectural cycle involves formal structures in logical space. The two circles are cognate but not identical.

### 4.5 Is a Complete Architecture of Meaning Possible, or Does RP-02 Forbid It?

The deepest question raised by the reflexive dimension is whether the four-dimensional architecture, applied to itself, generates a version of the impossibility results it describes. If meaning has an architecture, and if the architecture is itself a meaningful description, then the architecture is a system of meaning describing the system of meaning -- precisely the kind of self-referential structure that RP-02 shows to be necessarily incomplete.

The answer is yes: the four-dimensional architecture is necessarily incomplete, and this incompleteness is a feature rather than a defect. The architecture describes the dimensions within which meaning operates, but it cannot decide all questions about its own adequacy from within. Whether the four dimensions are truly necessary and sufficient, whether the cyclic dependency is productive or vicious, whether the architecture captures "meaning" in the fullest sense -- these are semantic questions about the architecture's own behavior, and by the reflexive dimension's own findings (Rice's theorem, Godel's incompleteness), they cannot be fully answered by the architecture itself. The architecture's self-description is necessarily partial, just as any sufficiently expressive system's self-description is necessarily partial.

This is not a defect but a consistency check. An architecture of meaning that claimed to be complete -- to fully characterize its own adequacy from within -- would violate the very impossibility results it incorporates. The four-dimensional architecture's self-acknowledged incompleteness is evidence of its correctness: it practices what it preaches about the limits of self-description.

The incompleteness does not, however, render the architecture useless. RP-02's seven design principles for self-governing systems apply: the architecture should stage its self-reference temporally (evaluating previous versions of itself rather than the current version), separate its syntactic from its semantic self-description (it can enumerate its own dimensions and formal properties, but it cannot fully evaluate its own adequacy), and submit to external verification (the philosophical community, the IRA panel, the reader of this dissertation) for the semantic assessments that it cannot make about itself.

---

## 5. Implications

### 5.1 For Philosophy of Language: The Architecture as Research Program

The four-dimensional architecture proposes a reorganization of the philosophy of language. Rather than treating the major debates -- referentialism versus descriptivism, compositionalism versus holism, formalism versus use-theory, realism versus anti-realism -- as competing answers to a single question ("what is meaning?"), the architecture treats them as contributions to different dimensions of a single, multi-faceted phenomenon.

The referentialism/descriptivism debate (Kripke versus Frege-Russell) concerns the internal structure of the *referential dimension*: is the attachment of sign to thing mediated by descriptive content (Frege, Russell) or secured by causal history (Kripke)? The architecture does not adjudicate this debate but identifies it as a debate about the mechanism of reference, not about the relationship between reference and the other dimensions.

The compositionalism/holism debate (Frege's principle versus Quine-Davidson holism) concerns the *structural dimension*: is meaning constituted by the composition of parts, or does the meaning of each part depend on its role in the whole? Semantic holism -- the view that a term's meaning depends on its relations to all other terms in the language -- challenges the principle of compositionality by suggesting that the meaning of a part cannot be determined independently of the whole. The architectural response is that compositionality and holism operate at different levels: compositionality describes the *structural mechanism* by which complex meanings are built from simpler ones, while holism describes the *epistemic condition* that the simpler meanings themselves are determined by their position in a network. These are compatible: a compositional semantics can operate on a holistically determined lexicon.

The formalism/use-theory debate (Montague versus Wittgenstein) concerns the relationship between the *structural* and *pragmatic* aspects of meaning. Formalists hold that meaning is constituted by formal structure; use-theorists hold that meaning is constituted by patterns of use. The architecture suggests that formal structure (the structural dimension) and use (the pragmatic context, which falls at the architecture's boundary) are complementary: formal structure provides the skeleton, and use provides the flesh. Neither alone constitutes meaning in the fullest sense.

The architecture thus reframes the philosophy of language as a research program in which different philosophical traditions contribute to different dimensions. Frege, Russell, and Kripke contribute to the referential dimension. Montague, Lambek, and Steedman contribute to the structural dimension. Chomsky, Church, and the type theorists contribute to the computational dimension. Godel, Tarski, and Turing contribute to the reflexive dimension. Wittgenstein, Austin, Grice, Gadamer, and Brandom contribute to the pragmatic boundary. The architecture provides a map of the territory, showing where each contribution fits and where the gaps remain.

### 5.2 For AI: Designing Systems That Instantiate All Four Dimensions

The four-dimensional architecture has direct implications for the design of artificial intelligence systems that aspire to process, generate, or understand meaning. Current AI systems -- particularly large language models based on the transformer architecture -- are strongest in the computational dimension (they process vast quantities of text with impressive efficiency) and weakest in the reflexive dimension (they have no principled self-knowledge of their own limitations).

A system that instantiated all four dimensions would need:

**A referential grounding mechanism.** Current language models operate on distributional representations that are not grounded in reference relations to the world. They associate words with vectors derived from co-occurrence patterns, but these vectors do not constitute reference in the Fregean or Kripkean sense. A four-dimensionally adequate system would need a mechanism for attaching signs to things -- a lexicon grounded in perception, ostension, or stipulated reference rather than in statistical co-occurrence alone. Recent work on vision-language models and embodied AI moves in this direction.

**A compositional architecture.** Current transformer models compute representations holistically: the meaning of a sentence emerges from the global interaction of all tokens through self-attention, not from a bottom-up compositional process. The DisCoCat framework and CCG-based semantic parsing provide compositional alternatives, but they have not yet been scaled to the coverage and fluency of transformer models. A four-dimensionally adequate system would combine the broad coverage of neural models with the compositional transparency of type-theoretic approaches.

**A computational self-awareness of complexity.** Current systems have no explicit representation of their own computational complexity. They do not know whether a given inference is context-free (tractable) or context-sensitive (potentially intractable). A four-dimensionally adequate system would maintain an explicit model of its own computational resources and the complexity of the tasks it undertakes, adjusting its processing strategies accordingly.

**A reflexive capacity with acknowledged incompleteness.** Current systems have no principled account of their own limitations. They cannot distinguish questions they can answer reliably from questions they cannot, and they have no mechanism for flagging their own uncertainty as a structural feature (arising from the impossibility landscape) rather than a contingent deficiency (arising from insufficient training data). A four-dimensionally adequate system would incorporate the seven design principles of RP-02: staging self-reference temporally, separating syntactic from semantic self-knowledge, employing external verification for semantic properties, and making its own incompleteness visible rather than hidden.

### 5.3 For ORGANVM: The System as a Four-Dimensional Meaning-Machine

The ORGANVM system -- the multi-organ governance architecture within which this research programme is conducted -- can be interpreted as a concrete instantiation of the four-dimensional architecture. The system's components map onto the four dimensions in a way that is both illuminating and prescriptive.

**The referential dimension: seed.yaml contracts.** Every repository in the ORGANVM system is required to contain a seed.yaml file -- a declarative contract specifying the repository's organ membership, tier, implementation status, produced and consumed event types, and dependency relationships. The seed.yaml is the system's lexicon: it establishes the referential attachments between names (repository identifiers, organ labels, event type names) and things (the actual repositories, their functions, their interfaces). The five failure modes of naming identified by RP-04 apply directly: reference failures (a seed.yaml that declares a dependency on a nonexistent repository), collisions (two repositories claiming the same event type), semantic drift (a seed.yaml whose declarations no longer match the repository's actual behavior), abstraction mismatch (different representations of the same entity across the registry and individual seed files), and governance failure (absence of a mechanism to enforce naming consistency).

**The structural dimension: registry operations.** The registry-v2.json file and the operations performed upon it -- promotion, dependency validation, cross-reference checking -- constitute the system's compositional semantics. The registry is the semantic algebra: its objects are repository records, and its operations (promotion transitions, dependency-graph transformations, cross-organ event routing) are structure-preserving maps that combine individual repository meanings into a system-level meaning. The compositionality of the registry -- the principle that the system's overall state is determined by the states of its components according to the registry's rules -- is the system-level instantiation of the functorial principle.

**The computational dimension: CI/CD pipelines.** The continuous integration and continuous deployment infrastructure realizes the system's computational dimension. Automated checks (linters, schema validators, dependency analyzers, test suites) implement the tractable, syntactic governance operations that lie on the decidable side of the Rice boundary. The computational resources allocated to these checks -- their complexity, their running time, their coverage -- are calibrated to the level of the Chomsky hierarchy appropriate to each check: naming convention validation is regular (finite-state pattern matching); schema validation is context-free (tree-structured parsing); type checking and dependency analysis are context-sensitive (requiring information about the surrounding code context).

**The reflexive dimension: the IRA panel.** The Independent Review Authority -- the human evaluative body that assesses repositories for promotion to PUBLIC_PROCESS and GRADUATED status -- instantiates the reflexive dimension. The IRA panel provides the external verification that Godel's and Tarski's theorems establish as structurally necessary. It evaluates semantic properties (fitness for purpose, architectural coherence, ethical alignment) that the automated system cannot decide about itself. The panel's judgments are not algorithmic; they are exercises in human understanding -- the kind of cognitive work that falls outside the scope of what any formal system can decide about its own behavior. The hierarchy -- automated checks, then IRA review, then human judgment -- is open at the top, terminating in human cognition rather than in another formal system, thereby avoiding the infinite regress that would result from requiring each governance level to be governed by a higher formal level.

The ORGANVM system thus provides a case study in four-dimensional meaning-architecture: a concrete system in which the referential, structural, computational, and reflexive dimensions are not merely theoretical abstractions but operational components with specific implementations, specific failure modes, and specific design constraints derived from the formal results of the four prior investigations.

---

## 6. Discussion

### 6.1 The Grand Arc: From Naming to Limits

The SYN-05 prospectus in the Research Program Prospectus identified a grand arc traversing the four foundational investigations: knowledge begins with naming (RP-04), naming acquires structure through grammar and type systems (RP-06), structured names receive formal semantics (RP-01), and formal semantics encounters the impossibility results that constrain all self-describing systems (RP-02). The four-dimensional architecture developed in this dissertation is the formal expression of this arc.

The arc is not merely a research trajectory -- a sequence of topics investigated in a convenient order. It is, the present work argues, a fundamental dynamic of meaning itself. Every system that means -- every language, every formal system, every institution that codifies norms and automates processes -- traverses this same path:

1. It begins by *naming* -- attaching signs to things, establishing a lexicon, creating the referential infrastructure that makes all subsequent meaning possible.
2. It proceeds to *structuring* -- organizing names into systems, defining compositional rules, creating the syntactic and type-theoretic apparatus that enables complex meaning to be built from simple parts.
3. It then *realizes* -- implementing the compositional rules in computational mechanisms, building parsers and type-checkers and validators, creating the processing infrastructure that makes meaning operationally effective.
4. It finally *encounters its own limits* -- discovering that its self-referential capacity, while real and productive, is necessarily incomplete; that its semantic self-description is bounded by the impossibility landscape; that certain questions about its own meaning, correctness, and adequacy cannot be answered from within.

This grand arc is, in a precise sense, the *life cycle of formalization*. It is the path that every formalization of knowledge must traverse, from the informal act of naming to the formal architecture of composition and computation to the discovery that formalization cannot close itself -- that there is always a remainder, a residual opacity, a question that the system cannot answer about itself.

### 6.2 Relationship to the Broader Research Programme

The four-dimensional architecture of meaning connects to the other investigations in the SGO research programme through specific structural bridges.

SYN-01, *The Architecture of Formal Meaning*, is the structural core of the present work. SYN-01's claim that meaning is the functorial passage from syntax to semantics is incorporated here as the characterization of the structural dimension. The present work extends SYN-01 by situating the functorial claim within a larger architecture that includes reference, computation, and reflexivity -- dimensions that SYN-01 acknowledges but does not develop.

SYN-02, *The Governance Impossibility Thesis*, draws implications from RP-02 and RP-03 for the design of governance systems. The present work connects to SYN-02 through the reflexive dimension: the impossibility results that constrain self-governing systems are the same results that constrain self-describing meaning-systems.

The broader ORGANVM system, with its eight-organ model and its aspiration to enable one person to enact ideas at enterprise level, is itself an exercise in the formalization of knowledge -- and therefore traverses the grand arc described above. The system's evolution from informal naming conventions to formalized registry operations to automated CI/CD checks to IRA panel review traces the same path from naming to limits that the four-dimensional architecture describes.

### 6.3 Open Questions

Several questions remain open after the present analysis.

First, the *type-theoretic characterization of the mildly context-sensitive level* remains an unsolved problem. RP-06 identified this as the critical gap in the fourfold correspondence: the grammar-automaton correspondence for MCS languages is well-established, but the type system that corresponds to MCS grammars has not been identified. Closing this gap would complete the computational dimension's account of natural language's computational niche and would have implications for the structural dimension's characterization of natural language compositionality.

Second, the *relationship between the four-dimensional architecture and phenomenal consciousness* remains unresolved. The architecture describes the formal structure of meaning but does not explain how (or whether) this structure gives rise to conscious understanding. The "hard problem" of meaning -- why there is something it is like to mean -- is the phenomenological version of the hard problem of consciousness, and it resists formal treatment for the same reasons.

Third, the *pragmatic boundary* -- the line between what the architecture captures and what it does not -- requires further investigation. The progressive formalization of pragmatic phenomena through dynamic semantics, game-theoretic pragmatics, and type-theoretic models of dialogue suggests that the boundary is not fixed but can be shifted by enriching the formal apparatus. Whether this progressive formalization will eventually absorb all of pragmatics into the four dimensions, or whether an irreducible pragmatic remainder will always persist, is an empirical question that depends on the success of future formal work.

Fourth, the *cyclic dependency* among the four dimensions merits formal development. The present work characterizes the cycle informally as a "strange loop" and draws analogies with the hermeneutic circle and the bootstrapping pattern. A formal treatment -- perhaps using the apparatus of fixed-point theory on categories, or the theory of circular definitions in non-well-founded set theory -- would provide a more rigorous account of the cycle's productivity and would establish whether the cycle has a fixed point (a stable architecture of meaning that is its own best description) or an infinite ascent (an ever-deepening sequence of approximations).

---

## 7. Conclusion

This dissertation has argued that meaning is not a single phenomenon but a four-dimensional architecture, whose dimensions are Reference (how meaning attaches), Structure (how meaning composes), Computation (how meaning is realized), and Reflexivity (where meaning encounters its own limits). These four dimensions were identified by four prior investigations in the SGO research programme: RP-04 established the referential dimension through its analysis of naming as compression; RP-01 and SYN-01 established the structural dimension through their analysis of compositionality as functoriality; RP-06 established the computational dimension through its fourfold grammar-automaton-type-proof correspondence; and RP-02 established the reflexive dimension through its mapping of the impossibility landscape.

The central architectural claim is that these four dimensions are orthogonal (no dimension can be reduced to another), interacting (each constrains the others in identifiable ways), and cyclically dependent (they form a directed cycle: Reference constrains Structure constrains Computation constrains Reflexivity constrains Reference). This cycle is not vicious but generative -- a strange loop in Hofstadter's sense, a hermeneutic circle in Gadamer's sense, a bootstrapping process in RP-02's sense -- that produces meaning through iterative elaboration rather than foundational derivation.

The architecture was compared with existing frameworks -- Frege's two-level semantics, Morris's tripartite semiotics, the Ogden-Richards triangle -- and found to subsume what each captures while adding dimensions that none addresses. The architecture's limits were examined: pragmatics, phenomenal consciousness, embodiment, the hermeneutic temporal process, and the distributional challenge all fall at or beyond the architecture's boundary, and the reflexive dimension's own impossibility results guarantee that the architecture's self-description is necessarily incomplete.

The implications were drawn for philosophy of language (the architecture reframes major debates as contributions to different dimensions), for AI (a four-dimensionally adequate system would need referential grounding, compositional transparency, computational self-awareness, and reflexive self-limitation), and for ORGANVM (whose seed.yaml contracts, registry operations, CI/CD pipelines, and IRA panel instantiate the four dimensions in a concrete governance system).

The architecture of meaning is not a theory *of* meaning but a theory of meaning's *shape*. It does not tell us what meaning is -- that question, as RP-02 would remind us, cannot be fully answered by any formal system from within. What it tells us is the space within which meaning operates: a four-dimensional space whose dimensions are reference, structure, computation, and reflexivity, bound together by a cyclic dependency that is simultaneously the source of meaning's generative power and the origin of its necessary incompleteness. The architecture does not resolve the question of meaning. It maps the terrain within which the question must be pursued -- the terrain from naming, through formalization, to the limits of self-description, and back.

---

## References

### Primary Philosophical Texts

Austin, J.L. (1962). *How to Do Things with Words*. Oxford: Clarendon Press.

Brentano, F. (1874). *Psychologie vom empirischen Standpunkt*. Leipzig: Duncker and Humblot. [Trans. as *Psychology from an Empirical Standpoint*, 1995.]

Brandom, R. (1994). *Making It Explicit*. Cambridge, MA: Harvard University Press.

Brandom, R. (2000). *Articulating Reasons*. Cambridge, MA: Harvard University Press.

Chalmers, D.J. (1996). *The Conscious Mind*. Oxford: Oxford University Press.

Davidson, D. (1967). "Truth and Meaning." *Synthese*, 17(1), 304-323.

Dummett, M. (1991). *The Logical Basis of Metaphysics*. Cambridge, MA: Harvard University Press.

Frege, G. (1879). *Begriffsschrift*. Halle: Louis Nebert.

Frege, G. (1892). "Uber Sinn und Bedeutung." *Zeitschrift fur Philosophie und philosophische Kritik*, 100, 25-50.

Gadamer, H.-G. (1960). *Wahrheit und Methode*. Tubingen: J.C.B. Mohr. [Trans. as *Truth and Method*, 1975.]

Grice, H.P. (1975). "Logic and Conversation." In P. Cole and J.L. Morgan (eds.), *Syntax and Semantics, Vol. 3: Speech Acts*. New York: Academic Press, 41-58.

Husserl, E. (1900-1901). *Logische Untersuchungen*. Halle: Max Niemeyer. [Trans. as *Logical Investigations*, 1970.]

Kripke, S. (1980). *Naming and Necessity*. Cambridge, MA: Harvard University Press.

Levine, J. (1983). "Materialism and Qualia: The Explanatory Gap." *Pacific Philosophical Quarterly*, 64(4), 354-361.

Mill, J.S. (1843). *A System of Logic*. London: John W. Parker.

Morris, C.W. (1938). "Foundations of the Theory of Signs." In *International Encyclopedia of Unified Science*, Vol. 1. Chicago: University of Chicago Press.

Ogden, C.K. and Richards, I.A. (1923). *The Meaning of Meaning*. London: Kegan Paul.

Peirce, C.S. (1931-1958). *Collected Papers of Charles Sanders Peirce*. C. Hartshorne, P. Weiss, and A.W. Burks (eds.). Cambridge, MA: Harvard University Press.

Putnam, H. (1975). "The Meaning of 'Meaning'." In *Mind, Language and Reality: Philosophical Papers, Vol. 2*. Cambridge: Cambridge University Press, 215-271.

Quine, W.V.O. (1948). "On What There Is." *Review of Metaphysics*, 2(5), 21-38.

Quine, W.V.O. (1960). *Word and Object*. Cambridge, MA: MIT Press.

Ricoeur, P. (1976). *Interpretation Theory: Discourse and the Surplus of Meaning*. Fort Worth: Texas Christian University Press.

Russell, B. (1905). "On Denoting." *Mind*, 14(56), 479-493.

Saussure, F. de (1916). *Cours de linguistique generale*. C. Bally and A. Sechehaye (eds.). Paris: Payot.

Searle, J. (1958). "Proper Names." *Mind*, 67(266), 166-173.

Searle, J. (1969). *Speech Acts*. Cambridge: Cambridge University Press.

Wittgenstein, L. (1953). *Philosophical Investigations*. G.E.M. Anscombe (trans.). Oxford: Blackwell.

### Logic, Computability, and Formal Foundations

Cantor, G. (1891). "Ueber eine elementare Frage der Mannigfaltigkeitslehre." *Jahresbericht der Deutschen Mathematiker-Vereinigung*, 1, 75-78.

Church, A. (1940). "A Formulation of the Simple Theory of Types." *Journal of Symbolic Logic*, 5(2), 56-68.

Coquand, T. and Huet, G. (1988). "The Calculus of Constructions." *Information and Computation*, 76(2-3), 95-120.

Curry, H.B. (1934). "Functionality in Combinatory Logic." *Proceedings of the National Academy of Sciences*, 20(11), 584-590.

Godel, K. (1931). "Uber formal unentscheidbare Satze der Principia Mathematica und verwandter Systeme I." *Monatshefte fur Mathematik und Physik*, 38, 173-198.

Howard, W.A. (1980). "The Formulae-as-Types Notion of Construction." In J.P. Seldin and J.R. Hindley (eds.), *To H.B. Curry: Essays on Combinatory Logic, Lambda Calculus and Formalism*. London: Academic Press, 479-490. [Originally circulated 1969.]

Kleene, S.C. (1938). "On Notation for Ordinal Numbers." *Journal of Symbolic Logic*, 3(4), 150-155.

Lob, M.H. (1955). "Solution of a Problem of Leon Henkin." *Journal of Symbolic Logic*, 20(2), 115-118.

Martin-Lof, P. (1984). *Intuitionistic Type Theory*. Naples: Bibliopolis.

Rice, H.G. (1953). "Classes of Recursively Enumerable Sets and Their Decision Problems." *Transactions of the American Mathematical Society*, 74(2), 358-366.

Tarski, A. (1936). "Der Wahrheitsbegriff in den formalisierten Sprachen." *Studia Philosophica*, 1, 261-405.

Turing, A.M. (1936). "On Computable Numbers, with an Application to the Entscheidungsproblem." *Proceedings of the London Mathematical Society*, 42, 230-265.

### Formal Semantics, Grammar, and Type Theory

Ajdukiewicz, K. (1935). "Die syntaktische Konnexitat." *Studia Philosophica*, 1, 1-27.

Bar-Hillel, Y. (1953). "A Quasi-Arithmetical Notation for Syntactic Description." *Language*, 29(1), 47-58.

Chomsky, N. (1956). "Three Models for the Description of Language." *IRE Transactions on Information Theory*, 2(3), 113-124.

Chomsky, N. (1957). *Syntactic Structures*. The Hague: Mouton.

Chomsky, N. (1995). *The Minimalist Program*. Cambridge, MA: MIT Press.

Coecke, B., Sadrzadeh, M., and Clark, S. (2010). "Mathematical Foundations for a Compositional Distributional Model of Meaning." *Linguistic Analysis*, 36(1-4), 345-384.

Girard, J.-Y. (1972). *Interpretation fonctionnelle et elimination des coupures de l'arithmetique d'ordre superieur*. PhD thesis, Universite Paris VII.

Heim, I. (1982). *The Semantics of Definite and Indefinite Noun Phrases*. PhD thesis, University of Massachusetts, Amherst.

Hoare, C.A.R. (1969). "An Axiomatic Basis for Computer Programming." *Communications of the ACM*, 12(10), 576-580, 583.

Joshi, A.K. (1985). "Tree Adjoining Grammars: How Much Context-Sensitivity Is Required to Provide Reasonable Structural Descriptions?" In D. Dowty, L. Karttunen, and A. Zwicky (eds.), *Natural Language Parsing*. Cambridge: Cambridge University Press, 206-250.

Kamp, H. (1981). "A Theory of Truth and Semantic Representation." In J. Groenendijk, T. Janssen, and M. Stokhof (eds.), *Formal Methods in the Study of Language*. Amsterdam: Mathematical Centre Tracts, 277-322.

Lambek, J. (1958). "The Mathematics of Sentence Structure." *American Mathematical Monthly*, 65(3), 154-170.

Montague, R. (1973). "The Proper Treatment of Quantification in Ordinary English." In J. Hintikka, J. Moravcsik, and P. Suppes (eds.), *Approaches to Natural Language*. Dordrecht: Reidel, 221-242.

Plotkin, G.D. (1981). "A Structural Approach to Operational Semantics." Technical Report DAIMI FN-19, Aarhus University.

Reynolds, J.C. (1974). "Towards a Theory of Type Structure." In *Colloque sur la Programmation*. Paris: Springer LNCS 19, 408-425.

Scott, D.S. and Strachey, C. (1971). "Toward a Mathematical Semantics for Computer Languages." In *Proceedings of the Symposium on Computers and Automata*. Brooklyn: Polytechnic Institute of Brooklyn, 19-46.

Shieber, S. (1985). "Evidence Against the Context-Freeness of Natural Language." *Linguistics and Philosophy*, 8(3), 333-343.

Steedman, M. (2000). *The Syntactic Process*. Cambridge, MA: MIT Press.

### Category Theory and Categorical Semantics

Abramsky, S. and Coecke, B. (2004). "A Categorical Semantics of Quantum Protocols." In *Proceedings of the 19th IEEE Symposium on Logic in Computer Science*. IEEE, 415-425.

Eilenberg, S. and Mac Lane, S. (1945). "General Theory of Natural Equivalences." *Transactions of the American Mathematical Society*, 58(2), 231-294.

Janssen, T.M.V. (1997). "Compositionality." In J. van Benthem and A. ter Meulen (eds.), *Handbook of Logic and Language*. Amsterdam: Elsevier, 417-473.

Lambek, J. (1972). "Deductive Systems and Categories III: Cartesian Closed Categories, Intuitionist Propositional Calculus, and Combinatory Logic." In *Toposes, Algebraic Geometry and Logic*. Springer LNM 274, 57-82.

Moggi, E. (1991). "Notions of Computation and Monads." *Information and Computation*, 93(1), 55-92.

### Self-Reference, Systems, and Governance

Beer, S. (1972). *Brain of the Firm*. London: Allen Lane.

Cousot, P. and Cousot, R. (1977). "Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints." In *Conference Record of the Fourth ACM Symposium on Principles of Programming Languages*. New York: ACM, 238-252.

Hofstadter, D. (1979). *Godel, Escher, Bach: An Eternal Golden Braid*. New York: Basic Books.

Hofstadter, D. (2007). *I Am a Strange Loop*. New York: Basic Books.

Maturana, H. and Varela, F. (1972). *De Maquinas y Seres Vivos: Autopoiesis, la Organizacion de lo Vivo*. Santiago: Editorial Universitaria.

Smith, B.C. (1984). "Reflection and Semantics in Lisp." In *Conference Record of the Eleventh ACM Symposium on Principles of Programming Languages*. New York: ACM, 23-35.

### Neural and Distributional Approaches

Clark, K., Khandelwal, U., Levy, O., and Manning, C.D. (2019). "What Does BERT Look At? An Analysis of BERT's Attention." In *Proceedings of the 2019 ACL Workshop BlackboxNLP*. Florence: ACL, 276-286.

Devlin, J., Chang, M.-W., Lee, K., and Toutanova, K. (2019). "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." In *Proceedings of NAACL-HLT 2019*. Minneapolis: ACL, 4171-4186.

Hewitt, J. and Manning, C.D. (2019). "A Structural Probe for Finding Syntax in Word Representations." In *Proceedings of NAACL-HLT 2019*. Minneapolis: ACL, 4129-4138.

Kartsaklis, D., Fan, M., and Sadrzadeh, M. (2021). "lambeq: An Efficient High-Level Python Library for Quantum NLP." arXiv:2110.04236.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, L., and Polosukhin, I. (2017). "Attention Is All You Need." In *Proceedings of NeurIPS 2017*. Long Beach: NeurIPS, 5998-6008.

### Wikipedia Articles Consulted

"Category theory." Wikipedia. Accessed 2026-03-21.

"Compositionality." Wikipedia. Accessed 2026-03-21.

"Edmund Husserl." Wikipedia. Accessed 2026-03-21.

"Hans-Georg Gadamer." Wikipedia. Accessed 2026-03-21.

"Hermeneutic circle." Wikipedia. Accessed 2026-03-21.

"Hermeneutics." Wikipedia. Accessed 2026-03-21.

"Inferentialism." Wikipedia. Accessed 2026-03-21.

"Intentionality." Wikipedia. Accessed 2026-03-21.

"J. L. Austin." Wikipedia. Accessed 2026-03-21.

"Meaning (philosophy)." Wikipedia. Accessed 2026-03-21.

"Natural transformation." Wikipedia. Accessed 2026-03-21.

"Paul Ricoeur." Wikipedia. Accessed 2026-03-21.

"Phenomenology (philosophy)." Wikipedia. Accessed 2026-03-21.

"Philosophy of language." Wikipedia. Accessed 2026-03-21.

"Pragmatics." Wikipedia. Accessed 2026-03-21.

"Self-reference." Wikipedia. Accessed 2026-03-21.

"Semantic holism." Wikipedia. Accessed 2026-03-21.

"Sense and reference." Wikipedia. Accessed 2026-03-21.

"Speech act." Wikipedia. Accessed 2026-03-21.

"Strange loop." Wikipedia. Accessed 2026-03-21.
