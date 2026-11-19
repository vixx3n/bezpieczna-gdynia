import csv
import io
import json
from pathlib import Path
from urllib.request import urlopen

API_URL = (
    "https://api.dane.gov.pl/1.4/resources/"
    "32633,liczba-wypadkow-drogowych-z-ofiarami-csv?lang=pl"
)

project_dir = Path(__file__).resolve().parents[1]
destination = project_dir / "data" / "raw" / "city_7_4_data.csv"

try:
    print("Pobieram informacje o pliku z dane.gov.pl...")
    with urlopen(API_URL, timeout=30) as response:
        metadata = json.load(response)

    csv_url = metadata["data"]["attributes"]["file_url"]

    print("Pobieram CSV z portalu Gdyni...")
    with urlopen(csv_url, timeout=30) as response:
        csv_data = response.read()

    # Sprawdzamy, czy odpowiedź zawiera kolumny naszego CSV.
    rows = csv.reader(io.StringIO(csv_data.decode("utf-8-sig")))
    header = next(rows, [])
    expected_columns = {
        "quarter",
        "liczba_wypadkow",
        "liczba_rannych",
        "liczba_zabitych",
        "liczba_wszystkich_poszkodowanych",
    }

    if not expected_columns.issubset(header):
        raise ValueError("W pobranym pliku brakuje oczekiwanych kolumn CSV.")

    row_count = sum(1 for row in rows if row)
    if row_count == 0:
        raise ValueError("Plik CSV nie zawiera żadnych rekordów.")

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(csv_data)

except (OSError, ValueError, KeyError, csv.Error) as error:
    raise SystemExit(f"Nie udało się pobrać lub zapisać danych. {error}") from None

print(f"Zapisano plik {destination.relative_to(project_dir)}")
print(f"Liczba rekordów: {row_count}")