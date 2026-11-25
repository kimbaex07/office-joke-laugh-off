"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line joke about office life to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure Python 3 stdlib, deterministic,
no network, no randomness.

Gate (per the kit RULES.txt): the entry must be UTF-8 text of 1 to
200 characters, a single line, and not only whitespace. This program
self-checks the gate before writing and raises on any violation.
"""

import os

JOKE = (
    "My boss told me to treat this job like my own business, "
    "so I took a three-hour lunch and blamed the economy."
)


def main() -> None:
    line = JOKE

    # Self-check the gate before writing anything.
    if not line or line.strip() == "":
        raise ValueError("entry is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(line)
        )

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
