# Image Generation MCP Server

A Model Context Protocol (MCP) server that provides AI image generation and manipulation capabilities. Enables Claude and other MCP clients to generate images using OpenAI's GPT-Image-1 model and perform various image processing operations.

## Features

### Image Generation
- **OpenAI GPT-Image-1**: Generate high-quality images from text prompts
- Multiple aspect ratios: square (1024x1024), portrait (1024x1536), landscape (1536x1024)
- Automatic image saving and management

### Image Manipulation
- **Resize**: Scale images while maintaining or ignoring aspect ratio
- **Format Conversion**: Convert between PNG, JPEG, WEBP, and GIF
- **Metadata**: Extract detailed image information (dimensions, format, size)

## Installation

### Prerequisites
- Python 3.10 or higher
- OpenAI API key

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

3. **Set up environment variables**

Create a `.env` file or export variables:
```bash
export OPENAI_API_KEY="your-api-key-here"
export OPENAI_ORG_ID="your-org-id"  # Optional
```

## Configuration

### Claude Desktop

Add to your Claude Desktop config file (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

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
        "OPENAI_ORG_ID": "your-org-id"
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
```
Claude, generate an image of a serene Hawaiian beach at sunset with palm trees
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
Generate images using AI models.

**Parameters:**
- `prompt` (required): Detailed description of the image
- `provider` (optional): Image generation provider (default: "openai")
- `size` (optional): Image dimensions (default: "1024x1024")
  - Options: "1024x1024", "1024x1536", "1536x1024"
- `output_filename` (optional): Custom filename for the generated image

**Returns:**
```json
{
  "image_path": "/absolute/path/to/generated_images/image.png",
  "url": "https://...",
  "size": "1024x1024",
  "prompt": "...",
  "provider": "openai"
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

- [ ] Add support for Stability AI
- [ ] Add support for HuggingFace models
- [ ] Add more image manipulation tools (crop, rotate, filters)
- [ ] Add batch image generation
- [ ] Add image upscaling capabilities
- [ ] Add image-to-image transformation
- [ ] Cache generated images with prompt hashing

## Troubleshooting

### API Key Issues
- Ensure `OPENAI_API_KEY` is set in environment variables
- Verify the key is valid and has sufficient credits
- Check that the key has access to the GPT-Image-1 model

### Image Generation Errors
- Prompts must be descriptive and follow OpenAI's content policy
- Check API rate limits if getting timeout errors
- Ensure you have sufficient API quota

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
