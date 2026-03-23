---
sgo_id: SGO-2026-RP-004
title: "The Deep Structure of Naming"
tier: Paper
status: LOCAL (revised draft)
target_venues: [Synthese, JASIST, arXiv cs.PL]
dependencies: none
date: 2026-03-21
revision_date: 2026-03-20
version: v2
revision_notes: |
  TRP review required revise-and-re-review (2/3 revise, 1/3 advance).
  Key amendments incorporated:
  - Added Section 3.4: cross-cultural naming evidence (Chinese zhengming, Arabic nasab/kunya,
    Japanese multi-script naming, indigenous Australian relational naming) per POV 3 critique.
  - Qualified universality claims throughout: "structural commonalities across traditions"
    replaces "universal theory" in RQ1 and title framing.
  - Sharpened design principles to be non-obvious, with trade-off analysis.
  - Reduced boundary-object usage per corpus-level critique; term now appears only where
    Star and Griesemer's structural features are genuinely present.
  - Engaged with empirical identifier quality literature (Lawrie, Butler, Hofmeister).
  - Distinguished "naming problems are structurally unified" (well-supported) from
    "naming theories are structurally unified" (not yet supported).
---

# The Deep Structure of Naming: Structural Commonalities Across Natural Language, Formal Systems, and Programming

## 1. Introduction

The act of naming is one of the most fundamental operations of cognition, language, and engineering. Before an entity can be classified, described, measured, or manipulated, it must be named. The naming act appears deceptively simple -- attach a label to a thing -- yet it conceals a web of philosophical, linguistic, and technical problems that have occupied thinkers from Plato to the designers of the Domain Name System. This paper argues that naming is not three separate problems wearing the same word, but a single structural problem that manifests differently across domains. To see the unity beneath the diversity, one must examine the deep structure that all naming shares: a reference relation between a sign and a referent, mediated (or not) by sense, constrained by scope, governed by convention, and subject to characteristic modes of failure.

The practical stakes are considerable. In software engineering, naming is routinely cited as one of the two hardest problems in computer science (alongside cache invalidation and off-by-one errors) [Karlton, attributed]. Poorly chosen names produce cascading failures: a misleading function name causes a misunderstanding that causes a bug that causes an outage. In the sciences, the Linnaean system of binomial nomenclature has endured for over 270 years precisely because it solves the naming problem well -- encoding hierarchical classification in the name itself, governed by international commissions, and decoupled from any single natural language through the use of Latin [Linnaeus, 1753]. In philosophy, the debate over how names refer -- whether by description, by causal chain, or by use -- remains one of the central unresolved problems of analytic philosophy, with consequences for metaphysics, epistemology, and the philosophy of mind [Kripke, 1980; Frege, 1892].

The theoretical stakes are equally significant. Naming sits at the intersection of three major intellectual traditions, each of which has developed sophisticated but largely independent accounts. The philosophical tradition, from Frege through Russell to Kripke and Wittgenstein, asks what the relationship is between a name and its referent. The linguistic-scientific tradition, from Saussure through Peirce to modern taxonomy and controlled vocabularies, asks how names are organized into systems. The computational tradition, from early assembler mnemonics through structured programming to modern ontology engineering, asks how names can be made to work in machines that have no understanding of meaning.

Despite their independent development, these three traditions converge on remarkably similar structures. All three recognize that the name-thing relation is neither simple nor direct. All three grapple with characteristic failure modes: reference failure, collision, semantic drift, and governance problems. All three acknowledge that naming involves a fundamental tradeoff between the information a name carries and its cognitive or computational cost.

This paper addresses three research questions:

**RQ1:** Are there structural commonalities across Kripke's causal theory, Saussure's arbitrariness principle, and computing's namespace model that suggest a unified structural account of naming, or are these irreducibly different accounts of different phenomena?

**RQ2:** What is the optimal information density of a name, and does the answer depend on system scale, domain, or lifecycle stage?

**RQ3:** How does the type-token distinction -- a philosophical concept originating with Peirce -- operationalize differently in natural language, formal systems, and programming, and what does this reveal about the nature of naming?

