#!/usr/bin/env python3
"""Cross-platform build and release runner for undreading book monograph."""

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK_DIR = ROOT / "books" / "001-daddys-boomer-mommys-sasuke-kun" / "release"
RU_MASTER = BOOK_DIR / "ru-edition" / "ru" / "daddys-boomer-mommys-sasuke-kun-v25.2.md"
EN_MASTER = BOOK_DIR / "en-edition" / "en" / "daddys-boomer-mommys-sasuke-kun-en-v2.4.md"
UA_MASTER = BOOK_DIR / "ua-edition" / "ua" / "daddys-boomer-mommys-sasuke-kun-ua-v1.9.md"

DIST_DIR = ROOT / "dist"
SITE_DIR = DIST_DIR / "site"
TEMPLATES_DIR = ROOT / "templates"
ASSETS_DIR = ROOT / "assets"

def run_cmd(cmd, desc=""):
    print(f"==> {desc or 'Running'}: {' '.join(str(c) for c in cmd)}")
    res = subprocess.run(cmd, cwd=str(ROOT))
    if res.returncode != 0:
        print(f"Error executing command (exit code {res.returncode})")
        return False
    return True

def split_chapters():
    print("==> Splitting master monographs into chapter packages...")
    for master in [RU_MASTER, EN_MASTER, UA_MASTER]:
        if master.exists():
            subprocess.run([sys.executable, str(BOOK_DIR / "split_chapters.py"), str(master)], check=True)
    return True

def validate():
    print("==> Running book integrity & structure validation...")
    val_script = BOOK_DIR / "validate_books.py"
    if val_script.exists():
        res = subprocess.run([sys.executable, str(val_script)], check=True)
        return res.returncode == 0
    return True

def build_docs():
    split_chapters()
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    vitepress_config = ROOT / "docs" / ".vitepress" / "config.ts"
    if shutil.which("npx") and vitepress_config.exists():
        return run_cmd(["npx", "vitepress", "build", "docs", "--outDir", str(SITE_DIR)], "Building VitePress docs")
    else:
        print(f"==> Populating {SITE_DIR} from release directory...")
        ru_dist = BOOK_DIR / "ru-edition" / "ru"
        if ru_dist.exists():
            shutil.copytree(ru_dist, SITE_DIR, dirs_exist_ok=True)
            print(f"Copied release navigation to {SITE_DIR}")
        return True

def build_epub():
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    out_file = DIST_DIR / "sanitary-engineering-of-being-ru.epub"
    if shutil.which("pandoc"):
        css_file = TEMPLATES_DIR / "epub-style.css"
        cmd = [
            "pandoc", str(RU_MASTER),
            "--toc", "--toc-depth=2",
            "--metadata", "title=Сантехника Бытия: Системная Инструкция для Человека",
            "--metadata", "author=Undre & Valera (Digital Plumber)",
            "-t", "epub3",
            "-o", str(out_file)
        ]
        if css_file.exists():
            cmd.extend(["--css", str(css_file)])
        return run_cmd(cmd, "Compiling EPUB 3 via Pandoc")
    else:
        print("==> Notice: 'pandoc' CLI not installed in PATH. Target ready for CI pipeline.")
        return True

def build_pdf():
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    out_file = DIST_DIR / "sanitary-engineering-of-being-paperback.pdf"
    typst_tpl = TEMPLATES_DIR / "book-paperback-6x9.typ"
    if shutil.which("typst"):
        cmd = [
            "typst", "compile",
            "--font-path", str(ASSETS_DIR / "fonts"),
            str(typst_tpl),
            str(out_file)
        ]
        return run_cmd(cmd, "Compiling 6x9 Paperback PDF via Typst")
    else:
        print("==> Notice: 'typst' CLI not installed in PATH. Target ready for CI pipeline.")
        return True

def pack_zta_kit():
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    out_file = DIST_DIR / "zta-architecture-kit-v25.2.zip"
    zta_src = TEMPLATES_DIR / "zta-kit"
    if zta_src.exists():
        archive_base = str(DIST_DIR / "zta-architecture-kit-v25.2")
        shutil.make_archive(archive_base, "zip", str(TEMPLATES_DIR), "zta-kit")
        print(f"==> ZTA Kit packaged: {out_file}")
    return True

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "all"
    targets = {
        "split:chapters": split_chapters,
        "validate": validate,
        "build:docs": build_docs,
        "build:epub": build_epub,
        "build:pdf": build_pdf,
        "pack:zta-kit": pack_zta_kit,
        "lint:markdown": validate,
        "lint:all": validate,
        "build": lambda: (build_docs() and build_epub() and build_pdf() and pack_zta_kit()),
        "all": lambda: (validate() and split_chapters() and build_docs() and build_epub() and build_pdf() and pack_zta_kit())
    }

    if target not in targets:
        print(f"Unknown target: '{target}'. Available: {list(targets.keys())}")
        sys.exit(1)

    success = targets[target]()
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
