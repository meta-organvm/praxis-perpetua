---
sgo_id: SGO-2026-RP-004
title: "The Deep Structure of Naming"
tier: Paper
status: LOCAL (first draft)
target_venues: [Synthese, JASIST, arXiv cs.PL]
dependencies: none
date: 2026-03-21
---

# The Deep Structure of Naming: Toward a Unified Theory Across Natural Language, Formal Systems, and Programming

## 1. Introduction

The act of naming is one of the most fundamental operations of cognition, language, and engineering. Before an entity can be classified, described, measured, or manipulated, it must be named. The naming act appears deceptively simple -- attach a label to a thing -- yet it conceals a web of philosophical, linguistic, and technical problems that have occupied thinkers from Plato to the designers of the Domain Name System. This paper argues that naming is not three separate problems wearing the same word, but a single structural problem that manifests differently across domains. To see the unity beneath the diversity, one must examine the deep structure that all naming shares: a reference relation between a sign and a referent, mediated (or not) by sense, constrained by scope, governed by convention, and subject to characteristic modes of failure.

The practical stakes are considerable. In software engineering, naming is routinely cited as one of the two hardest problems in computer science (alongside cache invalidation and off-by-one errors) [Karlton, attributed]. Poorly chosen names produce cascading failures: a misleading function name causes a misunderstanding that causes a bug that causes an outage. In the sciences, the Linnaean system of binomial nomenclature has endured for over 270 years precisely because it solves the naming problem well -- encoding hierarchical classification in the name itself, governed by international commissions, and decoupled from any single natural language through the use of Latin [Linnaeus, 1753]. In philosophy, the debate over how names refer -- whether by description, by causal chain, or by use -- remains one of the central unresolved problems of analytic philosophy, with consequences for metaphysics, epistemology, and the philosophy of mind [Kripke, 1980; Frege, 1892].

The theoretical stakes are equally significant. Naming sits at the intersection of three major intellectual traditions, each of which has developed sophisticated but largely independent accounts. The philosophical tradition, from Frege through Russell to Kripke and Wittgenstein, asks what the relationship is between a name and its referent -- whether names carry meaning beyond pointing, whether they are rigid or flexible, whether they describe or designate. The linguistic-scientific tradition, from Saussure through Peirce to modern taxonomy and controlled vocabularies, asks how names are organized into systems -- how naming conventions encode information, how nomenclatures balance expressiveness against usability, how authority structures govern the creation and evolution of names. The computational tradition, from early assembler mnemonics through structured programming to modern ontology engineering, asks how names can be made to work in machines that have no understanding of meaning -- how identifiers achieve uniqueness, how namespaces provide scope, how naming conventions serve as lightweight ontologies.

Despite their independent development, these three traditions converge on remarkably similar structures. All three recognize that the name-thing relation is neither simple nor direct. All three grapple with characteristic failure modes: reference failure (a name that points to nothing), collision (two names for the same thing or one name for two things), semantic drift (a name whose meaning changes over time), and governance problems (disputes over who has the authority to name). All three acknowledge that naming involves a fundamental tradeoff between the information a name carries and its cognitive or computational cost.

This paper addresses three research questions:

**RQ1:** Is there a universal theory of naming that subsumes Kripke's causal theory, Saussure's arbitrariness principle, and computing's namespace model, or are these irreducibly different accounts of different phenomena?

**RQ2:** What is the optimal information density of a name, and does the answer depend on system scale, domain, or lifecycle stage?

**RQ3:** How does the type-token distinction -- a philosophical concept originating with Peirce -- operationalize differently in natural language, formal systems, and programming, and what does this reveal about the nature of naming?

The paper proceeds as follows. Section 2 surveys the three traditions in detail. Section 3 identifies structural commonalities and differences through comparative analysis of the name-thing gap, information density, and the type-token distinction. Section 4 proposes a unification framework centered on the reference relation as a common structure, with convention and causation as the principal axes of variation. Section 5 draws implications for system design, using the ORGANVM double-hyphen naming convention as a case study in applied naming theory. Section 6 discusses open questions and limitations. Section 7 concludes.

The paper contributes: (a) a cross-domain taxonomy of naming failures showing structural analogues across philosophy, linguistics, and computing; (b) the "naming as compression" thesis, which frames every naming convention as a point on a universal expressiveness-usability tradeoff curve; and (c) a set of design principles for naming systems derived from the synthesis of all three traditions.

## 2. Three Traditions of Naming

### 2.1 The Philosophical Tradition

The philosophical tradition asks the most fundamental question about naming: what is the relationship between a name and the thing it names? Four major positions have emerged over 130 years of sustained argument.

#### 2.1.1 Frege's Sense/Reference Distinction

In his 1892 paper "Uber Sinn und Bedeutung," Gottlob Frege introduced a distinction that has structured every subsequent debate about naming. The *reference* (Bedeutung) of a name is the object it denotes; the *sense* (Sinn) is the "mode of presentation" -- the cognitive route by which a thinker grasps the referent [Frege, 1892]. Frege's motivating puzzle is elegant: the statement "Hesperus is Phosphorus" is informative, even surprising, while "Hesperus is Hesperus" is trivially true. Yet both statements are about the same object (the planet Venus). If the meaning of a name were simply its referent, the two statements would have the same meaning. Since they do not, names must carry something beyond reference -- namely, sense.

The implications for naming theory are profound. Two names can share a referent while differing in sense, and it is the sense that carries cognitive content. In Frege's framework, understanding a name is not merely knowing what it picks out, but grasping the particular way it picks it out. The morning star and the evening star present Venus under different aspects, and this aspectual difference is constitutive of meaning. Frege extended this analysis beyond proper names to definite descriptions ("the capital of Germany"), function expressions, and entire sentences, arguing that the sense of a sentence is the thought (Gedanke) it expresses and its reference is its truth-value.

