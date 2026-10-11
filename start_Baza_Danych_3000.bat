@echo off
cd /d "%~dp0"

if not exist "%~dp0baza" mkdir "%~dp0baza"
if not exist "%~dp0dane" mkdir "%~dp0dane"
if not exist "%~dp0dane\Dodawanie" mkdir "%~dp0dane\Dodawanie"
if not exist "%~dp0dane\Odejmowanie" mkdir "%~dp0dane\Odejmowanie"
if not exist "%~dp0dane\Gotowe" mkdir "%~dp0dane\Gotowe"

where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    set PYTHON_CMD=py
) else (
    set PYTHON_CMD=python
)

%PYTHON_CMD% -c "import tkinter, openpyxl; print('dependencies_ok')" >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Instalacja wymaganych bibliotek...
    %PYTHON_CMD% -m pip install openpyxl
)

start "" %PYTHON_CMD% main.py
