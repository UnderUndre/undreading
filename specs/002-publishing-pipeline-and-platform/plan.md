# Implementation Plan: 002-publishing-pipeline-and-platform — Web Reader & Publishing Platform

**Feature Branch**: `002-publishing-pipeline-and-platform`  
**Date**: 2026-10-11  
**Spec**: [`spec.md`](spec.md)

---

## Technical Context

**Frontend / Reader**: VitePress 1.x (Node.js 20+, TypeScript), Markdown SSG, Service Worker PWA  
**Print Pipeline**: Typst CLI (0.11+), Ghostscript (standalone CLI), cpdf (standalone CLI), veraPDF, Pandoc 3.1+  
**Storage & Distribution**: Cloudflare Pages (статический хостинг), Cloudflare R2 (приватный S3-бакет под артефакты), Paddle MoR (платежи)  
**Print-on-Demand APIs**: Amazon KDP Print, Lulu Print API v2 (вебхуки)  
**Security & Tax Compliance**: NACE 62.01 («Computer programming, consultancy and related activities»), 1% налог IT микробизнеса, 0% W-8BEN withholding  

---

## Constitution Check (Constitution v1.7.0)

| Принцип Конституции | Статус | Обоснование и Инженерный Затвор |
| :--- | :---: | :--- |
| **I. Source of Truth Discipline** | **PASS** | Мастер-исходники книг лежат в `books/.../release/`, веб-страницы генерируются статически на этапе сборки. |
| **II. Transformer, Not Fork** | **PASS** | Никаких ручных форков контента: сборка сайтов и e-книг автоматизирована через единый конвейер `scripts/build.py`. |
| **III. Protected Slots** | **PASS** | Кастомные конфигурации тем и стилей изолированы в `templates/`. |
| **IV. SemVer Discipline** | **PASS** | Версионирование артефактов следует SemVer (v25.2 release, v2.4, v1.9). |
| **V. Token Economy** | **PASS** | Чтение книги в вебе не использует live LLM API: 100% текста пре-рендерено статически (0 токенов на чтение). |
| **VI. Cross-AI Review Gate** | **PASS** | `/speckit.implement` блокируется до получения вердиктов `analyze.md` PASS + $\ge 2$ независимых внешних ревьюеров per Principle VI. |
| **VII. Artifact Versioning** | **PASS** | Каждый этап фиксируется через `snapshot-stage` тегами вида `platform-launch/002/v1`. Никаких `.history/` папок. |
| **VII-B. Business Plan Stage** | **PASS** | Полное соответствие `undreading-business-plan.md` v2.0: Supporter Kit $12.99 PWYW, KDP Paperback $24.99, NACE 62.01, маржа $>88\%$. |
| **VIII. Self-Maintaining Knowledge** | **PASS** | Извлеченные паттерны верстки Typst и калибровки полей фиксируются в `templates/`. |
| **IX. Two-Phase Review Flow** | **PASS** | Планирование ведется в выделенной ветке `002-publishing-pipeline-and-platform` до слияния. |
| **X. Zero-Downtime Data Architecture** | **PASS** | Проект представляет собой статический SSG без реляционной базы данных; отдача через Cloudflare CDN с нулевым downtime. |
| **XI. Spike Governance & Prototype Code** | **PASS** | Все сборочные скрипты пишутся как чистовые production-инструменты в `scripts/` с типизацией и обработкой ошибок. |

---

## Supply Chain & Dependency Licensing Isolation

- **Ghostscript (AGPL-3.0)**: Используется **строго как внешний CLI-процесс** через вызов `gs` из bash-скриптов для пост-обработки PDF. Не линкуется в кодовую базу платформы и не распространяется с веб-приложением, что исключает вирусное заражение лицензией AGPL.
- **cpdf (Coherent PDF Command Line Tool)**: Вызывается исключительно как автономная утилита командной строки.
- **Typst (Apache 2.0)**: Пермиссивная опенсорсная лицензия CLI-компилятора.
- **Pandoc (GPLv2+)**: Внешняя CLI-утилита сборки, не встраиваемая в рантайм сайта.
- **VitePress (MIT)**: Пермиссивная лицензия для веб-ридера.

---

## Observability, Health Checks & Rollback Protocol

- **Cloudflare Pages Rollbacks**: В случае деградации сборки откат на предыдущий рабочий коммит выполняется через мгновенное переключение активного деплоя в панели Cloudflare Pages (instant rollback < 5 сек).
- **R2 Signed URLs Telemetry**: Мониторинг кодов ответов 403/404 на ссылки скачивания цифровых бандлов через Cloudflare Analytics.
- **Automated Health Check**: Финальный шаг пайплайна валидирует доступность всех 9 маршрутов книги со статусом 200 OK.

---

## Target Project Layout

```text
undreading/
├── docs/                                             # VitePress Web Reader source
│   ├── .vitepress/
│   │   └── config.ts                                 # i18n routing (9 editions) + theme configs
│   ├── index.md                                      # Landing page & Executive TL;DR
│   └── read/                                         # 9-edition reader routes
├── templates/
│   ├── book-paperback-6x9.typ                        # Typst POD master layout
│   ├── epub-style.css                                # Clean CSS for EPUB 3
│   └── zta-kit/                                      # Infrastructure templates bundle
│       ├── engine/                                   # Compiled ztacheck CLI binary
│       └── configs/                                  # Hardened Terraform, Docker, WireGuard configs
├── scripts/
│   ├── build.py                                      # Cross-platform build runner
│   ├── generate-covers.py                            # Multi-vendor cover geometry engine
│   ├── transcode-pdfx1a.sh                           # Ghostscript/cpdf PDF/X-1a transcoder
│   └── validate-print-pdf.sh                         # veraPDF pre-flight quality gate
├── dist/                                             # Compiled artifacts (Git-ignored)
│   ├── site/                                         # Static web reader build
│   ├── sanitary-engineering-of-being-ru.epub         # EPUB 3
│   ├── sanitary-engineering-of-being-paperback.pdf   # Typst print PDF
│   └── zta-architecture-kit-v25.2.zip               # Commercial bundle
├── Makefile                                          # Build automation
└── package.json                                      # Scripts & toolchains
```
