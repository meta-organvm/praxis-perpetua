# Naming Convention Specification: The Double-Hyphen Convention

**Date:** 2026-03-21
**Status:** ENACTED
**Source:** Implementation Manifest P0-05 (RP-04 SS5.1 Principle 6; SYN-03 SS6.4; RP-02 SS4.5 Implication 2)
**Theoretical Basis:** RP-04 — The Philosophy of Naming in Software Systems; SYN-03 — Naming as Governance Infrastructure
**Scope:** All repository names across all organs; promotion naming patterns; organ-level naming

---

## The Convention

ORGANVM uses a structured naming convention that encodes semantic relationships into repository names. The convention has two tiers:

1. **Single hyphen** (`-`) separates words within a single concept
2. **Double hyphen** (`--`) separates two distinct functional concepts: the *function* from the *descriptor*

The double-hyphen is not decorative. It is a syntactic category marker that tells both humans and machines: "the string before `--` names what this thing does; the string after `--` names what it is about."

---

## Formal Rules

### Rule 1: Word Separation (Single Hyphen)

Within a concept, words are separated by single hyphens. This follows standard kebab-case convention.

```
recursive-engine          (two words, one concept)
auto-revision             (two words, one concept)
public-record             (two words, one concept)
```

### Rule 2: Concept Separation (Double Hyphen)

When a repository name encodes two distinct concepts — typically function and descriptor — they are separated by exactly one double-hyphen (`--`).

```
recursive-engine--generative-entity
  ├── function:    recursive-engine
  └── descriptor:  generative-entity

sema-metra--alchemica-mundi
  ├── function:    sema-metra
  └── descriptor:  alchemica-mundi

vigiles-aeternae--corpus-mythicum
  ├── function:    vigiles-aeternae
  └── descriptor:  corpus-mythicum
```

### Rule 3: At Most One Double-Hyphen

A repository name contains at most one `--` separator. Multiple `--` separators create ambiguity about which concepts are being separated.

**Valid:** `recursive-engine--generative-entity`
**Invalid:** `recursive-engine--generative--entity` (three concepts? two? ambiguous)

### Rule 4: Non-Empty Segments

Both the function and descriptor segments must be non-empty. A name cannot begin or end with `--`, and `--` cannot appear adjacent to another `--`.

**Valid:** `art-from--auto-revision-epistemic-engine`
**Invalid:** `--generative-entity` (empty function)
**Invalid:** `recursive-engine--` (empty descriptor)

### Rule 5: Valid Word Characters

Each word within a segment consists of lowercase alphanumeric characters. Segments follow kebab-case: `[a-z0-9]+(-[a-z0-9]+)*`. Special characters, underscores, and uppercase letters are not permitted in repository names.

**Exception:** The `.github` repository in each organ uses GitHub's required naming and is exempt from this convention.

### Rule 6: Latin/Greek Preference for Organ-Level Naming

Organ-level names (organ directories, flagship repos, constitutional artifacts) prefer Latin or Greek roots to signal permanence and theoretical grounding. This is a preference, not a hard constraint. Product-level names (ORGAN-III) use English for user-facing clarity.

**Organ-level (Latin/Greek preferred):**
- `organvm-i-theoria`, `organvm-ii-poiesis`, `organvm-iii-ergon`
- `praxis-perpetua`, `organvm-corpvs-testamentvm`
- `sema-metra--alchemica-mundi`, `vigiles-aeternae--corpus-mythicum`
- `studium-generale`, `hierarchia-mundi`

**Product-level (English expected):**
- `public-record-data-scrapper`, `tab-bookmark-manager`
- `search-local--happy-hour`, `fetch-familiar-friends`

---

## Promotion Naming Patterns

When repositories are promoted across organs, the naming follows documented patterns from `governance-rules.json`:

