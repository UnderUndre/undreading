# Implementation Plan: 001-daddys-boomer-mommys-sasuke-kun — «Сантехника Бытия»

**Branch**: `001-init` | **Date**: 2026-09-27 | **Spec**: [`spec.md`](spec.md)  
**Input**: Feature specification from `specs/001-daddys-boomer-mommys-sasuke-kun/spec.md`, Business Plan `undreading-business-plan.md` (v2.0), `undrlla-business-plan.md` (v15.1), `undreseller-business-plan.md` (v18.0)

---

## Summary

Монография «Сантехника Бытия» (Daddy's Boomer Mommy's Sasuke-kun) представляет собой открытую цифровую книгу-манифест и прикладную ZTA-инструкцию для человека (System Prompt for Humans). Проект реализует открытую дистрибуцию через статический веб-ридер (VitePress/Astro), физическую печать через Amazon KDP Print (Paperback 6"x9" PoD) и коммерческую продажу сопутствующего софтверного комплекта **ZTA Security Architecture Kit (NACE 62.01)** по модели Pay-What-You-Want ($12.99) через Paddle Merchant of Record.

---

## Technical Context

**Language/Version**: Markdown (CommonMark/GFM), Typst (0.11+), HTML/CSS/TypeScript (Node.js 20+, VitePress / Astro Starlight), Bash/Makefile  
**Primary Dependencies**: Pandoc 3.1+, Typst CLI, VitePress/Astro, epubcheck, pdfinfo, zip  
**Storage**: Static files (Markdown `.md`, Typst `.typ`, `.epub`, `.pdf`), Git-версионирование 3-2-1-1-0, Cloudflare CDN / GitHub Pages  
**Testing/Validation**: Markdownlint, epubcheck, pdfinfo, internal zero-trust fact-checking audit Level 1/2  
**Target Platform**: Web (undreading.com), E-readers (EPUB 3), Physical Print (Amazon KDP Paperback 6"x9"), GitHub Releases  
**Project Type**: Open-Source Digital Publishing & Infrastructure Architecture Kit Platform  
**Performance Goals**: 0 ms server latency (100% pre-rendered SSG on Cloudflare CDN), <2s сборка Typst PDF, <5s генерация EPUB через Pandoc  
**Constraints**: 0% DRM, 0 token cost per read (pre-generated static translations), 100% NACE 62.01 compliance в Paddle MoR для сохранения 1% ставки налога в Грузии/Армении  
**Scale/Scope**: 1 мастер-том монографии (12 глав, 11 частей, 5 приложений, 70 P0-задвижек, 220+ концептов, $\ge 120\,000$ слов, 4300+ строк), 3 формата дистрибуции (Web, EPUB, PDF), 1 ZTA Architecture Kit архив

---

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Принцип Конституции | Статус | Обоснование и Инженерный Затвор |
| :--- | :--- | :--- |
| **I. Negative Selection (Вычитание шума)** | **PASS** | Монография не содержит абстрактного инфобизнеса; все рекомендации строго выведены из физических, липидологических и юридических пределов. |
| **II. Zero-Trust & Level 1/2 Factuality** | **PASS** | Все дозировки (Аспирин 300 мг, Адреналин 0.3 мг, CWI), формулы (TCO, Little's Law, HOMA-IR) и статьи законов (IRC §864, 127-ФЗ, CP Испании) верифицированы. |
| **III. Strict Authorship Demarcation** | **PASS** | Личный опыт Undre N=1 изолирован в Прологе; внешняя доказательная база синтезирована от лица системного сантехника Валеры. |
| **IV. Open-Source First & Zero-DRM** | **PASS** | Отказ от проприетарного DRM в пользу открытого текста на VitePress/GitHub. Коммерциализация через Supporter Kit (NACE 62.01). |
| **V. Immutable Versioning** | **PASS** | Каждая версия фиксируется как неизменяемый файл `daddys-boomer-mommys-sasuke-kun-v<N>.md`. Старые версии не затираются. |

---

## Project Structure

### Documentation (this feature)

```text
specs/001-daddys-boomer-mommys-sasuke-kun/
├── spec.md              # Feature specification & Clarifications log
├── plan.md              # This file (Implementation Plan)
├── research.md          # Phase 0 Decision Records (Publishing, Pricing, Legal)
├── data-model.md        # Phase 1 Data Model & Schemas (Entities, Directives, SKUs)
├── quickstart.md        # Phase 1 Build & Release Pipeline Runbook
└── tasks.md             # Phase 2 Task Breakdown by Agents & Parallel Lanes
```

### Source Code & Monograph Layout (`repos/undreading`)

```text
undreading/
├── books/
│   └── 001-daddys-boomer-mommys-sasuke-kun/
│       ├── daddys-boomer-mommys-sasuke-kun-v17.5.md  # Master text (Current v17.5)
│       └── daddys-boomer-mommys-sasuke-kun-v18.0.md  # Target release volume
├── docs/                                             # VitePress / Astro Web Reader source
│   ├── .vitepress/
│   │   └── config.ts                                 # Site navigation & theme config
│   ├── index.md                                      # Landing page & Executive TL;DR
│   └── chapters/                                     # Web-reader chapters
├── templates/
│   ├── book-paperback-6x9.typ                        # Typst Print-on-Demand layout
│   ├── epub-style.css                                # Clean CSS for EPUB 3
│   └── zta-kit/                                      # Infrastructure templates bundle
├── assets/
│   ├── cover-paperback.pdf                           # Full wrap cover (6"x9" + spine)
│   ├── cover-ebook.jpg                               # Digital cover art
│   └── fonts/                                        # Licensed open typography
├── dist/                                             # Compiled artifacts (Git-ignored)
│   ├── site/                                         # Static website build
│   ├── sanitary-engineering-of-being.epub            # EPUB 3 release
│   ├── sanitary-engineering-of-being-paperback.pdf   # Typst print PDF
│   └── zta-architecture-kit-v18.0.zip               # Supporter Kit bundle
├── Makefile                                          # Build automation
└── package.json                                      # Node.js tooling & scripts
```

---

## Complexity Tracking

*Нет нарушений конституции. Архитектура предельно упрощена за счет удаления самописного DRM-бэкенда и перехода на статические артефакты (SSG + Pandoc + Typst).*
