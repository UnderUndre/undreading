# Implementation Plan: 001-daddys-boomer-mommys-sasuke-kun — «Сантехника Бытия»

**Branch**: `001-init` | **Date**: 2026-09-27 | **Spec**: [`spec.md`](spec.md)  
**Input**: Feature specification from `specs/001-daddys-boomer-mommys-sasuke-kun/spec.md`, Business Plan `undreading-business-plan.md` (v2.0), `undrlla-business-plan.md` (v15.1), `undreseller-business-plan.md` (v18.0)

---

## Summary

Монография «Сантехника Бытия» (Daddy's Boomer Mommy's Sasuke-kun) представляет собой открытую цифровую книгу-манифест и прикладную ZTA-инструкцию для человека (System Prompt for Humans). Фича `001-daddys-boomer-mommys-sasuke-kun` сосредоточена на каноническом тексте и **полной матрице из 3 региональных оригиналов и 6 перекрёстных переводов** (всего 9 книг в библиотеке).

Все платформенные, веб- и сборочно-издательские задачи (VitePress/Astro веб-ридер `undreading.com`, конвейер Amazon KDP Print / Typst PDF/X-1a, коммерческий Supporter & ZTA Architecture Kit через Paddle MoR) вынесены в спецификацию [`specs/002-publishing-pipeline-and-platform/`](../002-publishing-pipeline-and-platform/).

---

## Technical Context

**Language/Version**: Markdown (CommonMark/GFM), Python 3.10+ (сплиттеры, валидация)  
**Storage**: Иерархические каталоги `books/001-daddys-boomer-mommys-sasuke-kun/release/` (`ru-edition/`, `en-edition/`, `ua-edition/`), Git-версионирование 3-2-1-1-0  
**Testing/Validation**: Автоматический проверочный комплекс `validate_books.py` (байт-в-байт конкатенация, проверка монотонности, дефектоскопия 110 задвижек P0)  
**Target Matrix**: 3 региональных оригинала × 3 языка = 9 мастер-монолитов + раздельные пакеты глав `chapters/`  
**Scale/Scope**: 9 полных томов монографии (110 P0-задвижек, $\ge 120\,000$ слов в каждом томе)  

---

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Принцип Конституции | Статус | Обоснование и Инженерный Затвор |
| :--- | :--- | :--- |
| **I. Negative Selection (Вычитание шума)** | **PASS** | Монография не содержит абстрактного инфобизнеса; все рекомендации строго выведены из физических, липидологических и юридических пределов. |
| **II. Zero-Trust & Level 1/2 Factuality** | **PASS** | Все дозировки (Аспирин 300 мг, Адреналин 0.3 мг, CWI), формулы (TCO, Little's Law, HOMA-IR) и статьи законов (IRC §864, 127-ФЗ, CP Испании) верифицированы. |
| **III. Strict Authorship Demarcation** | **PASS** | Личный опыт Undre N=1 изолирован в Прологе; внешняя доказательная база синтезирована от лица системного сантехника Валеры / Bob / Дяди Толи. |
| **IV. Open-Source First & Zero-DRM** | **PASS** | Отказ от проприетарного DRM в пользу открытого текста на VitePress/GitHub. Коммерциализация через Supporter Kit (NACE 62.01). |
| **V. Immutable Versioning** | **PASS** | Каждая версия фиксируется как неизменяемый файл `daddys-boomer-mommys-sasuke-kun-v<N>.md`. Старые версии не затираются. |

---

## Project Structure

### Source Code & Monograph Layout (`repos/undreading`)

```text
undreading/
├── books/
│   └── 001-daddys-boomer-mommys-sasuke-kun/
│       ├── archive/                                      # Исторический архив ревизий (v10–v25.1)
│       └── release/                                      # Релизная матрица изданий (3 оригинала + 6 переводов)
│           ├── STYLE-GUARD-EN.md                         # Английский стилистический гайд (Bob the Gray)
│           ├── STYLE-GUARD-UA.md                         # Украинский стилистический гайд (Дядя Толя)
│           ├── split_chapters.py                         # Скрипт нарезки монолитов на главы
│           ├── validate_books.py                         # Комплексный верификатор целостности
│           │
│           ├── ru-edition/                               # [Оригинал: Валера, постсоветский контур L1-L5]
│           │   ├── ru/                                   # Канонический монолит v25.2, chapters/, index.md
│           │   ├── en/                                   # Перевод RU оригинала на английский язык
│           │   └── ua/                                   # Перевод RU оригинала на украинский язык
│           │
│           ├── en-edition/                               # [Оригинал: Bob the Gray, Anglo-Saxon US/UK L1-L5]
│           │   ├── en/                                   # Канонический монолит v2.4, chapters/, index.md
│           │   ├── ru/                                   # Перевод EN оригинала на русский язык
│           │   └── ua/                                   # Перевод EN оригинала на украинский язык
│           │
│           └── ua-edition/                               # [Оригинал: Дядя Толя, украинский контур во время войны]
│               ├── ua/                                   # Канонический монолит v1.9, chapters/, index.md
│               ├── ru/                                   # Перевод UA оригинала на русский язык
│               └── en/                                   # Перевод UA оригинала на английский язык
└── specs/
    ├── 001-daddys-boomer-mommys-sasuke-kun/              # Спецификация монографий и матрицы переводов
    └── 002-publishing-pipeline-and-platform/             # Спецификация веб-ридера, KDP, Typst и ZTA Kit
```

---

### Print Rendering & Pre-Flight Architecture

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                    TWO-STAGE PDF/X-1A COMPILATION PIPELINE                  │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. [TYPST ENGINE] (templates/book-paperback-6x9.typ)                        │
│    • Dynamic Gutter curve (0.500" -> 1.000" based on page count)            │
│    • DeviceGray 100% K text & vector lines, zero Rich Black                 │
│    • Recto chapter openings + enforced blank terminal verso for KDP barcode │
│    • Monospace ASCII width constraint <= 68 chars, repeating table headers  │
│    ──► Output: dist/raw-monograph.pdf (PDF 1.7 / PDF/A-2b)                  │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. [TRANSCODER STAGE] (scripts/transcode-pdfx1a.sh via Ghostscript / cpdf)  │
│    • Inject ISO 15930-1 OutputIntent (FOGRA39 / US Web Coated SWOP v2)      │
│    • Color space normalization & flattening of transparency layers          │
│    ──► Output: dist/sanitary-engineering-of-being-paperback-pdfx1a.pdf      │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. [PRE-FLIGHT VALIDATION GATE] (scripts/validate-print-pdf.sh)             │
│    • veraPDF ISO 15930-1 conformance verification                           │
│    • pdftops operator audit: strictly 0 setrgbcolor / DeviceRGB in interior │
│    • pdffonts: 100% embedded subset validation                              │
│    • pdfimages -list: 0 raster assets < 300 DPI, 0 RGB objects in interior  │
│    • pdfinfo: MediaBox, TrimBox, BleedBox exact dimensions verification     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 4. [MULTI-VENDOR COVER GENERATOR] (scripts/generate-covers.py)              │
│    • KDP: pages * 0.002252" (white) / 0.0025" (cream), min 79 pp spine text │
│    • Ingram: pages / PPI (474 white / 454 cream), 48 pp spine text          │
│    • Lulu: caliper bulk formula, barcode clearance >= 0.25" from spine fold │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Complexity Tracking

*Нет нарушений конституции. Архитектура предельно упрощена за счет удаления самописного DRM-бэкенда и перехода на статические артефакты (SSG + Pandoc + Typst).*