Frege's distinction generates what might be called the *sense preservation principle*: substituting co-referential names can change the cognitive content of an expression. This principle has direct consequences for any naming system. Two database columns that point to the same underlying data -- say, `customer_id` and `account_holder_id` -- are not interchangeable if they present that data under different conceptual aspects. A naming convention that ignores sense distinctions collapses information that users rely on.

#### 2.1.2 Russell's Description Theory

Bertrand Russell radicalized Frege's approach by arguing that ordinary proper names are, in logical form, disguised definite descriptions [Russell, 1905]. On this view, "Aristotle" is not a logically simple name but abbreviates something like "the teacher of Alexander who wrote the Metaphysics." The reference of a name is determined by whatever object uniquely satisfies the associated descriptions. If no object satisfies them, the name fails to refer; if multiple objects satisfy them, the name is ambiguous.

Russell's theory has the virtue of explaining how we can meaningfully use names for entities we have never encountered -- we grasp the descriptions and use them to fix reference. It also explains reference failure: "the present King of France" fails to refer because no object satisfies the description. But the theory faces a deep problem that John Searle attempted to address with his *cluster theory*: speakers do not typically associate a single definite description with a name, but rather a loosely organized cluster of descriptions, any sufficient subset of which can fix reference [Searle, 1958]. The cluster theory softens Russell's approach but preserves its core commitment: names mean via descriptions.

#### 2.1.3 Kripke's Causal/Rigid Designator Theory

Saul Kripke's 1970 Princeton lectures, published as *Naming and Necessity* in 1980, overturned the Frege-Russell consensus. Kripke argued that proper names are *rigid designators* -- terms that designate the same object in every possible world where that object exists [Kripke, 1980]. "Aristotle" refers to Aristotle in every counterfactual scenario: even in a world where Aristotle never taught Alexander and never wrote the Metaphysics, "Aristotle" still picks out the same individual. Definite descriptions, by contrast, are generally non-rigid: "the teacher of Alexander" could have been someone else.

The modal argument is devastating for descriptivism. If the meaning of "Aristotle" were "the teacher of Alexander," then "Aristotle might not have taught Alexander" would be self-contradictory -- it would mean "the teacher of Alexander might not have taught Alexander." But the sentence is perfectly intelligible. Therefore, "Aristotle" does not mean "the teacher of Alexander" or any other description. Names and descriptions have different modal profiles, which proves they have different semantic functions.

In place of descriptions, Kripke proposed the *causal theory of reference*: a name acquires its referent through an *initial baptism* -- a naming event in which the name is fixed to an object, either by ostension (pointing) or by description used to fix (but not to give the meaning of) the name. The name is then transmitted through a community via a *causal chain* of communication: each speaker intends to use the name with the same reference as the person from whom they acquired it [Kripke, 1980]. Keith Donnellan developed a similar account independently, and Hilary Putnam extended the causal approach to natural kind terms like "water" and "gold," arguing that these terms rigidly designate the underlying nature (H2O, Au) rather than any surface description [Putnam, 1975].

The causal theory has a striking consequence: names can survive total changes in associated descriptions. We could discover that everything we believe about Aristotle is false -- that he was not Greek, not a philosopher, not a teacher -- and "Aristotle" would still refer to the same person. The name's referential function is secured by causal history, not by descriptive content. This robustness is both the theory's strength and its limitation. It explains the stability of reference but struggles with cases of reference-shifting: "Madagascar" originally designated a portion of the African mainland before Marco Polo's misapplication redirected it to the island [Kripke, 1980; Evans, 1973].

#### 2.1.4 Wittgenstein's Use Theory

Ludwig Wittgenstein's later philosophy, developed in *Philosophical Investigations* (1953), offers a fundamentally different approach. Rather than asking what names mean -- what semantic content they carry -- Wittgenstein asks what names *do*. The meaning of a word is its use in the language [Wittgenstein, 1953, section 43]. A name functions as part of a *language game* -- a form of life in which language and action are interwoven. The word "Water!" can be an order, an answer, a warning, or an exclamation depending on the game being played. There is no single "meaning" extractable from a name independently of its contexts of use.

For naming theory, Wittgenstein's contribution is the recognition that the same name can participate in different language games with different rules for success. A variable name in a for-loop, a column name in a database schema, and a class name in a public API are governed by different norms of clarity, stability, and scope. The question "is this a good name?" has no context-free answer; it depends on which game the name is playing. This insight is directly relevant to the design of naming conventions, which are, in Wittgensteinian terms, codified rules for particular language games.

### 2.2 The Scientific/Linguistic Tradition

The linguistic-scientific tradition takes names as given and asks how they are organized into systems. Where philosophy asks *what* a name means, this tradition asks *how* naming systems are structured and governed.

#### 2.2.1 Saussure's Signifier/Signified

Ferdinand de Saussure's *Course in General Linguistics* (1916) established the foundational framework. A linguistic sign consists of two components: the *signifier* (the sound-image, the written mark -- the plane of expression) and the *signified* (the concept -- the plane of content). The relationship between signifier and signified is *arbitrary*: there is no natural reason why the sequence of sounds /tri:/ should evoke the concept of a tree [Saussure, 1916]. This arbitrariness is both the power and the vulnerability of naming. It enables infinite productivity -- we can name anything, since the link between name and thing is conventional rather than natural -- but it requires social convention to maintain stability. Without shared agreement on what signs mean, communication collapses.

Saussure's second major insight is that signs acquire meaning not in isolation but through their position in a *system of differences*. The sign "tree" means what it means partly by virtue of what it is not -- not "bush," not "shrub," not "forest." Meaning is *differential* and *relational*: it arises from the system of contrasts within which a sign is embedded. This structural approach has direct implications for naming conventions. A naming scheme in which `controller`, `service`, and `repository` denote different architectural layers works because the terms contrast with each other. Introducing a fourth term (say, `handler`) that overlaps with an existing term degrades the entire system's informativeness.

#### 2.2.2 Peirce's Triadic Sign Model

