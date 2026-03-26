---
status: reference-activated
---
# Cross-Reference Audit Report

**SGO Research Programme -- 13 Papers (v2 drafts)**
**Audit date: 2026-03-20**

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total cross-references found | 87 |
| Consistent | 74 |
| Inconsistent (terminology/format) | 8 |
| Missing (should exist) | 19 |
| Orphaned concepts | 3 |

---

## Per-Paper Cross-Reference Map

| Paper | SGO ID | References To | Referenced By |
|-------|--------|--------------|---------------|
| RP-04 (Naming) | SGO-2026-RP-004 | None declared | SYN-03, SYN-05, CAPSTONE |
| RP-02 (Self-Reference) | SGO-2026-RP-002 | None declared | RP-07, SYN-02, SYN-05, CAPSTONE |
| RP-07 (Measurement) | SGO-2026-RP-007 | RP-02, RP-03 (deps) | SYN-02, SYN-04, CAPSTONE |
| RP-01 (Semantics Bridge) | SGO-2026-RP-001 | RP-06 (dep) | SYN-01, SYN-05, CAPSTONE |
| RP-03 (Rhizome/Hierarchy) | SGO-2026-RP-003 | RP-05 (dep) | RP-07, SYN-02, SYN-03, CAPSTONE |
| RP-05 (Latour/ANT) | SGO-2026-RP-005 | RP-03 (dep) | SYN-02, SYN-03, SYN-04, CAPSTONE |
| SYN-03 (Naming as Infrastructure) | SGO-2026-SYN-003 | RP-04, RP-03, RP-05 (deps) | CAPSTONE |
| RP-06 (Chomsky to Computation) | SGO-2026-RP-006 | RP-01 (dep) | SYN-01, SYN-05, CAPSTONE |
| SYN-01 (Grand Unified Semantics) | SGO-2026-SYN-001 | RP-01, RP-06 (deps) | SYN-05, CAPSTONE |
| SYN-02 (Governance Impossibility) | SGO-2026-SYN-002 | RP-02, RP-03, RP-05, RP-07 (deps) | CAPSTONE |
| SYN-04 (Flat Ontology Measurement) | SGO-2026-SYN-004 | RP-05, RP-07 (deps) | CAPSTONE |
| SYN-05 (Architecture of Meaning) | SGO-2026-SYN-005 | RP-01, RP-02, RP-04, RP-06 (deps) | CAPSTONE |
| CAPSTONE | SGO-2026-CAP-001 | ALL (dep) | None |

### Dependency Graph Integrity

The declared dependency graph is a DAG (no cycles). The CAPSTONE correctly lists `dependencies: [ALL]`. Each synthesis paper lists its constituent research papers as dependencies. One observation:

- **RP-07 lists RP-03 as a dependency** but never directly references RP-03's compression/search framework. The dependency appears to be thematic (both deal with organizational structure) rather than structural. RP-07's connection to RP-03 could be made more explicit through a cross-reference to the emergence trap or the coupling-structure framework.

- **RP-05 lists RP-03 as a dependency** and this is justified -- RP-05's discussion of flat ontology in networks naturally extends RP-03's rhizome/hierarchy analysis. However, RP-05 does not explicitly cite RP-03 by name in its body text; the connection is implicit.

- **RP-03 lists RP-05 as a dependency** -- this is a mutual dependency (RP-03 depends on RP-05 and RP-05 depends on RP-03). RP-03's YAML says `dependencies: [RP-05]` while RP-05's YAML says `dependencies: [RP-03]`. This circular dependency should be reviewed. In practice, neither paper cites the other in its body text -- these appear to be thematic bridges, not true directional dependencies.

---

## Terminology Inconsistencies

### 1. "Governance Trilemma"

| Paper | Usage | Consistent? |
|-------|-------|-------------|
| SYN-02 | "Governance Trilemma" (capitalized, bold, defined) | Canonical |
| CAPSTONE | "Governance Trilemma" (capitalized, bold) | Yes |
| SYN-05 | Not mentioned directly | N/A |
| SYN-04 | Not mentioned directly | N/A |
| RP-02 | Does not use the term (predates SYN-02) | N/A |