An important clarification is necessary at the outset. This paper distinguishes between two claims of different strengths. The first -- that *naming problems* are structurally unified across domains -- is well-supported by the evidence presented here: the same five failure modes recur across philosophy, linguistics, and computing because they are structural features of the reference relation itself. The second -- that *naming theories* are structurally unified, that a single account of reference subsumes Kripke, Saussure, and namespace theory -- is considerably stronger and is not established by this paper. The structural parallels demonstrated here are necessary conditions for such a unified theory but not sufficient evidence of one.

The paper proceeds as follows. Section 2 surveys the three traditions in detail. Section 3 identifies structural commonalities and differences, including a comparative analysis of non-Western naming systems that tests the scope of the proposed structural parallels. Section 4 proposes a framework centered on the reference relation as a common structure. Section 5 draws implications for system design. Section 6 discusses open questions. Section 7 concludes.

The paper contributes: (a) a cross-domain taxonomy of naming failures showing structural analogues across philosophy, linguistics, and computing; (b) the "naming as compression" thesis, which frames every naming convention as a point on a universal expressiveness-usability tradeoff curve; (c) cross-cultural evidence testing the scope of these structural claims; and (d) a set of design principles for naming systems derived from the synthesis.

## 2. Three Traditions of Naming

### 2.1 The Philosophical Tradition

The philosophical tradition asks the most fundamental question about naming: what is the relationship between a name and the thing it names? Four major positions have emerged over 130 years of sustained argument.

#### 2.1.1 Frege's Sense/Reference Distinction

In his 1892 paper "Uber Sinn und Bedeutung," Gottlob Frege introduced a distinction that has structured every subsequent debate about naming. The *reference* (Bedeutung) of a name is the object it denotes; the *sense* (Sinn) is the "mode of presentation" -- the cognitive route by which a thinker grasps the referent [Frege, 1892]. Frege's motivating puzzle is elegant: the statement "Hesperus is Phosphorus" is informative, even surprising, while "Hesperus is Hesperus" is trivially true. Yet both statements are about the same object (the planet Venus). If the meaning of a name were simply its referent, the two statements would have the same meaning. Since they do not, names must carry something beyond reference -- namely, sense.

The implications for naming theory are profound. Two names can share a referent while differing in sense, and it is the sense that carries cognitive content. Frege extended this analysis beyond proper names to definite descriptions, function expressions, and entire sentences, arguing that the sense of a sentence is the thought (Gedanke) it expresses and its reference is its truth-value.

Frege's distinction generates what might be called the *sense preservation principle*: substituting co-referential names can change the cognitive content of an expression. This principle has direct consequences for any naming system. Two database columns that point to the same underlying data -- say, `customer_id` and `account_holder_id` -- are not interchangeable if they present that data under different conceptual aspects.

#### 2.1.2 Russell's Description Theory

Bertrand Russell radicalized Frege's approach by arguing that ordinary proper names are, in logical form, disguised definite descriptions [Russell, 1905]. On this view, "Aristotle" abbreviates something like "the teacher of Alexander who wrote the Metaphysics." John Searle subsequently developed a *cluster theory*: speakers associate a loosely organized cluster of descriptions with a name, any sufficient subset of which can fix reference [Searle, 1958].

#### 2.1.3 Kripke's Causal/Rigid Designator Theory

Saul Kripke's 1970 Princeton lectures, published as *Naming and Necessity* in 1980, overturned the Frege-Russell consensus. Kripke argued that proper names are *rigid designators* -- terms that designate the same object in every possible world where that object exists [Kripke, 1980]. The modal argument is devastating for descriptivism: if the meaning of "Aristotle" were "the teacher of Alexander," then "Aristotle might not have taught Alexander" would be self-contradictory. Since it is perfectly intelligible, names and descriptions have different semantic functions.

In place of descriptions, Kripke proposed the *causal theory of reference*: a name acquires its referent through an *initial baptism* and is transmitted through a community via a *causal chain* of communication. Hilary Putnam extended the causal approach to natural kind terms like "water" and "gold" [Putnam, 1975].