Charles Sanders Peirce developed a competing semiotic framework that is in important respects richer than Saussure's. Where Saussure's model is *dyadic* (signifier/signified), Peirce's is *triadic*: a sign consists of a *sign vehicle* (the material form), a *referent* (the object it stands for), and an *interpretant* (the mental effect or understanding the sign produces in an interpreter) [Peirce, 1931-1958]. The interpretant introduces a crucial element absent from Saussure's framework: the role of the mind that processes the sign. The same sign vehicle can produce different interpretants in different interpreters, which means that naming is inherently perspectival -- a name does not carry fixed meaning but produces understanding relative to an interpreter's context and background.

Peirce also classified signs into three types based on the nature of their relation to their referents. *Icons* relate to their referents by resemblance (a portrait, a map, an onomatopoeic word). *Indices* relate to their referents by causal or existential connection (smoke as a sign of fire, a pointing finger, a pronoun). *Symbols* relate to their referents by convention (most words, mathematical symbols, traffic signs). Names are primarily symbols in Peirce's taxonomy -- their connection to referents is conventional rather than natural. But naming acts can also be indexical (pointing and saying "that is X") or even iconic (onomatopoeia, sound-symbolic naming, the way chemical structural formulas visually resemble molecular geometry).

#### 2.2.3 Nomenclature, Taxonomy, and Systematic Naming

The scientific tradition has developed the most elaborate formal naming systems in any domain. *Nomenclature* provides the general framework: a naming system consists of rules for forming terms within a domain, governing morphology (how name-parts combine), scope (what can be named), and governance (who decides) [Wikipedia, "Nomenclature"]. *Taxonomy* provides the hierarchical structure that names often encode. The Linnaean system of biological nomenclature is perhaps the most successful formal naming system ever devised: stable for over 270 years, internationally recognized, encoding hierarchical classification in the name itself (*Homo sapiens* = genus *Homo*, species *sapiens*), and governed by five international codes of nomenclature [Linnaeus, 1753].

*Systematic naming* takes the encoding principle further. IUPAC chemical nomenclature encodes the full molecular structure in the name: "2,4,6-trinitrotoluene" specifies the positions and types of substituent groups on a toluene ring. A systematic name is, in effect, a *lossless compression* of the thing named. The cost is human unreadability -- no one says "2,4,6-trinitrotoluene" in conversation; they say "TNT." This tension between systematic names and common names reveals a fundamental tradeoff that every naming system faces: *expressiveness* (encoding more information in the name) versus *usability* (keeping names short, memorable, and speakable). Formal naming systems push toward the expressiveness end; vernacular naming pushes toward usability. Every naming convention is a point on this tradeoff curve.

*Controlled vocabularies* and *thesauri* address a different aspect of the naming problem: the many-to-many relationship between names and concepts. A controlled vocabulary is a predefined set of preferred terms for indexing and retrieval, mandating the use of canonical terms and managing synonymy through authority control [Wikipedia, "Controlled vocabulary"]. A thesaurus extends this by mapping semantic relationships: broader and narrower terms, synonyms, and related terms [Wikipedia, "Thesaurus (information retrieval)"]. These systems acknowledge that natural naming is messy -- synonyms proliferate, meanings drift, the same word means different things in different contexts -- and impose order through governance and standardization. The cost is flexibility; the gain is precision and interoperability.

### 2.3 The Computational Tradition

The computational tradition inherits problems from both philosophy and linguistics but faces a unique constraint: names must be processed by machines that have no understanding of meaning. All semantic content in a name is for human readers; the machine cares only about uniqueness and scope.

#### 2.3.1 Identifiers, Variables, and Naming Conventions

The *identifier* is the atomic unit of computational naming -- a character sequence that labels the identity of a unique object or class of objects [Wikipedia, "Identifier (computer science)"]. The distinction between a "name" and an "identifier" is connotatively significant even where denotationally synonymous: "Jamie Zawinski" is a name; "Netscape employee number 20" is an identifier. Both refer to the same individual, but they participate in different naming games with different norms [Wikipedia, "Identifier (computer science)"].

*Naming conventions* -- camelCase, snake_case, PascalCase, Hungarian notation, BEM (Block-Element-Modifier) -- are attempts to encode semantic information in the identifier's surface form. They are lightweight, convention-based ontologies. The identifier `getUserName()` encodes entity (User), attribute (Name), and operation (get) in a single token. Hungarian notation (e.g., `strName`, `nCount`) prefixes type information to the identifier, making the type system visible in the name itself [Simonyi, 1999]. These conventions are notoriously contested -- "a matter of dogma" according to one survey [Wikipedia, "Naming convention (programming)"] -- which suggests that even in the most formal of domains, naming carries aesthetic and tribal significance beyond pure function.

#### 2.3.2 Namespaces and Hierarchical Scoping

*Namespaces* solve the uniqueness problem through hierarchical scoping. They are the engineering equivalent of taxonomic classification: `java.util.List` and `java.awt.List` can coexist because the namespace disambiguates [Wikipedia, "Namespace"]. The Domain Name System (DNS) is the global namespace for the internet, and it is instructive both as a success and a cautionary tale. DNS achieves global uniqueness through a hierarchical tree (`.com.example.www` read right-to-left), governed by ICANN and national registrars. Its success demonstrates that namespace governance scales; its controversies (domain squatting, trademark disputes, the new gTLD program) demonstrate that naming governance is always political.

Namespaces are, in philosophical terms, artificial context. Natural language resolves ambiguity through pragmatic context -- the word "bank" is disambiguated by whether the speaker is near a river or a financial institution. Formal systems cannot rely on pragmatic context because machines do not process it. Namespaces supply the disambiguation that natural context provides for free. The implication for system design is that investment in namespace architecture should be proportional to system scale: a solo script needs no namespaces; a hundred-repository workspace needs a rigorous namespace hierarchy.

#### 2.3.3 Ontologies and Information Architecture

