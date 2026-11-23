#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch note to /output/entry.txt.

The bug: phantom vibration syndrome -- the thigh reports an incoming
phone call that never happened, even though the body ships with no
vibration motor at all. A real, widely recognised human bug, fixed in
the terse register of a genuine release note.
"""

import os

# Final entry: phantom vibration syndrome. 103 characters, one line.
ENTRY = (
    "v3.5.4: fixed a bug where the thigh hallucinated incoming calls. "
    "No vibration motor was ever installed."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
