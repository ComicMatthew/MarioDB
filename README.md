# Baza Danych 3000

Prosty program do obsługi danych w Excelu z GUI w Tkinter.

## Struktura projektu

- `app/` – cała logika aplikacji i punkt wejścia `app/__main__.py`
- `baza/` – katalog z głównym plikiem bazy
- `dane/` – foldery robocze
  - `dane/Dodawanie`
  - `dane/Odejmowanie`
  - `dane/Gotowe`
- `config_mac.json` / `config_win.json` – konfiguracja dla konkretnego systemu
- `start_Baza_Danych_3000.sh` – uruchomienie na macOS/Linux
- `start_Baza_Danych_3000.bat` – uruchomienie na Windows

## Uruchomienie

### macOS / Linux

```bash
./start_Baza_Danych_3000.sh
```

### Windows

Uruchom:

```bat
start_Baza_Danych_3000.bat
```

## Ważne

- Jeśli katalogi nie istnieją, program je utworzy automatycznie.
- Nie nadpisuje istniejących katalogów ani plików, jeśli pod tą samą ścieżką jest już plik.
- W katalogach `dane/Dodawanie`, `dane/Odejmowanie`, `dane/Gotowe` należy trzymać pliki do przetworzenia i wyniki.

## Wymagania

```bash
python3 -m pip install openpyxl
```

Tkinter jest częścią standardowej instalacji Pythona na wielu systemach.