*Ontologies* in information science go beyond naming to declare what names mean and how they relate. An ontology is "a way of showing the properties of a subject area and how they are related, by defining a set of terms and relational expressions that represent the entities in that area of concern" [Wikipedia, "Ontology (information science)"]. Where a naming convention says "use camelCase for methods," an ontology specifies the category structure, the property relationships, and the inference rules that names participate in. The Web Ontology Language (OWL), Resource Description Framework (RDF), and SKOS (Simple Knowledge Organization System) are standardized frameworks for expressing such ontologies in machine-readable form.

The connection between information-science ontology and philosophical ontology (Quine, Kripke) is more than etymological. Quine's criterion of ontological commitment holds that "to be is to be the value of a bound variable" -- that is, to name something in one's theory is to assert its existence [Quine, 1948]. Every information-science ontology is an ontological commitment in Quine's sense: to include a class `Customer` in a domain model is to assert that customers exist as a category in the domain. Naming is never ontologically innocent.

## 3. Structural Comparison

### 3.1 The Name-Thing Gap: Five Failure Modes Across Domains

When naming fails, a gap opens between the name and what it was supposed to name. This paper identifies five structural failure modes that recur across all three traditions.

**Reference failure** is the most basic: a name that points to nothing. In philosophy, Frege's "empty names" illustrate the problem -- "the largest integer" has sense but no reference; fictional names like "Sherlock Holmes" refer within a story-world but not in the actual world [Frege, 1892]. In computing, the structural analogue is the null pointer exception, the dangling reference, the undefined variable. A `NullPointerException` is Frege's puzzle made operational: the program presupposed that a name had a referent, but it did not. The descriptivist says empty names still mean something (they express a concept even if nothing satisfies it); the direct reference theorist says they are, strictly speaking, meaningless. The computational engineer says they crash the program.

**Namespace collision** occurs when a single name maps to multiple referents within a scope. In natural language, this is homonymy: "bank" (financial institution) versus "bank" (river edge), resolved by pragmatic context. In computing, the analogue is name collision across modules, libraries, or package registries. The JavaScript ecosystem's flat `npm` namespace has produced name-squatting, trademark disputes, and the infamous `left-pad` incident of 2016, in which the removal of a single trivially-named package broke thousands of downstream projects. Namespace collision reveals that uniqueness is not a property of names in isolation but of names within scopes, and that scope governance is a political as much as a technical problem.

**Semantic drift** occurs when a name's associated meaning changes over time while the name itself persists. In natural language, this is ubiquitous: "nice" once meant "foolish"; "computer" once meant a person who computes. In computing, semantic drift manifests as API names whose implementations have diverged from their original semantics: a function called `getUser()` that now also initializes a cache, a database column called `status` whose enumerated values have expanded beyond the original design. Semantic drift is insidious because machines cannot detect the discrepancy between name and behavior -- only human readers can, and only if they read carefully. The causal theory of reference predicts this phenomenon: the causal chain transmits the name, but the descriptions associated with it evolve independently.

**Abstraction mismatch** occurs when the same entity is represented by different names in different contexts. Kripke's puzzle about belief provides the philosophical archetype: Pierre believes "Londres est jolie" and "London is not pretty" without realizing these name the same city [Kripke, 1979]. In computing, the same entity routinely appears as `user_id` in the database, `userId` in the API, `uid` in the cache, and `person_identifier` in the analytics pipeline. Integration failures are often naming failures: two systems that cannot agree on what to call the same thing. Frege's sense/reference distinction illuminates the problem -- different names present the same referent under different aspects -- but does not resolve it, because the systems do not share each other's senses.

**Governance failure** occurs when there is no authoritative mechanism for resolving naming disputes. Biological nomenclature solved this problem through international commissions (the ICZN for zoology, the ICNafp for botany). Chemical nomenclature has IUPAC. Astronomical nomenclature has the IAU. Computing, by contrast, has fragmented governance: ICANN controls DNS; npm, PyPI, and crates.io each have their own rules for package naming; enterprise codebases often have no naming governance at all beyond inherited convention. Every naming system eventually requires a governance layer, and the design of that layer is always a social and political problem, not merely a technical one.

These five failure modes -- reference failure, collision, drift, mismatch, and governance failure -- constitute a cross-domain taxonomy of naming pathology. Their recurrence across philosophy, linguistics, and computing suggests that they are not domain-specific accidents but structural features of the name-thing relation itself. Any system that names things is susceptible to all five.

### 3.2 Information Density of Names

Every name occupies a position on a spectrum from maximally compressed (a single arbitrary character) to maximally expanded (a complete description of the referent). The variable name `x` carries almost no information; the IUPAC name "2,4,6-trinitromethylbenzene" encodes the complete molecular structure. Neither extreme is optimal in practice. The choice of where on the spectrum to place a name constitutes one of the most consequential design decisions in any naming system.

The information-density tradeoff has three dimensions. *Referential precision* measures how unambiguously a name picks out its referent: `x` is maximally ambiguous; a UUID is maximally precise. *Descriptive richness* measures how much the name reveals about the properties of the referent: `auth` says something about the module's function; `b7e3f` says nothing. *Cognitive cost* measures the mental effort required to read, remember, and use the name: short common words have low cost; systematic chemical names have prohibitive cost.

These three dimensions are in tension. Increasing referential precision (longer names, more qualifiers, namespace prefixes) increases cognitive cost. Increasing descriptive richness (encoding properties in the name) risks becoming outdated as the referent evolves (semantic drift). Decreasing cognitive cost (shorter, simpler names) sacrifices both precision and richness. The tradeoff is not merely aesthetic; it has measurable consequences for code comprehension, error rates, and maintenance costs in software engineering, and for retrieval precision and recall in information science.

The Linnaean system achieves a notable balance. The binomial *Homo sapiens* is short enough to remember and use, descriptively rich enough to encode genus membership, referentially precise enough to identify a unique species, and stable enough (via Latin and governance) to resist drift. The double-hyphen convention in the ORGANVM system (`sema-metra--alchemica-mundi`) aims for a similar balance: word-level hyphens preserve readability, while the double-hyphen encodes a structural distinction (function versus descriptor) that a single naming level would collapse.

