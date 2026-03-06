# Evaluation-to-Growth Review: IDENTITAS PERPETUA Implementation

## Context

The IDENTITAS PERPETUA sprint added per-project social identity to ORGAN-VII (Kerygma). The implementation spans a new `kerygma-profiles/` submodule (registry, secrets, CLI), extensions to `social-automation` (factory, config), `kerygma-pipeline` (profile-aware orchestration), `announcement-templates` (voice variables), plus workflow and documentation updates. All 375 tests pass. This review applies the Evaluation-to-Growth framework to the complete implementation.

**Mode**: Autonomous (full report)
**Output**: Markdown report with actionable items per phase

---

## Phase 1: Evaluation

### 1.1 Critique

**Strengths**:
- **Full backward compatibility**: `_HAS_PROFILES` try/except pattern means the entire profiles system is optional. Pipeline without `profiles_dir` behaves identically to before. Zero regression risk.
- **Clean separation of concerns**: Profile loading, secret resolution, and distributor construction are in separate modules with single responsibilities.
- **Delegation pattern in factory**: `build_distributor_for_profile()` delegates to `SocialConfig.from_profile()` then to existing `build_distributor()` — no parallel code paths to maintain.
- **Secret resolver design**: Three-tier resolution (`op://` → env fallback → empty) with caching is practical for both CI and local dev.
- **Test coverage**: 24 dedicated tests for kerygma-profiles, 8 for factory, 6 for pipeline profiles, 4 for template voice — comprehensive for a first iteration.
- **CLI completeness**: `list`, `show` (with secret redaction), `validate` (with live secret resolution check) — covers the essential operations.

**Weaknesses**:
- **Profile resolution is O(n×m)**: `resolve()` does a linear scan of all profiles × all repos lists. Fine for <50 profiles, problematic at scale.
- **`process_due_entries()` ignores profiles**: Calls `self.dispatch(channel_texts)` without `repo_name` or `profile_id` — scheduled entries always use the global config, never per-project identity. This is a functional bug for the multi-tenant use case.
- **Duplicated profile resolution logic**: The pattern `if self._profile_registry and self._profile_registry.total_profiles > 0: try: if profile_id: ... elif repo_name: ... except KeyError: pass` appears in `_build_distributor()`, `render_and_check()`, and `preview()` — three nearly identical blocks.
- **`_cmd_validate` imported into pipeline**: `kerygma_pipeline.py:1010` does `from kerygma_profiles.cli import _cmd_validate` — reaching into a private function across package boundaries.
- **`profiles show` in pipeline doesn't redact secrets**: The pipeline's `profiles show` handler at line 999-1008 dumps profile JSON without calling `_redact_secrets()`, while the standalone CLI at `cli.py:76-87` does redact.
- **Module-level `_secret_cache` is a global mutable singleton**: No thread safety, no TTL, no size limit. Process-shared mutable state.

**Priority areas** (ranked):
1. Fix `process_due_entries()` to thread profile through dispatch
2. Extract duplicated profile resolution into a helper method
3. Add secret redaction to pipeline's `profiles show`
4. Replace private import with a public function

### 1.2 Logic Check

**Contradictions found**:
- `process_due_entries()` creates channel_texts via `render_and_check()` (which resolves profiles for voice variables) but then calls `self.dispatch(channel_texts)` without `repo_name` — so the template renders with project voice but dispatches with global credentials. Mixed identity.

**Reasoning gaps**:
- `_build_distributor()` catches `(KeyError, NameError)` at line 242 — `NameError` would occur if `build_distributor_for_profile` isn't defined (i.e., `_HAS_PROFILES=False`), but the code already guards with `if self._profile_registry` which is `None` when `_HAS_PROFILES=False`. The `NameError` catch is dead code if the guard works correctly.
- `SocialConfig.from_profile()` resolves secrets eagerly (calls `resolve()` on every credential during construction). This means even platforms not being used get their secrets resolved. Not a bug, but unnecessary work and potential for confusing error messages.
- `resolve_secret()` returns empty string `""` for unresolvable secrets. Downstream, `build_distributor()` checks `if cfg.mastodon_instance_url:` etc. — so empty strings cause clients to not be built. This chain is correct but relies on an implicit contract.

