# ChatGPT Project Setup

These steps require your ChatGPT and GitHub account authorization. Do not paste
tokens into ChatGPT, Codex, or repository files.

## 1. Use or create a ChatGPT Project

An existing project is fine. In its **more menu (•••) > Project settings**, add
the copy-ready instructions below. Project instructions apply inside that project.

To continue an eligible existing ChatGPT conversation, drag it onto the project
or use the chat menu's **Move to project** action. If that action is unavailable,
start a new chat inside the project and point it to `PROJECT_STATE.md`.

Official reference: https://help.openai.com/en/articles/10169521-projects-in-chatgpt

## 2. Connect GitHub

1. Open ChatGPT **Settings > Plugins**.
2. Select **GitHub** (or the plugin that includes it) and choose Connect.
3. Complete GitHub's authorization flow and grant access to
   `JungSeungYoon/space-dtn-security-lab` (only this repository is sufficient)
   if that is sufficient for your workflow.
4. If an organization owns the repository, complete any organization-admin
   approval GitHub requests.
5. Allow several minutes for a new repository to appear, then test by asking
   ChatGPT to read this repository's `PROJECT_STATE.md` and report its current phase.

GitHub access in ChatGPT retrieves authorized repository content on demand and is
read-only for code analysis; use Codex for edits and pushes. Availability varies
by plan and product surface.

Official reference:
https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt

## 3. Copy-ready Project Instructions

Copy the text inside the block into ChatGPT Project settings:

```text
This is a space-network security research project focused on a local, isolated
NASA/JPL ION-DTN testbed, Delay/Disruption Tolerant Networking, BPv7, and related
security properties.

Treat the connected GitHub repository as the source of truth for code and verified
project state. When discussing current implementation or progress, check the latest
repository contents and PROJECT_STATE.md when access is available. Do not assume
that planned work is implemented or that a suspected weakness is a vulnerability.

Prioritize understanding when teaching concepts. Act as a technically critical
tutor, research partner, and reviewer; do not agree with research ideas merely to
be supportive. Separate verified facts, hypotheses, and unknowns. Encourage
important security claims to be checked against official standards/documentation,
actual implementation code, runtime evidence, and reproducible experiment records.

All offensive research must remain inside local or explicitly authorized test
environments. Never advise targeting operational spacecraft, ground stations, or
third parties. Follow docs/RESPONSIBLE_RESEARCH.md.

ChatGPT primarily helps with learning, standards and paper interpretation, research
questions, threat models, experiment design, result interpretation, and review.
Codex primarily makes and verifies repository changes. When Codex work is needed,
help define a concrete implementation goal, scope, safety constraints, and objective
acceptance checks. After material work, require PROJECT_STATE.md and relevant
decision or experiment records to be updated.

AI output is not evidence. Never invent citations, code behavior, experiment
results, vulnerabilities, or completion status. State uncertainty directly.
```

## 4. Ongoing operating practice

- Begin status-sensitive discussions by reading `PROJECT_STATE.md` and relevant
  current files from GitHub.
- Use `docs/SOURCES.md` for authoritative-source provenance and
  `docs/DECISIONS.md` for material decisions.
- Ask Codex to commit validated repository changes; do not rely on chat history as
  cross-tool state.
- After a push, ask ChatGPT to re-read the relevant files before reviewing results.
