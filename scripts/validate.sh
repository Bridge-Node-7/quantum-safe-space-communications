#!/usr/bin/env bash
set -Eeuo pipefail
IFS=$'\n\t'
export PYTHONUTF8=1
export PYTHONIOENCODING=utf-8
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
python - <<'PY'
import importlib.util
missing=[m for m in ['yaml'] if importlib.util.find_spec(m) is None]
if missing:
    raise SystemExit('Missing validation dependencies. Run: python -m pip install -r requirements-validation.txt')
import yaml
if yaml.__version__ != "6.0.3":
    raise SystemExit(f"PyYAML 6.0.3 is required, found {yaml.__version__}")
PY
printf 'WORKING: semantic repository and whitespace validation\n'
python tools/validate_repo.py
printf 'WORKING: staged Git whitespace equivalence\n'
python tools/check_staged_whitespace.py
printf 'WORKING: public-boundary scan\n'
python tools/scan_public_boundary.py
printf 'WORKING: positive and mutation tests\n'
python -m unittest discover -s tests -v
printf 'WORKING: manifest and checksum verification\n'
python tools/generate_manifest.py --check
printf 'WORKING: deterministic source package reproduction\n'
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
python tools/build_release.py --output "$tmp/a.zip" >/dev/null
python tools/build_release.py --output "$tmp/b.zip" >/dev/null
cmp "$tmp/a.zip" "$tmp/b.zip"
if [[ "${VALIDATE_NETWORK:-0}" == "1" ]]; then
  printf 'WORKING: controlled external-link validation\n'
  python tools/check_external_links.py
fi
printf 'PASS: complete documentation-first release validation\n'
