"""Build teacher-notes.md for one week from that week's slide files.

Usage:  python tools/make_notes.py 1
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def text_of(fragment):
    fragment = re.sub(r"<br\s*/?>", " ", fragment)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    return " ".join(html.unescape(fragment).split())


def main(week):
    src = ROOT / "deck-source" / f"week-{week:02d}" / "project"
    deck = json.loads((src / "deck.json").read_text(encoding="utf-8"))
    out_dir = next(ROOT.glob(f"Week-{week:02d}_*"))
    starts = {s["start"]: s["description"] for s in deck["sections"].values()}

    lines = [f"# {deck['title']}: teacher notes", ""]
    for number, slide_id in enumerate(deck["order"], 1):
        path = src / "slides" / f"{slide_id}.html"
        if not path.exists():
            continue
        body = path.read_text(encoding="utf-8")
        if slide_id in starts:
            lines += [f"## {starts[slide_id]}", ""]
        title = re.search(r"<h[12][^>]*>(.*?)</h[12]>", body, re.S)
        notes = re.search(r"<aside>(.*?)</aside>", body, re.S)
        lines.append(f"### Slide {number}: {text_of(title.group(1)) if title else slide_id}")
        lines += ["", text_of(notes.group(1)) if notes else "_No notes._", ""]

    target = out_dir / "teacher-notes.md"
    target.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {target}")


if __name__ == "__main__":
    main(int(sys.argv[1]))
