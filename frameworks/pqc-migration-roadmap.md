# PQC Migration Roadmap

## Purpose

This roadmap helps space organizations plan migration from quantum-vulnerable public-key cryptography to post-quantum cryptography.

It is designed for satellite operators, aerospace companies, ground-station providers, mission-infrastructure providers, mission-network owners, and space-data organizations.

## Migration Principle

PQC migration is not only an algorithm swap.

It is a mission assurance program involving:

- inventory
- evidence
- standards alignment
- vendor engagement
- test planning
- architecture modernization
- procurement language
- ownership
- executive decisions
- long-term governance

## Phase 0: Establish Governance

Timeframe: 0 to 30 days

Actions:

- assign executive sponsor
- assign crypto migration owner
- assign mission owner
- assign vendor owner
- create migration working group
- define decision authority
- define risk acceptance authority
- define reporting cadence

Outputs:

- owner matrix
- migration charter
- decision log
- initial risk register

## Phase 1: Build Crypto Inventory

Timeframe: 0 to 90 days

Actions:

- map all communication links
- find all certificates
- identify key exchange methods
- identify digital signature algorithms
- identify firmware signing dependencies
- identify secure boot dependencies
- identify VPN and TLS dependencies
- identify key storage and key rotation
- identify vendor-managed cryptography
- identify update and patch constraints

Primary tool:

`assessment/crypto-inventory-template.md`

Outputs:

- crypto dependency register
- top 10 crypto unknowns
- vendor evidence gap list
- command integrity exposure list
- harvest-now, decrypt-later exposure list

## Phase 2: Prioritize Quantum Exposure

Timeframe: 60 to 120 days

Actions:

- score mission criticality
- score data secrecy lifetime
- identify RSA and ECC dependencies
- identify command-link exposure
- identify long-lived data exposure
- identify unpatchable systems
- identify vendor-managed risk
- identify early migration candidates

Outputs:

- quantum exposure heat map
- priority migration list
- risk acceptance candidates
- executive exposure brief

## Phase 3: Define Migration Strategy

Timeframe: 90 to 180 days

Actions:

- select PQC candidate use cases
- define hybrid transition strategy
- identify systems suitable for ground-segment pilots
- define certificate lifecycle changes
- update procurement requirements
- update vendor questionnaires
- plan performance testing
- plan rollback and recovery
- identify standards dependencies

Outputs:

- PQC migration roadmap
- hybrid architecture plan
- test plan
- procurement language
- vendor roadmap request

## Phase 4: Run Ground-Segment Pilots

Timeframe: 6 to 18 months

Actions:

- test PQC key establishment in nonflight environments
- test PQC signatures for software and firmware workflows
- evaluate bandwidth and latency impact
- evaluate embedded processing impact
- test hybrid TLS or VPN pathways where applicable
- validate logging and monitoring
- validate rollback procedures
- document operational lessons

Outputs:

- pilot report
- performance results
- implementation constraints
- updated migration roadmap
- go or no-go decision memo

## Phase 5: Extend to Mission Systems

Timeframe: 12 to 36 months

Actions:

- migrate priority ground systems
- update secure update workflows
- update key management systems
- update certificate authority processes
- deploy hybrid protections where feasible
- coordinate with vendors
- plan for future flight system integration
- require crypto-agility in new acquisitions

Outputs:

- migrated priority systems
- updated operational procedures
- vendor compliance evidence
- updated risk score
- readiness level improvement

## Phase 6: Institutionalize Crypto-Agility

Timeframe: ongoing

Actions:

- require crypto-agility in all new acquisitions
- maintain crypto inventory
- review vendor roadmaps annually
- track NIST, CISA, and CCSDS guidance
- conduct periodic tabletop exercises
- integrate PQC readiness into risk governance
- update executive brief quarterly or annually

Outputs:

- continuous crypto inventory
- annual quantum readiness review
- updated readiness index score
- board-level reporting
- sustained mission resilience

## Priority Migration Targets

Fix first:

1. command authentication
2. TT&C authentication
3. software and firmware signatures
4. secure boot
5. key management
6. mission control VPN
7. ground station access
8. vendor-managed crypto
9. long-lived sensitive mission data
10. cloud KMS and identity pathways

## Standards Alignment

Use current official guidance as the baseline.

Important reference families include:

- NIST FIPS 203, ML-KEM
- NIST FIPS 204, ML-DSA
- NIST FIPS 205, SLH-DSA
- CISA and NIST quantum-readiness guidance
- CCSDS space data security guidance and profiles where applicable

## Vendor Requirements

Ask vendors:

- Which systems use RSA?
- Which systems use ECC?
- Which systems use DH or ECDH?
- What signs firmware?
- What protects secure boot?
- Who controls keys?
- Can algorithms be replaced?
- Is hybrid PQC supported?
- What is the PQC roadmap?
- What cannot be upgraded?
- What evidence can be provided?
- What support period is guaranteed?

## Migration Evidence

A migration is not complete without evidence.

Evidence may include:

- configuration records
- test results
- certificate inventory
- vendor attestation
- architecture diagram
- change records
- key management logs
- secure boot documentation
- firmware signing documentation
- procurement language
- risk acceptance record

## Executive Rule

Do not ask leaders to approve "PQC migration" in the abstract.

Ask for specific decisions:

- approve crypto inventory
- approve vendor evidence request
- approve PQC pilot
- approve procurement language
- approve budget category
- approve risk owner
- approve risk acceptance or remediation

Inventory first.
Pilot second.
Migrate third.
Govern always.

## Final Command

Map every link. Find every crypto dependency. Score every risk. Assign every owner. Migrate the mission. Govern always.
