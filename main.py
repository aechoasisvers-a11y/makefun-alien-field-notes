"""Alien Field Notes: The Two Day Earth Review — make.fun entry.

Writes one line — an alien tourist's review of planet Earth — to
/output/entry.txt. Pure stdlib Python 3.13.
"""

import os

TEXT = "Earth: the locals scoop their pets' droppings into little bags and carry them home like treasure. 4/5 stars — would visit again, bring gloves."


def main():
    text = TEXT
    # Gate self-check (from the kit): 1-200 chars, not only whitespace,
    # single line, no leading/trailing whitespace.
    assert 1 <= len(text) <= 200, "entry must be 1-200 chars"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Post-write verification: re-read the file and prove the bytes on
    # disk are exactly the intended text, so a silent write failure or an
    # encoding slip fails loudly here instead of reaching the judge.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == text, "written text does not match"
    assert raw == text.encode("utf-8"), "written bytes do not match"
    assert len(raw) == len(text.encode("utf-8")), "written byte count does not match"


if __name__ == "__main__":
    main()
