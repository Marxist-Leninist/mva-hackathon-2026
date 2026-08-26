from pathlib import Path
import tempfile
import unittest

from scripts.readthrough_context import derive
from scripts.validate_submission import validate


ROOT = Path(__file__).resolve().parents[1]


class SubmissionTests(unittest.TestCase):
    def test_public_prediction_is_valid(self):
        path = ROOT / "results" / "MarxistLeninist_bub1b_compound_het.csv"
        self.assertEqual(validate(path), [])

    def test_rejects_out_of_range_epcr(self):
        source = (ROOT / "results" / "MarxistLeninist_bub1b_compound_het.csv").read_text()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.csv"
            path.write_text(source.replace(",0.99,", ",1.01,"))
            self.assertTrue(validate(path))

    def test_exact_ptc_context(self):
        result = derive("TTA", 2, "G", "A")
        self.assertEqual(result["mutant_codon"], "TGA")
        self.assertEqual(result["rna_context"], "UGA-A")
        self.assertTrue(result["is_stop"])


if __name__ == "__main__":
    unittest.main()

