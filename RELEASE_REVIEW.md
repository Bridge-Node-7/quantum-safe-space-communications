# Release Review

- **Version:** 0.2.3
- **Source candidate status:** VALIDATED ONLY BY EXACT PR-HEAD CHECKS
- **Live release status:** AUTHORITATIVE ONLY WHEN THE SIGNED TAG AND FINAL SEAL EXIST
- **Release date:** 2026-08-07

## Scope

- align security and public contribution guidance with restricted issue creation
- reconcile citation, release review, release notes, metadata, package prefix, manifest, and SHA-256 records
- preserve the v0.2.2 assessment methodology without modification

## Gates required in the source candidate

| Gate | Result |
|---|---|
| Documentation-first scope preserved | REQUIRED |
| No methodology change | REQUIRED |
| Semantic validator and mutation tests | REQUIRED |
| Linux and Windows validation | REQUIRED |
| Deterministic package recipe | REQUIRED |
| Manifest and checksums regenerated | REQUIRED |

## Gates completed only by live execution

- exact hosted checks on the pull-request head
- explicit human merge authorization
- exact-head merge and tree-equivalence check
- signed `v0.2.3` tag and public release
- public asset re-download and checksum verification
- logged-out public access verification
- final release seal and seal checksum

The source package must not call itself a completed public release before those live gates pass.
