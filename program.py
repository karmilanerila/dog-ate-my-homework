#!/usr/bin/env python3
"""The dog ate my homework — make.fun entry.

When the homework itself says "chew on this problem", the only correct
response is to take it literally. This script writes that one-liner to
the file the judge reads.
"""

import os

LINE = "The homework said 'chew on this problem.' So I did. Problem solved."

# The judge reads exactly one line from this file.
ENTRY_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def resolve_output_dir():
    """Pick where entry.txt goes: the judge's dir when set, else /output."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir and env_dir.strip():
        return env_dir.strip()
    return DEFAULT_OUTPUT_DIR


def output_path():
    """Full path of the entry file, inside the resolved output dir."""
    return os.path.join(resolve_output_dir(), ENTRY_FILENAME)


def write_entry():
    """Write the excuse line (plus a trailing newline) as a fresh file."""
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("LINE must be a single line")
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    payload = (LINE + "\n").encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(payload)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    write_entry()
