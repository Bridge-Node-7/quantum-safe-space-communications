from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PublicBoundaryTests(unittest.TestCase):
    def test_token_in_validator_is_detected(self):
        tmp = Path(tempfile.mkdtemp()) / "repo"
        shutil.copytree(ROOT, tmp, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))
        target = tmp / "tools" / "validate_repo.py"
        target.write_text(target.read_text() + "\nLEAK='ghp_" + "A" * 36 + "'\n")
        result = subprocess.run(
            [sys.executable, str(tmp / "tools" / "scan_public_boundary.py")],
            cwd=tmp,
            text=True,
            capture_output=True,
        )
        shutil.rmtree(tmp.parent)
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("access token", result.stdout)


if __name__ == "__main__":
    unittest.main()
