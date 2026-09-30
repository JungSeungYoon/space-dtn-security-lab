# Initial Threat Model

Status: template with candidate assumptions. Nothing here establishes a finding.

## Assets

- Bundle payload confidentiality and integrity.
- Correct routing, forwarding, storage, and delivery behavior.
- Node availability, CPU, memory, disk, and queue capacity.
- Configuration, contact plans, security policy, and cryptographic material.
- Experiment evidence and reproducibility.

## Trust Boundaries

- Network input to convergence-layer and BP processing.
- BP agent to applications and persistent storage.
- Administrative/control interfaces to node runtime.
- Security-source/verifier/acceptor roles and key stores.
- Host, WSL/container/VM, and analysis-tool boundaries.

## Adversaries

- **Candidate A:** On-path DTN participant able to observe, delay, replay, drop, or
  inject bundles.
- **Candidate B:** Connected but untrusted node able to submit syntactically valid
  or malformed protocol data.
- **Candidate C:** Local low-privilege actor within the testbed.

The selected adversary and authorization boundary are **TBD**.

## Candidate Attacker Capabilities

Bundle construction, timing/contact awareness, repeated submission, malformed CBOR
or blocks, and possibly legitimate endpoint participation. Credentials, key access,
host access, and traffic volume remain TBD and must be explicit per experiment.

## Defender Assumptions

- Experiments run only in a local or explicitly authorized isolated environment.
- Host controls and resource limits are available but not assumed correctly set.
- Cryptography is not treated as broken without evidence; configuration and policy
  failures remain valid study targets.

## Security Goals

Confidentiality where configured, integrity/authenticity according to policy,
availability under defined resource limits, safe malformed-input handling,
observable failures, and recoverable operation.

## Out of Scope

Operational spacecraft, ground stations, third-party networks, social engineering,
credential theft, destructive persistence, and uncoordinated public disclosure.

## Open Questions

- What exact attacker position and initial access are realistic and useful?
- Which node interfaces are exposed in the chosen topology?
- What are the resource and contact-plan baselines?
- Which BPSec policies and key-management assumptions apply?
- What distinguishes protocol-permitted disruption from security-relevant failure?