| Promotion | Pattern | Example |
|-----------|---------|---------|
| ORGAN-I to ORGAN-II | `art-from--{source_repo_name}` | `art-from--auto-revision-epistemic-engine` |
| ORGAN-II to ORGAN-III | `{source_repo_name}` (unchanged) | (direct transfer) |
| Any to ORGAN-V | `essay-from--{source_repo_name}` | `essay-from--recursive-engine` |

These patterns use the double-hyphen convention: the function prefix (`art-from`, `essay-from`) is separated from the source descriptor by `--`.

---

## Validation Regex Patterns

### Pattern 1: Simple Name (no double-hyphen)

Names that consist of a single concept with no function/descriptor separation.

```regex
^[a-z0-9]+(-[a-z0-9]+)*$
```

**Matches:** `core-engine`, `metasystem-master`, `docs`, `praxis-perpetua`
**Does not match:** `Core-Engine`, `core_engine`, `core--engine` (use Pattern 2 for double-hyphen)

### Pattern 2: Double-Hyphen Name (function--descriptor)

Names that encode two distinct concepts separated by `--`.

```regex
^[a-z0-9]+(-[a-z0-9]+)*--[a-z0-9]+(-[a-z0-9]+)*$
```

**Matches:** `recursive-engine--generative-entity`, `art-from--auto-revision-epistemic-engine`
**Does not match:** `recursive-engine---generative-entity` (triple hyphen), `Recursive-Engine--Entity` (uppercase)

### Pattern 3: Combined (any valid repository name)

Accepts either a simple name or a double-hyphen name.

```regex
^[a-z0-9]+(-[a-z0-9]+)*(--[a-z0-9]+(-[a-z0-9]+)*)?$
```

### Pattern 4: Exempt Names

The following patterns are exempt from validation:

```regex
^\.github$
```

The `.github` directory is required by GitHub for org-level community health files and does not follow the naming convention.

---

## Classification of Existing Repository Names

### Compliant: Double-Hyphen Names (function--descriptor)

These names correctly use `--` to separate function from descriptor.

| Organ | Repository | Function | Descriptor |
|-------|-----------|----------|------------|
| I | `recursive-engine--generative-entity` | recursive-engine | generative-entity |
| I | `organon-noumenon--ontogenetic-morphe` | organon-noumenon | ontogenetic-morphe |
| I | `call-function--ontological` | call-function | ontological |
| I | `sema-metra--alchemica-mundi` | sema-metra | alchemica-mundi |
| I | `nexus--babel-alexandria` | nexus | babel-alexandria |
| I | `meta-source--ledger-output` | meta-source | ledger-output |
| I | `vigiles-aeternae--corpus-mythicum` | vigiles-aeternae | corpus-mythicum |
| II | `art-from--auto-revision-epistemic-engine` | art-from | auto-revision-epistemic-engine |
| II | `art-from--narratological-algorithmic-lenses` | art-from | narratological-algorithmic-lenses |
| II | `a-i-council--coliseum` | a-i-council | coliseum |
| III | `sovereign-ecosystem--real-estate-luxury` | sovereign-ecosystem | real-estate-luxury |
| III | `multi-camera--livestream--framework` | multi-camera | livestream--framework |
| III | `universal-mail--automation` | universal-mail | automation |
| III | `a-i-chat--exporter` | a-i-chat | exporter |
| III | `peer-audited--behavioral-blockchain` | peer-audited | behavioral-blockchain |
| IV | `agent--claude-smith` | agent | claude-smith |
| IV | `a-i--skills` | a-i | skills |
| META | `vigiles-aeternae--agon-cosmogonicum` | vigiles-aeternae | agon-cosmogonicum |

### Compliant: Simple Names (no double-hyphen needed)

These names are single concepts that do not require the `--` separator.

