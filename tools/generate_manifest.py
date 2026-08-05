#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "REPO_MANIFEST.json"
SUMS = ROOT / "SHA256SUMS"
EXCLUDED = {"REPO_MANIFEST.json", "SHA256SUMS"}

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def controlled_files():
    result=[]
    for p in ROOT.rglob("*"):
        if not p.is_file() or ".git" in p.parts or "__pycache__" in p.parts or p.suffix in {".pyc",".pyo"}:
            continue
        rel=p.relative_to(ROOT).as_posix()
        if rel in EXCLUDED or rel.startswith(("build/","dist/")):
            continue
        result.append(p)
    return sorted(result, key=lambda p:p.relative_to(ROOT).as_posix())

def build_manifest():
    metadata=json.loads((ROOT/"release/release-metadata.json").read_text(encoding="utf-8"))
    records=[{"path":p.relative_to(ROOT).as_posix(),"bytes":p.stat().st_size,"sha256":sha256(p)} for p in controlled_files()]
    return {
      "schema_version":"1.1",
      "repository":"Bridge-Node-7/quantum-readiness-space-communications",
      "title":metadata["title"],
      "version":metadata["version"],
      "release_date":metadata["release_date"],
      "methodology_scope":"documentation-first; no automated assessment engine or workbook decision calculator",
      "controlled_file_count":len(records),
      "integrity_note":"REPO_MANIFEST.json and SHA256SUMS are excluded from controlled files. SHA256SUMS includes REPO_MANIFEST.json but excludes itself.",
      "files":records,
    }

def sums_text(manifest):
    rows=[f"{e['sha256']}  {e['path']}" for e in manifest["files"]]
    rows.append(f"{sha256(MANIFEST)}  REPO_MANIFEST.json")
    return "\n".join(sorted(rows))+"\n"

def write_files():
    m=build_manifest(); MANIFEST.write_text(json.dumps(m,indent=2)+"\n",encoding="utf-8",newline="\n"); SUMS.write_text(sums_text(m),encoding="utf-8",newline="\n")

def check():
    if not MANIFEST.exists() or not SUMS.exists(): return 1
    expected=build_manifest(); actual=json.loads(MANIFEST.read_text(encoding="utf-8"))
    if actual!=expected: print("FAIL: manifest drift"); return 1
    if SUMS.read_text(encoding="utf-8")!=sums_text(actual): print("FAIL: checksum drift"); return 1
    print(f"PASS: manifest and {len(actual['files'])+1} hashes verify"); return 0

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); args=ap.parse_args()
    if args.check: return check()
    write_files(); print("PASS: generated manifest and checksums"); return 0
if __name__=="__main__": raise SystemExit(main())
