# Release Review

- **Version:** 0.2.1
- **Source candidate status:** VALIDATED ONLY BY EXACT PR-HEAD CHECKS
- **Live release status:** AUTHORITATIVE ONLY WHEN THE SIGNED TAG AND FINAL SEAL EXIST
- **Release date:** 2026-08-05

## Gates required in the source candidate

| Gate | Result |
|---|---|
| Documentation-first scope preserved | REQUIRED |
| No methodology change | REQUIRED |
| `actions/checkout` pinned to reviewed v7.0.1 SHA | REQUIRED |
| `actions/setup-python` pinned to reviewed v7.0.0 SHA | REQUIRED |
| GitHub Actions Dependabot updates grouped | REQUIRED |
| Semantic validator and mutation tests | REQUIRED |
| Linux and Windows validation | REQUIRED |
| Deterministic package recipe | REQUIRED |
| Manifest and checksums regenerated | REQUIRED |

## Gates completed only by live execution

- Exact hosted checks on the pull-request head
- Explicit human merge authorization
- Exact-head merge and tree-equivalence check
- Signed v0.2.1 tag and public release
- Public asset re-download and checksum verification
- Logged-out public access verification
- Final release seal and seal checksum
- Documentation of any allowed open maintenance pull requests

The source package must not call itself a completed public release before those live gates pass.
