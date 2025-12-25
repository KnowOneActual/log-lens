# Development Guide

## Getting Started

This guide covers how to set up your development environment and contribute to log-lens.

### Prerequisites
- Python 3.8+
- Git
- Poetry (for dependency management)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KnowOneActual/log-lens.git
   cd log-lens
   ```

2. **Install Poetry** (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install dependencies:**
   ```bash
   poetry install
   ```

4. **Activate virtual environment:**
   ```bash
   poetry shell
   # or use 'poetry run' prefix for individual commands
   ```

5. **Set up pre-commit hooks:**
   ```bash
   pre-commit install
   ```

---

## Development Workflow

### Running the CLI locally

```bash
# From project root
poetry run log-lens tests/fixtures/apache_access.log
```

### Running tests

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=src/log_lens tests/

# Run specific test file
poetry run pytest tests/test_parser.py

# Run with verbose output
poetry run pytest -v
```

### Code quality checks

```bash
# Format code with Black
poetry run black src/ tests/

# Sort imports with isort
poetry run isort src/ tests/

# Lint with pylint
poetry run pylint src/log_lens/

# Type check with mypy
poetry run mypy src/log_lens/

# Run all pre-commit hooks
pre-commit run --all-files
```

---

## Project Structure

See [ARCHITECTURE.md](./ARCHITECTURE.md) for detailed breakdown.

Key directories:
- `src/log_lens/` - Main package code
- `tests/` - Test files
- `docs/` - Documentation
- `pyproject.toml` - Project configuration and dependencies

---

## Adding Features

### 1. Create a feature branch

```bash
git checkout -b feat/your-feature-name
```

### 2. Implement your feature

- Follow Python best practices
- Add type hints to function signatures
- Write docstrings for modules/classes/functions
- Keep functions small and focused

### 3. Write tests

- Create tests in `tests/` with `test_` prefix
- Aim for 90%+ coverage
- Test both happy path and edge cases

Example test file structure:
```python
import pytest
from pathlib import Path
from log_lens.parser import parse_log, detect_format

class TestDetectFormat:
    def test_detects_apache_format(self):
        log_file = Path('tests/fixtures/apache_access.log')
        format_name = detect_format(log_file)
        assert format_name == 'apache'
    
    def test_returns_generic_for_unknown(self):
        # Test with unknown format
        pass
```

### 4. Run quality checks

```bash
poetry run black .
poetry run isort .
poetry run pylint src/log_lens/
poetry run mypy src/log_lens/
poetry run pytest --cov
```

### 5. Commit and push

```bash
git add .
git commit -m "feat: add your feature description"
git push origin feat/your-feature-name
```

Follow [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `test:` - Tests
- `refactor:` - Code refactoring
- `perf:` - Performance improvement
- `chore:` - Build, dependencies, etc.

### 6. Create Pull Request

- Title should follow conventional commits
- Description should explain **why** the change is needed
- Reference any related issues (e.g., "Fixes #123")
- Ensure all checks pass (CI/CD, coverage)

---

## Testing Guidelines

### Test Fixtures

Sample log files are in `tests/fixtures/`. When adding tests:

1. Use existing fixtures if available
2. Add new fixtures for new log formats
3. Include both valid and malformed entries
4. Keep fixtures small (< 100 lines) for quick tests

### Test Organization

```
tests/
├── __init__.py
├── fixtures/
├── test_parser.py
├── test_cli.py
├── test_analyzer.py
├── test_exporter.py
├── conftest.py            # pytest configuration
└── integration/           # End-to-end tests
```

---

## Documentation

### Writing Docstrings

Use Google-style docstrings:

```python
def parse_log(file_path: Path, format_hint: Optional[str] = None) -> Iterator[LogEntry]:
    """Parse log file and yield LogEntry objects.
    
    Auto-detects format if not provided. Gracefully handles unparseable lines
    by logging a warning and continuing.
    
    Args:
        file_path: Path to the log file.
        format_hint: Optionally force a specific format (apache, nginx, generic).
    
    Yields:
        LogEntry objects for each successfully parsed line.
    
    Raises:
        FileNotFoundError: If log file doesn't exist.
        ValueError: If format_hint is not recognized.
    
    Example:
        >>> for entry in parse_log(Path('access.log')):
        ...     print(entry.ip_address, entry.status_code)
    """
    pass
```

### Updating Documentation

- Update `README.md` for user-facing changes
- Update `CHANGELOG.md` with significant changes
- Add examples to `docs/examples/` for new features
- Update `ROADMAP.md` if priority/timeline changes

---

## Debugging

### Verbose mode

```bash
poetry run log-lens access.log -v
```

### Using pdb

```python
import pdb; pdb.set_trace()
```

### Logging

```python
import logging
logger = logging.getLogger(__name__)
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
```

---

## Performance Considerations

- Use generators for large file processing
- Avoid loading entire file into memory
- Pre-compile regex patterns
- Profile with `cProfile` before optimization

```bash
python -m cProfile -s cumtime script.py
```

---

## Release Checklist

Before tagging a new release:

- [ ] All tests passing
- [ ] Coverage maintained (90%+)
- [ ] `CHANGELOG.md` updated
- [ ] `pyproject.toml` version bumped
- [ ] `README.md` reflects current state
- [ ] No breaking changes (or documented in CHANGELOG)
- [ ] Documentation updated
- [ ] Pre-release testing on macOS/Linux

---

## Getting Help

- Check [CONTRIBUTING.md](../CONTRIBUTING.md) for community guidelines
- Open an issue with `question` label
- Start a GitHub Discussion
- Check existing issues/PRs for similar topics

---

## Resources

- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [pytest Documentation](https://docs.pytest.org/)
- [Click Documentation](https://click.palletsprojects.com/)
- [Rich Documentation](https://rich.readthedocs.io/)
