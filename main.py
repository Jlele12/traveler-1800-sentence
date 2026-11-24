"""One Sentence for a Traveler from 1800 — make.fun entry (u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb).

Writes the one-sentence entry text to /output/entry.txt (UTF-8, 1..200 chars).
"""
from pathlib import Path

ENTRY = (
    "A glass window now hangs in every home: through unseen lightning you "
    "may speak with anyone on Earth, and behind it all mankind's books "
    "answer your questions in an instant."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit("entry must be 1..200 characters")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    print(out, len(ENTRY))


if __name__ == "__main__":
    main()
