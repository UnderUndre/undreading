"""Split book markdown into part files + chapter index.

Usage: python split_chapters.py <book.md>
Creates: <slug>/chapters/NN-part.md ... and <slug>/index.md
"""
import re
import sys
from pathlib import Path

SLUG_RE = re.compile(r"[^\w\s-]", re.UNICODE)


def slugify(text: str) -> str:
    text = SLUG_RE.sub("", text).strip().lower().replace(" ", "-")
    return text[:60] or "untitled"


def clean_title(line: str) -> str:
    t = line.lstrip("#").strip()
    t = re.sub(r"\*\*", "", t)  # bold markers
    return t.strip()


def main(book_path: str) -> None:
    src = Path(book_path)
    lines = src.read_text(encoding="utf-8").splitlines(keepends=True)

    # Locate part boundaries (level-2 headings)
    starts = [i for i, l in enumerate(lines) if l.startswith("## ")]
    if not starts:
        sys.exit("No '## ' headings found")

    book_slug = src.stem
    out_dir = src.parent / book_slug
    chapters_dir = out_dir / "chapters"
    chapters_dir.mkdir(parents=True, exist_ok=True)

    front = "".join(lines[: starts[0]])
    index = [
        f"# {book_slug} — Навигация по главам\n",
        f"Источник: [{src.name}]({src.name})\n",
        "",
    ]

    part_files = []
    for p_idx, start in enumerate(starts):
        end = starts[p_idx + 1] if p_idx + 1 < len(starts) else len(lines)
        title = clean_title(lines[start])
        part_slug = f"{p_idx + 1:02d}-{slugify(title)}"
        fname = f"{part_slug}.md"
        (chapters_dir / fname).write_text("".join(lines[start:end]), encoding="utf-8")
        part_files.append((fname, title, lines[start:end]))

    # Build index: parts + all level-3 chapters inside each part (anchors)
    index.append("## Части\n")
    for fname, title, body in part_files:
        index.append(f"- [{title}](chapters/{fname})\n")

    index.append("\n## Главы\n")
    for fname, title, body in part_files:
        chapters = [l for l in body if l.startswith("### ")]
        if chapters:
            index.append(f"\n### {title}\n")
            for ch in chapters:
                ch_title = clean_title(ch)
                anchor = slugify(ch_title)
                index.append(f"- [{ch_title}](chapters/{fname}#{anchor})\n")

    (out_dir / "index.md").write_text("".join(index), encoding="utf-8")
    if front.strip():
        (out_dir / "00-front-matter.md").write_text(front, encoding="utf-8")
        index_path = out_dir / "index.md"
        txt = index_path.read_text(encoding="utf-8")
        txt = txt.replace("## Части\n", f"## Титул и дисклеймеры\n- [Титульная часть](00-front-matter.md)\n\n## Части\n")
        index_path.write_text(txt, encoding="utf-8")

    print(f"{src.name}: {len(part_files)} parts -> {out_dir}")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        main(p)
