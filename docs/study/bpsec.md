# BPSec Study Notes

## What is it?

BPSec is the BP security-block framework specified by RFC 9172.

## Why does this project need it?

It provides the standards baseline for reasoning about bundle integrity and
confidentiality rather than assuming transport security covers DTN behavior.

## Key Concepts

- Block Integrity Block (BIB)
- Block Confidentiality Block (BCB)
- Security sources, verifiers, acceptors, targets, contexts, and policy

## Questions

- Which BPSec features and contexts does the selected ION version implement?
- How are keys and node policies configured in the testbed?

## Verified Facts

- RFC 9172 defines BIB and BCB security blocks.
- RFC 9172 leaves key management to network management rather than defining one
  universal key-management strategy.

## Sources

- https://www.rfc-editor.org/rfc/rfc9172.html
- https://www.rfc-editor.org/rfc/rfc9173.html

## Things I Still Do Not Understand

- ION-specific policy evaluation and failure handling.
