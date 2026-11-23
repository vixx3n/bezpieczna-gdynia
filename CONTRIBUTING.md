#  Contributing to Bezpieczna Gdynia

Dziękuję za zainteresowanie projektem **Bezpieczna Gdynia**!

Projekt jest inicjatywą open source, której celem jest udostępnianie i wizualizacja danych dotyczących bezpieczeństwa drogowego w Gdyni.

Każda propozycja poprawy kodu, dokumentacji lub funkcjonalności jest mile widziana.

##  Jak możesz pomóc?

Możesz wesprzeć rozwój projektu poprzez:

- Zgłaszanie błędów i problemów technicznych.
- Proponowanie nowych funkcjonalności.
- Poprawianie wyglądu i responsywności interfejsu.
- Optymalizację kodu JavaScript i Python.
- Rozbudowę testów automatycznych.
- Ulepszanie dokumentacji.
- Weryfikację poprawności przetwarzania danych publicznych.

##  Zgłaszanie błędów

Jeżeli zauważysz błąd, utwórz nowe zgłoszenie w zakładce [Issues](https://github.com/vixx3n/bezpieczna-gdynia/issues).

Zgłoszenie powinno zawierać:

1. Krótki opis problemu.
2. Kroki pozwalające go odtworzyć.
3. Oczekiwane zachowanie aplikacji.
4. Rzeczywiste zachowanie aplikacji.
5. Informację o systemie operacyjnym i przeglądarce.
6. Zrzut ekranu lub komunikat błędu, jeśli jest dostępny.

Przed utworzeniem zgłoszenia sprawdź, czy podobny problem nie został już opisany.

## 💡 Proponowanie nowych funkcji

Pomysły na rozwój projektu można zgłaszać poprzez GitHub Issues.

Przykładowe propozycje:

- Nowe rodzaje wykresów.
- Porównywanie statystyk z różnych lat.
- Eksport danych do CSV.
- Rozbudowa obsługi urządzeń mobilnych.
- Uruchamianie aplikacji za pomocą Dockera.
- Publikacja demonstracji online.

Przed rozpoczęciem większych zmian warto omówić propozycję w zgłoszeniu.

## 🔧 Przygotowanie środowiska

### 1. Utwórz Fork

Utwórz własną kopię repozytorium za pomocą przycisku **Fork** na GitHubie.

### 2. Sklonuj repozytorium

```bash
git clone https://github.com/TWOJ_LOGIN/bezpieczna-gdynia.git
cd bezpieczna-gdynia
```

Zastąp `TWOJ_LOGIN` nazwą swojego konta.

### 3. Utwórz nową gałąź

```bash
git checkout -b feature/nazwa-zmiany
```

Przykładowo:

```bash
git checkout -b feature/nowy-wykres
```

### 4. Wprowadź zmiany

Projekt wykorzystuje HTML, CSS, JavaScript i Python.

Zachowuj istniejącą strukturę katalogów oraz dbaj o czytelność kodu.

### 5. Uruchom testy

Przed przesłaniem zmian wykonaj:

```bash
python -m unittest discover -s tests -v
```

Sprawdź również jakość kodu:

```bash
python -m pip install ruff==0.17.5
python -m ruff check scripts tests
```

### 6. Zapisz zmiany

```bash
git add .
git commit -m "Dodaj nową funkcjonalność"
git push -u origin feature/nazwa-zmiany
```

### 7. Utwórz Pull Request

Przejdź na GitHub i utwórz Pull Request do gałęzi `main`.

W opisie podaj:

- Co zostało zmienione.
- Dlaczego zmiana jest potrzebna.
- Jak przetestowano rozwiązanie.
- Czy zmiana wymaga aktualizacji dokumentacji.

##  Standardy jakości kodu

Przy wprowadzaniu zmian przestrzegaj następujących zasad:

- Stosuj czytelne nazwy zmiennych i funkcji.
- Unikaj niepotrzebnego powielania kodu.
- Zachowuj istniejące konwencje formatowania.
- Nie dodawaj haseł, tokenów API ani innych sekretów.
- Dodawaj testy do zmian w logice przetwarzania danych.
- Aktualizuj dokumentację przy zmianach funkcjonalności.
- Korzystaj z wiarygodnych źródeł danych.

##  Bezpieczeństwo i prywatność

Projekt wykorzystuje publiczne dane statystyczne.

Nie należy umieszczać w repozytorium danych osobowych, poufnych informacji ani danych umożliwiających identyfikację uczestników wypadków.

W przypadku wykrycia potencjalnej podatności bezpieczeństwa nie publikuj szczegółów umożliwiających jej wykorzystanie. Skontaktuj się z opiekunem repozytorium.

##  Zasady społeczności

Wszyscy uczestnicy projektu powinni przestrzegać zasad określonych w pliku [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

##  Licencja

Przesyłając zmiany do projektu, akceptujesz ich udostępnienie na warunkach licencji MIT obowiązującej w repozytorium.

##  Opiekun projektu

**Jakub Woźniak**

Repozytorium: [vixx3n/bezpieczna-gdynia](https://github.com/vixx3n/bezpieczna-gdynia)

Dziękuję za każdą propozycję ulepszenia projektu!