#!/usr/bin/env python3
"""Log Lens CLI - Professional output with rich."""

import argparse
import sys
import json
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich import print as rprint
from log_lens.parser import LogParser

console = Console()


def print_report(report: dict):
    """Pretty print analysis results with rich."""
    
    # Log Levels Table
    if report["levels"]:
        levels_table = Table(title="Log Levels")
        levels_table.add_column("Level", style="cyan")
        levels_table.add_column("Count", justify="right", style="magenta")
        
        for level, count in sorted(report["levels"].items(), key=lambda x: x[1], reverse=True):
            levels_table.add_row(level, str(count))
        console.print(levels_table)
    
    # Top IPs Table (FIXED)
    if report["ips"]:
        ips_table = Table(title="Top IPs")
        ips_table.add_column("IP", style="green")
        ips_table.add_column("Count", justify="right", style="yellow")
        
        for ip, count in sorted(report["ips"].items(), key=lambda x: x[1], reverse=True)[:10]:
            ips_table.add_row(ip, str(count))
        console.print(ips_table)


def main():
    parser = argparse.ArgumentParser(description="🚀 Analyze server log files")
    parser.add_argument("logfile", help="Path to log file")
    parser.add_argument("--export", "-e", help="Export JSON to file")
    parser.add_argument("--top-ips", "-t", type=int, default=10, help="Show top N IPs (default: 10)")
    
    args = parser.parse_args()
    
    if not Path(args.logfile).exists():
        rprint(f"[red]Error:[/red] {args.logfile} not found")
        sys.exit(1)
    
    # Parse with real LogParser
    log_parser = LogParser()
    line_count = 0
    
    with open(args.logfile, 'r') as f:
        for line in f:
            log_parser.parse_line(line.strip())
            line_count += 1
    
    result = log_parser.get_report()
    
    rprint(f"[bold green]✅ Analyzed[/bold green] {args.logfile}: {line_count} lines")
    rprint(f"[bold blue]📊 Found[/bold blue] {sum(result['levels'].values())} log entries")
    
    print_report(result)
    
    if args.export:
        Path(args.export).write_text(json.dumps(result, indent=2))
        rprint(f"[bold green]💾 Exported[/bold green] to {args.export}")


if __name__ == "__main__":
    main()
