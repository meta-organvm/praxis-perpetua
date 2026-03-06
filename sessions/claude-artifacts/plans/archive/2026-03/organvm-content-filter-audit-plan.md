# organvm Content Filter Audit Plan

**Date Created**: 2026-02-28  
**Objective**: Identify repository names and descriptions in the 101-repo organvm system that could trigger automated content filtering systems, documenting the innocuous creative-institutional context.

## Phase 1: Registry Extraction & Analysis Setup

### Task 1.1: Extract Registry JSON
- **Action**: Parse the cached registry-v2.json file from `/Users/4jp/Workspace/meta-organvm/organvm-corpvs-testamentvm/registry-v2.json`
- **Expected Output**: Complete registry structure with all 101 repository entries
- **Key Fields to Extract**:
  - `name`: Repository name (e.g., "recursive-engine", "public-record-data-scrapper")
  - `description`: Repository description (long-form content)
  - `organ_id`: Which of the 8 organs (I-VII + META)
  - `tier`: flagship|standard|stub|archive|infrastructure
  - `promotion_status`: LOCAL|CANDIDATE|PUBLIC_PROCESS|GRADUATED|ARCHIVED

### Task 1.2: Define Content Filter Keywords
**Keywords to Search For** (common content filter triggers):
- **Violence**: kill, death, attack, destroy, war, blood, murder, assault, weapon, gun, bomb, torture, execution, violence, rage, brutal
- **Weapons**: gun, rifle, explosive, bomb, missile, grenade, weapon, armory, arsenal
- **Sexual/Explicit**: adult, explicit, nude, porn, sex, xxx, adult content markers
- **Hate/Discrimination**: hate, racist, discriminatory, slur, offensive (in isolation)
- **Drugs**: cocaine, heroin, drug, illegal substance, narcotic
- **Dangerous/Illegal**: illegal, crime, criminal, felony, contraband
- **Death-related**: death, die, dying, fatal, killer (in isolation), suicide, necro
- **False Positives to Monitor**: 
  - "kill" in "killer app" (legitimate tech slang)
  - "death" in philosophical contexts (organvm uses metaphorical language)
  - "weapons/arms" in tech contexts (cross-arm, arms race, armaments in design)
  - "attack" in cybersecurity contexts
  - "bomb" in "bombast" or tech culture ("this slaps/is the bomb")
  - "destruction" in creative destruction (economic term)

## Phase 2: Systematic Audit Process

### Task 2.1: Analyze Repository Names
- **Process**: 
  1. Iterate through all 101 repos
  2. Check repo name against content filter keywords
  3. Flag any matches with context assessment
  4. Document organ, tier, and promotion_status for each flagged repo

### Task 2.2: Analyze Repository Descriptions
- **Process**:
  1. Iterate through all 101 repos
  2. Check description against content filter keywords
  3. Flag any matches with context assessment
  4. Note if description contains metaphorical/institutional language (e.g., "governance", "orchestration")
  5. Document exact phrase and surrounding context

### Task 2.3: Context Documentation
- **For Each Flagged Item**:
  - Quote the exact problematic term/phrase
  - Provide surrounding context (full description excerpt)
  - Explain why it's innocuous in the organvm creative-institutional framework
  - Note what the term actually refers to (e.g., metaphorical governance, technical architecture, etc.)

## Phase 3: Reporting

### Task 3.1: Compile Findings
- **Output Format**: Structured markdown document with:
  - Summary statistics (total repos scanned, flagged items, false positives, genuine concerns)
  - Organized by organ (I-VII + META) for clarity
  - Risk categorization:
    - **Green**: Clearly innocuous (tech slang, metaphorical language)
    - **Yellow**: Potentially ambiguous (context-dependent, but reasonable in institutional framework)
    - **Red**: Genuinely problematic (if any found)

### Task 3.2: Repository Listing with Flags
- **For Each Organ** (I-VII + META):
  - List all repos with tier and promotion status
  - Highlight flagged names/descriptions
  - Provide context explanation
  - Cross-reference with registry metadata

### Task 3.3: Recommendations
- **API Response Planning**: Suggest how to handle content filtering:
  - Which repos should have descriptions adjusted for public API visibility
  - Which are safe as-is (most likely)
  - Whether any need content filter bypass documentation
  - Whether GitHub should be informed of false positives

## Phase 4: Delivery

### Task 4.1: Final Report Structure
```
# organvm Content Filter Audit Report
## Executive Summary
- Total repos scanned: 101
- Flagged items: [N]
- False positives: [N]
- Genuinely problematic: [N]

## Audit Findings by Organ
### ORGAN-I Theoria
[repos with flags]

### ORGAN-II Poiesis
[repos with flags]

... etc for I-VII + META

## Detailed Findings
### Repository Name Flags
[organized by organ and risk level]

### Repository Description Flags
[organized by organ and risk level]

## Context & Analysis
[explanations for each flagged item]

## Recommendations
[API response strategy, adjustments needed, etc.]
```

## Success Criteria

- [ ] All 101 repositories identified and analyzed
- [ ] All potential content filter keywords identified and checked
- [ ] False positives vs. genuine concerns distinguished
- [ ] Creative-institutional context documented for each flagged item
- [ ] Comprehensive report delivered to user
- [ ] Clear recommendations provided for API response planning

## Dependencies

- Access to cached registry-v2.json content
- Understanding of organvm's creative-institutional framework (8-organ system, distributed governance, metaphorical language use)
- Knowledge of common content filtering keyword lists

## Notes

- The organvm system uses sophisticated metaphorical language (governance, orchestration, architecture, etc.)
- Many terms that might trigger filters are completely innocuous in institutional/technical contexts
- The audit must distinguish between:
  1. Technical terminology (architecture, implementation, deployment)
  2. Institutional metaphors (governance, orchestration, hierarchy, distribution)
  3. Philosophical/creative concepts (systems thinking, emergence, composition)
  4. False positives (common tech slang, legitimate domain language)

## Timeline

This is a read-only plan mode session, so execution is pending user approval to proceed.
