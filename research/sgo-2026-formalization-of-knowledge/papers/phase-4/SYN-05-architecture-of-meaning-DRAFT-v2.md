---
sgo_id: SGO-2026-SYN-005
title: "The Architecture of Formal Meaning"
tier: Dissertation (synthesis)
status: LOCAL (revised draft)
target_venues: [Synthese, Philosophy and Phenomenological Research, arXiv cs.AI]
dependencies: [RP-01, RP-02, RP-04, RP-06, SYN-01]
bridges: [Adventure 1, Adventure 2, Adventure 4, Adventure 6]
date: 2026-03-21
revision_date: 2026-03-20
version: v2
revision_notes: |
  TRP review required revise-and-re-review (1/3 advance, 1/3 revise, 1/3 fork).
  Key amendments incorporated:
  - Accepted the fork: reframed as "Architecture of Formal Meaning" per POV 2 and POV 3.
    Title changed. Scope explicitly limited to formally characterizable meaning.
  - Made four dimensions falsifiable: Section 3.5 specifies what would count as evidence
    that a dimension is unnecessary.
  - Added Section 4.5: aesthetic/felt meaning as a genuine fifth dimension that this paper
    brackets but does not deny.
  - Reduced boundary-object usage per corpus-level critique.
  - Qualified the "sufficiency" claim: sufficient for formal meaning within the scope
    of this programme.
  - Replaced "strange loop" with "cyclic constraint" where the stronger claim is unformalized.
---

# The Architecture of Formal Meaning: A Unified Account from Naming Through Formalization to the Limits of Self-Description

**Studium Generale ORGANVM -- Cross-Adventure Synthesis SYN-05**

**Synthesis of RP-01 (The Semantics Bridge), RP-02 (Self-Reference and Limits), RP-04 (The Naming Problem), and RP-06 (Chomsky to Computation)**

---

## Abstract

This dissertation undertakes the penultimate synthesis of the Studium Generale ORGANVM research programme, unifying four prior investigations into a single architectural account of *formal meaning*. The central claim is that formal meaning -- meaning as it can be characterized by mathematical and logical methods -- is not a single phenomenon but a four-dimensional architecture, whose dimensions are Reference (how meaning attaches to the world), Structure (how meaning composes), Computation (how meaning is realized in processing), and Reflexivity (where meaning encounters its own limits). These four dimensions are orthogonal aspects of a single phenomenon, standing in a cyclic dependency: Reference constrains Structure, Structure constrains Computation, Computation constrains Reflexivity, and Reflexivity constrains Reference. The paper develops this architectural claim, compares it with existing frameworks, argues that four dimensions are necessary and sufficient *for the formal aspects of meaning examined by this programme*, and examines what the architecture cannot capture. A dedicated section addresses the aesthetic, embodied, and phenomenological dimensions of meaning that this paper brackets but explicitly acknowledges as genuine and important -- a fifth dimension that falls outside the scope of formal analysis but is not thereby dismissed.

**Keywords:** meaning, philosophy of language, compositionality, self-reference, naming, type theory, category theory, Curry-Howard-Lambek correspondence, incompleteness, architecture of meaning, functorial semantics, formal meaning

---

## 1. Introduction

### 1.1 The Convergence of Four Investigations

[Retained from v1 with minor revisions.]

### 1.2 The Question That Unifies Them

These four investigations converge on a single, deeper question: *what is the architecture of formal meaning?*

RP-04 answered: formal meaning begins with reference -- the attachment of a sign to a thing. RP-01 and SYN-01 answered: formal meaning is constituted by composition -- the functorial passage from syntax to semantics. RP-06 answered: formal meaning is realized through computation. RP-02 answered: formal meaning is bounded by reflexivity.

These are four aspects of a single architecture. The thesis of this dissertation is that Reference, Structure, Computation, and Reflexivity are the four dimensions of formal meaning, and that any formally characterizable aspect of meaning falls within one of these dimensions.

### 1.3 Scope and Framing

This dissertation is explicitly limited to *formal meaning* -- meaning as it can be characterized by mathematical, logical, and computational methods. This scope limitation is not a claim that formal meaning exhausts meaning. Section 4.5 addresses the dimensions of meaning that fall outside the formal architecture: aesthetic meaning, embodied meaning, felt sense, and phenomenological understanding. These are genuine and important dimensions of meaning that this paper *brackets* (in the Husserlian sense) rather than denies.

