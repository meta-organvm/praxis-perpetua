# Application Tracking System - Discovery & Planning

**Date**: 2026-02-23  
**Status**: Planning Phase  
**Plan ID**: linked-bouncing-ocean-agent-a4b8df4c69552c269

## Executive Summary

Comprehensive search across `/Users/4jp/Workspace/` revealed **no existing dedicated application tracking system**. This document outlines findings and potential implementation approaches for building an application/job submission management system within the ORGANVM ecosystem.

## Phase 1: Discovery Results

### Search Scope
- **Breadth**: Top-level workspace directories (max 3 levels deep)
- **Patterns Searched**: "applications", "submissions", "tracking", "pipeline", "funnel"
- **File Types**: YAML, JSON, CSV, Markdown, Python
- **Key Directories Reviewed**:
  - `/Users/4jp/Workspace/organvm-i-theoria/`
  - `/Users/4jp/Workspace/organvm-ii-poiesis/`
  - `/Users/4jp/Workspace/organvm-iii-ergon/`
  - `/Users/4jp/Workspace/organvm-iv-taxis/`
  - `/Users/4jp/Workspace/organvm-v-logos/`
  - `/Users/4jp/Workspace/organvm-vii-kerygma/`
  - `/Users/4jp/Workspace/4444J99/`
  - `/Users/4jp/Workspace/intake/`

### Key Findings

#### No Existing Application Tracking System
- No seed.yaml files reference "applications", "submissions", or "career"
- No dedicated application database or tracking CSV/JSON files found
- No existing application pipeline infrastructure

#### Related Infrastructure Found
- **Kerygma Pipeline** (`organvm-vii-kerygma/kerygma_pipeline/`): Distribution pipeline for content, not applications
- **4444J99 Personal Workspace**: Portfolio and personal project directory structure exists, but no application tracking repos identified
- **intake/ Directory**: World registry and organizational material, but no job/application related content

## Phase 2: Architectural Considerations

### Where Should Application Tracking Live?

#### Option A: ORGAN-III (Ergon - Commercial/Professional)
**Rationale**: Application tracking is job-search/career management - fits commercial/professional product domain
- **Pros**: Aligned with commercial product focus; could be productized as SaaS tool
- **Cons**: May be overkill if purely personal use

#### Option B: ORGAN-IV (Taxis - Orchestration/Agents)
**Rationale**: Application tracking is a workflow orchestration problem - stages, validations, pipeline
- **Pros**: Aligns with orchestration domain; can leverage AI agent infrastructure
- **Cons**: ORGAN-IV is governance-focused, not product-focused

#### Option C: 4444J99 (Personal/Portfolio)
**Rationale**: If personal application tracking/career management
- **Pros**: Clear ownership; portfolio-aligned
- **Cons**: Won't scale if needs to be shared/team-based

#### Option D: New ORGAN-V integration (Logos - Discourse)
**Rationale**: If application tracking includes analytics/reporting on personal career narrative
- **Pros**: Fits public discourse/analytics focus of ORGAN-V
- **Cons**: Misses core functionality in wrong organ

### Recommended Path: ORGAN-III (Ergon)

**Rationale**: 
1. Application tracking is a professional/career workflow tool
2. ORGAN-III focuses on commercial products and developer utilities
3. Can be designed as either:
   - Personal tool (1-person CLI/web interface)
   - Productizable SaaS (multi-user, template library)
4. Fits unidirectional dependency model (I → II → III)

### Data Model Considerations

**Core Entities**:
- Application/Submission record
- Organization/Company metadata
- Position details
- Timeline events (applied, responded, interviewed, rejected, offered, etc.)
- Attachments (cover letter, resume version, etc.)
- Notes/follow-ups
- Tags (industry, location, salary range, etc.)

**Storage Options**:
- **Local-first**: SQLite for personal use, Postgres for team use
- **Format**: YAML/JSON for portability, database for querying
- **Integration**: Potential integration with ORGAN-IV agents for pipeline automation

## Phase 3: Next Steps (Pending User Confirmation)

### Decision Required
User should specify:

1. **Scope**: Personal tool vs. productizable system?
2. **Primary Use**: Self-directed job search, agent-assisted applications, analytics?
3. **Integration Level**: Standalone tool or integrated with ORGANVM orchestration?
4. **Platform**: CLI-only, web UI, both?
5. **Org Location**: ORGAN-III repo, 4444J99 repo, or new location?

### Implementation Options (Conditional on Decisions)

**If ORGAN-III + Self-Directed**:
```
organvm-iii-ergon/
  application-tracker/
    seed.yaml              # Org membership, tier, edges
    src/                   # Python implementation
    data/                  # SQLite/CSV data
    cli/                   # CLI interface
    tests/                 # Test suite
```

**If ORGAN-III + AI-Assisted**:
```
organvm-iii-ergon/
  application-conductor/   # AI-assisted application pipeline
    seed.yaml
    src/
    agents/                # Agent definitions
    templates/             # Application templates
    tests/
```

**If 4444J99 + Personal**:
```
4444J99/
  application-tracker/
    README.md
    data.yaml / data.json / data.sqlite
    scripts/               # CLI/utilities
```

## Files to Review Before Implementation

- `organvm-iii-ergon/CLAUDE.md` - ORGAN-III guidelines
- Existing ORGAN-III repos for architecture patterns
- `meta-organvm/organvm-corpvs-testamentvm/registry-v2.json` - Repo registry format
- Sample `seed.yaml` from existing repo

## Current Blockers
- Awaiting user decision on scope, integration level, and organizational location
- No implementation has begun pending clarification

---

**Plan Status**: ⏳ Awaiting User Input  
**Next Action**: User decision on architectural approach and integration level
