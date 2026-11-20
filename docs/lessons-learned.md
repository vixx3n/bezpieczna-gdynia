# Lessons Learned — Bezpieczna Gdynia

| Identyfikator | Wersja | Autor | Data |
|---|---|---|---|
| BG-LL-001 | 0.1 | Jakub Woźniak | 2026-11-20 |

## Co zadziałało

- Sprawdzenie zawartości CSV przed pisaniem strony pomogło ustalić
  prawdziwy zakres danych. Plik zawierał kolejne kwartały aż do 2026Q1,
  mimo że w opisie zasobu widniała data z 2017 r.
- Budowanie po kolei kart, filtra, wykresu i tabeli ułatwiło sprawdzanie
  każdej zmiany osobno.
- Skopiowanie całego folderu projektu pozwoliło kontynuować pracę
  na laptopie z zachowaną historią Git i danymi.

## Co nie zadziałało

- Polecenia z PowerShella nie działały w CMD. Trzeba było wrócić
  do instrukcji i dostosować je do faktycznie używanego terminala.
- Po zmianach przeglądarka nadal pokazywała starszy JavaScript lub CSS.
  Przez to lista lat wyglądała na zepsutą mimo poprawionego kodu.

## Co zrobilibyśmy inaczej

- Od początku ustalilibyśmy, w którym terminalu wykonujemy polecenia,
  i podawali komendy pasujące do niego.
- Wcześniej dodalibyśmy skrypt uruchamiający demo jedną komendą
  oraz sprawdzili start z folderu bez pobranych danych.
- W razie problemu z widokiem najpierw sprawdzilibyśmy w zakładce Sieć,
  jaki plik faktycznie pobiera przeglądarka.

## Rekomendacje

- Przed wyborem zakresu projektu otworzyć przykładowy plik i sprawdzić
  okres, jednostki oraz braki danych.
- Zachować dwa przypadki do ręcznego sprawdzenia po każdej zmianie
  filtra. Rok 2025 ma cztery kwartały, a 2026 w tej kopii ma jeden.
- Przed oddaniem uruchomić demo z nowej kopii publicznego repozytorium
  i potwierdzić, że GitHub Actions uruchamia testy oraz linter.

## Odniesienie

- [PMI — Lessons learned](https://www.pmi.org/learning/library/lessons-learned-sharing-knowledge-8189)

## Historia zmian

| Wersja | Data | Zmiana |
|---|---|---|
| 0.1 | 2026-11-20 | Zapisano doświadczenia z realizacji projektu i rekomendacje. |