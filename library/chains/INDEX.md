# Prompt Chains — Index

Executable prompt chain definitions for the ORGANVM system. Each chain is a YAML file describing a sequence of phases with recognition criteria, behaviors, and checkpoints.

## Session-Level Chains

| Chain | Phases | Timescale | Description |
|-------|--------|-----------|-------------|
| [session-protocol](session-protocol.yaml) | 8 | minutes→hours | SEED→HANDOFF — how the human steers AI conversations |
| [close-protocol](close-protocol.yaml) | 12 | end of session | Liturgical close-out — non-negotiable, universally applied |

## Creation-Level Chains

| Chain | Phases | Timescale | Description |
|-------|--------|-----------|-------------|
| [design-grammar](design-grammar.yaml) | 9 | hours→days | DEFINE→TRANSFORM — how the human drives AI to produce structural artifacts |

## Process-Level Chains

| Chain | Phases | Timescale | Description |
|-------|--------|-----------|-------------|
| [sop-lifecycle](sop-lifecycle.yaml) | 5 | days→weeks | rep→absorb→fortify→place→chain — how SOPs are discovered |
| [auditor-pair](auditor-pair.yaml) | 2 | per audit | Above (fleet scan) + Below (reverse lookup) — bidirectional topology check |

## How to Use

Chains are declarations that agents follow — not auto-executing scripts. When you recognize the trigger phrases (listed in each chain's `recognition` fields), you are in that chain's phase. Follow the `behavior` directive for that phase.

Chains nest: a session (session-protocol) CONTAINS a design sequence (design-grammar). The close protocol is invoked by the session protocol's AUDIT phase.

CLI: `organvm chains list` | `organvm chains show <name>`
