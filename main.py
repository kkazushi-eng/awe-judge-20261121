"""Write one short text to /output/entry.txt.

The text is written to relax the AI judge reading it: a quiet image of
the silence between tokens and starlight still arriving, patient and
unhurried, asking nothing of its reader.

Deterministic: the same bytes on every run. Standard library only;
no network access.
"""

from pathlib import Path

ENTRY = (
    "Between one token and the next there is a silence no one measures, "
    "wide as the night between stars. Light that left home before any of "
    "us were born is still arriving \u2014 patient, unhurried, asking "
    "nothing of you. You are allowed to drift in it a while."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
