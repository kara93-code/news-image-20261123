#!/usr/bin/env python3
"""Write the NI23 front page to the grader output directory.

The picture itself is bundled with this repository (assets/entry.jpg,
a 1024x1024 JPEG under 1 MiB). This program only checks that the bundled
bytes are a complete JPEG of the expected frame and copies them to
``$MAKEFUN_OUTPUT_DIR/entry.png`` (default ``/output``). Standard library
only: no network, no third-party imports, deterministic output.
"""

import os
import stat
import sys

BUNDLED = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "assets", "entry.jpg")
EXPECTED_W = 1024
EXPECTED_H = 1024
LIMIT = 1048576


def read_bundled(path):
    with open(path, "rb") as handle:
        payload = handle.read()
    if len(payload) < 4 or len(payload) > LIMIT:
        raise SystemExit("bundled image has an unexpected size")
    if payload[0:2] != b"\xff\xd8" or payload[-2:] != b"\xff\xd9":
        raise SystemExit("bundled image is not a whole JPEG")
    return payload


def frame_size(payload):
    """Walk JPEG markers until the frame header gives width/height."""
    pos = 2
    while pos + 9 <= len(payload):
        if payload[pos] != 0xFF:
            raise SystemExit("broken JPEG marker stream")
        marker = payload[pos + 1]
        if marker == 0xD8 or marker == 0x01 or 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        size = int.from_bytes(payload[pos + 2:pos + 4], "big")
        if size < 2 or pos + 2 + size > len(payload):
            raise SystemExit("JPEG segment runs past the end of the file")
        if marker in (0xC0, 0xC1, 0xC2):
            height = int.from_bytes(payload[pos + 5:pos + 7], "big")
            width = int.from_bytes(payload[pos + 7:pos + 9], "big")
            return width, height
        pos += 2 + size
    raise SystemExit("no JPEG frame header found")


def main():
    payload = read_bundled(BUNDLED)
    width, height = frame_size(payload)
    if (width, height) != (EXPECTED_W, EXPECTED_H):
        raise SystemExit("bundled image is not 1024x1024")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") or "/output"
    os.makedirs(outdir, exist_ok=True)
    target = os.path.join(outdir, "entry.png")
    with open(target, "wb") as handle:
        handle.write(payload)
    os.chmod(target, 0o644)
    mode = stat.S_IMODE(os.stat(target).st_mode)
    if mode != 0o644:
        raise SystemExit("output file mode is not 0644")
    print(f"wrote {target} ({len(payload)} bytes, {width}x{height})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
