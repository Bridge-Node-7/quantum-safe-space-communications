# Crypto Inventory Template

## Purpose

This template identifies where cryptography lives across space communications systems.

The goal is to build enough visibility to support quantum-safe migration, vendor questioning, risk scoring, and executive decision-making.

**Core doctrine:**

No crypto inventory, no quantum readiness.  
No algorithm agility, no mission resilience.  
No owner, no migration.  
No secure command link, no trusted space mission.

## Inventory Fields

| Field | Description |
|---|---|
| Asset ID | Unique identifier for the system, link, component, or dependency |
| Asset / System Name | Name of the system being assessed |
| Segment | Space, ground, cloud, vendor, enterprise, customer, or mission operations |
| Mission Function | Command, telemetry, payload data, update path, identity, storage, customer delivery |
| Communication Link | Uplink, downlink, TT&C, inter-satellite, ground-to-cloud, cloud-to-customer, vendor path |
| Data Type | Command, telemetry, imagery, logs, keys, firmware, customer data, mission data |
| Mission Criticality | Low, Medium, High, Critical |
| Data Secrecy Lifetime | < 1 year, 1-5 years, 5-10 years, 10+ years |
| Current Key Exchange | RSA, ECDH, DH, PSK, unknown, other |
| Current Digital Signature | RSA, ECDSA, EdDSA, ML-DSA, SLH-DSA, unknown |
| Current Encryption | AES, ChaCha20, vendor-managed, unknown, other |
| TLS / VPN Dependency | TLS version, VPN type, cipher suite, certificate dependency |
| Certificate Authority | Internal CA, commercial CA, vendor CA, government CA, unknown |
| Certificate Lifetime | Duration and renewal process |
| Firmware Signing | Algorithm and signing authority |
| Secure Boot | Yes, No, Unknown |
| Key Storage | HSM, TPM, software keystore, cloud KMS, vendor-managed, unknown |
| Key Rotation | Manual, automatic, vendor-managed, unavailable, unknown |
| Revocation Capability | Yes, No, Unknown |
| Patchability | None, limited, moderate, full |
| On-Orbit Update Capability | Yes, No, Unknown, not applicable |
| Vendor Managed | Yes, No, Partial |
| Vendor Evidence Received | Yes, No, Partial |
| PQC Support Status | Unknown, planned, pilot, production, not supported |
| Hybrid Mode Available | Yes, No, Unknown |
| QKD / QRNG Relevance | None, future candidate, mission-justified, unknown |
| Harvest-Now Decrypt-Later Risk | Low, Medium, High, Critical |
| Command Integrity Risk | Low, Medium, High, Critical |
| Quantum Exposure Score | 0 to 5 |
| Migration Complexity | Low, Medium, High, Critical |
| Owner | Named accountable person |
| Evidence Source | Config file, vendor response, architecture diagram, certificate scan, code review, contract, SBOM |
| Recommended Action | Inventory, verify, replace, migrate, monitor, accept risk |
| Target Date | Date for closure |
| Decision Required | Executive, technical, vendor, budget, procurement, risk acceptance |

## All-Source Collection Method

Crypto discovery must be done through multiple evidence streams. Do not rely on a single source.

### Source 1: Architecture Diagrams

Identify links:

- Uplinks
- Downlinks
- TT&C
- Ground station paths
- Cloud paths
- Customer portals
- Vendor paths
- Software update paths

### Source 2: Network and Security Configurations

Identify deployed crypto:

- TLS versions
- VPN settings
- Cipher suites
- Certificates
- Public-key exchange
- Authentication protocols

### Source 3: Certificate Inventories

Identify public-key dependencies:

- RSA certificates
- ECC certificates
- Certificate authorities
- Expiration dates
- Renewal process
- Long-lived certificates
- Vendor-issued certificates

### Source 4: Firmware and Secure Boot Evidence

Identify trust-chain risk:

- Firmware signing algorithms
- Secure boot design
- Update authority
- Rollback protection
- Emergency update process
- Signing-key storage

### Source 5: Vendor Questionnaires

Uncover hidden dependencies:

- Algorithms used
- RSA / ECC usage
- Firmware signing
- PQC roadmap
- Hybrid mode support
- Key control
- Upgrade limitations

### Source 6: Cloud and Identity Systems

Map operational access:

- Cloud KMS
- IAM
- MFA
- API authentication
- Service accounts
- Customer portal certificates
- Data-at-rest encryption
- Key rotation

### Source 7: Procurement and Contracts

Force future readiness:

- Crypto-agility language
- PQC roadmap requirements
- Vendor disclosure clauses
- SBOM / HBOM requirements
- Update support period
- Security evidence rights
- Risk acceptance terms

## Crypto Exposure Scoring

| Score | Meaning |
|---:|---|
| 0 | No evidence |
| 1 | Known system, unknown crypto |
| 2 | Crypto identified, quantum exposure unclear |
| 3 | Vulnerable crypto identified, owner assigned |
| 4 | Migration path defined |
| 5 | Quantum-safe or crypto-agile with evidence |

## Priority Rules

### Highest Priority

- Command authentication
- Firmware signing
- Secure boot
- Key management
- Ground station access
- Mission control VPN
- Vendor-managed crypto
- Long-lived sensitive mission data

### Medium Priority

- Customer portals
- Internal dashboards
- Standard cloud TLS
- Data-at-rest encryption
- Analytics pipelines

### Lower Priority

- Non-sensitive short-lifetime data
- Public data portals
- Systems with no public-key dependency
- Systems already crypto-agile with evidence

## Executive Outputs

A completed crypto inventory should produce these five deliverables:

1. **Crypto Dependency Register**: Master list of all cryptographic systems and dependencies.
2. **Quantum Exposure Heat Map**: Visual scoring of risk across the mission architecture.
3. **Top 10 Crypto Unknowns**: Highest-priority visibility gaps.
4. **Vendor Evidence Gap List**: Specific items requiring vendor disclosure.
5. **PQC Migration Candidate List**: Systems prioritized for post-quantum migration.

Find every link.  
Find every certificate.  
Find every key exchange.  
Find every signature.  
Find every vendor dependency.  
Find every owner.  
Find every missing evidence point.

Then score the risk.  
Then migrate the mission.

**Map the links. Find the crypto. Score the quantum risk. Assign the owner. Migrate the mission. Secure the space layer.**
