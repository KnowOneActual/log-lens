import pytest
from log_lens.parser import LogParser

class TestLogParser:
    def test_basic_parsing(self):
        parser = LogParser()
        parser.parse_line("192.168.1.1 INFO: User login")
        parser.parse_line("192.168.1.2 ERROR: DB failed")
        
        report = parser.get_report()
        assert report["levels"]["INFO"] == 1
        assert report["levels"]["ERROR"] == 1
        assert "192.168.1.1" in report["ips"]
    
    def test_ip_extraction(self):
        parser = LogParser()
        parser.parse_line("Client 192.168.1.100 connected")
        report = parser.get_report()
        assert report["ips"]["192.168.1.100"] == 1
    
    def test_no_levels(self):
        parser = LogParser()
        parser.parse_line("Plain text line")
        report = parser.get_report()
        assert len(report["levels"]) == 0
