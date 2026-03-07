# SOP: Security & Accessibility Audit

## 1. Ontological Purpose

This SOP defines the repeatable procedure for conducting security vulnerability scans and WCAG 2.1 AA accessibility assessments across the ORGANVM ecosystem. Point-in-time audit reports exist in the corpus (`security-audit-2026-03.md`, `accessibility-audit-2026-03.md`), but without a repeatable SOP, audits are ad-hoc and their coverage inconsistent.

Security and accessibility are not separate concerns — they are two dimensions of the same question: **"Can all intended users safely use this system?"** A system with XSS vulnerabilities fails some users through exploitation. A system without skip links fails some users through exclusion. Both are defects.

**Governed by:** `METADOC--sop-ecosystem.md` (Cluster 2: Quality & Integrity)
**Cross-reference:** `SOP--structural-integrity-audit.md` (code-level structural audit extends to security patterns), `SOP--product-deployment-and-revenue-activation.md` (security audit is a pre-deployment gate), `SOP--promotion-and-state-transitions.md` (no critical audit findings allowed for promotion)

---

## 2. Phase I: Dependency Scanning

### Process

1. **Scan all subprojects for known vulnerabilities:**
   ```bash
   # Python projects
   cd organvm-engine && pip-audit
   cd alchemia-ingestvm && pip-audit
   cd system-dashboard && pip-audit
   cd organvm-mcp-server && pip-audit

   # Node.js projects
   cd stakeholder-portal && npm audit
   # Any other Node subprojects
   ```

2. **Check for CVEs in pinned versions:**
   - Review `requirements.txt` / `pyproject.toml` version pins
   - Review `package-lock.json` / `pnpm-lock.yaml` for outdated dependencies

3. **Classify findings:**
   | Severity | Action | Timeline |
   |----------|--------|----------|
   | Critical | Fix immediately | Same day |
   | High | Fix before next deployment | Within 1 week |
   | Medium | Track as issue | Within 1 month |
   | Low | Note for next quarterly audit | Next quarter |

4. **Document findings** in the audit report.

### Starter Research Questions
- When was the last dependency scan run?
- Are there any dependencies with known end-of-life dates?
- Do any dependencies have alternative, more actively maintained forks?
- Are transitive dependencies also covered by the scan?

---

## 3. Phase II: Credential Audit

### Process

1. **Scan for secrets in codebase:**
   ```bash
   # Search for common secret patterns across all repos
   grep -rn "API_KEY\|SECRET\|PASSWORD\|TOKEN\|PRIVATE_KEY" \
     --include="*.py" --include="*.ts" --include="*.js" \
     --include="*.yaml" --include="*.yml" --include="*.json" \
     --include="*.env" --include="*.toml" \
     ~/Workspace/
   ```

2. **Verify `.gitignore` completeness:**
   - [ ] `.env` and `.env.local` are gitignored in all repos
   - [ ] No `*.pem`, `*.key`, `*.cert` files tracked
   - [ ] No config files with embedded credentials tracked

3. **Audit environment variable management:**
   - [ ] All secrets use platform secret managers (Render, Vercel, etc.)
   - [ ] No secrets in GitHub Actions workflows (use GitHub Secrets)
   - [ ] API keys have appropriate scope limitations

4. **Verify credential rotation:**
   - [ ] When was each API key last rotated?
   - [ ] Are there any keys older than 90 days?
   - [ ] Are revoked keys fully removed from all environments?

### Starter Research Questions
- Has `git log --all -p` been searched for historical secret commits?
- Are there any third-party services with long-lived API keys?
- Do any services support short-lived tokens instead of long-lived keys?
- Is there a credential rotation schedule?

---

## 4. Phase III: WCAG 2.1 AA Assessment

### Process

1. **Automated scanning** (run against all deployed web properties):
   ```bash
   # Lighthouse accessibility audit
   lighthouse <URL> --only-categories=accessibility --output=json

   # axe-core CLI (more detailed)
   npx @axe-core/cli <URL>
   ```

2. **Manual checks** (automated tools catch ~30-40% of a11y issues):

   **Keyboard Navigation:**
   - [ ] All interactive elements reachable via Tab
   - [ ] Focus order matches visual order
   - [ ] Focus indicators visible on all focused elements
   - [ ] No keyboard traps (can Tab out of every component)
   - [ ] Skip links present (jump to main content)

   **Screen Reader:**
   - [ ] All images have meaningful alt text (or empty alt for decorative)
   - [ ] Form inputs have associated labels
   - [ ] Landmarks used correctly (nav, main, aside, footer)
   - [ ] ARIA attributes used correctly (no aria-label on non-interactive elements without role)
   - [ ] Heading hierarchy is logical (no skipped levels)

   **Visual:**
   - [ ] Text contrast ratio >= 4.5:1 (AA standard)
   - [ ] Large text contrast ratio >= 3:1
   - [ ] Information not conveyed by color alone
   - [ ] Animations respect `prefers-reduced-motion`
   - [ ] Text resizable to 200% without loss of content

   **Content:**
   - [ ] Link text is descriptive (no "click here")
   - [ ] Error messages identify the field and provide guidance
   - [ ] Language attribute set on `<html>` element
   - [ ] Page titles are descriptive and unique

