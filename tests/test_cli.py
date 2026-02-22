"""Integration tests for log_lens CLI."""

import json
import tempfile
from pathlib import Path

import pytest
from click.testing import CliRunner

from log_lens.cli import main


class TestCliIntegration:
    """Test CLI functionality end-to-end."""

    @pytest.fixture
    def runner(self):
        """Click CLI runner."""
        return CliRunner()

    @pytest.fixture
    def sample_log_file(self):
        """Create a temporary Apache log file."""
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
            f.flush()
            temp_name = f.name
        yield temp_name
        Path(temp_name).unlink()

    def test_cli_basic_help(self, runner):
        """Test CLI help command."""
        result = runner.invoke(main, ["--help"])
        assert result.exit_code == 0
        assert "Analyze server log files" in result.output
        assert "--export" in result.output
        assert "--top-ips" in result.output

    def test_cli_missing_logfile(self, runner):
        """Test CLI with missing log file."""
        result = runner.invoke(main, ["nonexistent.log"])
        assert result.exit_code != 0
        assert "does not exist" in result.output.lower()

    def test_cli_analyze_logfile(self, runner, sample_log_file):
        """Test CLI analyzing a log file."""
        result = runner.invoke(main, [sample_log_file])
        assert result.exit_code == 0
        assert "Analyzed" in result.output
        assert "192.168.1" in result.output
        assert "200" in result.output

    def test_cli_export_json(self, runner, sample_log_file):
        """Test CLI exporting to JSON."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json_file = f.name

        try:
            result = runner.invoke(main, [sample_log_file, "--export", json_file])
            assert result.exit_code == 0
            assert Path(json_file).exists()
            with open(json_file) as f:
                data = json.load(f)
            assert "format" in data
            assert data["format"] == "apache"
        finally:
            Path(json_file).unlink(missing_ok=True)

    def test_cli_top_ips_flag(self, runner, sample_log_file):
        """Test CLI with --top-ips flag."""
        result = runner.invoke(main, [sample_log_file, "--top-ips", "5"])
        assert result.exit_code == 0
        assert "192.168.1" in result.output


class TestCliEdgeCases:
    """Test CLI edge cases."""

    @pytest.fixture
    def runner(self):
        """Click CLI runner."""
        return CliRunner()

    def test_cli_empty_logfile(self, runner):
        """Test CLI with empty log file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as f:
            f.flush()
            empty_file = f.name
        try:
            result = runner.invoke(main, [empty_file])
            assert result.exit_code == 0
            assert "Analyzed" in result.output
        finally:
            Path(empty_file).unlink()

    def test_cli_malformed_logfile(self, runner):
        """Test CLI with malformed log file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as f:
            f.write("This is not a valid log format\n")
            f.flush()
            malformed_file = f.name
        try:
            result = runner.invoke(main, [malformed_file])
            assert result.exit_code == 0
            assert "Analyzed" in result.output
        finally:
            Path(malformed_file).unlink()

    def test_cli_large_top_ips_value(self, runner):
        """Test CLI with large --top-ips value."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as f:
            for i in range(5):
                line = (
                    f"192.168.1.{i} - - [25/Dec/2025:17:15:32 -0600] "
                    f'"GET /api/users HTTP/1.1" 200 1234 "-" "Mozilla/5.0"\n'
                )
                f.write(line)
            f.flush()
            logfile = f.name
        try:
            result = runner.invoke(main, [logfile, "--top-ips", "100"])
            assert result.exit_code == 0
            assert "192.168.1" in result.output
        finally:
            Path(logfile).unlink()