**Assessment:** Consistent where used. The term is properly introduced and defined in SYN-02 and correctly referenced in the CAPSTONE. No lowercase or variant spellings found.

### 2. "syntactic/semantic boundary" vs. "syntactic-semantic boundary"

| Paper | Usage | Form |
|-------|-------|------|
| RP-02 | "syntactic/semantic boundary" (Section 4 heading and throughout) | slash |
| RP-02 | "syntactic from semantic governance" (Section 5.2) | natural language |
| SYN-02 | "syntactic/semantic boundary" (Section 2.1) | slash |
| CAPSTONE | "syntactic/semantic boundary" | slash |
| SYN-05 | "syntactic/semantic boundary" | slash |

**Assessment:** Consistent. The slash form "syntactic/semantic boundary" is used uniformly.

### 3. "Constrained Variation Principle"

**This term does not appear in any of the 13 papers.** If it was intended as a programme concept, it is entirely absent.

### 4. "fourfold correspondence" vs. "four-way correspondence"

| Paper | Usage |
|-------|-------|
| RP-06 | "fourfold structural correspondence" (abstract), "fourfold correspondence" (throughout), "fourfold grammar-automaton-type-proof correspondence" | Canonical: "fourfold" |
| SYN-01 | "fourfold correspondence" (Section 2.2 heading), "fourfold grammar-type-proof-category correspondence" | Consistent |
| SYN-05 | "fourfold correspondence" | Consistent |
| CAPSTONE | "fourfold correspondence" | Consistent |
| RP-01 | Does not use the term | N/A |

**Assessment:** Consistent. "Fourfold correspondence" is the standard term throughout. No "four-way" variant found.

### 5. "compression vs. search" vs. "compression/search"

| Paper | Usage |
|-------|-------|
| RP-03 | "compression/search" (Section 3 heading: "The Compression/Search Meta-Principle"), also "compression algorithm" and "search algorithm" separately | Slash form predominant |
| SYN-02 | "compression/search tradeoff" | Consistent |
| SYN-03 | "Names as Compression" (Section 3.2) | Consistent (uses the concept) |
| CAPSTONE | "compression/search tradeoff" | Consistent |

**Assessment:** Consistent. The slash form "compression/search" is standard.

### 6. "boundary object" usage

| Paper | Usage | Consistent with Star & Griesemer? |
|-------|-------|----------------------------------|
| RP-04 v2 | Reduced per corpus-level critique; used only where Star & Griesemer's structural features are present | Yes |
| RP-05 | "Boundary Objects" (Section 2.4 heading); used with precision, distinguishing from immutable mobiles | Yes |
| SYN-03 v2 | Section 5.1 provides precise application; distinguishes boundary objects from "coordination artifacts" and "shared references" | Yes (exemplary) |
| SYN-05 v2 | "Reduced boundary-object usage per corpus-level critique" (revision notes) | Yes |
| CAPSTONE v2 | "'Boundary object' usage reduced; replaced with 'coordination artifact' where Star and Griesemer's structural features are absent" | Yes |

**Assessment:** The v2 revisions addressed a corpus-level issue with boundary-object overuse. The term is now used consistently and precisely across all papers, with SYN-03 providing the definitive treatment. Where Star and Griesemer's four structural types (repositories, ideal types, coincident boundaries, standardized forms) are absent, papers now use "coordination artifact" or "shared reference" instead. This is consistent and well-disciplined.

### 7. "emergence trap"

| Paper | Usage |
|-------|-------|
| RP-03 | "The Emergence Trap" (Section 4.4 heading; defined) | Canonical |
| SYN-02 | "The Emergence Trap" (Section 2.2 heading) | Consistent |
| CAPSTONE | "emergence trap" | Consistent |

**Assessment:** Consistent.

### 8. INCONSISTENCY: "five-way correspondence" scope

| Paper | Scope claimed |
|-------|---------------|
| SYN-01 | "five-way correspondence among derivation, proof, programme, morphism, and meaning-composition" (abstract) | 5 columns |
| SYN-05 | "five-way correspondence table" (Section 6.1); presented at two levels: proven 4-way and conjectured 5th | 5 columns (qualified) |
| CAPSTONE | "five-way correspondence extending the proven Curry-Howard-Lambek correspondence to include meaning-assignment" (Section 1.2) | Consistent with SYN-05 |
| RP-06 | "fourfold correspondence" (grammar, automaton, type, proof) -- 4 columns, no meaning column | 4 columns |