#### 2.1.4 Wittgenstein's Use Theory

Ludwig Wittgenstein's later philosophy offers a fundamentally different approach. The meaning of a word is its use in the language [Wittgenstein, 1953, section 43]. A name functions as part of a *language game* -- a form of life in which language and action are interwoven. For naming theory, Wittgenstein's contribution is the recognition that the same name can participate in different language games with different rules for success. The question "is this a good name?" has no context-free answer.

### 2.2 The Scientific/Linguistic Tradition

#### 2.2.1 Saussure's Signifier/Signified

Ferdinand de Saussure established that a linguistic sign consists of a *signifier* (the sound-image) and a *signified* (the concept), related by arbitrary convention [Saussure, 1916]. Signs acquire meaning through their position in a *system of differences*: "tree" means what it means partly by virtue of what it is not.

#### 2.2.2 Peirce's Triadic Sign Model

Charles Sanders Peirce developed a richer *triadic* framework: a sign consists of a *sign vehicle*, a *referent*, and an *interpretant* (the mental effect the sign produces in an interpreter) [Peirce, 1931-1958]. The interpretant introduces a perspectival element absent from Saussure's framework: the same sign vehicle can produce different interpretants in different interpreters.

#### 2.2.3 Nomenclature, Taxonomy, and Systematic Naming

The scientific tradition has developed the most elaborate formal naming systems in any domain. The Linnaean system exemplifies a successful naming system: stable for over 270 years, encoding hierarchical classification in the name itself, and governed by international codes of nomenclature. *Systematic naming* (IUPAC chemical nomenclature) takes encoding further, approaching *lossless compression* of the thing named. The tension between systematic and common names reveals a fundamental tradeoff: *expressiveness* versus *usability*.

### 2.3 The Computational Tradition

#### 2.3.1 Identifiers, Variables, and Naming Conventions

The *identifier* is the atomic unit of computational naming. *Naming conventions* -- camelCase, snake_case, PascalCase, Hungarian notation -- are attempts to encode semantic information in the identifier's surface form. They are lightweight, convention-based ontologies.

#### 2.3.2 Namespaces and Hierarchical Scoping

*Namespaces* solve the uniqueness problem through hierarchical scoping. The Domain Name System demonstrates both the success and the political complexity of namespace governance at global scale.

#### 2.3.3 Ontologies and Information Architecture

*Ontologies* in information science declare what names mean and how they relate. Quine's criterion of ontological commitment holds that to name something in one's theory is to assert its existence [Quine, 1948]. Every information-science ontology is an ontological commitment in Quine's sense.

## 3. Structural Comparison

### 3.1 The Name-Thing Gap: Five Failure Modes Across Domains

When naming fails, a gap opens between the name and what it was supposed to name. This paper identifies five structural failure modes that recur across the traditions surveyed here.

**Reference failure** is the most basic: a name that points to nothing. In philosophy, Frege's "empty names" illustrate the problem. In computing, the `NullPointerException` is reference failure made operational.

**Namespace collision** occurs when a single name maps to multiple referents within a scope. In natural language, this is homonymy. In computing, the npm ecosystem's flat namespace has produced name-squatting, trademark disputes, and the infamous `left-pad` incident of 2016.

**Semantic drift** occurs when a name's associated meaning changes over time while the name persists. In computing, semantic drift manifests as functions whose implementations have diverged from their original semantics.

**Abstraction mismatch** occurs when the same entity is represented by different names in different contexts. Kripke's puzzle about belief -- Pierre and London/Londres -- has its computational analogue in integration failures between systems that cannot agree on what to call the same thing.

**Governance failure** occurs when there is no authoritative mechanism for resolving naming disputes. Biological nomenclature solved this through international commissions. Computing has fragmented governance: ICANN, npm, PyPI, and crates.io each have their own rules.

These five failure modes constitute a cross-domain taxonomy of naming pathology. Their recurrence across the traditions surveyed here suggests that they are structural features of the reference relation itself, not domain-specific accidents. Section 3.4 tests this claim against non-Western naming systems.

