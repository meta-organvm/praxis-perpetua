# Plan: Extract and Analyze Non-Liminal Repository Classifications

## Objective
Understand classification patterns established for repos NOT classified as "liminal_zone" to establish criteria framework for Phase 2 liminal repo classification.

## Expected Output
- ~49 repos across organ_i, organ_ii, organ_iii, organ_iv
- For each: repo_unit_id, org_unit_id, organ_id, realm_id
- Grouped by organ_id
- Analysis of repo types in each organ correlated with organ charter purposes

## Strategy

### Phase 1: Extract Non-Liminal Repos
- Use Grep tool to search topology_manifest.json for "organ_id" entries that are NOT "liminal_zone"
- Filter for organ_i, organ_ii, organ_iii, organ_iv only
- Extract: repo_unit_id, org_unit_id, organ_id, realm_id from each matching entry
- Organize results by organ grouping

### Phase 2: Cross-Reference with Organ Charter
- Use organ_charter_v0.md (already read, 200 lines) to document each organ's purpose
- Identify what types of repos belong in each organ based on established classification
- Document the conceptual, functional, and operational boundaries between organs

### Phase 3: Establish Classification Patterns
- Analyze repo metadata (names, paths, origins) in each organ grouping
- Identify common characteristics of repos in each organ
- Document criteria framework for Phase 2 liminal repo classification
- Establish decision tree or rubric for moving liminal repos into appropriate organs

## Files Reference
- Source: /Users/4jp/world/_registry/topology_manifest.json (75.5KB, requires Grep filtering)
- Reference: /Users/4jp/world/_registry/organ_charter_v0.md (fully read, available in context)

## Key Organ Purposes (from charter)
- **organ_i**: Conceptual structures - rules, grammars, ontologies, meaning-structures
- **organ_ii**: Art enactment - performances, scores, scripts, installations, temporal works
- **organ_iii**: Commerce & labor - services, tools, consulting, monetizable artifacts, deliverables
- **organ_iv**: Orchestration - governance, routing, flow control, system integrity

## Success Criteria
- All non-liminal repos identified and organized
- Clear correlation between repo types and organ purposes
- Reusable classification patterns documented for Phase 2
- No repos misclassified or overlooked
