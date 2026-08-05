from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from check_external_links import normalize_url, urls


class ExternalLinkParsingTests(unittest.TestCase):
    def test_normalize_strips_wrapping_quotes_and_punctuation(self):
        value = '"https://github.com/Bridge-Node-7/quantum-readiness-space-communications",'
        self.assertEqual(
            "https://github.com/Bridge-Node-7/quantum-readiness-space-communications",
            normalize_url(value),
        )

    def test_quoted_cff_and_markdown_urls_are_normalized_and_deduplicated(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "release").mkdir()
            (root / "README.md").write_text(
                '[Repository](https://github.com/Bridge-Node-7/quantum-readiness-space-communications)\n',
                encoding="utf-8",
            )
            (root / "CITATION.cff").write_text(
                'cff-version: 1.2.0\nmessage: Cite\ntitle: Test\nrepository-code: "https://github.com/Bridge-Node-7/quantum-readiness-space-communications"\n',
                encoding="utf-8",
            )
            metadata = {"url": "https://github.com/Bridge-Node-7/quantum-readiness-space-communications"}
            (root / "release/repository-metadata.json").write_text(json.dumps(metadata), encoding="utf-8")
            (root / "release/release-metadata.json").write_text(json.dumps(metadata), encoding="utf-8")
            found = urls(root)
            self.assertEqual(
                ["https://github.com/Bridge-Node-7/quantum-readiness-space-communications"],
                found,
            )
            self.assertFalse(any(url.endswith(('"', "'")) for url in found))


if __name__ == "__main__":
    unittest.main()
