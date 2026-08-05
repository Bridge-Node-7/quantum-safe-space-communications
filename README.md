# Quantum Readiness for Space Communications

Evidence-based assessment and migration-planning framework for post-quantum cryptography across spacecraft, satellite links, ground systems, mission operations, and supporting vendors.

## Status

**Source candidate validated. Live GitHub publication remains pending until the staged release controller completes its public read-back and final seal.**

Version 0.2.0 is documentation-first. It retires the invalid weighted readiness aggregate and compensating average risk method published in version 0.1.5. It does not contain an automated assessment engine, cryptographic implementation, or workbook decision calculator.

## Who It Is For

- Satellite and spacecraft operators
- Ground-station providers
- Mission operations teams
- Space cybersecurity and mission-assurance teams
- Vendors and systems integrators
- Government and defense programs
- Procurement and program-management teams
- Technical assessors and reviewers

## What the Framework Produces

The **Quantum Readiness Decision Pack** brings together four separate decision inputs:

1. **Quantum Exposure Severity**, where higher severity means greater concern and `Unknown / Not Assessed` remains distinct from `Not Applicable`.
2. **Migration Readiness Profile**, where higher stages mean stronger demonstrated capability across ten non-compensating domains.
3. **Evidence Confidence and Coverage**, which records support strength, provenance, currency, conflicts, exclusions, and unassessed critical scope.
4. **Critical Risk Overrides**, which cannot be canceled by progress elsewhere.

The final package also records ownership, actions, standards applicability, limitations, decisions, approvals, and review history.

## Canonical Quick Start

1. [Define scope](assessment/quantum-readiness-space-communications-assessment.md).
2. [Map systems and links](assessment/link-map-template.md).
3. [Inventory cryptography](assessment/crypto-inventory-template.md).
4. [Record exposure](assessment/quantum-exposure-severity.md).
5. [Profile migration readiness](assessment/migration-readiness-profile.md).
6. [Record evidence confidence and coverage](assessment/evidence-confidence-ledger.md).
7. [Review critical conditions](assessment/critical-risk-overrides.md).
8. [Assign ownership and actions](assessment/ownership-matrix-template.md).
9. [Assemble the Quantum Readiness Decision Pack](decision-pack/README.md).
10. [Review the complete fictional example](examples/sample-small-satellite-decision-pack/README.md).

Start with inventory. Do not make a favorable exposure or readiness statement before the relevant systems, cryptography, owners, and evidence are in scope.

## Decision-Support Postures

These human-governed postures support planning only:

- **Assessment Incomplete**
- **Evidence Required**
- **Critical Action Required**
- **Executive Decision Required**
- **Ready for Governed Migration**

`Not Applicable` is an applicability determination, not a decision-support posture. It requires sufficient evidence and an accountable scope decision.

The postures are not certification, compliance determination, deployment approval, flight qualification, operational authorization, or proof that a system is quantum-safe.

## Repository Structure

```text
quantum-readiness-space-communications/
├── assessment/       Assessment instruments and historical compatibility pointers
├── briefings/        Action-planning templates
├── decision-pack/    Quantum Readiness Decision Pack assembly guidance
├── docs/             Methodology, evidence, standards, limits, and reading paths
├── examples/         Complete fictional Decision Pack
├── frameworks/       Migration roadmap
├── release/          Release metadata, settings checklist, and seal templates
├── tests/            Positive and adversarial methodology tests
└── tools/            Repository, link, boundary, manifest, and packaging validators
```

## Validate the Source Candidate

```bash
python -m pip install -r requirements-validation.txt
bash scripts/validate.sh
```

Windows PowerShell:

```powershell
python -m pip install -r requirements-validation.txt
powershell -ExecutionPolicy Bypass -File scripts/validate.ps1
```

Network checks are enabled in hosted CI. To run them locally:

```bash
VALIDATE_NETWORK=1 bash scripts/validate.sh
```

The validators enforce repository and methodology boundaries. They do not calculate an assessment outcome.

## Publicly Distributable Use

For this repository, **publicly distributable** means content approved for unrestricted public release after privacy, security, export-control, contractual, and mission-sensitivity review. Use fictional or explicitly authorized information only. Do not publish credentials, keys, tokens, controlled technical data, real mission architecture, sensitive hostnames, private vendor responses, customer information, or security weaknesses that could enable targeting.

Read the [Documentation Index](docs/README.md), [SECURITY.md](SECURITY.md), [DISCLAIMER.md](DISCLAIMER.md), [Known Limitations](KNOWN_LIMITATIONS.md), [Public Claim Boundaries](docs/public-claim-boundaries.md), and [Accessibility and Mobile Use](docs/accessibility-and-mobile-use.md).

## Release Strategy

The direct documentation-first v0.2.0 release supersedes the interim v0.1.6 containment plan because the complete corrected methodology is being prepared for immediate controlled execution. The original v0.1.5 tag and assets remain preserved and receive a visible supersession notice. See [Release Strategy Decision](release/release-strategy-decision.md).

## License

MIT License. See [LICENSE](LICENSE).

Bridge Node 7: evidence-first methods for trusted frontier translation.
