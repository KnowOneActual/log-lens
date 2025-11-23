import unittest
from log_lens.parser import LogParser

class TestLogParser(unittest.TestCase):
    
    def setUp(self):
        """Runs before every test method."""
        self.parser = LogParser()

    def test_detect_log_levels(self):
        """It should correctly count log levels."""
        line = "2025-01-01 12:00:00 INFO System started"
        self.parser.parse_line(line)
        
        report = self.parser.get_report()
        self.assertEqual(report['levels']['INFO'], 1)

    def test_detect_ip_address(self):
        """It should extract IPv4 addresses."""
        line = "Connection refused from 192.168.1.55"
        self.parser.parse_line(line)
        
        report = self.parser.get_report()
        self.assertEqual(report['ips']['192.168.1.55'], 1)

    def test_mixed_content(self):
        """It should handle lines with both levels and IPs."""
        line = "ERROR: Connection dropped from 10.0.0.1"
        self.parser.parse_line(line)
        
        report = self.parser.get_report()
        self.assertEqual(report['levels']['ERROR'], 1)
        self.assertEqual(report['ips']['10.0.0.1'], 1)

    def test_ignore_garbage(self):
        """It should ignore lines with no relevant info."""
        line = "Just a random line of text with no timestamp or level."
        self.parser.parse_line(line)
        
        report = self.parser.get_report()
        self.assertEqual(len(report['levels']), 0)
        self.assertEqual(len(report['ips']), 0)

if __name__ == '__main__':
    unittest.main()