# Study Suite Output Directory

Output artifacts from the ORGANVM Study Suite — three observer-agent roles modeled on academia, scientific method, and governance.

**Founding specification:** [The Ontological Topology of ORGANVM](../research/2026-03-08-ontological-topology-of-organvm.md), Section IV.

## Directory Structure

```
studies/
  findings/     # Reviewer agent: consilience, contradiction, gap reports
  hypotheses/   # Experimenter agent: hypothesis registry and test results
  audits/       # Auditor agent: drift reports, violation alerts, opinions
```

## Design Principles

1. **Observers, not actors.** Study Suite agents produce knowledge artifacts but never modify production data.
2. **Append-only.** New findings supersede old ones by date. No output is ever overwritten.
3. **Human-readable.** All output is markdown. No JSON-only reports, no binary artifacts.
4. **Triggered, not polled.** Event-driven where possible (post-session, post-commit, post-promotion).

## CLI Access

```bash
organvm study feedback              # Feedback loop inventory
organvm study consilience            # Consilience index for derived principles
organvm study audit                  # Combined governance + feedback + consilience report
organvm study audit --output FILE    # Write report to file
```

## Relationship to Existing Infrastructure

- Study Suite agents are **observation** agents — fundamentally different from execution agents governed by `SOP--agent-seeding-and-workforce-planning.md`.
- The E2G review pattern is the closest manual analog. The Study Suite automates the observation layer while preserving human judgment for the action layer.
- `SOP--autopoietic-systems-diagnostics.md` Phase II (observer position) is the procedural foundation for the Auditor role.