**Assessment:** INCONSISTENCY. SYN-01 and SYN-05 speak of a "five-way correspondence" (derivation, proof, programme, morphism, meaning-composition), but RP-06 speaks of a "fourfold correspondence" (grammar, automaton, type, proof). The mapping between RP-06's "four" and SYN-01's "five" is not fully explicit. RP-06's automaton column drops out of SYN-01's five-way table, and a "meaning" column is added. The transition from four to five columns should be documented more clearly -- specifically, why "automaton" disappears and "meaning-composition" appears.

**Recommendation:** SYN-01 Section 2.3 (where RP-01 and RP-06 overlap) should explicitly state: "RP-06's automaton column is subsumed by the categorical morphism column (since automata correspond to morphisms in the appropriate category), while the meaning-assignment column is the contribution of RP-01."

---

## Citation Format Inconsistencies

### Author-Year Format

The papers are generally consistent in using [Author, Year] or (Author, Year) format. However:

| Issue | Papers | Detail |
|-------|--------|--------|
| Parenthetical vs. textual citation style varies | All | Most papers use textual citation ("Kripke (1980) argued...") mixed with parenthetical ("(Kripke, 1980)"). This is normal academic practice and not a true inconsistency. |
| Godel diacritical | All | Consistently written as "Godel" (without umlaut) throughout all papers. Consistent. |
| Uber/uber in Frege title | RP-04, RP-01 | Both use "Uber Sinn und Bedeutung" without umlaut. Consistent. |
| Saussure accent | RP-04 | "Saussure" without accent on first vowel. Consistent across papers. |
| Butler et al. (2010) | RP-04, SYN-03, CAPSTONE | All cite consistently: Butler, S., Wermelinger, M., Yu, Y., and Sharp, H. (2010). Consistent. |
| Hofmeister et al. (2017) | RP-04, SYN-03 | RP-04 cites venue as "Proceedings of the 26th IEEE International Conference on Software Analysis, Evolution, and Reengineering" while SYN-03 cites "IEEE SANER". These are the same venue but named differently. |
| Lawrie et al. (2006) | RP-04, SYN-03 | RP-04 cites venue as "Proceedings of the 14th IEEE International Conference on Program Comprehension" while SYN-03 cites "IEEE ICPC". Same venue, different naming. |

**Recommendation:** Standardize conference citation format: either always use the full name or always use the abbreviation. The full name is preferred for a reference list; abbreviations are acceptable for in-text citations. Choose one approach and apply it uniformly.

### Cross-Paper Reference Format

Papers reference each other using the format "RP-02" or "RP-07" (by ID number). This is consistent within the programme. SYN-02 uses the most complete format: "RP-02 (The Impossibility Landscape)", "RP-03 (The Topology of Organization)", etc. -- giving both ID and short title. Other papers (SYN-01, SYN-05, CAPSTONE) also use this format. This is the best practice and is mostly consistent.

---

## Missing Cross-References

These are cases where Paper A discusses a concept that Paper B has developed in detail, but Paper A does not cite Paper B (or vice versa).

