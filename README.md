# Space DTN Security Lab

A reproducible research workspace for studying NASA/JPL ION-DTN, Delay/Disruption
Tolerant Networking, Bundle Protocol Version 7, and their security properties.

Repository: https://github.com/JungSeungYoon/space-dtn-security-lab

## Current status

**Bootstrap / research preparation.** Repository conventions and research
templates are being established. ION-DTN has not been cloned or built, and no
attack, fuzzing campaign, or vulnerability finding exists yet.

## Research goal

Construct an isolated, virtual space-network testbed and use standards, source
code, execution evidence, and reproducible experiments to analyze protocol and
implementation security. Candidate topics are recorded in [PROJECT.md](PROJECT.md)
and are not commitments or findings.

## High-level architecture

The provisional design includes ground and satellite-like DTN nodes, an isolated
attacker node, and a security-analysis environment. See
[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Repository structure

| Path | Purpose |
| --- | --- |
| `docs/` | Research, architecture, decisions, safety, study, and setup notes |
| `environment/` | Future reproducible testbed definitions and setup scripts |
| `experiments/` | Experiment records and reviewable results |
| `fuzz/` | Future harnesses, minimized corpora, and reviewed crash artifacts |
| `pcaps/` | Curated packet captures; large temporary captures stay local |
| `patches/` | Candidate fixes with provenance and validation notes |
| `tests/` | Regression and integration checks when code exists |
| `scripts/` | Small repository and environment utilities |

## Principles

- Treat claims as unverified until supported by primary sources or evidence.
- Keep attack research local or explicitly authorized.
- Preserve commands, inputs, environment details, and raw-artifact references.
- Use the repository as the shared source of truth for ChatGPT and Codex.
- Record AI assistance openly; human understanding and verification remain
  required.

## Getting started

1. Read [PROJECT_STATE.md](PROJECT_STATE.md) for the current phase and next actions.
2. Run `powershell -ExecutionPolicy Bypass -File scripts/doctor.ps1`.
3. Read only the task-relevant documents linked from [AGENTS.md](AGENTS.md).
4. Create experiments from [experiments/TEMPLATE.md](experiments/TEMPLATE.md).

Project Codex defaults are in `.codex/config.toml` and apply only when this
repository is trusted. The requested defaults are GPT-5.6 Sol, medium reasoning,
workspace-write sandboxing, and approval prompts for elevated actions.

## AI workflow and safety

See [docs/AI_WORKFLOW.md](docs/AI_WORKFLOW.md) for role boundaries and
[docs/RESPONSIBLE_RESEARCH.md](docs/RESPONSIBLE_RESEARCH.md) before security
experiments. GitHub access from ChatGPT is read-only for analysis; repository
changes are primarily made and verified through Codex.
