"""Tests for image generation MCP server."""

import pytest
from pathlib import Path
from imagegen_mcp.server import (
    get_image_metadata,
    resize_image_file,
    convert_image_format,
    DEFAULT_OUTPUT_DIR,
)


@pytest.fixture
def sample_image_path(tmp_path):
    """Create a sample test image."""
    from PIL import Image
    
    img = Image.new("RGB", (100, 100), color="red")
    img_path = tmp_path / "test_image.png"
    img.save(img_path)
    return img_path


@pytest.mark.asyncio
async def test_get_image_metadata(sample_image_path):
    """Test getting image metadata."""
    metadata = await get_image_metadata(str(sample_image_path))
    
    assert metadata["width"] == 100
    assert metadata["height"] == 100
    assert metadata["format"] == "PNG"
    assert metadata["mode"] == "RGB"


@pytest.mark.asyncio
async def test_resize_image_maintain_aspect(sample_image_path, tmp_path):
    """Test resizing image while maintaining aspect ratio."""
    output_path = tmp_path / "resized.png"
    
    result = await resize_image_file(
        image_path=str(sample_image_path),
        width=50,
        maintain_aspect=True,
        output_path=str(output_path),
    )
    
    assert result["new_size"] == (50, 50)
    assert Path(result["image_path"]).exists()


@pytest.mark.asyncio
async def test_convert_image_format(sample_image_path, tmp_path):
    """Test converting image format."""
    output_path = tmp_path / "converted.jpg"
    
    result = await convert_image_format(
        image_path=str(sample_image_path),
        target_format="JPEG",
        output_path=str(output_path),
    )
    
    assert result["format"] == "JPEG"
    assert Path(result["image_path"]).exists()
    assert Path(result["image_path"]).suffix == ".jpg"


@pytest.mark.asyncio
async def test_resize_with_height_only(sample_image_path, tmp_path):
    """Test resizing with only height specified."""
    output_path = tmp_path / "resized_height.png"
    
    result = await resize_image_file(
        image_path=str(sample_image_path),
        height=50,
        maintain_aspect=True,
        output_path=str(output_path),
    )
    
    assert result["new_size"] == (50, 50)


@pytest.mark.asyncio
async def test_convert_png_with_transparency(tmp_path):
    """Test converting PNG with transparency to JPEG."""
    from PIL import Image
    
    # Create PNG with transparency
    img = Image.new("RGBA", (100, 100), color=(255, 0, 0, 128))
    png_path = tmp_path / "transparent.png"
    img.save(png_path)
    
    output_path = tmp_path / "converted.jpg"
    
    result = await convert_image_format(
        image_path=str(png_path),
        target_format="JPEG",
        output_path=str(output_path),
    )
    
    assert result["format"] == "JPEG"
    assert Path(result["image_path"]).exists()
