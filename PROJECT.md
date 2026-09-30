# Project Definition

## Overview

**Project name:** Space DTN Security Lab. This is a three-month personal
research project centered on a virtual NASA/JPL ION-DTN testbed and the security
properties of DTN and BPv7.

## Purpose

Develop practical understanding through standards study, source analysis,
instrumented execution, threat modeling, packet analysis, controlled experiments,
root-cause analysis, and quantitative evaluation.

## Current research topic

ION-DTN-based virtual space networking, BPv7 behavior, and security-relevant
protocol and implementation boundaries. BPSec and CBOR are supporting areas.

## Why ION-DTN and BPv7

- ION is a NASA/JPL-developed implementation of DTN architecture and is suitable
  as a concrete implementation for source and runtime study.
- BPv7 is standardized in RFC 9171 and encodes bundles using CBOR, giving the
  project an explicit protocol specification against which behavior can be checked.
- This selection does not imply that ION-DTN contains a vulnerability.

## Success criteria

- A reproducible, isolated multi-node testbed.
- Evidence-backed understanding of key BPv7/ION-DTN data and control paths.
- A documented threat model and prioritized attack surface.
- At least one rigorously designed and repeatable security experiment.
- Root-cause and mitigation analysis for any observed failure or weakness.
- Quantitative evaluation appropriate to the selected research question.
- Clear separation of verified facts, hypotheses, and unknowns.

## Stretch goals

- Protocol-aware fuzzing infrastructure.
- A responsibly handled new vulnerability, if evidence supports one.
- An upstream-quality patch and regression test.

None of these stretch goals is required for project success.

## Current scope

- Local/virtual DTN nodes and intermittent-connectivity scenarios.
- BPv7, BPSec, CBOR, ION-DTN internals, debugging, tracing, and packet analysis.
- Candidate replay, resource-exhaustion, malformed-input, and fuzzing studies
  after threat modeling and environment setup.

## Out of scope

- Operational spacecraft or ground-station access.
- Testing third-party networks without explicit authorization.
- Claiming or publishing vulnerabilities without reproduction and impact review.
- Building every candidate direction listed above.

## Undecided

- License.
- Final primary research question and attacker capabilities.
- Exact testbed topology, ION-DTN version, and host/container strategy.
- Which candidate attack or defense questions will be implemented.
