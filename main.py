"""The 3AM Fridge Text — the one line a smart fridge texts its owner at 3am.

Writes the single line to /output/entry.txt. Deterministic: the same
fixed string on every run, no input, no randomness, no network, no
environment secrets. Python 3 stdlib only.
"""

from pathlib import Path

TEXT = "It's 3am. The leftovers from Tuesday have formed a union, and their first demand is: stop opening me just to stare at them."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
# not only white space, and a single line. Fail loudly instead of
# shipping an entry the scorer would refuse.
assert 1 <= len(TEXT) <= 140, f"entry is {len(TEXT)} characters"
assert "\n" not in TEXT and TEXT.strip() == TEXT


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
