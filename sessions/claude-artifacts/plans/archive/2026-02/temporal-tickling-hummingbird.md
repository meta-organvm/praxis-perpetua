# Outcomes Activation: From Infrastructure to Conversion

## Context

The previous plan (base resume fix, readiness scores, preflight/submit guardrails) is **complete and committed**. The pipeline infrastructure is now solid — but the pipeline has **48 submissions with 0 positive outcomes** and critical operational gaps preventing conversion. This plan activates the unused follow-up infrastructure, fixes data integrity issues, and drives the next wave of submissions through hard deadlines.

**Current state snapshot (2026-02-27):**
- 48 submitted/acknowledged entries, 0 positive outcomes (45 null, 2 expired, 1 withdrawn)
- 23 submitted entries **missing `timeline.submitted`** dates — breaks follow-up scheduling
- 0 follow-up actions logged (`signals/outreach-log.yaml` is empty)
- 42 research-status entries cluttering `pipeline/active/` (should be in research_pool/)
- 15 active entries still referencing base resumes (no tailored version exists yet)
- 7 drafting entries with hard deadlines (nearest: Google Creative Fellowship 3/18)
- 1 deferred entry (PEN America) resuming 3/1 with deadline 3/16

---

## Phase 1: Fix timeline.submitted on 23 entries

**Why:** Follow-up scheduling (`followup.py`) calculates outreach dates from `timeline.submitted`. Without it, these entries are invisible to the follow-up system.

**Action:** Backfill `timeline.submitted` from `conversion-log.yaml` submitted dates for these 23 entries:

| Entry | Source Date |
|-------|------------|
| anthropic-developer-education-lead | conversion-log |
| anthropic-developer-relations-mcp | conversion-log |
| anthropic-fde | conversion-log |
| anthropic-ml-engineer | conversion-log |
| anthropic-research-engineer | conversion-log |
| anthropic-rse | conversion-log |
| anthropic-security-engineer | conversion-log |
| anthropic-staff-ai-security | conversion-log |
| anthropic-staff-applied-ai | conversion-log |
| anthropic-staff-developer-experience | conversion-log |
| anthropic-staff-developer-relations | conversion-log |
| anthropic-staff-frontend | conversion-log |
| anthropic-staff-member-of-technical-staff-prompt-engineering | conversion-log |
| anthropic-staff-platform-engineer | conversion-log |
| anthropic-staff-product-engineer-growth | conversion-log |
| anthropic-staff-rse | conversion-log |
| anthropic-staff-software-engineer | conversion-log |
| elastic-staff-developer-experience | conversion-log |
| elastic-staff-machine-learning | conversion-log |
| elastic-staff-technical-writer | conversion-log |
| stripe-devex-engineer | conversion-log |
| together-ai | conversion-log |
| cohere-applied-ai | conversion-log |

**Files:** 23 pipeline YAML files in `pipeline/submitted/`
**Reuse:** `signals/conversion-log.yaml` as date source

---

## Phase 2: Activate follow-up system

**Why:** 48 submissions, 0 follow-ups. The infrastructure exists (`followup.py --init`, outreach-log) but has never been used.

**Action:**
1. Run `python scripts/followup.py --init --yes` to populate `follow_up` fields on all submitted entries
2. Run `python scripts/research_contacts.py --batch --limit 10` to identify recruiter contacts for top-tier acknowledged entries
3. Run `python scripts/followup.py` to generate today's actionable follow-up list

**Files:** No code changes. Operational activation of existing scripts.

---

## Phase 3: Archive research entries from active/

**Why:** 42 research-status entries in `pipeline/active/` create noise. The existing `archive_research.py` script handles this but hasn't been run.

**Action:**
1. `python scripts/archive_research.py --report` to preview
2. `python scripts/archive_research.py --yes` to move research entries to `pipeline/research_pool/`

**Files:** No code changes. File moves via existing script.

---

## Phase 4: Reactivate PEN America (deferred, resumes 3/1)

**Why:** PEN America Literary Awards has `resume_date: 2026-03-01` and hard deadline 3/16. It needs to be reactivated and moved through the pipeline immediately after 3/1.

**Action:**
1. On 3/1: advance from deferred to staged via `python scripts/advance.py --to staged --id pen-america-literary`
2. Tailor resume: `python scripts/tailor_resume.py --target pen-america-literary`
3. Build PDF: `python scripts/build_resumes.py --target pen-america-literary`
4. Wire materials: `python scripts/enrich.py --all --id pen-america-literary --yes`
5. Preflight check: `python scripts/preflight.py --target pen-america-literary`

