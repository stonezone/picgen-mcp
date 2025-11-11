# Suggested Commands

## Development Setup
```bash
# Install dependencies
pip install -e .

# Install with dev dependencies
pip install -e ".[dev]"

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

## Code Quality
```bash
# Format code
black src/ tests/

# Lint code
ruff check src/ tests/

# Type check
mypy src/

# Run all checks
black src/ tests/ && ruff check src/ tests/ && mypy src/
```

## Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/imagegen_mcp --cov-report=html

# Run specific test file
pytest tests/test_server.py

# Run with verbose output
pytest -v
```

## Running the Server
```bash
# Run directly (for testing)
python src/imagegen_mcp/server.py

# The server is designed to run via MCP client (Claude Desktop, Claude Code)
# See README.md for configuration instructions
```

## Git Operations
```bash
# Initialize repository (if needed)
git init
git remote add origin https://github.com/stonezone/imagegenMCP.git

# Standard workflow
git add .
git commit -m "descriptive message"
git push origin main

# Create feature branch
git checkout -b feature/branch-name
```

## macOS-Specific Commands
```bash
# Find files
find . -name "*.py"

# Search in files (grep)
grep -r "pattern" src/

# List directory tree
tree -L 3

# View file with line numbers
cat -n file.py

# Open in default editor
open file.py
```

## Project Structure Commands
```bash
# View project structure
tree -L 3 -I '__pycache__|*.egg-info|.pytest_cache'

# Count lines of code
find src/ -name "*.py" | xargs wc -l

# List Python files
find . -name "*.py" -type f
```

## Troubleshooting
```bash
# Check Python version
python --version

# Check installed packages
pip list | grep -E "mcp|httpx|pillow"

# Verify environment variables
echo $OPENAI_API_KEY

# Test OpenAI API connection
python -c "import httpx; import os; print(httpx.get('https://api.openai.com/v1/models', headers={'Authorization': f'Bearer {os.getenv(\"OPENAI_API_KEY\")}'}).status_code)"
```
