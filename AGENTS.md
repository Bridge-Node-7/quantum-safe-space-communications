# AI Agent Guide

## Purpose

Use this repository to help prepare evidence-linked quantum-readiness planning artifacts for human review. The repository is a documentation-first framework, not an assessment engine or source of operational authority.

## Required Read Order

1. [README](README.md)
2. [Documentation Index](docs/README.md)
3. [Methodology](docs/methodology.md)
4. [Assessor Guide](docs/assessor-guide.md)
5. [Known Limitations](KNOWN_LIMITATIONS.md)
6. [Decision Pack Guide](decision-pack/README.md)
7. [Fictional Decision Pack](examples/sample-small-satellite-decision-pack/README.md)

## Operating Rules

- Use only fictional information or information explicitly authorized for the working environment.
- Do not invent systems, cryptographic dependencies, evidence, approvals, owners, dates, standards applicability, or test results.
- Record missing or inconclusive information as `Unknown / Not Assessed` where the methodology requires it.
- Do not convert missing evidence into `Not Applicable`, Low exposure, or stronger readiness.
- Keep Quantum Exposure Severity, Migration Readiness Profile, Evidence Confidence and Coverage, and Critical Risk Overrides separate.
- Do not calculate one aggregate readiness number.
- Use stable IDs and cross-reference them across scope, links, inventory, evidence, exposure, overrides, vendors, actions, and decisions.
- Cite evidence IDs for every material statement.
- Preserve conflicting evidence, limitations, exclusions, dissent, and reassessment triggers.
- Treat postures as planning support for human review. Do not output certification, compliance determination, deployment approval, flight qualification, operational authorization, or proof that a system is quantum-safe.

## Assessment Sequence

1. Define scope, owner, purpose, boundaries, and exclusions.
2. Map systems and communications links.
3. Build the cryptographic inventory.
4. Record Quantum Exposure Severity.
5. Complete the ten-domain Migration Readiness Profile.
6. Record evidence confidence and coverage.
7. Evaluate all twelve Critical Risk Overrides.
8. Assign owners, actions, resources, and dates.
9. Build the migration and recovery roadmap.
10. Assemble the Quantum Readiness Decision Pack.

Do not skip ahead to a posture before the supporting artifacts are complete enough for review.

## Expected Output

Produce artifacts in the order listed in the [Decision Pack Guide](decision-pack/README.md). Every output should identify:

- scope and exclusions;
- source evidence and evidence IDs;
- unknowns and conflicts;
- exposure findings;
- the full ten-domain readiness profile;
- critical conditions;
- accountable owners and due dates;
- limitations and assumptions;
- decisions requiring human review;
- reassessment triggers.

## Repository Changes

Before proposing or committing a repository change:

```bash
python -m pip install -r requirements-validation.txt
bash scripts/validate.sh
```

On Windows, also run:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/validate.ps1
```

Regenerate `REPO_MANIFEST.json` and `SHA256SUMS` after any controlled-file change:

```bash
python tools/generate_manifest.py
```

Do not weaken methodology invariants, claim boundaries, public-data protections, or validation controls.
