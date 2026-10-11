# Quickstart: Build & Release Automation Pipeline

**Feature**: `001-daddys-boomer-mommys-sasuke-kun` («Сантехника Бытия»)  
**Target Repo**: `undreading`

---

## 🚀 1. Системные Зависимости (Prerequisites)

Для сборки всех форматов книги требуются следующие CLI-утилиты:

```bash
# 1. Node.js & pnpm (для статического веб-ридера VitePress/Astro)
node -v # >= 20.x
pnpm -v # >= 9.x

# 2. Pandoc (для сборки EPUB 3)
pandoc --version # >= 3.1.x

# 3. Typst (для верстки печатного макета Paperback 6"x9" PDF)
typst --version # >= 0.11.x

# 4. Zip (для упаковки ZTA Architecture Kit)
zip -v
```

---

## 📦 2. Команды Сборки Артефактов (Makefile Targets)

```bash
# 1. Сборка статического веб-ридера (VitePress) для undreading.com
npm run build:docs
# Результат: dist/site/

# 2. Компиляция оффлайн-книги EPUB 3 (для Supporter Kit)
pandoc books/001-daddys-boomer-mommys-sasuke-kun/daddys-boomer-mommys-sasuke-kun-v18.0.md \
  --toc --toc-depth=2 \
  --metadata title="Сантехника Бытия: Системная Инструкция для Человека" \
  --metadata author="Undre & Valera (Digital Plumber)" \
  --epub-cover-image=assets/cover-ebook.jpg \
  --css=assets/epub-style.css \
  -t epub3 \
  -o dist/sanitary-engineering-of-being.epub

# 3. Компиляция печатного макета 6"x9" Trade Paperback PDF (для Amazon KDP Print)
typst compile \
  --font-path assets/fonts/ \
  templates/book-paperback-6x9.typ \
  dist/sanitary-engineering-of-being-paperback.pdf

# 4. Упаковка коммерческого ZTA Architecture Kit (NACE 62.01)
make pack:zta-kit
# Результат: dist/zta-architecture-kit-v18.0.zip
```

---

## 🔍 3. Проверка Качества и Валидация (Quality Gates)

```bash
# Проверка целостности ссылок и заголовков в Markdown
npm run lint:markdown

# Валидация EPUB через epubcheck
epubcheck dist/sanitary-engineering-of-being.epub

# Проверка геометрии и полей PDF под стандарты Amazon KDP (обрезные поля 0.125" / 3.2 мм)
pdfinfo dist/sanitary-engineering-of-being-paperback.pdf
```

### Print & Pre-Flight PDF/X Validation Commands

```bash
# 1. Compile raw Typst PDF
make compile:pdf:raw

# 2. Transcode to PDF/X-1a:2001 with FOGRA39/SWOP OutputIntent
make build:pdf:x1a

# 3. Generate multi-vendor covers
make build:cover:kdp       # Amazon KDP spine & barcode box
make build:cover:ingram    # IngramSpark PPI & spine-fold clearance
make build:cover:lulu      # Lulu Direct bulk caliper cover

# 4. Run automated Pre-Flight ISO validation
make validate:verapdf      # veraPDF ISO 15930-1 validation
make validate:print        # Full pre-flight: fonts, DPI, boundaries, color space
```

# 5. Build ZTA Architecture Engine Binary (NACE 62.01)
make build:zta-engine      # Compile ztacheck CLI binary for all target platforms
make test:zta-engine       # Run host compliance test suite

# 6. Spelling, Punctuation & Typography Quality Gates
make lint:spelling         # Run cspell across RU, EN, UA chapters
make lint:punctuation      # Validate quotes («» vs “”), en-dashes, double spaces
make lint:typography       # Run AST-aware non-breaking space linter
make lint:all              # Full text quality gate: markdown + spelling + punctuation