| # | Paper A | Should Cite | Paper B | Reason |
|---|---------|-------------|---------|--------|
| 1 | SYN-02 | RP-07's Guttman scale finding | RP-07 | SYN-02 discusses measurement impossibility extensively and cites RP-07 as a source, but does not specifically reference RP-07's finding that promotion state machines have Guttman scale structure. SYN-02's "measurability" horn would be strengthened by citing RP-07's specific finding that the Guttman scale assumption may be violated. |
| 2 | SYN-03 | RP-04's design principles | RP-04 | SYN-03 lists RP-04 as a dependency and references it in the header, but its own design principles (Section 6) do not explicitly cross-reference RP-04's seven design principles (Section 5.1). The naming principles in SYN-03 should note where they overlap or extend RP-04's principles. |
| 3 | RP-07 | RP-02's syntactic/semantic boundary | RP-02 | RP-07 lists RP-02 as a dependency but never explicitly references RP-02's core finding: the syntactic/semantic boundary drawn by Rice's theorem. RP-07's Tier 1/2/3 governance rule taxonomy (Section 4.6) recapitulates RP-02's distinction without citing it. The taxonomy should note: "This three-tier classification operationalizes the syntactic/semantic boundary formalized in RP-02." |
| 4 | RP-07 | RP-03's compression/search | RP-03 | RP-07 lists RP-03 as a dependency but never references RP-03's compression/search meta-principle or the emergence trap. The connection between organizational topology and measurement bias should be made explicit. |
| 5 | RP-01 | RP-04's naming framework | RP-04 | RP-01 discusses naming/homonymy in its opening ("The Homonymy Problem") -- the fact that "semantics" names three different traditions. This is precisely the naming failure mode (namespace collision) that RP-04 identifies as one of its five failure modes. A cross-reference would strengthen both papers. |
| 6 | RP-06 | RP-04's type-token distinction | RP-04 | RP-06 extensively discusses types and tokens in the formal language sense but never references RP-04's discussion of the Peircean type-token distinction across domains. A brief note connecting Peirce's type-token to RP-06's type system hierarchy would bridge philosophy and formalism. |
| 7 | SYN-04 | RP-04's reference relation | RP-04 | SYN-04's performative measurement strategy reconceives the relationship between sign and referent. RP-04's analysis of the reference relation (Section 4.1) is directly relevant but not cited. |
| 8 | SYN-04 | RP-02's Lob's theorem | RP-02 | SYN-04's argument about construct circularity (Section 2.3 -- "the construct-operationalization collapse") is structurally similar to Lob's theorem's finding about self-certification vacuity (RP-02, Section 3.6). A cross-reference would strengthen the formal grounding. |
| 9 | RP-05 | RP-02's impossibility landscape | RP-02 | RP-05 discusses constitutive opacity and the limits of depunctualization. RP-02's analysis of the impossibility landscape is directly relevant: constitutive opacity is the ANT vocabulary for the same structural impossibility that Godel/Tarski/Rice establish formally. RP-05 should cite RP-02 when introducing constitutive opacity. |
| 10 | SYN-01 | RP-04's naming analysis | RP-04 | SYN-01 synthesizes RP-01 and RP-06 but does not reference RP-04. Yet its discussion of compositionality assumes that the referential dimension (how names attach to things) is well-established. A brief note citing RP-04's referential analysis would anchor the semantic architecture in the naming analysis. |
| 11 | RP-03 | RP-04's governance failure mode | RP-04 | RP-03 discusses governance extensively (accountability, decision-speed, free-riders) but does not reference RP-04's "governance failure" as one of the five naming failure modes. The parallel is direct: RP-04 identifies governance failure as a naming pathology; RP-03 analyzes governance failure as an organizational pathology. |
| 12 | SYN-02 | SYN-03's naming-as-infrastructure | SYN-03 | SYN-02 discusses how governance rules are interpreted differently by different actants (Section 2.3, citing RP-05), but does not reference SYN-03's finding that naming conventions function as organizational infrastructure. Since governance rules are expressed as naming conventions (seed.yaml fields, promotion state names), SYN-03's infrastructure thesis is directly relevant. |
| 13 | SYN-05 | SYN-03 | SYN-03 | SYN-05 synthesizes RP-01, RP-02, RP-04, and RP-06, but does not reference SYN-03. SYN-03's finding that naming conventions are infrastructure strengthens SYN-05's referential dimension by showing that naming is not just a philosophical problem but an organizational one. |
| 14 | RP-05 | RP-04's Wittgenstein treatment | RP-04 | RP-05 discusses Wittgenstein's language games implicitly (through the concept of different "uses" of boundary objects in different communities). RP-04 explicitly treats Wittgenstein's use theory (Section 2.1.4). A cross-reference would connect the philosophical and STS treatments. |
| 15 | SYN-02 | RP-06's decidability hierarchy | RP-06 | SYN-02 discusses decidability extensively (Rice's theorem, the syntactic/semantic boundary) but does not reference RP-06's mapping of decidability properties across the Chomsky hierarchy. RP-06 demonstrates that decidability properties are preserved across the fourfold correspondence; SYN-02 could use this finding to strengthen the claim that governance decidability is not an engineering contingency but a formal necessity. |
| 16 | CAPSTONE | SYN-03 | SYN-03 | The CAPSTONE lists all 12 prior works in Section 1.4 and correctly includes SYN-03 in Phase 2. However, in Chapters 2-10, SYN-03's specific findings (naming conventions as infrastructure, the bikeshedding rebuttal, the cross-cultural naming evidence) are not visibly integrated. Chapter 2 (The Naming Problem) draws primarily from RP-04. SYN-03's contribution should be visible in Chapter 2 or Chapter 3. |
| 17 | CAPSTONE | SYN-04 | SYN-04 | Similarly, SYN-04's specific contributions (performative measurement, network-relative constructs, relational psychometrics) should be visible in Chapter 9 (Measurement and Its Discontents). The CAPSTONE lists SYN-04 in Phase 3 but its body text does not clearly integrate SYN-04's resolution strategies. |
| 18 | RP-01 | RP-02's Curry-Howard discussion | RP-02 | RP-01 discusses the Curry-Howard-Lambek correspondence as one of its eight bridges. RP-02 also discusses Curry-Howard (Section 4.4) in the context of governance-as-types. Neither paper references the other's treatment, even though they arrive at complementary conclusions (RP-01: CHL unifies semantics; RP-02: CHL illuminates governance limits). |
| 19 | SYN-05 | SYN-01's categorical architecture | SYN-01 | SYN-05's structural dimension is built on the same categorical architecture that SYN-01 develops in detail. SYN-05 should explicitly reference SYN-01 when discussing the functorial characterization of meaning. SYN-05's dependency list includes RP-01 but not SYN-01, even though SYN-01 is the more developed treatment. |

