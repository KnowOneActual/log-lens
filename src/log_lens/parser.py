import re
from collections import Counter


class LogParser:
    def __init__(self):
        self.log_counts = Counter()
        self.ip_counts = Counter()  # New counter for IPs

        # Regex for standard log levels
        self.level_pattern = re.compile(r"(INFO|WARN|WARNING|ERROR|CRITICAL|DEBUG)")

        # Regex for IPv4 addresses (Simple version)
        self.ip_pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

    def parse_line(self, line):
        # 1. Check for Log Level
        match_level = self.level_pattern.search(line)
        if match_level:
            self.log_counts[match_level.group(1)] += 1

        # 2. Check for IP Address
        match_ip = self.ip_pattern.search(line)
        if match_ip:
            self.ip_counts[match_ip.group(0)] += 1

    def get_report(self):
        return {"levels": dict(self.log_counts), "ips": dict(self.ip_counts)}
