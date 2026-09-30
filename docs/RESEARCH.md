# Research Framework

## Primary Research Question

**TBD.** Candidate: How do BPv7 and ION-DTN behave under security-relevant,
disruption-tolerant network conditions, and which controls measurably improve
resilience without unacceptable operational cost?

This is a candidate framing, not a finalized question.

## Secondary Questions

- Which trust boundaries and parser/resource-management paths dominate the attack
  surface of the selected ION-DTN version?
- How do intermittent contacts change detection, replay, recovery, and resource
  exhaustion assumptions?
- Which BPv7/BPSec requirements are enforced by implementation, policy, or neither?
- Which observable metrics distinguish expected DTN behavior from unsafe failure?

## Hypotheses

All items below are **Hypothesis / Unverified** until tested:

- Intermittent connectivity can amplify storage and queue-management pressure.
- Protocol-aware malformed inputs may reach materially different paths than random
  byte mutation.
- Security controls may trade resilience for bandwidth, latency, CPU, or storage.

## Candidate Metrics

- Bundle delivery ratio and end-to-end delay.
- Queue depth, retained bytes, memory, CPU, and disk use.
- Processing failures, drops, restarts, sanitizer findings, and recovery time.
- BPSec verification success/failure and policy outcomes.
- Fuzzing executions, path/coverage proxy, unique reproducible failures, and
  minimization rate.

Metric definitions, units, collection methods, and baselines remain TBD.

## Research Phases

1. Foundations and authoritative-source study.
2. Reproducible isolated testbed design and construction.
3. Implementation mapping, tracing, and baseline measurement.
4. Threat model and attack-surface prioritization.
5. Selected experiments with controlled variables.
6. Root-cause, mitigation, regression, and performance evaluation.
7. Reporting and, if needed, responsible disclosure.

## Unknowns

- Final ION-DTN version and supported BPv7/BPSec feature set.
- Testbed runtime (WSL, containers, VMs, or a minimal combination).
- Attacker position, credentials, protocol knowledge, and resource limits.
- Primary experiment and statistically appropriate repetitions.

## Validation Requirements

- Prefer standards/official documentation, implementation code, runtime evidence,
  then recorded experiment results.
- Preserve versions, configuration, commands, inputs, timestamps, and artifact hashes.
- Separate expected protocol behavior, implementation defects, security impact, and
  operational tradeoffs.
- Reproduce suspected failures and establish root cause before vulnerability language.
- Compare against a baseline and state uncertainty and limitations.

## Stretch Goals

Protocol-aware fuzzing, an upstream-quality patch, or a responsibly disclosed new
vulnerability. None is required for project success.
