# Governance

## Stewardship

Bridge Node 7 is the public steward of this repository.

## Accountable roles

| Function | Accountable party | Responsibility |
|---|---|---|
| Method ownership | Bridge Node 7 | Approves scope and breaking revisions |
| Technical maintenance | Bridge Node 7 | Maintains validators, tests, workflow, and release integrity |
| Standards review | Bridge Node 7 internal standards review | Verifies status, applicability, and primary sources |
| Security ownership | Bridge Node 7 repository security owner | Receives and coordinates private reports |
| Release approval | Bridge Node 7 repository owner | Authorizes the exact reviewed pull-request head and release assets |

These roles do not constitute independent validation.

## Solo-maintainer release policy

A release may use zero GitHub approving reviews only when:

- hosted validation passes on the exact pull-request head;
- a separate human authorization phase is invoked with the exact head SHA;
- the merge uses `--match-head-commit`;
- the merged tree equals the validated head tree;
- the final public state is independently read back and sealed.

Where a qualified independent reviewer is available, their review should be recorded before release.

## Change classes

- **Patch:** editorial, link, metadata, or non-breaking template correction.
- **Minor:** new or materially revised methodology preserving public claim boundaries.
- **Major:** incompatible method, scope, or output change.

See [Change Control](docs/change-control.md).