| Organ | Repository |
|-------|-----------|
| I | `auto-revision-epistemic-engine`, `narratological-algorithmic-lenses`, `cognitive-archaelogy-tribunal`, `a-recursive-root`, `radix-recursiva-solve-coagula-redi`, `linguistic-atomization-framework`, `my-knowledge-base`, `scalable-lore-expert`, `hierarchia-mundi`, `styx-behavioral-economics-theory`, `studium-generale` |
| II | `core-engine`, `performance-sdk`, `example-generative-music`, `metasystem-master`, `example-choreographic-interface`, `showcase-portfolio`, `archive-past-works`, `case-studies-methodology`, `learning-resources`, `example-generative-visual`, `example-interactive-installation`, `example-ai-collaboration`, `docs`, `a-mavs-olevm`, `artist-toolkit-and-templates`, `client-sdk`, `academic-publication`, `example-theatre-dialogue`, `audio-synthesis-bridge`, `life-betterment-simulation`, `universal-waveform-explorer`, `shared-remembrance-gateway`, `chthon-oneiros`, `krypto-velamen`, `alchemical-synthesizer`, `styx-behavioral-art` |
| III | `classroom-rpg-aetheria`, `gamified-coach-interface`, `trade-perpetual-future`, `fetch-familiar-friends`, `public-record-data-scrapper`, `mirror-mirror`, `the-invisible-ledger`, `enterprise-plugin`, `virgil-training-overlay`, `tab-bookmark-manager`, `the-actual-news`, `your-fit-tailored`, `my-block-warfare`, `card-trade-social`, `hokage-chess`, `anon-hookup-now`, `render-second-amendment`, `styx-behavioral-commerce` |
| IV | `orchestration-start-here`, `petasum-super-petasum`, `universal-node-network`, `agentic-titan`, `tool-interaction-design`, `system-governance-framework`, `reverse-engine-recursive-run`, `collective-persona-operations` |
| V | `public-process` |
| VI | `koinonia-db`, `community-hub`, `salon-archive`, `reading-group-curriculum`, `adaptive-personal-syllabus` |
| VII | `announcement-templates`, `social-automation`, `distribution-strategy` |
| META | `organvm-corpvs-testamentvm`, `alchemia-ingestvm`, `schema-definitions`, `organvm-engine`, `system-dashboard`, `organvm-mcp-server`, `praxis-perpetua`, `stakeholder-portal`, `materia-collider`, `organvm-ontologia` |

### Non-Compliant: Naming Violations

| Organ | Repository | Violation | Suggested Resolution |
|-------|-----------|-----------|---------------------|
| I | `4-ivi374-F0Rivi4` | Uppercase characters (`F`), numeric-heavy opaque name | Legacy/personal name; candidate for rename or archival note |
| I | `cog-init-1-0-` | Trailing hyphen | Legacy name; trailing hyphen violates word-boundary rule |
| II | `ivi374ivi027-05` | Numeric-heavy opaque name, no semantic content | Legacy/personal name; candidate for rename or archival note |
| III | `search-local--happy-hour` | **Compliant** (function: search-local, descriptor: happy-hour) | N/A |
| III | `life-my--midst--in` | Multiple `--` separators (Rule 3 violation) | Clarify intended function/descriptor or rename |
| III | `my--father-mother` | `my` as function segment is semantically empty | Consider whether the `--` is intentional or a typo |
| III | `select-or-left-or-right-or` | Trailing `or` reads as truncated; semantically unclear | Cosmetic concern, syntactically valid |
| III | `commerce--meta` | `--` separates "commerce" from "meta" but "meta" is ambiguous (organ name overlap) | Consider renaming to avoid confusion with META-ORGANVM organ |
| III | `multi-camera--livestream--framework` | Multiple `--` separators (Rule 3 violation) | Restructure: `multi-camera-livestream--framework` or `multi-camera--livestream-framework` |

### Exempt: Platform-Required Names

| Organ | Repository | Exemption Reason |
|-------|-----------|-----------------|
| All | `.github` | GitHub platform requirement for org-level community health files |

---

## Validator Specification

### Input

The validator accepts a repository name (string) and returns a structured verdict.

