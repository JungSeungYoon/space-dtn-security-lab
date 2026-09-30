# ChatGPT, Codex, and GitHub Workflow

## Roles

**ChatGPT** supports concept learning, RFC/paper discussion, research-direction
critique, threat-model and experiment-design review, result interpretation, and
presentation/research writing.

**Codex** explores the repository and source code, builds environments, implements
and instruments code, runs commands/tests, debugs, prepares fuzzing harnesses and
experiment automation, and updates repository records.

**GitHub repository** is the verified shared state: code, documentation, decisions,
experiments, and current status. Chat histories are not assumed to synchronize.

## Operating loop

1. Read `PROJECT_STATE.md` when current implementation status matters.
2. Discuss concepts or design; clearly mark hypotheses and unknowns.
3. Give Codex a concrete goal, scope, safety boundary, and acceptance checks.
4. Require evidence: sources, diffs, commands, test output, or experiment records.
5. Review results critically in ChatGPT; do not treat AI output as fact.
6. Commit verified updates, including `PROJECT_STATE.md` and decisions when material.

## Handoff format

- **Goal:** observable outcome.
- **Context:** relevant files, standards, and verified state.
- **Constraints:** safety, scope, versions, and forbidden actions.
- **Acceptance:** exact checks/evidence needed.
- **State update:** files that must reflect completion.
