#!/usr/bin/env python3
"""news-image-20261124 entry program.

Copies the entry image shipped next to this file to the make.fun output
directory, byte for byte. Standard library only; no network, no third-party
packages, no image processing — the PNG is copied exactly as shipped.

Usage:
    MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
import sys
from pathlib import Path

ENTRY_FILENAME = "entry.png"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    src = Path(__file__).resolve().parent / ENTRY_FILENAME
    if not src.is_file():
        print(f"error: {ENTRY_FILENAME} not found next to main.py",
              file=sys.stderr)
        return 1
    # Sanity check: the shipped file must really be a PNG.
    with src.open("rb") as fh:
        if fh.read(8) != b"\x89PNG\r\n\x1a\n":
            print(f"error: {ENTRY_FILENAME} is not a PNG file",
                  file=sys.stderr)
            return 1

    dest_dir = Path(out_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / ENTRY_FILENAME
    shutil.copyfile(src, dest)
    # Verify the copy landed intact before reporting success.
    if dest.stat().st_size != src.stat().st_size:
        print("error: copied file size does not match source", file=sys.stderr)
        return 1
    print(f"copied {src} -> {dest} ({src.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
