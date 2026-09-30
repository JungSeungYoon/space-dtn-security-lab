# Decision Log

Record decisions that materially affect research validity, architecture, safety,
or reproducibility. Do not record routine edits.

## 2026-10-01 — Name and publish the bootstrap repository

- **Decision:** Use `Space DTN Security Lab`, GitHub slug
  `space-dtn-security-lab`, and public visibility. The name may be changed later.
- **Context:** The bootstrap needs a stable repository and shareable source of truth.
- **Alternatives:** Delay creation; use a private repository; choose a narrower name.
- **Reasoning:** The broad name preserves research flexibility, and public visibility
  supports transparent learning and reproducibility.
- **Consequences:** Review every commit for secrets and disclosure-sensitive material;
  rename repository references together if the project name changes.

## 2026-10-01 — Repository as cross-tool source of truth

- **Decision:** Store verified state, decisions, code, and experiment records in Git.
- **Context:** ChatGPT and Codex conversation histories are not assumed to be shared.
- **Alternatives:** Depend on chat history or duplicate notes manually.
- **Reasoning:** Versioned files provide reviewable, durable shared context.
- **Consequences:** Material work must update `PROJECT_STATE.md` and related records.

## 2026-10-01 — Defer license selection

- **Decision:** Do not add a license during bootstrap.
- **Context:** License selection requires explicit user choice and may interact with
  future third-party code or disclosure constraints.
- **Alternatives:** Select a permissive license now.
- **Reasoning:** Avoid an irreversible or poorly informed legal choice.
- **Consequences:** The repository has no granted reuse license until one is chosen.
