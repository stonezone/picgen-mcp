# Code Style and Conventions

## Formatting
- **Tool**: Black
- **Line Length**: 100 characters
- **Target Version**: Python 3.10+

## Linting
- **Tool**: Ruff
- **Selected Rules**: E, F, I, N, W, UP
- **Line Length**: 100 characters

## Type Checking
- **Tool**: MyPy
- **Configuration**:
  - `python_version = "3.10"`
  - `warn_return_any = true`
  - `warn_unused_configs = true`
  - `disallow_untyped_defs = true`

## Naming Conventions
- **Functions/Variables**: snake_case
- **Classes**: PascalCase
- **Constants**: UPPER_SNAKE_CASE
- **Private Members**: _leading_underscore

## Type Hints
- All function signatures must include type hints
- Use `Optional[T]` for optional parameters
- Use `dict[K, V]` (not `Dict[K, V]`) for Python 3.10+
- Use `list[T]` (not `List[T]`) for Python 3.10+

## Docstrings
- **Style**: Google-style docstrings
- Required for all public functions and classes
- Include Args, Returns, and Raises sections as appropriate

## Async/Await
- Use async functions for I/O operations
- Prefer `httpx.AsyncClient` over synchronous HTTP
- Use `asyncio.run()` for entry points

## Error Handling
- Raise specific exceptions with descriptive messages
- Use try/except in tool handlers to return error messages
- Validate inputs before processing
