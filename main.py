#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

Writes a single line of text to /output/entry.txt: the note a smart
fridge leaves on its door screen for its owner.

The joke: the fridge remembered the owner's birthday and sat on it for
eleven months out of "respect" -- and now reports that even the magnets
are disappointed. Smug perfect memory, a small domestic grudge, and the
sting lands in the last clause.

Stdlib only, fully deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "I remember your birthday. I've kept it to myself for eleven months "
    "out of respect, but the magnets know, and they're disappointed."
)
# Gate: 1-200 characters, one line, UTF-8, not only whitespace.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
