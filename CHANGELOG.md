# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-11-11

### Added
- **Pollinations.ai provider** - FREE unlimited image generation, no API key required!
- **HuggingFace Inference API provider** - Free tier with FLUX and Stable Diffusion models
- **NPM package distribution** - Easy installation via npm/npx
- Support for custom image dimensions in any WIDTHxHEIGHT format
- Model selection for Pollinations (flux, turbo) and HuggingFace (any model ID)
- Seed parameter for reproducible image generation (Pollinations)
- Multi-platform configuration guides:
  - Claude Desktop
  - Claude Code (CLI)
  - Sourcegraph Cody (VS Code)
  - Gemini CLI
- Comprehensive README with badges, troubleshooting, and examples
- NPM executable wrapper for cross-platform compatibility

### Changed
- Default provider changed to Pollinations.ai (free, no API key needed)
- Improved error messages for HuggingFace cold starts
- Updated README with comprehensive installation instructions for all platforms
- Enhanced documentation with provider comparison table
- Added professional badges and shields to README

### Fixed
- Improved error handling for provider-specific issues
- Better guidance for cold start delays with HuggingFace

## [0.1.0] - 2025-11-11

### Added
- Initial release of Image Generation MCP Server
- OpenAI GPT-Image-1 integration for image generation
- Support for multiple image sizes: 1024x1024, 1024x1536, 1536x1024
- Image resizing with aspect ratio maintenance
- Image format conversion (PNG, JPEG, WEBP, GIF)
- Image metadata extraction tool
- Comprehensive documentation and README
- Test suite with pytest
- Code formatting with Black
- Linting with Ruff
- Type checking with MyPy
