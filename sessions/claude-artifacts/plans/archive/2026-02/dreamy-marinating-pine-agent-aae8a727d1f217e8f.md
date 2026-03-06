# orchestration-start-here Exploration Plan

## Objective
Thoroughly explore the orchestration-start-here/ submodule to understand governance, registry state, promotion pipeline, and overall system health. This is for strategic planning of ORGANVM IV.

## Investigation Areas (10 focus points)

### 1. Current state of registry.json
- [ ] Determine repo count (should be ~100-101)
- [ ] Check data completeness (all fields populated?)
- [ ] Assess last update timestamp
- [ ] Note any missing repos or placeholder entries

### 2. governance-rules.json status
- [ ] Review all 6 articles
- [ ] Identify what's fully codified vs TODO/aspirational
- [ ] Check for validation enforcement

### 3. validate-deps.py functionality
- [ ] Understand validation scope
- [ ] Check what rules it enforces
- [ ] Review test coverage
- [ ] Assess maturity/robustness

### 4. Promotion pipeline
- [ ] Identify what automation exists
- [ ] Check state machine implementation
- [ ] Review promotion recommender
- [ ] Assess manual vs automated workflows

### 5. CI workflows in .github/workflows/
- [ ] List all defined workflows
- [ ] Check validation coverage
- [ ] Review scheduling
- [ ] Note any gaps or failures

### 6. seed.yaml contracts
- [ ] Review schema version
- [ ] Check adoption rate across repos
- [ ] Assess schema completeness
- [ ] Note deprecations or TODOs

### 7. README documentation
- [ ] Identify documented content
- [ ] Note aspirational/planned features
- [ ] Check for outdated sections
- [ ] Assess accuracy of examples

### 8. TODOs, FIXMEs, roadmap
- [ ] Find all TODO/FIXME comments
- [ ] Check for roadmap files
- [ ] Assess prioritization
- [ ] Note timeline/ownership

### 9. organ-audit.py and calculate-metrics.py
- [ ] Understand actual functionality
- [ ] Check implementation completeness
- [ ] Review outputs/reports
- [ ] Assess metrics coverage

### 10. Overall DONE vs PLANNED vs MISSING
- [ ] Synthesize findings
- [ ] Identify core vs aspirational
- [ ] Note critical gaps
- [ ] Assess system health

## Key Files to Examine
- registry.json
- governance-rules.json
- scripts/validate-deps.py
- scripts/organ-audit.py
- scripts/calculate-metrics.py
- README.md
- docs/seed-schema/seed-schema-v1.yaml
- .github/workflows/
- audit-report.md
- Git history (recent commits)

## Status
- [ ] Registry analysis
- [ ] Governance review
- [ ] Scripts functionality
- [ ] Promotion pipeline assessment
- [ ] CI workflows mapping
- [ ] seed.yaml audit
- [ ] Documentation review
- [ ] TODOs/roadmap discovery
- [ ] Metrics analysis
- [ ] Final synthesis