**Unsupported claims**: None — the code doesn't make claims, it implements behavior.

**Coherence recommendations**:
- Remove the `NameError` from the except clause — it masks actual bugs
- Document the "empty string = not configured" contract explicitly
- Make `process_due_entries()` consistent with `run_full_pipeline()` profile threading

### 1.3 Logos Review (Rational/Structural Soundness)

**Argument clarity**: The architecture tells a clear story: profile YAML → registry → resolution → SocialConfig → distributor. Each step is traceable.

**Evidence quality**: 375 passing tests validate the happy paths. Integration tests in `test_profile_dispatch.py` cover the key scenarios (with profiles, without profiles, explicit ID, fallback).

**Persuasive strength**: The `build_distributor_for_profile → SocialConfig.from_profile → build_distributor` chain is convincing — it reuses existing infrastructure rather than creating parallel paths. The factory pattern is well-applied.

**Enhancement recommendations**:
- Add a test for `process_due_entries()` with profiles to verify (and fix) the threading gap
- Add a negative test: what happens when `resolve_secret()` fails for a required credential during dispatch?
- The `_default.yaml` profile uses `op://` references that won't resolve in test environments — tests work around this by creating fresh fixtures, but there's no test that loads the actual shipped `_default.yaml` and attempts a resolve flow

### 1.4 Pathos Review (Developer Experience)

**Current emotional tone**: The system is approachable. YAML profiles are human-readable. The CLI provides clear feedback. Secret redaction in `show` builds trust.

**Audience connection**: Good for the maintainer (single developer operating multi-project). The `kerygma-profiles validate` command gives immediate confidence feedback.

**Engagement level**: The `--profiles-dir` flag on every invocation could become tedious. No way to set a default profiles directory via config or env var.

**Recommendations**:
- Add `KERYGMA_PROFILES_DIR` env var support as default for `--profiles-dir`
- Consider auto-discovering `profiles/` directory relative to the superproject root (similar to how `_find_templates_dir()` works)
- The validate command could suggest corrective actions (e.g., "Set KERYGMA_PROFILE_MASTODON_SYSTEM_ACCESS_TOKEN or install 1Password CLI")

### 1.5 Ethos Review (Credibility/Authority)

**Perceived expertise**: Implementation follows established patterns (dataclasses, YAML config, factory pattern, CLI with subcommands). Code style is consistent with the existing codebase.

**Trustworthiness signals**:
- Present: Secret redaction in CLI output, dry-run by default, comprehensive tests, backward compatibility
- Missing: No schema validation for profile YAML (any typo in key names silently becomes a missing value), no version field in profile schema for future migration

**Authority markers**: The `seed.yaml`, `CLAUDE.md`, and RUNBOOK documentation are thorough. The RUNBOOK section covers onboarding, 1Password setup, and CLI reference.

**Credibility recommendations**:
- Add profile YAML schema validation (at minimum: warn on unknown top-level keys)
- Add a `schema_version: 1` field to profiles for forward compatibility
- The `_default.yaml` has empty values for `bluesky.handle` and `ghost.api_url` — this is technically correct but could confuse someone reading it as a template

---

## Phase 2: Reinforcement

### 2.1 Synthesis — Concrete Actions

