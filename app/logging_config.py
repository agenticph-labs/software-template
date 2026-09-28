"""Structured JSON logging configuration using Python stdlib.

Usage:
    from app.logging_config import setup_logging
    setup_logging()
    import logging
    log = logging.getLogger(__name__)
    log.info("Server started", extra={"port": 8080})
"""

import json
import logging
import sys
from typing import Any, Dict


class JSONFormatter(logging.Formatter):
    """Format log records as newline-delimited JSON objects."""

    def format(self, record: logging.LogRecord) -> str:
        log_entry: Dict[str, Any] = {
            "timestamp": self.formatTime(record, datefmt="%Y-%m-%dT%H:%M:%S.%03dZ"),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }

        if record.exc_info and record.exc_info[0]:
            log_entry["exception"] = self.formatException(record.exc_info)

        # Include any extra context passed via extra={}
        extra_keys = set(record.__dict__) - {
            "args", "asctime", "created", "exc_info", "exc_text",
            "filename", "funcName", "levelno", "levelname", "lineno",
            "message", "module", "msecs", "msg", "name", "pathname",
            "process", "processName", "relativeCreated", "stack_info",
            "thread", "threadName",
        }
        if extra_keys:
            log_entry["context"] = {k: record.__dict__[k] for k in extra_keys}

        return json.dumps(log_entry, default=str, ensure_ascii=False)


def setup_logging(level: int = logging.INFO) -> None:
    """Configure root logger to emit structured JSON to stdout.

    Args:
        level: Logging level (default: logging.INFO).
    """
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JSONFormatter())

    root = logging.getLogger()
    root.setLevel(level)
    # Remove default handlers to avoid duplicate output
    root.handlers.clear()
    root.addHandler(handler)
