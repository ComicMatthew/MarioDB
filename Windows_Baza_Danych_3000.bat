@echo off
cd /d "%~dp0"

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

start "" %PYTHON_CMD% -m app