---

## Orphaned Concepts

These are concepts introduced or named in one paper but referenced in others without proper definition, or concepts that appear to lack a canonical home.

| Concept | Introduced In | Referenced In | Issue |
|---------|--------------|---------------|-------|
| "Constrained Variation Principle" | NOT FOUND | NOT FOUND | This term does not appear in any of the 13 papers. If it was intended as a programme concept, it was never defined. |
| "coupling structure" (as formal design variable) | RP-03 (Section 3.4) | SYN-02 (implicit), CAPSTONE (implicit) | RP-03 v2 introduced the coupling-structure framework as a generalization of compression/search. SYN-02 and the CAPSTONE reference the compression/search tradeoff but do not propagate the coupling-structure generalization. This creates an orphan: RP-03's most important v2 contribution is not picked up by downstream papers. |
| "constitutive opacity" (as distinguished from practical opacity) | RP-05 (Section 5.3) | SYN-02 (Section 2.3) | The distinction between practical and constitutive opacity/blackboxing is introduced in RP-05 and picked up in SYN-02. This is properly handled. However, SYN-04 (which depends on RP-05) does not use the term, even though its discussion of measurement in constitutively opaque systems would benefit from it. |

---

## Concept Verification

For each major cross-referenced concept, I verified that the concept exists and is correctly characterized in the cited paper.

