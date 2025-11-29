# Contributing to Log Lens 🔍

Thank you for considering contributing! Contributions welcome! 🎉

## 🎯 Development Workflow

1. **Fork & clone**
```bash
git clone https://github.com/YOUR_USERNAME/log-lens.git
cd log-lens
pip install -e '.[dev]'
```

2. **Install pre-commit hooks** (auto-formatting)
```bash
pre-commit install
```

3. **Make your changes + tests**
```bash
# Your changes here...
pre-commit run --all-files  # Auto-format
pytest tests/               # Tests pass
log-lens sample_access.log  # CLI works
```

4. **Commit & push**
```bash
git add .
git commit -m "feat: add nginx parser"
git push origin your-branch
```

5. **Open Pull Request** → Auto-tested by CI!

## 🤝 Contribution Guidelines

- **Small PRs** (<200 lines) preferred
- **Tests required** for new features
- **Follow Black formatting** (pre-commit auto-fixes)
- **Update CHANGELOG.md** for user-facing changes
- **Link issues** with `fixes #123`

## 🧪 Testing

```bash
pytest tests/ --cov=log_lens  # Run + coverage
log-lens sample_access.log    # Manual test
```

## 📋 Commit Message Format

```bash
feat: add nginx log parser
fix: handle missing status codes
docs: update apache examples
style: fix black formatting
```

## 🤔 Questions?

- Open an [issue](https://github.com/KnowOneActual/log-lens/issues/new)
- Join [Discord](link-when-created)

**Happy contributing!** 🙌