### 3.3 The Type-Token Distinction Across Domains

The type-token distinction, originating with Peirce, differentiates between a *type* (an abstract class) and its *tokens* (concrete instances) [Peirce, 1931-1958]. The sentence "A rose is a rose is a rose" contains three word types but eight word tokens. This distinction is not merely taxonomic; it is foundational to how names function across all three traditions.

In philosophy of language, the type-token distinction structures the debate about what names refer to. A name-type (the string "Aristotle") has potentially unlimited tokens (every utterance or inscription of "Aristotle"). The philosophical question is whether the name-type has a meaning or only its tokens do. The use theory suggests the latter: each token-use of "Aristotle" participates in a particular language game, and meaning is constituted by the game, not by the type. The causal theory suggests the former: the name-type "Aristotle" is linked to a specific individual by a causal chain, and every token inherits that link.

In linguistics, the type-token distinction structures the study of lexical frequency, productivity, and creativity. A language's vocabulary is a set of word-types; a corpus is a collection of word-tokens. Hapax legomena (words that occur only once in a corpus) are types with a single token, and their frequency follows Zipf's law. For naming, the distinction is crucial: a naming convention is a set of name-type patterns (e.g., "use camelCase for variable names"); any particular name conforming to that pattern is a token of the convention.

In computing, the type-token distinction is operationalized with unusual precision. A class is a type; an object is a token. A schema is a type; a record is a token. A generic type (`List<T>`) is a type-constructor; a concrete type (`List<String>`) is a type; a specific list instance is a token. Programming languages enforce the type-token distinction through type systems, and naming conventions reflect it: PascalCase for type names (`UserService`), camelCase for instance names (`userService`), SCREAMING_SNAKE_CASE for constants (type-level values). The visual distinction between type-names and token-names is a form of lightweight static analysis: it catches category errors at read time, before the type checker or the runtime has a chance to report them.

What the cross-domain comparison reveals is that the type-token distinction is not merely a classification tool but a *design constraint* on naming systems. Any naming convention that fails to distinguish types from tokens -- that uses the same naming pattern for classes and instances, for schemas and records, for conventions and their applications -- invites confusion between levels of abstraction. The philosophical insight (types and tokens are ontologically distinct) becomes a practical principle (name them differently).

## 4. Toward Unification

### 4.1 Common Structure: The Reference Relation

Beneath the terminological differences, all three traditions describe the same fundamental structure: a *reference relation* between a sign (name, identifier, signifier) and a referent (object, entity, signified), established and maintained by some combination of convention, causation, and use. The traditions differ not in what they describe but in which aspects of this structure they foreground.

The philosophical tradition foregrounds the *metaphysics* of the reference relation: is it mediated by sense (Frege), constituted by description (Russell), fixed by causal history (Kripke), or enacted by use (Wittgenstein)? The linguistic-scientific tradition foregrounds the *systematics* of the reference relation: how are reference relations organized into nomenclatures, taxonomies, and controlled vocabularies? The computational tradition foregrounds the *engineering* of the reference relation: how are reference relations implemented, scoped, governed, and made to survive in large-scale distributed systems?

These are not competing accounts of different phenomena. They are complementary perspectives on the same phenomenon, each illuminating aspects that the others leave in shadow. Kripke's causal theory explains why names can survive radical redescription -- but it has nothing to say about how naming conventions should be designed. Saussure's principle of arbitrariness explains why any name can in principle name anything -- but it does not address how names acquire particular referents in practice. Computing's namespace model solves the uniqueness problem at scale -- but it takes for granted the philosophical question of what it means for a name to refer.

A unified theory of naming, if one is possible, would need to incorporate all three perspectives: the metaphysics of reference, the systematics of naming organization, and the engineering of naming at scale. The present paper does not claim to provide such a theory but to demonstrate that one is needed and to identify the structural commonalities that any such theory would have to account for.

### 4.2 Where Traditions Diverge: Social vs. Formal Naming

The most significant divergence between traditions concerns the role of social processes in naming. In philosophy and linguistics, naming is irreducibly social. A name works because a community agrees (tacitly or explicitly) on what it refers to. Kripke's causal chain is a social chain -- the name is transmitted from speaker to speaker, each intending to preserve the reference established by their predecessors. Saussure's arbitrariness principle entails that naming conventions are social conventions: they hold because a community upholds them, and they change when a community changes them. Wittgenstein's language games are social practices, and meaning is constituted by participation in those practices.

In computing, naming appears to escape the social. A variable name works not because a community agrees on its reference but because a compiler or interpreter binds it to a memory address. The reference relation is implemented mechanically: assignment statements, symbol tables, pointer dereferencing. An identifier in a running program refers to whatever the runtime says it refers to, regardless of what any human community thinks.

But this apparent escape is illusory. The *mechanical* reference relation (identifier to memory address) is established by code that was written by humans following *social* naming conventions. The name `getUserName` refers mechanically to a function at a particular address, but its *communicative* function -- telling a human reader what the function does -- depends on social conventions about English word meanings, camelCase formatting, and the get/set idiom. When a programmer encounters `getUserName`, they bring to bear the same kind of interpretive apparatus that a natural-language speaker brings to "the morning star": a mode of presentation, a sense, a set of expectations derived from convention and context. The computational tradition has not eliminated the social dimension of naming; it has *layered* a mechanical reference relation on top of it.

This layering is the key structural difference between computational and non-computational naming. In natural language, there is one reference relation (social/conventional). In computing, there are two: a mechanical reference relation (managed by the runtime) and a communicative reference relation (managed by human convention). The two can diverge, and when they do, the result is a semantic-drift bug: the name mechanically refers to one thing while communicatively suggesting another. The dual-reference structure of computational naming explains why naming in code is both easier (the mechanical layer ensures referential success) and harder (the communicative layer requires all the social coordination that natural-language naming requires, plus compatibility with the mechanical layer).