| Concept | Cited Paper | Verification |
|---------|-------------|-------------|
| Governance Trilemma (completeness, consistency, measurability) | SYN-02 | VERIFIED -- defined in SYN-02 Section 3, with three horns developed in Sections 3.1-3.4 |
| Five failure modes of naming | RP-04 | VERIFIED -- reference failure, namespace collision, semantic drift, abstraction mismatch, governance failure (Section 3.1) |
| Syntactic/semantic boundary | RP-02 | VERIFIED -- Section 4 heading and developed through Sections 4.1-4.6 |
| Compression/search meta-principle | RP-03 | VERIFIED -- Section 3 heading, developed through 3.1-3.5 |
| Emergence trap | RP-03 | VERIFIED -- Section 4.4 |
| Fourfold correspondence | RP-06 | VERIFIED -- grammar-automaton-type-proof, developed throughout |
| Eight semantic bridges | RP-01 | VERIFIED -- compositionality, lambda calculus, CHL, type theory, model theory, game semantics, dynamic semantics, proof-theoretic semantics (Section 3) |
| Four-phase model (naming, structuring, computing, reflecting) | CAPSTONE | VERIFIED -- Section 1.1, developed in Chapter 11 |
| Guttman scale properties of promotion state machine | RP-07 | VERIFIED -- Section 4.1 |
| Seven design principles for self-governing systems | RP-02 | VERIFIED -- Section 5 (5.1-5.7) |
| Five design principles for naming infrastructure | SYN-03 | VERIFIED -- Section 6 (6.1-6.5, plus 6.6 empirical section) |
| Three resolution strategies (performative, network-relative, relational) | SYN-04 | VERIFIED -- Section 3 (3.1-3.4) |
| Obligatory passage points | RP-05 | VERIFIED -- Section 2.3 |
| Callon's four moments of translation | RP-05 | VERIFIED -- Section 2.2 (problematization, interessement, enrollment, mobilization) |
| Boundary objects (Star and Griesemer) | RP-05, SYN-03 | VERIFIED -- RP-05 Section 2.4, SYN-03 Section 5.1 |
| Human as incompleteness response | CAPSTONE | VERIFIED -- Section 12.2 |

---

## Recommendations (Prioritized)

### Priority 1: Structural Issues

