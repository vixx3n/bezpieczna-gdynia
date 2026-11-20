import csv
import json
from pathlib import Path


def read_accidents(csv_path):
    records = []

    with csv_path.open(encoding="utf-8-sig", newline="") as csv_file:
        for row in csv.DictReader(csv_file):
            records.append({
                "quarter": row["quarter"],
                "accidents": int(row["liczba_wypadkow"]),
                "injured": int(row["liczba_rannych"]),
                "deaths": int(row["liczba_zabitych"]),
            })

    return records


def main():
    project_dir = Path(__file__).resolve().parents[1]
    csv_path = project_dir / "data" / "raw" / "city_7_4_data.csv"
    json_path = project_dir / "src" / "data" / "accidents.json"

    records = read_accidents(csv_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(records, indent=2), encoding="utf-8")

    print(f"Zapisano {len(records)} rekordow w src/data/accidents.json")


if __name__ == "__main__":
    main()