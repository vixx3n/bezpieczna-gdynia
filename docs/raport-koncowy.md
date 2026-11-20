# Raport końcowy projektu Bezpieczna Gdynia

| Identyfikator | Wersja | Autor | Data | Status |
|---|---|---|---|---|
| BG-RAPORT-001 | 1.0 | Jakub Woźniak | 2026-11-20 | Końcowy |

## 1. Cel projektu

Celem projektu było ułatwienie mieszkańcom sprawdzania statystyk
wypadków drogowych z ofiarami w Gdyni. Użytkownik może wybrać rok
i zobaczyć podsumowanie, wykres wypadków oraz dokładne wyniki kwartalne
bez przeglądania surowego pliku CSV.

## 2. Rezultaty

- Powstała strona pokazująca liczbę wypadków, rannych i zabitych.
- Wybór roku aktualizuje karty statystyk, wykres wypadków i tabelę kwartalną.
- Skrypt pobiera CSV przez API dane.gov.pl. Drugi skrypt przekształca
  dane do formatu JSON używanego przez stronę.
- Demo uruchamia się w systemie Windows jedną komendą `scripts\run_demo.cmd`.
  Działanie strony sprawdzono na laptopie i komputerze stacjonarnym.
- Dwa testy przetwarzania danych przeszły lokalnie na obu komputerach.
  Linter Ruff przeszedł na laptopie.
- Kod i dokumentację opublikowano na GitHubie. Kod udostępniono
  na licencji MIT.
- GitHub Actions skonfigurowano tak, aby uruchamiać testy i linter
  przy zgłoszeniach zmian. Przy commicie `8860a47` GitHub pokazał
  zielony status kontroli.

## 3. Porównanie z planem

| Plan | Wynik |
|---|---|
| Rozważyć zakres ogólnopolski i porównanie województw | Zakres ograniczono do Gdyni, ponieważ wybrany zbiór opisuje kwartały w jednym mieście. |
| Pokazać wyniki w czytelnej formie | Dodano karty statystyk, wybór roku, wykres wypadków i tabelę kwartalną. |
| Ułatwić odtworzenie danych i uruchomienie | Dodano skrypty pobierania i przetwarzania danych oraz uruchamianie demo jedną komendą. |
| Opublikować repozytorium i sprawdzić automatyczne kontrole | Repozytorium opublikowano na GitHubie. Przy commicie `8860a47` odnotowano zielony status kontroli. |

## 4. Wydajność

Pomiary wykonano 20 listopada 2026 r. w Chrome na laptopie z systemem
Windows. Demo działało lokalnie pod adresem `127.0.0.1`. Pamięć
podręczna przeglądarki była wyłączona. Nie stosowano sztucznego
spowolnienia połączenia.

| Próba | Czas do zakończenia wszystkich żądań | Czas pobrania `accidents.json` |
|---|---:|---:|
| 1 | 127 ms | 41 ms |
| 2 | 76 ms | 12 ms |
| 3 | 143 ms | 15 ms |
| **Mediana** | **127 ms** | **15 ms** |

Przy każdym odświeżeniu przeglądarka wykonała cztery żądania i pobrała
łącznie 11,6 kB. Wyniki opisują działanie lokalne. Nie są pomiarem
szybkości publicznego hostingu ani czasu potrzebnego na wyświetlenie
gotowych statystyk po pobraniu danych.

Przeglądarka pobiera jeden mały plik JSON, przygotowany wcześniej
z surowego CSV. Po zmianie roku JavaScript przelicza już wczytane dane.
Filtr nie wysyła kolejnego żądania do serwera. Strona nie pobiera
zewnętrznej biblioteki do rysowania wykresu.

## 5. Wpływ i ograniczenia

Strona pozwala porównać kwartały bez ręcznego filtrowania CSV.
Przykładowo dla 2025 r. pokazuje łącznie 96 wypadków, 100 rannych
i 6 zabitych. Na wykresie widać, że najwięcej wypadków w tym roku
odnotowano w trzecim kwartale. Było ich 36.

Nie badano, ilu mieszkańców skorzysta z aplikacji ani czy zmieni ona
ich wiedzę o bezpieczeństwie drogowym. Dane są zagregowane kwartalnie
i nie wskazują konkretnych ulic. W analizowanej kopii rok 2026 obejmuje
tylko pierwszy kwartał. Strona oznacza go jako rok z niepełnymi danymi,
żeby nie sugerować porównania z pełnym rokiem.

## 6. Wnioski

Mały zbiór danych wystarczył do stworzenia działającego demo z filtrem,
wykresem i tabelą. Najważniejsze było sprawdzenie zawartości CSV przed
ustaleniem zakresu projektu oraz porównanie wyników strony z danymi
źródłowymi.

W kolejnej wersji warto poprosić kilku użytkowników o znalezienie
statystyk dla konkretnego roku i sprawdzić, czy rozumieją oznaczenie
niepełnych danych. Warto też osobno udokumentować uruchomienie demo
ze świeżo pobranego repozytorium, bez wcześniej zapisanych danych.

## Odniesienia

- [Repozytorium Bezpieczna Gdynia](https://github.com/vixx3n/bezpieczna-gdynia)
- [Źródło danych na dane.gov.pl](https://dane.gov.pl/pl/dataset/2336/resource/32633,liczba-wypadkow-drogowych-z-ofiarami-csv)
- [ISO 21513:2026 – wytyczne dotyczące oceny po zakończeniu projektu](https://www.iso.org/standard/63585.html)

## Historia zmian

| Wersja | Data | Zmiana |
|---|---|---|
| 0.1 | 2026-11-20 | Opisano rezultaty lokalne, ograniczenia i trzy pomiary wydajności. |
| 1.0 | 2026-11-20 | Uzupełniono raport o publikację repozytorium, status kontroli i sprawdzenie demo na PC. |