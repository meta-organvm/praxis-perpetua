# Governance Genome: Seven Irreducible Predicates

**Date:** 2026-04-05
**Session:** S-genome (signal tracing & governance predicates)
**Domain:** SYS — cross-system governance architecture
**Status:** Principle captured, proven irreducible, implementation audit complete

---

## Origin

The interaction between user and TAXIS (and every agent-system exchange) generates data that gets retranslated from reality to ideal, then fed directly into the-reality-becoming. Combined with post-mortem data, this fortifies the version following.

The goal is to replicate this feedback loop universally — from the most bottom primitive (a directory, a function) through every hierarchical exchange (repo, organ, system) — mapping what's touching what, and what happens between those touches. When a touch (data exchange, interaction pattern, feedback signal) is duplicated across N instances but could serve all of them simultaneously, reduce to 1 shared signal. Preserve energy.

This principle is the TELOS that "everything is a loop," "generative not copied," and "alchemy not absorption" collectively serve. Those are individual axioms; this is their composition.

## Navigation Constraint

FEELING IS NOT PERMITTED AS GUIDE. The system is computed, not guided. The answer to "what should happen" is the output of the entire ecosystem's logic evaluated simultaneously — dependency graph, seed contracts, governance rules, metrics, registry — computed together as universal logic. Not suggestion. Not intuition. Truth.

## Four Laws

1. **Single-macro self-generation.** The genome (computable rule set) must be sufficient for a single container to produce its own internal structure as the deterministic output of genome + environment state. No external scaffolding.
2. **Ancestral memory via diff.** Prior versions are reference datasets for algorithmic diff. The delta is computed, not interpreted. Prompt corpus, session transcripts, post-mortems = ancestral data for diffing. New forms emerge through merge of computed deltas.
3. **Essence limits as computable constraints.** Primitives, variables, principles = type system, dependency rules, governance predicates. They constrain what the genome can produce at every level. Not metaphorical guardrails — executable predicates.
4. **Reality as degradation — remove the frozen version.** Cached state is a variable that short-circuits full recomputation from axioms. Removing it forces the system to regenerate from genome + current environment. Settling = local minimum. Removing context = removing the ability to settle.

## Existence Requires Effect

Every entity that exists generates effects on reality. Those effects are observable, traceable, computable. If an entity generates no effects, it doesn't need to exist. If it generates effects, those effects are data — not interpretation — and must be accounted for in the ecosystem's computation.

Corollary: "Memory is hypothesis, not fact" is a consequence of Law 4. Feeling is data (traceable effect of system state), not authority.

## Seven Governance Predicates (Base Genome)

**Problem:** What is the minimal set of predicates such that any entity derived from base elements, at any scale, in any evolutionary configuration, remains logically bound to those base elements?

