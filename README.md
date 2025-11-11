# Image Generation MCP Server

A Model Context Protocol (MCP) server that provides AI image generation and manipulation capabilities. Enables Claude and other MCP clients to generate images using multiple AI providers including **Pollinations.ai (FREE!)**, OpenAI's GPT-Image-1, and HuggingFace models. Also includes powerful image processing operations.

## Features

### Image Generation
- **Multiple AI Providers**:
  - **Pollinations.ai** (FREE, no API key required!) - Unlimited image generation
  - **OpenAI GPT-Image-1** - High-quality images (requires API key)
  - **HuggingFace Inference API** - Free tier available with FLUX and Stable Diffusion models
- Flexible image sizes: any dimensions in WIDTHxHEIGHT format (e.g., 1024x1024, 512x768, etc.)
- Automatic image saving and management

### Image Manipulation
- **Resize**: Scale images while maintaining or ignoring aspect ratio
- **Format Conversion**: Convert between PNG, JPEG, WEBP, and GIF
- **Metadata**: Extract detailed image information (dimensions, format, size)

## Installation

### Prerequisites
- Python 3.10 or higher
- API keys (optional, depending on provider):
  - **No API key needed** for Pollinations.ai (recommended for getting started!)
  - OpenAI API key for OpenAI provider
  - HuggingFace API token for HuggingFace provider (free tier available)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/stonezone/imagegenMCP.git
cd imagegenMCP
```

2. **Install dependencies**
```bash
pip install -e .
```

Or for development:
```bash
pip install -e ".[dev]"
```

3. **Set up environment variables (if needed)**

For **Pollinations.ai**: No API key required! You can start using it immediately.

For **OpenAI** (optional):
```bash
export OPENAI_API_KEY="your-api-key-here"
export OPENAI_ORG_ID="your-org-id"  # Optional
```

For **HuggingFace** (optional, free tier available):
```bash
export HUGGINGFACE_API_KEY="your-hf-token-here"
# Get free token at: https://huggingface.co/settings/tokens
```

## Configuration

### Claude Desktop

Add to your Claude Desktop config file (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

**Option 1: Use Pollinations.ai (FREE, no API key needed!)**
```json
{
  "mcpServers": {
    "imagegen": {
      "command": "python",
      "args": [
        "/absolute/path/to/imagegenMCP/src/imagegen_mcp/server.py"
      ]
    }
  }
}
```

**Option 2: With OpenAI and/or HuggingFace API keys**
```json
{
  "mcpServers": {
    "imagegen": {
      "command": "python",
      "args": [
        "/absolute/path/to/imagegenMCP/src/imagegen_mcp/server.py"
      ],
      "env": {
        "OPENAI_API_KEY": "your-api-key-here",
        "HUGGINGFACE_API_KEY": "your-hf-token-here"
      }
    }
  }
}
```

### Claude Code

Add to `.claudecode/config.json` in your project:

```json
{
  "mcpServers": {
    "imagegen": {
      "command": "python",
      "args": [
        "/absolute/path/to/imagegenMCP/src/imagegen_mcp/server.py"
      ]
    }
  }
}
```

Make sure environment variables are set in your shell.

## Usage

Once configured, Claude can use these tools:

### Generate an Image

**Using Pollinations.ai (FREE, default)**:
```
Claude, generate an image of a serene Hawaiian beach at sunset with palm trees
```

**Using a specific provider**:
```
Claude, generate an image using the pollinations provider: a futuristic city skyline
Claude, generate an image using openai: a mountain landscape
Claude, generate an image using huggingface: a portrait of a cat
```

**Custom sizes**:
```
Claude, generate a 512x768 portrait of a sunset beach scene
Claude, generate a 1920x1080 landscape wallpaper of mountains
```

### Resize an Image
```
Claude, resize the generated image to 512x512 pixels
```

### Convert Format
```
Claude, convert that image to JPEG format
```

### Get Image Information
```
Claude, what are the dimensions and format of this image?
```

## Available Tools

### `generate_image`
Generate images using AI models from multiple providers.

**Parameters:**
- `prompt` (required): Detailed description of the image
- `provider` (optional): Image generation provider (default: "pollinations")
  - Options: "pollinations" (FREE), "openai", "huggingface"
- `size` (optional): Image dimensions in WIDTHxHEIGHT format (default: "1024x1024")
  - Examples: "512x512", "1024x768", "1920x1080", "1024x1536"
- `output_filename` (optional): Custom filename for the generated image
- `model` (optional): AI model to use
  - Pollinations: "flux" (default) or "turbo"
  - HuggingFace: model ID (default: "black-forest-labs/FLUX.1-dev")
- `seed` (optional): Random seed for reproducibility (Pollinations only)

**Returns:**
```json
{
  "image_path": "/absolute/path/to/generated_images/image.png",
  "url": "https://...",
  "size": "1024x1024",
  "prompt": "...",
  "provider": "pollinations",
  "model": "flux"
}
```

### `resize_image`
Resize an existing image.

**Parameters:**
- `image_path` (required): Path to the image to resize
- `width` (optional): Target width in pixels
- `height` (optional): Target height in pixels
- `maintain_aspect` (optional): Keep aspect ratio (default: true)
- `output_path` (optional): Custom output path

**Returns:**
```json
{
  "image_path": "/path/to/resized_image.png",
  "original_size": [1024, 1024],
  "new_size": [512, 512]
}
```

### `convert_image_format`
Convert image to different format.

**Parameters:**
- `image_path` (required): Path to the source image
- `target_format` (required): Target format (PNG, JPEG, WEBP, GIF)
- `output_path` (optional): Custom output path
- `quality` (optional): Quality for lossy formats (1-100, default: 95)

**Returns:**
```json
{
  "image_path": "/path/to/converted_image.jpg",
  "format": "JPEG",
  "original_format": "PNG"
}
```

### `get_image_info`
Get image metadata and information.

**Parameters:**
- `image_path` (required): Path to the image file

**Returns:**
```json
{
  "path": "/absolute/path/to/image.png",
  "size": [1024, 1024],
  "width": 1024,
  "height": 1024,
  "format": "PNG",
  "mode": "RGB",
  "file_size_bytes": 1048576
}
```

## Project Structure

```
imagegenMCP/
├── src/
│   └── imagegen_mcp/
│       ├── __init__.py
│       └── server.py          # Main MCP server implementation
├── generated_images/          # Generated images directory (auto-created)
├── pyproject.toml            # Project configuration
├── README.md                 # This file
└── .gitignore
```

## Development

### Code Style
- **Formatter**: Black (line length: 100)
- **Linter**: Ruff
- **Type Checker**: MyPy

### Run formatters and linters
```bash
# Format code
black src/

