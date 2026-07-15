import csv
from pathlib import Path


def test_vocab_csv_has_at_least_one_well_formed_entry():
    csv_path = Path(__file__).resolve().parents[1] / "vocab.csv"

    with csv_path.open(newline="", encoding="utf-8") as f:
        rows = [row for row in csv.reader(f, delimiter="\t") if len(row) >= 2]

    assert rows, "vocab.csv must contain at least one tab-delimited word and translation pair"