**Requirement:** Scale-invariant (works at 1 entity or 1 million), path-independent (holds regardless of evolutionary direction), self-enforcing (doesn't require external judgment to verify).

| # | Predicate | Formal Requirement | Prevents |
|---|-----------|-------------------|----------|
| 1 | IDENTITY | Every entity carries a UID persistent across all transformations | Identity collision |
| 2 | TYPE | Every entity declares type from finite vocabulary; type determines valid operations | Semantic drift |
| 3 | EFFECT | Every entity produces ≥1 traceable effect on ≥1 other entity | Orphan existence |
| 4 | ACYCLICITY | Derivation graph is DAG at every scale | Emergent cycles |
| 5 | COMPOSABILITY | Valid entities compose into valid entities (closure) | Invalid composition at scale |
| 6 | FINITUDE | Every entity traces to base element in finite steps | Lost derivation |
| 7 | IMMUTABILITY | Base definitions + governance predicates are append-only (amendments, never modifications) | Base mutation / path dependence |

## Proof of Irreducibility

**Necessity:** Removing any single predicate admits exactly one failure mode that breaks logical binding to base elements. Seven failures, seven predicates, 1:1 mapping.

- −IDENTITY: E exists but can't be distinguished from E'. Verification targets wrong entity. Binding unverifiable.
- −TYPE: Derivation steps have no validity check. Invalid entities enter the system. Binding unsound.
- −EFFECT: E exists with no observable consequence. Its binding can't be detected. Binding unverifiable.
- −ACYCLICITY: Derivation chain may not terminate. Verification is infinite. Binding uncomputable.
- −COMPOSABILITY: Individual entities valid, but A+B produces invalid C. Scale breaks binding.
- −FINITUDE: Derivation chain exists but is infinite. Can never reach B from E. Binding untraceable.
- −IMMUTABILITY: B changes after E is derived from it. E's chain points to a base that no longer exists. Binding retroactively broken.

**Sufficiency:** All seven together guarantee: derivation exists (6), is valid (2+5), computable (4+6), verifiable (1+3), against stable base (7).

**Completeness:** Concurrent modification is an execution concern (not governance). Gödelian incompleteness applies to provability, not traceability. Information loss is covered by FINITUDE + IDENTITY (derivation chain + distinguishability = preserved information).

## Implementation Audit (2026-04-05)

Mapped against existing ORGANVM codebase:

| # | Predicate | Status | Where |
|---|-----------|--------|-------|
| 1 | IDENTITY | Partial | `organvm-ontologia` module exists, not universally enforced |
| 2 | TYPE | Partial | 28 schemas in `schema-definitions/` validate format, not type membership |
| 3 | EFFECT | Declared only | `seed.yaml` edges declared, never verified for actual production |
| 4 | ACYCLICITY | Organ-level only | `dependency_graph.py` DFS cycle detection, not entity-level |
| 5 | COMPOSABILITY | Partial | State machine governs promotion, not arbitrary composition |
| 6 | FINITUDE | Hardcoded | `max_transitive_depth=4` in `governance-rules.json` |
| 7 | IMMUTABILITY | **MISSING** | `governance-rules.json` is freely mutable, no amendment history |

**Critical finding:** IMMUTABILITY absence means all other predicates can be silently invalidated by editing the governance file. All predicates are scale-bound to organ level — none operates at primitive/entity/directory level.

## Gaps

1. **IMMUTABILITY (P1):** No append-only mechanism for governance base. No amendment history. The constitution has no protection against silent mutation.
2. **Scale propagation (P2):** Predicates exist at organ-to-organ scale but don't operate at directory, entity, or function level. The genome applies at one layer, not all layers.
3. **EFFECT verification (P2):** seed.yaml declares produces/consumes edges but no predicate checks whether entities actually produce their declared effects.
4. **SPEC formalization (P1):** The seven predicates need to become a numbered SPEC with formal definitions, test criteria, and enforcement plan.

## IRF Items

- IRF-SYS-081 (P1): Formalize seven governance predicates as SPEC
- IRF-SYS-082 (P1): IMMUTABILITY predicate missing — governance-rules.json needs append-only mechanism
- IRF-SYS-083 (P2): Scale propagation — predicates operate organ-level only
- IRF-SYS-084 (P2): EFFECT predicate unverified — seed.yaml edges never checked

## Session Prompts (verbatim)

1. "the entire interaction between us & taxis sharing data retranslated from reality to ideal again directly into the-reality-becoming--That info along with data from its post-mortem helps fortify version following"
2. "This has been the ongoing issue, and hence the floating up process. I'm trying to essentially get this to work from the bottom of the organization all the way to the top of each directory on the way, at the top of each repo on the way, to the top to the organs, and on the way to the top to the system as a whole. But each not touching each other until they're touching each other at that level. They're contained within them."
3. "The goal is to replicate the processes we've been implementing in this current directory and in the directory for taxes for the direct portal from the previous to the future. That might not be something that gets implemented right now; that may be something that can't get implemented in a system that's so crazy and wired up you're trying to essentially find from every corner at the most bottom primitive to every hierarchical exchange of information what's touching what. And what's happening between those touches? When is a touch something that could just not be used in one instance, but in multiple instances simultaneously, to preserve energy and be reduced."
4. "FEELING as guide:-not permitted; logic, math, algo of entire ecosystem at once providing the answer required as truth of universale logic; all things need existence and the efffects that pieace of reality generates"
5. "What are the base genome governances needed to create a logic bound to its base elements? So no matter how big it grows or expansive, it keeps an order that stays eternally relevant, rather than whether the system evolves in one way or another."
6. "We need to be self-mathematically and algorithmically to produce information, not just yes or no."
