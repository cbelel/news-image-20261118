#!/usr/bin/env python3
"""
Entry script for the make.fun bounty 'news-image-20261118':
"Sum up 18 November's world news in one image".

This script finds the pre-rendered newspaper front page image (entry.png)
relative to its own location, determines the target output directory from the
MAKEFUN_OUTPUT_DIR environment variable (defaulting to /output), ensures the
directory exists, and copies the image bytes to <output>/entry.png.
"""

import os
import pathlib
import sys


def main():
    # Resolve script's own directory
    script_dir = pathlib.Path(__file__).parent.resolve()
    source_image = script_dir / "entry.png"

    # Check if source image exists, fail gracefully with a clear message if missing
    if not source_image.is_file():
        sys.stderr.write(f"Error: Required source image '{source_image.name}' not found next to script.\n")
        sys.exit(1)

    # Get output directory from environment or fallback to /output
    output_dir_str = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_dir = pathlib.Path(output_dir_str)

    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    dest_image = output_dir / "entry.png"

    # Read bytes from source and write to destination
    image_bytes = source_image.read_bytes()
    dest_image.write_bytes(image_bytes)

    # Verify destination holds exactly the same number of bytes as the source
    if not dest_image.is_file() or dest_image.stat().st_size != len(image_bytes):
        sys.stderr.write(f"Error: Verification failed. Destination file size does not match source.\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
