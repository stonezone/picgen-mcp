# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-11-11

### Added
- **Pollinations.ai provider** - FREE unlimited image generation, no API key required!
- **HuggingFace Inference API provider** - Free tier with FLUX and Stable Diffusion models
- Support for custom image dimensions in any WIDTHxHEIGHT format
- Model selection for Pollinations (flux, turbo) and HuggingFace (any model ID)
- Seed parameter for reproducible image generation (Pollinations)
- Enhanced documentation with multi-provider examples

### Changed
- Default provider changed to Pollinations.ai (free, no API key needed)
- Improved error messages for HuggingFace cold starts
- Updated README with comprehensive provider comparison

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
