#!/usr/bin/env python3
"""Passive-aggressive fridge note.

The fridge has perfect memory and a grudge: it remembered the
owner's birthday, said nothing for eleven months, and now lets
the magnets do the judging.

Stdlib only. Deterministic: every run writes the same bytes.
"""

from pathlib import Path

# The note, kept in small pieces so each clause stays readable.
OPENING = "I remember your birthday. "
WITHHELD = "I've kept it to myself for eleven months "
REASON = "out of respect, "
PUNCHLINE = "but the magnets know, and they're disappointed."

OUTPUT_PATH = Path("/output/entry.txt")


def build_note() -> str:
    """Join the clauses into the single-line fridge note."""
    return OPENING + WITHHELD + REASON + PUNCHLINE


def main() -> None:
    note = build_note()
    # Guard the entry gate before writing: one line, 1-200 chars.
    assert 1 <= len(note) <= 200, "entry must be 1-200 characters"
    assert "\n" not in note and note.strip(), "entry must be a single non-blank line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(note, encoding="utf-8")


if __name__ == "__main__":
    main()
