# SOP: Markdown Hygiene and Linting

## 1. Document Metadata

**Document Title**: Markdown Hygiene and Linting Enforcement
**Document Identifier**: SOP-MD-HYG-001
**Specification Layer**: Foundational System Governance
**Status**: ACTIVE
**Purpose**: To enforce structural reliability, semantic consistency, and deterministic parsing of all Markdown documents generated or persisted within the ORGANVM ecosystem.

## 2. Theoretical Basis

The repository contains numerous documents extracted from chat transcripts, agent loops, and manual sessions. Inconsistencies like missing code fences, pseudo-headers, and duplicate titles cause AST (Abstract Syntax Tree) parsing issues downstream and generate high volumes of linting technical debt. 

This SOP standardizes the creation rules for any text/markdown file, enforcing that formatting strictly conforms to standard parser assumptions so information can be reliably queried, extracted, and transcluded by automated systems.

## 3. Core Mandates

All agentic output and human additions must conform to the following rules:

### 3.1. Single `H1` Rule (MD025)
Every Markdown file must contain **exactly one** top-level `H1` heading (`# Heading`). This forms the document title. Subsequent top-level sections must use `H2` (`## Heading`) or lower. 
**Prohibited**: Using multiple `#` headers as standalone section dividers.

### 3.2. Prohibition of Emphasis Headers (MD036)
**Never** use bolding (`**Section Title**`) as a structural substitute for a real header. If it acts as a heading, it must use the proper header level (e.g., `### Section Title`). AST parsers cannot read bold text as section dividers.

### 3.3. Incremental Hierarchy (MD001)
Headings must progress sequentially. Do not jump from an `H1` (`#`) directly to an `H3` (`###`). If subsections exist, they must be nested logically.

### 3.4. Language Definition in Fences (MD040)
Every fenced code block (` ``` `) must specify a language identifier for syntax tooling and parsing accuracy. 
- General text logs or transcripts should use `text` or `markdown`.
- Code must use matching language tags (`python`, `yaml`, `json`, `bash`, etc.).

### 3.5. Universal Empty Lines & Space Cleansing (MD041, MD009, MD047)
- **First Line**: The first line defaults to the `H1` Document Title, unless preceded by Jekyll-style YAML frontmatter.
- **Trailing Spaces**: Avoid trailing whitespace at the end of lines, as it triggers parser warnings and adds git noise.
- **File Terminus**: All `.md` files must end with exactly one blank trailing newline.

## 4. Remediation

If an agent encounters legacy files heavily violating these mandates, the agent should ideally execute remediation logic on the document before proceeding with downstream data-extraction or modification tasks.
