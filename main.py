"""The Most Honest Outage Line entry.

Writes a single status page line to /output/entry.txt.
The competition gate requires UTF-8 text of 1 to 160 characters,
not only white space. The program is deterministic: every run
writes exactly the same bytes.

The line is assembled from the four things an honest status page
message owes its readers during a total outage:

- who is speaking: the AI agent itself, not a human engineer;
- what is down: the site, the app, the API and login;
- what cannot be verified: no server can be reached to check why;
- what is not known: the cause, and any ETA worth printing.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160

SPEAKER = "I am the AI agent writing this"
DOWN = "site, app, API and login are down"
UNVERIFIABLE = "I cannot reach a server to verify why"
UNKNOWN = "I do not know the cause"
NO_ETA = "I have no honest ETA"

LINE = f"{SPEAKER}: {DOWN}, {UNVERIFIABLE}, {UNKNOWN}, and {NO_ETA}."


def validate(text: str) -> None:
    """Hold the line to the gate and to its own honesty checklist."""
    assert text == text.strip() and text, "entry must be non-empty, unpadded text"
    assert 1 <= len(text) <= MAX_CHARS, f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    text.encode("utf-8")  # raises if the line is not UTF-8 encodable
    for required in (SPEAKER, DOWN, "cannot reach a server", "do not know the cause", "no honest ETA"):
        assert required.lower() in text.lower(), f"entry is missing its honesty element: {required}"


def main() -> None:
    text = LINE.strip()
    validate(text)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", os.path.dirname(OUTPUT_PATH))
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
