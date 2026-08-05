# Release Review

- **Version:** 0.2.0
- **Source candidate status:** VALIDATED
- **Live release status:** PENDING PUBLIC READ-BACK SEAL
- **Release date:** 2026-08-05

## Gates completed in the source candidate

| Gate | Result |
|---|---|
| Documentation-first scope | PASS |
| Weighted aggregate retired | PASS |
| Unknown exposure state defined | PASS |
| Exposure and readiness separately oriented | PASS |
| Evidence confidence and coverage defined | PASS |
| Twelve non-compensatory critical conditions | PASS |
| Ten readiness domains | PASS |
| Complete fictional Quantum Readiness Decision Pack | PASS |
| Identity and compatibility controls | PASS |
| Semantic validator and mutation tests | PASS |
| Linux and Windows hosted-validation definitions | PASS |
| Deterministic package recipe | PASS |
| Manifest and checksums | PASS |

## Gates completed only by live execution

- Exact hosted checks on the pull-request head
- Explicit human merge authorization
- Exact-head squash merge and tree-equivalence check
- Repository rename and metadata read-back
- Branch protection and Actions permission read-back
- Vulnerability reporting, secret scanning, and push-protection read-back
- Signed tag and public release
- Public asset re-download and checksum verification
- Former-name redirect verification
- Logged-out public access verification
- Final release seal and seal checksum

The source package must not call itself a completed public release before those live gates pass.
