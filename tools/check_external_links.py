#!/usr/bin/env python3
from __future__ import annotations

import concurrent.futures
import json
import re
import urllib.error
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    raise SystemExit("PyYAML is required. Run: python -m pip install -r requirements-validation.txt") from exc

ROOT = Path(__file__).resolve().parents[1]
RAW_URL_RE = re.compile(r"https?://[^\s)>|\"']+")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\((https?://[^)\s]+)\)")
PLANNED_ENDPOINTS = {
    "https://github.com/Bridge-Node-7/quantum-readiness-space-communications",
}
EXCEPTIONS_FILE = ROOT / "release/external-link-exceptions.json"


def normalize_url(value: str) -> str:
    """Normalize URL tokens extracted from Markdown, YAML, JSON, or prose."""
    return value.strip().strip("<>\"'").rstrip(".,;:!?)]}\"'")


def _walk_strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from _walk_strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from _walk_strings(item)


def _urls_from_text(text: str) -> set[str]:
    found = {normalize_url(u) for u in RAW_URL_RE.findall(text)}
    found.update(normalize_url(u) for u in MARKDOWN_LINK_RE.findall(text))
    return {u for u in found if u.startswith(("http://", "https://"))}


def urls(root: Path = ROOT) -> list[str]:
    found: set[str] = set()

    for path in root.rglob("*.md"):
        found.update(_urls_from_text(path.read_text(encoding="utf-8")))

    cff_path = root / "CITATION.cff"
    cff = yaml.safe_load(cff_path.read_text(encoding="utf-8"))
    for value in _walk_strings(cff):
        found.update(_urls_from_text(value))

    for rel in ("release/repository-metadata.json", "release/release-metadata.json"):
        data = json.loads((root / rel).read_text(encoding="utf-8"))
        for value in _walk_strings(data):
            found.update(_urls_from_text(value))

    return sorted(found)


def exceptions(root: Path = ROOT) -> dict[str, dict]:
    data = json.loads((root / "release/external-link-exceptions.json").read_text(encoding="utf-8"))
    result: dict[str, dict] = {}
    for row in data.get("exceptions", []):
        url = normalize_url(str(row.get("url") or ""))
        if not url or not row.get("reason") or not row.get("verified_on") or not row.get("owner"):
            raise SystemExit(f"invalid external-link exception record: {row}")
        result[url] = row
    return result


def request(url: str, method: str) -> tuple[bool, str]:
    headers = {
        "User-Agent": "QRSC-release-validator/0.2.0",
        "Accept": "*/*",
    }
    if method == "GET":
        headers["Range"] = "bytes=0-0"
    try:
        req = urllib.request.Request(url, headers=headers, method=method)
        with urllib.request.urlopen(req, timeout=18) as response:
            return 200 <= response.status < 400, f"{method} {response.status}"
    except urllib.error.HTTPError as exc:
        return False, f"{method} {exc.code}"
    except Exception as exc:
        return False, f"{method} {type(exc).__name__}: {exc}"


def check(url: str, allowed: dict[str, dict]) -> tuple[str, bool, str]:
    if url in PLANNED_ENDPOINTS:
        return url, True, "planned post-rename endpoint"
    ok, detail = request(url, "HEAD")
    if ok:
        return url, True, detail
    get_ok, get_detail = request(url, "GET")
    if get_ok:
        return url, True, f"{detail}; {get_detail}"
    if url in allowed:
        row = allowed[url]
        return url, True, f"documented exception: {row['reason']} (verified {row['verified_on']})"
    return url, False, f"{detail}; {get_detail}"


def main() -> int:
    allowed = exceptions()
    targets = urls()
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results = sorted(pool.map(lambda u: check(u, allowed), targets), key=lambda item: item[0])
    failures = []
    for url, ok, detail in results:
        print(("PASS" if ok else "FAIL") + f": {url} [{detail}]")
        if not ok:
            failures.append(url)
    if failures:
        print(f"STOP: {len(failures)} external link(s) failed or require documented exceptions")
        return 1
    print(f"PASS: {len(results)} normalized external links checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
