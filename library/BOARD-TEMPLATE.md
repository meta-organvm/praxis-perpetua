# System Library — Project Board Template

Reusable template for tracking library component maturation. Each directory/chain/vocabulary item becomes a trackable issue.

## Issue Template

```markdown
## [LIB-{NNN}] {Component Name}

**Type:** chain | vocabulary | canon | plan-catalog | engine-wiring | mcp-tool
**Location:** `library/{path}`
**Lifecycle:** observed → absorbed → fortified → placed → chained
**Current:** {lifecycle_state}

### What It Is
{one paragraph}

### Acceptance Criteria
- [ ] File exists at canonical location
- [ ] YAML validates (no parse errors)
- [ ] Recognition criteria tested against 3+ real prompts
- [ ] Behavior directives actionable (not vague)
- [ ] INDEX.md updated
- [ ] Consumed by at least 1 downstream system (context sync, MCP, or agent memory)

### Dependencies
- Upstream: {what feeds this component}
- Downstream: {what consumes this component}
```

## Board Columns

| Column | Meaning | Entry Criteria |
|--------|---------|---------------|
| Observed | File exists, content extracted from memory | YAML file committed |
| Absorbed | Tested against real sessions, invariants confirmed | 3+ session validations |
| Fortified | Edge cases handled, recognition criteria hardened | Adversarial review pass |
| Placed | Correct scope assigned, INDEX updated | Scope verified |
| Chained | Wired to upstream triggers + downstream consumers | Context sync + MCP live |
