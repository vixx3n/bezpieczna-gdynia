import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.prepare_data import read_accidents


class PrepareDataTests(unittest.TestCase):
    def test_reads_quarters_and_numbers(self):
        project_dir = Path(__file__).resolve().parents[1]
        sample = project_dir / "data" / "sample" / "accidents_sample.csv"

        self.assertEqual(read_accidents(sample), [
            {"quarter": "2025Q1", "accidents": 14, "injured": 15, "deaths": 0},
            {"quarter": "2025Q4", "accidents": 19, "injured": 17, "deaths": 2},
        ])

    def test_rejects_text_instead_of_number(self):
        with TemporaryDirectory() as folder:
            sample = Path(folder) / "invalid.csv"
            sample.write_text(
                "quarter,liczba_wypadkow,liczba_rannych,liczba_zabitych\n"
                "2025Q1,brak,15,0\n",
                encoding="utf-8",
            )

            with self.assertRaises(ValueError):
                read_accidents(sample)