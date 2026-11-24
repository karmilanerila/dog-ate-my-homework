#!/usr/bin/env python3
"""Dog Ate My Homework — funniest excuse entry.

Writes the excuse line to a file called entry.txt inside the
directory the grader points to via MAKEFUN_OUTPUT_DIR. When that
variable is absent we fall back to /output.
"""

import os

LINE = "The homework said 'chew on this problem.' So I did. Problem solved."


def resolve_target_dir():
    """Pick the output directory: env var wins, /output is the fallback.

    An empty or whitespace-only env value is treated as unset, and the
    result is normalised so odd separators cannot sneak through.
    """
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if chosen and chosen.strip():
        return os.path.normpath(chosen.strip())
    return "/output"


def write_excuse():
    """Create entry.txt holding LINE plus a trailing newline, mode 0644."""
    target_dir = resolve_target_dir()
    os.makedirs(target_dir, exist_ok=True)
    target_path = os.path.join(target_dir, "entry.txt")
    with open(target_path, "wb") as handle:
        handle.write((LINE + "\n").encode("utf-8"))
    os.chmod(target_path, 0o644)
    return target_path


if __name__ == "__main__":
    write_excuse()
