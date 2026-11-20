# Jak pomóc w rozwoju projektu

## Zgłaszanie błędów

Otwórz zgłoszenie w zakładce Issues. Napisz, co zrobiłeś, jakiego wyniku
oczekiwałeś i co faktycznie się stało. Podaj wybrany rok, jeśli błąd
dotyczy statystyk, oraz wersję przeglądarki lub Pythona, jeśli ma znaczenie.

## Proponowanie zmian

1. Zrób własną kopię repozytorium na GitHubie (fork) i utwórz gałąź na zmiany.
2. Wprowadź zmianę i uruchom poniższe polecenia w głównym folderze projektu.
3. Otwórz pull request, czyli zgłoszenie zmian. Opisz, co zmieniłeś i jak
   sprawdziłeś wynik.

```cmd
python -m unittest discover -s tests -v
python -m pip install ruff==0.17.5
python -m ruff check scripts tests
```

Nie dodawaj do repozytorium pobranego CSV ani wygenerowanego JSON-a.
Małe próbki używane w testach trzymaj w `data/sample/`.

## Informacje o dokumencie

| Identyfikator | Wersja | Autor | Data |
|---|---|---|---|
| BG-CONTRIB-001 | 0.1 | Vixen | 2026-11-20 |

## Historia zmian

| Wersja | Data | Zmiana |
|---|---|---|
| 0.1 | 2026-11-20 | Dodano zasady zgłaszania błędów i proponowania zmian. |