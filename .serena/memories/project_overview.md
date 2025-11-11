# Project Overview

## Purpose
Image Generation MCP Server - A Model Context Protocol server that enables Claude and other MCP clients to generate and manipulate images using AI models.

## Key Features
- **Image Generation**: OpenAI GPT-Image-1 model integration
- **Image Manipulation**: Resize, format conversion, metadata extraction
- **Multiple Providers**: Designed to support multiple providers (OpenAI first, Stability AI and HuggingFace planned)
- **Async Architecture**: Built with asyncio for efficient I/O operations

## Tech Stack
- **Language**: Python 3.10+
- **Framework**: MCP (Model Context Protocol)
- **Dependencies**:
  - `mcp>=1.0.0` - MCP SDK
  - `httpx>=0.27.0` - Async HTTP client
  - `pillow>=10.0.0` - Image processing
  - `python-dotenv>=1.0.0` - Environment variable management

## Architecture
- **Entry Point**: `src/imagegen_mcp/server.py`
- **Output Directory**: `generated_images/` (auto-created)
- **Configuration**: Environment variables (OPENAI_API_KEY, OPENAI_ORG_ID)

## MCP Tools Provided
1. `generate_image` - AI image generation
2. `resize_image` - Resize with aspect ratio control
3. `convert_image_format` - Format conversion (PNG, JPEG, WEBP, GIF)
4. `get_image_info` - Extract image metadata
