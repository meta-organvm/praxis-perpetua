# Registry Drift Fix: Document-by-Document Cascade

## Context

Full review of all 18 documents in `/Users/4jp/Workspace/organvm-pactvm/ingesting-organ-document-structure/` to identify and fix classification drift between documented intent and current registry state (142 repos across 9 org dirs).

---

## Drift Register (accumulated across ALL documents)

### A. 6 commerce repos misclassified as organ_i — need organ_iii overrides

Original repos in ivviiviivvi (ORG_I), inheriting organ_i from org_unit_override. Documents consistently place these under ORGAN-III (Commerce):

| repo_unit_id | Current | Correct |
|---|---|---|
| `classroom-rpg-aetheria` | organ_i | organ_iii |
| `gamified-coach-interface` | organ_i | organ_iii |
| `fetch-familiar-friends` | organ_i | organ_iii |
| `trade-perpetual-future` | organ_i | organ_iii |
| `search-local-happy-hour` | organ_i | organ_iii |
| `sovereign-ecosystem-real-estate-luxury` | organ_i | organ_iii |

Confirmed in: 00-00, 00-a (registry-v2.json embedded), 00-b (org_unit_overrides for labores-profani-crux → organ_iii), 02 (repo inventory lists them under ORGAN-III).

### B. Mole fork: organ_i → organ_iii

`tw93:mole` — fork, not user's repo. Current override at line 45 of explicit_overrides.json sets `organ_id: "organ_i"`. Should be `organ_iii` (it's a recipe/commerce app).

### C. 2 repos on GitHub but not cloned locally — clone them

- `ivviiviivvi/auto-revision-epistemic-engine` — ORGAN I theory repo, 202KB
- `ivviiviivvi/a-i-chat--exporter` — AI chat export tool, 1735KB

### D. Debatable (user: "idk" — deferred)

- `life-my-midst-in` — currently organ_i/create, doc 00-00 said organ_v
- `domus-semper-palingenesis` — currently organ_i/create, doc 00-00 said organ_vii

No action now. Revisit when user decides.

### E. 4444JPP archival — already done

All 49 repos in liminal_alt already `liminal_zone/archive/archived`. Confirmed.

### F. Aspirational orgs/repos referenced in documents — NOT drift, future work

Documents reference orgs and repos that don't exist yet. These are aspirational targets from the design conversation, not current misclassifications:

**Non-existent orgs referenced:**
- `4444j99-orchestration` (ORGAN-IV)
- `4444j99-organs` (ORGAN-V)
- `4444j99-community` (ORGAN-VI)
- `4444j99-marketing` (ORGAN-VII)

**Non-existent repos referenced:**
- `orchestration-start-here`, `public-process`, `salon-archive`, `reading-group-curriculum`, `announcement-templates`, `social-automation`, `distribution-strategy`, `commerce--meta`

**Repo count drift:** Documents say 60-74 repos; reality is 142 (liminal_alt absorption added ~49).

No action needed — these are future creation targets, not fixes.

---

## Document Review Progress

- [x] 00-00-ORGAN_SYSTEM_AUDIT.md — deep dive, source of all drift items A-E
- [x] 00-a (11,054 lines) — CONFIRMS A,B,C. Contains embedded v1+v2 of all design docs. Aspirational orgs/repos identified (F)
- [x] 00-b (3,645 lines) — CONFIRMS A. Contains filesystem ontology, audit pipeline design, generator code, organ_charter_v0, realm_organ_matrix. Shows `labores-profani-crux → organ_iii` mapping that never landed as repo-level overrides
- [x] 00-c (432 lines) — Phase 1 master summary. No new drift. References 74 repos
- [x] 01-README-AUDIT-FRAMEWORK.md (213 lines) — Scoring rubric. No drift
- [x] 02-REPO-INVENTORY-AUDIT.md (187 lines) — CONFIRMS A. Lists commerce repos under "labores-profani-crux" org
- [x] 03-PER-ORGAN-README-TEMPLATES.md (400 lines) — Templates. No drift
- [x] 04-PER-ORGAN-VALIDATION-CHECKLISTS.md (269 lines) — Checklists. No drift
- [x] 05-RISK-MAP-AND-SEQUENCING.md (387 lines) — Risk map. No drift
- [x] github-actions-spec.md (844 lines) — 5 workflows. References non-existent orgs (F)
- [x] orchestration-system-v2.md (491 lines) — Parallel launch governance. References non-existent orgs (F)
- [x] IMPLEMENTATION-PACKAGE-v2.md (500+ lines) — 3-phase timeline. References non-existent orgs (F)
- [x] public-process-map-v2.md (500+ lines) — Essays, POSSE. References non-existent repos (F)
- [x] PARALLEL-LAUNCH-STRATEGY.md (396 lines) — Strategic overview. No new drift
- [x] PHASE-1-EXECUTION-INDEX.md (344 lines) — Master index. No new drift
- [x] registry-v2.json (500+ lines) — CONFIRMS A. Commerce repos under "labores-profani-crux". Aspirational (F)
- [x] archive/orchestration-system.md (604 lines) — v1 governance. No new drift
- [x] archive/public-process-map.md (791 lines) — v1 public process. No new drift
- [x] archive/IMPLEMENTATION-PACKAGE.md (449 lines) — v1 package. No new drift
- [x] archive/registry.json — v1 registry, 46 repos. No new drift

