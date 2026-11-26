@echo off
REM CampusHub - one-click run. Double-click this file.
cd /d "%~dp0"
title CampusHub Server

if not exist "env\Scripts\python.exe" (
    echo [1/3] Creating virtual environment...
    py -3.14 -m venv env 2>nul || py -3 -m venv env || python -m venv env
    if errorlevel 1 (
        echo Python not found. Install Python 3.12+ from https://www.python.org/downloads/
        pause
        exit /b 1
    )
    echo [2/3] Installing dependencies...
    env\Scripts\python.exe -m pip install --upgrade pip
    env\Scripts\python.exe -m pip install -r requirements.txt
)

echo Applying database migrations...
env\Scripts\python.exe manage.py migrate --noinput

if not exist ".seeded" (
    echo Loading sample data...
    env\Scripts\python.exe manage.py seed_data && echo done> .seeded
)

echo.
echo ==================================================
echo  CampusHub is running at http://127.0.0.1:8000/
echo  Sample login: seed_user_1 / seedpass123
echo  Press CTRL+C to stop the server.
echo ==================================================
start "" http://127.0.0.1:8000/
env\Scripts\python.exe manage.py runserver
pause
