@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0"

where py >nul 2>nul
if not errorlevel 1 (
    set PYTHON_EXE=py
    goto :python_ok
)

where python >nul 2>nul
if not errorlevel 1 (
    set PYTHON_EXE=python
    goto :python_ok
)

echo Brakuje Python 3 na tym komputerze.
echo Zainstaluj Python 3.10+ i uruchom ten plik ponownie.
echo Wiecej: https://www.python.org/downloads/windows/
pause
exit /b 1

:python_ok
if not exist "script_files" mkdir "script_files"
if not exist "dodawanie" mkdir "dodawanie"
if not exist "odejmowanie" mkdir "odejmowanie"
if not exist "gotowe" mkdir "gotowe"

copy /Y "ui.py" "script_files\ui.py" >nul
copy /Y "my_functions.py" "script_files\my_functions.py" >nul
copy /Y "dodawanie.py" "script_files\dodawanie.py" >nul
copy /Y "odejmowanie.py" "script_files\odejmowanie.py" >nul
copy /Y "config.json" "script_files\config.json" >nul
copy /Y "config_mac.json" "script_files\config_mac.json" >nul

(
    echo @echo off
    echo cd /d "%%~dp0script_files"
    echo "%%PYTHON_EXE%%" ui.py
    echo pause
) > "start_Baza_Danych_3000.bat"

rem Ensure the generated launcher can use the same Python command, even if py is not in PATH on the target box.
set "PYTHON_EXE=%PYTHON_EXE%"

echo ====================================================
echo Zrobione.
echo Przesylka jest gotowa do wyslania na Windows.
echo.
echo Uruchom:
echo   start_Baza_Danych_3000.bat

echo.
echo Alternatywnie:
echo   "%PYTHON_EXE%" script_files\ui.py
echo ====================================================
pause
