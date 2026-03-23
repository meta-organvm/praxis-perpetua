---
sgo_id: SGO-2026-SYN-003
title: "Names That Hold"
tier: Paper (synthesis)
status: LOCAL (revised draft)
target_venues: [JASIST, Information and Organization, arXiv cs.SE]
dependencies: [RP-04, RP-03, RP-05]
bridges: [Adventure 3, Adventure 4, Adventure 5]
date: 2026-03-21
revision_date: 2026-03-20
version: v2
revision_notes: |
  TRP review required revise-and-re-review (1/3 advance, 1/3 revise, 1/3 fork).
  Key amendments incorporated:
  - Added Section 2.4: cross-cultural naming systems (Chinese, Arabic, Japanese, indigenous)
    mirroring RP-04 v2's cross-cultural section.
  - Reduced boundary-object overuse: term now reserved for cases exhibiting Star and Griesemer's
    four structural types (repositories, ideal types, coincident boundaries, standardized forms).
    Replaced generic uses with more precise terms (coordination artifact, shared reference).
  - Added Section 6.6: the bikeshedding challenge -- empirical evidence on naming's measurable impact.
  - Tightened infrastructure argument with empirical cases of naming failure causing system failure.
  - Acknowledged single-operator limitation of ORGANVM case study more prominently.
---

# Names That Hold: How Naming Conventions Function as Organizational Infrastructure in Sociotechnical Systems