1. **Resolve RP-03/RP-05 circular dependency.** Both papers list the other as a dependency. Determine which genuinely depends on the other (likely RP-05 depends on RP-03's topological analysis, not the reverse) and correct the YAML.

2. **Propagate RP-03 v2's coupling-structure framework.** The coupling-structure generalization (RP-03 Section 3.4) is RP-03's most important v2 contribution. SYN-02 and the CAPSTONE should reference it explicitly, since it subsumes the compression/search binary that they cite.

3. **Clarify the four-to-five column transition.** Add a brief note in SYN-01 Section 2.3 explicitly explaining why RP-06's "fourfold" becomes SYN-01's "five-way" -- specifically, what happens to the automaton column and where the meaning column comes from.

### Priority 2: Missing Cross-References (High Value)

4. **RP-07 should cite RP-02's syntactic/semantic boundary** when introducing its three-tier taxonomy (Section 4.6). One sentence would suffice: "This three-tier classification operationalizes the syntactic/semantic boundary formalized in RP-02."

5. **SYN-02 should cite RP-07's Guttman scale finding** when discussing the measurability horn. RP-07's finding that promotion states may violate the cumulative assumption directly supports SYN-02's argument.

6. **RP-05 should cite RP-02** when introducing constitutive opacity (Section 5.3). The formal impossibility results provide the mathematical foundation for what RP-05 describes in STS vocabulary.

7. **SYN-03 should cross-reference RP-04's design principles.** SYN-03 Section 6 should note where its naming-infrastructure principles extend or operationalize RP-04's seven principles.

8. **CAPSTONE should visibly integrate SYN-03 and SYN-04.** These papers' findings should be woven into Chapters 2 and 9 respectively, not merely listed in the Phase overview.

### Priority 3: Citation Format

9. **Standardize conference citation format.** Choose either full name ("Proceedings of the 14th IEEE International Conference on Program Comprehension") or abbreviation ("IEEE ICPC") and apply consistently across all papers. The full name is recommended for reference lists.

### Priority 4: Minor Terminology

10. **The term "Constrained Variation Principle" does not exist in the corpus.** If this was intended as a programme concept, it needs to be defined somewhere. If it was a working title that was replaced, remove any external references to it.

11. **RP-04's reference list contains a typo:** "The Analerta" should be "The Analects" (line 247 of RP-04).

---

## Appendix: Complete Cross-Reference Inventory

Below is the exhaustive list of every cross-reference found, organized by source paper.

### RP-04 (The Deep Structure of Naming)
- Internal cross-references to other SGO papers: **0**
- This paper stands alone as a foundational investigation.

### RP-02 (The Impossibility Landscape)
- Internal cross-references to other SGO papers: **0** in body text
- The ORGANVM case study (Section 6) references system concepts shared with other papers but does not cite them by SGO ID.

### RP-07 (Measuring the Unmeasurable)
- YAML dependencies: RP-02, RP-03
- Body text cross-references: **0** explicit SGO citations
- Implicit connections: Tier 1/2/3 taxonomy parallels RP-02's syntactic/semantic boundary; promotion state machine analysis connects to RP-03's organizational analysis.

### RP-01 (Semantics Bridge)
- YAML dependencies: RP-06
- Body text cross-references: **0** explicit SGO citations in the excerpt read
- SYN-01 references RP-01 extensively.

### RP-03 (Rhizome vs. Hierarchy)
- YAML dependencies: RP-05
- Body text cross-references: **0** explicit SGO citations

### RP-05 (Actants in the Loop)
- YAML dependencies: RP-03
- Body text cross-references: **0** explicit SGO citations
- References ORGANVM system extensively as case study.

### SYN-03 (Names That Hold)
- YAML dependencies: RP-04, RP-03, RP-05
- Header: "Bridges: RP-04 (The Naming Problem), RP-03 (Rhizome vs. Hierarchy), RP-05 (Latour's Network Ontology)"
- Body cross-references: References RP-04 v2's cross-cultural evidence (Section 2.4); references the compression/search framework from RP-03; references Star and Griesemer and ANT from RP-05.
- **Total explicit SGO cross-references: 3** (in header)

### RP-06 (The Fourfold Correspondence)
- YAML dependencies: RP-01
- Body text cross-references: **0** explicit SGO citations in the excerpt read
- The paper is self-contained in its formal development.

### SYN-01 (Architecture of Compositional Formal Meaning)
- YAML dependencies: RP-01, RP-06
- Header: "Synthesis of RP-01 (The Semantics Bridge) and RP-06 (Chomsky to Computation)"
- Body cross-references: Extensive -- RP-01's eight bridges recapitulated (Section 2.1), RP-06's fourfold recapitulated (Section 2.2), overlap and divergence mapped (Sections 2.3-2.4).
- **Total explicit SGO cross-references: 20+** (the most densely cross-referenced synthesis paper)

### SYN-02 (Governance Impossibility Thesis)
- YAML dependencies: RP-02, RP-03, RP-05, RP-07
- Body cross-references: "RP-02 (The Impossibility Landscape)" cited in Section 2.1; "RP-03 (The Topology of Organization)" cited in Section 2.2; "RP-05 (Actants in the Loop)" cited in Section 2.3; "RP-07 (Measuring the Unmeasurable)" cited in Section 2.4.
- **Total explicit SGO cross-references: 15+** (each source paper cited multiple times)

### SYN-04 (Measuring Actants)
- YAML dependencies: RP-05, RP-07
- Body cross-references: "RP-07" cited in Sections 2.3, 4.1; "RP-05" cited in Section 2.3.
- **Total explicit SGO cross-references: 5+**

### SYN-05 (Architecture of Formal Meaning)
- YAML dependencies: RP-01, RP-02, RP-04, RP-06
- Header: "Synthesis of RP-01 (The Semantics Bridge), RP-02 (Self-Reference and Limits), RP-04 (The Naming Problem), and RP-06 (Chomsky to Computation)"
- Body cross-references: Each source paper cited in its corresponding dimension section (Reference from RP-04, Structure from RP-01/SYN-01, Computation from RP-06, Reflexivity from RP-02).
- Also cites SYN-01 implicitly (the functorial account).
- **Total explicit SGO cross-references: 10+**
- **Missing dependency: SYN-01** should be listed as a dependency since SYN-05 builds on SYN-01's categorical architecture.

### CAPSTONE (Formalization of Knowledge)
- YAML dependencies: ALL
- Section 1.4 lists all 12 prior works organized by phase.
- Body cross-references: Each chapter draws on the relevant prior works. The cross-referencing is most complete in Chapter 10 (Governance Trilemma, citing SYN-02), Chapter 11 (four-phase model, citing all), and Chapter 12 (conclusions, citing RP-02 for impossibility results).
- **Total explicit SGO cross-references: 30+**
- **Weakness: SYN-03 and SYN-04 are listed but their specific contributions are not visibly woven into the body chapters.**
