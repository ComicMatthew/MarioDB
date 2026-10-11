#!/bin/bash
set -u

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
APP_DIR="$SCRIPT_DIR/app"

find_python_with_tk() {
  local candidates=()

  if command -v python3 >/dev/null 2>&1; then
    candidates+=("$(command -v python3)")
  fi

  for p in \
    /opt/homebrew/bin/python3 \
    /usr/local/bin/python3 \
    /usr/bin/python3 \
    /Library/Frameworks/Python.framework/Versions/*/bin/python3
  do
    [ -x "$p" ] && candidates+=("$p")
  done

  local c
  for c in "${candidates[@]}"; do
    if [ -n "$c" ] && "$c" -c "import tkinter; print('tk_ok')" >/dev/null 2>&1; then
      printf '%s\n' "$c"
      return 0
    fi
  done

  return 1
}

PYTHON_BIN="$(find_python_with_tk)"
if [ -z "$PYTHON_BIN" ]; then
  echo "Brak poprawnej instalacji Pythona z Tkinterem."
  echo "Zainstaluj Python 3.10+ z python.org i uruchom ten plik ponownie."
  exit 1
fi

export TK_SILENCE_DEPRECATION=1
cd "$APP_DIR"

if ! "$PYTHON_BIN" -c "import openpyxl" >/dev/null 2>&1; then
  echo "Instalowanie brakujacej biblioteki: openpyxl"
  "$PYTHON_BIN" -m pip install openpyxl
  if [ $? -ne 0 ]; then
    echo "Nie udalo sie zainstalowac openpyxl."
    echo "Sprawdz polaczenie z internetem albo zainstaluj biblioteke recznie."
    exit 1
  fi
fi

"$PYTHON_BIN" ui.py
