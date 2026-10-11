# Feature Specification: 002-publishing-pipeline-and-platform — Undreading Web Reader, Publishing Pipeline & ZTA Kit Platform

**Feature Branch**: `feature/002-publishing-pipeline-and-platform`  
**Created**: 2026-10-11  
**Status**: Approved (Executable Spec)  
**Input**: Business Plans (`undreading-business-plan.md` v2.3, `undrlla-business-plan.md` v15.1, `undreseller-business-plan.md` v18.0), Feature Spec `001-daddys-boomer-mommys-sasuke-kun` (v25.2 Release & 9-Edition Matrix)

---

## 📖 1. Context & Architectural Overview

`undreading` (`undreading.com`) — открытая цифровая издательская платформа, веб-читалка и инфраструктурный хаб монетизации для фундаментальной монографии **«Сантехника Бытия»** и сопутствующего софтверного пакета **ZTA Security Architecture Kit**.

Данная спецификация консолидирует все платформенные, веб- и сборочно-издательские задачи, вынесенные из базовой книжной фичи 001.

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. ОТКРЫТЫЙ МУЛЬТИЯЗЫЧНЫЙ ВЕБ-РИДЕР (undreading.com)                        │
│    • Движок VitePress 1.x / Astro SSG (0ms server latency, 0 token cost)    │
│    • Доступ ко всем 9 изданиям библиотеки (3 оригинала + 6 переводов)        │
│    • Интерактивная матрица 110 задвижек P0 с плавным скроллом и поиском     │
│    • Визуальные темы: «Свиток Шиноби», «Терминал Убежища CRT-3000»          │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. МУЛЬТИ-ВЕНДОРНЫЙ ПЕЧАТНЫЙ КОНВЕЙЕР (Amazon KDP + Lulu + Ingram)          │
│    • Мастер-верстка Typst под 6"x9" Trade Paperback (Gutter 0.875", K-only) │
│    • Двухстадийный конвейер PDF/X-1a:2001 (Ghostscript / cpdf / veraPDF)    │
│    • Генератор обложек и корешков `generate-covers.py` (KDP/Ingram/Lulu)    │
│    • Автоматический дропшиппинг через Lulu Print API ($24.99, маржа 64.2%)  │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. КОММЕРЧЕСКИЙ SUPPORTER & ZTA ARCHITECTURE KIT (Paddle MoR)               │
│    • Модель PWYW ($5.00 min / $12.99 rec / $50+ sponsor)                    │
│    • Содержимое: EPUB 3 + Typst Print PDF + ZTA Terraform/Docker шаблоны    │
│    • Квалификация: NACE 62.01 (1% ставка налога в Армении/Грузии, 0% GAAR)  │
│    • Защищенная раздача через Cloudflare R2 временные подписанные ссылки    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🎯 2. Prioritized User Stories

### User Story 1 — Instant 9-Edition Web Reader & P0 Matrix (Priority: P1)
Посетитель переходит на `undreading.com/read`, выбирает любое из 9 изданий библиотеки:
- **RU-Edition**: RU оригинал (Валера), EN перевод, UA перевод;
- **EN-Edition**: EN оригинал (Bob the Gray), RU перевод, UA перевод;
- **UA-Edition**: UA оригинал (Дядя Толя), RU перевод, EN перевод.
Читатель мгновенно читает полный текст, пользуется поиском и кликает на любую из 110 задвижек P0 для мгновенного перехода к разделу.

### User Story 2 — EPUB 3 & Multi-Vendor Print Production (Priority: P2)
Читатель покупает бумажную книгу на Amazon KDP или через DTC-печать на Lulu, либо скачивает оффлайн EPUB 3:
- Автоматизированная генерация EPUB 3 через Pandoc со стилем `templates/epub-style.css`;
- Вёрстка Typst 6"x9" с автоматическим спуском полос и пустой страницей Verso под штрихкод Amazon;
- Транскодирование в PDF/X-1a:2001 и валидация через `veraPDF` (ISO 15930-1).

### User Story 3 — Commercial Supporter Bundle & ZTA Kit Checkout (Priority: P3)
Читатель на `/buy` приобретает *Supporter & ZTA Architecture Kit* ($12.99 PWYW) через Paddle MoR:
- Автоматическая валидация вебхука Paddle;
- Генерация 24-часовых Cloudflare R2 Signed URLs;
- Скачивание zip-архива с hardened конфигурациями (Terraform, Docker Compose, Traefik v3, WireGuard) под NACE 62.01.

### User Story 4 — Ecosystem Business Plans Sync (Priority: P4)
Синхронизация бизнес-моделей ресейл-маркетплейса `undreseller` и экосистемы `undrlla` с выпущенными релизами монографии.
