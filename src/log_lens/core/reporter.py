from rich import print as rprint
from rich.console import Console
from rich.table import Table

console = Console()


def print_report(report: dict) -> None:
    """Pretty print ALL analysis results using Rich."""
    fmt = report.get("format", "unknown")
    rprint(f"[bold magenta]📋 Format:[/bold magenta] {fmt.upper()}")

    if "levels" in report and report["levels"]:
        levels_table = Table(title="Log Levels")
        levels_table.add_column("Level", style="cyan")
        levels_table.add_column("Count", justify="right", style="magenta")
        for level, count in sorted(report["levels"].items(), key=lambda x: x[1], reverse=True):
            levels_table.add_row(level, str(count))
        console.print(levels_table)

    if "status_codes" in report and report["status_codes"]:
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
        for ip, count in sorted(report["ips"].items(), key=lambda x: x[1], reverse=True):
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
