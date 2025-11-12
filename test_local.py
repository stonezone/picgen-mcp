#!/usr/bin/env python3
"""
Quick test script to verify the MCP server works before publishing.
"""

import asyncio
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from imagegen_mcp.server import (
    generate_image_pollinations,
    generate_image_openai,
    generate_image_huggingface,
    resize_image_file,
    convert_image_format,
    get_image_metadata,
)


async def test_pollinations():
    """Test Pollinations.ai (FREE - no API key needed)."""
    print("\n🎨 Testing Pollinations.ai (FREE)...")
    try:
        result = await generate_image_pollinations(
            prompt="a red circle on white background",
            size="256x256",
            model="turbo"  # Faster for testing
        )
        print(f"✅ Success! Image saved to: {result['image_path']}")
        return result['image_path']
    except Exception as e:
        print(f"❌ Failed: {e}")
        return None


async def test_image_manipulation(image_path: str):
    """Test image manipulation tools."""
    print("\n🔧 Testing image manipulation...")
    
    # Test resize
    print("  → Resizing to 128x128...")
    try:
        result = await resize_image_file(
            image_path=image_path,
            width=128,
            height=128,
            maintain_aspect=True
        )
        print(f"  ✅ Resized: {result['image_path']}")
    except Exception as e:
        print(f"  ❌ Resize failed: {e}")
    
    # Test format conversion
    print("  → Converting to JPEG...")
    try:
        result = await convert_image_format(
            image_path=image_path,
            target_format="JPEG",
            quality=90
        )
        print(f"  ✅ Converted: {result['image_path']}")
    except Exception as e:
        print(f"  ❌ Conversion failed: {e}")
    
    # Test metadata extraction
    print("  → Getting metadata...")
    try:
        result = await get_image_metadata(image_path)
        print(f"  ✅ Metadata: {result['width']}x{result['height']} {result['format']}")
    except Exception as e:
        print(f"  ❌ Metadata failed: {e}")


async def test_openai():
    """Test OpenAI (requires API key)."""
    import os
    
    if not os.getenv("OPENAI_API_KEY"):
        print("\n⚠️  Skipping OpenAI test (no API key)")
        return
    
    print("\n🎨 Testing OpenAI GPT-Image-1...")
    try:
        result = await generate_image_openai(
            prompt="a blue square",
            size="1024x1024"
        )
        print(f"✅ Success! Image saved to: {result['image_path']}")
    except Exception as e:
        print(f"❌ Failed: {e}")


async def test_huggingface():
    """Test HuggingFace (requires API key, may have cold start)."""
    import os
    
    if not os.getenv("HUGGINGFACE_API_KEY"):
        print("\n⚠️  Skipping HuggingFace test (no API key)")
        return
    
    print("\n🎨 Testing HuggingFace...")
    print("   (This may take 1-2 minutes on first run due to cold start)")
    try:
        result = await generate_image_huggingface(
            prompt="a green triangle",
            size="512x512"
        )
        print(f"✅ Success! Image saved to: {result['image_path']}")
    except Exception as e:
        print(f"❌ Failed: {e}")


async def main():
    """Run all tests."""
    print("=" * 60)
    print("🧪 Testing Image Generation MCP Server")
    print("=" * 60)
    
    # Test Pollinations (always works, no API key needed)
    image_path = await test_pollinations()
    
    # Test image manipulation if we got an image
    if image_path:
        await test_image_manipulation(image_path)
    
    # Test optional providers (require API keys)
    await test_openai()
    await test_huggingface()
    
    print("\n" + "=" * 60)
    print("✅ Testing complete!")
    print("=" * 60)
    print("\n📁 Check the 'generated_images/' directory for output files")


if __name__ == "__main__":
    asyncio.run(main())