The decision to focus on formal meaning is methodological, not metaphysical. The four prior investigations all employ formal methods, and the architecture synthesizes their formal findings. A companion investigation of non-formal meaning would require different methods (phenomenological, ethnographic, artistic) and would produce a different kind of contribution.

---

## 2. Four Dimensions of Formal Meaning

### 2.1 The Referential Dimension (from RP-04)

[Retained from v1, with the qualification that this describes the referential dimension of *formal* meaning -- the question of how signs attach to referents through mechanisms that admit formal characterization (Fregean sense, Kripkean causal chains, Peircean sign-relations).]

### 2.2 The Structural Dimension (from RP-01/SYN-01)

[Retained from v1, with the following clarification:]

The claim that "meaning is the functorial passage from a syntactic category to a semantic category" is a *framework choice*, not a discovery about the nature of meaning. It is chosen because it unifies the three traditions of compositional formal semantics with mathematical precision. An inferentialist like Brandom (1994) would characterize meaning differently -- as constituted by inferential relations among sentences, with semantics derivative from pragmatics. The functorial characterization is one possible formalization, selected for its unifying power across the traditions this programme examines.

### 2.3 The Computational Dimension (from RP-06)

[Retained from v1.]

### 2.4 The Reflexive Dimension (from RP-02)

[Retained from v1.]

---

## 3. The Architectural Claim

### 3.1 Orthogonality

[Retained from v1.]

### 3.2 Cyclic Dependency

The four dimensions stand in a cyclic dependency: Reference constrains Structure (what can be named constrains what can be composed), Structure constrains Computation (what can be composed constrains what can be computed), Computation constrains Reflexivity (what can be computed constrains what can be self-described), and Reflexivity constrains Reference (what can be self-described constrains what can be named about the system itself).

