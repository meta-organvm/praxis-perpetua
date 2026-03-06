# ORGAN-VII (Kerygma) Cross-Organ Integration Exploration Plan

**Date**: 2026-02-24  
**Session ID**: lucky-snuggling-mango-agent-a6f6508a5a6485b08  
**Status**: Plan Mode - READ-ONLY Investigation  
**Context**: Comprehensive exploration of external dependencies and integration points for ORGAN-VII (Kerygma) distribution pipeline

## Objective

Perform a thorough read-only investigation of ORGAN-VII's cross-organ dependencies and integration points within the ORGANVM eight-organ system. Map current implementation status, identify integration patterns, and document the complete dependency chain.

## Investigation Areas (6 Primary)

### 1. ORGAN-IV Registry Integration
**Location**: `/Users/4jp/Workspace/organvm-iv-taxis/orchestration-start-here/registry.json`

**Objectives**:
- Verify registry file exists and is accessible
- Examine registry structure and ORGAN-VII entries
- Identify template variable interpolation requirements
- Map dependency declarations and event subscriptions
- Check promotion state (expect GRADUATED based on CLAUDE.md)

**Expected Findings**:
- Template variables used by kerygma_pipeline.py
- ORGAN-VII repo references and metadata
- Event subscription configuration
- Registry entry format and versioning

### 2. ORGAN-V (public-process) RSS/Atom Feed
**Location**: `/Users/4jp/Workspace/organvm-v-logos/`

**Objectives**:
- Verify public-process repo exists and contains Jekyll site
- Locate Atom feed URL and structure
- Examine feed polling configuration in social-automation
- Check rss_poller.py implementation
- Verify feed entry parsing and event triggering

**Expected Findings**:
- Feed URL and endpoint structure
- Feed entry format (title, content, publish date, author, tags)
- Polling interval configuration
- Event transformation pipeline
- Any custom metadata or extensions

### 3. GitHub Actions Workflows Maturity
**Location**: `/Users/4jp/Workspace/organvm-vii-kerygma/.github/.github/workflows/`

**Workflows to Analyze**:
- `ci-pipeline.yml` - Package installation, test runs
- `dispatch-receiver.yml` - ORGAN-IV repository_dispatch handler
- `rss-auto-dispatch.yml` - Cron-based RSS polling (6h interval)
- `weekly-analytics.yml` - Analytics report generation
- `dispatch-log.yml` - Dispatch logging infrastructure
- `notify-kerygma.yml` - Cross-organ notification handler
- `quarterly-feedback.yml` - Feedback collection
- `quarterly-synthesis-dispatch.yml` - Quarterly synthesis broadcast

**Objectives**:
- Assess workflow trigger conditions and event handling
- Verify dispatch-receiver.yml payload structure and variable parsing
- Check rss-auto-dispatch.yml cron timing and polling logic
- Examine analytics collection and reporting flow
- Verify error handling and retry logic
- Map notification broadcast patterns
- Check seasonal workflow timing and dependencies

**Expected Findings**:
- Workflow trigger patterns (push, dispatch, cron, manual)
- Environment variable configuration
- Payload schema from ORGAN-IV
- Success/failure handling patterns
- Integration with kerygma_pipeline.py orchestrator

### 4. Meta-ORGANVM Registry
**Location**: `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/registry-v2.json`

**Objectives**:
- Verify registry-v2.json exists and is current
- Locate ORGAN-VII entries and validate metadata
- Check ORGAN-VII promotion state (expect GRADUATED)
- Verify cross-organ dependency declarations
- Examine repo seed entries for all 4 ORGAN-VII repos
- Map event subscription topology

**Expected Findings**:
- ORGAN-VII organ entry with metrics and status
- All 4 repo entries (announcement-templates, social-automation, distribution-strategy, .github)
- Current promotion states
- Event subscription subscriptions (ORGAN-IV dispatch, ORGAN-V feed)
- Cross-organ produce/consume edge declarations
- Last sync timestamp and versioning info

### 5. GitHub Issues & Project Boards
**Locations**: 
- GitHub issues across 4 ORGAN-VII repos
- Project board URLs if configured

**Objectives**:
- Identify open/in-progress issues in each repo
- Map roadmap items and feature planning
- Locate integration-related issues with other organs
- Check for cross-organ issue linking or tracking
- Verify issue templates and triage process
- Examine project board organization and priorities

