# Raport końcowy projektu Bezpieczna Gdynia

| Identyfikator | Wersja | Autor | Data | Status |
|---|---|---|---|---|
| BG-RAPORT-001 | 0.1 | Jakub Woźniak | 2026-11-20 | Roboczy, przed publikacją |

## 1. Cel

Ułatwić mieszkańcom sprawdzanie statystyk wypadków drogowych z ofiarami
w Gdyni. Użytkownik może wybrać rok i zobaczyć sumy, wykres oraz dokładne
wartości kwartalne bez przeglądania pliku CSV.

## 2. Rezultaty

- Powstała strona pokazująca wypadki, rannych i zabitych.
- Filtr roku aktualizuje karty, wykres i tabelę.
- Skrypt pobiera dane przez API dane.gov.pl i przygotowuje JSON dla strony.
- Demo uruchamia się w Windows jedną komendą `scripts\run_demo.cmd`.
- Dwa testy przetwarzania danych i linter Ruff przeszły lokalnie.
- Przygotowano GitHub Actions. Uruchomienie CI zostanie sprawdzone po publikacji.

## 3. Porównanie z planem

| Plan | Wynik |
|---|---|
| Rozważano zakres ogólnopolski i porównanie województw | Wybrano Gdynię, bo dostępne dane opisują kwartały w jednym mieście. |
| Pokazać wyniki w czytelnej formie | Gotowe są karty, wykres, tabela i wybór roku. |
| Ułatwić odtworzenie danych i uruchomienie | Działają skrypty pobierania, przygotowania danych i startu demo. |
| Opublikować repozytorium i sprawdzić CI | Do potwierdzenia po publikacji. |

## 4. Wydajność

Pomiary wykonano 20 listopada 2026 r. w Chrome na laptopie z Windows.
Demo działało na `127.0.0.1`. Pamięć podręczna była wyłączona, a sieć nie
była sztucznie spowalniana.

| Próba | Zakończenie wszystkich żądań | Pobranie accidents.json |
|---|---:|---:|
| 1 | 127 ms | 41 ms |
| 2 | 76 ms | 12 ms |
| 3 | 143 ms | 15 ms |
| **Mediana** | **127 ms** | **15 ms** |

Każde odświeżenie wykonało 4 żądania i przesłało 11,6 kB. Powyższe liczby
opisują działanie lokalne. Nie są pomiarem szybkości publicznego hostingu.

Przeglądarka pobiera jeden mały plik JSON zamiast przetwarzać surowy CSV.
Po zmianie roku JavaScript filtruje już wczytane rekordy. Zmiana filtra
nie wymaga kolejnego zapytania do serwera. Strona nie używa zewnętrznej
biblioteki wykresów.

## 5. Wpływ i ograniczenia

Dane są łatwiejsze do przeglądania i porównywania niż w surowym CSV.
Przykładowo można szybko sprawdzić, że w 2025 r. najwięcej wypadków
odnotowano w III kwartale. Było ich 36.

Nie badano jeszcze, ilu mieszkańców skorzysta z aplikacji ani jak zmieni
ona ich wiedzę. Dane nie wskazują konkretnych ulic. W analizowanej kopii
rok 2026 obejmuje tylko pierwszy kwartał, co zaznaczono na stronie.

## 6. Wnioski

Mały, dobrze opisany zbiór wystarczył do stworzenia użytecznego demo.
Po publikacji należy sprawdzić CI i uruchomienie projektu ze świeżej
kopii. W kolejnej wersji warto poprosić kilku użytkowników o znalezienie
statystyk dla wybranego roku i sprawdzić, czy interfejs jest zrozumiały.

## Odniesienia

- [ISO 21513:2026](https://www.iso.org/standard/63585.html)
- [Źródło danych na dane.gov.pl](https://dane.gov.pl/pl/dataset/2336/resource/32633,liczba-wypadkow-drogowych-z-ofiarami-csv)

## Historia zmian

| Wersja | Data | Zmiana |
|---|---|---|
| 0.1 | 2026-11-20 | Opisano rezultaty lokalne, ograniczenia i trzy pomiary szybkości. |