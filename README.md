# Log Lens 🔍

[![PyPI version](https://badge.fury.io/py/log-lens.svg)](https://pypi.org/project/log-lens/)
[![Tests](https://github.com/KnowOneActual/log-lens/actions/workflows/ci.yml/badge.svg)](https://github.com/KnowOneActual/log-lens/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Lightweight CLI for analyzing Apache/Nginx server logs.** Auto-detects format, extracts status codes, top IPs/paths, HTTP methods, and exports JSON.

## 🚀 Features

- **Auto log format detection** (Apache, generic logs)
- **Status codes** (200, 404, 500 analysis)
- **Top IPs, paths, & methods** with beautiful tables
- **Rich CLI** with colors & professional formatting
- **JSON export** for dashboards/tools
- **Production ready** (tests, linting, CI)

## 🛠 Quick Install

```bash
pip install log-lens
```

Or from source:
```bash
git clone https://github.com/KnowOneActual/log-lens.git
cd log-lens
pip install -e .
```

## 📖 Usage Examples

**Basic analysis:**
```bash
log-lens access.log
```

**Apache access logs:**
```bash
log-lens /var/log/apache2/access.log
```

**Export JSON + limit IPs:**
```bash
log-lens access.log --top-ips 5 -e report.json
```

## 🎨 Sample Output

```
✅ Analyzed access.log: 1,234 lines
📊 Found 1,234 entries
📋 Format: APACHE

┌──────────────┐     ┌──────────────┐
│ Status Codes │     │   Top IPs    │
├──────────────┼─────┼──────────────┤
│     200      │ 892 │  192.1.2.3  │ 156
│     404      │  45 │  10.0.0.15  │  89
└──────────────┘     └──────────────┘
```

## 🧪 Development

```bash
# Install dev tools
pip install -e .[dev]

# Run tests
pytest tests/

# Format code
pre-commit run --all-files
```

## 📄 JSON Schema

```json
{
  "format": "apache",
  "ips": {"192.168.1.1": 42},
  "status_codes": {"200": 892, "404": 45},
  "top_paths": {"/": 156, "/api/login": 23}
}
```

## 🤝 Contributing

1. Fork & clone
2. `pip install -e .[dev]`
3. `pre-commit install`
4. Add tests in `tests/`
5. Submit PR!

## 📈 Roadmap

See [ROADMAP.md](ROADMAP.md)

---

**Made with ❤️ using [Rich](https://rich.readthedocs.io), [Black](https://black.readthedocs.io), [pre-commit](https://pre-commit.com)**