#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun entry.

Writes a single line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python 3, stdlib only, no network, no reading anything outside this file.
"""

import os
import sys

# v2 — revised in-session: stronger image (the mixtape in the drawer),
# sharper turn (the no you're already living with), more specific and
# harder-won than v1's generic therapist/mother advice.
LINE = (
    "That mixtape you made her will sit in a drawer for twenty years, "
    "so hand it to her tomorrow — the worst she can say is the no "
    "you're already living with."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Gate checks, mirroring the competition gate: UTF-8 text, 1-200 chars,
    # not only whitespace, exactly one line.
    if not LINE or not LINE.strip():
        print("gate failed: empty line", file=sys.stderr)
        return 1
    if len(LINE) > 200:
        print(f"gate failed: {len(LINE)} chars > 200", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("gate failed: line contains a newline", file=sys.stderr)
        return 1
    if LINE != LINE.strip():
        print("gate failed: leading/trailing whitespace", file=sys.stderr)
        return 1

    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Read back and verify the round-trip is byte-identical.
    with open(path, "rb") as f:
        if f.read() != data:
            print("gate failed: round-trip mismatch", file=sys.stderr)
            return 1

    print(f"wrote {len(LINE)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
