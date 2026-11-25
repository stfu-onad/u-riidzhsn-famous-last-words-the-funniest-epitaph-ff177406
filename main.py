"""The funniest one-line famous last words, a tombstone epitaph.

Writes the epitaph to /output/entry.txt (UTF-8, single line, 1-150 chars).
"""

import os

LINE = "Here lies Tom. He held the door for Death. Death said, 'After you.' He's still holding it."

MAX_CHARS = 150


def main() -> None:
    # Normalise once so stray surrounding whitespace can never leak into
    # the entry, then verify the written file round-trips byte-identical.
    line = LINE.strip()
    if not line:
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry line must be 1-{MAX_CHARS} chars, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        if f.read() != line + "\n":
            raise ValueError("written entry did not round-trip")


if __name__ == "__main__":
    main()
