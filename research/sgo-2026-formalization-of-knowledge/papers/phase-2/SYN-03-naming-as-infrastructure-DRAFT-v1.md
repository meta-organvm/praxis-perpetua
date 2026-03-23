---
sgo_id: SGO-2026-SYN-003
title: "Names That Hold"
tier: Paper (synthesis)
status: LOCAL (first draft)
target_venues: [JASIST, Information and Organization, arXiv cs.SE]
dependencies: [RP-04, RP-03, RP-05]
bridges: [Adventure 3, Adventure 4, Adventure 5]
date: 2026-03-21
---

# Names That Hold: How Naming Conventions Function as Organizational Infrastructure in Sociotechnical Systems

**SGO-2026-SYN-003 -- Cross-Adventure Synthesis Paper**
**Bridges:** RP-04 (The Naming Problem), RP-03 (Rhizome vs. Hierarchy), RP-05 (Latour's Network Ontology)

---

## Abstract

Naming conventions are typically treated as matters of style -- aesthetic preferences, team standards, or ergonomic choices with no deep structural consequences. This paper argues otherwise. Drawing on three bodies of theory -- the philosophy of naming (Frege, Kripke, Saussure, Wittgenstein), organizational topology (Deleuze and Guattari's rhizome, McCulloch's heterarchy, scale-free network theory), and actor-network theory (Latour, Callon, Star and Griesemer) -- we demonstrate that naming conventions function as organizational infrastructure: invisible when working, failure-revealing when broken, and constitutive of the organizational topologies they appear merely to describe. We develop the thesis that names in sociotechnical systems operate as boundary objects in Star and Griesemer's precise sense: plastic enough to be interpreted differently by different communities (human readers, AI parsers, automated tooling, management dashboards) yet robust enough to maintain structural coherence across these interpretive contexts. We further argue that the choice between hierarchical naming (DNS, file paths, taxonomic binomials) and flat naming (UUIDs, hashtags, content-addressable hashes) is not merely a technical decision but an organizational one, encoding and enforcing distinct topologies of authority, discovery, and accountability. Through a case study of a double-hyphen naming convention in a multi-repository software system, we derive five design principles for naming infrastructure that is stable under organizational change, interpretable at multiple levels of expertise, and capable of encoding structure without requiring it. The paper contributes to infrastructure studies, information science, and science and technology studies by showing that the humble act of choosing a name is simultaneously an ontological commitment, a governance decision, and an architectural choice.

**Keywords:** naming conventions, infrastructure studies, boundary objects, actor-network theory, organizational topology, namespaces, immutable mobiles, rhizome, hierarchy, sociotechnical systems

---

## 1. Introduction

Consider what happens when you type a file path: `/organvm-iii-ergon/sema-metra--alchemica-mundi/src/engine.py`. Before a single byte is read, the path has already communicated a cascade of structural information. The leading slash anchors the name in an absolute hierarchy. The first segment (`organvm-iii-ergon`) declares organizational membership -- a Roman numeral encoding position in a larger taxonomy. The second segment (`sema-metra--alchemica-mundi`) uses a double-hyphen convention to separate function from descriptor, encoding a relationship between what the component does and what domain it operates in. The remaining segments (`src/engine.py`) follow a familiar convention that every programmer recognizes. All of this information is carried by the name alone, before any file is opened, any code is read, any documentation is consulted.

Now consider what happens when this name breaks. A reorganization moves the component from organ III to organ IV, but the path still says `organvm-iii-ergon`. A refactoring changes the engine's purpose, but the name `sema-metra` (measuring signs) persists. An automated tool parses the double-hyphen as a single separator and misclassifies the repository. In each case, the failure is not merely cosmetic. It produces confusion, misrouted dependencies, broken automation, and -- most insidiously -- a divergence between the name's claims and the system's reality that slowly erodes trust in the entire naming regime.

These observations point to a thesis that this paper develops: **naming conventions are not stylistic choices layered atop organizational structure; they are organizational infrastructure in their own right.** They encode, enforce, and constitute the topologies of the systems they name. When naming conventions are well-designed, they are invisible -- taken for granted, relied upon without conscious attention, like plumbing or electrical wiring. When they fail, the organizational structures they supported become visible precisely through their collapse.

This thesis sits at the intersection of three bodies of theory that have not been systematically connected. First, the philosophy of naming -- from Frege's (1892) sense/reference distinction through Kripke's (1980) rigid designators to Wittgenstein's (1953) language games -- provides the conceptual vocabulary for understanding what names do and how they fail. Second, the literature on organizational topology -- Deleuze and Guattari's (1980) rhizome, McCulloch's (1945) heterarchy, Barabasi and Albert's (1999) scale-free networks, and Scott's (1998) analysis of legibility -- provides the structural framework for understanding the organizational forms that names encode. Third, actor-network theory (ANT) -- Latour's (1987) immutable mobiles, Callon's (1986) translation, and Star and Griesemer's (1989) boundary objects -- provides the relational vocabulary for understanding how names travel across contexts, how they mediate between communities, and how they participate in the constitution of the networks they describe.

The synthesis is this: naming conventions are boundary objects that simultaneously enable hierarchical legibility and rhizomatic connectivity. A hierarchical name (like a DNS address or a Linnaean binomial) compresses organizational structure into a string, making the system legible to a central observer. A rhizomatic name (like a UUID or a hashtag) enables lateral discovery and connection without presupposing any organizational hierarchy. The most effective naming conventions in complex sociotechnical systems do both -- encoding enough structure to support hierarchical navigation while remaining flexible enough to support lateral recombination.

The paper proceeds as follows. Section 2 establishes names as infrastructure, drawing on infrastructure studies to identify the properties that naming conventions share with roads, sewers, and electrical grids. Section 3 analyzes how hierarchical naming systems encode and enforce tree-like organizational structure. Section 4 examines how flat and rhizomatic naming systems enable lateral connectivity at the cost of legibility. Section 5 develops the central theoretical contribution: names as boundary objects and immutable mobiles, with a case study of the double-hyphen convention. Section 6 derives design principles for naming infrastructure. Section 7 concludes.

---

## 2. Names as Infrastructure

### 2.1 Infrastructure Studies: What Makes Something Infrastructure?

The concept of infrastructure has undergone significant theoretical development since Star and Ruhleder's (1996) foundational essay "Steps Toward an Ecology of Infrastructure." Their key insight was that infrastructure is not a fixed category of objects but a relational property: something *becomes* infrastructure in relation to organized practices. A railroad is infrastructure for a commuter; it is a topic of inquiry for an engineer; it is a barrier for a pedestrian trying to cross the tracks. Infrastructure is defined not by its materiality but by its position in networks of use.

Star and Ruhleder identify eight properties of infrastructure that distinguish it from mere tools or technologies:

1. **Embeddedness.** Infrastructure is sunk into and inside of other structures, social arrangements, and technologies.
2. **Transparency.** Infrastructure is transparent to use, in the sense that it does not have to be reinvented each time.
3. **Reach or scope.** Infrastructure has reach beyond a single event or site of practice.
4. **Learned as part of membership.** The conventions of infrastructure are learned as part of becoming a member of a community of practice.
5. **Links with conventions of practice.** Infrastructure shapes and is shaped by the conventions of a community.
6. **Embodiment of standards.** Infrastructure embeds and enforces standards.
7. **Built on an installed base.** Infrastructure does not grow de novo; it inherits strengths and limitations from existing arrangements.
8. **Becomes visible upon breakdown.** The normally invisible quality of infrastructure becomes visible when it breaks.

Every one of these properties applies to naming conventions. A naming convention is embedded in code, documentation, file systems, and communication practices. It is transparent to experienced practitioners -- a seasoned Java developer reads `com.google.common.collect.ImmutableList` without consciously processing the hierarchical namespace. It extends beyond any single artifact or interaction. It is learned as part of socialization into a development team or scientific discipline. It shapes and is shaped by how people talk about their work. It embodies standards -- often formally codified in style guides, linters, or international codes of nomenclature. It builds on existing conventions rather than starting from scratch. And it becomes agonizingly visible when it breaks -- when the name says one thing and the reality says another, when two teams use different names for the same concept, when an automated tool fails because a name violates an undocumented assumption.

### 2.2 Names as Invisible, Taken-for-Granted, and Failure-Revealing

The invisibility of names is not incidental but constitutive of their function. A name that demands attention is a name that has failed. The Linnaean binomial *Homo sapiens* succeeds precisely because a biologist can use it without thinking about the Latin roots, the historical convention, the international code of zoological nomenclature that governs it, or the political negotiations that produced the governance structure. The name is infrastructure: it works in the background, carrying information silently.

This invisibility makes naming conventions peculiarly resistant to deliberate design. Engineers will spend weeks debating database schemas but settle on naming conventions in an afternoon. Organizations will invest millions in enterprise architecture but leave naming to individual teams. The irony is that naming conventions typically outlast the architectures they were designed to serve. A variable named `userId` will be copied, adapted, and propagated across codebases long after the original user model has been redesigned. A file path like `/etc/passwd` persists decades after it ceased to contain passwords. The name becomes an archaeological stratum -- evidence of past decisions that constrains present possibilities.

Bowker and Star (2000) call this phenomenon "infrastructural inversion": the deliberate foregrounding of background conditions. To study naming conventions as infrastructure is to perform an infrastructural inversion -- to make visible what is normally invisible, to examine the conditions of possibility that names create and foreclose.

### 2.3 The Double Life of Names: Rigid Designation and Social Convention

Names lead a double life. On one hand, they function as rigid designators in Kripke's (1980) sense: a name, once fixed to a referent through an initial baptism, picks out the same entity across all contexts. The DNS name `google.com` refers to a specific network entity regardless of who types it, what browser they use, or what they know about Google's corporate structure. In this capacity, names are technical instruments -- mechanisms for reference-fixing that must be unambiguous, stable, and machine-processable.

On the other hand, names function as social conventions in Saussure's (1916) sense: the relationship between signifier and signified is arbitrary, maintained by communal agreement, and embedded in a system of differences. The name `google.com` also carries connotations, associations, brand identity, and cultural meaning that no machine processes but every human reader perceives. The choice of `google` over a more descriptive name was a social act; its persistence is a social achievement; its meaning shifts as the company's role in society evolves.

This double life -- rigid designator and social sign -- is not a tension to be resolved but a productive duality that gives names their infrastructural power. As rigid designators, names provide the stable reference that technical systems require. As social signs, names provide the interpretive flexibility that human communities require. A naming convention that honors only the technical function (pure UUIDs, numeric identifiers) loses the human dimension. A naming convention that honors only the social function (evocative but ambiguous names, unrestricted natural language) loses the technical dimension. Infrastructure must serve both.

Frege's (1892) distinction between sense (*Sinn*) and reference (*Bedeutung*) formalizes this duality. Two names can share a reference -- `userId` and `account_holder_id` may point to the same database row -- while differing in sense, presenting the referent under different "modes of access." In infrastructure terms, the reference is the technical function (which entity does this name pick out?) and the sense is the social function (how does this name present the entity to its human users?). A robust naming convention preserves both.

---

## 3. Names in Hierarchies

### 3.1 Hierarchical Naming: DNS, File Paths, Taxonomic Names, Org Charts

The most familiar naming conventions are hierarchical. A domain name (`mail.google.com`) reads from specific to general, encoding a tree: the host `mail` is a child of the domain `google`, which is a child of the top-level domain `com`, which is a child of the DNS root. A file path (`/usr/local/bin/python3`) traverses a tree from root to leaf. A Linnaean binomial (*Homo sapiens*) encodes a position in a taxonomic tree: genus *Homo*, species *sapiens*, nested within family, order, class, phylum, kingdom. A corporate email address (`j.smith@finance.acme.com`) encodes organizational membership: person within department within company.

In each case, the name is a *serialized tree traversal*. It compresses a path through a hierarchical structure into a linear string. The hierarchy pre-exists the name -- or rather, the naming convention and the hierarchy are co-constitutive. DNS did not merely name an existing internet hierarchy; it created the hierarchy by making it the basis for name resolution. The Linnaean system did not merely label an existing classification; it made the classification operational by embedding it in the name's structure. The file system path did not merely describe an existing directory tree; it made the tree navigable by encoding its structure in the name.

This observation is central to the paper's thesis: hierarchical naming conventions do not merely describe hierarchical organization; they constitute it. The act of naming is simultaneously an act of organizing.

### 3.2 Names as Compression: Encoding Hierarchy into String Structure

From an information-theoretic perspective, a hierarchical name is a compression scheme. The name `com.google.common.collect.ImmutableList` encodes at least five levels of organizational information in a single string: top-level domain (commercial), organization (Google), module (common libraries), sub-module (collections), and class (ImmutableList). A reader who knows the convention can decompress this string into a rich understanding of the entity's position in the organizational hierarchy, its relationship to other entities at the same level, and its relationship to entities at higher and lower levels.

This compression has a specific character: it is *lossy in the lateral dimension and lossless in the vertical dimension*. The name tells you everything about the entity's hierarchical ancestry (its parent, grandparent, and so on up to the root) but nothing about its siblings, cousins, or unrelated entities at other positions in the tree. This asymmetry is not a bug but a feature: it reflects the fundamental property of hierarchical organization, which reduces the combinatorial explosion of possible connections to a manageable tree by discarding lateral relationships.

The Linnaean system exemplifies this compression at its most elegant. The binomial *Panthera leo* encodes genus and species, but the genus name *Panthera* further implies family Felidae, order Carnivora, class Mammalia, and so on up the tree. A biologist reading the name can immediately infer a vast network of relationships -- not because the name explicitly encodes them all, but because the naming convention is embedded in a shared understanding of the taxonomic hierarchy. The name is a key that unlocks a structure stored elsewhere -- in textbooks, in databases, in the biologist's trained memory.

In computing, the same principle operates through namespaces. A namespace is, formally, a set of names structured to ensure uniqueness within a scope (Wikipedia, "Namespace"). Hierarchical namespaces allow name reuse across different contexts: `java.util.List` and `java.awt.List` coexist because the namespace disambiguates. The namespace hierarchy is an explicit organizational architecture, and the names within it are compressed representations of position within that architecture.

### 3.3 The Legibility Function of Hierarchical Names

James C. Scott's *Seeing Like a State* (1998) provides the key framework for understanding why hierarchical naming is so persistent: it produces legibility. Scott documents how states impose standardized naming systems -- surnames, cadastral maps, standardized weights and measures -- to make populations and territories legible to central administration. Before the imposition of fixed surnames, European peasants used contextual names (John the Miller, John of the Hill) that were perfectly functional locally but opaque to a distant tax collector. The state's demand for legibility -- the ability to identify, count, and track individuals from a central position -- drove the adoption of fixed, hierarchical naming.

The same dynamic operates in every large-scale naming system. IUPAC chemical nomenclature makes the molecular world legible to chemists by encoding structure in the name. The Dewey Decimal System makes library collections legible to librarians by encoding subject classification in the call number. Java package naming conventions make large codebases legible to developers by encoding organizational provenance in the fully qualified class name.

Legibility, in Scott's analysis, serves power. The state imposes legibility to facilitate taxation, conscription, and governance. But legibility also serves coordination. A developer navigating an unfamiliar codebase relies on hierarchical naming to orient themselves. A scientist reading an unfamiliar paper relies on taxonomic naming to understand the organisms discussed. A user typing a URL relies on DNS naming to reach the correct server. Hierarchical naming makes complex systems navigable by a central observer -- whether that observer is a state, a developer, or a machine.

### 3.4 Failure Mode: When the Hierarchy Changes but the Names Don't

The fundamental failure mode of hierarchical naming is rigidity. Hierarchical names encode a specific organizational structure at the moment of naming. When the organization changes -- when departments merge, when modules are refactored, when species are reclassified -- the names lag behind. The result is a growing gap between the name's claims and the system's reality.

This failure has a Kripkean dimension. If names are rigid designators, fixed to their referents by an initial baptism and transmitted through a causal chain, then the name `/etc/passwd` still refers to the password file even though it no longer contains passwords. The name rigidly designates the file across the system's evolution. But the name also carries a descriptive sense -- it implies that the file has something to do with passwords -- that is now false. The rigid designation succeeds while the descriptive sense fails. Users who rely on the sense (expecting to find passwords) are misled; users who rely on the reference (knowing to look in that file for user account information) are not.

In organizational contexts, this rigidity manifests as "naming debt" -- the accumulated cost of names that no longer accurately describe what they name. A company reorganizes its divisions, but the directory structure still reflects the old organization. A software system is refactored, but the module names still reflect the original architecture. A scientific field revises its classification, but the old names persist in the literature. Naming debt compounds over time and imposes cognitive overhead on every new participant who must learn not only what names mean but also how they are misleading.

The deeper problem is that hierarchical names encode a particular *view* of the organization -- the view from the top, the central observer's perspective. When the organization is viewed from a different angle, the hierarchy may not apply. A biologist studying horizontal gene transfer sees relationships that the Linnaean tree does not encode. A developer tracing a runtime dependency sees connections that the package namespace hierarchy does not capture. The hierarchy inscribed in the name is one possible organization among many, but its inscription in the name gives it a persistence and authority that alternatives lack.

---

## 4. Names in Rhizomes

### 4.1 Flat Naming: UUIDs, Hashes, Content-Addressable Storage

At the opposite pole from hierarchical naming stand flat naming systems: names that carry no structural information whatsoever. A UUID (Universally Unique Identifier) like `550e8400-e29b-41d4-a716-446655440000` identifies an entity uniquely but reveals nothing about its nature, its relationships, or its position in any organizational hierarchy. A content-addressable hash like `sha256:a3f2b...` identifies a piece of content by its cryptographic digest, guaranteeing that the name is permanently bound to exactly that content but encoding no information about what the content is, who created it, or where it belongs.

Flat names embody the rhizomatic principle that Deleuze and Guattari (1980) describe: any point can connect to any other point without predefined ordering. A UUID can be attached to any entity in any system without regard to organizational structure. A content hash can reference any content without regard to provenance or context. There is no root, no hierarchy, no predetermined path from one name to another.

The philosophical basis for flat naming lies in the direct reference theory of names (Mill 1843; Kripke 1980). A UUID is a pure rigid designator: it picks out its referent without attributing any properties. It has reference without sense -- or rather, its sense is exhausted by its reference. This is the logical extreme of Kripke's program: a name that is purely a tag, carrying no descriptive content, immune to changes in the properties or organizational position of its referent.

The Uniform Resource Identifier (URI) system occupies an instructive middle position. A URI is defined as "a unique sequence of characters that identifies an abstract or physical resource" (IETF RFC 3986). URIs can be hierarchical (URLs like `https://example.com/path/to/resource`) or flat (URNs like `urn:isbn:0451450523`). The URI system's ambition -- a universal namespace for all digital resources -- reveals the tension between the desire for hierarchical legibility (URLs) and the need for persistent, context-independent identification (URNs and persistent identifiers like DOIs). A Digital Object Identifier (DOI) such as `10.1000/xyz123` is designed to be a persistent identifier: stable, resolvable, and independent of the object's physical location or organizational context (ISO 26324). The DOI system achieves naming stability by separating the name from the location -- the DOI persists even as the resource moves between servers, institutions, or domains.

### 4.2 Names as Search Keys: Tagging, Folksonomies, Semantic Linking

Between the poles of hierarchical naming and pure flat naming lies a rich intermediate space: names that enable discovery through lateral connection rather than hierarchical traversal. Tags, hashtags, folksonomies, and semantic links all function as names in this intermediate sense.

A folksonomy -- a portmanteau of "folk" and "taxonomy" -- is a classification system created collaboratively by end users rather than imposed by a taxonomic authority. Where a taxonomy assigns each item to exactly one position in a hierarchy (the species belongs to one genus, the file belongs to one directory), a folksonomy allows an item to bear many tags simultaneously, each reflecting a different user's perspective. A photograph on Flickr tagged `#sunset #tokyo #2024 #iPhone #melancholy` participates in five different organizational schemes at once, none of them hierarchical.

The semiotic character of tags differs fundamentally from hierarchical names. In Saussure's (1916) terms, a hierarchical name derives its meaning primarily from its position in a *system of differences* -- `com.google` means what it means partly because it is not `com.amazon` or `org.apache`. A tag derives its meaning primarily from its *associative connections* -- `#sunset` means what it means because of the other entities tagged `#sunset`, a meaning that shifts with every new tagging act. Hierarchical names participate in Saussure's syntagmatic axis (the linear combination of signs); tags participate in the paradigmatic axis (the set of substitutable alternatives at any position).

This semiotic difference has organizational consequences. Hierarchical names support *navigation* -- you can traverse the tree to find what you are looking for. Tags support *search* -- you can query across the entire corpus for entities sharing a property. Navigation assumes you know the structure; search assumes you know a property. The choice between hierarchical naming and tagging is, at bottom, a choice about what kind of knowledge the user is assumed to have.

### 4.3 The Discovery Function of Rhizomatic Names

Rhizomatic names excel at discovery -- at revealing connections that no hierarchical scheme anticipated. The hashtag `#MeToo` connected experiences across industries, countries, and contexts that no organizational hierarchy would group together. The npm package name `left-pad` connected thousands of projects to a single dependency that no dependency tree visualized. Git commit hashes connect code changes across forks, branches, and repositories without regard to organizational provenance.

This discovery function corresponds to what RP-03 identifies as the "search" capacity of rhizomatic organization. Where hierarchy compresses the space of possible connections into a navigable tree (discarding lateral links), rhizomatic naming preserves the full space of possible connections, making every entity discoverable from every other through shared properties, tags, or direct reference.

The philosophical underpinning is Wittgenstein's (1953) concept of family resemblance. Hierarchical naming assumes that entities belong to well-defined categories with necessary and sufficient membership conditions. Rhizomatic naming assumes that entities cluster by overlapping similarities -- family resemblances -- that do not reduce to a single classificatory tree. A repository tagged `#generative-art #python #audio` participates in three family-resemblance clusters, none of which subsumes the others.

### 4.4 Failure Mode: Illegibility, Collision, Orphaning

The failure modes of rhizomatic naming are the mirror image of hierarchical naming's failures. Where hierarchical naming fails through rigidity (the name outlasts the hierarchy it encoded), rhizomatic naming fails through illegibility, collision, and orphaning.

**Illegibility.** Flat names are opaque to human readers. A UUID communicates nothing about what it identifies. A content hash communicates nothing about what the content is. In the absence of supplementary infrastructure (registries, indices, documentation), flat names are useless for navigation. This is the cost of abandoning hierarchy: the name no longer encodes the organizational context that makes it interpretable.

**Collision.** When names carry no structural information, the likelihood of accidental collision depends entirely on the size of the namespace. UUIDs solve this through sheer combinatorial space (2^128 possibilities). But human-readable flat names (like npm package names) are constrained by memorability, which limits the effective namespace. The result is name-squatting, disputes, and the `left-pad` problem: a single flat name in a globally shared namespace becomes an inadvertent obligatory passage point, concentrating dependency risk in a name that was never designed to bear it.

**Orphaning.** When a flat name loses its connection to metadata, context, or provenance, it becomes an orphan -- a reference with no interpretive frame. A UUID in a database column, disconnected from the registry that mapped it to a meaningful entity, is just a string of hexadecimal digits. Hierarchical names resist orphaning because the hierarchy itself provides context; flat names depend on external context that can be lost.

These failure modes reveal that rhizomatic naming, like rhizomatic organization, faces the "emergence trap" identified in RP-03: systems designed as flat tend to develop de facto hierarchies through use. The npm registry is formally flat (any name is available on a first-come-first-served basis), but in practice, a few packages (`react`, `lodash`, `express`) function as hubs in a scale-free network, concentrating dependency and influence in a way that resembles hierarchy without the legibility that hierarchy provides.

---

## 5. Names as Boundary Objects

### 5.1 Star and Griesemer's Boundary Objects

The concept of boundary objects, introduced by Susan Leigh Star and James R. Griesemer (1989), provides the theoretical key for understanding how names function across communities. Star and Griesemer developed the concept through a study of Berkeley's Museum of Vertebrate Zoology, where amateur collectors, professional scientists, and university administrators all used the same specimens, field notes, and classification systems -- but used them differently, for different purposes, with different interpretive frameworks.

A boundary object, in their definition, is "plastic enough to adapt to local needs and constraints of the several parties employing them, yet robust enough to maintain a common identity across sites" (Star and Griesemer 1989, 393). Boundary objects are not consensus objects -- they do not require that all parties agree on their meaning. Rather, they are objects that maintain enough structural coherence to enable collaboration while permitting enough interpretive flexibility to accommodate divergent interests.

Star and Griesemer identify four types of boundary objects:

1. **Repositories** -- ordered collections of objects indexed in a standardized way (libraries, museums, databases).
2. **Ideal types** -- abstract representations that are adaptable to local sites (maps, diagrams, atlases).
3. **Coincident boundaries** -- objects with the same boundaries but different internal contents (political maps that agree on borders but disagree on what matters within them).
4. **Standardized forms** -- methods of common communication across dispersed groups (forms, protocols, formats).

Naming conventions participate in all four types. A controlled vocabulary is a repository of standardized terms. A naming pattern (like `camelCase` or the `get/set` prefix convention) is an ideal type -- abstract enough to be adapted to any domain. A namespace boundary (the dot in `com.google`) is a coincident boundary -- both sides agree on where the boundary falls but may disagree on what it means. A naming convention documented in a style guide is a standardized form enabling communication across dispersed teams.

### 5.2 Names Interpreted Differently by Different Communities

The boundary-object character of names becomes vivid when we trace a single name through its interpretive communities. Consider the fully qualified class name `com.organvm.engine.metrics.RepoHealthScore`. This name is interpreted differently by at least four communities:

**Human developers** read the name as a narrative: this is a class that computes a health score for repositories, part of the metrics module of the ORGANVM engine, produced by the `organvm` organization in the commercial TLD. The developer uses the name for navigation (finding the class in the codebase), comprehension (understanding what it does), and communication (referring to it in code reviews and discussions). The developer's interpretation draws on descriptive sense -- the name means what it describes.

**The Java compiler** reads the name as a hierarchical address: a sequence of namespace segments terminating in a class identifier. The compiler uses the name for resolution (finding the corresponding `.class` file on the classpath), type-checking (verifying that `RepoHealthScore` exists and has the expected interface), and linking (connecting references to definitions). The compiler's interpretation is purely referential -- the name means what it points to.

**Automated documentation tools** read the name as structured data: each segment can be extracted, indexed, and cross-referenced. The tool generates API documentation organized by package, hyperlinks class references, and produces dependency graphs. The tool's interpretation is syntactic -- the name means what can be parsed from its structure.

**A project manager** reads the name (if they encounter it at all) as an organizational signal: this belongs to organ III (ergon, commercial products), it involves metrics, it seems to assess repository health. The manager uses the name for governance decisions -- should this component be promoted? does it belong in this organ? The manager's interpretation is institutional -- the name means what it implies about organizational jurisdiction.

The same name serves all four communities because it is a boundary object: structurally coherent (the hierarchical format is invariant) yet interpretively flexible (each community extracts different meaning). This is not a deficiency to be corrected but a feature to be preserved. A naming convention that served only one community's needs -- purely machine-parsable identifiers, or purely human-readable descriptions -- would fail as infrastructure precisely because infrastructure must serve heterogeneous communities simultaneously.

### 5.3 Latour's Immutable Mobiles: Names That Travel Without Distortion

Bruno Latour's concept of the immutable mobile complements Star and Griesemer's boundary object by emphasizing a different property: not interpretive flexibility but referential stability across contexts. An immutable mobile is an inscription -- a document, map, diagram, or notation -- that can be transported from one site to another without transformation (Latour 1987, 227). Scientific papers, legal contracts, and standardized metrics are immutable mobiles: they allow "action at a distance" by ensuring that what is read at the destination is the same as what was written at the origin.

Names are among the most elementary immutable mobiles. The DOI `10.1000/xyz123` can be printed in a journal, typed into a browser, embedded in a citation database, and parsed by an API -- in each context, it resolves to the same digital object. The referential function is preserved across contexts; the name is immutable (it does not change) and mobile (it travels freely between sites of use).

In sociotechnical systems, names function as immutable mobiles in a specific way: they carry organizational structure across the boundary between human cognition and machine execution. When a developer writes a function call `metrics.calculate_repo_health(repo_id)`, the names travel from the developer's cognitive model (where `repo_health` carries descriptive sense and professional context) into the machine's execution model (where `repo_health` is an opaque identifier resolved to a memory address). The names are immutable -- the same string appears in both contexts -- and mobile -- they cross the boundary between human and machine interpretation.

This immutability is what gives names their infrastructural power. Because the name does not change as it travels, it can serve as a coordination mechanism between communities that have no other shared context. The developer and the compiler do not negotiate the meaning of `RepoHealthScore`; they each interpret it according to their own conventions, and the name's structural invariance ensures that their interpretations, though different, remain compatible. This is precisely the mechanism of action at a distance that Latour attributes to immutable mobiles: coordination without consensus, alignment without agreement.

The concept of translation in actor-network theory (Callon 1986) further illuminates how names function in networks. Translation is the process by which diverse elements are aligned into a coherent network: problematization (defining a shared problem), interessement (locking actors into roles), enrollment (actors performing their assigned roles), and mobilization (one actor speaking for others). Names participate in each phase. The act of naming a component `RepoHealthScore` problematizes the domain (there is such a thing as repo health, and it can be scored). The naming convention's rules serve as interessement devices, constraining what kinds of names are acceptable. The adoption of the name by developers, tools, and documentation constitutes enrollment. And when someone refers to "the RepoHealthScore module" in a meeting, they are performing mobilization -- speaking for the code, the metrics, and the organizational decisions embodied in the name.

### 5.4 The Double-Hyphen Convention as Case Study

The double-hyphen naming convention used in the ORGANVM multi-repository system provides a concrete case study for the boundary-object thesis. The convention works as follows:

- **Single hyphen** (`-`) separates words within a concept: `sema-metra` (sign measurement), `alchemica-mundi` (world alchemy).
- **Double hyphen** (`--`) separates function from descriptor: `sema-metra--alchemica-mundi` separates the functional designation (what the component does: measure signs) from the descriptive designation (what domain it operates in: the alchemical world).

This convention is simultaneously hierarchical and rhizomatic. It is hierarchical in that it encodes a structural relationship: the function (left of `--`) is the primary organizational axis, the descriptor (right of `--`) is the secondary axis. The function `sema-metra` groups all components that measure signs, regardless of their descriptive domain; the descriptor `alchemica-mundi` groups all components that operate in the alchemical-world domain, regardless of their function. The double-hyphen thus creates a two-level hierarchy: function > descriptor.

But the convention is also rhizomatic. Any function can be combined with any descriptor. There is no predefined list of valid combinations; the space of possible names is the Cartesian product of all function-concepts and all descriptor-concepts. New combinations can be created without approval from a central authority. The naming convention enables lateral recombination -- any function-concept can be connected to any descriptor-concept -- while maintaining enough structure to support hierarchical navigation (grouping by function, grouping by descriptor).

The convention exhibits all the properties of a boundary object:

**Plasticity.** Human readers interpret the double-hyphen as a semantic separator carrying information about the component's purpose and domain. Machine tools can parse it as a delimiter for automated classification. Project managers can use it to identify organizational jurisdiction (the function part maps to an organ, the descriptor part maps to a domain). Each community reads the same convention differently.

**Structural coherence.** Despite these different interpretations, the convention maintains invariant properties: exactly one `--` separator, valid hyphenated words on each side, consistent parsing rules. These invariants ensure that the interpretations, though different, remain compatible.

**Immutability.** The name travels unchanged between contexts: from a GitHub repository name to a `seed.yaml` declaration to a conversation in a planning session to a system-metrics dashboard. The string is the same in every context.

**Encoding of organizational topology.** The function/descriptor split encodes a specific claim about organizational structure: that the primary axis of organization is *what things do* (function) and the secondary axis is *what domain they operate in* (descriptor). This is an ontological commitment in Quine's sense: to use the double-hyphen convention is to assert that function-descriptor is the right way to carve the organizational world at its joints.

The convention also illustrates the Wittgensteinian dimension of naming. The same name participates in different language games in different contexts. In a Git command (`git clone sema-metra--alchemica-mundi`), the name is an address. In a technical discussion ("the sema-metra engine measures signs in the alchemical domain"), the name is a description. In a governance decision ("should sema-metra--alchemica-mundi be promoted from LOCAL to CANDIDATE?"), the name is a bureaucratic identifier. The convention works not because all users agree on what the name means but because all users can extract what they need from the same syntactic structure.

---

## 6. Design Principles for Naming Infrastructure

The preceding analysis -- of names as infrastructure, of hierarchical and rhizomatic naming as complementary strategies, of names as boundary objects and immutable mobiles -- yields a set of design principles for naming conventions in complex sociotechnical systems.

### 6.1 Names Should Encode Structure Without Requiring It

The most effective naming conventions encode organizational structure as a resource for interpretation without making that structure a prerequisite for use. Hierarchical namespaces like Java packages encode the organizational hierarchy for those who know how to read it, but the name `ImmutableList` is meaningful even to a developer who ignores the `com.google.common.collect` prefix. The double-hyphen convention encodes the function/descriptor distinction for those who know the convention, but the full name `sema-metra--alchemica-mundi` is at least suggestive even to a reader encountering it for the first time.

The principle is: **structure as affordance, not as gate.** A name should be more useful to someone who understands the convention than to someone who does not, but it should not be useless to the latter. This is the boundary-object property in action: the name must serve communities with different levels of structural knowledge.

In practice, this means combining human-readable elements (descriptive words, recognizable roots) with machine-parsable structure (consistent delimiters, predictable formats, hierarchical segments). A name like `ORGANVM-III-ERGON--sema-metra--alchemica-mundi` encodes organ membership, organ name, function, and descriptor -- but each segment is also a recognizable word or abbreviation. The structure enables automated processing; the readability enables human navigation.

### 6.2 Names Should Be Stable Under Organizational Change

Naming debt -- the accumulated cost of names that no longer describe what they name -- is one of the most insidious forms of technical debt. It compounds silently, imposing cognitive overhead on every new participant and every automated tool that relies on naming conventions.

The principle for stability is: **names should refer to what is stable, not what is volatile.** In Kripke's terms, a good name is baptized to a referent that persists, not to a description that may change. A repository named `auth-service` is baptized to a description (it handles authentication) that may change as the service evolves. A repository named `sema-metra--alchemica-mundi` is baptized to a more abstract referent (the intersection of sign-measurement and alchemical-world domains) that is likely to persist even as the implementation changes.

The URI system provides a model: the persistent identifier (DOI, ISBN, ORCID) separates the name from the location. The name persists even as the resource moves. Similarly, naming conventions should separate the name from the organizational structure. A name that encodes what a thing *is* (its function and domain) is more stable than a name that encodes where a thing *sits* (its position in a hierarchy that may be reorganized).

This principle is in tension with the legibility function of hierarchical naming: names that encode organizational position are legible precisely because they reflect the current structure. The resolution is to encode structure at the level that changes least frequently. Function and domain change less frequently than organizational reporting lines. Conceptual category changes less frequently than physical location. The art is identifying the right level of abstraction.

### 6.3 Names Should Be Interpretable at Multiple Levels of Expertise

A naming convention in a large sociotechnical system is used by people with radically different levels of expertise: domain experts, novice developers, automated tools, managers reading dashboards, AI systems parsing code. The convention must be interpretable at each level without requiring expertise at any other level.

This is the boundary-object property restated as a design principle: **design for heterogeneous interpretive communities.** The convention should provide shallow interpretability (a novice can extract basic information from the name's surface form) and deep interpretability (an expert can extract rich structural and semantic information from the same name).

Consider the biological binomial *Escherichia coli*. A layperson can recognize it as a species name. A biology student can identify the genus (*Escherichia*) and infer membership in the Enterobacteriaceae. An expert can read a history of taxonomic revision in the genus name (honoring Theodor Escherich) and a description in the species name (*coli*, of the colon). The same name serves all three levels because the Linnaean convention has layered interpretability built into its structure.

Software naming conventions can aspire to the same property. The double-hyphen convention `sema-metra--alchemica-mundi` is interpretable at multiple levels: the novice sees two hyphenated phrases separated by a double hyphen; the intermediate user sees a function/descriptor split; the expert sees a specific ontological claim about the relationship between sign-measurement and alchemical-world domains. No level of interpretation requires or invalidates the others.

### 6.4 Names Should Fail Visibly

When a name ceases to accurately describe its referent, the failure should be detectable -- ideally by automated tools, but at minimum by attentive human readers. The infrastructural property of "visible upon breakdown" should be engineered into the naming convention, not left to chance.

Visible failure requires structural constraints. A naming convention with no formal rules cannot fail formally -- any string is a valid name, so no name is wrong. A naming convention with explicit structural requirements (delimiters in the right positions, valid vocabulary in each segment, consistent formatting) can be validated automatically, making violations visible.

The controlled vocabulary is the most direct tool for visible failure. A controlled vocabulary -- a predefined set of preferred terms for indexing and retrieval -- restricts the naming space to terms that have been explicitly authorized. When a new name violates the controlled vocabulary, the violation is immediately visible. The cost is flexibility (novel concepts require vocabulary updates); the gain is precision and early detection of naming drift.

In ANT terms, a naming convention with visible failure modes is a mediator rather than an intermediary. An intermediary transports without transforming -- you can ignore it. A mediator transforms what passes through it -- you must attend to it. A naming convention that silently accepts any name is an intermediary; a naming convention that validates, constrains, and reports violations is a mediator. Infrastructural robustness demands mediation.

### 6.5 The Namespace as Governance Boundary

Namespaces do not merely organize names; they define governance jurisdictions. The dot in `com.google.common.collect` is not just a hierarchical separator; it is a governance boundary. Google governs what names can appear in the `com.google` namespace. The Apache Software Foundation governs the `org.apache` namespace. The IETF governs the structure of domain names. The International Commission on Zoological Nomenclature governs the use of Linnaean binomials.

This governance function is often underappreciated. The question "what should we name this?" is inseparable from the question "who gets to decide?" A namespace without governance is a commons vulnerable to the tragedy of uncoordinated use: name-squatting, collision, drift, and the erosion of naming conventions through accumulated exceptions. A namespace with governance is a jurisdiction with boundaries, rules, and authorities.

The design principle is: **invest in namespace governance proportional to system scale.** A solo developer needs no namespace governance. A team of ten needs lightweight conventions. A hundred-repository system needs explicit governance: who can create top-level names? What are the rules for naming within each namespace? How are violations detected and resolved? Who arbitrates disputes?

The governance structure of the namespace mirrors the governance structure of the organization. A centralized namespace (like DNS) requires a centralized governance authority (ICANN). A federated namespace (like email domains) requires federated governance (each domain owner governs their subdomain). A flat namespace (like npm) requires -- and often lacks -- governance mechanisms for managing the commons.

The parallel to Callon's obligatory passage point is precise. A namespace authority is an OPP: it mediates all naming acts within its jurisdiction, defining the action program (what names are valid) and extracting concessions (compliance with naming conventions). The strength of the OPP determines the strength of the naming convention. A strong OPP (like ICANN or the ICZN) produces stable, well-governed naming. A weak OPP (like a style guide that is never enforced) produces naming drift.

---

## 7. Conclusion

This paper has argued that naming conventions are organizational infrastructure -- invisible when working, failure-revealing when broken, and constitutive of the organizational topologies they appear merely to describe. The argument rests on three pillars.

First, from the philosophy of naming: names lead a double life as rigid designators (stable references that persist across contexts) and social signs (arbitrary conventions embedded in systems of meaning). This double life gives names their infrastructural power -- they serve both the technical requirement for stable reference and the social requirement for interpretive flexibility.

Second, from organizational topology: the choice between hierarchical naming and rhizomatic naming encodes and enforces distinct organizational forms. Hierarchical naming produces legibility at the cost of rigidity; rhizomatic naming produces connectivity at the cost of legibility. The most effective naming conventions are hybrids that encode structure without requiring it, supporting both hierarchical navigation and lateral discovery.

Third, from actor-network theory: names function as boundary objects (interpreted differently by different communities but maintaining structural coherence) and immutable mobiles (traveling across contexts without transformation). They participate in translation -- the process by which heterogeneous elements are aligned into coherent networks. The double-hyphen case study demonstrates how a naming convention can simultaneously encode hierarchical structure (function > descriptor) and enable rhizomatic recombination (any function with any descriptor).

The five design principles derived from this analysis -- encode structure without requiring it, design for stability under change, enable multi-level interpretation, engineer visible failure, and invest in namespace governance -- provide actionable guidance for practitioners designing naming conventions for complex sociotechnical systems. These principles apply across domains: to software repositories, to scientific nomenclature, to organizational taxonomies, and to the emerging challenge of naming in human-AI collaborative systems where names must be interpretable by human readers, AI parsers, and automated tooling simultaneously.

The paper's central claim is that naming is not a cosmetic concern but a foundational one. To name is to commit to an ontology, to assert organizational structure, to create infrastructure that enables some connections and forecloses others. The naming problem is not a problem to be solved once and forgotten; it is an ongoing practice of infrastructural maintenance -- a practice that, like all infrastructure, becomes visible only when it fails.

---

## References

Barabasi, A.-L. and Albert, R. (1999). "Emergence of Scaling in Random Networks." *Science* 286(5439): 509--512.

Bowker, G.C. and Star, S.L. (2000). *Sorting Things Out: Classification and Its Consequences*. Cambridge, MA: MIT Press.

Callon, M. (1986). "Some Elements of a Sociology of Translation: Domestication of the Scallops and the Fishermen of St. Brieuc Bay." In J. Law (ed.), *Power, Action, and Belief: A New Sociology of Knowledge?* London: Routledge, 196--223.

DeLanda, M. (2006). *A New Philosophy of Society: Assemblage Theory and Social Complexity*. London: Continuum.

Deleuze, G. and Guattari, F. (1980). *A Thousand Plateaus: Capitalism and Schizophrenia*. Trans. B. Massumi. Minneapolis: University of Minnesota Press, 1987.

Frege, G. (1892). "Uber Sinn und Bedeutung." *Zeitschrift fur Philosophie und philosophische Kritik* 100: 25--50.

Gunderson, L.H. and Holling, C.S. (2002). *Panarchy: Understanding Transformations in Human and Natural Systems*. Washington, DC: Island Press.

Haraway, D. (1985). "A Cyborg Manifesto: Science, Technology, and Socialist-Feminism in the Late Twentieth Century." *Socialist Review* 80: 65--108.

Koestler, A. (1967). *The Ghost in the Machine*. London: Hutchinson.

Kripke, S. (1980). *Naming and Necessity*. Cambridge, MA: Harvard University Press.

Latour, B. (1987). *Science in Action: How to Follow Scientists and Engineers Through Society*. Cambridge, MA: Harvard University Press.

Latour, B. (1991). *We Have Never Been Modern*. Trans. C. Porter. Cambridge, MA: Harvard University Press, 1993.

Latour, B. (2005). *Reassembling the Social: An Introduction to Actor-Network-Theory*. Oxford: Oxford University Press.

McCulloch, W.S. (1945). "A Heterarchy of Values Determined by the Topology of Nervous Nets." *Bulletin of Mathematical Biophysics* 7(2): 89--93.

Mill, J.S. (1843). *A System of Logic, Ratiocinative and Inductive*. London: John W. Parker.

Putnam, H. (1975). "The Meaning of 'Meaning'." In *Mind, Language and Reality: Philosophical Papers*, vol. 2. Cambridge: Cambridge University Press, 215--271.

Quine, W.V.O. (1948). "On What There Is." *Review of Metaphysics* 2(5): 21--38.

Raymond, E.S. (1999). *The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary*. Sebastopol, CA: O'Reilly.

Saussure, F. de (1916). *Cours de linguistique generale*. Ed. C. Bally and A. Sechehaye. Paris: Payot. English trans.: *Course in General Linguistics*. New York: McGraw-Hill, 1959.

Scott, J.C. (1998). *Seeing Like a State: How Certain Schemes to Improve the Human Condition Have Failed*. New Haven: Yale University Press.

Star, S.L. and Griesemer, J.R. (1989). "Institutional Ecology, 'Translations' and Boundary Objects: Amateurs and Professionals in Berkeley's Museum of Vertebrate Zoology, 1907--39." *Social Studies of Science* 19(3): 387--420.

Star, S.L. and Ruhleder, K. (1996). "Steps Toward an Ecology of Infrastructure: Design and Access for Large Information Spaces." *Information Systems Research* 7(1): 111--134.

Wittgenstein, L. (1953). *Philosophical Investigations*. Trans. G.E.M. Anscombe. Oxford: Blackwell.

---

*Draft v1 -- SGO-2026-SYN-003. Generated 2026-03-21. Studium Generale ORGANVM.*