### 4.3 The Role of Convention vs. Causation

The philosophical debate between descriptivism and causal theory maps onto a broader structural question: is the name-thing relation sustained by *convention* (ongoing agreement about what the name means) or by *causation* (a historical chain linking the name to an initial baptism event)?

Saussure's answer is unequivocally conventionalist: the sign-referent link is arbitrary and maintained by social agreement. Kripke's answer is causal: the name-referent link is established by a baptism event and transmitted by a causal chain. Wittgenstein's answer resists both: meaning is constituted by patterns of use that are neither purely conventional (they are not rules one could write down exhaustively) nor purely causal (they are not mechanically transmitted but actively sustained).

In practice, most naming systems rely on both convention and causation. Scientific nomenclature is conventional (the rules are agreed upon by committees) but once a name is established, it functions as a rigid designator in Kripke's sense -- *Homo sapiens* picks out the same species across all possible contexts, regardless of changes in the descriptions associated with it. Software naming conventions are conventional (snake_case vs. camelCase is arbitrary), but individual names within a codebase function causally: `getUserName` was "baptized" at a particular commit, and subsequent uses inherit that reference through a causal chain of code reading and modification.

The convention/causation axis reveals a structural principle: *naming systems that rely solely on convention are vulnerable to drift, while systems that rely solely on causation are vulnerable to rigidity*. Pure convention allows names to evolve flexibly but provides no anchor against arbitrary change. Pure causation preserves reference stability but provides no mechanism for controlled evolution. The most successful naming systems -- Linnaean taxonomy, DNS, well-maintained codebases -- combine both: a conventional framework (the naming rules) with causal stability (once baptized, a name persists).

### 4.4 Names as Boundary Objects

Bruno Latour's concept of *boundary objects* -- entities that inhabit several intersecting social worlds and satisfy the informational requirements of each [Star and Griesemer, 1989] -- provides a framework for understanding why names are simultaneously so important and so difficult. A name is a paradigmatic boundary object: it exists at the intersection of the naming system (the nomenclature, the convention, the namespace), the community of users (who bring different backgrounds, expectations, and language games), and the referent itself (which may change, be redescribed, or turn out to be different from what was expected).

As boundary objects, names must be *plastic enough* to adapt to different contexts of use while being *robust enough* to maintain identity across contexts. The species name *Drosophila melanogaster* works as a boundary object because it is precise enough for genetics laboratories, recognizable enough for textbook authors, and stable enough for regulatory agencies -- while all three communities may associate very different descriptions and concerns with the same name. A well-designed namespace serves the same boundary function: `org.apache.commons.lang3.StringUtils` means something specific to a Java programmer, something different to a build tool, and something different again to a dependency auditor -- yet all three uses converge on the same referent.

The boundary-object perspective illuminates why naming disputes are so intractable: different communities need different things from the same name, and optimizing for one community's needs may degrade the name's usefulness for another. The governance problem of naming is, at bottom, a problem of managing boundary objects across communities with divergent interests.

## 5. Implications for System Design

### 5.1 Design Principles Derived from Naming Theory

The synthesis of philosophical, linguistic, and computational naming theory yields seven design principles for naming systems:

1. **Ontological commitment.** Every naming decision is an ontological commitment. To name a directory `models/` is to assert that there exists a category called "models" and that the contents belong to it. Naming is architecture, not decoration. System designers should treat naming decisions with the same rigor they apply to API design or schema definition.

2. **Sense preservation.** Two names that point to the same referent are not interchangeable if they present different modes of access (Frege). `customer_id` and `account_holder_id` may resolve to the same database row, but they imply different conceptual frames. A naming convention should preserve sense distinctions even when reference is shared. Aliases are dangerous precisely because they create the illusion that two things are different when they are the same, or vice versa.

3. **Namespace proportionality.** Investment in namespace architecture should be proportional to system scale. A solo script needs no namespaces. A hundred-repository enterprise system needs a rigorous namespace hierarchy. Under-investing in namespaces leads to collisions; over-investing leads to name-paths so long that they become unreadable and defeat the purpose of naming.

4. **Controlled vocabulary discipline.** The thesaurus model -- preferred terms, synonyms, broader/narrower relationships -- is directly applicable to system design. A project glossary that maps canonical terms to their synonyms and specifies which terms are preferred prevents the slow accumulation of inconsistent naming. Seed contracts that declare domain terminology are a form of controlled vocabulary.

5. **Type-token distinction.** A naming convention that visually distinguishes types from tokens (PascalCase for types, camelCase for instances, SCREAMING_SNAKE_CASE for constants) operationalizes a philosophical distinction in a way that catches category errors at read time. Confusing a class name with an instance name produces bugs invisible to type checkers but obvious to careful human readers.

6. **Governance proportionality.** Every naming system eventually requires governance: rules about who can create names, what form names take, and how disputes are resolved. The governance structure should be proportional to the system's complexity and the number of independent naming agents. A solo developer needs only self-consistency. A multi-team organization needs naming committees, style guides, and automated linting.

7. **Language-game specification.** A name that is clear in one context (a Git branch called `fix/auth-redirect`) may be opaque in another (a Jira ticket, a changelog entry, a metric label). When designing naming conventions, specify the language game: where will this name appear, who will read it, and what do they need to understand from the name alone? Different games may require different naming conventions for the same entities.

### 5.2 The Double-Hyphen Convention as Applied Naming Ontology

The ORGANVM project employs a naming convention that illustrates several of these principles in practice. The *double-hyphen convention* uses single hyphens to separate words within a semantic unit and double hyphens to separate the functional role from the descriptive content: `sema-metra--alchemica-mundi` parses as "sema-metra" (the engine that measures signs) functioning as "alchemica-mundi" (alchemy of the world). The double hyphen is a syntactic device that encodes a structural distinction -- function vs. descriptor -- in the name's surface form.

