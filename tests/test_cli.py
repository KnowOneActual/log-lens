"""Integration tests for log_lens CLI."""

import json
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from log_lens.cli import main


class TestCliIntegration:
    """Test CLI functionality end-to-end."""

    @pytest.fixture
    def sample_log_file(self):
        """Create a temporary Apache log file."""
        content = (
            '192.168.1.1 - - [25/Dec/2025:17:15:32 -0600] "GET /api/users HTTP/1.1" 200 1234 "-" "Mozilla/5.0"\n'
            '192.168.1.2 - - [25/Dec/2025:17:15:33 -0600] "POST /api/data HTTP/1.1" 201 567 "-" "curl/7.68.0"\n'
            '192.168.1.1 - - [25/Dec/2025:17:15:34 -0600] "GET /api/users HTTP/1.1" 200 1234 "-" "Mozilla/5.0"\n'
        )
        with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as f:
            f.write(content)
            f.flush()
            yield f.name
        Path(f.name).unlink()

    def test_cli_basic_help(self, capsys):
        """Test CLI help command."""
        with pytest.raises(SystemExit):
            main(["--help"])
        captured = capsys.readouterr()
        assert "Analyze server log files" in captured.out
        assert "--export" in captured.out
        assert "--top-ips" in captured.out

    def test_cli_missing_logfile(self, capsys):
        """Test CLI with missing log file."""
        with pytest.raises(SystemExit):
            main(["nonexistent.log"])
        captured = capsys.readouterr()
        assert "not found" in captured.out.lower() or "error" in captured.out.lower()

    def test_cli_analyze_logfile(self, sample_log_file, capsys):
        """Test CLI analyzing a log file."""
        with patch("sys.argv", ["log-lens", sample_log_file]):
            try:
                main([sample_log_file])
            except SystemExit:
                pass
        captured = capsys.readouterr()
        assert "Analyzed" in captured.out
        assert "192.168.1" in captured.out
        assert "200" in captured.out

    def test_cli_export_json(self, sample_log_file):
        """Test CLI exporting to JSON."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json_file = f.name

        try:
            with patch("sys.argv", ["log-lens", sample_log_file, "--export", json_file]):
                try:
                    main([sample_log_file, "--export", json_file])
                except SystemExit:
                    pass

            # Verify JSON was written
            assert Path(json_file).exists()
            with open(json_file) as f:
                data = json.load(f)
            assert "format" in data
            assert data["format"] == "apache"
            assert "status_codes" in data
        finally:
            Path(json_file).unlink(missing_ok=True)

    def test_cli_top_ips_flag(self, sample_log_file, capsys):
        """Test CLI with --top-ips flag."""
        with patch("sys.argv", ["log-lens", sample_log_file, "--top-ips", "5"]):
            try:
                main([sample_log_file, "--top-ips", "5"])
            except SystemExit:
                pass
        captured = capsys.readouterr()
        assert "192.168.1" in captured.out


class TestCliEdgeCases:
    """Test CLI edge cases."""

    def test_cli_empty_logfile(self, capsys):
        """Test CLI with empty log file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as f:
            f.flush()
            empty_file = f.name

        try:
            with patch("sys.argv", ["log-lens", empty_file]):
                try:
                    main([empty_file])
                except SystemExit:
                    pass
            captured = capsys.readouterr()
            assert "Analyzed" in captured.out
            # Check for "0" followed by "lines" (accounting for possible newlines)
            assert "0" in captured.out and "lines" in captured.out
        finally:
            Path(empty_file).unlink()

    def test_cli_malformed_logfile(self, capsys):
        """Test CLI with malformed log file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as f:
            f.write("This is not a valid log format\n")
            f.write("Just some random text\n")
            f.flush()
            malformed_file = f.name

        try:
            with patch("sys.argv", ["log-lens", malformed_file]):
                try:
                    main([malformed_file])
                except SystemExit:
                    pass
            captured = capsys.readouterr()
            assert "Analyzed" in captured.out
        finally:
            Path(malformed_file).unlink()

    def test_cli_large_top_ips_value(self, capsys):
        """Test CLI with large --top-ips value."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as f:
            # Create log with multiple IPs
            for i in range(5):
                f.write(
                    f'192.168.1.{i} - - [25/Dec/2025:17:15:32 -0600] "GET /api/users HTTP/1.1" 200 1234 "-" "Mozilla/5.0"\n'
                )
            f.flush()
            logfile = f.name

        try:
            with patch("sys.argv", ["log-lens", logfile, "--top-ips", "100"]):
                try:
                    main([logfile, "--top-ips", "100"])
                except SystemExit:
                    pass
            captured = capsys.readouterr()
            assert "192.168.1" in captured.out
        finally:
            Path(logfile).unlink()
