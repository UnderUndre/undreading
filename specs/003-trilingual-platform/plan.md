# Implementation Plan: Undreading Trilingual Open Publishing Platform & Store

**Branch**: `003-trilingual-platform` | **Date**: 2026-10-05 | **Spec**: [`spec.md`](spec.md)  
**Input**: Feature specification from `specs/003-trilingual-platform/spec.md`

---

## Summary

Разработка и развертывание трилингвальной издательской платформы **Undreading** (`undreading.com`):
1. Быстрый и открытый Web Reader на трех языках (RU v25.0, EN v2.2, UA v1.7) с интерактивной сеткой из 86 задвижек матрицы P0.
2. Цифровой чекаут *Supporter & ZTA Architecture Kit* (PWYW $5 min / $12.99 rec) через Paddle MoR с авто-выдачей EPUB/PDF/ZTA файлов.
3. Автоматизированный DTC конвейер печати русского издания через связку Paddle Webhook $\to$ **Lulu Print API**.
4. Нативные ссылки на Amazon Prime для англо- и украиноязычных печатных версий.

---

## Technical Context

**Language/Version**: TypeScript 5.x, Node.js 22 LTS  
**Static Site Generator**: VitePress 1.x / Astro SSG + Tailwind CSS  
**Client Storage**: IndexedDB (idb-keyval) + PWA Workbox Service Worker  
**E-Commerce**: Paddle Billing API (Merchant of Record), Lulu Print API v4 (OAuth2 Client Credentials)  
**Storage & File Delivery**: Cloudflare R2 Bucket (зашифрованные EPUB/PDF/ZIP ассеты) с подписанными URL (Signed URLs)  
**Hosting**: Cloudflare Pages (Edge SSG + Cloudflare Functions for Webhooks)  
**Performance Targets**: TTFB $< 50\text{ ms}$, Lighthouse Performance $= 100$, zero third-party tracking scripts  

---

## Project Structure & Architecture

```text
undreading/
├── docs/                              # VitePress / SSG content root
│   ├── .vitepress/
│   │   ├── config.mts                 # Trilingual navigation & i18n routing (ru/en/ua)
│   │   └── theme/
│   │       ├── Layout.vue             # Custom layout with P0 valve overlay & audio epigraphs
│   │       ├── P0MatrixWidget.vue     # Interactive 86-valve matrix with instant jumps
│   │       └── style.css              # Typography & dark/sepia/light palette
│   ├── ru/                            # Russian Edition (symlink or build from v25.0.md)
│   ├── en/                            # English Edition (from en-v2.2.md)
│   ├── ua/                            # Ukrainian Edition (from ua-v1.7.md)
│   ├── buy.md                         # Digital Supporter & ZTA Kit Checkout (Paddle)
│   └── print.md                       # Physical Book Ordering (Lulu API + Amazon KDP)
├── functions/                         # Cloudflare Pages Serverless Functions
│   └── api/
│       ├── webhooks/
│       │   └── paddle.ts              # Paddle webhook: transaction.completed ➔ Lulu Print API
│       └── shipping/
│           └── calculate.ts           # Lulu API shipping cost calculator
├── scripts/
│   ├── build-typst-pdf.sh             # Compiles Typst 6"x9" PDFs for KDP & Lulu
│   ├── build-epub.sh                  # Compiles EPUB 3 files via Pandoc
│   └── sync-release-to-docs.py        # Automated sync of release/*.md into VitePress routes
└── package.json
```

---

## Phase 1: Data Model & Integration Contracts

### 1. Paddle Webhook Payload Contract (`/api/webhooks/paddle`)
* **Event**: `transaction.completed`
* **Custom Data**: `customer_email`, `product_type` (`DIGITAL_ZTA_BUNDLE` | `RU_PRINT_PAPERBACK`), `shipping_address` (name, street, city, state, postal_code, country_code, phone).
* **Action for `DIGITAL_ZTA_BUNDLE`**: Генерирует 24-часовой signed download URL из Cloudflare R2 и отправляет письмо покупателю через Postmark / Resend.
* **Action for `RU_PRINT_PAPERBACK`**: Авторизуется в Lulu API (`https://api.lulu.com/auth/realms/glasstree/protocol/openid-connect/token`), отправляет `POST /print-jobs/` с параметрами заказа:
  ```json
  {
    "contact_email": "customer@example.com",
    "external_id": "undreading-tx-12345",
    "line_items": [
      {
        "printable_normalization": {
          "cover": { "source_url": "https://r2.undreading.com/assets/cover_ru_lulu.pdf" },
          "interior": { "source_url": "https://r2.undreading.com/assets/interior_ru_lulu.pdf" },
          "pod_package_id": "0600X0900BWSTDPB060UW444GXX"
        },
        "quantity": 1,
        "title": "Sanitary Engineering of Being (RU)"
      }
    ],
    "shipping_address": { ... },
    "shipping_level": "MAIL"
  }
  ```

---

## Phase 2: Implementation Sequence

1. **Step 1:** Настроить конфигурацию VitePress `docs/.vitepress/config.mts` со структурой локализации на 3 языка (`/ru/`, `/en/`, `/ua/`).
2. **Step 2:** Разработать скрипт `sync-release-to-docs.py`, автоматически нарезающий релизные монографии `release/*.md` на главы с правильными якорями.
3. **Step 3:** Разработать интерактивный Vue-компонент `P0MatrixWidget.vue` с мгновенным поиском и фильтрацией 86 задвижек.
4. **Step 4:** Сверстать страницу `/buy` с интеграцией оверлея `Paddle.js` (модель PWYW $5 / $12.99 / $50).
5. **Step 5:** Сверстать страницу `/print` с формой расчета стоимости доставки через Cloudflare Function `functions/api/shipping/calculate.ts` (Lulu API).
6. **Step 6:** Разработать Cloudflare Function `functions/api/webhooks/paddle.ts` для автоматического создания печатных заказов в Lulu Print API.
7. **Step 7:** Настроить PWA Workbox Service Worker для оффлайн-кэширования прочитанных глав.
8. **Step 8:** Провести сквозное тестирование и валидацию сборки (`npm run build:docs`).
