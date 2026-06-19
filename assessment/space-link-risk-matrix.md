# Space Link Risk Matrix

## Purpose

This matrix helps assess quantum-era cybersecurity risk across space communications links.

It converts link type, mission function, cryptographic dependency, data sensitivity, command integrity, vendor exposure, and update capability into a practical risk view.

## Core Doctrine

No secure command link, no trusted space mission.

## Risk Rating Scale

| Rating | Meaning |
|---|---|
| Low | Limited mission impact, short data lifetime, crypto known, migration path clear |
| Medium | Meaningful exposure, some uncertainty, owner identified, migration possible |
| High | Mission-critical exposure, quantum-vulnerable public-key dependency, limited evidence or difficult migration |
| Critical | Command integrity, safety, mission-critical, or long-lived sensitive data at risk with no clear owner or migration path |

## Link Categories

| Link Type | Description | Typical Risk Concern |
|---|---|---|
| Uplink | Ground to spacecraft or satellite command path | command spoofing, unauthorized injection, authentication failure |
| Downlink | Spacecraft or satellite to ground path | long-lived mission data exposure, telemetry protection |
| TT&C | Telemetry, tracking, and command link | mission control integrity, availability, authentication |
| Inter-Satellite Link | Cross-link between spacecraft | relay trust, key management, propagation of compromise |
| Ground Station to Mission Operations | Ground segment to mission control systems | VPN, TLS, identity, access control, vendor pathways |
| Ground Station to Cloud | Ground infrastructure to cloud environment | cloud KMS, API authentication, certificate lifecycle |
| Vendor Path | Supplier or managed service access | hidden crypto, vendor-managed keys, evidence gaps |
| Software Update Path | Firmware or software update chain | signing keys, secure boot, rollback protection |
| Customer Delivery Path | Data delivery to external users | TLS, API auth, customer portal certificates |

## Risk Matrix Fields

| Field | Description |
|---|---|
| Link ID | Unique identifier |
| Link Name | Human-readable link name |
| Link Type | Uplink, downlink, TT&C, inter-satellite, ground-cloud, vendor, update path |
| Mission Function | Command, telemetry, payload data, update, identity, storage |
| Data Type | Command, telemetry, imagery, logs, keys, firmware, mission data |
| Mission Criticality | Low, Medium, High, Critical |
| Data Secrecy Lifetime | Less than 1 year, 1 to 5 years, 5 to 10 years, 10+ years |
| Current Crypto Known | Yes, No, Partial |
| Public-Key Dependency | RSA, ECC, DH, ECDH, PSK, unknown, other |
| Command Integrity Impact | Low, Medium, High, Critical |
| Harvest-Now Decrypt-Later Risk | Low, Medium, High, Critical |
| Patchability | None, limited, moderate, full |
| Vendor Managed | Yes, No, Partial |
| Owner Assigned | Yes, No |
| Evidence Quality | Low, Medium, High |
| PQC Migration Path | Unknown, planned, pilot, active, complete |
| QKD Relevance | None, possible, mission-justified, not assessed |
| Overall Risk | Low, Medium, High, Critical |
| Recommended Action | Inventory, verify, migrate, monitor, accept risk, escalate |
| Target Date | Closure date |
| Decision Required | Technical, vendor, budget, executive, risk acceptance |

## Risk Scoring Guide

Score each category from 0 to 5.

| Area | Score 0 | Score 5 |
|---|---|---|
| Mission Criticality | noncritical | mission-critical or safety-critical |
| Quantum-Vulnerable Crypto | no public-key dependency | RSA or ECC dependency confirmed |
| Data Lifetime | short-lived public data | sensitive for 10+ years |
| Command Integrity Impact | no command role | unauthorized command could cause mission loss |
| Patchability | fully updateable | no update path |
| Vendor Dependence | no vendor dependence | vendor-managed hidden crypto |
| Evidence Quality | strong verified evidence | no evidence |

## Suggested Overall Risk Mapping

| Average Score | Overall Risk |
|---|---|
| 0.0 to 1.4 | Low |
| 1.5 to 2.4 | Medium |
| 2.5 to 3.9 | High |
| 4.0 to 5.0 | Critical |

## Highest Priority Links

Review these first:

1. command uplinks
2. TT&C links
3. software and firmware update paths
4. ground station access paths
5. mission control VPNs
6. vendor-managed access paths
7. long-lived mission data downlinks
8. inter-satellite key relay paths

## Example Row

| Link ID | Link Name | Link Type | Mission Function | Current Crypto Known | Public-Key Dependency | HNDL Risk | Owner Assigned | Overall Risk | Recommended Action |
|---|---|---|---|---|---|---|---|---|---|
| SL-001 | Primary Command Uplink | Uplink | Command | Partial | ECC | High | No | Critical | Assign owner, verify crypto, define PQC migration path |

## Executive Output

A completed link matrix should support:

- top 5 highest-risk links
- top 10 evidence gaps
- command integrity exposure summary
- harvest-now, decrypt-later exposure summary
- vendor-managed risk summary
- 90-day mitigation priorities
- executive decisions required

## Final Command

Map every link.
Find every crypto dependency.
Score every risk.
Assign every owner.
Secure the mission.
