"""Advanced web log parsers for Apache/Nginx."""

import re
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Optional


@dataclass
class LogEntry:
    ip: str
    timestamp: Optional[datetime]
    method: str
    path: str
    status: int
    size: int
    user_agent: str


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

    def parse_line(self, line: str) -> None:
        match = self.APACHE_PATTERN.search(line)
        if match:
            data = match.groupdict()
            ip = data["ip"]
            status = int(data["status"])
            path = data["path"]
            method = data["method"]

            self.ips[ip] += 1
            self.status_codes[status] += 1
            self.paths[path] += 1
            self.methods[method] += 1
            self.entries["total"] += 1

    def get_report(self) -> Dict[str, Any]:
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
        self.parser: Optional[ApacheParser] = None

    def parse_line(self, line: str) -> None:
        # Backward compatibility + new Apache parsing
        # Try log levels (old behavior)
        level_match = re.search(r"(INFO|WARN|WARNING|ERROR|CRITICAL|DEBUG)", line)
        if level_match:
            self.log_counts[level_match.group(1)] += 1

        ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        if ip_match:
            self.ip_counts[ip_match.group(0)] += 1

        # Try Apache format
        apache_parser = ApacheParser()
        apache_parser.parse_line(line)
        if apache_parser.entries:
            self.format = "apache"
            self.parser = apache_parser

    def get_report(self) -> Dict[str, Any]:
        if self.parser is not None:
            return self.parser.get_report()
        return {
            "format": self.format,
            "levels": dict(self.log_counts),
            "ips": dict(self.ip_counts),
        }
