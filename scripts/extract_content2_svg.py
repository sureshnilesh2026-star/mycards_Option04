"""Extract content2 SVG from agent transcript JSONL."""
import json
import re
from pathlib import Path

TRANSCRIPT = Path(
    r"C:\Users\Suresh\.cursor\projects\d-Work-HDFC-CursorProjects-MyCards-mycards-01"
    r"\agent-transcripts\c9bb43c7-4438-4d00-b62b-9ee6c9aa1791"
    r"\c9bb43c7-4438-4d00-b62b-9ee6c9aa1791.jsonl"
)
OUT = Path(__file__).resolve().parent.parent / "assets" / "content2-design.svg"


def main() -> None:
    with TRANSCRIPT.open(encoding="utf-8") as f:
        for line in f:
            # JSONL escapes double quotes as \"
            if 'width=\\"552\\" height=\\"221\\"' not in line:
                continue
            if "Add content2 layer" not in line:
                continue
            rec = json.loads(line)
            text = rec["message"]["content"][0]["text"]
            m = re.search(r"<svg[\s\S]*?</svg>", text)
            if not m:
                raise SystemExit("SVG not found in message")
            OUT.write_text(m.group(0), encoding="utf-8")
            print("Wrote", OUT, "bytes", len(m.group(0)))
            return
    raise SystemExit("No matching line in transcript")


if __name__ == "__main__":
    main()
