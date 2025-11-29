#!/usr/bin/env python3
"""Log Lens CLI entry point."""

import argparse
import sys
import json
from pathlib import Path
from log_lens.parser import LogParser


def main():
    parser = argparse.ArgumentParser(description="Analyze server log files")
    parser.add_argument("logfile", help="Path to log file")
    parser.add_argument("--export", help="Export JSON to file")
    
    args = parser.parse_args()
    
    if not Path(args.logfile).exists():
        print(f"Error: {args.logfile} not found", file=sys.stderr)
        sys.exit(1)
    
    # Use REAL LogParser class
    log_parser = LogParser()
    
    with open(args.logfile, 'r') as f:
        for line in f:
            log_parser.parse_line(line.strip())
    
    result = log_parser.get_report()
    print(f"Analyzed {args.logfile}: {sum(result['levels'].values())} log entries")
    print(f"Top IP: {max(result['ips'], key=result['ips'].get) if result['ips'] else 'None'}")
    
    if args.export:
        Path(args.export).write_text(json.dumps(result, indent=2))
        print(f"Exported to {args.export}")


if __name__ == "__main__":
    main()
