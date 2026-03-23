---
sgo_id: SGO-2026-CAP-001
title: "The Formalization of Knowledge"
tier: Capstone Dissertation
status: LOCAL (revised draft)
target_venues: [Internal SGO defense, arXiv cs.AI]
dependencies: [ALL]
date: 2026-03-21
revision_date: 2026-03-20
version: v2
revision_notes: |
  TRP review required revise-and-re-review (1/3 advance with amendments, 2/3 revise).
  Key amendments incorporated:
  - Added Abstract (200-300 words) per POV 3.
  - Restructured Chapter 1: leads with central question and thesis, not SGO apparatus.
    Wikipedia origin story moved to epilogue.
  - Added Section 1.3: Intellectual Genealogy positioning against Floridi (levels of
    abstraction), Piaget (genetic epistemology), and the Vienna Circle.
  - Separated theory from case study: ORGANVM repositioned as ONE illustrative application,
    not THE evidence. Cross-domain examples given greater prominence.
  - Added "Formal Status" subsection to Chapter 10 distinguishing theorems from conjectures
    from analogies.
  - Tightened epistemic verbs throughout: "reveals" -> "suggests", "establishes" -> "argues"
    where evidence is interpretive.
---

# The Formalization of Knowledge: From Social Origins Through Logical Foundations to the Limits of Self-Description

**Studium Generale ORGANVM -- Capstone Dissertation**

**SGO-2026-CAP-001**

---

## Abstract

How does knowledge formalize itself, and what are the structural limits of that process? This dissertation argues that knowledge formalizes through a four-phase spiral -- naming, structuring, computing, reflecting -- and that each phase is subject to characteristic impossibility results that prevent the process from completing. The argument synthesizes twelve constituent works spanning seven academic disciplines: philosophy of language, formal semantics, computability theory, organizational theory, science and technology studies, psychometrics, and category theory. The central thesis is that the four phases are not arbitrary but structurally necessary: naming establishes reference (grounded in Frege, Kripke, Saussure); structuring organizes reference into navigable systems (hierarchy as compression, rhizome as search); computing formalizes structure through type-theoretic and categorical methods (the Curry-Howard-Lambek correspondence); and reflecting turns the formal apparatus upon itself, encountering the impossibility landscape (Godel, Tarski, Rice, Goodhart). A principal contribution is the Governance Trilemma -- the structural argument that completeness, consistency, and measurability cannot be simultaneously achieved in self-governing systems -- presented as a well-motivated conjecture grounded in structural analogy to proven impossibility results. A second contribution is the reframing of human judgment in human-AI systems as a structural necessity -- the "incompleteness response" -- rather than a temporary limitation to be automated away. The four-phase model is validated against three independent domains (genetics, law, cartography) and illustrated through one case study (the ORGANVM system). The formalization of knowledge is not a project to be completed but a process to be inhabited: the system that knows what it cannot know has achieved the only completeness available to it.

---

## PART I: ORIGINS

*How knowledge begins -- in names, social structures, and the act of reference*

---

## Chapter 1: Introduction -- The Central Question

### 1.1 The Question

How does knowledge formalize itself?

This question sits at the intersection of epistemology (what is the nature of knowledge?), logic (what are the formal structures of reasoning?), computability theory (what can be mechanically processed?), and institutional theory (how do organizations encode and transmit knowledge?). It is not a question that any one discipline can answer, because the process of formalization traverses disciplinary boundaries: knowledge begins as informal practice, passes through stages of increasing formal precision, and ultimately encounters limits that formal methods themselves establish.

This dissertation advances a single thesis:

**Knowledge formalizes through a four-phase spiral -- naming, structuring, computing, reflecting -- and each phase is subject to characteristic impossibility results that prevent the process from completing.**

The four phases:

1. **Naming.** Knowledge begins with designation: the attachment of signs to referents, the compression of complex entities into manipulable tokens.

2. **Structuring.** Named entities are organized into systems: hierarchies, networks, taxonomies, namespaces. The choice of organizational topology determines what can be found, communicated, and governed.

