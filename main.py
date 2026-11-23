#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — entry program.

Writes a single one-line office joke to /output/entry.txt.
Gate: UTF-8, 1-199 characters, not only whitespace.
"""

import os

JOKE = "I asked HR for a raise and they gave me a pizza party \u2014 turns out my salary is paid in pepperoni."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
