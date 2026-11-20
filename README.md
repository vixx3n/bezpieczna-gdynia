# Bezpieczna Gdynia

Bezpieczna Gdynia to projekt otwartej aplikacji, która pomoże mieszkańcom
sprawdzić, jak zmieniała się liczba wypadków drogowych z ofiarami w Gdyni.
Zamiast przeglądać surowy plik CSV, będzie można wybrać rok i zobaczyć
liczby na wykresie oraz w tabeli.

## Źródło danych

- [Liczba wypadków drogowych z ofiarami na dane.gov.pl](https://dane.gov.pl/pl/dataset/2336/resource/32633,liczba-wypadkow-drogowych-z-ofiarami-csv)
- Dostawca danych — Gdynia – Otwarte Dane
- Sprawdzony plik zawiera 45 kwartalnych rekordów od I kwartału 2015 do
  I kwartału 2026. Rok 2026 jest w tym pliku niepełny.
- Dane obejmują liczbę wypadków, rannych, zabitych i wszystkich poszkodowanych.


## Uruchomienie

Potrzebujesz Pythona 3. Otwórz CMD w głównym folderze projektu i wpisz:

```cmd
scripts\run_demo.cmd
```

Otwórz [demo lokalne](http://127.0.0.1:8000/) w przeglądarce.
Skrypt pobierze CSV przez API dane.gov.pl, jeśli nie ma go na dysku,
przygotuje dane dla strony i uruchomi lokalny serwer. Nie wymaga dodatkowych
bibliotek. Żeby zatrzymać serwer, naciśnij Ctrl + C w CMD.

Skrypt pobierze dane przez API dane.gov.pl i zapisze je w pliku
`data/raw/city_7_4_data.csv`. Nie wymaga instalowania dodatkowych bibliotek.

Strona jest jeszcze w budowie. Instrukcja jej uruchomienia pojawi się
po przygotowaniu pierwszej działającej wersji.

## Informacje o dokumencie

| Identyfikator | Wersja | Autor | Data |
|---|---|---|---|
| BG-README-001 | 0.1 | Vixen | 2026-11-19 |

## Historia zmian

| Wersja | Data | Zmiana |
|---|---|---|
| 0.1 | 2026-11-19 | Pierwszy opis projektu i źródła danych. |
| 0.2 | 2026-11-19 | Dodano instrukcję pobierania danych przez API. |
| 0.3 | 2026-11-20 | Dodano instrukcję uruchomienia demo jedną komendą. |
| 0.4 | 2026-11-20 | Dodano odnośniki do raportu i Lessons Learned. |

## Dokumentacja

- [Raport końcowy i pomiary wydajności](docs/raport-koncowy.md)
- [Lessons Learned](docs/lessons-learned.md)