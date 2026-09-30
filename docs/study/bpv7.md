# BPv7 Study Notes

## What is it?

Bundle Protocol Version 7 is the delay-tolerant networking protocol specified by
RFC 9171.

## Why does this project need it?

It defines the bundle structure and processing baseline against which ION-DTN
behavior and test inputs can be analyzed.

## Key Concepts

- Primary block, canonical blocks, and payload block
- Endpoint IDs, creation time, lifetime, extension blocks, and processing flags
- CBOR bundle encoding

## Questions

- Where does ION parse and validate each BPv7 block?
- Which optional extension blocks and error paths does the selected version support?

## Verified Facts

- RFC 9171 requires a bundle to contain exactly one primary block and exactly one
  payload block.
- BPv7 bundle format uses CBOR.

## Sources

- https://www.rfc-editor.org/rfc/rfc9171.html

## Things I Still Do Not Understand

- Exact forwarding and deletion behavior under each relevant flag and policy.
