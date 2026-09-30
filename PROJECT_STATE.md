# Project State

Last updated: 2026-10-01

## Current Phase

Research preparation: local feasibility confirmed; ION baseline selection pending.

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
- Existing ChatGPT Project renamed to `Space DTN Security Lab`, project instructions
  applied, and live GitHub read access to `PROJECT_STATE.md` verified.
- Local hardware, WSL2 capacity, installed toolchain, and performance constraints
  assessed; a 12-week gated roadmap is documented in
  `docs/setup/LOCAL_FEASIBILITY.md`.

## In Progress

- None. Bootstrap is complete; the first research-phase task has not started.

## Current Questions

- Which license, if any, is appropriate after source and disclosure constraints
  are understood?
- Which research question and attacker capability should be prioritized?

## Next Actions

1. Decide whether to pin stable `ion-open-source-4.2.0` (`568df88`) as the
   research baseline and record the decision.
2. Study the minimum DTN, BPv7, CBOR, BPSec, and ION-DTN foundations.
3. With explicit approval, install the missing WSL Automake prerequisites.
4. Create an ExecPlan for the first baseline build and loopback/2-node validation.

## Known Problems

- Docker and native Windows C/C++ build tools are not installed.
- WSL2 Ubuntu 24.04 has GCC/G++, GNU Make, GDB, Git, and Python 3; Clang, CMake,
  and Ninja are not installed. Any installation requiring administrator rights
  remains deferred.
- The official default ION build path additionally needs Automake, Autoconf,
  Libtool, and M4; these are not installed yet.
- Host RAM is 16 GB and WSL currently exposes about 8 GB, so high-worker fuzzing,
  multiple full VMs, and sanitizer-heavy parallel workloads require limits.

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
