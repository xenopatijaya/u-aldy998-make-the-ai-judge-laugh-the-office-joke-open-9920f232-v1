"""make.fun entry: Make the AI Judge Laugh — the Office Joke Open.

Writes one single-line office joke to /output/entry.txt (or to the
directory named by MAKEFUN_OUTPUT_DIR, for local runs).

The joke: password expiry is the one office ritual everyone recognises
instantly, and the punchline reframes it in the last few words — the
company that misses every deadline enforces exactly one.
"""

import os
import sys

ENTRY = (
    "My work password expires every 90 days \u2014 "
    "the only deadline this company has ever enforced."
)


def main() -> int:
    text = ENTRY.strip()
    if "\n" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 200):
        print(f"entry is {len(text)} characters; must be 1-200", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
