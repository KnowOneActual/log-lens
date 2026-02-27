#!/usr/bin/env python3

"""Command Line Interface for Log Lens."""

import json
from pathlib import Path
from typing import Optional

import click
from rich import print as rprint

from log_lens.core.reporter import print_report
from log_lens.parser import LogParser


@click.command(name="log-lens")
@click.argument("logfile", type=click.Path(exists=True))
@click.option("--export", "-e", help="Export JSON to file")
@click.option("--top-ips", "-t", type=int, default=10, help="Show top N IPs")
def main(logfile: str, export: Optional[str], top_ips: int) -> None:
    """🚀 Analyze server log files"""
    log_path = Path(logfile)

    log_parser = LogParser()
    line_count = 0

    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            log_parser.parse_line(line.strip())
            line_count += 1

    result = log_parser.get_report()

    # Apply top_ips filter to report results if applicable
    if "ips" in result:
        # Sort and slice to respect top_ips
        sorted_ips = dict(sorted(result["ips"].items(), key=lambda x: x[1], reverse=True)[:top_ips])
        result["ips"] = sorted_ips

    rprint(f"[bold green]✅ Analyzed[/bold green] {logfile}: {line_count} lines")

    total_entries = sum(result.get("levels", {}).values()) + sum(
        result.get("status_codes", {}).values()
    )
    rprint(f"[bold blue]📊 Found[/bold blue] {total_entries} entries")

    print_report(result)

    if export:
        Path(export).write_text(json.dumps(result, indent=2), encoding="utf-8")
        rprint(f"[bold green]💾 Exported[/bold green] to {export}")


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