3. **Classify findings** using the same severity scale as Phase I.

### Starter Research Questions
- Which web properties are deployed and publicly accessible?
- What is the current Lighthouse accessibility score?
- Are there any user reports of accessibility issues?
- Does the design system include accessible component patterns?
- Are there any animations that don't respect prefers-reduced-motion?

---

## 5. Phase IV: Remediation & Tracking

### Process

1. **Create GitHub issues** for each finding:
   - Title: `fix(a11y): {description}` or `fix(security): {description}`
   - Body: Finding, severity, affected URLs/files, remediation guidance
   - Labels: `security` or `accessibility`, severity label

2. **Prioritize by severity** (Critical/High first, then by blast radius).

3. **Fix and verify:**
   - Each fix must be verified against the original finding
   - Re-run the relevant scan to confirm resolution
   - Document the fix in the audit report

4. **Track resolution rate:**
   - Target: 100% of Critical/High within stated timelines
   - Track open findings across quarters

### Starter Research Questions
- How many open findings exist from the previous audit?
- Were all Critical/High findings from last time resolved?
- Are there any findings that have been open for more than one quarter?
- Do any findings require architectural changes (not just patches)?

---

## 6. Phase V: Report Generation

### Process

1. **Generate audit report** following the established format:
   - File: `organvm-corpvs-testamentvm/docs/operations/{type}-audit-YYYY-MM.md`
   - Sections: Executive summary, methodology, findings by severity, remediation status, recommendations

2. **Archive in corpus** operations directory alongside previous audit reports.

3. **Update gap register** in `METADOC--sop-ecosystem.md` if new gaps found.

4. **Commit and push:**
   ```bash
   cd ~/Workspace/meta-organvm/organvm-corpvs-testamentvm
   git add docs/operations/*-audit-*.md
   git commit -m "docs: {security|accessibility} audit YYYY-MM"
   git push origin main
   ```

---

## 7. Execution Cadence

| Frequency | Scope | Action |
|-----------|-------|--------|
| **Quarterly** | Full ecosystem | Complete Phases I-V |
| **Post-major-deployment** | Deployed product | Targeted Phases I, III, IV |
| **On credential alert** | Affected repos | Immediate Phase II |
| **Pre-promotion (PUBLIC_PROCESS+)** | Promoting repo | Targeted Phases I-III |

---

## 8. Output Artifacts

- Audit report in corpus operations directory
- GitHub issues for all findings
- Updated dependency versions (if vulnerabilities patched)
- Remediation verification evidence
- Updated gap register (if applicable)

---

## Appendix A: WCAG 2.1 AA Quick Checklist

| Principle | Guideline | Check |
|-----------|-----------|-------|
| Perceivable | 1.1 Text alternatives | All images have alt text |
| Perceivable | 1.3 Adaptable | Semantic HTML, logical heading order |
| Perceivable | 1.4 Distinguishable | Contrast >= 4.5:1, resize to 200% |
| Operable | 2.1 Keyboard | All elements keyboard-accessible |
| Operable | 2.3 Seizures | No content flashes > 3/sec |
| Operable | 2.4 Navigable | Skip links, descriptive titles, focus visible |
| Understandable | 3.1 Readable | Language attribute, clear labels |
| Understandable | 3.3 Input assistance | Error identification, labels |
| Robust | 4.1 Compatible | Valid HTML, ARIA correct |

## Appendix B: Common Vulnerability Patterns

| Pattern | Where to Look | Fix |
|---------|---------------|-----|
| XSS | User input rendered in HTML | Sanitize/escape output |
| SQL injection | Raw queries with user input | Parameterized queries |
| Path traversal | File paths from user input | Validate/canonicalize paths |
| Secrets in code | `.env` files, config | Environment variables, secret managers |
| Outdated deps | `package.json`, `pyproject.toml` | `npm audit fix`, `pip-audit` |
| Missing CSP | HTTP headers | Add Content-Security-Policy header |

## Appendix C: Audit Report Template

```markdown
# {Security|Accessibility} Audit — YYYY-MM

**Date:** YYYY-MM-DD
**Scope:** [repos/URLs audited]
**Auditor:** [name/agent]

## Executive Summary
[2-3 sentences: overall posture, critical findings count, trend vs. previous]

## Methodology
[Tools used, manual checks performed, scope limitations]

## Findings

### Critical
| # | Finding | Location | Status |
|---|---------|----------|--------|

### High
| # | Finding | Location | Status |
|---|---------|----------|--------|

### Medium/Low
| # | Finding | Location | Status |
|---|---------|----------|--------|

## Recommendations
1.
2.
3.

## Comparison to Previous Audit
[Findings resolved, new findings, trend analysis]
```

---

*Version: 1.0.0 | System-Wide Directive | ORGANVM*
