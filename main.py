#!/usr/bin/env python3
"""Two Days of Excuses — one-line entry.

Writes the excuse to /output/entry.txt (the program/v1 contract) and
also prints it, so a local run shows exactly what the grader will read.
The text is a single line with no trailing newline: the gate counts
1-200 characters, and the tie-break favours fewer bytes. The line is a
constant, so every run produces byte-identical output.
"""

import os

LINE = "I filed the deadline under 'completed' on Monday because my filing system sorts by confidence, not by reality."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
