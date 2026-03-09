---
sop: true
name: architecture-decision-records
scope: system
phase: foundation
triggers:
  - context:architecture-change
  - context:technology-selection
  - context:api-design
complements:
  - api-design-patterns
  - coding-standards-enforcer
overrides: null
---
# SOP: Architecture Decision Records

**Version:** 1.0.0 | **Date:** March 8, 2026 | **Status:** Active
**Scope:** Capturing, tracking, and evolving architecture decisions across all ORGAN-III products and infrastructure repos.

---

## 1. Ontological Purpose

Architecture decisions are the bones of a system. They are invisible once made — buried under layers of code — but they determine what the organism can and cannot become. Without a record, teams (and future AI agents) cannot distinguish between "we chose X because of Y" and "X is here because nobody questioned it." ADRs make the invisible visible.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 5: Planning & Design)
**Cross-reference:** `SOP--repo-onboarding-and-habitat-creation.md` (ADR directory created at onboarding), `SOP--completeness-verification.md` (ADR presence checked at promotion gates)

---

## 2. Trigger

Execute this SOP when:
- Selecting a technology, framework, or service for a new or existing product
- Changing a public API contract (breaking or non-breaking)
- Choosing between two or more viable architectural approaches
- Deprecating or replacing an existing technical decision
- A previous ADR is challenged by new evidence or changed requirements

**Exception:** Trivial implementation choices (variable naming, formatting, minor refactors) do not require ADRs.

---

## 3. ADR Format

Every ADR follows this structure. The format is already de facto established by Styx's 5 ADRs and is now codified system-wide.

```markdown
# ADR-NNN: {Title}

**Status:** Proposed | Accepted | Deprecated | Superseded by ADR-NNN
**Date:** YYYY-MM-DD
**Decision-makers:** {persona(s) or human role}
**Department:** ENG

## Context

What is the issue that motivates this decision? What forces are at play?

## Decision

What is the change that is being proposed or decided?

## Consequences

What becomes easier or harder as a result of this decision?

### Positive
- ...

### Negative
- ...

### Neutral
- ...

## Alternatives Considered

| Alternative | Pros | Cons | Why Rejected |
|-------------|------|------|--------------|
| ... | ... | ... | ... |
```

---

## 4. Lifecycle

ADRs progress through a linear state machine:

```
Proposed → Accepted → [Deprecated | Superseded by ADR-NNN]
```

| State | Meaning |
|-------|---------|
| **Proposed** | Under discussion. Not yet binding. |
| **Accepted** | Ratified. The decision is in effect and code should conform. |
| **Deprecated** | The decision is no longer relevant (technology removed, feature sunset). |
| **Superseded** | A newer ADR replaces this one. Must reference the superseding ADR. |

**Transition rules:**
- Proposed → Accepted: requires at least one review pass (human or AI agent)
- Accepted → Deprecated: the context that motivated the decision no longer exists
- Accepted → Superseded: a new ADR explicitly references and replaces this one
- No state can be skipped. An ADR cannot go from Proposed directly to Deprecated.

---

## 5. Numbering Convention

- ADRs are numbered sequentially per repository: `ADR-001`, `ADR-002`, etc.
- Numbers are never reused, even after deprecation.
- Cross-repo ADRs (rare) are prefixed with the organ: `META-ADR-001`.
- File naming: `docs/adr/adr-NNN-{slug}.md` (e.g., `adr-001-consensus-mechanism.md`).

---

## 6. Directory Structure

```
docs/adr/
  README.md          → Index of all ADRs with status
  adr-001-{slug}.md
  adr-002-{slug}.md
  ...
```

The `README.md` in `docs/adr/` is an index table:

```markdown
# Architecture Decision Records

| # | Title | Status | Date |
|---|-------|--------|------|
| 001 | {title} | Accepted | YYYY-MM-DD |
| 002 | {title} | Proposed | YYYY-MM-DD |
```

---

## 7. When to Write an ADR

### Always write an ADR for:
- Database selection (SQL vs NoSQL, provider choice)
- API protocol choice (REST vs GraphQL vs gRPC)
- Authentication/authorization strategy
- Hosting/deployment platform selection
- Major dependency additions (frameworks, ORMs, state management)
- Data model changes that affect multiple modules
- Breaking changes to public APIs

### Never write an ADR for:
- Formatting preferences (covered by linter config)
- Internal implementation details that don't affect interfaces
- Bug fixes (use commit messages)
- Documentation changes

---

## 8. Output Artifacts

- ADR document in `docs/adr/`
- Updated ADR index (README.md)
- If superseding: updated status on the previous ADR

---

## 9. Verification

- [ ] ADR follows the standard format (Context, Decision, Consequences, Alternatives)
- [ ] ADR has a valid status (Proposed, Accepted, Deprecated, Superseded)
- [ ] ADR is numbered sequentially (no gaps, no reuse)
- [ ] ADR index in README.md is updated
- [ ] Superseded ADRs reference their successor
- [ ] At least one alternative was considered and documented

---

## 10. Starter Research Questions

- What forces (technical, business, team) are driving this decision?
- What is the blast radius if this decision is wrong?
- How reversible is this decision? (Irreversible decisions need more scrutiny.)
- What would need to change for us to revisit this decision?
- Are there precedent ADRs in sibling repos that should be referenced?

---

*Version: 1.0.0 | System-Wide Directive | ORGANVM*
