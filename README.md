<div align="center">
<img src="assets/img/log_lens_logo_v1.webp" alt="Log Lens Logo" width="250">

# Log Lens 🔍

**Lightweight, fast CLI for analyzing Apache/Nginx server logs with auto-format detection, rich formatting, and JSON export.**

</div>

[![PyPI version](https://badge.fury.io/py/log-lens.svg)](https://pypi.org/project/log-lens/)
[![Tests](https://github.com/KnowOneActual/log-lens/actions/workflows/test.yml/badge.svg)](https://github.com/KnowOneActual/log-lens/actions)
[![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen)](https://github.com/KnowOneActual/log-lens)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

---

## ✨ Features

- ✅ **Auto log format detection** - Apache, generic, and more
- 🎯 **Status codes analysis** - 200, 404, 500 breakdowns
- 🔝 **Top IPs, paths, & HTTP methods** - Rich table visualization
- 🎨 **Rich CLI output** - Colors, tables, formatted display
- 📊 **JSON export** - For dashboards, tools, and pipelines
- 🧪 **Production ready** - 95% test coverage, strict linting, CI/CD
- ⚡ **Zero dependencies** in runtime

---

## 🚀 Quick Start

### Install

```bash
pip install log-lens
```

Or from source:
```bash
git clone https://github.com/KnowOneActual/log-lens.git
cd log-lens
pip install -e .
```

### Basic Usage

```bash
# Analyze a log file
log-lens /path/to/access.log

# Export to JSON
log-lens access.log -e report.json

# Limit top IPs to 5
log-lens access.log --top-ips 5

# Help
log-lens --help
```

---

## 📖 Usage Examples

### Apache Access Logs

```bash
log-lens /var/log/apache2/access.log
```

**Output:**
```
✅ Analyzed /var/log/apache2/access.log: 1,234 lines
📊 Found 1,234 entries
📋 Format: APACHE

┌────────────────┐      ┌────────────────┐
│  Status Codes  │      │    Top IPs     │
├────────────────┤      ├────────────────┤
│ 200 │    892   │      │ 192.168.1.100  │ 156
│ 404 │     45   │      │ 10.0.0.15      │  89
│ 500 │      8   │      │ 172.16.0.50    │  42
└────────────────┘      └────────────────┘

┌────────────────────┐     ┌───────────────────┐
│    HTTP Methods    │     │   Top Paths       │
├────────────────────┤     ├───────────────────┤
│ GET  │    945     │     │ /                 │ 234
│ POST │     87     │     │ /api/login        │  89
│ HEAD │    134     │     │ /assets/style.css │  67
└────────────────────┘     └───────────────────┘
```

### Export JSON for Dashboards

```bash
log-lens access.log -e metrics.json

cat metrics.json
```

**Output:**
```json
{
  "format": "apache",
  "ips": {
    "192.168.1.100": 156,
    "10.0.0.15": 89
  },
  "status_codes": {
    "200": 892,
    "404": 45,
    "500": 8
  },
  "top_paths": {
    "/": 234,
    "/api/login": 89,
    "/assets/style.css": 67
  },
  "methods": {
    "GET": 945,
    "POST": 87,
    "HEAD": 134
  }
}
```

### Limit Results

```bash
# Show only top 5 IPs
log-lens access.log --top-ips 5
```

---

## 🛠 Development Setup

### Prerequisites
- Python 3.12+
- Poetry
- Git

### Install Development Environment

```bash
git clone https://github.com/KnowOneActual/log-lens.git
cd log-lens

# Install with dev dependencies
pip install -e '.[dev]'

# Install pre-commit hooks (auto-formatting)
poetry run pre-commit install
```

### Running Tests

```bash
# Run all tests
poetry run pytest tests/ -v

# Run with coverage
poetry run pytest tests/ -v --cov=log_lens

# Run specific test
poetry run pytest tests/test_cli.py::TestCliIntegration -v
```

**Expected output (95% coverage):**
```
========== 11 passed in 0.24s ==========
---------- coverage: platform darwin, python 3.12.2-final-0 ----------
Name                   Stmts   Miss  Cover
------------------------------------------
log_lens/__init__.py       4      0   100%
log_lens/cli.py           73      7    90%
log_lens/parser.py        52      0   100%
------------------------------------------
TOTAL                    129      7    95%
```

### Code Quality

```bash
# Format code
poetry run black log_lens/ tests/

# Sort imports
poetry run isort log_lens/ tests/

# Lint
poetry run ruff check log_lens/ tests/

# Run ALL checks at once
poetry run pre-commit run --all-files
```

---

## 📋 Pre-Commit Checklist

**Always run this before committing:**

```bash
# Run tests
poetry run pytest tests/ -v --cov=log_lens

# Run all formatters & linters
poetry run pre-commit run --all-files
```

**See [PRE_COMMIT_CHECKLIST.md](PRE_COMMIT_CHECKLIST.md) for detailed workflow.**

If formatters modify files:
```bash
git add .
git commit -m "style: format code"
poetry run pre-commit run --all-files  # Re-run to verify
```

---

## 🤝 Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Development workflow
- Commit message format
- Testing requirements
- PR guidelines

**Quick summary:**
1. Fork & clone
2. `pip install -e '.[dev]'`
3. `poetry run pre-commit install`
4. Make changes + write tests
5. `poetry run pytest tests/ -v --cov=log_lens` (must pass)
6. `poetry run pre-commit run --all-files` (must pass)
7. Commit & push
8. Submit PR

---

## 📚 Documentation

- **[README.md](README.md)** - This file, getting started
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Development workflow & guidelines
- **[PRE_COMMIT_CHECKLIST.md](PRE_COMMIT_CHECKLIST.md)** - Testing checklist before commits
- **[CHANGELOG.md](CHANGELOG.md)** - Version history
- **[JSON_SCHEMA.md](JSON_SCHEMA.md)** - JSON export format
- **[docs/](docs/)** - Additional documentation

---

## 🏗 Project Structure

```
log-lens/
├── log_lens/              # Main package
│   ├── __init__.py
│   ├── cli.py            # CLI entry point
│   └── parser.py         # Log parsing logic
├── tests/                # Test suite (11 tests, 95% coverage)
│   ├── test_cli.py
│   └── test_parser.py
├── docs/                 # Documentation
├── pyproject.toml        # Project metadata & dependencies
├── poetry.lock           # Locked dependencies
├── README.md             # This file
├── CONTRIBUTING.md       # Contribution guidelines
├── PRE_COMMIT_CHECKLIST.md  # Pre-commit testing
└── .pre-commit-config.yaml  # Auto-formatting hooks
```

---

## 🔧 Technical Stack

- **Language:** Python 3.12+
- **Package Manager:** Poetry
- **Testing:** pytest + pytest-cov (95% coverage)
- **Code Quality:**
  - Black (formatting)
  - isort (import sorting)
  - Ruff (linting)
  - pre-commit (hooks)
- **CLI:** Rich library for beautiful output
- **CI/CD:** GitHub Actions

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