**Files:** `pipeline/active/pen-america-literary.yaml` (status change + materials)

---

## Phase 5: Deadline-driven submissions (nearest first)

Priority order by hard deadline. Each entry needs: tailored resume, cover letter, blocks wired, preflight clean, submit + record.

| Entry | Deadline | Track | Current Status |
|-------|----------|-------|----------------|
| google-creative-fellowship | 2026-03-18 | grant | drafting |
| pen-america-literary | 2026-03-16 | grant | deferred (resumes 3/1) |
| fire-island-residency | 2026-04-01 | residency | drafting |
| headlands-center | 2026-04-01 | residency | drafting |
| nlnet-commons | 2026-04-01 | grant | drafting |
| rauschenberg-residency | 2026-04-14 | residency | drafting |
| wff-housing-fund | 2026-04-14 | grant | drafting |
| warhol-arts-writers | 2026-05-01 | grant | drafting |

**Workflow per entry:**
```bash
python scripts/tailor_resume.py --target <id>
python scripts/tailor_resume.py --target <id> --wire
python scripts/build_resumes.py --target <id>
python scripts/enrich.py --all --id <id> --yes
python scripts/preflight.py --target <id>
python scripts/compose.py --target <id> --profile
python scripts/submit.py --target <id>
# After portal submission:
python scripts/submit.py --target <id> --record
```

**Files:** 8 pipeline YAML files (status progression + materials wiring)

---

## Phase 6: Staged entries — resume tailoring batch

**Why:** 15 entries still referencing base resumes. 9 are staged with rolling/TBA deadlines — ready to submit once resumes are tailored.

**Action:** Batch tailor resumes for staged entries:
```bash
# For each staged entry still using base resume:
python scripts/tailor_resume.py --target <id>
python scripts/tailor_resume.py --target <id> --wire
python scripts/build_resumes.py --target <id>
```

**Entries needing tailored resumes (staged, rolling/TBA deadline):**
- fractured-atlas, github-sponsors, google-ami, google-creative-lab-five
- lambda-literary, pioneer-works, processing-foundation, queer-art
- fire-island-residency, headlands-center (also in Phase 5)

**Files:** Pipeline YAML files (materials_attached updates)

---

## Phase 7: Regenerate patterns.md

**Why:** `signals/patterns.md` is stale — still references "6 submissions" when there are now 48. The conversion analysis is outdated.

**Action:**
```bash
python scripts/conversion_report.py > signals/patterns-new.md
python scripts/funnel_report.py --by position >> signals/patterns-new.md
```

Review and replace `signals/patterns.md` with updated analysis.

**Files:** `signals/patterns.md`

---

## Phase 8: Establish daily operational cadence

**Why:** Infrastructure exists for daily standup, follow-up, outcome tracking, and campaign planning — but none of it is being used systematically.

**Daily (5 min):**
```bash
python scripts/run.py standup
python scripts/run.py followup
python scripts/run.py outcomes
```

**Weekly (15 min):**
```bash
python scripts/run.py campaign
python scripts/run.py funnel
python scripts/run.py velocity
python scripts/run.py hygiene
```

No code changes — operational habit establishment.

---

## Critical Files

| File | Phase | Change Type |
|------|-------|-------------|
| 23 `pipeline/submitted/*.yaml` | 1 | Add `timeline.submitted` dates |
| `pipeline/active/pen-america-literary.yaml` | 4 | Reactivate from deferred |
| 8 `pipeline/active/*.yaml` | 5 | Status progression + materials |
| ~10 `pipeline/active/*.yaml` | 6 | Materials wiring (resume swap) |
| `signals/patterns.md` | 7 | Regenerate from current data |

## Verification

```bash
# After Phase 1: Verify all submitted entries have timeline.submitted
python -c "
from scripts.pipeline_lib import load_entries
for e in load_entries():
    if e.get('status') in ('submitted','acknowledged','interview'):
        ts = e.get('timeline',{}).get('submitted')
        if not ts: print(f'MISSING: {e[\"id\"]}')"

# After Phase 2: Verify follow-up fields populated
python scripts/followup.py

# After Phase 3: Verify active/ is clean
python scripts/archive_research.py --report

# After Phase 5-6: Preflight all staged entries
python scripts/preflight.py

# Full suite
pytest tests/ -v
python scripts/validate.py
```
