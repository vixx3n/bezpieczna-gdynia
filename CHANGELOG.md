# Changelog

Historia zmian projektu **Bezpieczna Gdynia**.

Dokument opisuje najważniejsze funkcjonalności, poprawki oraz etapy rozwoju aplikacji. Zmiany pogrupowano zgodnie z konwencją [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Planned
- Dalsze ulepszanie responsywności i wyglądu interfejsu.
- Rozbudowa możliwości wizualizacji danych.
- Rozważenie uruchamiania aplikacji w kontenerze Docker.
- Rozważenie udostępnienia demonstracji online.

## [1.0.0] - 2026-11-23

Pierwsza kompletna wersja projektu, przygotowana do prezentacji i oceny.

### Added
- Interaktywny dashboard statystyk wypadków drogowych w Gdyni.
- Karty przedstawiające liczbę wypadków, rannych i ofiar śmiertelnych.
- Filtrowanie danych według roku.
- Wykres porównujący wyniki kwartalne.
- Tabela szczegółowych danych.
- Komunikat informujący o niepełnym roku.
- Skrypt pobierający dane z publicznego API dane.gov.pl.
- Konwersja danych CSV do formatu JSON.
- Automatyczny skrypt uruchamiający lokalne demo.
- Testy jednostkowe przetwarzania danych.
- Kontrola jakości kodu za pomocą Ruff.
- Konfiguracja GitHub Actions.
- Publiczne repozytorium projektu.
- Licencja MIT.
- Dokumentacja README i CONTRIBUTING.
- Kodeks postępowania CODE_OF_CONDUCT.
- Szablony zgłoszeń i Pull Requestów.
- Raport końcowy i dokument Lessons Learned.

### Changed
- Uporządkowano strukturę katalogów projektu.
- Dopracowano wygląd dashboardu.
- Ulepszono prezentację statystyk kwartalnych.
- Zaktualizowano raport końcowy po publikacji repozytorium.
- Rozbudowano dokumentację użytkownika.

### Fixed
- Poprawiono obsługę odświeżania plików CSS i JavaScript w przeglądarce.
- Poprawiono sposób prezentowania niepełnych danych rocznych.
- Zweryfikowano uruchamianie projektu na dwóch komputerach.

### Tested
- Uruchomiono testy jednostkowe.
- Przeprowadzono kontrolę kodu za pomocą Ruff.
- Sprawdzono działanie lokalnego serwera HTTP.
- Zweryfikowano filtrowanie, wykres i tabelę.
- Wykonano pomiary wydajności w Chrome DevTools.

## Informacje o wydaniu

**Wersja:** 1.0.0  
**Status:** gotowa do prezentacji  
**Autor:** Jakub Woźniak  
**Repozytorium:** https://github.com/vixx3n/bezpieczna-gdynia

Szczegółowy opis testów i wyników znajduje się w pliku `docs/raport-koncowy.md`.