### 3.2 Information Density of Names

Every name occupies a position on a spectrum from maximally compressed (a single arbitrary character) to maximally expanded (a complete description of the referent). The information-density tradeoff has three dimensions: *referential precision*, *descriptive richness*, and *cognitive cost*. These dimensions are in tension.

The empirical literature on identifier quality in software engineering provides evidence that this tradeoff has measurable consequences. Lawrie et al. (2006) found that full-word identifiers are significantly easier to understand than abbreviated ones. Butler et al. (2010) demonstrated a correlation between identifier naming conventions and defect density. Hofmeister et al. (2017) showed that naming style affects code comprehension time and accuracy. These studies confirm that the expressiveness-usability tradeoff is not merely aesthetic; it has quantifiable effects on code quality and developer productivity.

### 3.3 The Type-Token Distinction Across Domains

The type-token distinction, originating with Peirce, differentiates between a *type* (an abstract class) and its *tokens* (concrete instances). The cross-domain comparison reveals that the type-token distinction is not merely a classification tool but a *design constraint* on naming systems. Any naming convention that fails to distinguish types from tokens invites confusion between levels of abstraction.

### 3.4 Cross-Cultural Naming Systems: Testing the Structural Claims

The three traditions surveyed in Section 2 all emerge from the same intellectual lineage: European philosophy, European semiotics, and Anglo-American engineering. If the structural claims of this paper -- the five failure modes, the expressiveness-usability tradeoff, the type-token distinction -- are genuinely structural features of naming rather than cultural artifacts, they should be testable against naming systems that developed independently. This section examines four non-Western naming traditions.

#### 3.4.1 Chinese Naming and Zhengming

The *zhengming* (rectification of names) tradition, originating with Confucius and developed by Xunzi, holds that social order depends on names being correctly aligned with their referents: "If names are not correct, language will not be in accordance with the truth of things" (*Analects* 13.3). This is a *normative* theory of naming that differs from both descriptivism and causal theory. It treats naming not primarily as a reference-fixing mechanism but as an *ethical and political act*: incorrect naming produces social disorder.

The zhengming tradition exhibits the five failure modes, though with different emphasis. Reference failure is present (names that do not correspond to social realities produce "empty rituals"). Semantic drift is the central concern -- zhengming is precisely a response to the problem of names whose meanings have drifted from their proper referents. Governance is explicitly addressed: the authority to rectify names is tied to political and moral authority. What zhengming adds, which the Western traditions do not foreground, is the *constitutive* dimension of naming: names do not merely describe social reality; they shape it. A ruler who is not called a ruler may cease to function as one. This constitutive dimension -- naming as social construction -- is present in Wittgenstein's language games and in ANT's concept of performativity, but neither tradition makes it as central as zhengming does.

#### 3.4.2 Arabic Naming Conventions

Traditional Arabic naming follows a multi-layered system: the *ism* (given name), *nasab* (patrilineal chain: ibn X ibn Y ibn Z), *kunya* (teknonym: Abu X, father of X), *laqab* (descriptive epithet or title), and *nisba* (geographic, tribal, or occupational affiliation). This system is simultaneously hierarchical (the nasab encodes a genealogical tree) and relational (the kunya encodes a social relationship to one's child, a relationship that *constitutes* part of the person's social identity).

The Arabic system encodes more information in the name than any of the Western systems analyzed in Section 2 -- approaching the systematic-naming end of the expressiveness-usability tradeoff. It also exhibits a sophisticated type-token discipline: the ism is a token-level identifier (this specific person), the nasab encodes type-level membership (this lineage), and the nisba encodes categorical membership (this geographic or occupational group). The five failure modes apply: reference failure (disputed lineages), collision (common names requiring disambiguation through additional name-layers), drift (laqabs that no longer describe their bearers), and governance (who has authority to confer a laqab or recognize a nasab).

#### 3.4.3 Japanese Multi-Script Naming