**Expected Findings**:
- Integration issues between ORGAN-VII and ORGAN-IV/V
- Feature requests and enhancement backlog
- Known issues with platform APIs or resilience patterns
- Tech debt and refactoring priorities
- Issue linking patterns to other organs

### 6. Documentation & Operational Scripts
**Locations**:
- `.github/docs/` - Architecture Decision Records (ADRs)
- `.github/scripts/` - Operational utilities

**Objectives**:
- Review ADRs for POSSE architecture decisions
- Examine cross-organ workflow documentation
- Analyze deployment scripts and their cross-organ dependencies
- Check platform integration documentation (Mastodon, Discord, Bluesky, Ghost)
- Verify analytics and reporting documentation
- Examine config management and credential handling docs

**Expected Findings**:
- ADRs covering: POSSE pattern, resilience stack, dry-run model, template engine design, analytics strategy
- Operational procedures: deployment, platform credential rotation, feed polling setup, analytics review
- Cross-organ coordination workflows
- Integration setup guides for ORGAN-IV and ORGAN-V
- Error handling and incident response procedures

## Dependency Mapping Strategy

**Primary Dependency Chain**:
```
ORGAN-VII (Kerygma)
├── Consumes from ORGAN-IV (Orchestration)
│   ├── registry.json for template variables
│   └── repository_dispatch for event triggering
└── Consumes from ORGAN-V (Public Process)
    └── Atom feed for new essay detection
```

**Integration Points**:
1. **Event-Driven**: repository_dispatch from ORGAN-IV triggers distribution
2. **Feed-Driven**: RSS polling from ORGAN-V detects new content
3. **Registry-Driven**: Template variables resolved from ORGAN-IV registry
4. **Analytics-Driven**: Engagement metrics fed back to ORGAN-V/IV for optimization

## Execution Sequence

### Phase 1: Registry & Configuration (2 items)
1. Verify ORGAN-IV registry structure and ORGAN-VII entries
2. Review kerygma_config.yaml or example config for integration variables

### Phase 2: Event Sources (2 items)
3. Examine ORGAN-V public-process repo structure and feed
4. Analyze rss_poller.py and feed parsing logic

### Phase 3: Automation & Workflows (2 items)
5. Review all GitHub Actions workflows in `.github/.github/workflows/`
6. Map dispatch payload structure and variable interpolation

### Phase 4: Validation & Documentation (2 items)
7. Cross-reference entries in meta-organvm registry-v2.json
8. Review ADRs and operational scripts in `.github/docs/` and `.github/scripts/`

## Read-Only Verification Steps

For each investigation area:
- Verify file/directory exists without modification
- Read content to understand structure and integration
- Search for cross-references to other organs (ORGAN-IV, ORGAN-V, meta-organvm)
- Document findings with line numbers and key quotes
- Create summary of dependencies and integration patterns
- Flag any missing documentation or unclear integration points

## Expected Outcomes

1. **Dependency Map**: Visual representation of ORGAN-VII's integration with ORGAN-IV and ORGAN-V
2. **Integration Checklist**: Verification that all declared dependencies are actually implemented
3. **Documentation Audit**: Gaps or outdated information in ADRs, CLAUDE.md, or workflow docs
4. **Configuration Status**: Current config state, live_mode settings, credential management
5. **Workflow Analysis**: Maturity assessment of GitHub Actions automation
6. **Cross-Organ Patterns**: Identification of reusable integration patterns for other organs
7. **Risk Assessment**: Potential single points of failure or missing error handling

## Success Criteria

- All 6 investigation areas fully explored with evidence
- Complete dependency chain documented with file locations
- Integration points verified against actual code/config
- ADRs reviewed for architectural decisions
- No destructive actions taken (read-only verification only)
- Comprehensive summary report generated

## Notes

- This is a read-only investigation - no edits, configs, or commits
- All findings should reference specific file paths and line numbers
- Cross-references to ORGAN-IV and ORGAN-V should include their repo locations
- Platform-specific configurations (Mastodon, Discord, Bluesky, Ghost) should be documented as integration points
- Timeline: No immediate time constraints; thorough exploration prioritized
