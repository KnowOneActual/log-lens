# Contributing to Log Lens 🔍

Thank you for considering contributing! We welcome contributions of all kinds.  🌟

---

## 🎣 Getting Started

### Prerequisites
- Python 3.9+
- Poetry (package manager)
- Git
- GitHub account (for forking)

### 1. Fork & Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/log-lens.git
cd log-lens
```

### 2. Install Development Environment

```bash
# Install with Poetry:
poetry install
```

### 3. Install Pre-Commit Hooks

This ensures your code is automatically formatted before committing:

```bash
poetry run pre-commit install
```

Now pre-commit hooks will run on every commit!

---

## 🚀 Development Workflow

### Step 1: Create a Feature Branch

```bash
git checkout -b feat/your-feature-name
# or for bug fixes:
git checkout -b fix/issue-name
```

### Step 2: Make Your Changes

Edit files in `src/log_lens/` and `tests/`:

```
src/log_lens/
├── core/            # Analytics and reporting
├── models/          # Pydantic data models
├── cli.py           # CLI entry point (Click commands)
└── parser.py        # Log parsing logic
```

### Step 3: Write Tests

**Always write tests for new features!**

```bash
# Run tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=log_lens tests/
```

**Test requirements:**
- New features must have corresponding tests
- Coverage must stay >= 90% (currently 95%)
- Use descriptive test names
- Test edge cases (empty files, malformed logs, etc.)

**Example test structure:**
```python
def test_feature_description():
    """Test that feature does X when given Y."""
    # Arrange
    test_data = ...  # Set up test data
    
    # Act
    result = my_function(test_data)
    
    # Assert
    assert result == expected_value
```

### Step 4: Format & Lint Your Code

**This is critical before committing!**

Run the pre-commit checklist:

```bash
# Run ALL formatters and linters
poetry run pre-commit run --all-files
```

This runs:
- **Black** - Code formatter
- **isort** - Import sorter
- **Ruff** - Linter + formatter
- **ruff-format** - Additional formatting

**If hooks modify files:**
```bash
# Review the changes
git diff

# Stage them
git add .

# Commit the formatting
git commit -m "style: format code with black/isort/ruff"

# Run hooks again to verify
poetry run pre-commit run --all-files
```

### Step 5: Commit with Proper Message Format

Use semantic commit messages:

```
<type>: <short description>

<optional longer explanation>
```

**Types:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `style:` - Formatting, no code change
- `test:` - Add/update tests
- `chore:` - Maintenance, dependencies
- `refactor:` - Code restructuring

**Examples:**
```bash
git commit -m "feat: add Apache log format detection"
git commit -m "fix: handle missing status codes in parser"
git commit -m "docs: update README with examples"
git commit -m "test: add edge case tests for empty files"
git commit -m "style: format code with black"
```

### Step 6: Test Locally Before Pushing

**Complete pre-commit checklist:**

```bash
# Run tests
poetry run pytest tests/ -v --cov=log_lens

# Verify coverage >= 90%

# Run all hooks
poetry run pre-commit run --all-files

# Manual test
log-lens sample_access.log
```

**One-liner:**
```bash
poetry run pytest tests/ -v --cov=log_lens && poetry run pre-commit run --all-files
```

Both must succeed before pushing!

### Step 7: Push & Create Pull Request

```bash
# Push your branch
git push origin feat/your-feature-name

# Go to GitHub and create a PR
# Link related issues: "Fixes #123"
```

**PR template:**
```markdown
## Description
Briefly describe what this PR does.

## Type of Change
- [ ] Bug fix (non-breaking)
- [ ] New feature (non-breaking)
- [ ] Breaking change
- [ ] Documentation

## Related Issues
Fixes #123

## Testing
Describe how you tested this.

## Checklist
- [ ] Tests pass locally
- [ ] Coverage >= 90%
- [ ] Code formatted (pre-commit)
- [ ] Commit messages follow format
- [ ] Updated CHANGELOG.md
```

---

## 🛠 Development Tools

### Running Tests

```bash
# Run all tests
poetry run pytest tests/ -v

# Run with coverage report
poetry run pytest tests/ -v --cov=log_lens --cov-report=html

# View coverage in browser
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux

# Run specific test
poetry run pytest tests/test_cli.py::TestCliIntegration -v

# Run tests matching pattern
poetry run pytest tests/ -k "test_cli_" -v
```

### Code Quality

```bash
# Lint and format with Ruff
poetry run ruff check .
poetry run ruff format .

# Type checking
poetry run mypy src/log_lens/

# Run ALL checks
poetry run pre-commit run --all-files
```

### Manual Testing

```bash
# Test on sample log
log-lens tests/fixtures/apache_access.log

