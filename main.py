#!/usr/bin/env python3
"""The Vacuum's Alibi: write one deadpan excuse, <= 200 chars, to /output/entry.txt."""

import os

ENTRY = (
    "14:02 — spot found, scanned twice, and formally classified as "
    "load-bearing. Removing it would void the warranty on the entire house."
)


def main() -> None:
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
