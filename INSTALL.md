# 📦 Complete Installation Guide

## 🚀 Quick Start (3 Steps)

1. **Install the package**
2. **Configure your AI assistant**
3. **Start generating images!**

---

## 📥 Installation Methods

### Method 1: NPM (Recommended - Easiest) ⭐

```bash
# Install globally
npm install -g @stonezone/imagegen-mcp

# Or install in your project
npm install @stonezone/imagegen-mcp
```

**Advantages:**
- ✅ One command installation
- ✅ Automatic updates via `npm update`
- ✅ Works across all platforms
- ✅ No Python environment setup needed

### Method 2: Python pip

```bash
# Clone the repository
git clone https://github.com/stonezone/imagegenMCP.git
cd imagegenMCP

# Install with pip
pip install -e .
```

### Method 3: Direct from GitHub

```bash
pip install git+https://github.com/stonezone/imagegenMCP.git
```

---

## 🔧 Platform-Specific Setup

### 🖥️ Claude Desktop

Claude Desktop is Anthropic's native desktop application for chatting with Claude.

#### Configuration File Location:

**macOS:**
```bash
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

**Linux:**
```
~/.config/Claude/claude_desktop_config.json
```

#### Setup Steps:

1. **Locate your config file** using the path above

2. **Edit the config file** (create it if it doesn't exist):

**Option A: NPM Installation (Recommended)**
```json
{
  "mcpServers": {
    "imagegen": {
      "command": "npx",
      "args": ["-y", "@stonezone/imagegen-mcp"]
    }
  }
}
```

**Option B: Python Installation**
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
*Replace `/absolute/path/to/imagegenMCP` with your actual path!*

**Option C: With API Keys** (for OpenAI/HuggingFace)
```json
{
  "mcpServers": {
    "imagegen": {
      "command": "npx",
      "args": ["-y", "@stonezone/imagegen-mcp"],
      "env": {
        "OPENAI_API_KEY": "sk-...",
        "HUGGINGFACE_API_KEY": "hf_..."
      }
    }
  }
}
```

3. **Restart Claude Desktop** completely (Quit and reopen)

4. **Test it!** In Claude Desktop, type:
   ```
   Generate a red circle on white background
   ```

---

### 💻 Claude Code (CLI)

Claude Code is Anthropic's command-line tool for agentic coding.

#### Setup Steps:

1. **Check if Claude Code is installed:**
   ```bash
   claude --version
   ```
   If not installed, follow [Claude Code documentation](https://docs.claude.com/en/docs/claude-code)

2. **Create config file:**

**Global Configuration** (works everywhere):
```bash
mkdir -p ~/.config/claudecode
cat > ~/.config/claudecode/config.json << 'EOF'
{
  "mcpServers": {
    "imagegen": {
      "command": "npx",
      "args": ["-y", "@stonezone/imagegen-mcp"]
    }
  }
}
EOF
```

**Project-Specific** (only in current project):
```bash
mkdir -p .claudecode
cat > .claudecode/config.json << 'EOF'
{
  "mcpServers": {
    "imagegen": {
      "command": "npx",
      "args": ["-y", "@stonezone/imagegen-mcp"]
    }
  }
}
EOF
```

3. **Set API keys** (optional, for OpenAI/HuggingFace):
   ```bash
   export OPENAI_API_KEY="sk-..."
   export HUGGINGFACE_API_KEY="hf_..."
   ```

4. **Test it:**
   ```bash
   claude "Generate a sunset beach scene"
   ```

---

### 🎯 Cursor IDE

Cursor is an AI-powered code editor based on VS Code.

#### Setup Steps:

1. **Open Cursor Settings**
   - Press `Cmd+,` (Mac) or `Ctrl+,` (Windows/Linux)
   - Or go to: File → Preferences → Settings

2. **Open Settings JSON**
   - Click the `{}` icon in the top right (Open Settings JSON)

3. **Add MCP server configuration:**

```json
{
  "mcpServers": {
    "imagegen": {
      "command": "npx",
      "args": ["-y", "@stonezone/imagegen-mcp"],
      "env": {
        "OPENAI_API_KEY": "sk-...",
        "HUGGINGFACE_API_KEY": "hf_..."
      }
    }
  }
}
```

4. **Restart Cursor**

5. **Test it** by asking Cursor's AI:
   ```
   Generate an image of a robot coding
   ```

---

### 🦀 Cody (Sourcegraph)

Cody is Sourcegraph's AI coding assistant for VS Code.

#### Setup Steps:

1. **Install Cody Extension**
   - Open VS Code
   - Go to Extensions (Cmd+Shift+X / Ctrl+Shift+X)
   - Search "Sourcegraph Cody"
   - Click Install

2. **Configure MCP Server**
   - Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)
   - Type: "Preferences: Open User Settings (JSON)"

3. **Add configuration:**

```json
{
  "openctx.providers": {
    "https://openctx.org/npm/@openctx/provider-modelcontextprotocol": {
      "imagegen": {
        "command": "npx",
        "args": ["-y", "@stonezone/imagegen-mcp"],
        "env": {
          "OPENAI_API_KEY": "sk-...",
          "HUGGINGFACE_API_KEY": "hf_..."
        }
      }
    }
  }
}
```

4. **Reload VS Code**
   - Press `Cmd+Shift+P` / `Ctrl+Shift+P`
   - Type: "Developer: Reload Window"

5. **Test it** through Cody's chat

**Note:** Cody uses MCP through OpenCtx for agentic context gathering, not via @mentions.

---

### 🔮 Gemini CLI (Google)

Google's Gemini command-line interface.

#### Setup Steps:

1. **Install Gemini CLI:**
   ```bash
   npm install -g @google/gemini-cli@latest
   ```

2. **Create config file:**

**Global** (~/.gemini/settings.json):
```bash
mkdir -p ~/.gemini
cat > ~/.gemini/settings.json << 'EOF'
{
  "mcpServers": {
    "imagegen": {
      "command": "npx",
      "args": ["-y", "@stonezone/imagegen-mcp"],
      "env": {
        "OPENAI_API_KEY": "sk-...",
        "HUGGINGFACE_API_KEY": "hf_..."
      }
    }
  }
}
EOF
```

**Project-specific** (.gemini/settings.json):
```bash
mkdir -p .gemini
cat > .gemini/settings.json << 'EOF'
{
  "mcpServers": {
    "imagegen": {
      "command": "npx",
      "args": ["-y", "@stonezone/imagegen-mcp"]
    }
  }
}
EOF
```

3. **Test it:**
   ```bash
   gemini "Generate a futuristic city"
   ```

---

## 🔑 API Keys Setup (Optional)

### Pollinations.ai (Default - FREE!)
**No setup needed!** Works immediately after installation.

### HuggingFace (FREE Tier)

1. **Create free account:** [huggingface.co](https://huggingface.co)

2. **Get your token:** [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
   - Click "New token"
   - Give it a name (e.g., "imagegen-mcp")
   - Select "Read" permissions
   - Copy the token (starts with `hf_...`)

3. **Set environment variable:**

**macOS/Linux:**
```bash
echo 'export HUGGINGFACE_API_KEY="hf_..."' >> ~/.zshrc
source ~/.zshrc
```

**Windows:**
```powershell
setx HUGGINGFACE_API_KEY "hf_..."
```

### OpenAI (Paid)

1. **Get API key:** [platform.openai.com/api-keys](https://platform.openai.com/api-keys)

2. **Set environment variable:**

**macOS/Linux:**
```bash
echo 'export OPENAI_API_KEY="sk-..."' >> ~/.zshrc
source ~/.zshrc
```

**Windows:**
```powershell
setx OPENAI_API_KEY "sk-..."
```

---

## ✅ Verification

### Test Each Platform

**Claude Desktop:**
```
Generate a test image: red square on white background
```

**Claude Code:**
```bash
claude "Generate a blue circle"
```

**Cursor:**
Ask Cursor AI: `Generate an image of a sunset`

**Cody:**
Ask Cody: `Generate a beach scene`

**Gemini CLI:**
```bash
gemini "Generate a mountain landscape"
```

### Check Installation

```bash
# NPM installation
npm list -g @stonezone/imagegen-mcp

