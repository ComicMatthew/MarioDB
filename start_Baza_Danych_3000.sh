#!/bin/bash
set -u

cd "$(dirname "$0")"

for folder in \
  "$(pwd)/baza" \
  "$(pwd)/dane" \
  "$(pwd)/dane/Dodawanie" \
  "$(pwd)/dane/Odejmowanie" \
  "$(pwd)/dane/Gotowe"
do
  if [ -e "$folder" ] && [ ! -d "$folder" ]; then
    echo "Pomijam: $folder istnieje jako plik, nie tworze katalogu." >&2
    continue
  fi
  mkdir -p "$folder"
done

PYTHON_BIN=""
for candidate in python3 python; do
  if command -v "$candidate" >/dev/null 2>&1; then
    if "$candidate" - <<'PY' >/dev/null 2>&1
import tkinter
import openpyxl
PY
    then
      PYTHON_BIN="$candidate"
      break
    fi
  fi
done

if [ -z "$PYTHON_BIN" ]; then
  echo "Brak Python 3 z Tkinter i openpyxl. Zainstaluj je i uruchom ponownie."
  exit 1
fi

"$PYTHON_BIN" -m pip install openpyxl >/dev/null 2>&1 || true
exec "$PYTHON_BIN" main.py