**SGO-2026-SYN-003 -- Cross-Adventure Synthesis Paper**
**Bridges:** RP-04 (The Naming Problem), RP-03 (Rhizome vs. Hierarchy), RP-05 (Latour's Network Ontology)

---

## Abstract

Naming conventions are typically treated as matters of style -- aesthetic preferences with no deep structural consequences. This paper argues otherwise. Drawing on the philosophy of naming (Frege, Kripke, Saussure, Wittgenstein), organizational topology (hierarchy/rhizome spectrum, scale-free network theory), and actor-network theory (Latour, Callon, Star and Griesemer), we demonstrate that naming conventions function as organizational infrastructure: invisible when working, failure-revealing when broken, and constitutive of the organizational topologies they appear merely to describe. We argue that names in sociotechnical systems can operate as boundary objects in Star and Griesemer's precise sense -- when they exhibit the structural features (repositories, ideal types, coincident boundaries, standardized forms) that the concept requires -- and more generally as coordination artifacts that mediate between communities with divergent interpretive needs. A comparative section tests these claims against Chinese, Arabic, Japanese, and indigenous naming systems. Through a case study of a double-hyphen naming convention, we derive five design principles with empirical grounding. The paper contributes to infrastructure studies, information science, and STS by showing that naming conventions have measurable effects on system reliability, maintenance cost, and coordination efficiency.

**Keywords:** naming conventions, infrastructure studies, organizational topology, namespaces, immutable mobiles, hierarchy, sociotechnical systems

---

## 1. Introduction

[Retained from v1 with minor revisions.]

Consider what happens when you type a file path: `/organvm-iii-ergon/sema-metra--alchemica-mundi/src/engine.py`. Before a single byte is read, the path has already communicated a cascade of structural information.

Now consider what happens when this name breaks. A reorganization moves the component from organ III to organ IV, but the path still says `organvm-iii-ergon`. A refactoring changes the engine's purpose, but the name persists. In each case, the failure produces confusion, misrouted dependencies, broken automation, and a divergence between the name's claims and the system's reality.

These observations point to the thesis: **naming conventions are not stylistic choices layered atop organizational structure; they are organizational infrastructure in their own right.**

---

## 2. Names as Infrastructure

### 2.1 Infrastructure Studies: What Makes Something Infrastructure?

Star and Ruhleder's (1996) foundational essay identifies eight properties of infrastructure: embeddedness, transparency, reach, learned as part of membership, links with conventions of practice, embodiment of standards, built on an installed base, and visible upon breakdown. Every one of these properties applies to naming conventions.

### 2.2 Names as Invisible, Taken-for-Granted, and Failure-Revealing

[Retained from v1.]

### 2.3 The Double Life of Names: Rigid Designation and Social Convention

[Retained from v1.]

### 2.4 Cross-Cultural Naming: Testing the Infrastructure Thesis

If naming conventions are genuinely infrastructure -- not merely Western-specific organizational practice -- then the infrastructure properties should appear in naming systems that developed independently of the European philosophical and computational traditions.

**Chinese naming and zhengming.** The Confucian *zhengming* (rectification of names) tradition treats naming as a constitutive political act: names do not merely describe social reality; they *shape* it. This is the infrastructure thesis stated as political philosophy. When names are "incorrect" (when officials are called by titles they do not deserve), social functions break down -- precisely the "visible upon breakdown" property of infrastructure. The zhengming tradition adds a dimension that Western infrastructure studies have not fully developed: naming infrastructure is not politically neutral. The *choice* of which names to use and how to rectify them is always an exercise of power.

**Arabic multi-layered naming.** The traditional Arabic system (ism, nasab, kunya, laqab, nisba) is simultaneously hierarchical (the nasab encodes a genealogical tree) and relational (the kunya encodes a social relationship). It demonstrates that naming infrastructure can encode multiple organizational topologies simultaneously -- a property that the Western convention of single-hierarchy naming (DNS, file paths) typically does not achieve.

**Japanese multi-script naming.** The use of kanji, hiragana, katakana, and romaji for the same name, each carrying different social registers, demonstrates that naming infrastructure can encode social-register information in the *material substrate* of the name itself. This is invisible when working (a Japanese reader processes the script choice without conscious effort) and visible upon breakdown (a name written in the wrong script signals social incompetence or intentional provocation).

**Relational naming in oral cultures.** In systems where names change with social relationships (Nuer context-dependent naming, Australian Aboriginal name taboos), naming infrastructure is *designed for impermanence*. This challenges the assumption, common in both Western philosophy and computing, that naming infrastructure should maximize stability. In these systems, the infrastructure function of naming is served not by stable reference but by *accurate relational indexing* -- the name correctly encodes the current social relationship, and its change upon relationship change is a feature, not a failure.

These cases confirm that naming conventions function as infrastructure across culturally independent traditions. They also reveal that the infrastructure thesis needs qualification: the *form* of naming infrastructure varies with cultural and organizational context, even if the *functional role* (invisible when working, constitutive of organizational structure, visible upon breakdown) is consistent.

---

## 3. Names in Hierarchies

### 3.1 Hierarchical Naming: DNS, File Paths, Taxonomic Names

[Retained from v1.]

### 3.2 Names as Compression

[Retained from v1.]

### 3.3 The Legibility Function of Hierarchical Names

[Retained from v1.]

### 3.4 Failure Mode: When the Hierarchy Changes but the Names Don't

[Retained from v1.]

---

## 4. Names in Rhizomes

### 4.1 Flat Naming: UUIDs, Hashes, Content-Addressable Storage

[Retained from v1.]

### 4.2 Names as Search Keys: Tagging, Folksonomies, Semantic Linking

[Retained from v1.]

### 4.3 The Discovery Function of Rhizomatic Names

[Retained from v1.]

### 4.4 Failure Mode: Illegibility, Collision, Orphaning

[Retained from v1.]

---

## 5. Names as Coordination Artifacts

### 5.1 Star and Griesemer's Boundary Objects: Precise Application

The concept of boundary objects (Star and Griesemer, 1989) has been widely adopted and frequently over-extended. This section applies the concept with precision, distinguishing cases where naming conventions genuinely exhibit the structural features of boundary objects from cases where a less specific term -- *coordination artifact* or *shared reference* -- is more appropriate.

Star and Griesemer identify four structural types of boundary objects: repositories (ordered collections indexed in a standardized way), ideal types (abstract representations adaptable to local sites), coincident boundaries (objects with the same boundaries but different internal contents), and standardized forms (methods of common communication across dispersed groups).

Naming conventions participate in the boundary-object concept when they exhibit these structural features:

- A **controlled vocabulary** is a boundary object of the repository type: an ordered collection of standardized terms that different communities index and use differently.
- A **naming pattern** (camelCase, the get/set prefix convention, the double-hyphen convention) is a boundary object of the ideal-type variety: abstract enough to be adapted to any domain, interpreted differently by developers, compilers, and documentation tools.
- A **namespace boundary** (the dot in `com.google`) is a boundary object with coincident boundaries: both sides of the boundary agree on where it falls but may interpret its significance differently.
- A **style guide** documenting naming conventions is a boundary object of the standardized-form type: a method of common communication across dispersed teams.

However, not every name that is interpreted differently by different communities is a boundary object. A variable name like `count` that a developer and a compiler process differently is better described as a *shared reference* -- a coordination artifact that enables collaboration without requiring the structural features (ordered indexing, abstract adaptability, coincident boundaries, standardized forms) that boundary objects exhibit. The distinction matters because the analytical power of the boundary-object concept depends on its precision. Applying it to every instance of differential interpretation drains it of diagnostic value.

### 5.2 Names Interpreted Differently by Different Communities

[Retained from v1, with "boundary object" replaced by "coordination artifact" where the structural features are absent.]

Consider the fully qualified class name `com.organvm.engine.metrics.RepoHealthScore`. This name is a coordination artifact interpreted differently by at least four communities: human developers (who read it as a narrative about organizational structure), the Java compiler (which reads it as a hierarchical address), documentation tools (which read it as structured data for indexing), and project managers (who read it as an organizational signal). The name serves all four communities because it is structurally coherent yet interpretively flexible.

The controlled vocabulary that governs this name (the set of valid organ identifiers, module names, and class naming conventions) *is* a boundary object in the repository sense. The individual name `RepoHealthScore` is a coordination artifact that participates in the boundary-object vocabulary but is not itself a boundary object.

### 5.3 Latour's Immutable Mobiles: Names That Travel Without Distortion

[Retained from v1.]

### 5.4 The Double-Hyphen Convention as Case Study

[Retained from v1, with the following addition:]

**Limitation of the case study.** The ORGANVM system is a single-operator system. The double-hyphen convention does not face the cross-community interpretation challenges that arise in multi-team organizations where naming conventions must mediate between communities with genuinely divergent interests, vocabularies, and organizational incentives. The theoretical analysis is sound -- the convention exhibits the structural properties that the framework predicts -- but the empirical validation is limited to a context where the namer, the primary interpreter, and the governance authority are the same person. The design principles derived below (Section 6) are theoretically motivated and would benefit from validation in larger, multi-team contexts.

---

## 6. Design Principles for Naming Infrastructure

### 6.1 Names Should Encode Structure Without Requiring It

[Retained from v1.]

### 6.2 Names Should Be Stable Under Organizational Change

[Retained from v1, with the following revision per POV 3:]

The principle should be qualified: names should be designed for the *expected frequency and type of organizational change*, not simply for maximum stability. In organizations where change is the norm (agile teams with regular retrospective reorganization, seasonal restructuring, iterative product development), names that encode current organizational position may be *more* useful than names that encode stable but abstract function -- because in high-change environments, the current position is the information most needed for coordination. The principle is: match name stability to organizational stability, not maximize name stability unconditionally.

### 6.3 Names Should Be Interpretable at Multiple Levels of Expertise

[Retained from v1.]

### 6.4 Names Should Fail Visibly

[Retained from v1.]

### 6.5 The Namespace as Governance Boundary

[Retained from v1.]

### 6.6 The Bikeshedding Challenge: Does Naming Actually Matter?

A serious objection to this paper's thesis is that naming conventions are trivial -- that the elaborate theoretical apparatus deployed here is disproportionate to a phenomenon that, in practice, amounts to bikeshedding (Parkinson's law of triviality: committees give disproportionate attention to minor issues). This section confronts the objection with empirical evidence.

