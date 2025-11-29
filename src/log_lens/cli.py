#!/usr/bin/env python3
"""Log Lens CLI entry point."""

import argparse
import sys
from pathlib import Path
from log_lens.parser import parse_log_file


def main():
    parser = argparse.ArgumentParser(description="Analyze server log files")
    parser.add_argument("logfile", help="Path to log file")
    parser.add_argument("--export", help="Export JSON to file")
    
    args = parser.parse_args()
    
    if not Path(args.logfile).exists():
        print(f"Error: {args.logfile} not found", file=sys.stderr)
        sys.exit(1)
    
    # Parse and print results (placeholder for now)
    result = parse_log_file(args.logfile)
    print(f"Analyzed {args.logfile}: {len(result)} lines")
    
    if args.export:
        import json
        Path(args.export).write_text(json.dumps(result, indent=2))
        print(f"Exported to {args.export}")


if __name__ == "__main__":
    main()
