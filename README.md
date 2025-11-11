# 🎨 Image Generation MCP Server

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![MCP](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io/)
[![npm version](https://img.shields.io/npm/v/@stonezone/imagegen-mcp.svg)](https://www.npmjs.com/package/@stonezone/imagegen-mcp)

A powerful Model Context Protocol (MCP) server that enables AI assistants (Claude, Gemini, Cody) to generate and manipulate images using multiple providers. **Start generating images for FREE** with Pollinations.ai—no API key required!

## ✨ Features

### 🎨 Multiple AI Image Providers

| Provider | Cost | API Key | Quality | Speed | Notes |
|----------|------|---------|---------|-------|-------|
| **Pollinations.ai** | ✅ FREE | ❌ None | ⭐⭐⭐⭐ | ⚡ Fast | **Recommended** - Unlimited usage! |
| **HuggingFace** | ✅ FREE Tier | ✅ Required | ⭐⭐⭐⭐⭐ | 🐢 Slow | FLUX & Stable Diffusion models |
| **OpenAI** | 💰 Paid | ✅ Required | ⭐⭐⭐⭐⭐ | ⚡ Fast | GPT-Image-1 (DALL-E) |

### 🛠️ Image Manipulation Tools
- **Resize**: Scale images with aspect ratio control
- **Format Conversion**: PNG ↔ JPEG ↔ WEBP ↔ GIF
- **Metadata Extraction**: Dimensions, format, file size
- **Custom Dimensions**: Any size (512x512, 1920x1080, etc.)

### 🔧 Supported Platforms
- ✅ Claude Desktop
- ✅ Claude Code (CLI)
- ✅ Sourcegraph Cody (VS Code)
- ✅ Gemini CLI
- ✅ Any MCP-compatible client

---

## 📦 Installation

### Option 1: NPM (Recommended)

```bash
# Install globally
npm install -g @stonezone/imagegen-mcp

# Or install locally in your project
npm install @stonezone/imagegen-mcp
```

### Option 2: Python (pip)

```bash
# Clone the repository
git clone https://github.com/stonezone/imagegenMCP.git
cd imagegenMCP

# Install with pip
pip install -e .

# Or for development
pip install -e ".[dev]"
```

### Option 3: Direct from GitHub

```bash
pip install git+https://github.com/stonezone/imagegenMCP.git
```

---

## 🔑 API Keys (Optional)

### Pollinations.ai (Default - FREE!)
**No API key needed!** This is the default provider and works immediately after installation.

### HuggingFace (Optional - FREE Tier)
1. Create a free account at [huggingface.co](https://huggingface.co)
2. Get your token: [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
3. Set environment variable:
   ```bash
   export HUGGINGFACE_API_KEY="your-token-here"
   ```

### OpenAI (Optional - Paid)
1. Get API key from [platform.openai.com](https://platform.openai.com/api-keys)
2. Set environment variable:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

---

## ⚙️ Configuration

### 🖥️ Claude Desktop

**Location:** `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows)

#### With NPM Installation:
```json
{
  "mcpServers": {
    "imagegen": {
      "command": "npx",
      "args": ["@stonezone/imagegen-mcp"]
    }
  }
}
```

#### With Python Installation:
```json
{
  "mcpServers": {
    "imagegen": {
      "command": "python",
      "args": ["/absolute/path/to/imagegenMCP/src/imagegen_mcp/server.py"]
    }
  }
}
```

#### With API Keys (Optional):
```json
{
  "mcpServers": {
    "imagegen": {
      "command": "npx",
      "args": ["@stonezone/imagegen-mcp"],
      "env": {
        "OPENAI_API_KEY": "sk-...",
        "HUGGINGFACE_API_KEY": "hf_..."
      }
    }
  }
}
```

**Restart Claude Desktop** after editing the config file.

---

### 💻 Claude Code (CLI)

**Location:** `.claudecode/config.json` in your project or `~/.config/claudecode/config.json` globally

```json
{
  "mcpServers": {
    "imagegen": {
      "command": "npx",
      "args": ["@stonezone/imagegen-mcp"]
    }
  }
}
```

Or set environment variables in your shell:
```bash
export OPENAI_API_KEY="sk-..."
export HUGGINGFACE_API_KEY="hf_..."
```

---

### 🤖 Sourcegraph Cody (VS Code)

**Location:** VS Code Settings (JSON)

Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux), type "Preferences: Open User Settings (JSON)"

```json
{
  "openctx.providers": {
    "https://openctx.org/npm/@openctx/provider-modelcontextprotocol": {
      "imagegen": {
        "command": "npx",
        "args": ["@stonezone/imagegen-mcp"],
        "env": {
          "OPENAI_API_KEY": "sk-...",
          "HUGGINGFACE_API_KEY": "hf_..."
        }
      }
    }
  }
}
```

**Note:** MCP works through Cody's agentic context gathering, not via @mentions.

---

### 🔮 Gemini CLI

**Location:** `~/.gemini/settings.json` (global) or `.gemini/settings.json` (project)

First, install Gemini CLI:
```bash
npm install -g @google/gemini-cli@latest
```

Then configure the MCP server:
```json
{
  "mcpServers": {
    "imagegen": {
      "command": "npx",
      "args": ["@stonezone/imagegen-mcp"],
      "env": {
        "OPENAI_API_KEY": "sk-...",
        "HUGGINGFACE_API_KEY": "hf_..."
      }
    }
  }
}
```

---

## 🚀 Usage Examples

### Generate an Image (FREE!)

```
Generate an image of a serene Hawaiian beach at sunset with palm trees
```
*Uses Pollinations.ai by default—completely free!*

### Specify Provider

```
Generate using huggingface: a futuristic cyberpunk cityscape
Generate using openai: a professional headshot photo
Generate using pollinations with turbo model: a cute cat
```

### Custom Sizes

```
Generate a 1920x1080 desktop wallpaper of mountains
Generate a 512x768 portrait of a sunset
Create a square 1024x1024 image of abstract art
```

### Image Manipulation

```
Resize that image to 512x512 pixels
Convert the image to JPEG format
What are the dimensions and format of this image?
Resize to width 800 maintaining aspect ratio
```

### Advanced Options

```
Generate with seed 12345: a landscape (reproducible results with Pollinations)
Generate using huggingface model stabilityai/stable-diffusion-xl-base-1.0: a portrait
```

---

## 🔧 Available Tools

### `generate_image`
Generate images using AI models.

**Parameters:**
- `prompt` (required): Description of the image to generate
- `provider` (optional): `"pollinations"` (default, FREE), `"openai"`, `"huggingface"`
- `size` (optional): Image dimensions, e.g., `"1024x1024"`, `"512x768"`, `"1920x1080"`
- `model` (optional):
  - Pollinations: `"flux"` (default) or `"turbo"`
  - HuggingFace: Model ID like `"black-forest-labs/FLUX.1-dev"`
- `seed` (optional): Random seed for reproducibility (Pollinations only)
- `output_filename` (optional): Custom filename

**Returns:**
```json
{
  "image_path": "/path/to/generated_images/image.png",
  "url": "https://...",
  "size": "1024x1024",
  "prompt": "...",
  "provider": "pollinations"
}
```

### `resize_image`
Resize an existing image.

**Parameters:**
- `image_path` (required): Path to the image
- `width` (optional): Target width in pixels
- `height` (optional): Target height in pixels
- `maintain_aspect` (optional): Keep aspect ratio (default: true)
- `output_path` (optional): Custom output path

### `convert_image_format`
Convert image to different format.

**Parameters:**
- `image_path` (required): Path to source image
- `target_format` (required): `"PNG"`, `"JPEG"`, `"WEBP"`, or `"GIF"`
- `quality` (optional): Quality for lossy formats (1-100, default: 95)
- `output_path` (optional): Custom output path

### `get_image_info`
Get image metadata.

**Parameters:**
- `image_path` (required): Path to the image

---

## 🧪 Testing

Run the test suite:
```bash
pytest
```

Test image generation directly:
```bash
python -c "
import asyncio
from pathlib import Path
from src.imagegen_mcp.server import generate_image_pollinations

async def test():
    result = await generate_image_pollinations(
        prompt='a red circle on white background',
        size='256x256'
    )
    print(f'Success! Image saved to: {result[\"image_path\"]}')

asyncio.run(test())
"
```

---

## 🐛 Troubleshooting

### Getting Started
- ✅ **Try Pollinations.ai first** - No setup needed, completely free
- If you see errors, check which provider you're using
- Make sure Python 3.10+ is installed: `python --version`

### Provider-Specific Issues

#### Pollinations.ai (Recommended)
- ✅ No API key needed
- ✅ No rate limits
- ✅ Very fast and reliable
- ❌ If it fails, check your internet connection

#### HuggingFace
- Get free token: [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
- Free tier has monthly credit limits
- **Cold starts:** First request may take 1-2 minutes (model loading)
- If you get `503 Service Unavailable`, wait a minute and try again
- Error `402 Payment Required`: You've exceeded monthly free credits

#### OpenAI
- Requires paid API key from [platform.openai.com](https://platform.openai.com/api-keys)
- Check your API quota and billing
- Prompts must follow OpenAI's content policy
- Model name: `gpt-image-1`

### Common Issues

**"Command not found" or "Module not found"**
```bash
# For NPM installation
npm install -g @stonezone/imagegen-mcp

# For Python installation
pip install -e .
```

**"Permission denied"**
```bash
# Make sure the server script is executable
chmod +x src/imagegen_mcp/server.py
```

**Images not saving**
```bash
# Check the generated_images directory exists and is writable
mkdir -p generated_images
chmod 755 generated_images
```

**Python version issues**
```bash
# Check Python version (must be 3.10+)
python --version

# Use python3 if needed
python3 --version
```

---

## 📁 Project Structure

```
imagegenMCP/
├── src/
│   └── imagegen_mcp/
│       ├── __init__.py
│       └── server.py          # Main MCP server
├── bin/
│   └── imagegen-mcp.js        # NPM executable wrapper
├── generated_images/          # Output directory (auto-created)
├── tests/                     # Test suite
├── package.json               # NPM package config
├── pyproject.toml            # Python package config
├── README.md
├── LICENSE
└── CHANGELOG.md
```

---

## 🔄 Updating

### NPM Installation
```bash
npm update -g @stonezone/imagegen-mcp
```

### Python Installation
```bash
cd imagegenMCP
git pull
pip install -e .
```

---

## 🛠️ Development

### Setup Development Environment
```bash
git clone https://github.com/stonezone/imagegenMCP.git
cd imagegenMCP
pip install -e ".[dev]"
```

### Code Quality Tools
```bash
# Format code
black src/

# Lint code
ruff check src/

# Type checking
mypy src/

# Run tests
pytest
```

### Contributing
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Run tests and linting
5. Commit: `git commit -m 'Add amazing feature'`
6. Push: `git push origin feature/amazing-feature`
7. Open a Pull Request

---

## 🗺️ Roadmap

- [x] Pollinations.ai provider (FREE!)
- [x] HuggingFace Inference API
- [x] OpenAI GPT-Image-1
- [x] NPM package distribution
- [x] Multiple platform support
- [ ] Stability AI integration
- [ ] Replicate.com provider
- [ ] Image-to-image transformation
- [ ] Batch image generation
- [ ] Image upscaling
- [ ] Advanced manipulation (crop, rotate, filters)
- [ ] Prompt template library
- [ ] Image caching system

---

## 📊 Comparison: Why This MCP Server?

| Feature | This Server | Alternatives |
|---------|-------------|--------------|
| **Free Provider** | ✅ Pollinations.ai (unlimited) | ❌ Usually paid only |
| **Multiple Providers** | ✅ 3 providers | ⚠️ Usually 1 |
| **No API Key to Start** | ✅ Works immediately | ❌ API keys required |
| **Custom Sizes** | ✅ Any dimensions | ⚠️ Limited options |
| **Image Manipulation** | ✅ Resize, convert, info | ❌ Generation only |
| **NPM Distribution** | ✅ Easy install | ⚠️ Manual setup |
| **Multi-Platform** | ✅ 4+ platforms | ⚠️ Limited |

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Zack Jordan**

- GitHub: [@stonezone](https://github.com/stonezone)
- Repository: [imagegenMCP](https://github.com/stonezone/imagegenMCP)

---

## 🙏 Acknowledgments

- [Anthropic](https://www.anthropic.com/) for the Model Context Protocol
- [Pollinations.ai](https://pollinations.ai/) for free image generation
- [HuggingFace](https://huggingface.co/) for their Inference API
- [OpenAI](https://openai.com/) for GPT-Image-1

---

## 📚 Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [OpenAI Images API](https://platform.openai.com/docs/guides/images)
- [HuggingFace Inference API](https://huggingface.co/docs/api-inference/)
- [Pollinations.ai Docs](https://pollinations.ai/)

---

## ⭐ Star History

If you find this project useful, please consider giving it a star on GitHub! It helps others discover the project.

---

## 🤝 Support

- 📫 Issues: [GitHub Issues](https://github.com/stonezone/imagegenMCP/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/stonezone/imagegenMCP/discussions)
- 📖 Documentation: [Wiki](https://github.com/stonezone/imagegenMCP/wiki)

---

**Made with ❤️ for the MCP community**
