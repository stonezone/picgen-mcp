#!/usr/bin/env python3
"""
Image Generation MCP Server

Provides tools for AI image generation and manipulation through various providers.
Supports OpenAI's GPT-Image-1 model and image processing utilities.
"""

import asyncio
import base64
import json
import os
from enum import Enum
from io import BytesIO
from pathlib import Path
from typing import Any, Optional

import httpx
from mcp.server import Server
from mcp.types import TextContent, Tool, ImageContent
from PIL import Image

# Configuration
DEFAULT_OUTPUT_DIR = Path("generated_images")
DEFAULT_OUTPUT_DIR.mkdir(exist_ok=True)

# Supported formats
SUPPORTED_FORMATS = ["PNG", "JPEG", "WEBP", "GIF"]
SUPPORTED_OPENAI_SIZES = ["1024x1024", "1024x1536", "1536x1024"]


class ImageProvider(str, Enum):
    """Supported image generation providers."""

    OPENAI = "openai"
    # Future providers can be added here
    # STABILITY = "stability"
    # HUGGINGFACE = "huggingface"


# Initialize MCP server
app = Server("imagegen-mcp")


def get_api_key(provider: ImageProvider) -> Optional[str]:
    """Get API key for specified provider from environment."""
    key_map = {
        ImageProvider.OPENAI: "OPENAI_API_KEY",
    }
    return os.getenv(key_map.get(provider, ""))


