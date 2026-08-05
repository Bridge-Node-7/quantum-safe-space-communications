# Quantum Readiness for Space Communications Assessment

## Purpose

This assessment organizes the evidence needed to build a **Quantum Readiness Decision Pack** for spacecraft, links, ground systems, mission operations, software and firmware trust paths, PKI and certificate dependencies, vendors, and recovery processes.

## Required sequence

1. Define scope, accountable owner, boundaries, and exclusions.
2. Build the system and communications-link map.
3. Inventory algorithms, protocols, certificates, libraries, firmware, key stores, signing paths, and vendor dependencies.
4. Record Quantum Exposure Severity, preserving `Unknown / Not Assessed`.
5. Complete the ten-domain Migration Readiness Profile.
6. Record Evidence Confidence and Coverage.
7. Evaluate all twelve Critical Risk Overrides.
8. Assign owners, resources, actions, dates, and escalation paths.
9. Build the migration roadmap and recovery plan.
10. Assemble, approve, and retain the Quantum Readiness Decision Pack.

## Minimum scope categories

- Spacecraft and payload systems
- Uplink, downlink, crosslink, relay, and tracking paths
- Ground stations, networks, cloud, and mission operations
- PKI, certificates, authentication, key establishment, signing, secure boot, and update paths
- Software, firmware, libraries, hardware roots of trust, and recovery mechanisms
- Vendors, integrators, service providers, and support lifecycles
- Testing, interoperability, rollback, contingency, and incident recovery
- Ownership, funding, staffing, schedule, procurement, and governance

## Quality rules

- Unknown is never converted to Not Applicable or Low.
- Exposure, readiness, evidence, and critical conditions remain separate.
- No weighted readiness total is produced.
- Critical conditions cannot be averaged away.
- Every material statement cites evidence or is marked unsupported.
- Every critical item has an owner, action, date, and decision authority.
- The package states limitations and reassessment triggers.

Use [Assessor Guide](../docs/assessor-guide.md) and [Known Limitations](../KNOWN_LIMITATIONS.md).
