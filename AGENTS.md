# Working Agreement

## Purpose

Build a reproducible, local research testbed for studying NASA/JPL ION-DTN,
DTN, BPv7, and related security properties. The current phase is preparation;
no vulnerability or attack result is established.

## Rules

- Label unsupported claims as **Hypothesis** or **Unverified**. Prefer official
  standards and documentation, then implementation code, runtime evidence, and
  recorded experiments.
- Do not call behavior a vulnerability until it is reproduced, its root cause
  is understood, and its security impact is supported.
- Run offensive experiments only in isolated local or explicitly authorized
  environments. Never target operational spacecraft, ground stations, or third
  parties. Follow `docs/RESPONSIBLE_RESEARCH.md` for security work.
- Read `PROJECT_STATE.md` when current status affects the task. Record important
  research or design decisions in `docs/DECISIONS.md`; do not log trivia.
- Test modified code. Add a regression test for a security fix when practical.
- Record experiments reproducibly using `experiments/TEMPLATE.md`.
- Use `.agent/PLANS.md` only for multi-hour, cross-cutting, or otherwise complex
  work. Small changes do not need an ExecPlan.
- Update `PROJECT_STATE.md` after materially completing or changing project work.