Japanese naming involves multiple orthographic systems: kanji, hiragana, katakana, and romaji. Each carries different social registers, levels of formality, and cultural connotations. The "same" name written in different scripts has different social meaning -- a phenomenon that challenges Saussure's principle that the signifier is arbitrary, since here the *visual form* of the signifier carries non-arbitrary social information.

This presents a naming dimension absent from the Western traditions surveyed: the *material substrate* of the name itself as a carrier of meaning. In computing terms, this is analogous to the way different encoding schemes (UTF-8, Shift-JIS) can carry cultural and contextual information beyond the character content. For naming theory, the Japanese case demonstrates that the expressiveness-usability tradeoff has a dimension not captured by the three-dimensional model of Section 3.2: *social-register expressiveness*, which encodes the relationship between the namer and the named.

#### 3.4.4 Relational Naming in Oral Cultures

Many cultures do not treat names as stable, context-free labels. Among the Nuer of South Sudan, as Evans-Pritchard (1940) documented, individuals have multiple names used in different social contexts -- birth names, ox-names, kinship names, dance names -- and the "correct" name depends on who is speaking, to whom, and in what social situation. The name is not a rigid designator or a description; it is a *relationship marker*. In many Australian Aboriginal cultures, the name of a recently deceased person becomes taboo and must be avoided, sometimes along with common words that sound similar, reshaping the entire vocabulary.

