# Plan: Map Parlor Games Spec Tasks to GitHub Epics

## Objective
Understand the structure of GitHub issues (epics) in organvm-iii-ergon/parlor-games--ephemera-engine and map tasks from the 6 SpecKit specifications to the correct epic issues.

## Current State
- Successfully retrieved JSON data for ~30 GitHub issues via gh CLI
- Data saved to: `/Users/4jp/.claude/projects/-Users-4jp-Workspace-organvm-iii-ergon-parlor-games--ephemera-engine/65efd28e-edc7-425f-a6c6-cb388bad8528/tool-results/b80be33.txt` (35.9KB)
- Preview shows Issue #30 (Initiative 004: Murder Mystery) and #29 (Initiative 003: Confession Album)
- Project is in DESIGN_ONLY status with artifact rendering pipeline built

## SpecKit Dependencies (Build Order)
```
001 (Auth, profiles, session state) → foundation
002 (Invitations, contributions) → depends on 001
003 (Confession Album) → depends on 001, 002
004 (Murder Mystery) → depends on 001, 002
005 (Dashboard shell, offline infra) → depends on 001
006 (Server artifact rendering) → depends on 001
```

## Analysis Tasks

### Task 1: Parse Complete JSON Output
- Read full JSON file from tool results
- Extract all issues with their:
  - Number
  - Title
  - Body (task descriptions and dependencies)
  - Labels (epic identifier, priority, spec number)
- Identify epic structure and issue relationships

### Task 2: Map Spec Files to Epic Issues
- For each of 6 specs (001-006):
  - Identify corresponding GitHub issue/initiative
  - Extract task list from issue body
  - Map individual tasks to spec's requirements
  - Document dependencies between specs

### Task 3: Create Epic-Spec Mapping Document
- Structured mapping showing:
  - Epic issue number → Spec number
  - Epic title and purpose
  - Number of tasks per epic
  - Direct dependencies (blockedBy relationships)
  - Task categories within each epic

### Task 4: Identify Task Dependencies
- Cross-reference issue bodies for task dependencies
- Create dependency graph showing:
  - Which spec tasks block which other specs
  - Critical path for implementation
  - P0/P1/P2 priority distribution

## Constitutional Gates to Verify
- **Simplicity**: Max 3 Supabase Edge Functions
- **Offline**: Game night works with zero connectivity
- **Privacy**: No social feed, contributions encrypted
- **Analog**: Screen-dark during active play

## Deliverables (READ-ONLY PLAN MODE)
1. Complete epic-to-spec mapping document
2. Task dependency graph/matrix
3. Constitution gate checklist against task list
4. Recommended implementation sequence confirmation

## Status
- **Plan Mode**: Awaiting user authorization to proceed with analysis
- **No modifications**: All work is read-only analysis of existing data
- **Next Action**: User to review and authorize execution of analysis tasks
