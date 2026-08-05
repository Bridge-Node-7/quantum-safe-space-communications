# Quantum Exposure Severity

## Orientation

**Higher severity means greater concern.**

Exposure is recorded per asset, link, protocol, trust function, update path, vendor dependency, or protected data set. The framework does not calculate a compensating portfolio average.

## Required pre-scale result

### Unknown / Not Assessed

Use `Unknown / Not Assessed` when scope, cryptographic dependency, consequence, protection horizon, or evidence is incomplete. It is outside the ordered 0 through 4 scale and cannot be converted to zero, Low, or Not Applicable.

## Ordered severity scale

| Level | Label | Meaning |
|---:|---|---|
| 0 | Not Applicable | Sufficient evidence and an accountable applicability decision establish that no quantum-vulnerable public-key dependency is present in the approved scope |
| 1 | Low | Limited consequence, short protection horizon, and practical migration path supported by current evidence |
| 2 | Moderate | Material dependency or protection horizon requiring planned migration and owner action |
| 3 | High | Major mission, command, authentication, update, confidentiality, recovery, or supply-chain consequence |
| 4 | Critical | Potential mission loss, safety impact, unauthorized command, unrecoverable trust failure, or long-lived sensitive exposure without an acceptable path |

## Applicability rule

`Not Applicable` requires:

- identified scope item;
- sufficient current evidence;
- written rationale;
- named accountable decision owner;
- review date and reassessment trigger.

Missing or inconclusive information is `Unknown / Not Assessed`, never `Not Applicable`.

## Non-compensating rule

Use the highest supported severity associated with a material consequence or mandatory trigger. Do not average command integrity, safety, confidentiality, patchability, evidence, or vendor dependence into one reassuring value.

## Record template

### Identification

- Exposure ID:
- Asset, link, dependency, or protected data set:
- Mission function:
- Owner:

### Technical basis

- Cryptographic function:
- Algorithm, protocol, implementation, and version:
- Data protection horizon:
- Updateability, recovery, and rollback:
- Vendor or supply-chain dependency:

### Determination

- Result: Unknown / Not Assessed, Not Applicable, Low, Moderate, High, or Critical
- Rationale:
- Evidence IDs:
- Applicability authority when Not Applicable:
- Required treatment:
- Due date:
- Reassessment trigger:

Review [Critical Risk Overrides](critical-risk-overrides.md) whenever a mandatory trigger may apply.
