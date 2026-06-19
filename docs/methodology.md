# Methodology

## Purpose

This methodology explains how the Quantum-Safe Space Communications Security Assessment turns quantum-era cryptographic risk into an evidence-based decision package.

The goal is to help space operators, aerospace teams, ground-station providers, space-data organizations, research programs, and mission-network owners move from uncertainty to action.

## Assessment Logic

The assessment follows seven modules:

1. Communications Inventory
2. Cryptographic Dependency Map
3. Quantum Exposure Assessment
4. PQC Migration Readiness
5. QKD Feasibility
6. Governance and Ownership
7. Executive Decision Package

Each module produces an output that feeds the next decision.

## Evidence Standard

The framework uses evidence from multiple sources. Do not rely on self-declaration alone.

Preferred evidence sources include:

- architecture diagrams
- network configurations
- certificate inventories
- cryptographic libraries
- firmware signing documentation
- secure boot documentation
- HSM or key management records
- vendor questionnaires
- procurement language
- SBOM or HBOM materials
- cloud KMS records
- identity and access management records
- system owner interviews
- test results
- red-team or tabletop findings

## Module 1: Communications Inventory

Map the mission communication layer.

Include:

- uplinks
- downlinks
- TT&C
- inter-satellite links
- ground station paths
- mission operations paths
- software update paths
- vendor paths
- cloud paths
- customer delivery paths
- key management paths

Primary output:

Space Communications Link Map

## Module 2: Cryptographic Dependency Map

Find where cryptography lives.

Use `assessment/crypto-inventory-template.md` to capture:

- key exchange
- digital signatures
- encryption
- TLS and VPN dependencies
- certificate authorities
- firmware signing
- secure boot
- key storage
- key rotation
- revocation capability
- patchability
- vendor ownership
- PQC support status
- hybrid mode availability

Primary output:

Crypto Dependency Register

## Module 3: Quantum Exposure Assessment

Score each asset or link for quantum-era exposure.

Consider:

- RSA or ECC dependency
- data secrecy lifetime
- harvest-now, decrypt-later exposure
- command integrity consequences
- mission criticality
- key rotation capability
- patchability
- vendor dependence
- operational exposure
- implementation security

Primary output:

Quantum Exposure Heat Map

## Module 4: PQC Migration Readiness

Assess the ability to migrate to post-quantum cryptography.

Evaluate:

- crypto-agility
- protocol compatibility
- embedded system constraints
- bandwidth impact
- certificate lifecycle management
- vendor roadmap maturity
- hybrid mode readiness
- test environment availability
- procurement requirements

Primary output:

PQC Migration Roadmap

## Module 5: QKD Feasibility

Evaluate whether Quantum Key Distribution or related quantum communication methods are mission-justified.

Assess:

- link geometry
- optical terminal maturity
- pointing, acquisition, and tracking requirements
- atmospheric conditions
- key-rate requirements
- SWaP constraints
- trusted-node assumptions
- ground station availability
- cost and operational complexity
- mission value

Primary output:

QKD Feasibility Decision Memo

## Module 6: Governance and Ownership

Assign accountability.

Every major gap should have:

- risk owner
- system owner
- mission owner
- crypto owner
- vendor owner
- budget owner
- migration authority
- risk acceptance authority
- target date

Primary output:

Quantum-Safe Ownership Matrix

## Module 7: Executive Decision Package

Convert technical evidence into executive action.

Include:

- current risk state
- readiness score
- top risks
- top unknowns
- 90-day actions
- budget categories
- owner matrix
- vendor decisions
- standards alignment
- residual risk
- decision required

Primary output:

Executive Quantum-Safe Space Communications Brief

## Readiness Index

The readiness index uses a Level 0 to Level 5 scale:

| Level | Name | Meaning |
|---|---|---|
| 0 | Unknown | No inventory, no crypto map, no assigned owners |
| 1 | Aware | Leadership recognizes quantum risk, but dependencies remain unmapped |
| 2 | Mapped | Communications links, cryptography, vendors, and data flows are documented |
| 3 | Migration-Ready | PQC candidates, hybrid strategy, test plans, and procurement requirements are defined |
| 4 | Quantum-Resilient | PQC is deployed across priority ground systems and planned for space systems |
| 5 | Quantum-Safe Architecture | PQC, selective QKD, QRNG, secure boot, key management, vendor assurance, and governance operate as one architecture |

## Scoring Guidance

Use scores as decision support, not as false precision.

For each area, document:

- score
- evidence
- uncertainty
- owner
- recommended action
- target date

## Priority Rule

Fix first:

1. command authentication
2. firmware signing
3. secure boot
4. key management
5. ground station access
6. mission control VPN
7. vendor-managed crypto
8. long-lived sensitive mission data

## Executive Rule

Leaders need the next decision, not a technical fog bank.

Every assessment should answer:

- What is exposed?
- Why does it matter?
- Who owns it?
- What must happen in 90 days?
- What decision is required now?

## Final Command

**Map the links. Find the crypto. Score the quantum risk. Assign the owner. Migrate the mission. Secure the space layer.**
