---
status: reference-activated
---
# Dependency Audit: Metasystem-Master Backplane (ORGAN-II)

**Date:** March 9, 2026
**Backbone Repo:** `organvm-ii-poiesis/metasystem-master` (Omni-Dromenon Engine)

## 1. Dependency Map (12 Repositories)
The following repositories depend on `metasystem-master` for real-time performance orchestration:

| Repository | Organ | Tier | Status |
|------------|-------|------|--------|
| `a-i-council--coliseum` | II | standard | ACTIVE |
| `audio-synthesis-bridge` | II | standard | ACTIVE |
| `client-sdk` | II | standard | ACTIVE |
| `core-engine` | II | archive | ARCHIVED |
| `docs` | II | archive | ARCHIVED |
| `example-choreographic-interface` | II | standard | ACTIVE |
| `example-generative-music` | II | standard | ACTIVE |
| `example-generative-visual` | II | archive | ARCHIVED |
| `example-interactive-installation` | II | standard | ACTIVE |
| `example-theatre-dialogue` | II | standard | ACTIVE |
| `performance-sdk` | II | archive | ARCHIVED |
| `public-process` | V | flagship | ACTIVE |

## 2. Risk Assessment
- **Concentration Risk:** HIGH. `metasystem-master` is the sole provider for all generative examples and the flagship community narrative (`public-process`).
- **Archive Debt:** 4 of the 12 dependencies are ARCHIVED, representing legacy code paths that should be decoupled to reduce the surface area of the backplane.
- **Cross-Organ Sensitivity:** The dependency from ORGAN-V (`public-process`) creates a critical link where a breaking change in the engine could de-validate the system's primary publication layer.

## 3. Recommendations
- **Version Pinning:** Implement strict semantic versioning for `metasystem-master` to prevent breakage in the 8 active dependent repos.
- **Decoupling Strategy:** Evaluate if `public-process` can depend on a static export rather than the live engine.
- **Regression Suite:** The `commercial-validation-testbed` (ORGAN-III) should include a smoke test specifically for the `metasystem-master` -> `client-sdk` link.
