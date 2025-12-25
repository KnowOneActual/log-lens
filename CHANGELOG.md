# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.0] - 2025-12-25
### Fixed
- **Package Structure**: Migrated from `src/` layout to root-level `log_lens/` package
- **Poetry Configuration**: Switched from Hatchling to Poetry-native build system
- **Python Version**: Updated minimum Python requirement to 3.9+ (pre-commit compatibility)
- **Type Hints**: Added comprehensive type annotations to parser.py for mypy compliance
- **Code Formatting**: Applied Black formatting standards across codebase
- **Dependencies**: Pinned all dev dependencies with proper version constraints

### Added
- **Type Safety**: Full mypy type checking with no errors
- **Dev Tools**: Black, isort, mypy, pytest, pytest-cov, ruff, pre-commit, pylint
- **Quality Assurance**: All linting and formatting checks passing

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

**Follow [ROADMAP.md](ROADMAP.md) for v1.0 release!**
