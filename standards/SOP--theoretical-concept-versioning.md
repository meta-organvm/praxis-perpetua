# SOP: Theoretical Concept Versioning (The Epistemic Protocol)

## 1. Ontological Purpose
This SOP fills the Architecture Records gap in ORGAN-I (Theoria). Because pure philosophical theory does not compile like code, it requires a unique versioning protocol to track how concepts evolve, fork, or merge based on community feedback and commercial realities.

**Governed by:** `METADOC--sop-ecosystem.md`
**Applicable to:** ORGAN-I (Theoria) theoretical repositories.

---

## 2. Phase I: Concept Hashing
**Goal:** Create a cryptographically stable ID for an abstract idea.
1. **Definition:** When a new theory is drafted, summarize it into a strict 500-word abstract.
2. **Hashing:** Run the abstract through SHA-256 to generate the "Genesis Hash" for that concept.
3. **Registry:** Store the Genesis Hash in the repo's `seed.yaml` as the `epistemic_root`.

## 3. Phase II: Thesis Commits
**Goal:** Track evolutionary changes over time.
1. **Semantic Versioning for Philosophy:**
    - **MAJOR:** A complete paradigm shift or contradiction of the previous thesis.
    - **MINOR:** Expansion or clarification of an existing concept.
    - **PATCH:** Fixing typographical errors or updating citations.
2. **Changelog:** Maintain a `THEORY_CHANGELOG.md` detailing the philosophical justification for every Minor or Major bump.

## 4. Phase III: Dialectical Branching
**Goal:** Handle intellectual disagreements.
1. **Forking:** If a concept splits (e.g., due to feedback from an ORGAN-VI salon), create a new Git branch.
2. **Resolution:** Use `SOP--formal-methods-master-taxonomy.md` (Dialogical Logic) to debate the two branches. If one branch is proven superior, merge it into main. If both are valid but distinct, split them into two separate ORGAN-I repositories.

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