# Test JSON export
log-lens tests/fixtures/apache_access.log -e test_report.json
```

---

## 📋 Pre-Commit Checklist

**Before every commit, verify:**

- [ ] Tests pass: `poetry run pytest tests/ -v --cov=log_lens`
  - Coverage must be >= 90%
  - All 11 tests must pass
- [ ] Code formatted: `poetry run pre-commit run --all-files`
  - No files modified by formatters
  - All hooks show "Passed"
- [ ] Commit message follows format (feat/fix/docs/style/test)
- [ ] Updated CHANGELOG.md (if user-facing change)
- [ ] Manual test on sample log works

**See [PRE_COMMIT_CHECKLIST.md](PRE_COMMIT_CHECKLIST.md) for detailed troubleshooting.**

---

## 🤝 Contribution Guidelines

### Code Style
- **Follow Black formatting** (auto-enforced by pre-commit)
- **Follow PEP 8** via Ruff linting
- **Write docstrings** for all functions
- **Use type hints** where possible
- **Keep functions small** (~20 lines max)

### Testing Requirements
- New features must have tests
- Tests must cover normal AND edge cases
- Coverage must stay >= 90%
- All existing tests must still pass

### PR Requirements
- Link related issues ("Fixes #123")
- Describe what changed and why
- Include test results
- Keep changes focused (one feature per PR)

### Documentation
- Update README.md if user-facing
- Update CHANGELOG.md with user-facing changes
- Add docstrings to new functions
- Use clear, concise language

---

## 📄 Commit Message Examples

### Good Examples ✅

```
feat: add Apache log format detection

Implements auto-detection of Apache access log format
by checking for common fields and patterns.

feat: add --top-ips flag

Allows users to limit the number of top IPs displayed.

fixes #45

fix: handle missing status codes gracefully

Previously crashed on logs without status codes.
Now treats missing codes as None and skips them.

docs: update README with JSON schema

Add examples of JSON export format and structure.

test: add edge case tests for empty files

Add tests for:
- Empty log files
- Malformed entries
- Very large values

style: format code with black and isort
```

### Bad Examples ❌

```
update  # Too vague
fixed stuff  # Unclear what was fixed
work in progress  # Don't commit WIP
Merge branch 'main'  # Avoid merge commits
```

---

## 🏗 Project Structure

```
log-lens/
├── log_lens/
│   ├── __init__.py      # Package metadata (version, etc.)
│   ├── cli.py           # CLI logic (argparse, output)
│   └── parser.py        # Log parsing (format detection, extraction)
├── tests/
│   ├── test_cli.py      # CLI tests (integration tests)
│   ├── test_parser.py   # Parser tests (unit tests)
│   └── fixtures/        # Sample log files for testing
├── docs/
│   ├── api.md           # API documentation
│   └── roadmap.md       # Future plans
├── .github/
│   └── workflows/
│       └── test.yml        # CI/CD pipeline
├── .pre-commit-config.yaml  # Auto-formatting hooks
├── pyproject.toml           # Project metadata & dependencies
├── poetry.lock              # Locked dependencies
├── README.md                # Project overview
├── CONTRIBUTING.md          # This file
├── PRE_COMMIT_CHECKLIST.md  # Testing checklist
└── CHANGELOG.md             # Version history
```

---

## 🐛 Common Issues & Solutions

### "Tests are failing"

```bash
# Run with verbose output
poetry run pytest tests/ -v

# Check coverage
poetry run pytest tests/ --cov=log_lens --cov-report=html

# Run specific test for debugging
poetry run pytest tests/test_cli.py::TestCliIntegration::test_cli_basic_help -v
```

### "Pre-commit hooks keep failing"

```bash
# Run hooks with verbose output
poetry run pre-commit run --all-files --verbose

# Fix formatting issues
poetry run black log_lens/ tests/
poetry run isort log_lens/ tests/
poetry run ruff check --fix log_lens/ tests/

# Try again
poetry run pre-commit run --all-files
```

### "Black/isort keeps reformatting my code"

This is expected! Just commit the changes:
```bash
git add .
git commit -m "style: format code"
poetry run pre-commit run --all-files  # Verify it passes
```

### "I committed something before running checks"

```bash
# You can amend the last commit
git add .  # Stage new changes
git commit --amend  # Update last commit
poetry run pre-commit run --all-files  # Verify
```

---

## 📚 Useful Resources

- [Black documentation](https://black.readthedocs.io/)
- [isort documentation](https://pycqa.github.io/isort/)
- [Ruff documentation](https://docs.astral.sh/ruff/)
- [pytest documentation](https://pytest.org/)
- [Poetry documentation](https://python-poetry.org/docs/)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

## 🙋 Need Help?

- **Questions?** [Open a discussion](https://github.com/KnowOneActual/log-lens/discussions)
- **Found a bug?** [Open an issue](https://github.com/KnowOneActual/log-lens/issues)
- **Have an idea?** [Submit a feature request](https://github.com/KnowOneActual/log-lens/issues/new?labels=enhancement)

---

## 🎆 Your First Contribution

Looking for a good first issue? Check for:
- Issues labeled `good first issue`
- Issues labeled `help wanted`
- Typos in documentation
- Missing edge case tests

---

**Thank you for contributing! 🙏 Your work makes log-lens better for everyone.** 

**Happy coding!** 🚀✨
