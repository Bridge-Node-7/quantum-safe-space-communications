# Evidence Confidence and Coverage

## Purpose

Evidence support is separate from exposure severity and migration readiness. Weak or incomplete evidence does not reduce exposure and does not justify a stronger readiness statement.

## Confidence levels

| Level | Label | Typical basis |
|---:|---|---|
| E0 | Unsupported | Assertion without usable supporting material |
| E1 | Self-Attested | Interview, questionnaire, or owner statement |
| E2 | Documented | Controlled architecture, policy, inventory, design, or vendor documentation |
| E3 | Demonstrated | Configuration, test, measurement, artifact, or operational record |
| E4 | Independently Observed | Evidence reproduced or observed by a qualified independent reviewer within the stated scope |

## Orthogonal evidence fields

Record confidence separately from:

- source type;
- source owner;
- reviewer independence;
- scope supported;
- collection and verification dates;
- current status;
- integrity reference;
- limitations and conflicts.

## Evidence status

Use one status:

- Current
- Stale
- Conflicting
- Withdrawn
- Superseded

Only current, applicable evidence may support a current statement. Conflicting evidence must be reconciled or escalated under CR-12.

## Coverage method

Define the denominator before calculating coverage.

```text
Evidence Coverage (%) = Evidence-complete in-scope items / Total in-scope items × 100
```

The denominator must include every approved in-scope asset, link, dependency, critical condition, vendor dependency, and readiness-domain claim. Exclusions require a written rationale, accountable authority, and reassessment trigger.

An item is evidence-complete only when all material claims for that item cite current and applicable evidence meeting the stated support floor.

## Required summary

Every Quantum Readiness Decision Pack must report:

```text
Evidence Coverage: ___%
Total In-Scope Items: ___
Evidence-Complete Items: ___
Critical Unknowns: ___
Stale Evidence Items: ___
Conflicting Evidence Items: ___
Withdrawn or Superseded Items: ___
Unassessed Critical-Scope Items: ___
Approved Exclusions: ___
```

The summary is descriptive and human-reviewed. It is not an automated favorable disposition.

## Core ledger

| Evidence ID | Title | Level | Status | Claims supported | Limitations |
|---|---|---:|---|---|---|
|  |  |  |  |  |  |

## Record details

For each evidence ID, record source type and owner, independence, collection date, verification date, integrity reference, scope supported, conflicts, and reviewer.

## Claim-linkage rule

Every material exposure, readiness, override, vendor, closure, and Not Applicable statement must cite evidence IDs. Unknown or unavailable evidence must remain visible.
