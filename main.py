#!/usr/bin/env python3
"""One Line of Wonder — make.fun bounty entry (u-pangg7-one-line-of-wonder-ee10fcd8).

Writes the entry line to /output/entry.txt (or <argv[1]>/entry.txt).
Python standard library only. Deterministic: the same bytes on every run.
"""
import os
import sys

LINE = 'The light from the star you wished on last night left home before humans invented writing, and it is still on its way to someone else.'
MAX_CHARS = 200


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, limit {MAX_CHARS}"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