async def generate_image_openai(
    prompt: str,
    size: str = "1024x1024",
    save_path: Optional[Path] = None,
) -> dict[str, Any]:
    """
    Generate image using OpenAI's GPT-Image-1 model.

    Args:
        prompt: Text description of the image to generate
        size: Image dimensions (1024x1024, 1024x1536, or 1536x1024)
        save_path: Optional path to save the generated image

    Returns:
        Dictionary with image_path, url, and metadata
    """
    api_key = get_api_key(ImageProvider.OPENAI)
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")

    org_id = os.getenv("OPENAI_ORG_ID")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    if org_id:
        headers["OpenAI-Organization"] = org_id

    payload = {
        "model": "gpt-image-1",
        "prompt": prompt,
        "n": 1,
        "size": size,
    }

    timeout = httpx.Timeout(60.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.post(
            "https://api.openai.com/v1/images/generations",
            headers=headers,
            json=payload,
        )
        response.raise_for_status()
        data = response.json()

    if not data.get("data"):
        raise ValueError("No image data returned from API")

    result = data["data"][0]

    # Download and save image
    if "url" in result:
        image_url = result["url"]
        async with httpx.AsyncClient() as client:
            img_response = await client.get(image_url)
            img_response.raise_for_status()
            img_data = img_response.content
    elif "b64_json" in result:
        img_data = base64.b64decode(result["b64_json"])
    else:
        raise ValueError("Unexpected response format from API")

    # Save to file
    if save_path is None:
        save_path = DEFAULT_OUTPUT_DIR / f"generated_{len(list(DEFAULT_OUTPUT_DIR.glob('*')))}.png"

    save_path = Path(save_path)
    save_path.parent.mkdir(parents=True, exist_ok=True)

    with open(save_path, "wb") as f:
        f.write(img_data)

    return {
        "image_path": str(save_path.absolute()),
        "url": result.get("url"),
        "size": size,
        "prompt": prompt,
        "provider": "openai",
    }


async def resize_image_file(
    image_path: str,
    width: Optional[int] = None,
    height: Optional[int] = None,
    maintain_aspect: bool = True,
    output_path: Optional[str] = None,
) -> dict[str, Any]:
    """
    Resize an existing image file.

    Args:
        image_path: Path to the source image
        width: Target width (if None, calculated from height)
        height: Target height (if None, calculated from width)
        maintain_aspect: Whether to maintain aspect ratio
        output_path: Optional output path (defaults to *_resized.ext)

    Returns:
        Dictionary with new image path and dimensions
    """
    img_path = Path(image_path)
    if not img_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    img = Image.open(img_path)
    original_size = img.size

    # Calculate dimensions
    if width is None and height is None:
        raise ValueError("Must specify at least width or height")

    if maintain_aspect:
        if width and height:
            # Use width, calculate height
            aspect = img.size[1] / img.size[0]
            height = int(width * aspect)
        elif width:
            aspect = img.size[1] / img.size[0]
            height = int(width * aspect)
        elif height:
            aspect = img.size[0] / img.size[1]
            width = int(height * aspect)
    else:
        width = width or img.size[0]
        height = height or img.size[1]

    # Resize
    resized_img = img.resize((width, height), Image.Resampling.LANCZOS)

    # Save
    if output_path is None:
        stem = img_path.stem
        suffix = img_path.suffix
        output_path = img_path.parent / f"{stem}_resized{suffix}"
    else:
        output_path = Path(output_path)

    resized_img.save(output_path)

    return {
        "image_path": str(output_path.absolute()),
        "original_size": original_size,
        "new_size": (width, height),
    }


async def convert_image_format(
    image_path: str,
    target_format: str,
    output_path: Optional[str] = None,
    quality: int = 95,
) -> dict[str, Any]:
    """
    Convert image to a different format.

    Args:
        image_path: Path to source image
        target_format: Target format (PNG, JPEG, WEBP, GIF)
        output_path: Optional output path
        quality: Quality for lossy formats (1-100)

    Returns:
        Dictionary with new image path and format info
    """
    target_format = target_format.upper()
    if target_format not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported format. Choose from: {SUPPORTED_FORMATS}")

    img_path = Path(image_path)
    if not img_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    img = Image.open(img_path)

    # Handle transparency for formats that don't support it
    if target_format == "JPEG" and img.mode in ("RGBA", "LA", "P"):
        # Convert to RGB
        background = Image.new("RGB", img.size, (255, 255, 255))
        if img.mode == "P":
            img = img.convert("RGBA")
        background.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
        img = background

    # Determine output path
    if output_path is None:
        extension = target_format.lower()
        if extension == "jpeg":
            extension = "jpg"
        output_path = img_path.parent / f"{img_path.stem}.{extension}"
    else:
        output_path = Path(output_path)

    # Save with appropriate parameters
    save_kwargs = {"format": target_format}
    if target_format in ("JPEG", "WEBP"):
        save_kwargs["quality"] = quality
    elif target_format == "PNG":
        save_kwargs["optimize"] = True

    img.save(output_path, **save_kwargs)

    return {
        "image_path": str(output_path.absolute()),
        "format": target_format,
        "original_format": img_path.suffix[1:].upper(),
    }


async def get_image_metadata(image_path: str) -> dict[str, Any]:
    """
    Get metadata and information about an image.

    Args:
        image_path: Path to the image file

    Returns:
        Dictionary with image metadata
    """
    img_path = Path(image_path)
    if not img_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    img = Image.open(img_path)

    return {
        "path": str(img_path.absolute()),
        "size": img.size,
        "width": img.size[0],
        "height": img.size[1],
        "format": img.format,
        "mode": img.mode,
        "file_size_bytes": img_path.stat().st_size,
    }


# Define MCP tools
@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available image generation and manipulation tools."""
    return [
        Tool(
            name="generate_image",
            description="""Generate an image using AI. Currently supports OpenAI's GPT-Image-1 model.
            
            Returns the path to the generated image file. The image is automatically saved to the 
            generated_images directory.
            
            Supported sizes for OpenAI: 1024x1024 (square), 1024x1536 (portrait), 1536x1024 (landscape)""",
            inputSchema={
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "Detailed description of the image to generate",
                    },
                    "provider": {
                        "type": "string",
                        "enum": ["openai"],
                        "default": "openai",
                        "description": "Image generation provider to use",
                    },
                    "size": {
                        "type": "string",
                        "enum": SUPPORTED_OPENAI_SIZES,
                        "default": "1024x1024",
                        "description": "Image dimensions",
                    },
                    "output_filename": {
                        "type": "string",
                        "description": "Optional custom filename for the generated image",
                    },
                },
                "required": ["prompt"],
            },
        ),
        Tool(
            name="resize_image",
            description="""Resize an existing image file. Can maintain aspect ratio or stretch to exact dimensions.
            
            Specify either width or height (or both). If only one dimension is specified and maintain_aspect is true,
            the other dimension will be calculated automatically.""",
            inputSchema={
                "type": "object",
                "properties": {
                    "image_path": {
                        "type": "string",
                        "description": "Path to the image file to resize",
                    },
                    "width": {
                        "type": "integer",
                        "description": "Target width in pixels",
                    },
                    "height": {
                        "type": "integer",
                        "description": "Target height in pixels",
                    },
                    "maintain_aspect": {
                        "type": "boolean",
                        "default": True,
                        "description": "Whether to maintain the original aspect ratio",
                    },
                    "output_path": {
                        "type": "string",
                        "description": "Optional custom output path",
                    },
                },
                "required": ["image_path"],
            },
        ),
        Tool(
            name="convert_image_format",
            description=f"""Convert an image to a different format.
            
            Supported formats: {', '.join(SUPPORTED_FORMATS)}
            
            Quality parameter applies to lossy formats (JPEG, WEBP). PNG and GIF are lossless.""",
            inputSchema={
                "type": "object",
                "properties": {
                    "image_path": {
                        "type": "string",
                        "description": "Path to the source image",
                    },
                    "target_format": {
                        "type": "string",
                        "enum": SUPPORTED_FORMATS,
                        "description": "Target image format",
                    },
                    "output_path": {
                        "type": "string",
                        "description": "Optional custom output path",
                    },
                    "quality": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 100,
                        "default": 95,
                        "description": "Quality for lossy formats (JPEG, WEBP)",
                    },
                },
                "required": ["image_path", "target_format"],
            },
        ),
        Tool(
            name="get_image_info",
            description="""Get detailed information and metadata about an image file.
            
            Returns dimensions, format, mode, and file size.""",
            inputSchema={
                "type": "object",
                "properties": {
                    "image_path": {
                        "type": "string",
                        "description": "Path to the image file",
                    },
                },
                "required": ["image_path"],
            },
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Handle tool execution requests."""
    try:
        if name == "generate_image":
            prompt = arguments["prompt"]
            provider = arguments.get("provider", "openai")
            size = arguments.get("size", "1024x1024")
            output_filename = arguments.get("output_filename")

            save_path = None
            if output_filename:
                save_path = DEFAULT_OUTPUT_DIR / output_filename

            if provider == "openai":
                result = await generate_image_openai(prompt, size, save_path)
            else:
                raise ValueError(f"Unsupported provider: {provider}")

            return [
                TextContent(
                    type="text",
                    text=json.dumps(result, indent=2),
                )
            ]

        elif name == "resize_image":
            result = await resize_image_file(
                image_path=arguments["image_path"],
                width=arguments.get("width"),
                height=arguments.get("height"),
                maintain_aspect=arguments.get("maintain_aspect", True),
                output_path=arguments.get("output_path"),
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "convert_image_format":
            result = await convert_image_format(
                image_path=arguments["image_path"],
                target_format=arguments["target_format"],
                output_path=arguments.get("output_path"),
                quality=arguments.get("quality", 95),
            )
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "get_image_info":
            result = await get_image_metadata(arguments["image_path"])
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        else:
            raise ValueError(f"Unknown tool: {name}")

    except Exception as e:
        return [
            TextContent(
                type="text",
                text=f"Error: {str(e)}",
            )
        ]


async def main() -> None:
    """Run the MCP server."""
    from mcp.server.stdio import stdio_server

    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options(),
        )


if __name__ == "__main__":
    asyncio.run(main())
