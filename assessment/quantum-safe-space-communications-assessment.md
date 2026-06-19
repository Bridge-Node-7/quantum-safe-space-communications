# Quantum-Safe Space Communications Security Assessment

## Purpose

The Quantum-Safe Space Communications Security Assessment helps organizations identify, score, and prioritize quantum-era cybersecurity risks across space communications systems.

## Core Question

Are the organization's space communications systems ready for quantum-era cybersecurity risk?

## Scope

The assessment covers:

- Satellite command links
- Telemetry, tracking, and command systems
- Mission data links
- Inter-satellite links
- Ground-station infrastructure
- Cloud and vendor paths
- Software and firmware update paths
- Cryptographic dependencies
- Quantum risk exposure
- Post-quantum cryptography readiness
- Quantum communication feasibility
- Governance and ownership

## Assessment Modules

### Module 1: Communications Inventory

Doctrine: No inventory, no quantum security.

Output: **Space Communications Link Map**

### Module 2: Cryptographic Dependency Map

Doctrine: No crypto map, no migration plan.

Document RSA, ECC, TLS, VPNs, certificates, firmware signatures, secure boot, authentication, key exchange, encryption at rest and in transit, hardware security modules, and vendor-managed cryptography.

Output: **Crypto Dependency Register**

### Module 3: Quantum Exposure Assessment

Doctrine: Long-lived secrets require quantum-safe planning now.

Score each system by mission criticality, data secrecy lifetime, crypto vulnerability, patchability, vendor dependence, operational exposure, command integrity risk, and key-rotation capability.

Output: **Quantum Exposure Heat Map**

### Module 4: PQC Migration Readiness

Doctrine: No algorithm agility, no future resilience.

Assess algorithm agility, protocol compatibility, hardware constraints, bandwidth impact, signature-size impact, implementation maturity, testing requirements, certification requirements, and vendor roadmaps.

Output: **PQC Migration Roadmap**

### Module 5: QKD Feasibility

Doctrine: Do not buy quantum hardware before validating the mission need.

Evaluate link geometry, optical terminal readiness, pointing/acquisition/tracking requirements, atmospheric conditions, key-rate requirements, trusted-node assumptions, mission value, cost and complexity, and ground-station availability.

Output: **QKD Feasibility Decision Memo**

### Module 6: Governance and Ownership

Doctrine: No owner, no closure.

Assign risk owner, system owner, mission owner, crypto owner, vendor owner, budget owner, migration authority, and acceptance authority.

Output: **Quantum-Safe Ownership Matrix**

### Module 7: Executive Decision Package

Doctrine: Leaders need the next decision, not a technical fog bank.

Deliver current-state risk, priority gaps, migration path, 90-day action plan, vendor questions, budget categories, residual risk, and the decision required.

Output: **Executive Quantum-Safe Space Communications Brief**

## Supporting Template: Crypto Inventory Template

Use:

- `assessment/crypto-inventory-template.md`

This file operationalizes Module 2, Cryptographic Dependency Map.

The completed inventory should produce:

- Crypto Dependency Register
- Quantum Exposure Heat Map
- Top 10 Crypto Unknowns
- Vendor Evidence Gap List
- PQC Migration Candidate List