| # | Finding | Action | File(s) | Priority |
|---|---------|--------|---------|----------|
| R1 | `process_due_entries()` ignores profiles | Thread `repo_name` from `entry.content_id` through to `dispatch()` call | `kerygma_pipeline.py:624-629` | HIGH |
| R2 | Duplicated profile resolution | Extract `_resolve_profile(repo_name, profile_id) -> ProjectProfile \| None` helper | `kerygma_pipeline.py` | MEDIUM |
| R3 | Pipeline `profiles show` doesn't redact secrets | Import and use `_redact_secrets` or make it a public function | `kerygma_pipeline.py:999-1008`, `cli.py:90` | MEDIUM |
| R4 | Private `_cmd_validate` imported cross-package | Rename to `cmd_validate` (public) or expose through `__init__.py` | `cli.py:108`, `kerygma_pipeline.py:1010` | LOW |
| R5 | `NameError` in except clause is dead code | Change `except (KeyError, NameError)` to `except KeyError` | `kerygma_pipeline.py:242` | LOW |
| R6 | No `KERYGMA_PROFILES_DIR` env var default | Add env var lookup in pipeline CLI before falling back to None | `kerygma_pipeline.py:main()` | LOW |

---

## Phase 3: Risk Analysis

### 3.1 Blind Spots

**Hidden assumptions**:
- Profile `repos` lists are assumed to be non-overlapping. If two profiles claim the same repo, whichever loads first (alphabetical YAML filename order) wins silently. No warning.
- Secret caching assumes secrets don't rotate during a process lifetime. For long-running CI jobs, this could serve stale credentials.
- `resolve_secret()` returns `""` for failures, which is indistinguishable from "intentionally empty." A profile with a typo in its `op://` path silently becomes "platform not configured" rather than failing loudly.

**Overlooked perspectives**:
- **Multiple organs, same project**: A project could span multiple organs (e.g., a product in ORGAN-III with essays in ORGAN-V). The current model is repo→profile, not project→organs.
- **Profile inheritance**: No way to say "this profile inherits from _default but overrides Mastodon credentials." Each profile must be fully self-contained.
- **Calendar per-profile**: The profile schema has `calendar.events` but `KerygmaPipeline` constructs its calendar from the global config, not from profiles. Profile calendar events are loaded but never used.

**Potential biases**:
- The design assumes 1Password as the primary secret manager. Teams using HashiCorp Vault, AWS Secrets Manager, or plain env vars would need to work around the `op://` convention.

**Mitigation strategies**:
- Add duplicate repo detection in `load_directory()` (warn on overlap)
- Add `--strict` flag to `validate` that errors (not warns) on unresolvable secrets
- Document the `calendar.events` limitation or implement profile-calendar merging
- Consider a generic `secret://` prefix with pluggable backends <!-- allow-secret -->

### 3.2 Shatter Points

**Critical vulnerabilities** (severity: HIGH/MEDIUM/LOW):

| Vulnerability | Severity | Impact |
|--------------|----------|--------|
| `process_due_entries()` always uses global config | HIGH | Scheduled posts for project-specific profiles publish under the wrong identity |
| Unresolvable secrets return `""` silently | MEDIUM | Misconfigured profile dispatches nothing but reports no error — silent failure |
| No YAML schema validation | MEDIUM | Typo in profile YAML (`platfroms:` instead of `platforms:`) silently ignored |
| Module-level `_secret_cache` has no TTL | LOW | Long-running process could use stale credentials after rotation |
| Profile resolution O(n×m) | LOW | Only matters at scale (>50 profiles) which is years away |

**Potential attack vectors** (how critics might respond):
- "Why not use an existing multi-tenant config system like Dynaconf?" — Fair, but would add a heavy dependency to a stdlib-focused project. The current approach is proportionate.
- "YAML profiles without schema validation is fragile" — Correct. A JSON Schema or Pydantic model would catch errors early.
- "op:// subprocess calls are a security surface" — True, but `op read` is read-only and runs as the current user. The risk is minimal for a local dev tool.

**Preventive measures**:
- Fix `process_due_entries()` — this is the most consequential bug
- Add basic key validation in `_load_profile()` (warn on unexpected keys)
- Log clearly when a secret resolution returns empty for an `op://` reference

**Contingency preparations**:
- The `_default` fallback ensures the system always has a working identity even if profile resolution fails
- Dry-run mode prevents accidental live dispatch with wrong credentials

---

## Phase 4: Growth

### 4.1 Bloom (Emergent Insights)

