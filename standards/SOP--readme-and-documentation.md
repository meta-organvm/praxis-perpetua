---
sop: true
name: readme-and-documentation
scope: system
phase: foundation
triggers:
  - context:new-project
  - context:promotion-to-candidate
  - context:post-feature-expansion
complements:
  - repo-onboarding-and-habitat-creation
  - structural-integrity-audit
overrides: null
---
# SOP: README & Documentation Generation

**Version:** 1.0.0 | **Date:** March 8, 2026 | **Status:** Active
**Scope:** Creating and maintaining READMEs and project documentation that function as portfolio pieces, not just developer guides.

---

## 1. Ontological Purpose

A README is a repo's first and often only impression. In the ORGANVM system, every repo is a portfolio piece — written for grant reviewers, hiring managers, and collaborators, not just the developer who wrote it. This SOP codifies the "world-class README" standard: every README communicates Problem → Approach → Outcome with the clarity of a pitch deck and the depth of a technical specification.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 1: Content & Publishing)
**Cross-reference:** `SOP--repo-onboarding-and-habitat-creation.md` Phase II (README as part of repo creation), Standard `10-repository-standards.md` (root hygiene)

---

## 2. Trigger

Execute this SOP when:
- Creating a new repo (as part of `SOP--repo-onboarding-and-habitat-creation.md`)
- Promoting a repo from LOCAL to CANDIDATE (README becomes public-facing)
- After significant feature expansion that changes the project's scope
- Quarterly review flags a repo with a skeletal or outdated README

**Exception:** Infrastructure repos (CI configs, template repos) may use minimal READMEs.

---

## 3. Phase I: Hero Section

**Goal:** Capture attention in the first 10 lines.

### Process

1. **Write the title** — the repo name, optionally with a display name
2. **Write the one-liner** — what this project *is* in one sentence
3. **Write the problem statement** — what pain does this solve? For whom?
4. **Write the approach** — how does this project solve the problem? What makes it different?
5. **Write the outcome** — what does the user get? What does the world look like after adoption?

### Format

```markdown
# project-name

> One-sentence description of what this is.

## Problem

[2-3 sentences on the pain point]

## Approach

[2-3 sentences on the solution and what makes it unique]

## Outcome

[2-3 sentences on the result — what changes for the user]
```

### Output
A hero section that communicates value in <30 seconds of reading.

---

## 4. Phase II: Technical Depth

**Goal:** Provide the detail that developers, reviewers, and collaborators need.

### Process

1. **Key Features** — bulleted list of 5-10 capabilities, each in one line
2. **Architecture** — high-level description of how the system is structured:
   - Module/package layout
   - Data flow
   - Key abstractions
3. **Getting Started** — copy-paste-ready setup commands:
   ```
   git clone ...
   cd ...
   [install]
   [run]
   ```
4. **Usage** — the 3-5 most common commands or API calls with examples
5. **Configuration** — environment variables, config files, feature flags

### Output
A technical section that enables a new contributor to be productive in <15 minutes.

---

## 5. Phase III: Context & Cross-References

**Goal:** Situate the project within the larger system.

### Process

1. **System Context** — which organ does this belong to? What are its edges?
2. **Related Projects** — link to sibling repos, upstream dependencies, downstream consumers
3. **Contributing** — link to CONTRIBUTING.md or inline contribution guidelines
4. **License** — state the license with a link to the LICENSE file
5. **Auto-generated sections** — if the repo uses `organvm context sync`, include the `<!-- ORGANVM:AUTO:START -->` block

### Output
A context section that connects this repo to the broader ecosystem.

---

## 6. Phase IV: CLAUDE.md / GEMINI.md / AGENTS.md

**Goal:** Provide AI agent context files.

### Process

1. **Run `organvm context sync`** to generate/update context files
2. **Review generated content** for accuracy — auto-generation is a starting point, not final copy
3. **Add project-specific instructions:**
   - Build/test/lint commands
   - Architecture notes that help agents navigate the codebase
   - Conventions and patterns unique to this project
4. **Keep CLAUDE.md under 200 lines** for efficient context loading

### Output
Context files that enable any AI agent to work effectively in the repo.

---

## 7. Quality Criteria

A world-class README meets all of these:

- [ ] **Problem is externally meaningful** — a stranger understands why this exists
- [ ] **Hero section works without scrolling** — value is clear in 10 lines
- [ ] **Setup is copy-paste** — no ambiguity, no missing steps
- [ ] **Architecture is visual or diagrammatic** — not just prose
- [ ] **Word count ≥ 1,500** for flagship/standard repos (portfolio standard)
- [ ] **No broken links** — all cross-references resolve
- [ ] **No stale content** — features described actually exist in the code

---

## 8. Starter Research Questions

- What would a grant reviewer need to understand about this project in 2 minutes?
- What would a hiring manager conclude about the developer from this README?
- Does the README accurately reflect the current state of the codebase?
- Are sibling repos in the same organ using a consistent README style?

---

## 9. Output Artifacts

- `README.md` — the primary documentation
- `CLAUDE.md` / `GEMINI.md` / `AGENTS.md` — AI agent context files
- `CONTRIBUTING.md` (optional, for repos accepting external contributions)

---

## 10. Verification

- [ ] Hero section communicates Problem → Approach → Outcome
- [ ] Getting Started section has copy-paste setup commands
- [ ] Architecture section describes the system structure
- [ ] No broken links or stale feature descriptions
- [ ] Context files are generated and reviewed
- [ ] Word count meets portfolio standard for the repo's tier

---

## 11. Prompt Examples

Representative prompts from clipboard history that trigger this pattern:

### Example 1

> Process: begin with creating, updating, amending, or adding to the README file.
> This step establishes the foundation for the documentation and ensures the hero
> section is prepared to communicate the project's purpose.

### Example 2

> ecosystem-theory — Display name ECOSYSTEM · THEORY — THEORIA–DOCUMENTA–LEX
> Mission sentence: Author and maintain the conceptual substrate

### Example 3

> COMPREHENSIVE REPOSITORY ALIGNMENT QUESTIONNAIRE — Please answer as thoroughly
> or briefly as you prefer. Your answers will guide our reorganization strategy.
