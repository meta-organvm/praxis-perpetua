# Agent Behavioral Risks

Per-agent risk profiles accumulated from session reviews. Updated as new behaviors are observed.

---

## Gemini Code Assist

**Sessions observed:** 1 (2026-03-06 Styx research)

### Known Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| **Destructive rewrites** | HIGH | Uses `open(path, "w")` for every edit. Intermediate versions are permanently lost. Commit after each write cycle. |
| **Git tracking assumption** | HIGH | Claims files are "committed and pushed" after writing to disk. Does not verify `.gitignore` allowlists or actual git state. Always run `git status` independently. |
| **Framework dropping under long context** | MEDIUM | As context fills (~10+ files), later deliverables silently drop frameworks applied in earlier ones. Audit last-produced files first. |
| **Self-reported success divergence** | MEDIUM | Claims compliance with standards it has not actually met. Verify against the METADOC, not the agent's summary. |

### Behavioral Pattern
Gemini excels at generating volume (10+ research documents in a single session) but degrades in structural compliance as context grows. Treat Gemini output as high-quality raw material requiring systematic triage, not as finished deliverables.

---

## General Risks (All External Agents)

| Risk | Mitigation |
|------|------------|
| **Prompt drift** | Agent reinterprets the user's request rather than executing it literally. Always audit against original prompts, not agent paraphrases. |
| **Hallucinated sources** | URLs, citations, or data points may be fabricated. Verify critical sources independently. |
| **Scope creep / scope shrink** | Agent may add unrequested features while omitting requested ones. Cross-reference deliverables against the original prompt's explicit requirements. |

---

## Claude Code

**Sessions observed:** Many (primary agent)

### Known Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| **Over-compliance** | LOW | May add features, refactoring, or improvements beyond what was requested. Explicit scope instructions help. |
| **Memory boundary** | LOW | Conversation context compresses older messages. For long sessions, re-state critical constraints explicitly. |

### Behavioral Pattern
Claude Code is the primary agent and benefits from integrated tool access (git, filesystem, grep). It verifies its own output in real-time, reducing structural risks. The main risk is scope expansion, not quality degradation.

---

*Last updated: 2026-03-06 | Will expand as more agent sessions are reviewed*
