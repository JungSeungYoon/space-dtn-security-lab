# DTN Study Notes

## What is it?

Delay/Disruption Tolerant Networking supports communication where end-to-end
paths may be delayed, intermittent, or unavailable; nodes can retain data until
a forwarding opportunity exists.

## Why does this project need it?

It is the architectural context for ION and the network conditions this project
intends to emulate.

## Key Concepts

- Store-and-forward operation
- Scheduled/intermittent contacts
- Persistent storage and custody/reliability assumptions (**details TBD**)

## Questions

- Which DTN architecture requirements does the selected ION version implement?
- Which resource assumptions matter most under long disruptions?

## Verified Facts

- NASA describes DTN nodes as storing data across communication disruptions.
- NASA describes ION as an implementation of DTN architecture developed by JPL.

## Sources

- https://www.nasa.gov/communicating-with-missions/delay-disruption-tolerant-networking/
- https://www.nasa.gov/technology/space-comms/delay-disruption-tolerant-networking-mission-resources/

## Things I Still Do Not Understand

- Precise ION routing/contact-plan behavior and operational constraints.
