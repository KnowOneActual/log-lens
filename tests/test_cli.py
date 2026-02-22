import json
import tempfile
from pathlib import Path

import pytest
from click.testing import CliRunner

from log_lens.cli import main


class TestCliIntegration:
    @pytest.fixture
    def runner(self):
        return CliRunner()

    @pytest.fixture
    def temp_log(self):
        """Create a temporary Apache log file."""
        # Broken into smaller strings to stay under the 100-character limit
        content = (
            "192.168.1.1 - - [25/Dec/2025:17:15:32 -0600] "
            '"GET /api/users HTTP/1.1" 200 1234 "-" "Mozilla/5.0"\n'
            "192.168.1.2 - - [25/Dec/2025:17:15:33 -0600] "
            '"POST /api/data HTTP/1.1" 201 567 "-" "curl/7.68.0"\n'
            "192.168.1.1 - - [25/Dec/2025:17:15:34 -0600] "
            '"GET /api/users HTTP/1.1" 200 1234 "-" "Mozilla/5.0"\n'
        )
        with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as f:
            f.write(content)
            temp_path = f.name
        yield temp_path
        Path(temp_path).unlink()

    def test_cli_basic_help(self, runner):
        result = runner.invoke(main, ["--help"])
        assert result.exit_code == 0
        assert "Analyze Apache/Nginx logs" in result.output

    def test_cli_missing_logfile(self, runner):
        result = runner.invoke(main, ["nonexistent.log"])
        assert result.exit_code != 0
        assert "Error" in result.output

    def test_cli_analyze_logfile(self, runner, temp_log):
        result = runner.invoke(main, [temp_log])
        assert result.exit_code == 0
        assert "Total Requests" in result.output
        assert "192.168.1.1" in result.output

    def test_cli_export_json(self, runner, temp_log):
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            export_path = f.name

        try:
            result = runner.invoke(main, [temp_log, "--output", export_path])
            assert result.exit_code == 0

            with open(export_path, "r") as f:
                data = json.load(f)
                assert "summary" in data
                assert data["summary"]["total_requests"] == 3
        finally:
            Path(export_path).unlink()

    def test_cli_top_ips_flag(self, runner, temp_log):
        result = runner.invoke(main, [temp_log, "--top-ips", "1"])
        assert result.exit_code == 0
        # Should only show the top 1 IP
        assert "192.168.1.1" in result.output
        assert "192.168.1.2" not in result.output


class TestCliEdgeCases:
    @pytest.fixture
    def runner(self):
        return CliRunner()

    def test_cli_empty_logfile(self, runner):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as f:
            temp_path = f.name

        try:
            result = runner.invoke(main, [temp_path])
            assert result.exit_code == 0
            assert "Total Requests: 0" in result.output
        finally:
            Path(temp_path).unlink()

    def test_cli_malformed_logfile(self, runner):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as f:
            f.write("this is not a log entry\n")
            temp_path = f.name

        try:
            result = runner.invoke(main, [temp_path])
            assert result.exit_code == 0
            assert "Total Requests: 0" in result.output
        finally:
            Path(temp_path).unlink()

    def test_cli_large_top_ips_value(self, runner):
        # Create a log with multiple IPs
        with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as f:
            for i in range(5):
                # Formatted to avoid long line error
                log_line = (
                    f"192.168.1.{i} - - [25/Dec/2025:17:15:32 -0600] "
                    f'"GET /api/users HTTP/1.1" 200 1234 "-" "Mozilla/5.0"\n'
                )
                f.write(log_line)
            f.flush()
            temp_path = f.name

        try:
            # Ask for more top IPs than exist
            result = runner.invoke(main, [temp_path, "--top-ips", "10"])
            assert result.exit_code == 0
            assert "Total Requests: 5" in result.output
        finally:
            Path(temp_path).unlink()