# Lint code
ruff check src/

# Type check
mypy src/
```

### Testing
```bash
pytest
```

## Future Enhancements

- [x] Add support for Pollinations.ai (FREE!)
- [x] Add support for HuggingFace models
- [ ] Add support for Stability AI
- [ ] Add more image manipulation tools (crop, rotate, filters)
- [ ] Add batch image generation
- [ ] Add image upscaling capabilities
- [ ] Add image-to-image transformation
- [ ] Cache generated images with prompt hashing
- [ ] Add support for Replicate models
- [ ] Add image editing capabilities (inpainting, outpainting)

## Troubleshooting

### Getting Started
- **Try Pollinations.ai first!** No API key needed, completely free
- If you encounter any issues, try using a different provider

### Provider-Specific Issues

**Pollinations.ai:**
- No authentication required - if it fails, it's likely a network issue
- Very fast and reliable
- No rate limits

**OpenAI:**
- Ensure `OPENAI_API_KEY` is set in environment variables
- Verify the key is valid and has sufficient credits
- Check that the key has access to the GPT-Image-1 model
- Prompts must follow OpenAI's content policy

**HuggingFace:**
- Get free API token from: https://huggingface.co/settings/tokens
- Set `HUGGINGFACE_API_KEY` in environment variables
- Free tier has monthly credit limits
- Models may be slow on first request (cold start) - wait 1-2 minutes
- If you get 503 errors, the model is loading - try again after a minute

### File Permission Errors
- Verify the `generated_images/` directory is writable
- Check that output paths are accessible

## License

MIT

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## Author

Zack Jordan

## Links

- [GitHub Repository](https://github.com/stonezone/imagegenMCP)
- [OpenAI API Documentation](https://platform.openai.com/docs/guides/images)
- [MCP Protocol](https://modelcontextprotocol.io/)
