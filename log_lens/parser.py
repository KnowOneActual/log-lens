import re
from collections import Counter

class LogParser:
    def __init__(self):
        # Counter is a specialized dictionary that defaults to 0
        self.log_counts = Counter()
        # Regex to find uppercase log levels (e.g., INFO, WARN)
        self.level_pattern = re.compile(r"(INFO|WARN|WARNING|ERROR|CRITICAL|DEBUG)")

    def parse_line(self, line):
        """
        Scans a single line for log levels and updates the counter.
        """
        match = self.level_pattern.search(line)
        if match:
            # extracting the level found (e.g., "ERROR")
            level = match.group(1)
            self.log_counts[level] += 1

    def get_report(self):
        """
        Returns the dictionary of counts.
        """
        return dict(self.log_counts)