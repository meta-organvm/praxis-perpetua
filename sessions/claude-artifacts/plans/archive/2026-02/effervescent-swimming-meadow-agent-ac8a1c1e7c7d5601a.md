# Meta-Organvm Thorough Exploration Plan

## Objective
Conduct a very thorough exploration of meta-organvm submodules focusing on:
1. Standalone scripts (organvm-corpvs-testamentvm/scripts/) - code quality, duplication, error handling
2. Schema definitions - currency and completeness vs actual data structures
3. System dashboard - code quality and architectural patterns
4. MCP server - tool implementations, error handling, test coverage
5. Alchemia ingestvm - implementation status and quality
6. Cross-cutting concerns - code duplication between scripts and engine modules

## Current Progress
- ✅ Initial discovery: identified 34 Python scripts in organvm-corpvs-testamentvm/scripts/
- ⏳ NEXT: Detailed analysis of scripts with duplication focus

## Phase 1: Standalone Scripts Analysis
- [ ] Read calculate-metrics.py and compare with organvm-engine/metrics/calculator.py
- [ ] Read propagate-metrics.py and compare with organvm-engine/metrics/propagator.py
- [ ] Read generate-claude-md.py and compare with organvm-engine/contextmd/generator.py
- [ ] Analyze remaining 31 scripts for code quality, error handling, documentation
- [ ] Document all duplication patterns with file paths and line numbers

## Phase 2: Schema Definitions
- [ ] Review all JSON schema files in schema-definitions/schemas/
- [ ] Compare schema definitions with actual registry-v2.json structure
- [ ] Check schema-definitions/scripts/validate.py implementation
- [ ] Identify missing or outdated schema definitions

## Phase 3: System Dashboard
- [ ] Examine code architecture in system-dashboard/src/dashboard/
- [ ] Assess route implementations and templates
- [ ] Check error handling and logging patterns
- [ ] Review dependency usage (FastAPI, Jinja2, HTMX)

## Phase 4: MCP Server
- [ ] Review organvm-mcp-server/src/organvm_mcp/server.py dispatch table
- [ ] Analyze all 16 tool implementations
- [ ] Check error handling and response formatting
- [ ] Review test coverage in organvm-mcp-server/tests/

## Phase 5: Alchemia Ingestvm
- [ ] Examine alchemia-ingestvm/src/alchemia/ structure
- [ ] Assess implementation status vs seed.yaml
- [ ] Check integration with organvm-engine

## Phase 6: Synthesis & Recommendations
- [ ] Document all findings with specific file paths and line numbers
- [ ] Create detailed duplication report with refactoring recommendations
- [ ] Assess overall code quality across submodules
- [ ] Prioritize issues and improvements

## Output
Detailed written findings with:
- Code quality assessment per submodule
- Duplication patterns with specific locations
- Architecture observations
- Recommended improvements (ordered by priority)
