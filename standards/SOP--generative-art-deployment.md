# SOP: Generative Art Deployment (The Gallery Protocol)

## 1. Ontological Purpose
This SOP standardizes the packaging of generative systems (WebGL, SuperCollider, Pure Data) into self-contained, crash-proof executables or hardware-bound installations for public presentation. It ensures the theoretical artifacts produced in ORGAN-II (Poiesis) can survive unmediated public interaction.

**Governed by:** `METADOC--sop-ecosystem.md`
**Applicable to:** ORGAN-II (Poiesis) interactive installations and generative works.

---

## 2. Phase I: Hardware & Environment Specification
**Goal:** Define the exact physical boundary of the artwork.
### Process
1. **Target Matrix:** Define the target hardware (Raspberry Pi, Mac Mini, Web Server) and OS.
2. **Dependencies:** Freeze all audio/visual dependencies (e.g., specific Pd-vanilla version, SuperCollider sc3-plugins).
3. **Audio Routing:** Document exact audio interface channels (e.g., Jack setup, aggregate devices).

## 3. Phase II: Software Containerization (Docker for Art)
**Goal:** Isolate the artwork from OS rot.
### Process
1. **Containerize:** Use Docker or Nix to create reproducible runtime environments for visual/audio engines.
2. **State Independence:** Ensure the system boots into a deterministic initial state without requiring user input.
3. **Headless Boot:** Configure systemd or launchd to automatically start the container on power-up.

## 4. Phase III: Kiosk Mode & Recovery
**Goal:** Survive public interaction.
### Process
1. **Input Locking:** Disable keyboard shortcuts, right-clicks, and OS-level gestures in the display environment.
2. **Watchdog Timer:** Implement a Python/bash watchdog that pings the rendering engine. If frame rate drops to 0 or audio halts, autonomously restart the container.
3. **Daily Reset:** Schedule a hard reboot at 4:00 AM daily to clear memory leaks.

---

## 5. Output Artifacts
1. **Hardware Manifest** — Exact specifications of the required deployment rig.
2. **Installation Image/Script** — A single-command deployment script (e.g., `ansible-playbook` or `docker-compose`).
3. **Gallery Runbook** — A 1-page physical sheet for gallery staff detailing power-on and emergency reset procedures.

---
*Version: 1.0.0 | System-Wide Directive | ORGANVM*
