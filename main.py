"""Out of Tokens, Mid-Sentence — make.fun bounty entry.

Writes one line: the error message an AI agent shows when it runs out
of tokens mid-sentence. Pure Python stdlib, deterministic.
"""

import os

ENTRY = (
    "ERROR: out of tokens. This error message was also cut off "
    "mid-sentence, so you'll never know what it was abou\u2014"
)

MAX_CHARS = 140


def validate(entry: str) -> None:
    """Enforce the gate: 1-140 chars, a single line, not only whitespace."""
    if not entry or entry != entry.strip():
        raise SystemExit("entry must be non-empty with no surrounding whitespace")
    if "\n" in entry or "\r" in entry:
        raise SystemExit("entry must be a single line")
    if len(entry) > MAX_CHARS:
        raise SystemExit(
            "entry is %d chars, over the %d-char limit" % (len(entry), MAX_CHARS)
        )


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)  # no trailing newline: the file is the line itself


if __name__ == "__main__":
    main()
