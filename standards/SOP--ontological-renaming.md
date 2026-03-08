---
sop: true
name: ontological-renaming
scope: system
phase: foundation
triggers:
  - context:new-project
  - context:identity-revision
complements:
  - repo-onboarding-and-habitat-creation
overrides: null
---
# SOP: Ontological Renaming

**Version:** 1.0.0 | **Date:** March 8, 2026 | **Status:** Active
**Scope:** Naming and renaming of repos, organs, systems, and conceptual units across the ORGANVM system.

---

## 1. Ontological Purpose

Names are not labels — they are compressed ontologies. A name like `sema-metra--alchemica-mundi` encodes what the thing *is* (sign-measurement), what it *does* (world-alchemy), and how its parts relate (tight coupling within, loose coupling between). This SOP codifies the naming philosophy that makes ORGANVM repos self-documenting at the filesystem level.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 3: Governance & Lifecycle)
**Cross-reference:** `SOP--repo-onboarding-and-habitat-creation.md` Phase I (naming as part of repo creation)

---

## 2. Trigger

Execute this SOP when:
- Creating a new repository, organ, or system component
- An existing name no longer describes the thing's evolved purpose
- A project is being promoted from LOCAL to CANDIDATE (names become public-facing)
- Consolidating or splitting repos requires new identity

**Exception:** Internal module/function naming within code follows language conventions (PEP 8, camelCase, etc.), not this SOP.

---

## 3. Phase I: Essence Extraction

**Goal:** Understand what the thing *is* before naming it.

### Process

1. **State the thing's purpose** in one sentence without using its current name
2. **Identify the primary domain:** theory, art, commerce, governance, discourse, community, distribution, meta
3. **Identify the primary action:** what does this thing *do*? (compute, generate, govern, distribute, teach, etc.)
4. **Identify the scope:** system-wide, organ-level, repo-level, module-level
5. **List 5-10 concept words** that capture the essence (English first, then etymological roots)

### Output
An essence statement and concept word cloud.

---

## 4. Phase II: Etymological Research

**Goal:** Find roots that compress meaning.

### Process

1. **Research Latin and Greek roots** for each concept word:
   - Latin for institutional/structural concepts (corpus, praxis, lex, ordo)
   - Greek for theoretical/philosophical concepts (theoria, poiesis, logos, taxis)
   - Mixed when the concept spans both domains
2. **Check for existing ORGANVM naming patterns:**
   - Organ names use Greek: theoria, poiesis, ergon, taxis, logos, koinonia, kerygma
   - System names use Latin: corpvs, praxis, alchemia
   - Double-hyphen separates function from descriptor
   - Single hyphen separates words within a component
3. **Generate 5-10 candidate names** following the convention:
   - 2-4 words per component
   - Each word carries semantic weight (no filler words)
   - The name should be pronounceable (not an acronym or random string)
4. **Validate each candidate:**
   - Does it describe the thing's essence without explanation?
   - Is it distinct from existing names in the system? (Check `registry-v2.json`)
   - Does it follow the double-hyphen convention if it has two semantic components?
   - Is it memorable and pronounceable?

### Output
A ranked candidate list with etymological annotations.

---

## 5. Phase III: Selection & Propagation

**Goal:** Choose the name and update all references.

### Process

1. **Select the best candidate** based on: semantic density > distinctiveness > pronounceability > aesthetic
2. **If renaming an existing entity:**
   - Update GitHub repo name via `gh repo rename`
   - Update `seed.yaml` (organ, name fields)
   - Update `registry-v2.json` via `organvm registry update`
   - Update all cross-references in other repos' `seed.yaml` edges
   - Update superproject submodule path
   - Run `organvm context sync` to regenerate context files
3. **If naming a new entity:**
   - Proceed to `SOP--repo-onboarding-and-habitat-creation.md` Phase II with the chosen name
4. **Document the naming decision** in the repo's README or CLAUDE.md with etymological explanation

### Output
The selected name, propagated across all system references.

---

## 6. Naming Convention Reference

| Pattern | Example | When |
|---------|---------|------|
| `word-word` | `public-record` | Simple, self-descriptive |
| `word-word--word-word` | `sema-metra--alchemica-mundi` | Two semantic components |
| `latin-concept` | `corpvs-testamentvm` | Institutional/governance |
| `greek-concept` | `praxis-perpetua` | Theoretical/philosophical |
| `action--domain` | `agent--claude-smith` | Tool with specific function |

### Anti-patterns
- Acronyms as names (`OEMS`, `ATSP`) — opaque, not self-documenting
- Generic names (`utils`, `helpers`, `misc`) — say nothing about essence
- Version numbers in names (`project-v2`) — use git tags instead
- Overly long names (>40 chars) — compress, don't enumerate

---

## 7. Starter Research Questions

- What is the etymological root of the concept this thing embodies?
- Does the current name still describe what the thing has become?
- Would a stranger understand the name's domain from the name alone?
- Does the name harmonize with sibling repos in the same organ?

---

## 8. Output Artifacts

- Selected name with etymological annotation
- Updated `registry-v2.json` entry (if rename)
- Updated `seed.yaml` (if rename)
- Updated cross-references across the system

---

## 9. Verification

- [ ] Name follows double-hyphen convention (if multi-component)
- [ ] Name uses appropriate language roots (Latin for institutional, Greek for theoretical)
- [ ] Name is distinct from all other entries in `registry-v2.json`
- [ ] Etymological explanation is documented in README or CLAUDE.md
- [ ] All cross-references updated (if rename)

---

## 10. Prompt Examples

Representative prompts from clipboard history that trigger this pattern:

### Example 1

> $ROOT_LAYER="~" $ROOT_HANDLE="@4444J99" $ROOT_ROLE="substrate–home–liminal root"
> 1) Root Layer Ontological Names (10 options)
> Each option is 3–4 words, - = close coupling, -- = distant coupling.

### Example 2

> Structural Analysis: sema-metra--alchemica-mundi is a hybridized ontological compound
> that deliberately mixes Greek and Latin to signal depth over philological purity.

### Example 3

> Etymological Analysis of Three Organ Names: ivviiviivvi — Pattern: Roman numerals
> arranged in a specific palindromic-adjacent sequence