**Naming failures that caused system failures.** The claim that naming is infrastructure -- and that infrastructure failures have systemic consequences -- can be tested against documented cases:

- The **left-pad incident** (2016): the removal of an 11-line npm package with the ambiguous name `left-pad` broke thousands of downstream projects, including React and Babel. The failure was a naming-governance failure: npm's flat namespace allowed a trivially-named package to become an inadvertent obligatory passage point for the entire JavaScript ecosystem.

- The **Mars Climate Orbiter** (1999): the spacecraft was lost because one engineering team used imperial units and another used metric units for thrust calculations. This is an abstraction-mismatch naming failure: the same physical quantity was named differently (in different unit systems) by different teams, and the naming convention provided no mechanism for detecting the discrepancy.

- The **Therac-25 accidents** (1985-1987): six radiation overdoses, three fatal, were partly caused by a race condition in software that reused variable names from an earlier, hardware-interlocked version. The software variable names implied safety properties (inherited from the earlier system's naming conventions) that the software alone could not guarantee. This is a semantic-drift failure: the names persisted across system versions while the properties they implied did not.

**Empirical studies of naming's impact.** The software engineering literature provides quantitative evidence:

- Lawrie et al. (2006) found that full-word identifiers are significantly easier to comprehend than abbreviations, with a measured effect on code-understanding accuracy.
- Butler et al. (2010) demonstrated a statistically significant correlation between identifier naming convention violations and software defect density.
- Arnaoudova et al. (2016) identified "linguistic antipatterns" -- naming conventions that contradict the code's behavior (e.g., a method named `isValid` that modifies state) -- and showed they correlate with higher defect rates.
- Hofmeister et al. (2017) showed that identifier style (camelCase vs. underscore) affects comprehension time, with effects varying by developer experience.

These studies confirm that naming conventions have measurable effects on code quality, comprehension, and defect rates. The theoretical apparatus of this paper provides the *explanatory framework* for these empirical findings: naming conventions are infrastructure, and infrastructure quality has systemic effects.

**The bikeshedding response.** The bikeshedding objection has a precise rebuttal: naming conventions *appear* trivial because they are infrastructure, and infrastructure is invisible when working. The theoretical apparatus is not disproportionate to the phenomenon; the phenomenon is more consequential than its invisibility suggests.

---

## 7. Conclusion

This paper has argued that naming conventions are organizational infrastructure -- invisible when working, failure-revealing when broken, and constitutive of the organizational topologies they appear merely to describe. The argument rests on three pillars: the double life of names as rigid designators and social signs (philosophy of naming), the encoding of organizational topology in naming structure (hierarchy/rhizome spectrum), and the function of names as coordination artifacts and, in specific structural cases, boundary objects (actor-network theory and infrastructure studies).

The cross-cultural comparison (Section 2.4) confirms that naming's infrastructural function is not culturally specific, though its form varies. The empirical evidence (Section 6.6) confirms that naming conventions have measurable effects on system reliability and code quality.

The case study has a notable limitation: the ORGANVM system is a single-operator system, and the design principles derived from it would benefit from validation in multi-team contexts. This validation is identified as the highest-priority empirical agenda for subsequent work.

---

## References

[Retained from v1, with the addition of:]

Arnaoudova, V., Di Penta, M., and Antoniol, G. (2016). "Linguistic Antipatterns: What They Are and How Developers Perceive Them." *Empirical Software Engineering*, 21(1), 104-158.

Butler, S., Wermelinger, M., Yu, Y., and Sharp, H. (2010). "Exploring the Influence of Identifier Names on Code Quality." *Proceedings of the 14th European Conference on Software Maintenance and Reengineering*, 156-165.

Hofmeister, J., Siegmund, J., and Holt, D.V. (2017). "Shorter Identifier Names Take Longer to Comprehend." *IEEE SANER*, 217-227.

Lawrie, D., Morrell, C., Feild, H., and Binkley, D. (2006). "What's in a Name? A Study of Identifiers." *IEEE ICPC*, 3-12.
