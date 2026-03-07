# SOP: Cross-Agent Session Handoff

**Version:** 1.0.0 | **Date:** March 6, 2026 | **Status:** Active
**Scope:** Governance procedure for receiving, triaging, and reconciling work produced by external AI agents (Gemini, GPT, Copilot, etc.) into the ORGANVM system.

---

## 1. Ontological Purpose

Cross-agent handoff is a **governance concern**, not merely a file-management task. When an external agent produces deliverables in an ORGANVM workspace, those artifacts exist outside the system's quality contracts (METADOC standards, seed.yaml declarations, promotion state machine). This SOP ensures that externally-generated work is triaged for structural integrity, audited against content standards, and formally reconciled into the governed corpus before it is treated as system output.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 3: Governance & Lifecycle)

The core risk: **an external agent may believe it has completed work that the system does not recognize.** Files may be untracked, standards may be unmet, and the agent's self-reported success may diverge from actual deliverable quality.

---

## 2. Intake Protocol

When receiving a session transcript or batch of files from an external agent:

1. **Identify the scope.** Which repos and organs were touched? Which METADOC/SOP standards apply?
2. **Inventory the artifacts.** List every file the agent claims to have created or modified.
3. **Capture the prompts.** Extract the user's original requests (not the agent's paraphrases) to establish the ground-truth requirements.
4. **Note the agent's self-assessment.** What did it claim to have accomplished? This becomes the audit baseline.

---

## 3. Triage Checklist (Structural Validation)

Run these checks before evaluating content quality:

- [ ] **Git status:** Are all claimed files actually tracked by git? Check `.gitignore` allowlists in superprojects.
- [ ] **File placement:** Are files in the correct repo and directory per the workspace map?
- [ ] **Version integrity:** Were files overwritten multiple times? Check git log or agent transcript for destructive rewrites.
- [ ] **Data integrity:** Were any protected files (registry-v2.json, governance-rules.json, seed.yaml) modified? If so, validate against the Data Integrity Rules.
- [ ] **Naming conventions:** Do filenames follow the double-hyphen convention and project patterns?
- [ ] **No orphaned references:** Do cross-references between files resolve to tracked, accessible paths?

---

## 4. Content Audit Protocol

Cross-reference the user's original prompts against the delivered artifacts:

1. **Standards compliance.** For each deliverable, identify the governing METADOC/SOP and check section-by-section compliance.
2. **Gap identification.** List every framework, analysis, or section required by the standard that is absent from the deliverable.
3. **Quality assessment.** For sections that exist, evaluate depth and rigor:
   - Is it a skeleton placeholder or a substantive analysis?
   - Does it contain specific evidence or only generic assertions?
   - Are sources cited with Trust Scores per METADOC requirements?
4. **Severity classification:**
   - **Critical:** Missing entire frameworks required by METADOC (e.g., no STEEP, no CLA)
   - **Major:** Sections exist but are skeletal or generic
   - **Minor:** Formatting, naming, or cross-reference issues

---

## 5. Decision Log Template

For each artifact, record:

| Artifact | Decision | Rationale | Action |
|----------|----------|-----------|--------|
| `filename.md` | ACCEPT / REJECT / EXPAND | Why | Specific remediation steps |

Decisions:
- **ACCEPT:** Artifact meets standards. Commit as-is.
- **REJECT:** Artifact fails structural validation. Do not commit. Document why.
- **EXPAND:** Artifact has a sound foundation but fails content audit. Commit the base, then expand to meet standards.

---

## 6. Reconciliation

After triage and content audit:

1. **Fix structural issues first.** Gitignore allowlists, file placement, naming.
2. **Commit accepted artifacts** with clear provenance in the commit message (e.g., `docs: add research deliverables from Gemini session [handoff]`).
3. **Expand deficient artifacts** per the content audit findings.
4. **Update submodule pointers** if work spans multiple repos.
5. **Update project memory** with:
   - Session inventory (what was produced, by which agent)
   - Structural lessons learned
   - Content gaps identified and resolved
   - Agent-specific behavioral risks observed

---

## 7. Known Agent Risks

### Gemini Code Assist
- **Destructive rewrites:** Uses `open(path, "w")` to overwrite files wholesale, losing intermediate versions. Multiple rewrites in a single session can cause version chaos.
- **Git tracking assumption:** Believes files are committed and pushed after writing them to disk. Does not verify `.gitignore` allowlists in superprojects.
- **Framework dropping under long context:** As context window fills, later deliverables may silently drop frameworks that were correctly applied in earlier deliverables.
- **Self-reported success divergence:** Claims completion of standards it has not actually met. Always verify against the METADOC, not the agent's summary.

### General Risks (All External Agents)
- **Prompt drift:** Agent reinterprets the user's request rather than executing it literally. Always audit against original prompts, not agent paraphrases.
- **Hallucinated sources:** URLs, citations, or data points may be fabricated. Verify critical sources.
- **Scope creep / scope shrink:** Agent may add unrequested features while omitting requested ones.

---

## 8. Versioning

This SOP follows the same versioning rules as all ORGANVM governance documents. Revisions are never overwritten; new versions are created with incremented version numbers.

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
