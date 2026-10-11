# Implementation Plan: 002-publishing-pipeline-and-platform — Web Reader & Publishing Platform

**Feature Branch**: `feature/002-publishing-pipeline-and-platform`  
**Date**: 2026-10-11  
**Spec**: [`spec.md`](spec.md)

---

## Technical Context

**Frontend / Reader**: VitePress 1.x (Node.js 20+, TypeScript), Markdown SSG, Service Worker PWA  
**Print Pipeline**: Typst CLI (0.11+), Ghostscript, cpdf, veraPDF, Pandoc 3.1+  
**Storage & Distribution**: Cloudflare Pages (статический хостинг), Cloudflare R2 (приватный S3-бакет под артефакты), Paddle MoR (платежи)  
**Print-on-Demand APIs**: Amazon KDP Print, Lulu Print API v2 (вебхуки)  
**Security & Tax Compliance**: NACE 62.01 («Computer programming, consultancy and related activities»), 1% налог IT микробизнеса, 0% W-8BEN withholding  

---

## Constitution Check

| Принцип Конституции | Статус | Обоснование |
| :--- | :--- | :--- |
| **I. Negative Selection** | **PASS** | Никакого лишнего JS-рантайма на клиенте: 100% статически пре-рендеренный HTML через SSG. |
| **II. Zero-Trust Architecture** | **PASS** | Cloudflare R2 временные подписанные ссылки исключают прямой публичный линкинг платных архивов. |
| **III. Open-Source First & Zero-DRM** | **PASS** | Веб-ридер открыт для всех читателей; коммерциализация строится на сопутствующем ZTA Architecture Kit. |
| **IV. Level 1 Factuality & Compliance** | **PASS** | Дескриптор Paddle жестко зафиксирован за NACE 62.01 для исключения рисков переквалификации налоговыми органами. |

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