Analyzed through the lens of naming theory, the convention exhibits several notable properties. First, it is a *micro-nomenclature*: a small formal system with explicit rules for forming names, analogous to Linnaean binomials or IUPAC prefixes. Second, the double-hyphen separator encodes *type-level information* (the functional category) alongside *token-level information* (the specific descriptor), operationalizing the type-token distinction in a domain-specific way. Third, the question of whether the functional part ("sema-metra") is a rigid designator or a description is genuinely open: if it rigidly designates this specific engine across all possible evolutions, the name survives refactoring; if it describes whatever engine measures signs, the name may need to change if the engine's function shifts.

The convention also illustrates the governance principle. In a single-developer system, the convention is self-enforced. As the system scales and multiple agents (human or automated) create names, governance mechanisms become necessary: validation rules in CI pipelines, naming guidelines in contribution documentation, and registry entries that canonicalize names and prevent drift.

### 5.3 When Naming Conventions Fail

Naming conventions fail in predictable ways, each corresponding to one of the five failure modes identified in Section 3.1. Conventions produce *reference failures* when names are chosen before their referents are well-understood (a module named `utils` or `misc` that accumulates unrelated functionality). They produce *collisions* when namespace hierarchies are too flat or when naming rules are ambiguous. They produce *semantic drift* when implementations evolve but names do not (`getUser()` that now also manages sessions). They produce *abstraction mismatches* when different subsystems use different conventions for the same domain concepts. And they produce *governance failures* when no one has the authority -- or the tooling -- to enforce naming consistency across a growing codebase.

The recurring lesson is that naming conventions are necessary but insufficient. A naming convention provides the *rules* for a language game, but rules alone do not ensure good play. Enforcement (linters, code review, automated checks), education (onboarding documentation, style guides), and governance (clear authority over naming decisions) are all required to maintain naming quality over time.

## 6. Discussion and Open Questions

This paper has argued for a structural unity beneath the three traditions of naming theory, centered on the reference relation and its characteristic failure modes. Several questions remain open.

**The possibility of formal unification.** The structural parallels identified in this paper -- between reference failure and null pointers, between rigid designation and identifier binding, between controlled vocabularies and type systems -- may reflect genuine isomorphism or surface analogy. Demonstrating genuine isomorphism would require formalizing the reference relation in a framework general enough to encompass Kripke's possible-world semantics, Saussure's differential structures, and computational namespace theory. Whether such a framework is achievable, or even desirable, remains unclear. Category theory, with its emphasis on structure-preserving mappings between domains, is a candidate formalism, but the social and pragmatic dimensions of naming may resist formalization.

**Optimal information density.** The tradeoff between expressiveness and usability has been described qualitatively, but a quantitative model remains elusive. Information-theoretic approaches might formalize the tradeoff: a name's information content can be measured in bits, and its cognitive cost can be approximated by length, frequency, and morphological complexity. But the relevant information depends on context (the language game), and cognitive cost varies across populations (expert vs. novice readers). An adequate model would need to be parameterized by context and audience.

**Naming in the era of AI code generation.** Large language models trained on vast codebases develop implicit naming conventions derived from statistical patterns across millions of repositories. When an LLM generates code, its names reflect this statistical consensus. This raises novel questions: Is LLM-generated naming a new form of governance -- governance by corpus rather than by committee? Does it stabilize naming conventions (by converging on frequent patterns) or degrade them (by averaging over inconsistent practices)? Does the LLM's inability to access causal chains of reference -- it has no baptism events, only token co-occurrences -- produce names that are semantically hollow despite being syntactically conventional?

**Naming and identity.** The naming problem is, at its deepest, an identity problem. In philosophy, naming is tied to personal identity: is the Ship of Theseus still the Ship of Theseus after every plank has been replaced? In computing, naming is tied to entity identity: is the refactored `AuthService` still the same service after its internals have been completely rewritten? The parallel suggests that a fully adequate theory of naming would need to incorporate a theory of identity -- and the problem of identity across time is one of the oldest unsolved problems in metaphysics.

**Self-referential naming and incompleteness.** Self-reference in naming produces paradoxes (the liar paradox, Russell's paradox) and impossibility results (Godel's incompleteness theorems, the halting problem). Computing has partial solutions -- reflection APIs, metaclasses, homoiconic languages -- but no general theory. Whether there exists a naming analogue to Godel's incompleteness -- a proof that no naming system can consistently name all of its own parts -- is an intriguing open question that connects the naming problem to the foundations of mathematics and computation.

**The boundary between rigid designation and description in evolving systems.** Kripke's distinction between rigid designators and descriptions is crisp in modal logic but blurry in practice. In an evolving codebase, a module name begins as a description (it names the module that does X) and gradually becomes a rigid designator (it names this module regardless of what it does). The transition is not a discrete event but a social process: as more code depends on the name, the cost of renaming increases, and the name becomes rigid not by philosophical necessity but by engineering inertia. A theory of naming that could model this transition -- from descriptive flexibility to rigid lock-in -- would illuminate both philosophical debates and practical engineering decisions about when and how to rename.

## 7. Conclusion

Naming is the most basic act of intellectual organization. Before an entity can be classified, described, measured, or computed upon, it must be named. This paper has surveyed three major traditions of naming theory -- philosophical (Frege, Russell, Kripke, Wittgenstein), linguistic-scientific (Saussure, Peirce, Linnaeus, controlled vocabularies), and computational (identifiers, namespaces, ontologies) -- and argued that beneath their terminological and methodological differences, they describe the same fundamental structure: a reference relation between sign and referent, established by some combination of convention and causation, organized into systems of contrasts and hierarchies, and subject to five characteristic failure modes (reference failure, collision, drift, mismatch, and governance failure).

The paper has proposed the "naming as compression" thesis: every name compresses a complex entity into a manipulable token, and every naming convention represents a point on a universal tradeoff curve between expressiveness and usability. It has identified seven design principles for naming systems derived from the cross-domain synthesis and illustrated their application through analysis of the ORGANVM double-hyphen convention as an applied micro-nomenclature.

