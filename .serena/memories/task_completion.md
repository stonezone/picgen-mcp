# Task Completion Checklist

When completing a task on this project, follow these steps:

## 1. Code Quality Checks
- [ ] Format code with Black: `black src/ tests/`
- [ ] Lint with Ruff: `ruff check src/ tests/`
- [ ] Type check with MyPy: `mypy src/`
- [ ] All checks pass without errors

## 2. Testing
- [ ] Run test suite: `pytest`
- [ ] All tests pass
- [ ] Add new tests for new functionality
- [ ] Test coverage remains high

## 3. Documentation
- [ ] Update README.md if public API changed
- [ ] Update CHANGELOG.md with changes
- [ ] Add/update docstrings for new code
- [ ] Update type hints

## 4. Git Operations
- [ ] Stage changes: `git add .`
- [ ] Commit with descriptive message: `git commit -m "feat: description"`
- [ ] Push to repository: `git push origin main`

## 5. Verification
- [ ] Test the MCP server locally if possible
- [ ] Verify environment variables are documented
- [ ] Check that all dependencies are in pyproject.toml
- [ ] Ensure .gitignore is up to date

## Commit Message Format
Follow conventional commits:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting)
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

## Pre-Push Checklist
```bash
# Quick validation before pushing
black src/ tests/ && \
ruff check src/ tests/ && \
mypy src/ && \
pytest && \
echo "✅ All checks passed!"
```
