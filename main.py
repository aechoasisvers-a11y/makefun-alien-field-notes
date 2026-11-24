"""Alien Field Notes: The Two Day Earth Review -- make.fun entry.

Writes one original one-line review of planet Earth, left by an alien
tourist, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure stdlib Python 3.13 only. Deterministic: the same bytes every run.
"""

import os

ENTRY_TEXT = (
    "Earth: the locals scoop their pets' droppings into little bags "
    "and carry them home like treasure. "
    "4/5 stars \u2014 would visit again, bring gloves."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)

    # Pass 2 -- self-check: the written file must match the intended text
    # exactly and sit inside the competition's 1-200 character gate, with
    # no trailing newline and more than whitespace.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY_TEXT, "entry.txt does not match intended text"
    assert 1 <= len(written) <= 200, (
        f"char count {len(written)} outside 1-200 gate"
    )
    assert written.strip(), "entry must not be only whitespace"
    assert not written.endswith("\n"), "no trailing newline allowed"


if __name__ == "__main__":
    main()