### Verdict Structure

```yaml
name: "recursive-engine--generative-entity"
valid: true
pattern: "double-hyphen"     # "simple" | "double-hyphen" | "exempt"
function: "recursive-engine"  # null for simple names
descriptor: "generative-entity"  # null for simple names
violations: []                # list of rule IDs violated
warnings: []                  # advisory notes (e.g., "Latin/Greek naming in product-level repo")
```

### Violation Codes

| Code | Rule | Description |
|------|------|-------------|
| `NC-01` | Rule 3 | Multiple `--` separators |
| `NC-02` | Rule 4 | Empty segment (leading/trailing `--`) |
| `NC-03` | Rule 5 | Invalid characters (uppercase, underscore, special characters) |
| `NC-04` | Rule 5 | Segment does not match kebab-case pattern |
| `NC-05` | Rule 3+4 | Triple or more consecutive hyphens (`---`) |

### Warning Codes

| Code | Description |
|------|-------------|
| `NW-01` | Latin/Greek name used in ORGAN-III (product-level); consider English for user clarity |
| `NW-02` | English name used in organ-level/constitutional artifact; consider Latin/Greek |
| `NW-03` | Name exceeds 50 characters; may cause display truncation in GitHub UI |
| `NW-04` | Function segment is a single character; may be too terse for clarity |
| `NW-05` | Name collides with organ/system reserved term (e.g., "meta", "organ", "system") |

---

## Integration Points

### CI Pipeline

The naming validator runs as a syntactic governance check (per `2026-03-21-syntactic-semantic-boundary.md`, naming pattern compliance is SYNTACTIC). It should be integrated into:

1. **Repository creation workflows** — validate before the repo is created
2. **Registry validation** (`organvm registry validate`) — validate all names in `registry-v2.json`
3. **Seed.yaml validation** — validate the repo name declared in `seed.yaml`

### Controlled Vocabulary (P0-06)

The naming validator works in conjunction with the controlled vocabulary registry (P0-06). The validator checks structural compliance (Rules 1-5); the controlled vocabulary checks semantic appropriateness (whether terms are used consistently across the system). These are complementary checks at different levels: syntactic and semantic.

### Naming Debt Tracking (P1-09)

The validator's output feeds into the naming debt tracker. Repos with violations are flagged as naming debt. The debt tracker monitors whether violations are resolved, deferred (with justification), or accepted as legacy exceptions.

---

## Legacy Exception Policy

Repositories that predate this specification and violate the naming convention are not required to rename immediately. Renaming a repository has cascading effects (git remotes, CI references, cross-repo links, registry entries). The policy is:

1. **Violations are recorded** in the naming debt tracker
2. **New repositories** must comply; no new violations are permitted
3. **Existing violations** are resolved opportunistically (e.g., during archival, major refactoring, or tier promotion)
4. **Permanent exceptions** may be granted for repos with external users who depend on the current name; these require documented justification

---

## Cross-References

- **RP-04:** The Philosophy of Naming in Software Systems (theoretical foundation)
- **SYN-03:** Naming as Governance Infrastructure (formal treatment)
- **P0-02:** `2026-03-21-syntactic-semantic-boundary.md` (naming is classified as SYNTACTIC)
- **P0-06:** Controlled vocabulary registry (semantic naming governance)
- **P1-08:** Namespace governance proportional to scale
- **P1-09:** Naming debt tracking and naming health metrics
- **P1-20:** Language-game specification for naming contexts
- **governance-rules.json:** Promotion naming patterns (`art-from--`, `essay-from--`)
- **docs/standards/10-repository-standards.md:** Repository standards (naming section)

---

*This specification governs the syntactic structure of names. It does not govern whether names are meaningful, accurate, or appropriate -- those are semantic properties assessed through human review and the controlled vocabulary (P0-06). The naming convention is enforceable by automation precisely because it is a syntactic property: pattern compliance is decidable.*
