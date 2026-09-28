"""Health check endpoint for application monitoring."""

import json
import time
import platform
from typing import Optional

# Module-level state
_start_time = time.time()
_db_connected: Optional[bool] = None


def set_db_connected(status: bool) -> None:
    """Set database connection status from application startup."""
    global _db_connected
    _db_connected = status


def get_health() -> str:
    """Return a JSON health-check response.

    Returns:
        JSON string with status, version, uptime, and db_connected fields.
    """
    uptime_seconds = time.time() - _start_time

    body = {
        "status": "ok",
        "version": "1.0.0",
        "uptime": round(uptime_seconds, 2),
        "uptime_human": _format_uptime(uptime_seconds),
        "db_connected": _db_connected if _db_connected is not None else False,
        "python_version": platform.python_version(),
        "platform": platform.system(),
    }
    return json.dumps(body)


def _format_uptime(seconds: float) -> str:
    """Format uptime seconds into a human-readable string."""
    days, remainder = divmod(int(seconds), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, secs = divmod(remainder, 60)
    parts = []
    if days:
        parts.append(f"{days}d")
    if hours:
        parts.append(f"{hours}h")
    if minutes:
        parts.append(f"{minutes}m")
    parts.append(f"{secs}s")
    return " ".join(parts)
