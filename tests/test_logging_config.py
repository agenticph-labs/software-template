"""Tests for structured JSON logging."""

import logging
import json
from io import StringIO

from app.logging_config import JSONFormatter, setup_logging


class TestJSONFormatter:
    def test_basic_format(self):
        formatter = JSONFormatter()
        logger = logging.getLogger("test_logger")
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(StringIO())
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False

        stream = handler.stream
        logger.info("hello world")

        record = json.loads(stream.getvalue())
        assert record["level"] == "INFO"
        assert record["logger"] == "test_logger"
        assert record["message"] == "hello world"
        assert "timestamp" in record

    def test_extra_context(self):
        formatter = JSONFormatter()
        logger = logging.getLogger("test_extra_logger")
        logger.setLevel(logging.INFO)
        stream = StringIO()
        handler = logging.StreamHandler(stream)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False

        logger.info("with context", extra={"user_id": "abc123", "path": "/health"})

        record = json.loads(stream.getvalue())
        assert record["message"] == "with context"
        assert record["context"]["user_id"] == "abc123"
        assert record["context"]["path"] == "/health"

    def test_exception_formatting(self):
        formatter = JSONFormatter()
        logger = logging.getLogger("test_exc_logger")
        logger.setLevel(logging.INFO)
        stream = StringIO()
        handler = logging.StreamHandler(stream)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False

        try:
            raise ValueError("test error")
        except ValueError:
            logger.exception("something failed")

        record = json.loads(stream.getvalue())
        assert record["message"] == "something failed"
        assert "exception" in record
        assert "ValueError" in record["exception"]
        assert "test error" in record["exception"]

    def test_setup_logging_adds_handler(self):
        root = logging.getLogger()
        root.handlers.clear()

        setup_logging(logging.DEBUG)
        assert len(root.handlers) == 1
        assert isinstance(root.handlers[0].formatter, JSONFormatter)
        assert root.level == logging.DEBUG
