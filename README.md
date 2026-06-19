# Quantum-Safe Space Communications

**Public-safe assessment and migration-planning templates for post-quantum cryptography readiness in space communications.**

## Mission

Long-lived space communications systems depend on cryptography that may need to survive for years or decades. Post-quantum cryptography migration is not only an algorithm swap; it requires inventory, ownership, testing, vendor engagement, risk scoring, and clear executive decisions.

**Quantum-Safe Space Communications** helps teams:

- Map space communications links and cryptographic dependencies
- Identify RSA, ECC, Diffie-Hellman, certificate, signing, and key-management exposure
- Score quantum-era risk using evidence, not assumptions
- Prioritize command authentication, firmware signing, secure boot, and key management
- Plan migration toward NIST-standardized post-quantum cryptography
- Evaluate whether QKD or QRNG concepts are mission-relevant without treating them as universal replacements for PQC
- Produce executive-ready decision materials

## What This Is

A defensive governance and assessment toolkit for satellite operators, smallsat teams, ground-station providers, aerospace cybersecurity teams, research programs, space-data organizations, product teams, and reviewers preparing for quantum-era cybersecurity risk.

This repository focuses on **post-quantum readiness, cryptographic visibility, migration planning, evidence, and ownership**.

This toolkit is **Quantum-Safe Space Communications**. Its primary assessment instrument is the **Quantum-Safe Space Communications Security Assessment**.

## What This Is Not

This repository does **not** certify that any system is quantum-safe.

It does **not** provide cryptographic implementations, operational testing authority, exploit instructions, live-system targeting guidance, private mission data, regulated technical data, or production deployment approval.

It is a documentation and workflow foundation for defensive assessment and planning.

## Quick Start

Start with the assessment, then build the evidence package.

1. Read `assessment/quantum-safe-space-communications-assessment.md`.
2. Use `assessment/crypto-inventory-template.md` to find cryptographic dependencies.
3. Use `assessment/vendor-questionnaire.md` to collect vendor evidence.
4. Use `assessment/readiness-index.md` to score current readiness.
5. Use `assessment/space-link-risk-matrix.md` to prioritize link-level risk.
6. Use `frameworks/pqc-migration-roadmap.md` to plan migration.
7. Use `briefings/90-day-action-plan-template.md` to turn findings into action.
8. Use `assessment/executive-brief-template.md` to prepare the decision package.
9. Review `examples/sample-smallsat-operator-assessment.md` for a fictional example.

**First action for most users:** open `assessment/crypto-inventory-template.md` and identify where cryptography is used before making any readiness claim.

## Assessment Flow

```text
Communications Inventory
        |
Cryptographic Dependency Map
        |
Quantum Exposure Assessment
        |
PQC Migration Readiness
        |
QKD / QRNG Feasibility
        |
Governance and Ownership
        |
Executive Decision Package
```

## Repository Structure

```text
quantum-safe-space-communications/
├── README.md
├── LICENSE
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── DISCLAIMER.md
├── SECURITY.md
├── RELEASE_REVIEW.md
├── REPO_MANIFEST.json
├── assessment/
│   ├── crypto-inventory-template.md
│   ├── executive-brief-template.md
│   ├── quantum-safe-space-communications-assessment.md
│   ├── readiness-index.md
│   ├── space-link-risk-matrix.md
│   └── vendor-questionnaire.md
├── briefings/
│   └── 90-day-action-plan-template.md
├── docs/
│   ├── glossary.md
│   ├── methodology.md
│   └── references.md
├── examples/
│   └── sample-smallsat-operator-assessment.md
└── frameworks/
    └── pqc-migration-roadmap.md
```

## Core Modules

### 1. Assessment

`assessment/quantum-safe-space-communications-assessment.md`

Defines the full assessment flow: communications inventory, cryptographic dependency mapping, quantum exposure assessment, PQC migration readiness, QKD / QRNG feasibility, governance, and executive decision package.

### 2. Crypto Inventory

`assessment/crypto-inventory-template.md`

Captures where cryptography lives across communication links, command paths, certificates, firmware signing, secure boot, key management, vendors, and update paths.

### 3. Readiness Index

`assessment/readiness-index.md`

Provides a 0 to 5 evidence-based readiness model from Unknown to Quantum-Safe Architecture.

### 4. Link Risk Matrix

`assessment/space-link-risk-matrix.md`

Scores link-level risk across command, telemetry, mission data, inter-satellite, ground-station, cloud, vendor, and update paths.

### 5. PQC Migration Roadmap

`frameworks/pqc-migration-roadmap.md`

Defines a practical migration path from inventory to governance, pilots, procurement requirements, vendor engagement, and long-term crypto agility.

### 6. Executive Brief

`assessment/executive-brief-template.md`

Turns technical findings into decision-ready executive materials.

### 7. Vendor Questionnaire

`assessment/vendor-questionnaire.md`

Helps teams ask vendors about cryptographic dependencies, PQC readiness, hybrid modes, certificates, signing, update paths, and evidence.

### 8. Example Assessment

`examples/sample-smallsat-operator-assessment.md`

Shows the framework applied to a fictional smallsat operator with no real mission or customer data.

## Technical Reference Points

This repository aligns to public guidance and standards around:

- NIST FIPS 203: ML-KEM
- NIST FIPS 204: ML-DSA
- NIST FIPS 205: SLH-DSA
- NIST and CISA post-quantum migration guidance
- CCSDS space data link security references
- crypto-agility, cryptographic inventory, and evidence-based migration planning

See `docs/references.md`.

## Public-Safe Use

Use fictional examples unless you have explicit permission to publish real information.

Do not publish:

- credentials
- private keys
- tokens
- real mission data
- regulated or controlled technical data
- sensitive architecture diagrams
- internal hostnames or IP addresses
- proprietary vendor disclosures
- customer or partner data

## Release Evidence

This release includes `RELEASE_REVIEW.md`, a self-review using public-safety, claim-scoping, and UX criteria.

The review is a self-assessment, not an independent audit.

## License

MIT License. See `LICENSE`.

## Security

See `SECURITY.md` before reporting security issues or submitting security-sensitive material.

## Disclaimer

See `DISCLAIMER.md`. This repository is for defensive assessment and planning only.

---

**Bridge Node 7: public-safe frameworks for evidence-based technology readiness.**
