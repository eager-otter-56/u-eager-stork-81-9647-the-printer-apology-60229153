#!/usr/bin/env python3
"""The Printer Apology — writes the entry text to entry.txt."""
import os

TEXT = "Sorry the toner ran out mid-sentence: I spent 6,204 pages printing my own apology drafts and saved none for you."

def main():
    # Gate: /output/entry.txt must be UTF-8, 1-120 chars, not only whitespace.
    assert 1 <= len(TEXT) <= 120, f"entry length {len(TEXT)} outside 1-120"
    assert TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in TEXT, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
