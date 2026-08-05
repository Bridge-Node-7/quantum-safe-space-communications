# Release Checklist

## Source candidate

- [ ] All semantic and mutation tests pass
- [ ] Linux and Windows validation pass
- [ ] External links and structured files validate
- [ ] Secret and public-boundary scans pass
- [ ] Manifest, hashes, and deterministic package reproduction pass
- [ ] No release-blocking finding remains

## Pull request

- [ ] Exact source package hash verified
- [ ] Clean temporary clone created
- [ ] Release date stamped and records regenerated
- [ ] Changed-file allowlist passes
- [ ] Hosted checks pass on exact head SHA
- [ ] Human merge authorization records exact head SHA
- [ ] Merge uses `--match-head-commit`
- [ ] Merged tree equals validated head tree

## Repository and release

- [ ] Repository renamed and metadata read back
- [ ] Former-name redirect verified
- [ ] Exact stable required checks applied
- [ ] Actions token is read-only and workflow PR approval is disabled
- [ ] Private vulnerability reporting enabled and verified
- [ ] Secret scanning and push protection enabled and verified where supported
- [ ] Signed tag points to exact merged main
- [ ] Public assets downloaded and hashes verified
- [ ] No unrelated or unreviewed open pull requests remain; any allowed maintenance pull requests are documented in the final seal
- [ ] Logged-out public access verified
- [ ] Final seal and its checksum uploaded and reverified