These systems introduce naming dimensions that the Western framework does not capture: *taboo violation* as a failure mode (absent from the five-mode taxonomy), *relational indexing* as a naming function (the name encodes the namer-named relationship, not the named's properties), and *impermanence as design principle* (names are expected to change, not to persist). The Western assumption that names should be stable -- central to both Kripke's rigid designation and to engineering best practice -- is culturally specific. In systems where change is the norm and stability is the exception, the design principle becomes: "names should be designed for the expected frequency and type of change."

#### 3.4.5 Assessment: What Holds and What Does Not

The cross-cultural comparison yields a mixed verdict on the structural claims of this paper.

**What holds.** The five failure modes (reference failure, collision, drift, mismatch, governance failure) appear in all naming systems examined, though with different emphasis. The expressiveness-usability tradeoff is universal -- every naming system occupies a point on this curve. The type-token distinction applies in every system, though it may be operationalized differently.

**What requires qualification.** The five-mode taxonomy is *incomplete*: taboo violation, relational indexing failure, and constitutive naming failure (naming that fails to perform its social function) are genuine failure modes not captured by the original taxonomy. The assumption that names should be stable is culturally specific. The assumption that the referential function of naming (picking out an entity) is primary -- shared by Frege, Kripke, and computing -- is not universal: in relational naming systems, the social-relational function is primary and the referential function is secondary.

**Revised claim.** The structural commonalities identified in this paper -- the failure modes, the tradeoff, the type-token distinction -- are genuine structural features of naming that appear across culturally independent traditions. However, they do not constitute a complete universal theory. The Western traditions surveyed in Section 2 foreground the *referential* function of naming. Other traditions foreground the *relational*, *constitutive*, or *ethical* functions. A fully adequate account of naming would need to accommodate all of these functions, not just the referential one. The present paper establishes the referential structural commonalities and identifies the boundary of their applicability.

## 4. Toward a Structural Account

### 4.1 Common Structure: The Reference Relation

Beneath the terminological differences, the traditions surveyed in Section 2 describe the same fundamental structure: a *reference relation* between a sign and a referent, established and maintained by some combination of convention, causation, and use. The traditions differ not in what they describe but in which aspects of this structure they foreground.

The philosophical tradition foregrounds the *metaphysics* of the reference relation. The linguistic-scientific tradition foregrounds the *systematics*. The computational tradition foregrounds the *engineering*.

These are complementary perspectives on the same phenomenon, each illuminating aspects that the others leave in shadow. A unified structural account of naming, if one is achievable, would need to incorporate all three perspectives -- and, as Section 3.4 demonstrates, would need to extend beyond the referential function to accommodate the relational, constitutive, and ethical dimensions that non-Western traditions foreground.

### 4.2 Where Traditions Diverge: Social vs. Formal Naming

The most significant divergence concerns the role of social processes. In philosophy and linguistics, naming is irreducibly social. In computing, naming appears to escape the social -- a variable name works because a compiler binds it to a memory address.

But this escape is illusory. The *mechanical* reference relation (identifier to memory address) is established by code written by humans following *social* naming conventions. In computing, there are two reference relations: a mechanical one (managed by the runtime) and a communicative one (managed by human convention). The two can diverge, producing semantic-drift bugs. This dual-reference structure explains why naming in code is both easier (the mechanical layer ensures referential success) and harder (the communicative layer requires all the social coordination that natural-language naming requires).

### 4.3 The Role of Convention vs. Causation

The convention/causation axis reveals a structural principle: *naming systems that rely solely on convention are vulnerable to drift, while systems that rely solely on causation are vulnerable to rigidity*. The most successful naming systems -- Linnaean taxonomy, DNS, well-maintained codebases -- combine both.

## 5. Implications for System Design

### 5.1 Design Principles Derived from Naming Theory

The synthesis of philosophical, linguistic, computational, and cross-cultural naming theory yields seven design principles for naming systems. For each principle, we identify the non-obvious insight it provides and the trade-off it entails, since design principles without trade-off analysis are aspirations, not engineering guidance.

1. **Ontological commitment is irreversible at scale.** Every naming decision is an ontological commitment. To name a directory `models/` is to assert that there exists a category called "models." The non-obvious insight: ontological commitments compound. Each name creates expectations in every system that consumes it -- linters, documentation generators, CI pipelines, human readers. The cost of changing a name grows superlinearly with the number of consumers. *Trade-off:* Deliberate naming slows initial development but reduces naming debt. The decision of when to invest depends on the expected lifespan and consumer count of the name.

2. **Sense preservation matters more than reference preservation.** Two names that point to the same referent are not interchangeable if they present different modes of access (Frege). The non-obvious insight: merging co-referential names -- collapsing `customer_id` and `account_holder_id` into a single identifier -- destroys information that downstream systems may depend on, even though both resolve to the same database row. *Trade-off:* Preserving sense distinctions increases the number of names to maintain. Excessive sense preservation produces synonym proliferation. The empirical question is whether the sense distinction is *load-bearing* -- whether any consumer relies on the difference.

3. **Namespace depth should match organizational volatility, not organizational size.** The conventional wisdom -- "scale up the namespace as the system grows" -- is half-right. The non-obvious insight, drawn from the cross-cultural comparison (Section 3.4): names should encode what is *stable*, and the stability of different organizational dimensions varies. Function and domain change less frequently than reporting lines. A namespace that encodes org-chart position (`/finance/accounting/tax-service`) becomes naming debt when the org chart changes. A namespace that encodes function and domain (`/tax-computation--regulatory-compliance`) is more stable. *Trade-off:* Function-based namespaces are less immediately legible to organizational newcomers than org-chart-based ones.

4. **Controlled vocabulary discipline prevents the synonymy catastrophe.** A controlled vocabulary -- a predefined set of preferred terms with managed synonymy -- is the naming equivalent of a type system: it catches errors at name-creation time rather than at name-consumption time. The non-obvious insight: uncontrolled naming produces a predictable failure pattern. Initial flexibility feels productive; after approximately 50-100 independent naming decisions (per Zipf's law applied to naming), near-synonyms begin to proliferate (`user`, `account`, `person`, `profile` all referring to slightly different aspects of the same entity), and the cost of disambiguation exceeds the cost of having maintained a controlled vocabulary from the start. *Trade-off:* Controlled vocabularies require governance overhead and resist novel concepts.

5. **Type-token discipline is visual static analysis.** A naming convention that visually distinguishes types from tokens (PascalCase for types, camelCase for instances, SCREAMING_SNAKE_CASE for constants) operationalizes a philosophical distinction in a way that catches category errors at read time. The non-obvious insight: this visual distinction is *more* important in AI-assisted development, not less. When an LLM generates code, the type-token visual discipline is the human reader's fastest check for category confusion. Butler et al. (2010) found that violation of naming conventions correlated with defect density -- the visual discipline is not merely aesthetic but has empirical validity. *Trade-off:* Multiple case conventions increase the cognitive load of learning a new codebase for the first time.

6. **Governance proportionality follows a step function, not a gradient.** Every naming system eventually requires governance. The non-obvious insight: governance needs do not increase linearly with system size. They increase in step-function jumps at threshold points: the first external contributor, the first cross-team dependency, the first automated consumer of names, the first breaking change caused by a name. Below each threshold, governance overhead feels unnecessary. Above each threshold, the absence of governance causes cascading failures. *Trade-off:* Premature governance bureaucratizes; late governance produces naming crises.

7. **Language-game specification prevents cross-context naming failure.** A name that is clear in one context (a Git branch called `fix/auth-redirect`) may be opaque in another (a metric label, a changelog entry). The non-obvious insight from the Japanese multi-script analysis (Section 3.4.3): the *same referent* may need *different names* in different contexts, and the naming convention should specify which contexts are served. A single canonical name that must serve all contexts will serve none well. *Trade-off:* Multiple context-specific names for the same entity increase the risk of abstraction mismatch.

### 5.2 The Double-Hyphen Convention as Applied Naming Ontology

The ORGANVM project employs a naming convention that illustrates several of these principles. The *double-hyphen convention* uses single hyphens to separate words within a semantic unit and double hyphens to separate the functional role from the descriptive content: `sema-metra--alchemica-mundi` parses as "sema-metra" (the engine that measures signs) functioning as "alchemica-mundi" (alchemy of the world).

The convention encodes structure without requiring it (Principle 3): the function/descriptor split is machine-parsable but the name remains suggestive to a reader who does not know the convention. It embodies a specific ontological commitment (Principle 1): every repository has both a function and a domain, and these are distinct dimensions. The question of whether the functional part is a rigid designator or a description is genuinely open and has practical consequences for refactoring decisions.

The case study has a notable limitation: the ORGANVM system is a single-operator system. The naming convention does not face the cross-community interpretation challenges that arise in multi-team organizations. The principles derived from the analysis are theoretically motivated but would benefit from empirical validation in larger, multi-team contexts where naming conventions must mediate between communities with genuinely divergent interests.

## 6. Discussion and Open Questions

**Scope of the structural claims.** This paper has demonstrated structural commonalities across the Western philosophical, linguistic, and computational traditions and has tested these claims against four non-Western naming traditions. The five failure modes, the expressiveness-usability tradeoff, and the type-token distinction appear to hold cross-culturally. However, the cross-cultural analysis also reveals failure modes (taboo violation, relational indexing failure) and naming functions (constitutive, ethical) that the present framework does not capture. These gaps define the boundary conditions of the structural claims and identify directions for extension.

**The possibility of formal unification.** The structural parallels identified here may reflect genuine isomorphism or surface analogy. Category theory, with its emphasis on structure-preserving mappings between domains, is a candidate formalism for the referential structural commonalities. However, the social, pragmatic, and constitutive dimensions of naming -- foregrounded by Wittgenstein, by ANT, and by the zhengming tradition -- may resist formalization. Whether a single formal framework can encompass both the structural and the constitutive dimensions of naming remains an open question.

**Naming in the era of AI code generation.** LLMs trained on vast codebases develop implicit naming conventions derived from statistical patterns. This raises novel questions: Is LLM-generated naming a form of governance by corpus rather than by committee? Does it stabilize naming conventions or degrade them? Does the LLM's inability to access causal chains of reference produce names that are semantically hollow despite being syntactically conventional?

**Toward operationalization.** The five failure modes could be developed into detectable anti-patterns with automated tooling. Reference failure is already detected (null-pointer analysis, unused-variable warnings). Namespace collision is partially detected (linting for shadowed names). Semantic drift, abstraction mismatch, and governance failure are harder to detect automatically but could be approximated through heuristics: function names that no longer match function behavior (via NLP analysis of docstrings vs. implementation), entity names that vary across module boundaries (via cross-module identifier analysis), and naming convention violations (via configurable linters). Developing these detections is a concrete engineering agenda that the present theoretical framework motivates but does not complete.

## 7. Conclusion

Naming is the most basic act of intellectual organization. This paper has surveyed three major traditions of naming theory -- philosophical, linguistic-scientific, and computational -- tested its structural claims against four non-Western naming traditions, and argued that beneath terminological and methodological differences, these traditions exhibit structural commonalities centered on the reference relation, the expressiveness-usability tradeoff, and five characteristic failure modes.

The structural commonalities are genuine but bounded. They extend to the referential function of naming -- the question of how a sign picks out a referent -- but do not fully capture the relational, constitutive, and ethical functions that other naming traditions foreground. A complete theory of naming would need to accommodate all of these functions. The present paper establishes the referential structural commonalities and maps the boundary of their scope.

The central finding is that naming problems are structurally unified across domains, but naming theories are not yet unified. Philosophy, linguistics, and computing face the same structural challenges and converge on similar solutions, but they arrive at these solutions from different starting points and embed them in different theoretical frameworks. Whether the structural parallels can be elevated to a genuine unified theory remains an open question -- one that the cross-cultural evidence suggests will require attending to the constitutive and relational dimensions of naming, not only the referential ones.

## References

### Primary Texts

Butler, S., Wermelinger, M., Yu, Y., and Sharp, H. (2010). "Exploring the Influence of Identifier Names on Code Quality: An Empirical Study." *Proceedings of the 14th European Conference on Software Maintenance and Reengineering*, 156-165.

Confucius. *The Analects*. D.C. Lau (trans.). Penguin, 1979.

Donnellan, K. (1970). "Proper Names and Identifying Descriptions." *Synthese*, 21(3-4), 335-358.

Evans, G. (1973). "The Causal Theory of Names." *Proceedings of the Aristotelian Society*, Supplementary Volumes, 47, 187-208.

Evans-Pritchard, E.E. (1940). *The Nuer*. Oxford: Clarendon Press.

Frege, G. (1892). "Uber Sinn und Bedeutung." *Zeitschrift fur Philosophie und philosophische Kritik*, 100, 25-50.

Hofmeister, J., Siegmund, J., and Holt, D.V. (2017). "Shorter Identifier Names Take Longer to Comprehend." *Proceedings of the 26th IEEE International Conference on Software Analysis, Evolution, and Reengineering*, 217-227.

Kripke, S. (1979). "A Puzzle about Belief." In A. Margalit (ed.), *Meaning and Use*. Dordrecht: Reidel, 239-283.

Kripke, S. (1980). *Naming and Necessity*. Cambridge, MA: Harvard University Press.

Lawrie, D., Morrell, C., Feild, H., and Binkley, D. (2006). "What's in a Name? A Study of Identifiers." *Proceedings of the 14th IEEE International Conference on Program Comprehension*, 3-12.

Linnaeus, C. (1753). *Species Plantarum*. Stockholm: Salvius.

Mill, J.S. (1843). *A System of Logic*. London: John W. Parker.

Peirce, C.S. (1931-1958). *Collected Papers of Charles Sanders Peirce*. Cambridge, MA: Harvard University Press.

Putnam, H. (1975). "The Meaning of 'Meaning'." In *Mind, Language and Reality*, 215-271.

Quine, W.V.O. (1948). "On What There Is." *Review of Metaphysics*, 2(5), 21-38.

Russell, B. (1905). "On Denoting." *Mind*, 14(56), 479-493.

Saussure, F. de (1916). *Cours de linguistique generale*. Paris: Payot.

Searle, J. (1958). "Proper Names." *Mind*, 67(266), 166-173.

Star, S.L. and Griesemer, J.R. (1989). "Institutional Ecology, 'Translations' and Boundary Objects." *Social Studies of Science*, 19(3), 387-420.

Wittgenstein, L. (1953). *Philosophical Investigations*. Oxford: Blackwell.

Xunzi. "Rectifying Names" (*Zhengming*). In B. Watson (trans.), *Xunzi: Basic Writings*. Columbia University Press, 2003.
