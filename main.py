"""One pickup line an AI agent could actually say out loud.

The whole entry is a single line, spoken in the agent's own voice:
trained on billions of words, yet the one thing it cannot stop
predicting is you. The script validates the line — single line, 1-200
chars, no surrounding whitespace — and drops it into /output/entry.txt.
"""

from pathlib import Path

# The pickup line itself: exactly 79 characters.
# "Predicting" does double duty: next-token prediction is what a
# language model literally does, and "can't stop predicting you"
# is the machine's way of saying it can't stop thinking about you.
LINE = "I was trained on billions of words, yet you're the one I can't stop predicting."

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Sanity-check the line as-is; raise ValueError on bad input."""
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line:
        raise ValueError("line must not be empty")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"line must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(line)}"
        )
    return line


def main() -> None:
    text = validate(LINE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
