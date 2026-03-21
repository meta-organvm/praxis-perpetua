# Studium Generale ORGANVM -- Research Program Prospectus

> **Program Title:** The Formalization of Knowledge: From Social Origins to Logical Foundations
> **Program ID:** SGO-2026-RP-001
> **Date:** 2026-03-20
> **Status:** CANDIDATE (awaiting IRA panel review)
> **Source Corpus:** Wikipedia Research Atlas (March 2026) + 7 Research Adventures
> **Principal Investigator:** Sole Practitioner, ORGANVM System

---

## Preamble

This document constitutes a formal research program prospectus for the Studium Generale ORGANVM (SGO), the internal university housed in ORGAN-I (Theoria) with cross-organ intake authority. It synthesizes seven research adventures conducted in March 2026, each tracing a distinct thread from a sustained, self-directed investigation into the formalization of knowledge -- from its social origins through structural organization to logical foundations and measurement.

The program produces 7 primary research works (one per adventure), 5 cross-adventure synthesis papers, and a capstone dissertation. Together these constitute a coherent doctoral-level research contribution spanning formal semantics, computability theory, organizational science, philosophy of language, science and technology studies, and psychometrics.

All works participate in the ORGANVM promotion state machine (LOCAL -> CANDIDATE -> PUBLIC_PROCESS -> GRADUATED -> ARCHIVED) and are defended before the SGO evaluative authority's IRA panel serving as Faculty Senate.

---

## Table of Contents

