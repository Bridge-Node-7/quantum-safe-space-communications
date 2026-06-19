# Sample Smallsat Operator Assessment

## Quantum-Safe Space Communications Security Assessment

**Fictional Operator:** Asterion Orbital Analytics  
**Assessment Type:** Fictional sample for framework demonstration  
**Framework:** Quantum-Safe Space Communications  

## Executive Summary

Asterion Orbital Analytics is a fictional smallsat Earth-observation company operating six low-Earth-orbit satellites, one primary ground-station provider, a cloud-based mission-data pipeline, and multiple vendor-managed software and firmware dependencies.

The assessment finds Asterion at **Readiness Level 1: Aware**.

The decisive bottleneck is cryptographic visibility. Until Asterion knows where the crypto lives across its mission architecture, it cannot build a credible migration plan or make informed vendor requirements.

## Communications Map

| Link | Description | Mission Role | Initial Risk |
|---|---|---|---|
| Uplink | Mission control to satellite command channel | Command authority | High |
| Downlink | Satellite to ground station telemetry | Mission status and health | Medium |
| Payload Data Downlink | Imagery from satellite to ground station | Revenue-generating mission data | High |
| Ground Station to Cloud | Ground provider transfers data into cloud pipeline | Data processing and storage | High |
| Cloud to Customer Portal | Processed imagery delivered to customers | Customer access | Medium |
| Vendor Firmware Path | Satellite bus vendor provides firmware updates | Software and firmware trust | High |
| Mission Operations Login | Operators access dashboard through identity provider | Command and control access | High |
| Key Management Path | Keys managed through mixed internal and vendor systems | Trust foundation | High |

## Crypto Map

| System Area | Known Crypto | Unknowns | Quantum Relevance |
|---|---|---|---|
| Mission Control VPN | TLS 1.2 / 1.3 assumed | Exact cipher suites not documented | Possible RSA or ECC dependency |
| Ground Station Link | Vendor-managed encryption | Algorithms not disclosed | Hidden vendor exposure |
| Payload Data Transfer | Cloud TLS | Certificate chains not reviewed | Public-key dependency likely |
| Firmware Signing | Vendor-controlled signatures | Signing algorithm unknown | Critical if RSA or ECC |
| Secure Boot | Claimed by vendor | Evidence not provided | Trust-chain exposure |
| Identity Provider | MFA enabled | Backend crypto not reviewed | Operational access risk |
| Data at Rest | AES-256 claimed | Key-management details unknown | Symmetric crypto less exposed, key exchange still matters |

## Link Risk Matrix Snapshot

This sample uses `assessment/space-link-risk-matrix.md` to prioritize where the first evidence requests should go.

| Link ID | Link Name | Public-Key Dependency | HNDL Risk | Owner Assigned | Overall Risk | Recommended Action |
|---|---|---|---|---|---|---|
| SL-001 | Primary Command Uplink | Unknown | Medium | No | Critical | Assign owner, verify command-auth crypto, request vendor evidence |
| SL-002 | Firmware Update Path | Unknown | Low | Partial | Critical | Identify signing algorithm and secure-boot evidence |
| SL-003 | Payload Data Downlink | Likely | High | No | High | Map certificate chain and data-secrecy lifetime |
| SL-004 | Ground Station to Cloud | Likely | Medium | Partial | High | Verify TLS profile, key ownership, and provider roadmap |
| SL-005 | Customer Portal | Likely | Medium | Yes | Medium | Review certificate lifecycle and PQC support path |

## Vendor Evidence Gap List

This sample uses `assessment/vendor-questionnaire.md` to identify missing evidence.

| Vendor / System | Evidence Needed | Why It Matters | Priority |
|---|---|---|---|
| Satellite bus vendor | Firmware signing algorithm, secure-boot documentation, update process | Protects trust chain and command-adjacent software | High |
| Ground-station provider | Link encryption details, key ownership, crypto-agility roadmap | Determines hidden public-key exposure | High |
| Cloud provider | Certificate lifecycle and KMS roadmap | Supports migration planning and ownership | Medium |
| Identity provider | Authentication crypto and recovery process | Supports operator access assurance | Medium |

## Readiness Index Result

**Overall Level:** Level 1, Aware

Asterion leadership recognizes that quantum risk exists, but the organization has not yet completed the inventories, maps, vendor evidence collection, or ownership assignments required for readiness.

## Executive Brief Inputs

This sample feeds `assessment/executive-brief-template.md` with decision-ready material.

| Executive Question | Sample Answer |
|---|---|
| What is exposed? | Command authentication, firmware signing, vendor-managed link encryption, and long-lived mission data dependencies are not fully visible. |
| Why does it matter? | These areas affect command authority, update trust, data confidentiality, and future migration cost. |
| Who owns it? | Ownership is incomplete; the first 90 days must assign owners for command, firmware, vendor, cloud, and key-management paths. |
| What decision is needed now? | Approve a 90-day readiness sprint focused on crypto inventory, vendor evidence, and migration candidate selection. |

## Executive Decision Required

Approve a **90-Day Quantum-Safe Space Communications Readiness Sprint**.

## Success Criteria

By the end of 90 days, Asterion should have:

- Complete communications link map
- Cryptographic dependency register
- Vendor crypto evidence package
- Quantum exposure heat map
- Assigned owner matrix
- PQC migration candidate list
- Updated procurement requirements
- Executive decision memo

## Final Assessment Verdict

Asterion Orbital Analytics is not behind. It is early. The window to shape its cryptographic trust layer through procurement and vendor contracts is still open. Once the fleet grows and data sensitivity increases, that window narrows.

The decisive bottleneck is **cryptographic visibility**.

Until Asterion knows where the crypto lives, it cannot build a credible migration plan.

## Final Command

**Map the links. Find the crypto. Score the quantum risk. Assign the owner. Migrate the mission. Secure the space layer.**

## Related Templates

- `assessment/space-link-risk-matrix.md`
- `assessment/vendor-questionnaire.md`
- `assessment/executive-brief-template.md`
- `frameworks/pqc-migration-roadmap.md`
