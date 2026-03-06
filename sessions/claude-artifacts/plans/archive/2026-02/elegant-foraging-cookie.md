# Plan: Implement GitHub Repository Standards

## Context

Two skills define standards for this repo: `github-repo-curator` (portfolio
curation, README quality, license, badges, documentation) and
`github-repository-standards` (Minimal Root philosophy, World-Class README
anatomy, community health file placement, config centralization).

This repo already follows many of these standards well — community health files
are properly symlinked, `.config/` centralization is established, the README has
badges/Quick Start/Mermaid diagram. The work here closes the remaining gaps.

## Current State (Audit Summary)

### Already Compliant
- Community health files (CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT) —
  symlinked from root to `docs/governance/`
- CHANGELOG.md — symlinked to `docs/CHANGELOG.md`
- CLAUDE.md — symlinked to `.ai/CLAUDE.md`
- `.config/` centralization — 46+ config files properly centralized
- `.pre-commit-config.yaml` — symlink to `.config/pre-commit.yaml`
- `.devcontainer` — symlink to `.config/devcontainer`
- LICENSE — present in root (MIT)
- CODEOWNERS — in `.github/`
- FUNDING.yml — in `.github/`
- Issue templates — 18 templates in `.github/ISSUE_TEMPLATE/`
- PR template — in `.github/PULL_REQUEST_TEMPLATE.md`
- profile/README.md — org profile page exists
- Build artifacts (.coverage, coverage.xml, .DS_Store) — already in `.gitignore`
- Badges — consistent `flat-square` styling
- Quick Start — 4 copy-paste commands
- Mermaid diagram — architecture overview present

### Gaps to Fix

| # | Gap | Severity | Source Skill |
|---|-----|----------|--------------|
| 1 | `.gitattributes` missing from root — exists at `.config/gitattributes` but no symlink | High | repository-standards |
| 2 | `.lycheeignore` is a regular file in root — should follow `.config/` + symlink pattern | Medium | repository-standards |
| 3 | README missing "Why?" / value proposition section | Medium | both skills |
| 4 | README missing Table of Contents | Low | both skills |
| 5 | README missing "Acknowledgments" in footer | Low | repo-curator |
| 6 | README Mermaid diagram has no alt text | Low | repository-standards |
| 7 | README badges missing coverage and version badges | Low | repo-curator |

## Implementation

### 1. Create `.gitattributes` symlink in root

Git requires `.gitattributes` in root to apply line-ending rules. The file
already exists at `.config/gitattributes` but has no root symlink, so its rules
are currently **not being applied**.

```bash
cd /Users/4jp/Workspace/ivviiviivvi/.github
ln -s .config/gitattributes .gitattributes
```

**File**: New symlink `.gitattributes` → `.config/gitattributes`

### 2. Relocate `.lycheeignore` to `.config/` with symlink

Follows the established pattern (`.pre-commit-config.yaml`, `.devcontainer`,
`.vscode` all symlink into `.config/`). Lychee auto-discovers `.lycheeignore`
from the repo root, so the symlink preserves functionality.

```bash
mv .lycheeignore .config/.lycheeignore
ln -s .config/.lycheeignore .lycheeignore
```

**Files**: `.lycheeignore` (becomes symlink), `.config/.lycheeignore` (new
location)

### 3. Enhance README.md

Apply World-Class README standards to the existing README. Changes:

**a) Add "Why?" value proposition section** (after the intro paragraph, before
the `<!-- UPDATE_COUNTS -->` comment):

```markdown
## Why This Repository?

Managing organization-wide standards across dozens of repositories is tedious
and error-prone. This `.github` repo solves that by providing a single source of
truth — workflows, templates, governance docs, and AI configurations that every
org repo inherits automatically. Change it once here, and every repository
benefits.
```

**b) Add Table of Contents** (after the `</div>` closing tag, before the intro
paragraph):

```markdown
## Contents

- [Why This Repository?](#why-this-repository)
- [Quick Start](#quick-start)
- [Workflows](#workflows)
- [AI Framework](#ai-framework)
- [Organization Governance](#organization-governance)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Security](#security)
- [License](#license)
```

**c) Add alt text to Mermaid diagram** — Mermaid blocks in GitHub markdown don't
support HTML alt text directly, but we can add an accessible description before
the diagram:

Add a visually-hidden accessible description:
```markdown
<!-- Accessible description: Architecture diagram showing the .github repository
providing Community Health files, Workflows, and AI Framework to all org repos -->
```

**d) Add Acknowledgments to footer** (before `## License`):

```markdown
## Acknowledgments

- GitHub Copilot customizations adapted from
  [github/awesome-copilot](https://github.com/github/awesome-copilot)
- Workflow SHA-pinning via [ratchet](https://github.com/sethvargo/ratchet)
```

**e) Add coverage and version badges** to the badge dashboard (after CI badge):

```markdown
[![Coverage](https://img.shields.io/badge/coverage-58%25-yellow?style=flat-square)](pyproject.toml)
[![Version](https://img.shields.io/badge/version-1.0.0-blue?style=flat-square)](pyproject.toml)
```

**File**: `README.md`

## Files to Modify

| # | File | Action |
|---|------|--------|
| 1 | `.gitattributes` | Create symlink → `.config/gitattributes` |
| 2 | `.lycheeignore` | Move to `.config/.lycheeignore`, create symlink |
| 3 | `README.md` | Add TOC, "Why?" section, acknowledgments, badges, alt text |

## Verification

1. `ls -la .gitattributes` — should show symlink to `.config/gitattributes`
2. `ls -la .lycheeignore` — should show symlink to `.config/.lycheeignore`
3. `cat .gitattributes | head -3` — should show content (confirms symlink works)
4. `cat .lycheeignore | head -3` — should show content (confirms symlink works)
5. Read `README.md` — verify TOC, "Why?" section, acknowledgments, badges present
6. `grep -c 'agentsphere.example.com' README.md` — should be 0
7. Root item count: `ls -1a | wc -l` — should remain at 41 (net +1 for .gitattributes, no change for lycheeignore)
