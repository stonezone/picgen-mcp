import os
import json
import base64
import argparse
import httpx
import webbrowser
import platform
from pathlib import Path

# CLI flags
supported_sizes = [
    "1024x1024",
    "1024x1536",
    "1536x1024",
]

parser = argparse.ArgumentParser(
    description=(
        "Generate an image using OpenAI's GPT‑Image‑1 model via the Images API. "
        "Usage: python openai_image_generator_api.py --prompt 'your description' "
        "[--size 1024x1024|1024x1536|1536x1024] [--verbose]. Provide a descriptive "
        "prompt via --prompt and choose an optional image size via --size; if you "
        "omit --size, the default resolution of " + supported_sizes[0] + " is used. "
        "Supported image sizes are: " + ", ".join(supported_sizes) + ". "
        "For example: python openai_image_generator_api.py --prompt 'bricks bouncing' "
        "--size 1024x1536."
    ),
    epilog=(
        "Options:\n"
        "  --prompt    A required text description of the image you want to generate.\n"
        "  --size      Optional image size; choose from " + ", ".join(supported_sizes) + ".\n"
        "  --verbose   Optional flag to print detailed request and response payloads."
    ),
    formatter_class=argparse.RawDescriptionHelpFormatter
)

# Prompt is now provided at runtime via a required argument. This allows automation and
# removes any interactive input. A sensible default image size is used when none is
# specified.
parser.add_argument(
    '--prompt',
    required=True,
    help='The text description of the image you want to generate.'
)

# Expose all allowed sizes as choices for the size argument. If the user does not
# specify a size, the first entry in the list will be used as a default. See
# OpenAI documentation for supported sizes【545151518883858†L639-L643】【767385743998620†L168-L170】.
parser.add_argument(
    '--size',
    choices=supported_sizes,
    default=supported_sizes[0],
    help=(
        "Desired resolution for the generated image. "
        "Choose from " + ", ".join(supported_sizes) + ". "
        "Defaults to " + supported_sizes[0] + " if omitted."
    )
)

parser.add_argument(
    '--verbose',
    action='store_true',
    help='Print full request and response payloads for debugging.'
)

args = parser.parse_args()

# Env
api_key = os.getenv("OPENAI_API_KEY")
org_id = os.getenv("OPENAI_ORG_ID")  # Optional

if not api_key:
    print("Missing OPENAI_API_KEY")
    exit(1)

# Always use OpenAI's gpt-image-1 model for image generation.
# GPT-5 and other models are not supported for images as of 2025【251186143409396†L125-L131】【490526228550146†L642-L664】.
model_choice = {
    "name": "gpt-image-1",
    # Supported sizes for gpt-image-1: square and two rectangular formats
    # according to OpenAI's documentation【545151518883858†L639-L643】【767385743998620†L168-L170】.
    "sizes": ["1024x1024", "1024x1536", "1536x1024"],
}

# Prompt for image comes from CLI. Strip to remove accidental whitespace.
prompt = args.prompt.strip()

# Use the provided size argument or fallback to the default defined in argparse.
size = args.size

# Compose request
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Only add org ID header if it exists
if org_id:
    headers["OpenAI-Organization"] = org_id

json_payload = {
    "model": model_choice['name'],
    "prompt": prompt,
    "n": 1,
    "size": size
}

if args.verbose:
    print("\n--- REQUEST ---")
    print("POST https://api.openai.com/v1/images/generations")
    print("Headers:", json.dumps(headers, indent=2))
    print("Payload:", json.dumps(json_payload, indent=2))

# Make request with longer timeout
timeout = httpx.Timeout(60.0)
try:
    with httpx.Client(timeout=timeout) as client:
        response = client.post(
            "https://api.openai.com/v1/images/generations",
            headers=headers,
            json=json_payload
        )
    
    print("\n--- RESPONSE ---")
    print(f"Status: {response.status_code}")
    response_json = response.json()
    print("Response JSON:", json.dumps(response_json, indent=2))
    
    data = response_json.get("data", [])
    if not data:
        print("❌ No image returned.")
        exit(1)
    
    # Save image
    result = data[0]
    image_path = Path("generated_image.png").resolve()
    
    if "url" in result:
        image_url = result["url"]
        print(f"\n✅ Image URL: {image_url}")
        img_data = httpx.get(image_url).content
    elif "b64_json" in result:
        print("\n✅ Image returned as base64.")
        img_data = base64.b64decode(result["b64_json"])
    else:
        print("❌ Unexpected data format.")
        exit(1)
    
    with open(image_path, "wb") as f:
        f.write(img_data)
    
    print(f"💾 Image saved as: {image_path}")
    
    # Auto-preview image
    print("🖼️ Opening image...")
    webbrowser.open(image_path.as_uri())
    
except Exception as e:
    print(f"\n❗ Exception occurred: {e}")