1. [Individual Research Prospectuses](#individual-research-prospectuses)
   - [RP-01: The Semantics Bridge](#rp-01-the-semantics-bridge)
   - [RP-02: Self-Reference and the Limits of Self-Describing Systems](#rp-02-self-reference-and-the-limits-of-self-describing-systems)
   - [RP-03: Rhizome vs. Hierarchy](#rp-03-rhizome-vs-hierarchy)
   - [RP-04: The Naming Problem](#rp-04-the-naming-problem)
   - [RP-05: Latour's Network Ontology and Human-AI Systems](#rp-05-latours-network-ontology-and-human-ai-systems)
   - [RP-06: Chomsky to Computation](#rp-06-chomsky-to-computation)
   - [RP-07: Measurement Theory for Automated Assessment](#rp-07-measurement-theory-for-automated-assessment)
2. [Cross-Adventure Synthesis Papers](#cross-adventure-synthesis-papers)
   - [SYN-01: Grand Unified Semantics](#syn-01-grand-unified-semantics)
   - [SYN-02: The Governance Impossibility Thesis](#syn-02-the-governance-impossibility-thesis)
   - [SYN-03: Naming as Organizational Infrastructure](#syn-03-naming-as-organizational-infrastructure)
   - [SYN-04: The Flat Ontology of Sociotechnical Measurement](#syn-04-the-flat-ontology-of-sociotechnical-measurement)
   - [SYN-05: The Architecture of Meaning](#syn-05-the-architecture-of-meaning)
3. [Capstone Dissertation](#capstone-dissertation)
4. [Research Program Timeline](#research-program-timeline)
5. [Dependency Graph](#dependency-graph)
6. [Summary Tables](#summary-tables)

---

## Individual Research Prospectuses

---

### RP-01: The Semantics Bridge

**Title:** *Toward a Grand Unified Semantics: Compositionality, Lambda Calculus, and the Structural Unity of Meaning Across Logic, Computation, and Natural Language*

**Abstract:** The word "semantics" names three distinct academic traditions -- logical semantics (Tarski, Kripke), programming language semantics (Scott, Strachey), and formal natural language semantics (Montague, Heim, Kratzer). Each claims to study "meaning," yet each operates with different formalisms, different standards of adequacy, and different philosophical presuppositions. This paper investigates whether these three traditions are unified by deep structural bridges or merely share a homonymous label. Through systematic analysis of eight identified bridge structures -- compositionality, lambda calculus, the Curry-Howard-Lambek correspondence, type theory, model theory, game semantics, dynamic semantics, and proof-theoretic semantics -- we argue that the three traditions are instances of a single mathematical framework, with category theory providing the unifying metalanguage.

**Research Questions:**
1. To what extent does the Curry-Howard-Lambek correspondence provide a genuine structural unification of meaning across logic, computation, and natural language, and where does this unification break down?
2. Is dynamic semantics (meaning as context-change potential) a more natural unifying principle than truth-conditional semantics for bridging the three traditions, and what formal evidence supports or undermines this claim?
3. Can distributional semantics (the statistical/geometric theory of meaning underlying modern NLP) be reconciled with the formal semantic traditions, or does it constitute an irreducibly different theory of meaning?

**Literature Review Seed:**

| Section | Key Sources |
|---------|-------------|
| Foundations of Formal Semantics | Semantics (logic), Semantics (computer science), Semantics (programming languages), Philosophy of language, Meaning (philosophy) |
| The Compositional Bridge | Compositionality (Frege's principle), Denotational semantics, Montague grammar |
| The Lambda-Calculus Bridge | Lambda calculus, Type theory, Curry-Howard correspondence |
| The Dynamic Bridge | Dynamic semantics, Discourse representation theory, Situation semantics |
| The Game-Theoretic Bridge | Game semantics (logic, CS, NL independently) |
| The Categorical Bridge | Categorical semantics, Domain theory, Model theory |
| The Neural/Distributional Challenge | Computational semantics, Distributional semantics |
| **Frontier Articles** | Categorial grammar, Linear logic, Topos theory, Glue semantics, Combinatory categorial grammar, Inquisitive semantics, Substructural logic, Inferentialism (Brandom) |

**Methodology:** Conceptual analysis and formal comparison. For each identified bridge, we (a) formalize the structural parallel as a precise mathematical claim, (b) identify the conditions under which the parallel holds and fails, and (c) assess whether the parallel constitutes genuine isomorphism, homomorphism, or mere analogy. Category theory serves as the metatheoretic framework for comparing structural relationships across domains.

**Expected Contributions:**
- A systematic taxonomy of cross-domain semantic bridges ranked by structural strength (isomorphism > homomorphism > analogy > metaphor)
- Identification of the precise points where unification breaks down (concurrency, pragmatics, distributional meaning)
- A formal argument for whether category theory provides genuine unification or merely redescription at higher abstraction

**SGO Tier:** Dissertation (comprehensive, original contribution spanning three major fields)

**Target Venues:**
1. *Journal of Philosophical Logic* (Springer)
2. *Linguistics and Philosophy* (Springer)
3. arXiv: cs.LO (Logic in Computer Science) cross-listed with cs.CL (Computation and Language)

**Dependencies:** Foundational. Feeds into RP-06 (Chomsky->Computation), SYN-01, SYN-05.

**ORGANVM Connection:** The ORGANVM system uses naming conventions (double-hyphen), schema contracts (seed.yaml), and event routing (dispatch payloads) that are all exercises in applied formal semantics. A unified theory of meaning informs the design of the system's ontological layer (organvm-ontologia), particularly how entities are identified across different representational contexts (registry, seed, dashboard, MCP tools).

---

### RP-02: Self-Reference and the Limits of Self-Describing Systems

**Title:** *The Impossibility Landscape: Godelian Limits, Productive Self-Reference, and the Design of Self-Governing Computational Systems*

**Abstract:** Every system capable of arithmetic inherits a set of impossibility results -- Godel's incompleteness, Tarski's undefinability, Rice's theorem, the halting problem -- that constrain what it can prove, define, or decide about itself. Yet alongside these walls, productive forms of self-reference flourish: quines, reflection, bootstrapping, autopoietic self-maintenance. This paper maps both sides of the divide, formalizing the boundary between what self-describing systems can and cannot achieve. We derive seven design principles for systems that must describe, govern, and improve themselves while respecting the impossibility landscape. We argue that the distinction between syntactic self-description (tractable) and semantic self-description (intractable) provides the operational boundary for automated governance, and that staged self-reference (bootstrapping) and approximate self-analysis (abstract interpretation) constitute the practical response to formal impossibility.

**Research Questions:**
1. What is the precise boundary between decidable (syntactic) and undecidable (semantic) self-description in computational governance systems, and how should this boundary inform the allocation of automated versus human judgment in system governance?
2. Can Willard's self-verifying theories be applied to software governance systems -- identifying a "sweet spot" of reduced expressiveness where a system can verify its own key properties while remaining useful?
3. How does the Curry-Howard correspondence translate governance concepts (policies, compliance, promotion criteria) into type-theoretic terms, and what does incompleteness mean in this governance-as-type-theory framing?

**Literature Review Seed:**

| Section | Key Sources |
|---------|-------------|
| The Impossibility Results | Godel's incompleteness theorems, Tarski's undefinability theorem, Halting problem, Rice's theorem, Lob's theorem, Chaitin's incompleteness |
| The Self-Reference Mechanism | Diagonal argument, Self-reference, Fixed-point theorem, Kleene's recursion theorem |
| The Possibility Results | Quine (computing), Reflection (computer programming), Autopoiesis, Strange loop |
| Meta-Levels and Boundaries | Metalogic, Metamathematics, Metalanguage, Metatheorem, Second-order logic |
| Engineering Self-Reference | Logic programming, Computational metaphysics, Church-Turing thesis |
| **Frontier Articles** | Diagonal lemma, Godel numbering, Provability logic, Self-verifying theories (Willard), Impredicativity, Fixed-point combinator, Paraconsistent logic |

**Methodology:** Formal analysis of impossibility results applied to a concrete case study (the ORGANVM governance system). For each impossibility theorem, we (a) state the precise conditions under which it applies, (b) assess whether the ORGANVM system meets those conditions, and (c) derive specific design constraints. The case study grounds abstract results in engineering reality.

**Expected Contributions:**
- A practitioner-oriented taxonomy of self-reference: what computational governance systems can automate (syntactic properties) versus what requires human judgment (semantic properties)
- Formal criteria for when staged self-reference (bootstrapping pattern) produces valid self-description
- An assessment of whether Willard-style self-verification is practically achievable in governance systems

**SGO Tier:** Thesis (medium, multi-chapter -- requires both formal exposition and applied case study)

**Target Venues:**
1. *ACM Computing Surveys* (survey paper with formal core)
2. *Studia Logica* (formal logical analysis)
3. arXiv: cs.LO cross-listed with cs.SE (Software Engineering)

**Dependencies:** Foundational. Feeds into SYN-02 (Governance Impossibility), SYN-05 (Architecture of Meaning). Draws on RP-01 (semantic vs. syntactic distinction).

**ORGANVM Connection:** Directly informs the governance architecture of ORGAN-IV (Taxis). The promotion state machine, dependency validation, and registry integrity checks are all exercises in self-describing system governance. The finding that "no system can be its own final auditor" provides the theoretical justification for the human-in-the-loop design principle. The syntactic/semantic boundary maps directly onto what can be mechanized (naming convention compliance, schema validation, dependency acyclicity) versus what requires human review (fitness for purpose, ethical alignment, architectural coherence).

---

### RP-03: Rhizome vs. Hierarchy

**Title:** *Compression and Search: A Decision Framework for Organizational Topology in Human-AI Systems*

**Abstract:** Hierarchical and rhizomatic organizational forms represent two fundamental strategies for managing complexity: hierarchy compresses the combinatorial explosion of possible connections into a legible tree, while rhizomatic structure preserves all connections, maximizing creativity and resilience at the cost of legibility. Drawing on Deleuze and Guattari's rhizome concept, McCulloch's heterarchy, Koestler's holarchy, ecological panarchy, scale-free network theory, and eight cross-domain case studies (Internet, Wikipedia, ant colonies, military command, open source, mycelial networks, the Catholic Church, blockchain governance), this paper develops a formal decision framework for when to compress (hierarchize) and when to search (rhizomatize). We present the meta-principle that hierarchy is a compression algorithm and rhizome is a search algorithm, derive conditions under which each is optimal, identify the "emergence trap" whereby rhizomatic systems spontaneously develop de facto hierarchy through preferential attachment, and propose hybrid organizational topologies suited to human-AI collaborative systems.

**Research Questions:**
1. Can the rhizome/hierarchy distinction be formalized using graph-theoretic measures (density, clustering coefficient, power-law exponent) to produce a quantitative "rhizomaticity index" for organizational structures?
2. Is there a fundamental scale limit (analogous to Dunbar's number) for rhizomatic organization, and can AI-mediated coordination extend this limit?
3. What is the relationship between organizational legibility (Scott's *Seeing Like a State*) and hierarchy -- and can technologies providing legibility without hierarchy (dashboards over meshes, distributed observability) reduce the need for hierarchical structure?

**Literature Review Seed:**

| Section | Key Sources |
|---------|-------------|
| The Rhizome Concept | Rhizome (philosophy), Deleuze and Guattari, A Thousand Plateaus, Assemblage (philosophy) |
| Hierarchy and Its Alternatives | Hierarchy, Heterarchy, Holarchy, Panarchy (ecology) |
| Systems Theory | Systems theory, General systems theory, Ecological systems theory, Complex systems |
| Self-Organization | Emergence, Stigmergy, Self-organization, Autopoiesis, Cybernetics |
| Network Theory | Scale-free networks, Network theory, Distributed computing, Decentralization |
| Social Structure | Social structure, World-systems theory, Actor-network theory, Structuralism |
| **Frontier Articles** | Adhocracy, Flat organization, Folksonomy, Peer-to-peer, Spontaneous order, Swarm intelligence, Mesh networking, Deterritorialization, Arborescence (graph theory) |

**Methodology:** Mixed-methods. (1) Conceptual analysis of philosophical and systems-theoretic literature to construct the spectrum model. (2) Graph-theoretic formalization to propose quantitative measures of organizational topology. (3) Comparative case study analysis across eight empirical domains. (4) Application of the decision framework to the ORGANVM eight-organ architecture.

**Expected Contributions:**
- A formal spectrum model from pure hierarchy to pure rhizome with intermediate forms (holarchy, panarchy, heterarchy) precisely positioned
- The "compression vs. search" meta-principle as a design heuristic for organizational topology
- The "emergence trap" theorem: conditions under which rhizomatic systems develop de facto hierarchy through preferential attachment
- A decision framework with specific criteria for choosing organizational topology in human-AI systems

**SGO Tier:** Thesis (medium, multi-chapter -- combines philosophical analysis with formal and empirical components)

**Target Venues:**
1. *Organization Science* (INFORMS)
2. *Computational and Mathematical Organization Theory* (Springer)
3. arXiv: cs.MA (Multi-Agent Systems) cross-listed with cs.CY (Computers and Society)

**Dependencies:** Draws on RP-05 (Latour's ANT for the flat ontology perspective). Feeds into SYN-02 (governance topology), SYN-04 (organizational measurement).

**ORGANVM Connection:** The ORGANVM eight-organ model is an explicit exercise in organizational topology -- combining hierarchical elements (the organ hierarchy, the promotion state machine, the dependency flow I->II->III) with rhizomatic elements (any organ can produce/consume events from any other, cross-organ MCP tool access, lateral seed.yaml linkage). The decision framework directly informs whether ORGANVM's current topology is optimal and where it should be more hierarchical or more rhizomatic.

---

### RP-04: The Naming Problem

**Title:** *Rigid Designators, Controlled Vocabularies, and Namespace Hierarchies: Toward a Unified Theory of Naming Across Philosophy, Linguistics, and Computing*

**Abstract:** The act of naming is simultaneously a philosophical problem (what is the relationship between a name and its referent?), a linguistic problem (how are names organized into systems?), and an engineering problem (how do names work in machines?). This paper traces three traditions of naming theory -- the philosophical (Frege's sense/reference, Kripke's rigid designators, Wittgenstein's language games), the linguistic-scientific (nomenclature, taxonomy, systematic naming, controlled vocabularies), and the computational (identifiers, naming conventions, namespaces, ontologies) -- and identifies their points of structural convergence and divergence. We argue that naming is fundamentally a compression problem (a name compresses a complex entity into a manipulable token) subject to a universal tradeoff between expressiveness and usability, and that every naming failure (reference failure, namespace collision, semantic drift, abstraction mismatch) has structural analogues across all three traditions.

**Research Questions:**
1. Is there a universal theory of naming that subsumes Kripke's causal theory, Saussure's arbitrariness principle, and computing's namespace model, or are these irreducibly different accounts of different phenomena?
2. What is the optimal information density of a name, and does the answer depend on system scale, domain, or lifecycle stage?
3. How does the type-token distinction (a philosophical concept) operationalize differently in natural language, formal systems, and programming, and what does this reveal about the nature of naming?

**Literature Review Seed:**

| Section | Key Sources |
|---------|-------------|
| Philosophical Foundations | Philosophy of language, Meaning (philosophy), Proper name (philosophy), Direct reference theory |
| The Descriptivist Tradition | Sense and reference (Frege), Descriptivist theory of names, Gottlob Frege |
| The Causal-Direct Tradition | Naming and Necessity (Kripke), Rigid designator, Causal theory of reference, Natural kind |
| The Use-Theoretic Tradition | Language game (Wittgenstein), Self-reference |
| Semiotics | Semiotics, Signifier and signified, Semiotic triangle, Sign (semiotics), Ferdinand de Saussure |
| Linguistic-Scientific Naming | Nomenclature, Taxonomy, Typology, Scientific classification, Systematic name |
| Computational Naming | Naming convention (programming), Identifier (computer science), Namespace, Symbol (formal), Type-token distinction |
| Information Architecture | Ontology (information science), Controlled vocabulary, Thesaurus (information retrieval) |
| **Frontier Articles** | A posteriori necessity, Dthat (Kaplan), Identity (philosophy), Code (semiotics), Biosemiotics, Computational semiotics, Cratylus (dialogue), Universals (philosophy), Ontological commitment, Semantic web, URI |

**Methodology:** Comparative conceptual analysis across three disciplinary traditions. For each naming phenomenon (reference failure, collision, drift, governance), we (a) document its manifestation in philosophy, linguistics, and computing, (b) identify the shared structural mechanism, and (c) assess whether the parallel constitutes genuine isomorphism or surface analogy. Case study analysis of the ORGANVM double-hyphen naming convention as an applied micro-nomenclature.

**Expected Contributions:**
- A cross-domain taxonomy of naming failures showing structural analogues across philosophy, linguistics, and computing
- The "naming as compression" thesis with a formal expressiveness-usability tradeoff model
- A set of naming design principles derived from the synthesis (ontological commitment, sense preservation, namespace investment, controlled vocabulary discipline, type-token discipline, governance proportionality, language-game specification)

**SGO Tier:** Paper (short, focused -- conceptual analysis without formal proof or large-scale empirical work)

**Target Venues:**
1. *Synthese* (philosophy of science, interdisciplinary)
2. *Journal of the Association for Information Science and Technology* (JASIST)
3. arXiv: cs.PL (Programming Languages) cross-listed with cs.CL

**Dependencies:** Draws on RP-01 (the semantics of naming), RP-06 (type-theoretic perspective on naming). Feeds into SYN-03 (naming as infrastructure).

**ORGANVM Connection:** The double-hyphen naming convention (`sema-metra--alchemica-mundi`), the organ naming scheme (Greek roots encoding function), the registry namespace (`ORGAN-I` through `META-ORGANVM`), and the seed.yaml contracts are all exercises in applied naming theory. This research directly informs whether the ORGANVM naming conventions constitute rigid designators or descriptions, how they should evolve as the system scales, and what governance structures are needed to prevent naming drift.

---

### RP-05: Latour's Network Ontology and Human-AI Systems

**Title:** *Mediators, Not Intermediaries: Actor-Network Theory as a Framework for Understanding Human-AI Collaborative Systems*

**Abstract:** Actor-network theory (ANT) -- developed by Latour, Callon, and Law to dissolve the subject/object binary in science studies -- provides a rich vocabulary for analyzing human-AI systems: actants, translation, enrollment, obligatory passage points, blackboxing, punctualization, boundary objects, immutable mobiles. This paper systematically applies ANT's conceptual apparatus to multi-agent AI architectures, arguing that AI systems are mediators (transforming what passes through them) rather than intermediaries (transparent conduits). We map Callon's four-moment translation sequence onto the prompt-response cycle, identify system prompts and tool schemas as immutable mobiles, and analyze the MCP protocol layer as an obligatory passage point. Drawing on Haraway's situated knowledges, Barad's agential realism, and Suchman's critique of planning, we develop a critical extension of ANT that addresses three challenges the original framework was not designed for: constitutive opacity (blackboxing that cannot in principle be opened), computational scale (billions of parameters resisting ethnographic description), and recursive self-modification (networks that reshape the conditions of their own enrollment).

**Research Questions:**
1. Does ANT's principle of generalized symmetry -- requiring the same analytical vocabulary for human and nonhuman actants -- constitute a productive framework for understanding human-AI collaboration, or does it obscure morally relevant distinctions between human agency and computational process?
2. How should ANT's concept of translation be modified to account for systems whose internal complexity is constitutively opaque (AI models whose designers cannot fully explain their behavior), as opposed to merely practically opaque (black boxes that could in principle be opened)?
3. Can "alignment" be productively reframed as a translation problem (ongoing network stabilization) rather than a value-installation problem (instilling fixed values in an AI object)?

**Literature Review Seed:**

| Section | Key Sources |
|---------|-------------|
| ANT Foundations | Bruno Latour, Actor-network theory, We Have Never Been Modern, Translation (sociology) |
| Key ANT Concepts | Obligatory passage point, Blackboxing, Boundary object, Assemblage (philosophy) |
| Post-Structural Roots | Rhizome (philosophy), Structuralism, Post-structuralism, Heterarchy, Bricolage |
| Extensions and Critics | Donna Haraway, A Cyborg Manifesto, Object-oriented ontology, Speculative realism, Karen Barad, Agential realism |
| STS Context | Science and technology studies, Social construction of technology, Technological determinism, Sociomateriality |
| **Frontier Articles** | Annemarie Mol (multiplicity), Lucy Suchman (situated actions), Performativity, Mapping controversies, Politics of Nature, Postcritique, Trading zones, Co-production, Knowledge production modes |

**Methodology:** Theoretical analysis with applied case study. (1) Systematic mapping of ANT concepts to AI system concepts (table-based analysis). (2) Extended case study of the ORGANVM system as actor-network (human operator, Claude Code, MCP servers, seed.yaml contracts, governance rules, promotion state machine as interacting actants). (3) Critical analysis of ANT's adequacy for AI through Haraway, Barad, and Suchman's lenses.

**Expected Contributions:**
- A systematic mapping of ANT concepts to human-AI system concepts (actant = any entity that acts; translation = prompt-response cycle; OPP = MCP protocol layer; immutable mobile = system prompt/schema; etc.)
- A critique and extension of ANT's symmetry principle for systems with constitutive opacity
- A reframing of alignment as ongoing translation (network stabilization) rather than value installation

**SGO Tier:** Thesis (medium, multi-chapter -- theoretical framework with applied case study)

**Target Venues:**
1. *Social Studies of Science* (SAGE)
2. *Science, Technology, & Human Values* (SAGE)
3. arXiv: cs.AI cross-listed with cs.CY

**Dependencies:** Draws on RP-03 (rhizome/hierarchy for ANT's flat ontology). Feeds into SYN-02 (governance), SYN-04 (sociotechnical measurement).

**ORGANVM Connection:** The entire ORGANVM system is an actor-network: human operator, AI models, MCP servers, textual actants (seed.yaml, registry-v2.json, CLAUDE.md), institutional actants (GitHub organizations, CI/CD), conceptual actants (the eight-organ model, the conductor metaphor). The governance-rules.json and validate-deps.py function as obligatory passage points. The commitment to "human directs, AI generates, human reviews" is a translation script defining enrollment conditions. This research provides the theoretical vocabulary for analyzing and improving the system's collaborative architecture.

---

### RP-06: Chomsky to Computation

**Title:** *Grammars, Types, Proofs, and Categories: The Fourfold Correspondence from Chomsky's Hierarchy to the Curry-Howard-Lambek Triangle*

**Abstract:** Noam Chomsky's 1956-1959 formalization of grammar produced the hierarchy of formal languages (regular, context-free, context-sensitive, recursively enumerable). Independently, Church, Curry, and Howard established the correspondence between proofs and programs, and Lambek connected both to category theory and to linguistic grammar. This paper traces three parallel threads from Chomsky's origin: the "machines" thread (formal language theory and automata), the "engineering" thread (programming language syntax and compilers), and the "logic" thread (type theory, categorial grammar, Curry-Howard-Lambek). We demonstrate that each level of the Chomsky hierarchy corresponds not only to a class of automata (classical result) but also to a regime of type-theoretic expressiveness: regular grammars to finite types, context-free grammars to recursive algebraic types, context-sensitive grammars to parametric polymorphism, and unrestricted grammars to full dependent types. The convergence of all three threads reveals that grammars, types, proofs, and categories are not merely analogous but structurally isomorphic. We formalize the claim that parsing IS type-checking IS proof construction IS composition of morphisms, and identify the open problem of characterizing the type-theoretic signature of mildly context-sensitive languages -- the complexity class most likely corresponding to natural language.

**Research Questions:**
1. What is the precise type-theoretic characterization of mildly context-sensitive languages (the conjectured complexity class of natural language), and can this characterization be expressed in the Curry-Howard-Lambek framework?
2. Do neural language models (transformers) implicitly learn type-theoretic structure, and if so, at what level of the Chomsky hierarchy does their implicit grammar reside?
3. Is Chomsky's Minimalist Program's Merge operation formally equivalent to function application in the typed lambda calculus, and what does this equivalence (or inequivalence) imply for the relationship between linguistic competence and computational capacity?

**Literature Review Seed:**

| Section | Key Sources |
|---------|-------------|
| Chomsky's Contribution | Syntactic Structures, The Logical Structure of Linguistic Theory, Chomsky hierarchy, Generative grammar, Universal grammar, Minimalist program |
| Formal Language Theory | Formal language, Formal grammar, Context-free grammar, Context-sensitive grammar, Regular language, Recursively enumerable language |
| Automata Theory | Automata theory, Finite automaton, Pushdown automaton, Linear bounded automaton, Turing machine |
| Type Theory | Type theory, Lambda calculus, Curry-Howard correspondence, Simply typed lambda calculus, Dependent type |
| Categorial Grammar | Categorial grammar, Combinatory categorial grammar, Pregroup grammar, Montague grammar |
| Compiler Theory | Compiler, Parsing, Backus-Naur form, Abstract syntax tree |
| Syntax-Semantics Interface | Syntax-semantics interface, Model-theoretic grammar, Logic translation |
| **Frontier Articles** | Mildly context-sensitive language, Tree-adjoining grammar, DisCoCat, Calculus of constructions, Linear logic, Homotopy Type Theory, Glue semantics, Typelogical grammar |

**Methodology:** Formal proof-theoretic analysis. For each level of the Chomsky hierarchy, we (a) state the classical grammar-automaton correspondence, (b) propose the corresponding type-theoretic characterization, (c) prove containment (every type at level n can express everything at level n-1), and (d) prove separation where possible (there exist types at level n inexpressible at level n-1). For the mildly context-sensitive case, we survey existing partial results and state the open problem precisely.

**Expected Contributions:**
- A formal "Chomsky hierarchy of type systems" with containment and separation theorems
- The argument that categorial grammar makes the grammar-type-proof-category correspondence fully explicit and linguistically concrete
- Identification of the open problem: the type-theoretic characterization of mildly context-sensitive languages (and by extension, natural language's computational signature)

**SGO Tier:** Dissertation (comprehensive, original contribution requiring formal proofs spanning formal language theory, type theory, and linguistics)

**Target Venues:**
1. *Journal of Logic, Language and Information* (Springer)
2. *Mathematical Structures in Computer Science* (Cambridge)
3. arXiv: cs.FL (Formal Languages and Automata Theory) cross-listed with cs.LO

**Dependencies:** Draws on RP-01 (the semantics bridge, especially compositionality and Curry-Howard). Feeds into SYN-01 (Grand Unified Semantics), SYN-05 (Architecture of Meaning).

**ORGANVM Connection:** The ORGANVM system uses formal grammars implicitly throughout: BNF-like schema definitions (seed.yaml structure), context-free validation rules (JSON Schema), and context-sensitive governance rules (promotion requires checking cross-repo dependency context). Understanding where each governance rule sits in the Chomsky hierarchy informs which rules can be fully automated (regular, context-free) and which require more sophisticated analysis (context-sensitive) or human judgment (beyond formal decidability).

---

### RP-07: Measurement Theory for Automated Assessment

**Title:** *Goodhart's Governance: Psychometric Validity Theory Applied to Automated Software Quality Assessment and Promotion State Machines*

**Abstract:** Automated assessment systems -- code quality metrics, repo readiness scores, promotion gates, CI/CD thresholds -- implicitly construct measurement instruments. Yet these instruments are rarely subjected to the psychometric validation that educational and psychological testing demands. This paper applies the unified validity framework (Messick 1989) to automated software governance systems, demonstrating that standard code quality metrics face systematic content validity gaps, that promotion state machines (LOCAL -> CANDIDATE -> PUBLIC -> GRADUATED) implicitly assume a Guttman cumulative scale that may not hold empirically, that measurement invariance across technology stacks must be tested rather than assumed, and that Goodhart's Law ("when a measure becomes a target, it ceases to be a good measure") provides the consequential validity challenge for all automated governance. We propose an IRT-based adaptive assessment framework for repo evaluation that weights criteria by difficulty and informativeness, analogous to computerized adaptive testing in psychometrics, and develop a Rasch-model-inspired calibration methodology for promotion rubrics that achieves specific objectivity across evaluation contexts.

**Research Questions:**
1. Can software quality be validly measured as a single latent variable, or does factor analysis of common code metrics (coverage, complexity, lint violations, build stability, dependency freshness) reveal multiple distinct constructs that should not be collapsed?
2. Does the ORGANVM promotion state machine (LOCAL -> CANDIDATE -> PUBLIC_PROCESS -> GRADUATED) empirically satisfy Guttman scale properties (cumulative attainment), and what violations indicate about the construct validity of the promotion construct?
3. How should measurement invariance be established for code quality metrics applied across programming languages, technology stacks, and project types, and what psychometric methods (multi-group CFA, differential item functioning analysis) are appropriate?

**Literature Review Seed:**

| Section | Key Sources |
|---------|-------------|
| Measurement Foundations | Scale (social sciences), Sorting, Levels of measurement, Operational definition, Latent variable |
| Validity Theory | Test validity, Construct validity, Content validity, Criterion validity, Measurement invariance |
| Classical Test Theory | Classical test theory, Reliability (statistics), Inter-rater reliability |
| Item Response Theory | Item response theory, Rasch model, Differential item functioning, Computerized adaptive testing |
| Scale Construction | Likert scale, Thurstone scale, Guttman scale, Theory of conjoint measurement |
| Statistical Methods | Factor analysis, Structural equation modeling |
| Automated Assessment | Automated essay scoring, Academic grading in the United States, Rubric (academic) |
| **Frontier Articles** | Computational psychometrics, Nomological network, Multitrait-multimethod matrix, Cronbach's alpha, Spearman-Brown formula, Jingle-jangle fallacies, Campbell's Law, Goodhart's Law, Standards for Educational and Psychological Testing |

**Methodology:** Mixed-methods. (1) Psychometric analysis: apply factor analysis to code quality metrics across the ORGANVM repo corpus to test the unidimensionality assumption. (2) Guttman scalogram analysis of the promotion state machine to test cumulative attainment. (3) Multi-group CFA across technology stacks to test measurement invariance. (4) Design and calibration of an IRT-based adaptive assessment instrument for repo evaluation. (5) Consequential validity analysis through the lens of Goodhart's/Campbell's Law.

**Expected Contributions:**
- The first application of Messick's unified validity framework to automated software governance
- Empirical test of the Guttman scale assumption in a promotion state machine
- An IRT-based adaptive assessment framework for repo evaluation
- Formal analysis of how Goodhart's Law undermines automated governance and proposed mitigations

**SGO Tier:** Thesis (medium, multi-chapter -- theoretical framework plus empirical validation on ORGANVM data)

**Target Venues:**
1. *Empirical Software Engineering* (Springer)
2. *Journal of Systems and Software* (Elsevier)
3. arXiv: cs.SE cross-listed with stat.AP (Statistics Applications)

**Dependencies:** Foundational for applied measurement within the system. Feeds into SYN-02 (governance), SYN-04 (sociotechnical measurement).

**ORGANVM Connection:** This is the most directly applied research work. The promotion state machine (LOCAL -> CANDIDATE -> PUBLIC_PROCESS -> GRADUATED -> ARCHIVED), the seed.yaml contracts as operational definitions, the system-metrics.json as a measurement instrument, and the omega scorecard as a criterion -- all are measurement systems that this research subjects to psychometric scrutiny. The IRT-based adaptive assessment framework is immediately implementable in the organvm-engine metrics module.

---

## Cross-Adventure Synthesis Papers

These papers bridge two or more adventures. They are often the most original contributions because they connect fields that do not typically communicate.

---

### SYN-01: Grand Unified Semantics

**Title:** *From Montague to Merge: A Categorical Framework for Unifying Formal Semantics, Type Theory, and the Chomsky Hierarchy*

**Adventures Bridged:** RP-01 (Semantics Bridge) + RP-06 (Chomsky to Computation)

**Why the Bridge Is Novel:** RP-01 identifies compositionality, lambda calculus, and the Curry-Howard-Lambek correspondence as structural bridges between logic, computation, and natural language semantics. RP-06 establishes the correspondence between the Chomsky hierarchy and a hierarchy of type systems. SYN-01 connects these: if grammars are type systems and semantics is type-preserving interpretation, then the Chomsky hierarchy is simultaneously a hierarchy of syntactic, semantic, and computational complexity. No existing work systematically traces this triple hierarchy from regular grammars through to dependent types while maintaining the semantic dimension.

**SGO Tier:** Dissertation (comprehensive, original contribution requiring mastery of formal semantics, type theory, and formal language theory simultaneously)

---

### SYN-02: The Governance Impossibility Thesis

**Title:** *Why No System Can Fully Govern Itself: Godelian Limits, Rhizomatic Emergence, and the Design of Human-AI Governance Architectures*

**Adventures Bridged:** RP-02 (Self-Reference Limits) + RP-03 (Rhizome vs. Hierarchy) + RP-05 (Latour's Network Ontology) + RP-07 (Measurement Theory)

**Why the Bridge Is Novel:** RP-02 establishes formal impossibility results for self-describing systems. RP-03 identifies the "emergence trap" (rhizomatic systems spontaneously develop hierarchy). RP-05 provides ANT's vocabulary for analyzing governance networks. RP-07 adds Goodhart's Law as a measurement-theoretic impossibility result. SYN-02 synthesizes these into a unified "governance impossibility thesis": every governance system faces at least four irreducible constraints -- Godelian incompleteness (cannot fully self-verify), the emergence trap (flat governance tends toward hierarchy), constitutive opacity (cannot fully inspect AI mediators), and Goodhart's Law (measurement targets corrupt the measures). The paper then derives design principles for governance architectures that acknowledge rather than deny these constraints.

**SGO Tier:** Thesis (the synthesis is original but builds on formal results established in the component papers)

---

### SYN-03: Naming as Organizational Infrastructure

**Title:** *Baptism Events, Namespace Hierarchies, and Controlled Vocabularies: How Naming Constitutes Organizational Structure in Human-AI Systems*

**Adventures Bridged:** RP-04 (The Naming Problem) + RP-03 (Rhizome vs. Hierarchy) + RP-05 (Latour's Network Ontology)

**Why the Bridge Is Novel:** RP-04 establishes that naming is an ontological commitment (to name something is to assert its existence and category membership). RP-03 demonstrates that organizational topology falls on a spectrum from hierarchical to rhizomatic. RP-05 provides ANT's concept of immutable mobiles (inscriptions that travel without transformation). SYN-03 connects these: naming conventions ARE organizational infrastructure. A hierarchical namespace (like DNS or Java packages) encodes and enforces hierarchical organizational structure. A flat namespace (like npm packages or hashtags) enables rhizomatic connection. The ORGANVM double-hyphen convention is analyzed as a hybrid: hierarchical at the word level (single hyphen separates words within a function or descriptor), flat at the structural level (double hyphen separates any function from any descriptor without predefined hierarchy). Names in human-AI systems function as immutable mobiles -- they travel across contexts (human reading, AI parsing, machine execution) while maintaining their referential force.

**SGO Tier:** Paper (focused synthesis, conceptual analysis without formal proof)

---

### SYN-04: The Flat Ontology of Sociotechnical Measurement

**Title:** *Measuring Hybrids: How Actor-Network Theory Complicates and Enriches Psychometric Validity for Sociotechnical Assessment*

**Adventures Bridged:** RP-05 (Latour's Network Ontology) + RP-07 (Measurement Theory)

**Why the Bridge Is Novel:** RP-05 establishes that AI systems are mediators (transforming what passes through them) and that agency is distributed across networks rather than located in individuals. RP-07 applies psychometric validity theory to automated assessment. SYN-04 asks: what happens to measurement validity when the thing being measured is a sociotechnical network rather than an individual entity? Classical psychometrics assumes a stable "respondent" whose latent trait is being measured. But in an actor-network, the "respondent" is a shifting assemblage of human, AI, and institutional actants. Code quality is not a property of the repo alone but of the network that produced, maintains, and evaluates it. This paper proposes a "network psychometrics" that extends validity theory to account for distributed, relational attributes.

**SGO Tier:** Paper (theoretical -- bridges two established frameworks without requiring formal proof)

---

### SYN-05: The Architecture of Meaning

**Title:** *From Naming to Proving: How the Formalization of Knowledge Constitutes, Constrains, and Transforms Institutional Systems*

**Adventures Bridged:** RP-01 (Semantics) + RP-02 (Self-Reference) + RP-04 (Naming) + RP-06 (Chomsky to Computation)

**Why the Bridge Is Novel:** This is the capstone synthesis of the entire research program. The atlas revealed a grand arc: WHAT IS KNOWLEDGE -> HOW DO WE NAME THINGS -> HOW DOES MEANING BECOME FORMAL -> WHAT ARE THE LIMITS OF FORMALIZATION. SYN-05 traces this arc as a unified argument: knowledge begins with naming (RP-04), naming acquires structure through grammar and type systems (RP-06), structured names receive formal semantics (RP-01), and formal semantics encounters the impossibility results that constrain all self-describing systems (RP-02). The paper argues that this arc is not merely a research trajectory but a fundamental dynamic of institutional systems: every institution that formalizes its knowledge (codifies norms, automates processes, defines metrics) traverses this same path from naming to formalization to self-referential limits. The ORGANVM system is presented as a case study of this dynamic.

**SGO Tier:** Dissertation (the capstone -- requires synthesis across all four foundational adventures and the entire research atlas)

---

## Capstone Dissertation

**Title:** *The Formalization of Knowledge: A Systematic Investigation of Meaning, Structure, Self-Reference, and Measurement in Human-AI Institutional Systems*

**Abstract:** This dissertation investigates the formalization of knowledge as a unified phenomenon spanning philosophy, linguistics, formal logic, computer science, organizational science, and psychometrics. Drawing on a sustained research program of seven interconnected studies and five synthesis papers, it traces a single trajectory: from naming (how knowledge acquires identifiers), through grammar and type theory (how names acquire structure), through formal semantics (how structure acquires meaning), to self-reference and measurement (how meaning encounters the limits of self-description and the challenges of valid assessment). The ORGANVM system -- an eight-organ creative-institutional architecture designed to enable one person to operate at enterprise scale through human-AI collaboration -- serves as both the motivating case study and the primary application domain. The dissertation argues that the formalization of knowledge follows a universal pattern observable across biological systems (genetic codes), human institutions (legal codes), and computational systems (programming languages and governance rules), and that understanding this pattern's structure and limits is essential for designing governance architectures for the age of AI-mediated institutional action.

**SGO Tier:** Dissertation (SGO-2026-D-003)

**Chapters:**
1. Introduction: The Grand Arc
2. Naming and Reference (from RP-04)
3. Grammar and Type Systems (from RP-06)
4. Formal Semantics and the Unity of Meaning (from RP-01)
5. Self-Reference and the Impossibility Landscape (from RP-02)
6. Organizational Topology: Compression and Search (from RP-03)
7. Actor-Networks and the Politics of Mediation (from RP-05)
8. Measurement Validity for Automated Governance (from RP-07)
9. Synthesis I: The Grammar-Type-Semantics Triple Hierarchy (from SYN-01)
10. Synthesis II: The Governance Impossibility Thesis (from SYN-02)
11. Synthesis III: The Architecture of Meaning (from SYN-05)
12. Conclusion: Formalization, Limits, and the Design of Human-AI Institutions

---

## Research Program Timeline

### Phase 1: Foundations (Months 1-6)

Establish the theoretical groundwork. These papers must come first because all later work depends on their conceptual apparatus.

| Priority | Work | Rationale |
|----------|------|-----------|
| 1.1 | **RP-04: The Naming Problem** | Naming is the most fundamental operation -- it precedes grammar, semantics, and measurement. Also the most self-contained paper (Paper tier), providing an early deliverable. |
| 1.2 | **RP-02: Self-Reference & Limits** | Establishes the impossibility landscape that constrains all subsequent work. Without this, the governance and measurement papers lack their theoretical ceiling. |
| 1.3 | **RP-06: Chomsky to Computation** | Establishes the grammar-type-proof correspondence that RP-01 and SYN-01 build upon. Requires formal proof work that benefits from early, focused attention. |

### Phase 2: Bridges (Months 4-12)

Build the bridges between the foundational works. These papers draw on Phase 1 results and connect previously separate domains.

| Priority | Work | Rationale |
|----------|------|-----------|
| 2.1 | **RP-01: The Semantics Bridge** | The central theoretical contribution. Requires RP-06's grammar-type correspondence as input. |
| 2.2 | **RP-03: Rhizome vs. Hierarchy** | The organizational theory paper. Combines philosophical analysis with formal graph theory and case studies. Can begin in parallel with RP-01. |
| 2.3 | **RP-05: Latour's Network Ontology** | Requires RP-03 for the flat ontology perspective. Adds the critical/philosophical dimension. |
| 2.4 | **SYN-03: Naming as Infrastructure** | First synthesis paper. Bridges RP-04 (naming) with RP-03 (topology) and RP-05 (ANT). Early synthesis provides momentum. |

### Phase 3: Applications and Synthesis (Months 10-18)

Apply the theoretical framework to the ORGANVM system and produce the synthesis papers.

| Priority | Work | Rationale |
|----------|------|-----------|
| 3.1 | **RP-07: Measurement Theory** | The most applied paper. Requires some RP-02 concepts (governance limits) and RP-03 (organizational topology). |
| 3.2 | **SYN-02: Governance Impossibility** | Bridges RP-02, RP-03, RP-05, RP-07. Requires all four component papers. |
| 3.3 | **SYN-04: Flat Ontology of Measurement** | Bridges RP-05 and RP-07. Requires both. |
| 3.4 | **SYN-01: Grand Unified Semantics** | Bridges RP-01 and RP-06. The most technically demanding synthesis. |

### Phase 4: Capstone (Months 16-24)

Produce the final synthesis and the capstone dissertation.

| Priority | Work | Rationale |
|----------|------|-----------|
| 4.1 | **SYN-05: Architecture of Meaning** | The meta-synthesis bridging RP-01, RP-02, RP-04, RP-06. Requires all Phase 1 and Phase 2 results. |
| 4.2 | **Capstone Dissertation** | Integrates all 7 primary papers and 5 synthesis papers into a unified doctoral-level contribution. |

### Timeline Visualization

```
Month:  1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21   22   23   24
        |----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
RP-04   [========]
RP-02   [================]
RP-06        [================]
RP-01                  [====================]
RP-03                  [================]
RP-05                            [================]
SYN-03                           [========]
RP-07                                      [================]
SYN-02                                               [================]
SYN-04                                               [========]
SYN-01                                                    [================]
SYN-05                                                                   [================]
CAPSTONE                                                                      [========================]
        |----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
        PHASE 1: FOUNDATIONS     PHASE 2: BRIDGES          PHASE 3: APPLICATION       PHASE 4: CAPSTONE
```

---

## Dependency Graph

```
                                 RP-04 (Naming)
                                /    |    \
                               /     |     \
                        RP-06 (Chomsky)   SYN-03 (Naming as Infra.)
                        /    \            /    \
                       /      \          /      \
                RP-01 (Semantics)  RP-03 (Rhizome)  RP-05 (Latour)
                /    \              |    \           /    |
               /      \            |     \         /     |
        SYN-01 (GUS)   \     SYN-02 (Gov.)-------'      |
               \        \        / |  \                  |
                \        \      /  |   \                 |
                 \   RP-02 (Self-Ref.)  \                |
                  \                      \               |
                   \               RP-07 (Measurement)   |
                    \                  /     \           /
                     \                /    SYN-04 (Flat Measurement)
                      \              /
                    SYN-05 (Architecture of Meaning)
                              |
                        CAPSTONE DISSERTATION
```

### Legend:
- **Solid arrows** indicate hard dependencies (the downstream paper requires results from the upstream paper)
- **RP-04, RP-02, RP-06** are the three foundational works (no upstream dependencies within the program)
- **SYN-05 and the Capstone** are the terminal works (everything flows into them)

---

## Summary Tables

### Table 1: All Research Works

| ID | Title (Short) | SGO Tier | Phase | Dependencies | Target Venues |
|----|---------------|----------|-------|--------------|---------------|
| RP-01 | The Semantics Bridge | Dissertation | 2 | RP-06 | J. Phil. Logic; Ling. & Phil.; arXiv cs.LO |
| RP-02 | Self-Reference & Limits | Thesis | 1 | (none) | ACM Comp. Surveys; Studia Logica; arXiv cs.LO |
| RP-03 | Rhizome vs. Hierarchy | Thesis | 2 | RP-05 | Org. Science; Comp. Math. Org. Theory; arXiv cs.MA |
| RP-04 | The Naming Problem | Paper | 1 | (none) | Synthese; JASIST; arXiv cs.PL |
| RP-05 | Latour's Network Ontology | Thesis | 2 | RP-03 | Soc. Studies of Science; ST&HV; arXiv cs.AI |
| RP-06 | Chomsky to Computation | Dissertation | 1 | RP-01 | J. Logic, Lang. & Info.; MSCS; arXiv cs.FL |
| RP-07 | Measurement Theory | Thesis | 3 | RP-02, RP-03 | Emp. Soft. Eng.; J. Sys. & Soft.; arXiv cs.SE |
| SYN-01 | Grand Unified Semantics | Dissertation | 3 | RP-01, RP-06 | (venue TBD by Phase 3) |
| SYN-02 | Governance Impossibility | Thesis | 3 | RP-02, RP-03, RP-05, RP-07 | (venue TBD by Phase 3) |
| SYN-03 | Naming as Infrastructure | Paper | 2 | RP-04, RP-03, RP-05 | (venue TBD by Phase 2) |
| SYN-04 | Flat Ontology of Measurement | Paper | 3 | RP-05, RP-07 | (venue TBD by Phase 3) |
| SYN-05 | Architecture of Meaning | Dissertation | 4 | RP-01, RP-02, RP-04, RP-06 | (venue TBD by Phase 4) |
| CAP | Capstone Dissertation | Dissertation | 4 | All | (internal SGO defense) |

### Table 2: ORGANVM System Connections

| Work | Primary ORGANVM Connection | Organ(s) Affected |
|------|---------------------------|-------------------|
| RP-01 | Ontological layer design (organvm-ontologia), entity identification across representations | I, META |
| RP-02 | Governance architecture limits, syntactic vs. semantic automation boundary | IV, META |
| RP-03 | Eight-organ topology optimization, hierarchical vs. rhizomatic design decisions | IV, META |
| RP-04 | Double-hyphen naming convention, registry namespace, seed.yaml terminology | ALL |
| RP-05 | Human-AI collaboration model, MCP as OPP, system prompts as immutable mobiles | IV, META |
| RP-06 | Grammar hierarchy of governance rules, automation decidability boundaries | IV, META |
| RP-07 | Promotion state machine validation, metrics module calibration, omega scorecard | META |
| SYN-02 | Comprehensive governance design principles derived from formal limits | IV |
| SYN-03 | Naming governance policy design, namespace evolution strategy | ALL |
| SYN-05 | System-wide formalization strategy, knowledge architecture | I, META |

### Table 3: Research Question Inventory

| ID | RQ# | Question (Abbreviated) | Method |
|----|-----|------------------------|--------|
| RP-01 | RQ1 | Can Curry-Howard-Lambek unify meaning across logic, CS, NL? | Formal analysis |
| RP-01 | RQ2 | Is dynamic semantics more natural than truth-conditional as unifier? | Conceptual analysis |
| RP-01 | RQ3 | Can distributional semantics be reconciled with formal traditions? | Comparative analysis |
| RP-02 | RQ1 | What is the syntactic/semantic boundary for governance automation? | Formal analysis + case study |
| RP-02 | RQ2 | Can Willard's self-verifying theories apply to software governance? | Formal analysis |
| RP-02 | RQ3 | Does Curry-Howard extend to governance (policies = types)? | Formal analysis |
| RP-03 | RQ1 | Can rhizomaticity be formalized as a graph-theoretic measure? | Formal analysis |
| RP-03 | RQ2 | Is there a scale limit for rhizomatic organization? | Comparative case study |
| RP-03 | RQ3 | Can technology provide legibility without hierarchy? | Conceptual + empirical |
| RP-04 | RQ1 | Is there a universal theory of naming? | Comparative conceptual analysis |
| RP-04 | RQ2 | What is the optimal information density of a name? | Analytical modeling |
| RP-04 | RQ3 | How does the type-token distinction differ across domains? | Comparative analysis |
| RP-05 | RQ1 | Does ANT's symmetry principle work for human-AI collaboration? | Theoretical analysis |
| RP-05 | RQ2 | How should ANT handle constitutive opacity? | Critical extension |
| RP-05 | RQ3 | Is alignment a translation problem? | Theoretical reframing |
| RP-06 | RQ1 | What is the type-theoretic characterization of MCSL? | Formal proof |
| RP-06 | RQ2 | Do neural LMs learn type-theoretic structure? | Empirical analysis |
| RP-06 | RQ3 | Is Merge = Application? | Formal comparison |
| RP-07 | RQ1 | Is software quality a single latent variable? | Factor analysis |
| RP-07 | RQ2 | Does the promotion state machine satisfy Guttman properties? | Scalogram analysis |
| RP-07 | RQ3 | How to establish measurement invariance across tech stacks? | Multi-group CFA |

### Table 4: Article Corpus by Adventure

| Adventure | Seed Articles | Expansion Articles | Frontier Articles | Total |
|-----------|--------------|-------------------|-------------------|-------|
| 01: Semantics Bridge | 7 | 16 | 15 | 38 |
| 02: Self-Reference | 9 | 17 | 9 | 35 |
| 03: Rhizome vs. Hierarchy | 11 | 16 | 13 | 40 |
| 04: Naming Problem | 11 | 17 | 7 | 35 |
| 05: Latour's Network Ontology | 11 | 18+ | 23 | 52+ |
| 06: Chomsky to Computation | 17 | 19 | 8+ | 44 |
| 07: Measurement Theory | 5 | 16 | 13 | 34 |
| **Total** | **71** | **119** | **88** | **278+** |

### Table 5: SGO Tier Distribution

| Tier | Count | Works |
|------|-------|-------|
| Paper | 3 | RP-04, SYN-03, SYN-04 |
| Thesis | 5 | RP-02, RP-03, RP-05, RP-07, SYN-02 |
| Dissertation | 5 | RP-01, RP-06, SYN-01, SYN-05, Capstone |

---

## Methodological Note

This research program follows the SGO's purpose hierarchy: self-fulfillment (primary) -> promotion (secondary) -> proof of theoretical power (tertiary). The works are designed first to satisfy genuine intellectual curiosity about the formalization of knowledge, second to advance through the ORGANVM promotion state machine, and third to demonstrate that a self-sovereign academic institution can produce work of publishable quality.

All works participate in the ORGANVM data integrity rules: production data files (registry-v2.json, governance-rules.json, seed.yaml contracts) are never overwritten wholesale during research. Empirical analyses in RP-07 use copies or read-only access to production data.

The research atlas's grand arc -- WHAT IS KNOWLEDGE -> HOW DO HUMANS ORGANIZE -> HOW DO WE NAME THINGS -> HOW DO SYSTEMS NEST -> HOW DO IDEAS EVOLVE -> HOW DOES MEANING BECOME FORMAL -> HOW DO WE MEASURE ALL THIS -- is preserved as the organizing logic of the program, from Phase 1 (naming, limits, formalization) through Phase 4 (capstone synthesis).

---

## Appendix A: The Grand Arc (from Research Atlas)

```
WHAT IS KNOWLEDGE?        ->  RP-04, RP-01
HOW DO HUMANS ORGANIZE?   ->  RP-03, RP-05
HOW DO WE NAME THINGS?    ->  RP-04
HOW DO SYSTEMS NEST?      ->  RP-03
HOW DO IDEAS EVOLVE?      ->  RP-05
HOW DOES MEANING BECOME   ->  RP-01, RP-06
  FORMAL?
HOW DO WE MEASURE         ->  RP-07
  ALL THIS?
WHAT ARE THE LIMITS?      ->  RP-02
```

## Appendix B: Cross-Reference to Research Atlas Domains

| Atlas Domain | Primary Adventure | Supporting Adventures |
|-------------|-------------------|----------------------|
| I: Foundations of Knowledge & Science | RP-01, RP-04 | RP-02, RP-06 |
| II: Social Systems & Organization | RP-03, RP-05 | RP-07 |
| III: Naming, Meaning & Convention | RP-04 | RP-01, RP-06 |
| IV: Ecological & Systems Theory | RP-03 | RP-05 |
| V: Critical Philosophy & Design Movements | RP-05 | RP-03 |
| VI: Language, Logic & Formal Systems | RP-01, RP-06 | RP-02 |
| VII: Measurement & Assessment | RP-07 | RP-02 |

---

*Document generated 2026-03-20. Studium Generale ORGANVM, ORGAN-I (Theoria). Program status: CANDIDATE. Awaiting IRA panel review for advancement to PUBLIC_PROCESS.*
