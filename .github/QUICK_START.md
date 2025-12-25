# Quick Start Guide - Log Lens Development

Welcome to Log Lens! This guide will get you up and running in minutes.

## TL;DR

```bash
# 1. Clone and setup
git clone https://github.com/KnowOneActual/log-lens.git
cd log-lens
poetry install
pre-commit install

# 2. Run tests
poetry run pytest

# 3. Try it out
poetry run log-lens tests/fixtures/apache_access.log

# 4. Start coding!
git checkout -b feat/your-feature
# ... make changes ...
poetry run pytest
git commit -m "feat: your feature"
git push origin feat/your-feature
```

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Git
- Poetry (install via https://install.python-poetry.org)

### Setup

```bash
# Clone repository
git clone https://github.com/KnowOneActual/log-lens.git
cd log-lens

# Install dependencies
poetry install

# Activate virtual environment
poetry shell
# OR use: poetry run <command>

# Set up git hooks
pre-commit install
```

---

## Running the CLI

```bash
# Basic usage
poetry run log-lens <log-file>

# Examples
poetry run log-lens /var/log/apache2/access.log
poetry run log-lens access.log --top-ips 10 --export report.json
poetry run log-lens access.log -v  # Verbose mode
```

---

## Development Commands

### Testing
```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=src/log_lens

# Run specific test file
poetry run pytest tests/test_parser.py

# Run with verbose output
poetry run pytest -v
```

### Code Quality
```bash
# Format code
poetry run black src/ tests/

# Sort imports
poetry run isort src/ tests/

# Lint
poetry run pylint src/log_lens/

# Type check
poetry run mypy src/log_lens/

# Run all checks (pre-commit)
pre-commit run --all-files
```

### Debugging
```bash
# Verbose output
poetry run log-lens file.log -v

# Use Python debugger
# Add this to your code: import pdb; pdb.set_trace()
```

---

## Project Structure

```
log-lens/
├── src/log_lens/          # Main package
├── tests/                 # Tests
├── docs/                  # Documentation
├── pyproject.toml         # Project config
├── README.md              # Overview
└─┐ CONTRIBUTING.md        # Guidelines
```

---

## Common Tasks

### Add a new feature

1. Create branch: `git checkout -b feat/my-feature`
2. Implement feature with tests
3. Run tests: `poetry run pytest --cov`
4. Commit: `git commit -m "feat: my feature"`
5. Push: `git push origin feat/my-feature`
6. Open pull request on GitHub

### Fix a bug

1. Create branch: `git checkout -b fix/bug-name`
2. Add test that reproduces bug
3. Implement fix
4. Verify test passes
5. Commit: `git commit -m "fix: brief description"`
6. Push and create PR

### Add a test

```python
# In tests/test_parser.py
import pytest
from log_lens.parser import parse_log

def test_parses_apache_log():
    # Arrange
    log_file = Path('tests/fixtures/apache_access.log')
    
    # Act
    entries = list(parse_log(log_file))
    
    # Assert
    assert len(entries) > 0
    assert entries[0].ip_address is not None
```

### Update documentation

- User guide: `README.md`
- Architecture: `docs/ARCHITECTURE.md`
- Development: `docs/DEVELOPMENT.md`
- Roadmap: `docs/ROADMAP.md`
- Examples: `docs/examples/`

---

## Useful Resources

### Project Docs
- [README](../README.md) - Project overview
- [ROADMAP](docs/ROADMAP.md) - Development plan
- [ARCHITECTURE](docs/ARCHITECTURE.md) - Technical design
- [DEVELOPMENT](docs/DEVELOPMENT.md) - Detailed guide

### External References
- [Poetry Documentation](https://python-poetry.org/docs/)
- [pytest Guide](https://docs.pytest.org/)
- [Click CLI Framework](https://click.palletsprojects.com/)
- [Rich Terminal Library](https://rich.readthedocs.io/)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

## Troubleshooting

### Poetry not found
```bash
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"
```

### Tests failing after changes
```bash
# Make sure you're using the latest code
poetry install
poetry run pytest --cache-clear
```

### Import errors
```bash
# Reinstall package in editable mode
poetry install
```

### Pre-commit hook issues
```bash
# Skip pre-commit temporarily
git commit --no-verify

# Or fix issues
pre-commit run --all-files
```

---

## Need Help?

- 📄 Check [DEVELOPMENT.md](docs/DEVELOPMENT.md) for detailed guide
- 🔍 Search [existing issues](https://github.com/KnowOneActual/log-lens/issues)
- 🗣️ Open a new issue with `question` label
- 🤝 Check [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines

---

## Phase 1 Tasks

Looking for something to work on? Check out Phase 1 tasks:

1. [#1 Parser Refactoring](https://github.com/KnowOneActual/log-lens/issues/1) - Medium effort
2. [#2 Test Coverage](https://github.com/KnowOneActual/log-lens/issues/2) - Good for onboarding
3. [#3 Nginx Support](https://github.com/KnowOneActual/log-lens/issues/3) - Advanced
4. [#4 CLI Improvements](https://github.com/KnowOneActual/log-lens/issues/4) - Medium effort
5. [#5 Documentation](https://github.com/KnowOneActual/log-lens/issues/5) - Good for onboarding

---

**Happy coding! 🚀**
