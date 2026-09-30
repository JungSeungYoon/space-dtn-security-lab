# Source Register

Record authoritative sources before relying on them. “Verified facts” must be
narrowly attributable to the cited source; notes and hypotheses stay separate.

| Source | URL / identifier | Type | Accessed | Why relevant | Verified facts | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Bundle Protocol Version 7 | https://www.rfc-editor.org/rfc/rfc9171.html | IETF Standards Track RFC | 2026-10-01 | Normative BPv7 baseline | BPv7 bundle format uses CBOR; primary protocol version is 7 | RFC 9171 |
| Bundle Protocol Security | https://www.rfc-editor.org/rfc/rfc9172.html | IETF Standards Track RFC | 2026-10-01 | Normative BPSec baseline | Defines Block Integrity Block and Block Confidentiality Block | RFC 9172 |
| Default Security Contexts for BPSec | https://www.rfc-editor.org/rfc/rfc9173.html | IETF Standards Track RFC | 2026-10-01 | Standard security contexts | Defines the default BPSec security contexts referenced by RFC 9172 | RFC 9173 |
| Concise Binary Object Representation | https://www.rfc-editor.org/rfc/rfc8949.html | Internet Standard | 2026-10-01 | BPv7 serialization baseline | CBOR is a binary data format with deterministic-encoding guidance | RFC 8949 / STD 94 |
| DTN resources for mission developers | https://www.nasa.gov/technology/space-comms/delay-disruption-tolerant-networking-mission-resources/ | NASA documentation | 2026-10-01 | Official ION context | NASA describes ION as an implementation of DTN architecture developed by JPL | Verify software source/version separately |
| Codex config basics | https://learn.chatgpt.com/docs/config-file/config-basic | OpenAI documentation | 2026-10-01 | Project Codex setup | Project `.codex/config.toml` is loaded only for trusted projects | Settings remain subject to higher-priority requirements |
| Connecting GitHub to ChatGPT | https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt | OpenAI Help Center | 2026-10-01 | ChatGPT repository access | Authorized repositories are retrieved on demand; GitHub access is read-only for analysis | Availability depends on plan/product surface |
| Projects in ChatGPT | https://help.openai.com/en/articles/10169521-projects-in-chatgpt | OpenAI Help Center | 2026-10-01 | Project setup and chat continuity | Project instructions apply within a project; eligible chats can be moved into a project | UI availability can vary |
| NASA/JPL ION-DTN | https://github.com/nasa-jpl/ION-DTN | Official source repository | 2026-10-01 | Authoritative implementation source | Linux is supported; ION Open Source is the full research-oriented suite | Pin a release tag before analysis |
| ION Quick Start Guide | https://github.com/nasa-jpl/ION-DTN/blob/integration/site-docs/docs/quick-start-guide.md | Official build/run documentation | 2026-10-01 | Build dependencies and local topology support | Documents Automake prerequisites and `ionrun` loopback, 2-node, and 3-node workflows | Use documentation matching the pinned release |
| ION releases | https://github.com/nasa-jpl/ION-DTN/releases | Official release history | 2026-10-01 | Candidate baseline selection | `ion-open-source-4.2.0` is the current stable release shown | Record exact tag and commit when selected |

## Entry template

| Source | URL / identifier | Type | Date accessed | Why relevant | Verified facts | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| TBD | TBD | RFC / CCSDS / paper / NASA-JPL / source / issue / advisory | YYYY-MM-DD | TBD | TBD | Clearly label hypotheses |
