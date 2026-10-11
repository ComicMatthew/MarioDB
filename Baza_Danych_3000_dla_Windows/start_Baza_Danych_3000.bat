@echo off
setlocal
set "TK_SILENCE_DEPRECATION=1"

where py >nul 2>nul
if not errorlevel 1 (
    set PYTHON_CMD=py
    goto :check_dependency
)

where python >nul 2>nul
if not errorlevel 1 (
    set PYTHON_CMD=python
    goto :check_dependency
)

echo Brakuje Python 3 na tym komputerze.
echo Zainstaluj Python 3.10+ (najlepiej z python.org) i uruchom ten plik ponownie.
pause
exit /b 1

:check_dependency
cd /d "%~dp0app"

%PYTHON_CMD% -c "import tkinter; print('tk_ok')" >nul 2>nul
if errorlevel 1 (
    echo Nie znaleziono poprawnej instalacji Pythona z Tkinterem.
    echo Zainstaluj Python 3.10+ z python.org i uruchom ten plik ponownie.
    pause
    exit /b 1
)

%PYTHON_CMD% -c "import openpyxl" >nul 2>nul
if errorlevel 1 (
    echo Instalowanie brakujacej biblioteki: openpyxl
    %PYTHON_CMD% -m pip install openpyxl
    if errorlevel 1 (
        echo Nie udalo sie zainstalowac openpyxl.
        echo Sprawdz polaczenie z internetem albo zainstaluj biblioteke recznie.
        pause
        exit /b 1
    )
)

start "" %PYTHON_CMD% ui.py
exit /b 0
