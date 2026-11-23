 Bezpieczna Gdynia

Interaktywny dashboard statystyk wypadków drogowych w Gdyni

Bezpieczna Gdynia to projekt open source, którego celem jest przedstawienie publicznych danych o wypadkach drogowych w przejrzystej i interaktywnej formie.

Aplikacja umożliwia analizowanie liczby wypadków, osób rannych i ofiar śmiertelnych w poszczególnych latach i kwartałach.

 Funkcjonalności

Wyświetlanie liczby wypadków drogowych.

Prezentowanie liczby rannych i ofiar śmiertelnych.

Filtrowanie statystyk według roku.

Wizualizacja danych kwartalnych na wykresie.

Szczegółowa tabela wyników.

Informowanie o niepełnych danych dla wybranego roku.

Automatyczne pobieranie i przygotowywanie danych.

Uruchamianie lokalnego demo jedną komendą.

 Źródło danych

Dane pochodzą z publicznego portalu dane.gov.pl, ze zbioru dotyczącego liczby wypadków drogowych z ofiarami w Gdyni.

Wykorzystywane informacje obejmują:

Okres sprawozdawczy (rok i kwartał).

Liczbę wypadków.

Liczbę osób rannych.

Liczbę osób zabitych.

Łączną liczbę poszkodowanych.

Dane są pobierane w formacie CSV i przekształcane do JSON.

Ważne: statystyki dotyczą zarejestrowanych zdarzeń w określonych okresach. Aplikacja nie prognozuje przyszłych wypadków.

 Wykorzystane technologie

Technologia

Zastosowanie

HTML5

Struktura strony

CSS3

Wygląd i układ interfejsu

JavaScript

Obsługa danych, filtrowania i wykresu

Python

Pobieranie i przetwarzanie danych

Git i GitHub

Kontrola wersji

GitHub Actions

Automatyczne testowanie

Ruff

Kontrola jakości kodu

unittest

Testy automatyczne

🚀 Uruchomienie aplikacji

Wymagania

Windows

Python 3

Połączenie z internetem podczas pierwszego pobierania danych

Krok 1. Pobierz repozytorium

git clone https://github.com/vixx3n/bezpieczna-gdynia.git
cd bezpieczna-gdynia

Krok 2. Uruchom demo

W wierszu polecenia Windows (CMD) wykonaj:

scripts\run_demo.cmd

Skrypt przygotuje potrzebne dane i uruchomi lokalny serwer HTTP.

Krok 3. Otwórz aplikację

W przeglądarce przejdź pod adres:

http://127.0.0.1:8000/

Aby zatrzymać serwer, naciśnij Ctrl+C w terminalu.

Demo działa lokalnie. Projekt nie wymaga publikowania aplikacji na zewnętrznym serwerze.

📈 Przykładowa analiza

Według danych wykorzystanych w projekcie w 2025 roku odnotowano:

Kwartał

Liczba wypadków

Q1 (styczeń–marzec)

14

Q2 (kwiecień–czerwiec)

27

Q3 (lipiec–wrzesień)

36

Q4 (październik–grudzień)

19

Razem

96

Najwięcej wypadków w 2025 roku odnotowano w trzecim kwartale.

🧪 Testowanie

Projekt zawiera automatyczne testy sprawdzające przetwarzanie danych.

Uruchomienie testów:

python -m unittest discover -s tests -v

Kontrola jakości kodu:

python -m pip install ruff==0.17.5
python -m ruff check scripts tests

Repozytorium zawiera również workflow GitHub Actions uruchamiający testy i kontrolę jakości kodu przy zmianach w repozytorium.

📂 Struktura projektu

Bezpieczna-Gdynia/
├── .github/                # Automatyzacja i szablony GitHub
├── data/
│   └── sample/             # Przykładowe dane
├── docs/                   # Dokumentacja i raporty
├── scripts/
│   ├── prepare_data.py     # Przetwarzanie CSV do JSON
│   └── run_demo.cmd        # Uruchomienie demo
├── src/
│   ├── index.html          # Strona aplikacji
│   ├── style.css           # Style
│   └── app.js              # Logika dashboardu
├── tests/                  # Testy automatyczne
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
└── LICENSE

📚 Dokumentacja

Dodatkowe materiały znajdują się w katalogu docs/:

raport-koncowy.md zawiera podsumowanie realizacji projektu, wyniki testów i pomiary wydajności.

lessons-learned.md opisuje zdobyte doświadczenia i wnioski.

Historia zmian jest dostępna w pliku CHANGELOG.md.

🤝 Współpraca

Projekt jest publiczny i otwarty na propozycje zmian.

Można zgłaszać błędy, proponować ulepszenia oraz przesyłać Pull Requesty.

Szczegółowe zasady opisano w pliku CONTRIBUTING.md.

📄 Licencja

Projekt jest udostępniany na licencji MIT. Szczegóły znajdują się w pliku LICENSE.

👨‍💻 Autor

Jakub Woźniak

Projekt edukacyjny z zakresu tworzenia oprogramowania open source, przetwarzania danych publicznych i tworzenia aplikacji internetowych.

GitHub: vixx3n/bezpieczna-gdynia