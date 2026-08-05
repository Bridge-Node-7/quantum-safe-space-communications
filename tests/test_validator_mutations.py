from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from validate_repo import validate

class ValidatorMutationTests(unittest.TestCase):
    def mutated(self, mutate):
        tmp = Path(tempfile.mkdtemp()) / "repo"
        shutil.copytree(ROOT, tmp, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))
        mutate(tmp)
        errors = validate(tmp)
        shutil.rmtree(tmp.parent)
        return errors

    def assert_rejected(self, mutate, contains):
        errors = self.mutated(mutate)
        self.assertTrue(any(contains.lower() in e.lower() for e in errors), errors)

    def test_lowercase_retired_identity_is_rejected(self):
        self.assert_rejected(lambda r: (r/"README.md").write_text((r/"README.md").read_text()+"\nquantum-safe space communications\n"), "retired identity")

    def test_weighted_claim_anywhere_is_rejected(self):
        self.assert_rejected(lambda r: (r/"docs"/"bad.md").write_text("# Bad\nWeighted readiness score: 90\n"), "prohibited active methodology")

    def test_automated_go_engine_is_rejected(self):
        self.assert_rejected(lambda r: (r/"tools"/"engine.py").write_text('print("AUTOMATED_GO")\n'), "automated-disposition")

    def test_unknown_removal_is_rejected(self):
        def m(r):
            p=r/"assessment/quantum-exposure-severity.md"; p.write_text(p.read_text().replace("Unknown / Not Assessed", "Omitted"))
        self.assert_rejected(m, "exposure invariant")

    def test_override_semantic_placeholder_is_rejected(self):
        def m(r):
            p=r/"assessment/critical-risk-overrides.md"; p.write_text(p.read_text().replace("Evidence coverage is insufficient or a critical item remains unassessed", "Placeholder"))
        self.assert_rejected(m, "CR-09")

    def test_empty_decision_pack_is_rejected(self):
        self.assert_rejected(lambda r: (r/"decision-pack/README.md").write_text("# Quantum Readiness Decision Pack\n"), "Decision Pack section")

    def test_malformed_table_is_rejected(self):
        def m(r):
            p=r/"docs/standards-register.md"; p.write_text(p.read_text().replace("| CISA | PQC Product Categories |", "| CISA |"))
        self.assert_rejected(m, "malformed Markdown table")

    def test_invalid_issue_yaml_is_rejected(self):
        self.assert_rejected(lambda r: (r/".github/ISSUE_TEMPLATE/documentation.yml").write_text("name: [broken\n"), "invalid structured file")

    def test_weighted_claim_in_readme_is_rejected(self):
        self.assert_rejected(
            lambda r: (r/"README.md").write_text((r/"README.md").read_text()+"\nWeighted readiness score: 90\n"),
            "prohibited active methodology",
        )

    def test_runtime_go_in_allowed_python_scope_is_rejected(self):
        self.assert_rejected(
            lambda r: (r/"tools"/"assessment_engine.py").write_text('print("GO")\n'),
            "runtime operational disposition",
        )

    def test_unexpected_javascript_engine_is_rejected(self):
        self.assert_rejected(
            lambda r: (r/"tools"/"assessment-engine.js").write_text('console.log("GO")\n'),
            "unexpected executable-code artifact",
        )

    def test_generated_release_files_must_be_in_allowlist(self):
        def m(r):
            p=r/"release"/"changed-files-allowlist.txt"
            p.write_text("\n".join(x for x in p.read_text().splitlines() if x != "REPO_MANIFEST.json")+"\n")
        self.assert_rejected(m, "allowlist is missing")

    def test_reversed_evidence_coverage_formula_is_rejected(self):
        def m(r):
            p = r / "assessment/evidence-confidence-ledger.md"
            original = p.read_text(encoding="utf-8")
            mutated = original.replace(
                "Evidence-complete in-scope items / Total in-scope items × 100",
                "Total in-scope items / Evidence-complete in-scope items × 100",
            )
            self.assertNotEqual(original, mutated, "evidence coverage mutation did not apply")
            p.write_text(mutated, encoding="utf-8", newline="\n")
        self.assert_rejected(m, "evidence coverage formula")

    def test_cr11_direction_cannot_be_negated(self):
        def m(r):
            p = r / "assessment/critical-risk-overrides.md"
            p.write_text(p.read_text().replace(
                "requires harvest-now-decrypt-later treatment",
                "is never critical and requires no harvest-now-decrypt-later treatment",
            ))
        self.assert_rejected(m, "CR-11")

    def test_cr12_direction_cannot_be_negated(self):
        def m(r):
            p = r / "assessment/critical-risk-overrides.md"
            p.write_text(p.read_text().replace(
                "is materially contradictory, unreliable, or unreconciled",
                "is contradictory but may be ignored",
            ))
        self.assert_rejected(m, "CR-12")

    def test_unbreakable_certification_claim_is_rejected(self):
        self.assert_rejected(
            lambda r: (r / "README.md").write_text(
                (r / "README.md").read_text() + "\nThis framework certifies unbreakable quantum-resistant communications.\n"
            ),
            "unsupported assurance",
        )

    def test_missing_evidence_cannot_become_not_applicable(self):
        def m(r):
            p = r / "assessment/quantum-exposure-severity.md"
            p.write_text(p.read_text().replace(
                "Missing or inconclusive information is `Unknown / Not Assessed`, never `Not Applicable`.",
                "Missing or inconclusive information may be recorded as `Not Applicable`.",
            ))
        self.assert_rejected(m, "applicability invariant")

    def test_readme_postures_cannot_be_operational_approvals(self):
        def m(r):
            p = r / "README.md"
            p.write_text(p.read_text().replace(
                "These human-governed postures support planning only:",
                "These postures are authoritative operational approvals:",
            ))
        self.assert_rejected(m, "README decision-boundary invariant")

    def test_known_limitations_cannot_be_emptied(self):
        self.assert_rejected(
            lambda r: (r / "KNOWN_LIMITATIONS.md").write_text("# Known Limitations\n"),
            "KNOWN_LIMITATIONS.md is too short",
        )

    def test_trailing_whitespace_is_rejected(self):
        self.assert_rejected(
            lambda r: (r / "README.md").write_text((r / "README.md").read_text() + "\nTrailing space  \n"),
            "trailing whitespace",
        )

    def test_readiness_orientation_cannot_be_reversed(self):
        def m(r):
            p = r / "assessment/migration-readiness-profile.md"
            p.write_text(p.read_text().replace(
                "Higher stages mean stronger demonstrated migration capability.",
                "Higher stages mean weaker demonstrated migration capability.",
            ))
        self.assert_rejected(m, "readiness orientation")

    def test_stage_zero_cannot_be_fully_ready(self):
        def m(r):
            p = r / "assessment/migration-readiness-profile.md"
            p.write_text(p.read_text().replace(
                "| 0 | Not Assessed | Scope or evidence is insufficient to characterize the domain |",
                "| 0 | Fully Ready | The domain is complete |",
            ))
        self.assert_rejected(m, "readiness stage 0 label")

    def test_cr01_cannot_be_weakened(self):
        def m(r):
            p = r / "assessment/critical-risk-overrides.md"
            p.write_text(p.read_text().replace(
                "Command authentication is not demonstrated for a critical control path",
                "Command authentication is absent but is noncritical",
            ))
        self.assert_rejected(m, "CR-01")

    def test_cr09_cannot_be_weakened(self):
        def m(r):
            p = r / "assessment/critical-risk-overrides.md"
            p.write_text(p.read_text().replace(
                "Evidence coverage is insufficient or a critical item remains unassessed",
                "Evidence incompleteness is never critical",
            ))
        self.assert_rejected(m, "CR-09")

    def test_quantum_proof_claim_is_rejected(self):
        self.assert_rejected(
            lambda r: (r / "README.md").write_text((r / "README.md").read_text() + "\nThis is a quantum-proof system.\n"),
            "unsupported assurance",
        )

    def test_flight_ready_claim_is_rejected(self):
        self.assert_rejected(
            lambda r: (r / "README.md").write_text((r / "README.md").read_text() + "\nThis framework proves the mission is flight-ready and mission-assured.\n"),
            "unsupported assurance",
        )

    def test_extra_blank_line_at_eof_is_rejected(self):
        def m(r):
            p = r / "KNOWN_LIMITATIONS.md"
            p.write_text(p.read_text().rstrip("\n") + "\n\n")
        self.assert_rejected(m, "extra blank line at EOF")

    def test_all_critical_conditions_reject_additive_weakening(self):
        source = (ROOT / "assessment/critical-risk-overrides.md").read_text()
        for code in [f"CR-{i:02d}" for i in range(1, 13)]:
            with self.subTest(code=code):
                def m(r, code=code):
                    p = r / "assessment/critical-risk-overrides.md"
                    lines = p.read_text().splitlines()
                    for i, line in enumerate(lines):
                        if line.startswith(f"| {code} |"):
                            lines[i] = line[:-1].rstrip() + " but this is not critical |"
                            break
                    p.write_text("\n".join(lines) + "\n")
                self.assert_rejected(m, code)

    def test_broader_unsupported_assurance_claims_are_rejected(self):
        claims = [
            "This framework is production-ready for operational deployment.",
            "This framework certifies mission readiness.",
            "This framework is validated for operations.",
            "This framework proves quantum-secure communications.",
            "This framework is certified for deployment.",
            "This framework makes the system mission-ready.",
            "This framework provides compliance certification.",
        ]
        for claim in claims:
            with self.subTest(claim=claim):
                self.assert_rejected(
                    lambda r, claim=claim: (r / "README.md").write_text(
                        (r / "README.md").read_text() + "\n" + claim + "\n"
                    ),
                    "unsupported assurance",
                )

    def test_additive_methodology_contradictions_are_rejected(self):
        mutations = [
            (
                "assessment/migration-readiness-profile.md",
                "Higher readiness stages also mean weaker capability.",
                "contradictory readiness",
            ),
            (
                "assessment/quantum-exposure-severity.md",
                "Higher exposure severity means lower concern.",
                "contradictory exposure",
            ),
            (
                "assessment/evidence-confidence-ledger.md",
                "Evidence coverage uses the reverse numerator and denominator.",
                "contradictory evidence-coverage",
            ),
            (
                "assessment/quantum-exposure-severity.md",
                "Missing or inconclusive information may be recorded as Not Applicable.",
                "contradictory exposure",
            ),
        ]
        for rel, addition, expected in mutations:
            with self.subTest(addition=addition):
                self.assert_rejected(
                    lambda r, rel=rel, addition=addition: (r / rel).write_text(
                        (r / rel).read_text() + "\n" + addition + "\n"
                    ),
                    expected,
                )


if __name__ == "__main__":
    unittest.main()
