# Log Lens Development Roadmap

This roadmap outlines prioritized improvements for Log Lens, ordered by logical progression: start with core stability and packaging, then enhance usability, expand features, and finally add polish. Each phase builds on the previous one.

## Phase 1: Core Stability & Packaging (Week 1)

- **Move code to single package structure**: Consolidate under `src/log_lens/` and clean up redundant directories (`log_lens/` at root).
- **Add `pyproject.toml`**: Enable `pip install -e .` and proper packaging with console script entrypoint `log-lens`.
- **Expand tests**: Add CLI tests, error handling, JSON export coverage.
- **Add type hints**: Run `mypy` locally and in CI.

*Goal*: Make the project installable and testable like a real Python package.

## Phase 2: CLI Ergonomics (Week 2)

- **Upgrade CLI with `argparse` or `typer`**: Add flags `--top-ips`, `--since`, `--level`, `--format`, `--follow`.
- **Pretty output**: Use `tabulate` or `rich` for tables, colorize log levels.
- **Set up linting/CI**: `black`, `isort`, `ruff` via `pre-commit` and GitHub Actions.

*Goal*: Professional command-line experience that users love.

## Phase 3: Enhanced Analysis (Week 3)

- **Pluggable parsers**: Support Apache/Nginx logs with `--format` flag and auto-detection.
- **New metrics**: Status codes, top paths, requests per time unit, error rate trends.
- **Structured JSON schema**: Document stable output format.

*Goal*: Analyze real-world logs from different servers.

## Phase 4: Documentation & Polish (Week 4)

- **README overhaul**: Pip install instructions, CLI examples, log format docs, JSON schema.
- **Docs folder**: End-to-end examples with sample logs.
- **CHANGES.md updates**: Log releases properly.

*Goal*: Users can onboard in 2 minutes.

## Phase 5: Stretch Goals (Ongoing)

- Streaming mode (`--follow` for live logs).
- Config files (TOML/YAML for defaults).
- HTML/Markdown reports.

*Progress*: Track completion with GitHub issues or checkboxes.