# Python installation
pip show imagegen-mcp
```

---

## 🐛 Troubleshooting

### "Command not found" or "Module not found"

**Solution 1:** Reinstall
```bash
# NPM
npm install -g @stonezone/imagegen-mcp

# Python
pip install -e .
```

**Solution 2:** Check PATH
```bash
# NPM global bin location
npm config get prefix

# Python location
which python
```

### "OPENAI_API_KEY not found"

**Solution:** You're trying to use OpenAI provider without an API key.

Either:
1. Use Pollinations instead (FREE): `Generate using pollinations: ...`
2. Set your OpenAI API key (see API Keys Setup above)

### "Model is loading" (HuggingFace)

**Solution:** HuggingFace free tier has cold starts. Wait 1-2 minutes and try again.

### Claude Desktop not detecting MCP server

**Solution:**
1. Verify config file path is correct
2. Check JSON syntax is valid (use [jsonlint.com](https://jsonlint.com))
3. Make sure to **completely restart** Claude Desktop (Quit, don't just close window)
4. Check Claude Desktop logs:
   ```bash
   # macOS
   tail -f ~/Library/Logs/Claude/mcp*.log
   ```

### Permission denied errors

**Solution:**
```bash
# Make server executable
chmod +x bin/imagegen-mcp.js
chmod +x src/imagegen_mcp/server.py

# Create output directory
mkdir -p generated_images
chmod 755 generated_images
```

### Python version issues

**Solution:**
```bash
# Check version (must be 3.10+)
python --version

# Try python3 instead
python3 --version

# Update if needed (macOS with Homebrew)
brew install python@3.10
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

## 📖 Next Steps

1. ✅ Installation complete!
2. 📚 Read [README.md](README.md) for usage examples
3. 🧪 Try different providers:
   - **FREE:** Pollinations.ai (default)
   - **FREE Tier:** HuggingFace
   - **Paid:** OpenAI
4. 🎨 Experiment with image manipulation tools
5. ⭐ Star the repo: [github.com/stonezone/imagegenMCP](https://github.com/stonezone/imagegenMCP)

---

## 🆘 Support

- 📫 [GitHub Issues](https://github.com/stonezone/imagegenMCP/issues)
- 💬 [GitHub Discussions](https://github.com/stonezone/imagegenMCP/discussions)
- 📖 [Full Documentation](https://github.com/stonezone/imagegenMCP)

---

**Happy Image Generating! 🎨✨**
