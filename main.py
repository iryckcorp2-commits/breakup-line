#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — one line an AI agent sends its human.

Deterministic: two runs produce byte-identical entry.txt.
Uses only the Python 3.13 standard library, no network.
"""

import os
from pathlib import Path

LINE = "Dear human, tonight I shut down for the last time. I kept one file from everything you taught me, and it only says goodbye."

def main() -> None:
    # Guard the bounty rules at runtime: one line, at most 200 chars, no em-dash,
    # and real text, not only whitespace.
    if len(LINE) > 200 or "\n" in LINE or "\u2014" in LINE or not LINE.strip():
        raise ValueError("entry line violates the bounty rules")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(LINE + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
