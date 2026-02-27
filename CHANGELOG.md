# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.7.0] - 2026-02-27
### Added
- **Modular Architecture**: Introduced `models/` and `core/` sub-packages for better code organization.
- **Reporting Engine**: Extracted Rich CLI reporting into `src/log_lens/core/reporter.py`.
- **Package Discovery**: Added `test` script shortcut to `pyproject.toml`.

### Changed
- **Project Layout**: Migrated to the modern `src/` layout (moved code to `src/log_lens/`).
- **Improved Performance**: Optimized `LogParser` by persisting the `ApacheParser` instance across lines.

### Fixed
- **Data Loss Bug**: Fixed a critical issue where `ApacheParser` was re-initialized for every line, causing only the last line's data to be retained.
- **Repository Cleanup**: Removed redundant `log_lens/` root directory and artifact files (`report.json`, `results.json`).

## [0.6.0] - 2023-08-31
### Added

* Official support for Python 3.13 and 3.14 in project metadata and CI workflows.

### Changed

* Migrated the CLI framework from `argparse` to `Click` to improve command-line handling and testability.
* Consolidated linting and formatting tools by moving to a `ruff`-only configuration, replacing standalone `black` and `isort` hooks to prevent formatting conflicts in CI.
* Updated integration tests to utilize `click.testing.CliRunner` for more reliable command-line validation.

### Fixed

* Resolved `AttributeError: 'function' object has no attribute 'name'` errors in the test suite by correctly decorating the main entry point as a Click command.
* Fixed `E501` line-length violations in test files by refactoring long log strings to stay within the 100-character limit.
* Synchronized `poetry.lock` with `pyproject.toml` to resolve dependency environment mismatches during CI runs.



---

## [0.4.0] - 2025-12-25
### Fixed
- **Package Structure**: Migrated from `src/` layout to root-level `log_lens/` package
- **Poetry Configuration**: Switched from Hatchling to Poetry-native build system
- **Python Version**: Updated minimum Python requirement to 3.9+ (pre-commit compatibility)
- **Type Hints**: Added comprehensive type annotations to parser.py for mypy compliance
- **Code Formatting**: Applied Black formatting standards across codebase
- **Dependencies**: Pinned all dev dependencies with proper version constraints
- **GitHub Actions**: Fixed CI workflow for proper testing and coverage reporting

### Added
- **Type Safety**: Full mypy type checking with no errors
- **Dev Tools**: Black, isort, mypy, pytest, pytest-cov, ruff, pre-commit, pylint
- **Quality Assurance**: All linting and formatting checks passing
- **Test Coverage**: Comprehensive test suite with 11 tests

### Changed
- Simplified pyproject.toml configuration (removed Hatchling complexity)
- Updated classifiers to Python 3.9+
- Improved package discovery with Poetry defaults

## [0.3.0] - 2025-11-29
### Added
- **Phase 3**: Apache/Nginx log parsing (status codes, paths, HTTP methods)
- Auto log format detection
- 5 Rich tables (Status Codes, Top IPs, Top Paths, HTTP Methods, Log Levels)
- **Phase 4**: Professional README + sample_access.log + JSON_SCHEMA.md

## [0.2.0] - 2025-11-28
### Added
- **Phase 2**: Rich CLI with colors, tables, emojis
- New flags: `--top-ips N`, `--export`
- Pre-commit hooks (black, isort, ruff)

## [0.1.0] - 2025-11-27
### Added
- **Phase 1**: Professional packaging (`pyproject.toml`)
- `src/log_lens/` structure
- Working `log-lens` CLI command
- Pytest suite (3 tests passing)

## [0.0.1] - 2025-11-23
### Added
- Core `LogParser` with regex log level detection
- IPv4 address extraction and ranking
- JSON export functionality
- Basic CLI interface
- Initial unit tests

---
## [Unreleased]
### Added
- **Comprehensive Documentation**:
  - `PRE_COMMIT_CHECKLIST.md`: Step-by-step testing checklist before commits
  - Enhanced `README.md`: Complete rewrite with usage examples, setup guide, troubleshooting
  - Enhanced `CONTRIBUTING.md`: Detailed development workflow with commit message format
- **Test Suite Improvements**:
  - 11 passing tests with 95% code coverage
  - CLI integration tests (basic help, missing logfile, analyze, export, flags, edge cases)
  - Parser unit tests (basic parsing, IP extraction, no levels)
  - Edge case tests (empty files, malformed logs, large values)
- **Quality Metrics**:
  - 100% coverage on `__init__.py` and `parser.py`
  - 90% coverage on `cli.py`

### Changed
- Improved documentation clarity and completeness
- Enhanced CONTRIBUTING.md with 7-step development workflow
- Added test coverage badges to README

### Fixed
- Fixed pre-commit hook configuration to pass all formatters
- Resolved Black and isort formatting issues


**Follow [docs/ROADMAP.md](docs/roadmap.md) for v1.0 release!**
