#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKEN = "{{RELEASE_DATE}}"
TARGETS = ["CHANGELOG.md", "CITATION.cff", "RELEASE_REVIEW.md", "release/release-metadata.json"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True)
    args = parser.parse_args()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date):
        raise SystemExit("Release date must be YYYY-MM-DD")
    try:
        dt.date.fromisoformat(args.date)
    except ValueError as exc:
        raise SystemExit(f"Release date is not a real calendar date: {args.date}") from exc
    changed = 0
    for rel in TARGETS:
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        if TOKEN in text:
            path.write_text(text.replace(TOKEN, args.date), encoding="utf-8", newline="\n")
            changed += 1
    metadata = json.loads((ROOT / "release/release-metadata.json").read_text(encoding="utf-8"))
    if metadata["release_date"] != args.date:
        raise SystemExit("release metadata date did not stamp correctly")
    print(f"PASS: stamped release date {args.date} in {changed} files")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
