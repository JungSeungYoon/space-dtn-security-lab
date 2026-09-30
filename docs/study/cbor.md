# CBOR Study Notes

## What is it?

Concise Binary Object Representation is the binary data format standardized in
RFC 8949.

## Why does this project need it?

BPv7 bundles are encoded using CBOR, so correct parsing and canonicalization are
central to packet analysis and malformed-input reasoning.

## Key Concepts

- Major types and additional information
- Definite and indefinite-length items
- Deterministic encoding and canonical form

## Questions

- Which CBOR library and validation mode does the selected ION version use?
- Which non-preferred but valid encodings are accepted or normalized?

## Verified Facts

- RFC 8949 defines CBOR and deterministic-encoding guidance.
- RFC 9171 applies CBOR encoding requirements to BPv7 blocks.

## Sources

- https://www.rfc-editor.org/rfc/rfc8949.html
- https://www.rfc-editor.org/rfc/rfc9171.html

## Things I Still Do Not Understand

- ION's exact decode, allocation, and error-recovery paths.
