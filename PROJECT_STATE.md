# Project State

Last updated: 2026-10-01

## Current Phase

Initial bootstrap / research preparation.

## Completed

- Environment inventory: Windows 11, Git, GitHub CLI authentication, Python,
  Codex, and WSL2 availability checked.
- Independent local Git repository initialized on `main`.
- Public GitHub repository created, `origin` configured, and initial bootstrap
  commit pushed.
- Repository conventions, documentation framework, planning system, experiment
  template, safety policy, and local validation tools created.
- Project-scoped Codex defaults prepared.
- ChatGPT/Codex collaboration and ChatGPT Project setup guidance prepared.

## In Progress

- User authorization of this repository in ChatGPT's GitHub connection.

## Current Questions

- Which license, if any, is appropriate after source and disclosure constraints
  are understood?
- Which research question and attacker capability should be prioritized?

## Next Actions

1. Authorize the repository for ChatGPT and confirm read access.
2. Select and record authoritative ION-DTN source/version information.
3. Study the minimum DTN, BPv7, CBOR, BPSec, and ION-DTN foundations.
4. Design the first local testbed plan before cloning or building ION-DTN.

## Known Problems

- Docker and native Windows C/C++ build tools are not installed.
- WSL2 Ubuntu 24.04 has GCC/G++, GNU Make, GDB, Git, and Python 3; Clang, CMake,
  and Ninja are not installed. Any installation requiring administrator rights
  remains deferred.

## Blockers

- License selection is intentionally deferred for explicit user choice.

## Important Recent Decisions

- Use `Space DTN Security Lab` with public GitHub repository slug
  `space-dtn-security-lab`; naming may be changed later.
- Keep offensive work isolated and treat unverified claims as hypotheses.
- Do not clone/build ION-DTN during repository bootstrap.

## Explicitly Not Completed

- ION-DTN clone or build; BPv7 traffic generation; BPSec implementation analysis;
  attack implementation; fuzzing; vulnerability discovery; NASA/JPL code changes.