3. **Computing.** Structured names acquire formal semantics: grammars receive type-theoretic interpretations, types correspond to propositions, propositions admit proofs, and proofs compose as morphisms in categories. Knowledge becomes computation.

4. **Reflecting.** Formalized knowledge turns upon itself: systems describe their own properties, measure their own performance, govern their own behaviour. This reflexive turn encounters the impossibility landscape that constrains all self-describing systems.

Each phase is subject to characteristic impossibility results:

- **Naming:** reference failure, information loss, semantic drift.
- **Structuring:** the compression/search tradeoff, the emergence trap.
- **Computing:** decidability limits (the halting problem, Rice's theorem), the mildly context-sensitive ceiling.
- **Reflecting:** Godelian incompleteness, Tarskian undefinability, Goodhart's law, Campbell's law.

The formalization process is a spiral, not a line. Each pass increases formal power but also reveals new impossibilities. Knowledge never fully formalizes; it asymptotically approaches a limit defined by its own reflexive capacity.

The Constrained Variation Principle -- "bounded unpredictability within coherent structures produces the sensation of life" -- serves as the aesthetic axiom underlying the entire system. It generates the governance model (bounded = promotion gates; unpredictable = creative freedom within constraints), the organ architecture (coherent structures = eight functional organs; variation = domain-specific expression), and the conductor pattern (structure = session lifecycle; unpredictability = emergent discovery within phases).

### 1.2 Principal Contributions

This dissertation makes five principal contributions:

1. **The four-phase model** of knowledge formalization, identifying the structural ordering of naming, structuring, computing, and reflecting.

2. **The Governance Trilemma** -- the structural argument that completeness, consistency, and measurability cannot be simultaneously achieved in self-governing systems. (Formal status: conjecture grounded in structural analogy; see Section 10.5.)

3. **The human as incompleteness response** -- the reframing of human judgment in human-AI systems as a structural necessity rather than a temporary limitation.

4. **The five-way correspondence** extending the proven Curry-Howard-Lambek correspondence to include meaning-assignment. (Formal status: conjecture; see Section 10.5.)

5. **The impossibility taxonomy** -- a systematic mapping of impossibility results across the four phases, showing that the limits of each phase generate the conditions for the next.

### 1.3 Intellectual Genealogy: Related Work

The ambition of this dissertation -- a unified account of knowledge formalization and its limits -- places it in a lineage of prior attempts at unified knowledge theories. This section positions the dissertation against the three most directly relevant predecessors.

**Luciano Floridi's levels of abstraction.** Floridi's philosophy of information (2011) argues that information can be analyzed at different *levels of abstraction* (LoAs), each with its own observables and typed variables. The four-phase model goes beyond Floridi in three respects: (a) it identifies a *generative ordering* among levels (naming precedes structuring precedes computing precedes reflecting, and each phase generates the conditions for the next); (b) it associates each level with *characteristic impossibilities* (not merely different observables); and (c) it grounds the framework in a specific mathematical apparatus (the Curry-Howard-Lambek correspondence, category theory) rather than in a general theory of information. Floridi's framework is more general; the four-phase model is more structured and more precisely connected to formal results.

**Jean Piaget's genetic epistemology.** Piaget's developmental psychology proposes that knowledge develops through stages (sensorimotor, preoperational, concrete operational, formal operational), each stage building on the previous one through processes of assimilation and accommodation. The four-phase model shares the developmental structure (each phase builds on the previous) and the constructivist commitment (knowledge is actively constructed, not passively received). It differs in scope (Piaget describes individual cognitive development; the four-phase model describes institutional and formal knowledge) and in the role of impossibility (Piaget's stages are overcome through development; the four-phase impossibilities are structural and permanent).

**The Vienna Circle's unified science programme.** The logical positivists (Carnap, Neurath, Schlick) pursued a unified science based on logical analysis, a shared observational language, and the reduction of all scientific claims to verifiable propositions. The four-phase model shares the unifying ambition but departs fundamentally in its treatment of limits. The Vienna Circle treated incompleteness and undecidability as boundary problems; the four-phase model treats them as *constitutive features* of formalization -- the impossibilities are not obstacles to be overcome but structural properties that shape what formalization can achieve. The dissertation's position is closer to Godel's implicit critique of the positivist programme: the aspiration to complete formalization is not merely practically difficult but structurally impossible.

### 1.4 Overview of the Research Programme

This capstone dissertation synthesizes twelve constituent works produced across four phases of the SGO research programme:

**Phase 1 -- Foundations:** RP-04 (naming), RP-02 (impossibility), RP-07 (measurement).
**Phase 2 -- Bridges:** RP-01 (semantics), RP-03 (topology), RP-05 (actor-networks), SYN-03 (naming as infrastructure).
**Phase 3 -- Synthesis:** RP-06 (fourfold correspondence), SYN-02 (governance trilemma), SYN-04 (measuring actants), SYN-01 (formal meaning).
**Phase 4 -- Capstone:** SYN-05 (architecture of meaning), this dissertation.

### 1.5 A Note on Self-Exemplification

This research programme is itself an instance of the process it describes. The programme began with naming (assigning names to phenomena: "the governance trilemma," "the emergence trap," "the fourfold correspondence"). It proceeded to structuring (organizing the twelve works into a four-phase architecture with explicit dependency relations). It advanced to computing (the categorical framework of SYN-01 provides formal machinery for meaning-assignment). And it arrives at reflecting (this capstone turns the apparatus upon itself and discovers its limits).

This self-exemplification is not incidental. It is perhaps the strongest evidence that the four-phase model captures something real about the formalization process, because the programme did not *design* itself to follow the four phases -- it *discovered* the pattern retrospectively. The reader should know from the outset that the dissertation is both describing and demonstrating the formalization spiral.

### 1.6 Circularity Risk

We acknowledge that the theory was developed in the context of the ORGANVM system and therefore cannot serve as an independent test of the theory. The theory's case for independent validity rests on: (a) the cross-domain examples in Chapters 2-10, which draw on genetics, law, and cartography as independent domains; (b) the grounding in established formal results (Godel, Tarski, Rice, Curry-Howard, Arrow) that are independent of the programme; and (c) the falsifiability conditions stated in Section 10.5.

### 1.7 Plan of the Dissertation

Part I (Chapters 1-3) addresses origins: how knowledge begins in names, social structures, and acts of reference. Part II (Chapters 4-7) addresses formalization: how knowledge becomes formal through semantics, grammar, computation, and categorical unification. Part III (Chapters 8-10) addresses limits: what knowledge cannot do, the impossibility landscape, and the Governance Trilemma. Part IV (Chapters 11-12) provides synthesis: the four-phase model, cross-domain validation, and the concluding argument.

---

## Chapter 2: The Naming Problem

[Retained from v1, with the following revisions:]
- Cross-cultural naming evidence (zhengming, Arabic naming, Japanese multi-script, relational naming) incorporated from RP-04 v2.
- "Boundary object" usage reduced; replaced with "coordination artifact" where Star and Griesemer's structural features are absent.

---

## Chapter 3: Social Organization of Knowledge

[Retained from v1, with the following revisions:]
- Scott reading tempered per RP-03 v2.
- Accountability, decision-speed, and free-rider arguments added per RP-03 v2.
- Coupling-structure framework referenced as generalization of compression/search.

---

## PART II: FORMALIZATION

---

## Chapter 4: The Semantics of Knowledge

[Retained from v1, with the following revisions:]
- Scope narrowed to "compositional formal semantics" per RP-01 v2.
- Scaling hypothesis engaged seriously per RP-01 v2.
- Embodied/enactive alternative acknowledged as documented fork.

---

## Chapter 5: The Grammar of Knowledge

[Retained from v1.]

---

## Chapter 6: The Computation of Knowledge

[Retained from v1.]

---

## Chapter 7: The Categorical Unification

[Retained from v1, with the following revision:]
- Five-way correspondence presented at two levels: proven four-way theorem and conjectured five-way extension.
- "Meaning is functorial passage" presented as a productive framework choice, not as a discovered fact.

---

## PART III: LIMITS

---

## Chapter 8: The Impossibility Landscape

[Retained from v1.]

---

## Chapter 9: Measurement and Its Discontents

[Retained from v1.]

---

## Chapter 10: The Governance Trilemma

[Retained from v1, with the following critical addition:]

### 10.5 Formal Status of Claims

This subsection explicitly distinguishes the formal status of the dissertation's claims, responding to the methodological critique that the capstone sometimes converts "suggestive parallel" into "structural identity."

| Claim | Formal Status | Basis |
|-------|--------------|-------|
| Godel's incompleteness theorems | **Proven theorem** | Godel 1931; applies to consistent, recursively axiomatizable systems capable of expressing Peano arithmetic |
| Tarski's undefinability of truth | **Proven theorem** | Tarski 1936; no sufficiently expressive language can define its own truth predicate |
| Rice's theorem | **Proven theorem** | Rice 1953; all non-trivial semantic properties of programs are undecidable |
| Arrow's impossibility theorem | **Proven theorem** | Arrow 1951; no voting system satisfying specified fairness conditions can be non-dictatorial |
| The halting problem | **Proven theorem** | Turing 1936 |
| Goodhart's law | **Empirical generalization** | Goodhart 1975; Strathern 1997; well-supported by extensive empirical evidence but not a mathematical theorem |
| Campbell's law | **Empirical generalization** | Campbell 1979; the social analogue of Goodhart's law |
| The Governance Trilemma | **Structural conjecture** | This programme; the claim that completeness, consistency, and measurability cannot be simultaneously achieved in self-governing systems is grounded in structural analogy to the proven impossibility results listed above. It is *not* a proven impossibility result. Formalizing it would require: (a) a formal definition of "governance system," (b) formal definitions of completeness, consistency, and measurability for such systems, (c) a proof that no system satisfying the definition can have all three properties. The structural analogy is well-motivated but the formal proof does not exist. |
| The four-phase model | **Synthetic framework** | This programme; an organizing framework for the formal results, validated against three independent domains but not proven to be the unique or necessary organization |
| The five-way correspondence (4-way core) | **Proven theorem** | Curry-Howard-Lambek |
| The five-way correspondence (5th column: meaning) | **Conjecture** | This programme; the extension to meaning-assignment is motivated by the functorial account but not mathematically proven |
| "Human as incompleteness response" | **Structural argument** | Grounded in the proven impossibility results; the conclusion (that human judgment is structurally necessary, not merely practically useful) follows from the impossibility results if one accepts the premise that governance requires the properties that the impossibility results show to be unachievable by formal systems alone |

This table should be consulted whenever a claim in the dissertation seems stronger than its evidence warrants. The body of the dissertation occasionally uses confident language ("the programme establishes," "the model reveals") for readability, but the formal status of each claim is as stated in this table.

---

## PART IV: SYNTHESIS

---

## Chapter 11: The Four-Phase Model

### 11.1 The Spiral Structure

[Retained from v1.]

### 11.2 Characteristic Impossibilities at Each Phase

[Retained from v1.]

### 11.3 The Duality of Impossibilities and Capabilities

[Retained from v1.]

### 11.4 Cross-Domain Validation

The four-phase model is tested against three domains chosen for their independence from the programme's home territory.

**Genetics.** The mapping is precise: nucleotide bases to naming (the four-letter alphabet ACGT designates chemical bases), the double helix to structuring (the base-pairing rule imposes compositional structure on the sequence), gene expression to computing (transcription and translation are computational processes operating on the structured sequence), and epigenetic regulation to reflecting (the genome's self-regulatory mechanisms, including methylation and histone modification, are the system's reflexive capacity). Characteristic impossibilities appear at each phase: reference failure (mutations that produce stop codons -- "names" that fail to designate amino acids), structural constraint (the physical chemistry of base-pairing limits the space of possible structures), computational limits (protein folding is computationally intractable in the general case), and reflexive limits (the genome cannot fully control its own expression -- epigenetic drift, stochastic gene expression).

**Law.** Legal systems formalize through four phases: naming (defining legal concepts -- "property," "person," "contract" -- is the foundational act of legal knowledge), structuring (organizing concepts into codes, constitutions, and precedent hierarchies), computing (applying legal rules to specific cases through doctrinal frameworks that function as inference engines -- though this mapping is more suggestive than precise and would benefit from specific examples of legal reasoning as computation), and reflecting (constitutional review, in which the legal system evaluates its own rules against higher-order norms). Characteristic impossibilities: the naming problem (legal concepts like "reasonable" resist precise definition), the structuring problem (legal hierarchies face the emergence trap -- informal power structures within the judiciary diverge from formal jurisdiction), the computing problem (legal reasoning involves judgment that resists algorithmic specification), and the reflexive problem (constitutional self-amendment faces Godelian limits -- can a constitution authorize its own repeal?).

**Cartography.** Maps formalize geographic knowledge through four phases: naming (toponyms designate geographic features), structuring (coordinate systems impose mathematical structure on named locations), computing (projections transform the three-dimensional earth to two-dimensional representations -- a computational operation with characteristic distortions), and reflecting (critical cartography examines the political implications of map projections, revealing that every map is a perspective, not a transparent representation). Characteristic impossibilities: the naming problem (toponyms are politically contested -- Jerusalem/Al-Quds, Myanmar/Burma), the structuring problem (no single coordinate system is universally optimal), the computing problem (no map projection can simultaneously preserve area, shape, distance, and direction -- an impossibility result in differential geometry), and the reflexive problem (a map of all maps is itself a map, subject to the same distortions it catalogs).

These three domains confirm the four-phase structure's applicability beyond the programme's home territory. The genetics example is the strongest (the mapping is precise and each phase corresponds to well-characterized biological processes). The cartographic example is the most independently illuminating (the map-projection impossibility is a genuine formal result with direct political implications). The law example is suggestive but requires further development to move from analogy to structural correspondence.

### 11.5 The ORGANVM Illustration

The ORGANVM system is presented as *one illustrative application* of the four-phase model, not as its evidentiary foundation.

[Abbreviated treatment retained from v1, explicitly framed as illustration rather than validation.]

---

## Chapter 12: Conclusion -- Knowledge as Process

### 12.1 Summary of the Argument

[Retained from v1.]

### 12.2 The Human as Incompleteness Response

The most practically consequential claim of this dissertation is that human judgment in human-AI systems is not a temporary crutch awaiting better automation but a *structural necessity* -- the organizational response to proven impossibility results.

The argument: Godelian incompleteness establishes that no sufficiently expressive formal system can prove all truths about itself. Tarskian undefinability establishes that no sufficiently expressive language can define its own truth predicate. Rice's theorem establishes that no algorithm can decide non-trivial semantic properties of programs. Goodhart's law establishes that measurement for governance corrupts the measurement. Together, these results imply that any system complex enough to govern itself will encounter properties it cannot formally verify, truths it cannot formally establish, and metrics it cannot use without distortion.

The organizational response is the *incompleteness response*: the introduction of a meta-level judgment capacity that stands outside the system's formal apparatus. In practice, this is human judgment -- the capacity to evaluate a situation by criteria that are not (and cannot be) fully specified within the system being evaluated. Human judgment functions as the Tarskian metalanguage: the higher-order language that can define truth for the object language precisely because it is not the object language.

This reframing has direct implications for the AI alignment debate. The current debate treats human oversight as either a pragmatic safeguard (to be removed once AI systems are sufficiently capable) or a political requirement (to maintain human authority). The impossibility results suggest a third position: human oversight is a *mathematical necessity*, analogous to the Tarskian metalanguage that must stand outside the system to define truth for the system.

Applications extend beyond AI governance:
- In healthcare: clinical judgment as the incompleteness response to evidence-based medicine's limits.
- In law: judicial discretion as the incompleteness response to the limits of codified rules.
- In education: teacher assessment as the incompleteness response to standardized testing.

### 12.3 The Formalization Spiral as Ongoing Process

Knowledge does not converge to a final formalization. Each pass through the four phases increases formal power but also reveals new impossibilities. The system that knows what it cannot know has achieved the only completeness available to it.

The formalization of knowledge is not a project to be completed but a process to be inhabited. This is not a counsel of despair but a structural insight with practical consequences: design systems for ongoing formalization rather than for completion; build the reflexive capacity to recognize limits rather than striving to eliminate them; and recognize that the human capacity for judgment at the boundary of the formal is not a limitation to be engineered away but a capability to be cultivated.

### 12.4 Significance for External Audiences

The contributions of this programme connect to existing problems in multiple fields:

- **AI alignment:** The human-as-incompleteness-response provides formal grounding for the claim that human oversight is structurally necessary, not merely politically desirable. This is directly relevant to current debates at Anthropic, OpenAI, DeepMind, and regulatory bodies.

- **Governance theory:** The Governance Trilemma, if formalized, would establish structural limits on what automated governance can achieve -- relevant to public administration, corporate governance, and platform governance.

- **Philosophy of information:** The four-phase model extends Floridi's levels of abstraction by identifying a generative ordering among levels and associating each with characteristic impossibilities.

- **Software engineering:** The naming-as-compression thesis and the five failure modes provide a theoretical framework for the empirical finding that naming quality correlates with code quality (Butler et al., 2010).

### 12.5 Future Research Directions

1. **Formalization of the Governance Trilemma.** The highest-priority formal agenda: define "governance system" precisely, specify completeness/consistency/measurability formally, and prove the impossibility (or discover that it does not hold under precise definitions).

2. **Embodied meaning as a fifth dimension.** The fork identified in RP-01 v2 and SYN-05 v2: investigate the relationship between formal meaning and embodied/aesthetic/felt meaning using phenomenological and artistic methods.

3. **Empirical validation of the four-phase model.** Test the model against additional independent domains (music theory, urban planning, religious law) to determine whether the four-phase structure is genuinely universal or limited to the domains examined here.

4. **The scaling hypothesis and formal semantics.** Engage empirically with the question of whether transformer-based models implicitly learn the categorical structures that the Curry-Howard-Lambek correspondence describes.

---

## Epilogue: The Wikipedia Origin Story

This dissertation is the product of a sustained, self-directed investigation into the formalization of knowledge -- a research programme conducted under the auspices of the Studium Generale ORGANVM (SGO). The programme originated in a series of seven research adventures undertaken in March 2026, each centred on a sustained reading session through interconnected Wikipedia articles and the scholarly sources they reference.

What began as an exercise in intellectual curiosity -- following hyperlinks from "semantics" to "compositionality" to "lambda calculus" to "Curry-Howard correspondence" -- gradually revealed a coherent structure beneath the surface connections. The articles were not randomly linked. They traced a grand arc from social origins through logical foundations to the limits of self-description.

The Wikipedia origin story is worth telling not as an apology but as evidence. Wikipedia itself is a self-formalizing knowledge system: a rhizomatic network of articles that progressively structures its content through categorization, linking, and editorial governance. The experience of tracing hyperlinks through Wikipedia and discovering formal structure is an instance of the four-phase model in action: naming (the articles designate concepts), structuring (the hyperlinks organize concepts into navigable networks), computing (the reader's interpretive activity transforms structure into understanding), and reflecting (the reader becomes aware of the patterns underlying the surface connections).

This self-referential origin -- a theory of knowledge formalization that was itself formalized through the process it describes -- is not a methodological weakness. It is the theory's most direct evidence.

---

## References

[Retained from v1, with the addition of:]

Arrow, K.J. (1951). *Social Choice and Individual Values*. New Haven: Yale University Press.

Butler, S., et al. (2010). "Exploring the Influence of Identifier Names on Code Quality." *IEEE CSMR*, 156-165.

Floridi, L. (2011). *The Philosophy of Information*. Oxford: Oxford University Press.

Piaget, J. (1970). *Genetic Epistemology*. New York: Columbia University Press.

Carnap, R. (1928). *Der logische Aufbau der Welt*. Berlin: Weltkreis.
