#!/usr/bin/env bash
# Linux/macOS startup script for software-template
# Usage: bash scripts/start.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_DIR"

echo "============================================"
echo " software-template - Quick Start"
echo "============================================"

# Create virtual environment if missing
if [ ! -d "venv" ]; then
    echo "[1/4] Creating virtual environment..."
    python3 -m venv venv
fi

# Activate and install deps
echo "[2/4] Installing dependencies..."
source venv/bin/activate
pip install -r requirements.txt

# Start server
echo "[3/4] Starting server..."
echo ""
echo "Server will open at http://127.0.0.1:8000"
echo "Press Ctrl+C to stop."
echo ""

# Open browser (macOS: open, Linux: xdg-open)
case "$(uname -s)" in
    Darwin) open "http://127.0.0.1:8000" ;;
    Linux)  xdg-open "http://127.0.0.1:8000" || true ;;
esac

python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