**Emergent themes**:
- The profile system is really a **tenant** system. The pattern of YAML-defined identity + credential resolution + factory construction could serve any multi-tenant service, not just social distribution.
- The `voice` system (tone, hashtags, tagline) is a lightweight **brand kit**. Combined with `organ-aesthetic.yaml`, this creates a two-layer identity system: visual (organ) + verbal (project).
- Profile calendar events suggest a future where each project has autonomous scheduling — a **decentralized content calendar** across the organ system.

**Expansion opportunities**:
- **Profile-specific templates**: `announcement-templates/templates/project/<profile-id>/` could override default templates. The `{{#if project.name}}` conditional in the plan was a first step.
- **Profile analytics**: `AnalyticsCollector` could segment metrics by profile, enabling per-project engagement dashboards.
- **Profile webhooks**: Each profile could define notification webhooks for dispatch events, enabling project teams to receive their own notifications.

**Novel angles**:
- The `resolve()` function's repo→profile mapping could be inverted: instead of "which profile owns this repo," ask "which repos does this profile see?" — enabling profile-scoped views of the dispatch log.
- Secret resolution could become a standalone micro-library (`kerygma-resolve`) usable across all organs, not just VII.

**Cross-domain connections**:
- ORGAN-IV's orchestration registry (`registry-v2.json`) already maps repos→organs. Profile resolution could delegate to the registry instead of maintaining a separate `repos` list — single source of truth.
- ORGAN-III product launches could auto-generate profile stubs from `seed.yaml` contracts.

### 4.2 Evolve (Implementation Plan)

**Revision summary** — changes to implement during this review's action phase:

| Step | Action | Files | Effort |
|------|--------|-------|--------|
| 1 | Fix `process_due_entries()` profile threading | `kerygma_pipeline.py` | Small |
| 2 | Extract `_resolve_profile()` helper to DRY up 3 resolution blocks | `kerygma_pipeline.py` | Small |
| 3 | Make pipeline `profiles show` use secret redaction | `kerygma_pipeline.py` | Trivial |
| 4 | Rename `_cmd_validate` → `cmd_validate` and export it | `cli.py`, `__init__.py` | Trivial |
| 5 | Clean `except (KeyError, NameError)` → `except KeyError` | `kerygma_pipeline.py:242` | Trivial |
| 6 | Add `KERYGMA_PROFILES_DIR` env var default | `kerygma_pipeline.py:main()` | Small |
| 7 | Add duplicate repo warning in `load_directory()` | `registry.py` | Small |
| 8 | Add test for `process_due_entries()` with profiles | `test_profile_dispatch.py` | Small |

**Strength improvements (before/after)**:
- Before: scheduled entries always use global config → After: scheduled entries use profile-matched identity
- Before: 3 duplicated resolution blocks → After: single `_resolve_profile()` helper
- Before: pipeline `show` exposes secrets → After: consistent redaction everywhere
- Before: private cross-package import → After: clean public API

**Risk mitigations applied**:
- `process_due_entries()` fix closes the highest-severity shatter point
- DRYing resolution logic prevents future divergence between the three call sites
- Secret redaction prevents accidental credential exposure in CI logs

---

## Verification

After applying the Evolve changes:

```bash
# All existing tests still pass
source .venv/bin/activate
pytest kerygma-profiles/tests/ -v
pytest social-automation/tests/ -v
pytest announcement-templates/tests/ -v
pytest kerygma-pipeline/tests/ -v
cd .github && pytest tests/ -q && cd ..

# New test for process_due_entries + profiles passes
pytest kerygma-pipeline/tests/test_profile_dispatch.py -v

# Verify pipeline profiles show redacts secrets
python kerygma-pipeline/kerygma_pipeline.py --profiles-dir kerygma-profiles/profiles profiles show _default
# Should show op:// refs, not literal secrets

# Verify KERYGMA_PROFILES_DIR env var works
export KERYGMA_PROFILES_DIR=kerygma-profiles/profiles
python kerygma-pipeline/kerygma_pipeline.py profiles list
```
