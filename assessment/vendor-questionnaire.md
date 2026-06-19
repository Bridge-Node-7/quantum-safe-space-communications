# Quantum-Safe Space Communications Vendor Questionnaire

## Purpose

This questionnaire helps assess vendor exposure to quantum-era cybersecurity risk in space communications systems.

## Vendor Identity

- Vendor name:
- Product or service:
- Space system supported:
- Mission dependency:
- Contact owner:
- Internal vendor owner:

## Cryptographic Dependencies

- What cryptographic algorithms are used?
- Is RSA used?
- Is elliptic-curve cryptography used?
- What key exchange methods are used?
- What digital signature schemes are used?
- What encryption is used for data in transit?
- What encryption is used for data at rest?
- Are certificates used?
- What are the certificate lifetimes?
- Who manages the certificate authority?
- Are cryptographic libraries internally developed or third-party?

## Post-Quantum Readiness

- Does the vendor have a PQC migration roadmap?
- Does the product support crypto-agility?
- Can algorithms be replaced without hardware replacement?
- Does the vendor support hybrid classical/PQC modes?
- Has the vendor tested NIST-standardized PQC algorithms?
- What is the timeline for PQC support?
- What systems cannot be upgraded?
- What is the vendor's plan for legacy systems?

## Space-Specific Constraints

- Is the product used in flight, ground, or both?
- Is the product radiation-hardened?
- Can firmware be updated after deployment?
- Can keys be rotated remotely?
- What are the SWaP constraints?
- What is the expected operational lifetime?
- What mission-critical links depend on this product?

## Evidence Requested

- Cryptographic architecture document
- PQC roadmap
- Software bill of materials
- Hardware bill of materials
- Firmware update procedure
- Key-management procedure
- Supply-chain assurance documentation
- Incident response process