The central finding is that the naming problem is genuinely unified across domains, but the unification is structural rather than theoretical. Philosophy, linguistics, and computing face the same structural challenges (ambiguity, drift, collision, governance) and converge on similar solutions (hierarchical scoping, controlled vocabularies, type-token discipline, governance bodies), but they arrive at these solutions from different starting points and embed them in different theoretical frameworks. Whether these structural parallels can be elevated to a genuine unified theory remains an open question -- one that would require formalizing the reference relation in a framework capacious enough to encompass possible-world semantics, differential semiotics, and namespace engineering.

What is clear is that naming deserves more theoretical attention than it typically receives. In philosophy, naming is a central topic; in linguistics and information science, it is well-studied; but in software engineering -- where naming decisions are made thousands of times a day and their consequences compound over years -- naming is treated as a craft skill rather than a subject of systematic inquiry. The traditions surveyed here offer resources for elevating naming from craft to discipline: from an art learned by imitation to a practice grounded in principles. The deep structure of naming, once made visible, reveals that every naming decision -- from christening a child to declaring a variable -- participates in the same ancient, difficult, and consequential activity: the attempt to fix a sign to a thing and make it hold.

## References

### Primary Texts

Donnellan, K. (1970). "Proper Names and Identifying Descriptions." *Synthese*, 21(3-4), 335-358.

Evans, G. (1973). "The Causal Theory of Names." *Proceedings of the Aristotelian Society*, Supplementary Volumes, 47, 187-208.

Frege, G. (1892). "Uber Sinn und Bedeutung." *Zeitschrift fur Philosophie und philosophische Kritik*, 100, 25-50. [Trans. as "On Sense and Reference."]

Kripke, S. (1979). "A Puzzle about Belief." In A. Margalit (ed.), *Meaning and Use*. Dordrecht: Reidel, 239-283.

Kripke, S. (1980). *Naming and Necessity*. Cambridge, MA: Harvard University Press. [Originally published in D. Davidson and G. Harman (eds.), *Semantics of Natural Language*, 1972.]

Linnaeus, C. (1753). *Species Plantarum*. Stockholm: Salvius.

Mill, J.S. (1843). *A System of Logic*. London: John W. Parker.

Ogden, C.K. and Richards, I.A. (1923). *The Meaning of Meaning*. London: Kegan Paul.

Peirce, C.S. (1931-1958). *Collected Papers of Charles Sanders Peirce*. C. Hartshorne, P. Weiss, and A.W. Burks (eds.). Cambridge, MA: Harvard University Press.

Putnam, H. (1975). "The Meaning of 'Meaning'." In *Mind, Language and Reality: Philosophical Papers, Vol. 2*. Cambridge: Cambridge University Press, 215-271.

Quine, W.V.O. (1948). "On What There Is." *Review of Metaphysics*, 2(5), 21-38.

Russell, B. (1905). "On Denoting." *Mind*, 14(56), 479-493.

Saussure, F. de (1916). *Cours de linguistique generale*. C. Bally and A. Sechehaye (eds.). Paris: Payot. [Trans. as *Course in General Linguistics*, 1959.]

Searle, J. (1958). "Proper Names." *Mind*, 67(266), 166-173.

Simonyi, C. (1999). "Hungarian Notation." MSDN Library, Microsoft Corporation.

Star, S.L. and Griesemer, J.R. (1989). "Institutional Ecology, 'Translations' and Boundary Objects." *Social Studies of Science*, 19(3), 387-420.

Wittgenstein, L. (1953). *Philosophical Investigations*. G.E.M. Anscombe (trans.). Oxford: Blackwell.

### Wikipedia Articles Consulted

"Causal theory of reference." Wikipedia. Accessed 2026-03-20.

"Controlled vocabulary." Wikipedia. Accessed 2026-03-20.

"Descriptivist theory of names." Wikipedia. Accessed 2026-03-20.

"Direct reference theory." Wikipedia. Accessed 2026-03-20.

"Ferdinand de Saussure." Wikipedia. Accessed 2026-03-20.

"Gottlob Frege." Wikipedia. Accessed 2026-03-20.

"Identifier (computer science)." Wikipedia. Accessed 2026-03-20.

"Language game (philosophy)." Wikipedia. Accessed 2026-03-20.

"Meaning (philosophy)." Wikipedia. Accessed 2026-03-20.

"Naming and Necessity." Wikipedia. Accessed 2026-03-20.

"Naming convention (programming)." Wikipedia. Accessed 2026-03-20.

"Namespace." Wikipedia. Accessed 2026-03-20.

"Natural kind." Wikipedia. Accessed 2026-03-20.

"Nomenclature." Wikipedia. Accessed 2026-03-20.

"Ontology (information science)." Wikipedia. Accessed 2026-03-20.

"Philosophy of language." Wikipedia. Accessed 2026-03-20.

"Proper name (philosophy)." Wikipedia. Accessed 2026-03-20.

"Rigid designator." Wikipedia. Accessed 2026-03-20.

"Saul Kripke." Wikipedia. Accessed 2026-03-20.

"Scientific classification." Wikipedia. Accessed 2026-03-20.

"Semiotic triangle." Wikipedia. Accessed 2026-03-20.

"Semiotics." Wikipedia. Accessed 2026-03-20.

"Sense and reference." Wikipedia. Accessed 2026-03-20.

"Sign (semiotics)." Wikipedia. Accessed 2026-03-20.

"Signifier and signified." Wikipedia. Accessed 2026-03-20.

"Symbol (formal)." Wikipedia. Accessed 2026-03-20.

"Systematic name." Wikipedia. Accessed 2026-03-20.

"Taxonomy." Wikipedia. Accessed 2026-03-20.

"Thesaurus (information retrieval)." Wikipedia. Accessed 2026-03-20.

"Type-token distinction." Wikipedia. Accessed 2026-03-20.

"Typology." Wikipedia. Accessed 2026-03-20.
