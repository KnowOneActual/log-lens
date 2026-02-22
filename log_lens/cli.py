#!/usr/bin/env python3

import json
from pathlib import Path
from typing import Optional

import click
from rich import print as rprint
from rich.console import Console
from rich.table import Table

from log_lens.parser import LogParser

console = Console()


def print_report(report: dict) -> None:
    """Pretty print ALL analysis results."""
    fmt = report.get("format", "unknown")
    rprint(f"[bold magenta]📋 Format:[/bold magenta] {fmt.upper()}")

    if "levels" in report and report["levels"]:
        levels_table = Table(title="Log Levels")
        levels_table.add_column("Level", style="cyan")
        levels_table.add_column("Count", justify="right", style="magenta")
        for level, count in sorted(report["levels"].items(), key=lambda x: x[1], reverse=True):
            levels_table.add_row(level, str(count))
        console.print(levels_table)

    elif "status_codes" in report and report["status_codes"]:
        status_table = Table(title="Status Codes")
        status_table.add_column("Code", style="cyan")
        status_table.add_column("Count", justify="right", style="magenta")
        for code, count in sorted(report["status_codes"].items(), key=lambda x: x[1], reverse=True):
            status_table.add_row(str(code), str(count))
        console.print(status_table)

    if report.get("ips"):
        ips_table = Table(title="Top IPs")
        ips_table.add_column("IP", style="green")
        ips_table.add_column("Count", justify="right", style="yellow")
        for ip, count in sorted(report["ips"].items(), key=lambda x: x[1], reverse=True)[:10]:
            ips_table.add_row(ip, str(count))
        console.print(ips_table)

    if report.get("top_paths"):
        paths_table = Table(title="Top Paths")
        paths_table.add_column("Path", style="blue")
        paths_table.add_column("Count", justify="right", style="yellow")
        for path, count in report["top_paths"].items():
            paths_table.add_row(path, str(count))
        console.print(paths_table)

    if report.get("methods"):
        methods_table = Table(title="HTTP Methods")
        methods_table.add_column("Method", style="bold magenta")
        methods_table.add_column("Count", justify="right", style="green")
        for method, count in sorted(report["methods"].items(), key=lambda x: x[1], reverse=True):
            methods_table.add_row(method, str(count))
        console.print(methods_table)


@click.command(name="log-lens")
@click.argument("logfile", type=click.Path(exists=True))
@click.option("--export", "-e", help="Export JSON to file")
@click.option("--top-ips", "-t", type=int, default=10, help="Show top N IPs")
def main(logfile: str, export: Optional[str], top_ips: int) -> None:
    """🚀 Analyze server log files"""
    log_path = Path(logfile)

    log_parser = LogParser()
    line_count = 0

    with open(log_path, "r") as f:
        for line in f:
            log_parser.parse_line(line.strip())
            line_count += 1

    result = log_parser.get_report()

    rprint(f"[bold green]✅ Analyzed[/bold green] {logfile}: {line_count} lines")

    total_entries = sum(result.get("levels", {}).values()) + sum(
        result.get("status_codes", {}).values()
    )
    rprint(f"[bold blue]📊 Found[/bold blue] {total_entries} entries")

    print_report(result)

    if export:
        Path(export).write_text(json.dumps(result, indent=2))
        rprint(f"[bold green]💾 Exported[/bold green] to {export}")


if __name__ == "__main__":
    main()
