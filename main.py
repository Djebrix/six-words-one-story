#!/usr/bin/env python3
"""Six Words, One Story — writes a complete six-word story to entry.txt.

Standard library only, no network, deterministic.
"""
import os
from pathlib import Path

STORY = "Widow remarried. The portrait still watches."


def main() -> None:
    words = STORY.split()
    assert len(words) == 6, f"expected exactly 6 words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, f"expected 1-60 chars, got {len(STORY)}"
    assert STORY.strip(), "story must not be only whitespace"
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(STORY, encoding="utf-8")


if __name__ == "__main__":
    main()
