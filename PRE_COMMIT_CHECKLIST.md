# Pre-Commit Testing Checklist ✅

**Complete this checklist BEFORE committing to avoid CI failures!**

## 🧪 Step 1: Run All Tests

```bash
poetry run pytest tests/ -v --cov=log_lens
```

✅ **Check:**
- All tests pass (green checkmarks)
- Coverage >= 90% (currently at 95%)
- No test errors or failures

**Example passing output:**
```
tests/test_cli.py::TestCliIntegration::test_cli_basic_help PASSED
tests/test_parser.py::TestLogParser::test_basic_parsing PASSED
=========== 11 passed in 0.24s ===========
```

---

## 🎨 Step 2: Run Pre-Commit Hooks

```bash
poetry run pre-commit run --all-files
```

This runs ALL formatters & linters:
- **Black** - Code formatting
- **isort** - Import sorting
- **Ruff** - Linting & formatting
- **ruff-format** - Additional formatting

✅ **Check:**
- All hooks show **Passed** ✓
- NO files modified by hooks

**What if hooks modify files?**

If any hook modifies files:
1. Review the changes
2. Stage them: `git add .`
3. Commit the formatting fixes: `git commit -m "style: format code"`
4. Run pre-commit again: `poetry run pre-commit run --all-files`
5. Continue once all hooks pass

---

## 🚀 Step 3: Manual Testing (Optional but Recommended)

Test your changes work in practice:

```bash
# Test on sample log
log-lens sample_access.log

# Test JSON export
log-lens sample_access.log -e test_report.json

# Test different flags
log-lens sample_access.log --top-ips 5
```

---

## 📝 Step 4: Verify Code Quality

```bash
# Type checking (if enabled)
poetry run mypy log_lens/

# Security scanning (optional)
poetry run bandit -r log_lens/
```

---

## ✨ Step 5: Check Your Commit Message

Use the format:

```
feat: add new feature
fix: resolve bug
docs: update documentation
style: format code
test: add test coverage
chore: maintenance
```

**Good example:**
```bash
git commit -m "feat: add status code analysis for Apache logs"
```

**Bad example:**
```bash
git commit -m "update"  # ❌ Too vague
```

---

## 🎯 Complete Checklist Before Push

- [ ] `poetry run pytest tests/ -v --cov=log_lens` **PASSED**
- [ ] `poetry run pre-commit run --all-files` **PASSED** (no modified files)
- [ ] Manually tested on sample log (optional)
- [ ] Commit message follows format
- [ ] Updated CHANGELOG.md if user-facing change
- [ ] Ready to `git push origin your-branch`

---

## ⚡ Quick Reference: One-Liner Full Check

Run this before pushing:

```bash
poetry run pytest tests/ -v --cov=log_lens && poetry run pre-commit run --all-files
```

If both pass, you're good to commit & push! 🚀

---

## 🚨 Common Issues & Fixes

### Black reformatted my code!
```bash
# Black will reformat, that's expected
# Just add and commit the changes
git add .
git commit -m "style: format code with black"
poetry run pre-commit run --all-files  # Should pass now
```

### isort changed import order!
```bash
# Same as above - it's expected
git add .
git commit -m "style: sort imports with isort"
```

### Tests failing?
```bash
# Check the error message
poetry run pytest tests/ -v

# Run specific test for details
poetry run pytest tests/test_cli.py::TestCliIntegration -v

# Check coverage
poetry run pytest tests/ --cov=log_lens --cov-report=html
# Open htmlcov/index.html
```

### Pre-commit hooks won't pass?
```bash
# See what's failing
poetry run pre-commit run --all-files --verbose

# Fix manually or auto-fix
poetry run black log_lens/
poetry run isort log_lens/
poetry run ruff check --fix log_lens/
```

---

**Made with ❤️ to keep the repo clean and CI passing!**