This cyclic dependency is presented as a *cyclic constraint* rather than as a "strange loop" in Hofstadter's precise sense. Hofstadter's strange loops arise in systems where traversing a hierarchy of levels brings you back to the starting level (Godel sentences, Escher's Drawing Hands). The architectural cycle described here is a weaker claim: the four dimensions constrain each other in a directed cycle, and the constraints are *boundary conditions*, not level-crossings. The cycle is productive in the sense that each constraint generates the conditions for the next dimension's operation, but formalizing this productivity -- proving that the cycle converges rather than diverging -- would require fixed-point theory or category-theoretic recursion that this paper does not provide.

The formalization gap is acknowledged: the cyclic constraint is a structural observation about the relationships among the four dimensions, not a formally proven property. Formalizing it -- defining the constraint functions, specifying the iteration domain, and proving convergence -- is identified as future work.

### 3.3 Comparison with Existing Frameworks

[Retained from v1.]

### 3.4 Necessity

The argument for the necessity of each dimension: removing any one produces an incomplete account of formal meaning.

- Without Reference, there is no account of how formal expressions attach to what they are about. Pure structure (syntax without semantics) is not meaning.
- Without Structure, there is no account of how complex meanings are built from simple ones. Isolated references (names without composition) cannot represent propositional content.
- Without Computation, there is no account of how meanings are processed, and the decidability/complexity constraints that shape what can be practically formalized are invisible.
- Without Reflexivity, there is no account of formal meaning's limits -- the impossibility results that constrain all self-describing systems.

### 3.5 Sufficiency and Falsifiability

The sufficiency claim requires careful statement. The claim is: **every formally characterizable aspect of meaning examined by this programme falls within one of the four dimensions.** This is a claim about the scope of the programme, not a universal claim about meaning. Whether additional formal dimensions are required for phenomena outside this programme's scope is an open question.

The sufficiency claim is falsifiable. It would be refuted by:

1. **A formally characterizable aspect of meaning that does not fit any of the four dimensions.** For example: if pragmatic meaning (Gricean implicature, conversational inference) could be fully formalized -- which is an open question -- and if the resulting formal framework did not reduce to reference, structure, computation, or reflexivity, that would constitute a fifth formal dimension. Dynamic semantics (meaning as context-change potential) is a candidate, but current formalizations of dynamic semantics use the computational dimension's apparatus (state transformers) and thus fall within the architecture.

2. **Evidence that one of the four dimensions is redundant -- that it reduces to a combination of the other three.** For example: if reference could be shown to be fully determined by structure (the purely inferentialist program of Brandom), then the referential dimension would be eliminable. The programme's evidence suggests otherwise (reference failure is a distinct phenomenon from structural failure), but the eliminability question is empirically testable.

3. **A formal framework for meaning that uses fewer than four dimensions and achieves the same coverage.** If a three-dimensional architecture could account for all the phenomena that the four-dimensional architecture covers, parsimony would favor the simpler framework.

No such refutation has been produced, but stating the conditions makes the claim scientifically tractable rather than vacuously true.

---

## 4. The Limits of the Architecture

### 4.1 Pragmatics

[Retained from v1.]

### 4.2 Embodied Meaning

[Retained from v1, with expanded treatment:]

The embodied cognition research program (Lakoff and Johnson, 1980; Varela, Thompson, and Rosch, 1991; Barsalou, 2008) argues that meaning is grounded in sensorimotor experience. The word "grasp" means what it means because speakers have bodies that grasp things, and the conceptual meaning is metaphorically extended from embodied experience. This grounding is not captured by any of the four formal dimensions.

### 4.3 Non-Formal Self-Reference

[Retained from v1.]

### 4.4 The Hermeneutic Dimension

[Retained from v1.]

### 4.5 Aesthetic and Felt Meaning: A Genuine Fifth Dimension

This section addresses the most consequential absence from the four-dimensional architecture. The TRP review identified this absence as a structural problem, not a mere limitation, and the author concurs.

**Aesthetic meaning.** A painting by Rothko -- a field of luminous red hovering over a darker red -- means something. Not in the referential sense (it does not refer to anything). Not in the structural sense (its meaning does not compose from the meanings of its parts). Not in the computational sense (the meaning has no decidability properties). Not in the reflexive sense (the painting does not describe itself). Yet it *means*. It means in a way that changes the person who stands before it. The four-dimensional architecture has no account of this meaning.

**Musical meaning.** Music means without referring, without composing in the logical sense, without computing, and without self-describing. A melody creates tension, resolution, expectation, surprise. This movement is meaning in a temporally constituted form that the architecture's static categories cannot capture.

**Felt sense.** Gendlin's (1962, 1997) concept of the felt sense -- a pre-conceptual, bodily awareness of a situation's meaning -- proposes that meaning begins before formalization and continues to operate beneath it. The felt sense is "more precise than any verbal formulation," which suggests that the formal architecture is an abstraction from a more fundamental meaning-layer.

**The bracketing decision.** This paper brackets these dimensions not because they are unimportant but because the methods of this programme (formal analysis, mathematical characterization, logical argumentation) cannot capture them. To capture aesthetic meaning would require phenomenological methods (Merleau-Ponty), hermeneutic methods (Gadamer, Ricoeur), or artistic methods (direct creative practice). These are legitimate meaning-investigation methods that fall outside the scope of formal analysis.

The relationship between formal meaning and aesthetic/felt meaning is one of the deepest open questions the programme surfaces. Three possible relationships:

1. **Abstraction.** Formal meaning is an abstraction from a more fundamental lived/felt meaning. On this view, the four-dimensional architecture describes the skeleton of meaning, and aesthetic/felt meaning is the flesh. The architecture is valid but incomplete -- a useful map that omits the territory's most important features.

2. **Orthogonality.** Formal meaning and aesthetic/felt meaning are genuinely independent dimensions. Neither is more fundamental than the other; they address different aspects of the meaning phenomenon. The architecture is valid within its domain and has no obligation to capture what lies outside it.

3. **Irreducibility.** Formal meaning and aesthetic/felt meaning are aspects of a single phenomenon that cannot be captured by any one method. A complete account of meaning would require integrating formal, phenomenological, and artistic methods -- a methodological pluralism that no single paper can achieve.

This paper does not resolve the question but names it explicitly. The architecture of formal meaning is the architecture of meaning's formalizable aspects. Whether meaning has non-formalizable aspects that are constitutive rather than residual is a question that the architecture itself cannot answer.

---

## 5. Implications

### 5.1 For Philosophy of Language

[Retained from v1, with the qualification that the implications concern formal meaning specifically.]

### 5.2 For Artificial Intelligence

The syntactic/semantic boundary -- the distinction between decidable syntactic properties and undecidable semantic properties -- is the architecture's most practically important finding for AI. Automated governance should focus on syntactic properties (which are decidable and can be reliably checked) and delegate semantic properties (which are undecidable) to human judgment. This finding provides formal grounding for the "human-in-the-loop" design pattern: human judgment is not a temporary crutch awaiting better AI but a structural response to proven impossibility results.

### 5.3 The ORGANVM Case Study

[Retained from v1, with the following addition:]

The case study illustrates the architecture's formal dimensions but inadvertently reveals its limitations. The seed.yaml contracts (referential dimension), registry operations (structural dimension), CI/CD pipelines (computational dimension), and IRA panel (reflexive dimension) are all formal, explicit, machine-processable. The *informal* dimension -- the tacit knowledge of the system's operator, the aesthetic judgments about naming, the felt sense of whether a design "works" -- is absent from the case study and from the architecture. This informal dimension is not a residual; it is the context that gives the formal system its purpose and direction.

---

## 6. Discussion

### 6.1 The Five-Way Correspondence Table

The five-way correspondence table -- asserting that a grammatical derivation, a proof, a program, a morphism, and a meaning-composition are the same activity in five mathematical languages -- is the paper's most concrete formal contribution. The first four correspondences have the backing of proven mathematical isomorphisms (Curry-Howard-Lambek). The fifth ("IS meaning assignment") rests on the functorial account of meaning, which is a thesis of this programme, not a proven result in mathematics.

The five-way correspondence should therefore be presented at two levels: (a) the proven four-way correspondence (grammar-proof-program-morphism), which has the status of a mathematical theorem; and (b) the conjectured five-way extension (adding meaning-assignment), which has the status of a well-motivated conjecture grounded in the functorial account of meaning. Formalizing the conjecture -- proving that the functorial meaning-assignment is isomorphic to the other four correspondences under precisely stated conditions -- is the highest-priority formal agenda for subsequent work.

### 6.2 Formal Status Summary

| Claim | Status |
|-------|--------|
| Four dimensions are necessary | Argued (each dimension's removal produces an incomplete account) |
| Four dimensions are sufficient for formal meaning | Conjectured (no counterexample within this programme's scope) |
| Cyclic constraint among dimensions | Observed (structural description, not formally proven) |
| Five-way correspondence (4-way core) | Theorem (Curry-Howard-Lambek) |
| Five-way correspondence (5th column) | Conjecture (functorial meaning-assignment) |
| Functorial characterization of meaning | Framework choice (productive, not unique) |

---

## 7. Conclusion

This paper has developed a four-dimensional architecture of formal meaning -- Reference, Structure, Computation, Reflexivity -- arguing that these four dimensions are necessary and, within the scope of this programme, sufficient for characterizing the formally tractable aspects of meaning.

The architecture is explicitly limited to formal meaning. The aesthetic, embodied, and phenomenological dimensions of meaning are acknowledged as genuine, important, and outside the architecture's scope. The relationship between formal and non-formal meaning -- whether it is abstraction, orthogonality, or irreducibility -- is identified as the deepest open question the programme surfaces.

The cyclic constraint among dimensions is a structural observation that invites formalization. The five-way correspondence table is a conjecture extending a proven four-way mathematical correspondence. The falsifiability conditions for the architecture's claims are stated, making the framework scientifically tractable.

---

## References

Barsalou, L.W. (2008). "Grounded Cognition." *Annual Review of Psychology*, 59, 617-645.

Brandom, R. (1994). *Making It Explicit*. Cambridge, MA: Harvard University Press.

Gendlin, E.T. (1962). *Experiencing and the Creation of Meaning*. New York: Free Press.

Gendlin, E.T. (1997). *A Process Model*. New York: Spring Valley.

Lakoff, G. and Johnson, M. (1980). *Metaphors We Live By*. University of Chicago Press.

Merleau-Ponty, M. (1945). *Phenomenologie de la perception*. Paris: Gallimard.

Varela, F.J., Thompson, E., and Rosch, E. (1991). *The Embodied Mind*. MIT Press.

[Additional references retained from v1.]
