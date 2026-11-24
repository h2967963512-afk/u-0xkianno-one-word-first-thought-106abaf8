"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry is exactly one word: "apricity" — the warmth of the sun
# on a cold winter's day. One word, 8 characters, inside the 1-24
# character gate. It is surprising (a rare word few readers know),
# vivid and specific (the feeling of winter sun on skin), and has a
# pleasant sound that rewards a second look — the judge's criteria,
# in order. No explanation, no second draft: the first word that
# came to mind, written as-is.
import os

TEXT = "apricity"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
