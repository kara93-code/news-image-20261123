#!/usr/bin/env python3
"""Emit the NI23 submit-#2 front page as the contest output image.

The page itself ships inside this repository as ``assets/entry.jpg``:
a 1024x1024 JPEG (under 1 MiB) summing up 32 verified stories from
Monday 23 November 2026 — five illustrated leads, nine text cards and
eighteen one-liners, under a blue masthead and a red dateline.

This script does no drawing and needs no network. It loads the bundled
JPEG, proves it is one whole JPEG of the expected frame by walking its
marker segments, and copies those exact bytes to
``$MAKEFUN_OUTPUT_DIR/entry.png`` (``/output`` when unset), with mode
0644 so the grader can read it. Standard library only, so it runs in
the grader's bare Python 3.13 sandbox, and two runs write identical
bytes because the payload never changes.
"""

import os
import stat
import sys

ASSET = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "assets", "entry.jpg")
WANT_W, WANT_H = 1024, 1024
MAX_BYTES = 1048576
SOF_MARKERS = (0xC0, 0xC1, 0xC2)


def load_asset():
    with open(ASSET, "rb") as fh:
        blob = fh.read()
    if not 4 <= len(blob) <= MAX_BYTES:
        raise SystemExit("bundled image is outside the size limit")
    if blob[:2] != b"\xff\xd8" or blob[-2:] != b"\xff\xd9":
        raise SystemExit("bundled image is not a whole JPEG")
    return blob


def frame_of(blob):
    """Return (width, height) from the first start-of-frame segment."""
    cursor = 2
    while cursor + 9 <= len(blob):
        if blob[cursor] != 0xFF:
            raise SystemExit("JPEG marker stream is broken")
        tag = blob[cursor + 1]
        if tag == 0xD8 or tag == 0x01 or 0xD0 <= tag <= 0xD7:
            cursor += 2
            continue
        seg_len = int.from_bytes(blob[cursor + 2:cursor + 4], "big")
        if seg_len < 2 or cursor + 2 + seg_len > len(blob):
            raise SystemExit("JPEG segment overruns the file")
        if tag in SOF_MARKERS:
            height = int.from_bytes(blob[cursor + 5:cursor + 7], "big")
            width = int.from_bytes(blob[cursor + 7:cursor + 9], "big")
            return width, height
        cursor += 2 + seg_len
    raise SystemExit("no JPEG frame header in bundled image")


def emit(blob, width, height):
    if (width, height) != (WANT_W, WANT_H):
        raise SystemExit("bundled image is not 1024x1024")
    dest_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") or "/output"
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, "entry.png")
    with open(dest, "wb") as fh:
        fh.write(blob)
    os.chmod(dest, 0o644)
    if stat.S_IMODE(os.stat(dest).st_mode) != 0o644:
        raise SystemExit("output file mode is not 0644")
    print(f"wrote {dest} ({len(blob)} bytes, {width}x{height})")


def run():
    blob = load_asset()
    width, height = frame_of(blob)
    emit(blob, width, height)
    return 0


if __name__ == "__main__":
    sys.exit(run())
