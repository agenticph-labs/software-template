"""Tests for health endpoint."""

import json
import time

from app.health import get_health, set_db_connected, _format_uptime


class TestFormatUptime:
    def test_seconds_only(self):
        assert _format_uptime(42) == "42s"

    def test_minutes_and_seconds(self):
        assert _format_uptime(125) == "2m 5s"

    def test_hours_minutes_seconds(self):
        assert _format_uptime(3661) == "1h 1m 1s"

    def test_days_hours_minutes_seconds(self):
        assert _format_uptime(90061) == "1d 1h 1m 1s"

    def test_zero(self):
        assert _format_uptime(0) == "0s"


class TestHealth:
    def test_get_health_default_db_disconnected(self):
        body = json.loads(get_health())
        assert body["status"] == "ok"
        assert body["version"] == "1.0.0"
        assert isinstance(body["uptime"], float)
        assert body["uptime"] >= 0
        assert body["db_connected"] is False
        assert "python_version" in body
        assert "platform" in body

    def test_db_connected_flag(self):
        set_db_connected(True)
        body = json.loads(get_health())
        assert body["db_connected"] is True

    def test_db_disconnected_flag(self):
        set_db_connected(False)
        body = json.loads(get_health())
        assert body["db_connected"] is False

    def test_uptime_increases(self):
        body1 = json.loads(get_health())
        time.sleep(0.01)
        body2 = json.loads(get_health())
        assert body2["uptime"] > body1["uptime"]

    def test_uptime_human_present(self):
        body = json.loads(get_health())
        assert isinstance(body["uptime_human"], str)
        assert body["uptime_human"].endswith("s")
