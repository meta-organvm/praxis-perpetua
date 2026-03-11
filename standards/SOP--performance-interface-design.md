# SOP: Performance Interface Design (The Stage Protocol)

## 1. Ontological Purpose
This SOP formalizes the creation of live performance interfaces, mapping complex internal logic (e.g., Pure Data, SuperCollider patches) to visceral, stage-ready control surfaces. It bridges the gap between deep synthesis and human performance.

**Governed by:** `METADOC--sop-ecosystem.md`
**Applicable to:** ORGAN-II (Poiesis) live performance tools.

---

## 2. Phase I: Signal Flow Mapping
**Goal:** Define the control taxonomy.
1. **Parameter Audit:** Identify which parameters of the generative engine are "live-safe" versus "structurally destructive."
2. **OSC/MIDI Binding:** Map live-safe parameters to Open Sound Control (OSC) addresses or MIDI CC values.
3. **Latency Bounding:** Use formal checks to ensure control signal processing does not interrupt audio DSP threading.

## 3. Phase II: UI/UX Brutalist Formatting
**Goal:** Design for high-stress visibility.
1. **High Contrast:** Enforce CMYK/Monochrome brutalist styling for stage visibility under harsh lighting.
2. **Hitboxes:** Ensure touch/click targets are massively oversized to account for adrenaline and movement.
3. **State Feedback:** Provide immediate visual confirmation of state changes (e.g., flash arrays, color inversion).

## 4. Phase III: Live State Recovery
**Goal:** Survive the inevitable crash.
1. **State Snapshotting:** Continuously write macro-states to a lightweight local file (e.g., JSON).
2. **Panic Buttons:** Implement a physical or easily accessible digital "Panic" button that instantly mutes all audio and resets DSP routing without closing the application.

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
