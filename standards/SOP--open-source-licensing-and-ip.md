# SOP: Open Source Licensing and IP (The Commons Protocol)

## 1. Ontological Purpose
This SOP defines strict rules for open-source versus proprietary licensing across the 8 Organs. It ensures that the system's intellectual property is protected where necessary (Commerce) while remaining open and generative where beneficial (Theory, Art).

**Governed by:** `METADOC--sop-ecosystem.md`
**Applicable to:** All repositories in the ORGANVM ecosystem.

---

## 2. Phase I: License Boundary Definition
**Goal:** Apply the correct license to the correct organ.
1. **ORGAN-I (Theory):** Default to MIT License or CC0 to encourage maximal spread of philosophical concepts.
2. **ORGAN-II (Art):** Default to CC BY-NC 4.0 to protect generative outputs from unauthorized commercial exploitation while allowing artistic remixing.
3. **ORGAN-III (Commerce):** Default to Proprietary/Closed Source. Ensure no permissive licenses accidentally leak the core business logic.
4. **META/Taxis:** Default to Apache 2.0 or MIT to encourage standard adoption, but withhold proprietary orchestration keys.

## 3. Phase II: Dependency Auditing
**Goal:** Prevent viral license contamination.
1. **Scan:** Use `reverse-engine-recursive-run` to scan all dependencies.
2. **Block:** Fail the CI build if a GPLv3 dependency is introduced into an ORGAN-III (Proprietary) repository.

## 4. Phase III: Contributor Enforcement
**Goal:** Manage external input safely.
1. **CLA:** Ensure all public repositories have a Contributor License Agreement (CLA) bot active.
2. **Code of Conduct:** Enforce the Contributor Covenant to maintain a healthy dialectical environment in ORGAN-VI.

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
