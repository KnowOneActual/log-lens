<div align="center">
<img src="assets/img/log_lens_logo_v1.webp" alt="Log Lens Logo" width="250">

# Log Lens 🔍

**Lightweight, fast CLI for analyzing Apache/Nginx server logs with auto-format detection, rich formatting, and JSON export.**

</div>

[![PyPI version](https://badge.fury.io/py/log-lens.svg)](https://pypi.org/project/log-lens/)
[![Tests](https://github.com/KnowOneActual/log-lens/actions/workflows/ci.yml/badge.svg)](https://github.com/KnowOneActual/log-lens/actions)
[![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen)](https://github.com/KnowOneActual/log-lens)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

---

## ✨ Features

- ✅ **Auto log format detection** - Apache (Combined), generic, and more
- 🎯 **Status codes analysis** - 200, 404, 500 breakdowns
- 🔝 **Top IPs, paths, & HTTP methods** - Rich table visualization
- 🎨 **Rich CLI output** - Colors, tables, formatted display
- 🧪 **Production ready** - 95% test coverage, strict linting, CI/CD
- 📦 **Pydantic Validation** - Robust data parsing and type safety

---

## 🚀 Quick Start

### Install

```bash
pip install log-lens
```

### Basic Usage

```bash
# Analyze a log file
log-lens /path/to/access.log

# Limit top IPs to 5
log-lens access.log --top-ips 5

# Help
log-lens --help
```

---

## 🛠 Development Setup

### Prerequisites
- Python 3.9+
- Poetry
- Git

### Install Development Environment

```bash
git clone https://github.com/KnowOneActual/log-lens.git
cd log-lens

# Install with dependencies
poetry install

# Install pre-commit hooks
poetry run pre-commit install
```

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=log_lens tests/
```

### Code Quality

```bash
# Lint and format with Ruff
poetry run ruff check .
poetry run ruff format .

# Type check with mypy
poetry run mypy src/log_lens/

# Run ALL checks at once
poetry run pre-commit run --all-files
```

---

## 🏗 Project Structure

```
log-lens/
├── src/log_lens/         # Main package
│   ├── core/            # Analytics and reporting
│   ├── models/          # Pydantic data models
│   ├── cli.py           # CLI entry point
│   └── parser.py        # Log parsing logic
├── tests/               # Test suite (95% coverage)
├── docs/                # Documentation
├── pyproject.toml       # Project metadata & dependencies
├── GEMINI.md            # AI context (local-only)
└── README.md            # This file
```

---

## 🔧 Technical Stack

- **Language:** Python 3.9+
- **CLI Framework:** Click
- **UI:** Rich
- **Validation:** Pydantic v2
- **Testing:** pytest + pytest-cov
- **Quality:** Ruff, Mypy, pre-commit

---

## 📊 Specifications

### Supported Log Formats
- Apache access logs
- Generic syslog format
- Custom logs with log levels

### Parsed Data
- **Status codes** - HTTP response codes (200, 404, 500, etc.)
- **IP addresses** - Source IPs and frequency
- **HTTP methods** - GET, POST, HEAD, etc.
- **Request paths** - Top accessed endpoints
- **Log levels** - DEBUG, INFO, WARNING, ERROR, CRITICAL

---

## 📈 Performance

- **Speed:** ~5000 lines/sec on typical hardware
- **Memory:** Minimal (~10MB for 100k log lines)
- **Output:** Rich tables with ANSI colors

---

## 🐛 Troubleshooting

### "Log format not detected"
The file might be in an unsupported format. Check [JSON_SCHEMA.md](JSON_SCHEMA.md).

### "Permission denied"
Ensure you have read permissions:
```bash
chmod +r /path/to/log/file
```

### Tests failing?
See [PRE_COMMIT_CHECKLIST.md](PRE_COMMIT_CHECKLIST.md) for debugging.

---

## 📜 License

MIT License - See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

Made with ❤️ using:
- [Rich](https://rich.readthedocs.io/) - Beautiful terminal output
- [Black](https://black.readthedocs.io/) - Code formatting
- [pre-commit](https://pre-commit.com/) - Git hooks
- [pytest](https://pytest.org/) - Testing framework

---

**Questions?** [Open an issue](https://github.com/KnowOneActual/log-lens/issues/new) or [start a discussion](https://github.com/KnowOneActual/log-lens/discussions/new).

**Happy analyzing!** 🔍✨
