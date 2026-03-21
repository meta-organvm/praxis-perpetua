# Adventure 4: The Naming Problem

## Central Question

What is the deep structure of naming across natural language, formal systems, and programming? Is there a unified theory of how names work -- or do philosophy, linguistics, and computing each solve fundamentally different problems under the same word?

---

## Seed Articles

### Naming Convention (programming)
A naming convention is a set of rules for choosing character sequences for identifiers (variables, types, functions, entities) in source code and documentation. The goals are readability, reduced cognitive load during code review, and enabling automated quality tools. Convention choice is notoriously contested -- "a matter of dogma" -- suggesting that even in the most formal of domains, naming carries aesthetic and tribal weight beyond pure function.

### Systematic Name
A systematic name is assigned via a deterministic procedure to one unique entity within a population. Complexity ranges from simple prefix/number schemes to full structural encodings (as in IUPAC chemical nomenclature). Systematic names often coexist uneasily with earlier common names -- chemists still say "water" rather than "dihydrogen monoxide." This dual naming reveals a persistent tension: human cognition prefers short, familiar, contextual names; formal systems demand unambiguous, compositional ones.

### Nomenclature
A system of names or rules for forming names within a field. The key insight: naming is an aspect of everyday taxonomy -- people distinguish, identify, name, and classify the objects of experience as a single cognitive act. Nomenclature connects to theoretical linguistics (names as nouns embedded in language structure) and philosophy of language (the relationship between word-meanings and experience). The five codes of biological nomenclature are the most elaborated formal naming systems in science.

