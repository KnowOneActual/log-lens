#!/usr/bin/env python3
"""Log Lens CLI - Phase 3 with web metrics."""

import argparse
import json
import sys
from pathlib import Path
from typing import Optional, Sequence

from rich import print as rprint
from rich.console import Console
from rich.table import Table

from log_lens.parser import LogParser

console = Console()


def print_report(report: dict) -> None:
    """Pretty print ALL analysis results."""

    # Format detection
    fmt = report.get("format", "unknown")
    rprint(f"[bold magenta]📋 Format:[/bold magenta] {fmt.upper()}")

    # Log Levels (old format) OR Status Codes (Apache)
    if "levels" in report and report["levels"]:
        levels_table = Table(title="Log Levels")
        levels_table.add_column("Level", style="cyan")
        levels_table.add_column("Count", justify="right", style="magenta")
        for level, count in sorted(
            report["levels"].items(), key=lambda x: x[1], reverse=True
        ):
            levels_table.add_row(level, str(count))
        console.print(levels_table)

    elif "status_codes" in report and report["status_codes"]:
        status_table = Table(title="Status Codes")
        status_table.add_column("Code", style="cyan")
        status_table.add_column("Count", justify="right", style="magenta")
        for code, count in sorted(
            report["status_codes"].items(), key=lambda x: x[1], reverse=True
        ):
            status_table.add_row(str(code), str(count))
        console.print(status_table)

    # Top IPs
    if report.get("ips"):
        ips_table = Table(title="Top IPs")
        ips_table.add_column("IP", style="green")
        ips_table.add_column("Count", justify="right", style="yellow")
        for ip, count in sorted(
            report["ips"].items(), key=lambda x: x[1], reverse=True
        )[:10]:
            ips_table.add_row(ip, str(count))
        console.print(ips_table)

    # Top Paths (NEW!)
    if report.get("top_paths"):
        paths_table = Table(title="Top Paths")
        paths_table.add_column("Path", style="blue")
        paths_table.add_column("Count", justify="right", style="yellow")
        for path, count in report["top_paths"].items():
            paths_table.add_row(path, str(count))
        console.print(paths_table)

    # Methods (NEW!)
    if report.get("methods"):
        methods_table = Table(title="HTTP Methods")
        methods_table.add_column("Method", style="bold magenta")
        methods_table.add_column("Count", justify="right", style="green")
        for method, count in sorted(
            report["methods"].items(), key=lambda x: x[1], reverse=True
        ):
            methods_table.add_row(method, str(count))
        console.print(methods_table)


def main(args: Optional[Sequence[str]] = None) -> None:
    """Main CLI entry point.

    Args:
        args: Optional list of command line arguments. If None, uses sys.argv.
    """
    parser = argparse.ArgumentParser(description="🚀 Analyze server log files")
    parser.add_argument("logfile", help="Path to log file")
    parser.add_argument("--export", "-e", help="Export JSON to file")
    parser.add_argument("--top-ips", "-t", type=int, default=10, help="Show top N IPs")

    parsed_args = parser.parse_args(args)

    if not Path(parsed_args.logfile).exists():
        rprint(f"[red]Error:[/red] {parsed_args.logfile} not found")
        sys.exit(1)

    log_parser = LogParser()
    line_count = 0

    with open(parsed_args.logfile, "r") as f:
        for line in f:
            log_parser.parse_line(line.strip())
            line_count += 1

    result = log_parser.get_report()

    rprint(f"[bold green]✅ Analyzed[/bold green] {parsed_args.logfile}: {line_count} lines")

    # FIXED: Use 'result' not 'report'
    total_entries = sum(result.get("levels", {}).values()) + sum(
        result.get("status_codes", {}).values()
    )
    rprint(f"[bold blue]📊 Found[/bold blue] {total_entries} entries")

    print_report(result)

    if parsed_args.export:
        Path(parsed_args.export).write_text(json.dumps(result, indent=2))
        rprint(f"[bold green]💾 Exported[/bold green] to {parsed_args.export}")


if __name__ == "__main__":
    main()
