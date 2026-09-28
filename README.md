# software-template

![MIT License](https://img.shields.io/badge/license-MIT-green)

A standardized development template with CI/CD, health checks, monitoring, cross-platform startup scripts, and optional database support. Batteries included — fork or download to bootstrap your next Python/FastAPI project in minutes.

## Quick Start

1. **Download** the [latest ZIP](https://github.com/agenticph-labs/software-template/releases/latest) from Releases.
2. **Extract** the ZIP anywhere on your machine.
3. **Double-click** `scripts/START.bat` (Windows) or run `bash scripts/start.sh` (Mac/Linux).

The script creates a virtual environment, installs dependencies, opens your browser at `http://127.0.0.1:8000`, and starts the dev server with hot-reload.

### Manual Setup

```bash
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

## PH Use Case

This template is designed for Philippine development teams and BPO engineering units that need a standardized, production-ready project scaffold. It enforces:

- **Code quality gates** — CI enforces Ruff linting, 80%+ coverage, and security audits on every push.
- **Health monitoring** — The `/health` endpoint provides JSON status for Uptime Robot / Grafana.
- **Cross-platform** — `start.bat` (Windows) and `start.sh` (Mac/Linux) handle local setup identically.
- **Docker-ready** — `docker-compose.yml` runs the app with optional PostgreSQL.

## Project Structure

```
software-template/
├── .github/workflows/   # CI/CD pipelines
│   ├── test.yml          # pytest + Ruff + coverage
│   ├── security.yml      # pip-audit + Bandit
│   └── build.yml         # Release ZIP on tag push
├── app/
│   ├── __init__.py
│   ├── health.py          # /health JSON endpoint
│   └── logging_config.py  # Structured JSON logging
├── scripts/
│   ├── start.bat          # Windows quick start
│   └── start.sh           # Mac/Linux quick start
├── monitoring/
│   ├── healthcheck.sh     # Docker HEALTHCHECK command
│   └── UPTIME_CONFIG.md   # Uptime Robot setup guide
├── docker-compose.yml     # App + optional PostgreSQL
├── env.template           # Environment variables
├── README.md
├── LICENSE                # MIT
├── requirements.txt
└── .gitignore
```

## Health Endpoint

Once running, check `http://127.0.0.1:8000/health`:

```json
{
  "status": "ok",
  "version": "1.0.0",
  "uptime": 42.60,
  "uptime_human": "42s",
  "db_connected": false,
  "python_version": "3.12.0",
  "platform": "Linux"
}
```

## CI/CD Pipelines

| Workflow | Trigger | What it does |
|----------|---------|-------------|
| Test | Every push/PR to `main` | Ruff lint + pytest with 80% coverage threshold |
| Security | Every push/PR + weekly Monday | pip-audit (vulnerability scan) + Bandit (SAST) |
| Build | Tag push `v*.*.*` | Tests pass → release ZIP + GitHub Release |

---

### Need a production system? Contact us

AgenticPH Labs builds and operates production-grade software for Philippine enterprises. Reach out at **agenticph.com** for consulting, managed deployments, or custom development.