**Result: No new drift items beyond what 00-00 surfaced. All subsequent documents either CONFIRM the same items or contain aspirational references (future work).**

---

## Files to Modify

| File | Change |
|------|--------|
| `_registry/explicit_overrides.json` | 1. Add 6 repo_overrides for commerce repos (organ_iii) in ORG_I section |
| `_registry/explicit_overrides.json` | 2. Fix existing mole override: `organ_i` → `organ_iii` (line 45) |

### Exact overrides to add (insert before the tw93:mole entry at line 45):

```json
{"match": {"org_unit_id_env": "ORG_I", "repo_unit_id": "classroom-rpg-aetheria"}, "set": {"organ_id": "organ_iii"}},
{"match": {"org_unit_id_env": "ORG_I", "repo_unit_id": "gamified-coach-interface"}, "set": {"organ_id": "organ_iii"}},
{"match": {"org_unit_id_env": "ORG_I", "repo_unit_id": "fetch-familiar-friends"}, "set": {"organ_id": "organ_iii"}},
{"match": {"org_unit_id_env": "ORG_I", "repo_unit_id": "trade-perpetual-future"}, "set": {"organ_id": "organ_iii"}},
{"match": {"org_unit_id_env": "ORG_I", "repo_unit_id": "search-local-happy-hour"}, "set": {"organ_id": "organ_iii"}},
{"match": {"org_unit_id_env": "ORG_I", "repo_unit_id": "sovereign-ecosystem-real-estate-luxury"}, "set": {"organ_id": "organ_iii"}}
```

### Mole fix (modify existing line 45):

```json
// BEFORE:
{"match": {"repo_uid": "tw93:mole"}, "set": {"org_unit_id": "liminal", "organ_id": "organ_i", "realm_id": "research", "lifecycle": "reference"}}
// AFTER:
{"match": {"repo_uid": "tw93:mole"}, "set": {"org_unit_id": "liminal", "organ_id": "organ_iii", "realm_id": "research", "lifecycle": "reference"}}
```

---

## Actions (sequenced)

1. **Edit** `_registry/explicit_overrides.json` — add 6 commerce overrides + fix mole
2. **Clone** `ivviiviivvi/auto-revision-epistemic-engine` into `~/Workspace/` (will land in world tree via symlink)
3. **Clone** `ivviiviivvi/a-i-chat--exporter` into `~/Workspace/`
4. **Run** `phase1_audit.py` to rescan and produce new `git_repos.json`
5. **Run** `gen_manifests.sh $RUN_DIR` to regenerate all 4 manifests
6. **Verify**: Check organ_manifest for the 6 repos showing `organ_iii`, mole showing `organ_iii`, and the 2 new repos present

---

## Verification

After steps 1-5:
- `jq '.repos[] | select(.repo_unit_id == "classroom-rpg-aetheria") | .organ_id' organ_manifest.json` → `"organ_iii"`
- Same check for the other 5 commerce repos
- `jq '.repos[] | select(.repo_uid == "tw93:mole") | .organ_id' organ_manifest.json` → `"organ_iii"`
- `jq '.repos[] | select(.repo_unit_id == "auto-revision-epistemic-engine")' organ_manifest.json` → exists
- `jq '.repos[] | select(.repo_unit_id == "a-i-chat--exporter")' organ_manifest.json` → exists
- Total repo count: 144 (142 + 2 new clones)
