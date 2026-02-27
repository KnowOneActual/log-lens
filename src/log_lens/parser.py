"""Advanced web log parsers for Apache/Nginx."""

import re
from collections import Counter
from typing import Any, Dict

from pydantic import ValidationError

from log_lens.models.log_entry import LogEntry


class ApacheParser:
    """Parse Apache combined log format."""

    APACHE_PATTERN = re.compile(
        r"(?P<ip>\S+) "  # IP
        r'\S+ \S+ \[(?P<timestamp>[^]]+)\] "'
        r'(?P<method>\S+) (?P<path>\S+) (?P<protocol>\S+)" '
        r'(?P<status>\d{3}) (?P<size>\d+|-) "[^"]*" "(?P<user_agent>[^"]*)"'
    )

    def __init__(self) -> None:
        self.entries: Counter[str] = Counter()
        self.ips: Counter[str] = Counter()
        self.status_codes: Counter[int] = Counter()
        self.paths: Counter[str] = Counter()
        self.methods: Counter[str] = Counter()

    def parse_line(self, line: str) -> bool:
        """Parse a line and return True if it matched Apache format."""
        match = self.APACHE_PATTERN.search(line)
        if match:
            data = match.groupdict()
            try:
                # Validate with Pydantic
                entry = LogEntry(**data)

                self.ips[entry.ip] += 1
                self.status_codes[entry.status] += 1
                self.paths[entry.path] += 1
                self.methods[entry.method] += 1
                self.entries["total"] += 1
                return True
            except ValidationError:
                # If it matches the regex but fails Pydantic validation,
                # we still return True but don't count it as a success for the whole file?
                # Actually, let's just return False so it can try other parsers if needed.
                return False
        return False

    def get_report(self) -> Dict[str, Any]:
        """Generate a dictionary report of parsed Apache log data."""
        return {
            "format": "apache",
            "summary": dict(self.entries),
            "ips": dict(self.ips.most_common(10)),
            "status_codes": dict(self.status_codes),
            "top_paths": dict(self.paths.most_common(10)),
            "methods": dict(self.methods),
        }


class LogParser:
    """Main parser with format auto-detection."""

    def __init__(self) -> None:
        self.log_counts: Counter[str] = Counter()
        self.ip_counts: Counter[str] = Counter()
        self.format = "unknown"
        self.apache_parser = ApacheParser()

    def parse_line(self, line: str) -> None:
        """Parse a single log line, detecting format and extracting data."""
        # Backward compatibility + new Apache parsing

        # 1. Try Apache format first (more specific)
        if self.apache_parser.parse_line(line):
            self.format = "apache"
            return

        # 2. Fallback to generic log levels (old behavior)
        level_match = re.search(r"(INFO|WARN|WARNING|ERROR|CRITICAL|DEBUG)", line)
        if level_match:
            self.log_counts[level_match.group(1)] += 1

        ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        if ip_match:
            self.ip_counts[ip_match.group(0)] += 1

    def get_report(self) -> Dict[str, Any]:
        """Retrieve the final report from the underlying parser."""
        if self.format == "apache":
            return self.apache_parser.get_report()

        return {
            "format": self.format,
            "levels": dict(self.log_counts),
            "ips": dict(self.ip_counts),
        }