### Naming Convention (general)
Conventions differ in intent: to encode useful information (Manhattan's numbered streets), to show relationships (family naming), or to ensure uniqueness within a scope. The general article reveals the universality of the naming problem -- every human domain, from geography to kinship to bureaucracy, develops naming conventions that balance information density against cognitive accessibility.

### Philosophy of Language
The philosophical study of the relationship between language, its users, and the world. Investigates meaning, reference, intentionality, the constitution of sentences, concepts, learning, and thought. The "linguistic turn" (Frege, Russell, Wittgenstein, the Vienna Circle, Quine) made language the central problem of philosophy. For our purposes: the philosophy of language is where the naming problem gets its deepest theoretical treatment.

### Meaning (philosophy)
Meaning is "a relationship between two sorts of things: signs and the kinds of things they intend, express, or signify." The major theories: psychological (thought, intention), logical (intension/extension, sense/reference), communicative (message, information), truth-conditional, and use-based. Each theory implies a different account of how names mean -- whether a name carries its meaning intrinsically, by convention, by causal history, or by its role in a language game.

### Communication
The transmission of information. Models posit a source, coding system, message, channel, receiver, and decoding. Names are part of the coding system -- they are the compressed tokens that allow sender and receiver to coordinate reference. The breakdown modes of communication (noise, ambiguity, context mismatch) directly parallel the failure modes of naming.

### Paradigm
A distinct set of concepts or thought patterns within a field. Relevant because naming conventions are paradigm-dependent: what counts as a good name shifts when the paradigm shifts. A variable named `i` is perfectly clear in a for-loop paradigm; it is opaque in a declarative-programming paradigm.

### Taxonomy
The practice of developing classification schemes and allocating things to classes. A taxonomy organizes "taxa" (units) into hierarchies. Taxonomies are distinct from typologies: the former address empirical/objective characteristics, the latter abstract/subjective criteria. For naming: taxonomy provides the hierarchical structure that names often encode -- genus/species in biology, module/class/method in programming.

### Typology
Classification by abstract or subjective criteria. Whereas taxonomy asks "what is this thing empirically?", typology asks "what kind of thing is this conceptually?" In naming, typological thinking produces category names (design patterns, architectural styles) that group by family resemblance rather than strict inheritance.

### Scientific Classification
The specific application of taxonomy to organisms. Linnaean binomial nomenclature (Genus species) is perhaps the most successful formal naming system ever devised -- stable for 270 years, internationally recognized, encoding hierarchical relationship in the name itself. Its success criteria are instructive: uniqueness, compositionality, language-independence (Latin), and governance by international codes.

---

## Expansion Articles

### Naming and Necessity (Kripke, 1980)
One of the most important philosophical works of the 20th century. Three lectures arguing that proper names are "rigid designators" -- they pick out the same object in every possible world where that object exists. This directly opposes the descriptivist view that names are shorthand for bundles of descriptions. Kripke's "initial baptism" model: a name is fixed to a referent in a naming event, then transmitted through a community via a causal chain. This has profound implications: names do not describe, they point. Their meaning is their referent, not any set of properties.

### Saul Kripke (1940-2022)
American analytic philosopher and logician. Central contributions: Kripke semantics for modal logic (possible worlds), rigid designators, the causal theory of reference, "Kripkenstein" (rule-following paradox). His work revived metaphysics and essentialism after logical positivism. The Kripkenstein paradox is particularly relevant: it asks how we can ever be sure that a name (or any symbol) means what we think it means, given that any finite set of uses is compatible with infinitely many interpretations.

### Sense and Reference (Frege, 1892)
Frege's foundational distinction: the reference (Bedeutung) of a name is the object it denotes; the sense (Sinn) is the mode of presentation. "Hesperus" and "Phosphorus" have the same reference (Venus) but different senses (the evening star vs. the morning star). This is "Frege's puzzle" -- why "Hesperus is Phosphorus" is informative while "Hesperus is Hesperus" is trivial, even though both are true. The puzzle reveals that names carry cognitive content beyond mere reference. In computing terms: two variables can point to the same memory address while having different semantic roles in the program.

### Gottlob Frege (1848-1925)
Father of analytic philosophy. Developed modern logic (Begriffsschrift), argued for two types of meaning (sense and reference), and championed descriptivism -- the view that names mean via associated descriptions. His work is the origin point for nearly every subsequent debate about how names work.

### Proper Name (philosophy)
Mill's common-sense view (1843): a proper name shows what thing we are talking about but tells nothing about it. Frege's objection: names can refer to nonexistent entities without becoming meaningless, and co-referential names can differ in cognitive content. Russell's descriptivism: "Aristotle" means "the teacher of Alexander the Great." Kripke and Donnellan's causal-historical theory: names are fixed by baptism events and transmitted through social chains. Current consensus leans toward direct reference theory: proper names refer to their referents without attributing additional sense or connotation.

### Descriptivist Theory of Names
The view that a name's meaning is identical to the descriptions speakers associate with it, and that reference is determined by whatever object satisfies those descriptions. The Frege-Russell view. Attacked in the 1970s by Kripke (names are rigid designators, not description-clusters) and Putnam (natural kind terms like "water" refer to the underlying nature, not surface descriptions). Revived in 2D semantics (Chalmers). The debate is unresolved but the consensus has shifted toward causal/direct theories.

### Causal Theory of Reference
Names acquire referents through: (1) an initial baptism that fixes the referent, and (2) a causal chain transmitting the name-referent link through a community. Weaker versions merely insist that causal history must be considered when assigning reference. Kripke and Donnellan developed this in the 1970s; Putnam extended it to natural kind terms. The theory explains how names can survive changes in associated descriptions (we can be wrong about everything we believe about Aristotle and still refer to him) but struggles with reference-shifting (how "Madagascar" came to name the island rather than the mainland region it originally designated).

### Semiotics
The study of signs -- anything that communicates meaning beyond itself. Three branches: syntactics (formal relations between signs), semantics (signs and meanings), pragmatics (signs and users). Two major models: Saussure's dyadic (signifier/signified, relation is arbitrary/conventional) and Peirce's triadic (sign vehicle/referent/interpretant). Sign types: iconic (resemblance), indexical (causal link), symbolic (convention). Names are primarily symbolic signs in Peirce's taxonomy -- their connection to referents is conventional rather than natural.

### Signifier and Signified (Saussure)
The two components of a sign: the signifier (plane of expression -- the sound-image, the written mark) and the signified (plane of content -- the concept). The relationship between them is arbitrary -- there is no natural reason "tree" should mean tree. This arbitrariness is both the power and the vulnerability of naming: it enables infinite productivity (we can name anything) but requires social convention to maintain stability.

### Ferdinand de Saussure (1857-1913)
Swiss linguist, co-founder of semiotics. Key contributions: the sign as signifier+signified, the arbitrariness of the sign, the distinction between langue (language system) and parole (individual speech acts), synchronic vs. diachronic linguistics. His structural approach treats names not as labels attached to pre-existing things but as positions within a system of differences -- a name means what it means partly by virtue of what it does not mean.

### Type-Token Distinction
The difference between a type (a class) and its tokens (instances). "A rose is a rose is a rose" has three word types but eight word tokens. Critical for naming: a name-type (the string "x") can have many name-tokens (each use of "x" in code or speech). In programming, this maps directly to class/instance, and in naming conventions, to the distinction between a naming pattern (camelCase) and any particular name conforming to that pattern.

### Rigid Designator
A term that designates the same object in all possible worlds where that object exists. Proper names are rigid designators ("Nixon" refers to Nixon in every counterfactual scenario); definite descriptions are generally not ("the 37th president" could have been someone else). This concept is the hinge of the Kripke revolution: if names are rigid, they cannot be synonymous with descriptions, because descriptions can vary across possible worlds.

### Natural Kind
A grouping that reflects actual structure in the world rather than human convention. "Water," "gold," "tiger" name natural kinds. Putnam's Twin Earth argument: even if Twin Earth water is qualitatively identical to ours but has a different molecular structure (XYZ instead of H2O), "water" on Earth still refers only to H2O. Natural kind terms are like proper names for categories -- they rigidly designate the underlying nature, not the surface appearance.

### Sign (semiotics)
Anything that communicates meaning beyond itself. Saussure's dyadic model: signifier + signified, relation is arbitrary, maintained by convention. Peirce's triadic model: sign vehicle + referent + interpretant, classified as icon (similarity), index (causal connection), or symbol (convention). A name is a symbol-type sign: its connection to its referent is purely conventional. But naming acts can also be indexical (pointing and saying "that is X") or even iconic (onomatopoeia, sound-symbolic naming).

### Semiotic Triangle (Ogden & Richards, 1923)
The triangle of reference: symbol (word/name) -- thought/reference (concept) -- referent (object). The crucial claim: there is no direct connection between symbol and referent; the connection is always mediated by thought. This mediating role of cognition is what makes naming both powerful and fragile -- the same symbol can trigger different thoughts in different minds, leading to communication failure.

### Direct Reference Theory
The view that a name's meaning is simply its referent -- no intervening sense, description, or concept. Associated with Mill, refined by Kripke. Wittgenstein's later work is the major counterargument: "the meaning of a word is its use." The tension between direct reference and use-theory is one of the deepest unresolved problems in the philosophy of naming.

### Language Game (Wittgenstein)
A word or sentence has meaning only as a result of the "rules" of the "game" being played. "Water!" can be an order, an answer, or a warning depending on context. For naming: the same name can function differently in different language games. A variable name in a for-loop, a column name in a database schema, and a class name in an API are three different language games with different rules for what makes a name good.

### Self-Reference
A sentence, formula, or system referring to itself. Self-referential naming creates paradoxes (the liar paradox, Russell's paradox, Godel's incompleteness). In computing: recursive data structures, self-modifying code, reflection APIs. Self-reference reveals the limits of naming -- some names cannot name themselves without contradiction.

### Identifier (computer science)
A name that labels the identity of a unique object or class. Can follow an encoding system (codes) or be arbitrary. The article makes a crucial observation: "name" and "identifier" are denotatively synonymous but connotatively different. "Jamie Zawinski" is a name; "Netscape employee number 20" is an identifier. Both refer to the same person, but they participate in different naming games with different rules of use.

### Symbol (formal)
In formal languages, a symbol refers to the idea, and marks are tokens of that symbol. This is the type-token distinction applied to formal systems. Formal symbols have the unique property of being defined entirely by their role within a system of rules -- their meaning is purely structural, unlike natural-language names which carry historical, cultural, and connotative baggage.

### Namespace
A set of names used to identify and refer to objects, structured to ensure uniqueness within scope. Hierarchical namespaces allow name reuse in different contexts (the "Jane" in the Doe family vs. the "Jane" in the Smith family). Computing examples: file systems, programming language modules, DNS. Namespaces are the engineering solution to the philosophical problem of reference ambiguity -- they add context to resolve what would otherwise be underdetermined references.

### Ontology (information science)
A formal representation of categories, properties, and relations between concepts in a domain. An ontology is, in effect, a naming system with declared semantics -- it does not just name things but specifies what the names mean and how they relate. The connection to philosophical ontology (Quine, Kripke) and information science (Sowa, Guarino) reveals that naming is always embedded in an ontological commitment: to name something is to assert that it exists and belongs to a category.

### Controlled Vocabulary
A predefined set of preferred terms for indexing and retrieval. The opposite of natural language's open vocabulary. Controlled vocabularies solve the naming problem by fiat: instead of allowing names to drift and multiply, they freeze a canonical set. The cost is flexibility; the gain is precision and interoperability.

### Thesaurus (information retrieval)
A controlled vocabulary that maps semantic relationships: broader/narrower terms, synonyms, related terms. A thesaurus is a naming system that acknowledges the many-to-many relationship between names and concepts -- it does not pretend that one name maps to one thing, but explicitly manages the mappings.

---

## Three Traditions of Naming

### I. The Philosophical Tradition: What Does a Name Mean?

The philosophical tradition asks the most fundamental question: what is the relationship between a name and the thing it names?

**The Descriptivist Answer (Frege, Russell).** A name means the descriptions associated with it. "Aristotle" means "the teacher of Alexander, the author of the Metaphysics, the Stagirite philosopher." Reference is mediated by sense -- you get to the thing through a conceptual route. This is the "indirect" or "mediated" theory.

**The Causal/Direct Answer (Kripke, Donnellan, Putnam).** A name means its referent, period. The connection is established by an initial baptism and maintained by a causal-social chain. Names are rigid designators -- "Aristotle" picks out the same person in every possible world. Descriptions may be associated with a name, but they are not its meaning; we could discover that every description we associate with Aristotle is false, and "Aristotle" would still refer to him.

**The Use-Theoretic Answer (Wittgenstein).** A name means what it does in the language game where it is used. There is no single "meaning" of a name extractable from its patterns of use. Meaning is not a thing a name has but an activity a name performs.

**The Semiotic Synthesis (Saussure, Peirce).** Names are signs. In Saussure's framework, the signifier-signified relationship is arbitrary and maintained by convention within a system of differences. In Peirce's framework, a name is a symbol (conventional sign) that creates an interpretant (a mental effect) linking sign-vehicle to referent. Both frameworks emphasize that naming is a system-level phenomenon -- a name does not mean in isolation but only within a network of other names.

The philosophical tradition reveals that the naming problem is fundamentally about the gap between symbols and the world. No purely formal account bridges this gap; every theory requires some extra-formal element -- a baptism event, a social convention, a pattern of use, or a cognitive interpretation.

### II. The Linguistic-Scientific Tradition: How Do We Organize Names?

The linguistic tradition takes names as given and asks how they are organized into systems.

**Nomenclature** provides the general framework: a naming system consists of rules for forming terms within a domain. The rules govern morphology (how name-parts combine), scope (what can be named), and governance (who decides).

**Taxonomy** provides the hierarchical structure. The Linnaean system is the paradigm: names encode classification (Homo sapiens = genus Homo, species sapiens). The name itself carries structural information -- it is not just a label but a compressed description of the entity's position in a classification hierarchy.

**Systematic naming** takes this further: IUPAC chemical nomenclature encodes the full molecular structure in the name. A systematic name is a lossless compression of the thing named. The cost is human unreadability -- no one says "2,4,6-trinitrotoluene" in conversation; they say "TNT."

**Controlled vocabularies and thesauri** manage the many-to-many mapping between names and concepts. They acknowledge that natural naming is messy -- synonyms proliferate, meanings drift, the same word means different things in different contexts -- and impose order through authority and governance.

The linguistic-scientific tradition reveals that naming systems face a fundamental tradeoff between **expressiveness** (encoding more information in the name) and **usability** (keeping names short, memorable, and speakable). Every naming convention is a point on this tradeoff curve.

### III. The Computing Tradition: How Do We Make Names Work in Machines?

The computing tradition inherits problems from both philosophy and linguistics but faces a unique constraint: names must be processed by machines that have no understanding of meaning.

**Identifiers** are the atomic unit -- a character sequence that labels a unique entity. The machine cares only about uniqueness and scope; all semantic content is for humans.

**Naming conventions** (camelCase, snake_case, Hungarian notation) are attempts to encode semantic information in the identifier's surface form. They are lightweight, convention-based ontologies: `getUserName()` encodes entity (User), attribute (Name), and operation (get) in a single identifier.

**Namespaces** solve the uniqueness problem through hierarchical scoping. They are the engineering equivalent of taxonomic classification -- `java.util.List` and `java.awt.List` can coexist because the namespace disambiguates. DNS is the global namespace for the internet, and it is instructive that it is both the most successful and the most contested naming system in computing.

**Ontologies (information science)** go beyond naming to declare what names mean and how they relate. An ontology is a naming convention with declared semantics -- it does not just say "use camelCase" but specifies the category structure, the property relationships, and the inference rules that names participate in.

**The type-token distinction** is operationalized in computing as class/instance, schema/record, type/value. A type name (`String`) denotes a class of possible values; a token name (`userName`) denotes a specific instance. The discipline of keeping these levels distinct is one of the central challenges of software naming.

The computing tradition reveals that **naming is a form of compression** -- a name compresses a complex entity into a short token that can be manipulated, transmitted, and composed. The art of programming naming conventions is the art of choosing how much information to compress into the name versus leaving in the surrounding context (types, documentation, module structure).

---

## The Name-Thing Gap

What breaks when names fail? Each tradition has its own failure modes, but they share a common structure: a gap opens between the name and what it was supposed to name.

### Reference Failure
**Philosophy:** Frege's empty names -- "the largest integer" has sense but no reference. Fictional names ("Sherlock Holmes") refer within a fictional context but not in the actual world. The descriptivist says empty names still mean (they express a concept); the direct reference theorist says they are, strictly speaking, meaningless.

**Computing:** Null pointer exceptions, dangling references, undefined variables. A name that was supposed to point to an object but points to nothing. The `NullPointerException` is Frege's puzzle made operational -- the program believed the name had a referent, but it did not.

### Namespace Collisions
**Linguistics:** Homonymy -- "bank" (financial institution) vs. "bank" (river edge). Resolved by context in natural language, but context is expensive to process and ambiguity persists.

**Computing:** Name collisions across modules, libraries, or APIs. Resolved by namespaces, but namespace design is itself a naming problem (what should the namespace be called? how deep should the hierarchy go?). The JavaScript ecosystem's flat `npm` namespace has led to name-squatting and the infamous `left-pad` incident -- a single-name dependency that, when removed, broke thousands of projects.

### Semantic Drift
**Linguistics:** Words change meaning over time. "Nice" once meant "foolish." "Computer" once meant a person who computes. Names in natural language are never permanently fixed -- the causal chain transmits the name, but the associated descriptions evolve.

**Computing:** API names whose implementations have drifted from their original semantics. A function called `getUser()` that now also initializes a cache. A database column called `status` whose enumerated values have been extended beyond the original design. Semantic drift in code is a major source of bugs because machines cannot detect the discrepancy between name and behavior -- only humans can, and only if they read carefully.

### The Abstraction Mismatch
**Philosophy:** Kripke's puzzle about belief -- Pierre believes "Londres est jolie" and "London is not pretty" without realizing these are the same city under different names. The name-thing gap is not just between name and thing but between different names for the same thing.

**Computing:** The same entity represented by different names in different parts of a system -- `user_id` in the database, `userId` in the API, `uid` in the cache, `person_identifier` in the analytics pipeline. Integration bugs are often naming bugs: two systems that cannot agree on what to call the same thing.

### The Governance Problem
**Science:** Who decides the name? Biological nomenclature has international commissions. Chemical nomenclature has IUPAC. Astronomical nomenclature has the IAU. Without governance, naming devolves into competing conventions, forks, and dialect.

**Computing:** Who owns the namespace? Domain name disputes, package registry squatting, trademark conflicts in open-source project names. The DNS root is controlled by ICANN; npm packages are first-come-first-served; Python packages on PyPI have no formal governance for name quality. Every naming system eventually needs a governance layer, and the governance is always political.

---

## Conceptual Map

```
THE NAMING PROBLEM
    |
    +-- WHAT DOES A NAME MEAN? (Philosophy)
    |       |
    |       +-- Descriptivist: name = bundle of descriptions (Frege, Russell)
    |       +-- Causal/Direct: name = rigid designator, fixed by baptism (Kripke)
    |       +-- Use-theoretic: name = role in language game (Wittgenstein)
    |       +-- Semiotic: name = sign (signifier/signified, arbitrary link) (Saussure, Peirce)
    |
    +-- HOW ARE NAMES STRUCTURED? (Linguistics / Science)
    |       |
    |       +-- Nomenclature: rules for forming names in a domain
    |       +-- Taxonomy: hierarchical classification encoded in names
    |       +-- Systematic naming: compositional encoding of structure
    |       +-- Controlled vocabulary: canonical term sets, managed synonymy
    |       +-- Thesaurus: explicit mapping of name-concept relationships
    |
    +-- HOW DO NAMES WORK IN MACHINES? (Computing)
    |       |
    |       +-- Identifier: character sequence labeling an entity
    |       +-- Naming convention: surface-form rules encoding semantics
    |       +-- Namespace: hierarchical scope for uniqueness
    |       +-- Ontology: names + declared semantics + inference rules
    |       +-- Type-token: class names vs. instance names <!-- allow-secret -->
    |
    +-- WHAT BREAKS? (The Name-Thing Gap)
            |
            +-- Reference failure (empty names, null pointers)
            +-- Collision (homonymy, namespace conflicts)
            +-- Drift (semantic change, API rot)
            +-- Mismatch (same thing, different names across systems)
            +-- Governance (who decides? who enforces?)

CROSS-CUTTING THEMES:
    - Arbitrariness vs. motivation (how much should a name describe its referent?)
    - Compression vs. readability (information density of names)
    - Local vs. global (scope and context-dependence of names)
    - Stability vs. evolution (can names be fixed forever?)
    - Individual vs. social (names require shared convention to work)
```

---

## Implications for System Design

### 1. Every naming convention is an ontological commitment

When you name a directory `models/`, you assert that there is a category called "models" and that the contents belong to it. When you name a variable `userEmail`, you assert that there exists a user entity with an email property. Naming is not decoration; it is architecture. The Kripkean insight applies: once you baptize a module as `auth`, that name will rigidly designate that module across the system's possible evolutions, even if the module's responsibilities drift far from authentication.

### 2. The Frege principle: sense matters, not just reference

Two names that point to the same thing are not interchangeable if they present different "modes of access." `customer_id` and `account_holder_id` may refer to the same database row, but they imply different conceptual frames. A good naming convention preserves sense distinctions even when reference is shared. This is why aliases are dangerous: they create the illusion that two things are different when they are the same (or vice versa).

### 3. Namespaces are the engineering solution to context-dependence

Natural language resolves ambiguity through context. Formal systems cannot rely on context because machines do not understand it. Namespaces are artificial context -- they provide the disambiguation that natural context provides for free. The implication: invest in namespace design proportional to system scale. A solo script needs no namespaces. A 100-repo workspace needs a rigorous namespace hierarchy.

### 4. Controlled vocabularies prevent semantic drift

The thesaurus model -- preferred terms, synonyms, broader/narrower relationships -- is directly applicable to system design. A project glossary that maps canonical terms to their synonyms and specifies which terms are preferred prevents the slow accumulation of inconsistent naming. `seed.yaml` contracts that declare terminology are a form of controlled vocabulary.

### 5. The type-token discipline prevents category errors

Confusing a class name with an instance name, or a schema name with a value, produces bugs that are invisible to type checkers but obvious to humans. A naming convention that visually distinguishes types from tokens (e.g., `PascalCase` for types, `camelCase` for instances) operationalizes the philosophical distinction in a way that catches errors at read time.

### 6. Naming governance scales with system complexity

Biological nomenclature works because international commissions arbitrate disputes. Package registries work (to the extent they do) because there are rules about name ownership. A multi-organ system like ORGANVM needs naming governance: who can create a new top-level name? What are the rules for naming repos, modules, events, and schemas? The double-hyphen convention (word-separator vs. function-descriptor separator) is a micro-nomenclature -- a small formal system that encodes structural information in the name's surface form.

### 7. The Wittgensteinian warning: names work only within their language game

A name that is perfectly clear in one context (a Git branch called `fix/auth-redirect`) may be opaque in another (a Jira ticket title, a commit message, a changelog entry). When designing naming conventions for complex systems, specify the language game: where will this name appear? Who will read it? What do they need to understand from the name alone?

---

## Open Questions

1. **Is there a universal theory of naming?** Kripke's causal theory, Saussure's arbitrariness principle, and computing's namespace model all describe aspects of how names work. Can they be unified, or are they irreducibly different accounts of different phenomena?

2. **What is the optimal information density of a name?** IUPAC names encode everything but are unreadable. Common names encode nothing but are memorable. Where on the spectrum should system names sit, and does the answer depend on the system's scale, domain, or lifecycle stage?

3. **Can naming conventions be derived from first principles?** Or are they always contingent, evolved, and culturally determined? The existence of Kripke's "initial baptism" suggests that every naming system has an arbitrary origin -- but does that mean all conventions are equally good?

4. **How does naming interact with AI code generation?** LLMs trained on vast codebases develop implicit naming conventions. When an LLM generates code, its names reflect statistical patterns across millions of repos. Is this a new form of naming governance -- governance by corpus rather than by committee?

5. **What is the relationship between naming and identity?** In philosophy, naming is closely tied to personal identity (is the Ship of Theseus still the Ship of Theseus?). In computing, naming is tied to entity identity (is the refactored `AuthService` still the same service?). The parallel suggests that the naming problem is ultimately an identity problem.

6. **Can self-referential naming be made safe?** Self-reference in naming produces paradoxes (a directory named `..`, a variable that stores its own name, a schema that describes itself). Computing has partial solutions (reflection APIs, metaclasses) but no general theory. Is there a naming analogue to Godel's incompleteness -- a proof that no naming system can consistently name all of its own parts?

7. **Is the double-hyphen convention a rigid designator or a description?** In the ORGANVM system, `sema-metra--alchemica-mundi` uses double-hyphen to separate function from descriptor. Is "sema-metra" a rigid designator (it names this specific engine across all possible evolutions) or a description (it names whatever engine measures signs)? The answer determines whether the name survives refactoring.

---

## Frontier Articles

Discovered via link-graph exploration of *Naming and Necessity* and *Semiotics*. These represent the next layer of investigation.

### From Naming and Necessity's link graph:
- **Rigid designator** -- the core technical concept; explored above
- **Natural kind** -- extends naming theory to category terms; explored above
- **A posteriori necessity** -- Kripke's claim that some necessary truths (water = H2O) are known empirically, not a priori; challenges Kant's framework
- **Ruth Barcan Marcus** -- often credited with anticipating Kripke's theory of names as "tags"; priority dispute with Kripke
- **Scott Soames** -- contemporary philosopher who has written extensively on the legacy of Naming and Necessity
- **Dthat** -- David Kaplan's formal device for directly referring expressions; bridges naming theory and formal logic
- **Identity (philosophy)** -- the metaphysical problem underlying all naming: what makes something the same thing over time?

### From Semiotics' link graph:
- **Semiotic triangle** -- the Ogden-Richards model; explored above
- **Code (semiotics)** -- the system of rules governing sign use; naming conventions are codes
- **Interpretant** -- Peirce's concept of the sign's effect on the interpreter; the "meaning" of a name is the interpretant it produces
- **Markedness** -- in structural linguistics, the asymmetry between a default (unmarked) term and a specialized (marked) term; relevant to naming conventions where one form is default and others are marked
- **Paradigmatic analysis** -- analysis of substitution possibilities at a given position; relevant to naming: what other names could have been chosen?
- **Biosemiotics** -- sign processes in living systems (DNA as a naming system, protein naming); extends the naming problem to pre-linguistic biology
- **Cognitive semiotics** -- how minds process signs; the cognitive science of naming
- **Computational semiotics** -- formal models of sign processes; bridges semiotics and computing

### Additional frontier candidates:
- **Cratylus (dialogue)** -- Plato's dialogue on whether names are natural or conventional; the original naming debate
- **Universals (philosophy)** -- do general names (like "red" or "justice") refer to real universals or are they mere conveniences?
- **Ontological commitment** -- Quine's principle that to use a name is to assert the existence of its referent; naming as existence claim
- **Semantic web** -- the attempt to make all names on the web machine-interpretable via URIs and ontologies
- **Uniform Resource Identifier (URI)** -- the most ambitious naming system ever attempted: a universal namespace for all digital resources

---

## Sources

### Seed Articles (Wikipedia)
1. [Naming convention (programming)](https://en.wikipedia.org/wiki/Naming_convention_(programming))
2. [Systematic name](https://en.wikipedia.org/wiki/Systematic_name)
3. [Nomenclature](https://en.wikipedia.org/wiki/Nomenclature)
4. [Naming convention](https://en.wikipedia.org/wiki/Naming_convention)
5. [Philosophy of language](https://en.wikipedia.org/wiki/Philosophy_of_language)
6. [Meaning (philosophy)](https://en.wikipedia.org/wiki/Meaning_(philosophy))
7. [Communication](https://en.wikipedia.org/wiki/Communication)
8. [Paradigm](https://en.wikipedia.org/wiki/Paradigm)
9. [Taxonomy](https://en.wikipedia.org/wiki/Taxonomy)
10. [Typology](https://en.wikipedia.org/wiki/Typology)
11. [Scientific classification](https://en.wikipedia.org/wiki/Scientific_classification)

### Expansion Articles (Wikipedia)
12. [Naming and Necessity](https://en.wikipedia.org/wiki/Naming_and_Necessity)
13. [Saul Kripke](https://en.wikipedia.org/wiki/Saul_Kripke)
14. [Sense and reference](https://en.wikipedia.org/wiki/Sense_and_reference)
15. [Gottlob Frege](https://en.wikipedia.org/wiki/Gottlob_Frege)
16. [Semiotics](https://en.wikipedia.org/wiki/Semiotics)
17. [Signifier and signified](https://en.wikipedia.org/wiki/Signifier_and_signified)
18. [Ferdinand de Saussure](https://en.wikipedia.org/wiki/Ferdinand_de_Saussure)
19. [Type-token distinction](https://en.wikipedia.org/wiki/Type%E2%80%93token_distinction)
20. [Proper name (philosophy)](https://en.wikipedia.org/wiki/Proper_name_(philosophy))
21. [Descriptivist theory of names](https://en.wikipedia.org/wiki/Descriptivist_theory_of_names)
22. [Causal theory of reference](https://en.wikipedia.org/wiki/Causal_theory_of_reference)
23. [Identifier (computer science)](https://en.wikipedia.org/wiki/Identifier_(computer_science))
24. [Symbol (formal)](https://en.wikipedia.org/wiki/Symbol_(formal))
25. [Namespace](https://en.wikipedia.org/wiki/Namespace)
26. [Ontology (information science)](https://en.wikipedia.org/wiki/Ontology_(information_science))
27. [Controlled vocabulary](https://en.wikipedia.org/wiki/Controlled_vocabulary)
28. [Thesaurus (information retrieval)](https://en.wikipedia.org/wiki/Thesaurus_(information_retrieval))

### Frontier Articles (Wikipedia)
29. [Rigid designator](https://en.wikipedia.org/wiki/Rigid_designator)
30. [Natural kind](https://en.wikipedia.org/wiki/Natural_kind)
31. [Direct reference theory](https://en.wikipedia.org/wiki/Direct_reference_theory)
32. [Semiotic triangle](https://en.wikipedia.org/wiki/Semiotic_triangle)
33. [Language game (philosophy)](https://en.wikipedia.org/wiki/Language_game_(philosophy))
34. [Self-reference](https://en.wikipedia.org/wiki/Self-reference)
35. [Sign (semiotics)](https://en.wikipedia.org/wiki/Sign_(semiotics))

### Key Primary Texts (not fetched, for further reading)
- Frege, G. (1892). "Uber Sinn und Bedeutung" (*Zeitschrift fur Philosophie und philosophische Kritik*)
- Saussure, F. de (1916). *Cours de linguistique generale*
- Kripke, S. (1980). *Naming and Necessity* (Harvard University Press)
- Ogden, C.K. & Richards, I.A. (1923). *The Meaning of Meaning*
- Wittgenstein, L. (1953). *Philosophical Investigations*
- Putnam, H. (1975). "The Meaning of 'Meaning'" in *Mind, Language and Reality*
- Mill, J.S. (1843). *A System of Logic*

---

*Research adventure compiled 2026-03-20. 35 Wikipedia articles consulted, 11 seed + 18 expansion + 6 frontier. Cross-domain synthesis connecting analytic philosophy, structural linguistics, scientific nomenclature, and software engineering.*
