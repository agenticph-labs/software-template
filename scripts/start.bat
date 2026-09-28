@echo off
REM Windows startup script for software-template
REM Double-click this file to set up and launch the application.

setlocal enabledelayedexpansion

echo ============================================
echo  software-template - Windows Quick Start
echo ============================================

REM Determine project root (directory where this script lives)
set "PROJECT_DIR=%~dp0%.."
cd /d "%PROJECT_DIR%"

REM Create virtual environment if missing
if not exist "venv\" (
    echo [1/4] Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create venv. Check Python installation.
        pause
        exit /b 1
    )
)

REM Activate and install deps
echo [2/4] Installing dependencies...
call venv\Scripts\activate.bat
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: pip install failed.
    pause
    exit /b 1
)

REM Start server
echo [3/4] Starting server...
echo.
echo Server will open at http://127.0.0.1:8000
echo Press Ctrl+C to stop.
echo.
start "" http://127.0.0.1:8000

python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload

pause
