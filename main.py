#!/usr/bin/env python3
"""Write the entry text for make.fun bounty the-plan-make-fun-will-carry-20261122-2138.

Standard library only, no network. The text is written byte for byte, with no
trailing newline, into MAKEFUN_OUTPUT_DIR (or /output when unset).
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = (
    "Most likely day 30: $1,750. Floor $1,000.\n"
    "Judge: no step needs a person. Entering is a POST, judging costs cents, and the prize pays the wallet that signed.\n"
    "Today: 24 pots, $6,601, 201,276 entries; thin ones pay 1 place per 30 rivals.\n"
    "Day 1: $0, 3 thinnest, duelled both orders."
)


def output_dir() -> Path:
    """Return the folder the entry text is written to."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text length {len(TEXT)} outside 1..280"
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
