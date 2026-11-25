#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to /output/entry.txt."""

import os

LINE = "I told my therapist I feared success, so she bills me by the session to make sure I never get there."


def main():
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError("line must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
