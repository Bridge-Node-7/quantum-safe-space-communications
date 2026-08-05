# Critical Risk Overrides

## Purpose

Critical overrides are non-compensatory. A stronger readiness domain, lower-severity record elsewhere, or larger amount of unrelated evidence cannot cancel an unresolved critical condition.

## Required taxonomy

| ID | Condition |
|---|---|
| CR-01 | Command authentication is not demonstrated for a critical control path |
| CR-02 | Secure update, firmware signing, or rollback verification has failed or is absent for a critical component |
| CR-03 | Critical key material or trust anchors lack governed custody, rotation, revocation, or recovery |
| CR-04 | A safety-critical function has unacceptable residual exposure |
| CR-05 | An unpatchable or unsupported critical component has no approved migration or compensating-control path |
| CR-06 | Authenticated recovery or rollback is not demonstrated for a critical service |
| CR-07 | A critical vendor or supply-chain dependency is unresolved or unsupported |
| CR-08 | A critical exposure has no accountable owner and due date |
| CR-09 | Evidence coverage is insufficient or a critical item remains unassessed |
| CR-10 | An assessment-specific mission-loss condition is declared by the accountable authority |
| CR-11 | Long-lived sensitive information depends on quantum-vulnerable key establishment and requires harvest-now-decrypt-later treatment |
| CR-12 | Evidence on a critical path is materially contradictory, unreliable, or unreconciled |

Unknown critical flags must be recorded and escalated. They must not be ignored because they are absent from a prior taxonomy.

## Status

- Open
- Mitigated
- Accepted Exception
- Not Applicable
- Closed

## Governance requirements

An accepted exception requires named authority, rationale, evidence IDs, residual exposure, compensating controls, owner, action, acceptance date, and review or expiration date.

A closed override requires closure evidence, named verifier, accountable approver, closure date, and reassessment trigger.

`Not Applicable` requires evidence and an accountable applicability determination.

## Core register

| Override ID | Condition | Scope item | Status | Owner | Due date |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Governance details

For each override, record required action, authority, evidence IDs, residual exposure, acceptance or closure rationale, verification date, and review trigger.

## Decision-support effect

- Missing critical evidence: **Evidence Required**
- Open critical override: **Critical Action Required**
- Accepted material exception: **Executive Decision Required**
- No unresolved override after adequate assessment: continue to complete human review of the Quantum Readiness Decision Pack
