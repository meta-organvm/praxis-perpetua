# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

## What This Is

A **docs-only process governance corpus**. No code, no build system, no runtime. Contains SOPs, research standards, session review logs, derived principles, and continuous improvement templates.

**Organ:** META-ORGANVM | **Tier:** standard | **Status:** CANDIDATE

## Key Rules

- **Session logs are append-only.** Never overwrite a dated session file in `sessions/`. Create a new dated file instead.
- **Derived principles are a living document.** Update `lessons/derived-principles.md` when new patterns emerge. Do not duplicate existing entries — refine them.
- **Standards follow ORGANVM versioning.** Never overwrite a standard in `standards/`. Create a new version (`-v2.md`, `-v3.md`) and move the old one to `archive/YYYY-MM/`.
- **Templates are reusable scaffolds.** Files in `templates/` are not instances — they are copied to `sessions/` or used as checklists during reviews.

## Directory Layout

```
standards/     Governing METADOCs and SOPs
templates/     Reusable review scaffolds
sessions/      Dated session logs (YYYY-MM-DD--description.md)
lessons/       Extracted principles and risk profiles
archive/       Superseded standards
```

## Working Here

- No `pytest`, no `ruff`, no build commands. CI validates markdown structure only.
- Cross-references to other repos use relative paths from the workspace root (e.g., `meta-organvm/organvm-corpvs-testamentvm/registry-v2.json`).
- The founding session log (`sessions/2026-03-06--gemini-styx-research.md`) documents the beta run that motivated this repo's creation.

## Relationship to Other Subprojects

- **organvm-corpvs-testamentvm**: System-state governance (registry, metrics, planning). This repo: process governance (how we work).
- **organvm-engine**: Provides CLI and automation. This repo: provides the human-readable standards that the engine enforces.
