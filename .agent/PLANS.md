# ExecPlans

Use an ExecPlan for multi-hour debugging, cross-cutting implementation,
testbed construction, fuzzing infrastructure, or work that must survive context
loss. Do not create one for routine edits.

An active plan lives at `.agent/plans/<short-name>.md` and is updated as work
progresses. It must be understandable without chat history and contain:

1. **Outcome** — observable result and acceptance checks.
2. **Context** — relevant files, constraints, and verified starting state.
3. **Scope** — in-scope and explicitly out-of-scope work.
4. **Steps** — ordered, independently verifiable milestones.
5. **Progress** — timestamped completed/current/remaining items.
6. **Decisions and discoveries** — evidence and consequences.
7. **Validation** — exact commands and expected evidence.
8. **Recovery** — how to resume safely after interruption.

Keep the plan current, concise, and committed with the work it describes.
