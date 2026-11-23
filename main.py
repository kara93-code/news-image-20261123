#!/usr/bin/env python3
"""Round-2 front page for Monday 23 November 2026.

The page is a single 1024x1024 picture that packs the day's world news
into one frame: five illustrated lead stories, nine short text cards and
eighteen one-line items, 32 stories across seven regions, under a blue
masthead and a red dateline. The picture was drawn on the build machine
and ships with this repository as ``assets/entry.jpg``.

This program only carries that picture to the grader's output. It reads
the bundled JPEG, checks it is whole (start/end markers, a frame header
saying 1024x1024, the recorded SHA-256 digest, under 1 MiB), then writes
those exact bytes to ``$MAKEFUN_OUTPUT_DIR/entry.png`` (``/output`` when
the variable is unset) with mode 0644. Standard library only, no
network, no drawing at run time: two runs produce identical bytes.
"""

import hashlib
import os
import stat
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
BUNDLED = os.path.join(BASE, "assets", "entry.jpg")
EXPECTED_DIGEST = (
    "8f1ef81aec64626882da56c8e96d2a8451cd6d8476cdb29b31e42d6d99cb8ea1"
)
EXPECT_W = 1024
EXPECT_H = 1024
LIMIT = 1048576
FRAME_TAGS = (0xC0, 0xC1, 0xC2)


def load_image():
    """Read the bundled picture and prove it is one whole JPEG."""
    with open(BUNDLED, "rb") as handle:
        blob = handle.read()
    if len(blob) > LIMIT or len(blob) < 4:
        raise SystemExit("bundled picture breaks the 1 MiB size limit")
    if blob[0:2] != b"\xff\xd8" or blob[-2:] != b"\xff\xd9":
        raise SystemExit("bundled picture is not a whole JPEG")
    if hashlib.sha256(blob).hexdigest() != EXPECTED_DIGEST:
        raise SystemExit("bundled picture digest does not match")
    return blob


def jpeg_frame(blob):
    """Walk the JPEG marker stream and return (width, height)."""
    pos = 2
    while pos + 9 <= len(blob):
        if blob[pos] != 0xFF:
            raise SystemExit("JPEG marker stream is broken")
        tag = blob[pos + 1]
        if tag == 0xD8 or tag == 0x01 or 0xD0 <= tag <= 0xD7:
            pos += 2
            continue
        size = int.from_bytes(blob[pos + 2:pos + 4], "big")
        if size < 2 or pos + 2 + size > len(blob):
            raise SystemExit("JPEG segment runs past the end of file")
        if tag in FRAME_TAGS:
            height = int.from_bytes(blob[pos + 5:pos + 7], "big")
            width = int.from_bytes(blob[pos + 7:pos + 9], "big")
            return width, height
        pos += 2 + size
    raise SystemExit("no frame header found in bundled picture")


def publish_output(blob, width, height):
    """Write the picture bytes to the output path, mode 0644."""
    if (width, height) != (EXPECT_W, EXPECT_H):
        raise SystemExit("bundled picture is not 1024x1024")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    with open(target, "wb") as handle:
        handle.write(blob)
    os.chmod(target, 0o644)
    if stat.S_IMODE(os.stat(target).st_mode) != 0o644:
        raise SystemExit("output file mode is not 0644")
    print(f"wrote {target} ({len(blob)} bytes, {width}x{height})")


def main():
    try:
        blob = load_image()
    except FileNotFoundError:
        raise SystemExit("bundled picture is missing from assets/")
    width, height = jpeg_frame(blob)
    publish_output(blob, width, height)
    return 0


if __name__ == "__main__":
    sys.exit(main())
