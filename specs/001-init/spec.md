# Feature Specification: 001-init — Undreading Web Reader & Headless Digital Publishing Platform

**Feature Branch**: `specs/001-init`  
**Created**: 2026-08-18  
**Status**: Draft / Approved  
**Input**: Business Plan `undreading-business-plan.md`, `plan-updates.md`, `research.md`, Web Reader App Architecture (foliate-js fork), AI Translation Pipeline (UndeRoute/OmniRoute), Persona Themes Engine, Single Sign-On Contract (`undrlla/specs/005-sso-jwt-contract.md`).

---

## 1. Context & Architectural Overview

`undreading` — это автономное цифровое книжное веб-приложение и Headless-платформа для монетизации и чтения книги **«Сантехника Бытия»** (и дальнейших изданий экосистемы `Undrlla`).

### Ключевые технологические столбы:
1. **Единый провайдер авторизации (Undrlla IdP / Single Sign-On):**  
   Пользователи авторизуются в веб-приложении `undreading.com` через центральный паспортный стол **Undrlla IdP (`id.undrlla.network`)**. Аутентификация выполняется по стандарту **Directus 12.x Native OIDC PKCE flow**. Выданный асимметричный **RS256 JWT-токен** валидируется клиентом и бэкендом читалки без лишних запросов к IdP — через публичный эндпоинт **JWKS** (`/.well-known/jwks.json`) в соответствии со спецификацией `undrlla/specs/005-sso-jwt-contract.md`.
2. **Headless Backend Architecture via `undreseller`:**  
   Вся бэкенд-логика (PostgreSQL Supabase DB, вебхуки Paddle MoR, пейвол-отгрузка глав, хранение `BookEntitlements`, логирование и ИИ-перевод) делегирована единому бэкенд-конвейеру **`undreseller`** (`demo.undreseller.com` / `api.undreseller.com`), обеспечивая 100% dogfooding агентского стека. `undreading` выступает изолированным легковесным Storefront & Web Reader приложением.
3. **Коммерческий Фиатный Контур (Paddle MoR):**  
   Продажа электронной книги (PDF/EPUB Bundle) по единому ценнику **$12.99 USD** через Paddle (Merchant of Record) с обработкой вебхуков на бэкенде `undreseller` и уплатой 1% налога ИП Грузии (NACE 62.01).
4. **Глобальная Органика (Amazon KDP + Payoneer ACH):**  
   Публикация версии для Kindle ($12.99) строго в **Open KDP** (без KDP Select эксклюзивности). Выплаты производятся на Payoneer US Checking Account с 0% withholding tax в США по форме W-8BEN (договор 1973 г.).
5. **Защищённый Веб-Ридер (Foliate-js Fork / MIT):**  
   Поглавная отгрузка через API Gateway `undreseller` с цифровыми водяными знаками (Digital Watermarking), офлайн-кэшированием в IndexedDB через Service Worker и защитой от скачивания файла целиком.
6. **ИИ-Переводчик (UndeRoute / OmniRoute Integration via `undreseller`):**  
   Потоковый перевод глав через `undreseller` (проксирующий во встроенный `UndeRoute` `/v1/chat/completions`) с сохранением HTML-структуры, глоссарием сущностей и ролевыми режимами перевода (Наруто, Геральт, Валера).

---

## 2. User Scenarios & Testing

### User Story 1 — Seamless SSO Login via Undrlla IdP (Priority: P1)
As a reader visiting `undreading.com`,  
I want to log in using my central Undrlla Citizen account (`id.undrlla.network`),  
So that I don't have to register a separate account or manage new credentials.

**Acceptance Scenarios**:
1. **Given** an unauthenticated reader clicking "Login" on `undreading.com`, **When** the OIDC PKCE flow triggers, **Then** the browser is redirected to `https://id.undrlla.network/oauth/authorize`.
2. **Given** successful authentication on Undrlla IdP, **When** redirected back to `undreading.com/api/auth/callback`, **Then** the backend exchanges the auth code for a signed RS256 JWT, sets an `HttpOnly` `__Secure-undrlla-session` cookie on `.undrlla.network` (or local domain token), and unlocks the Web Reader.
3. **Given** an inbound request to `/api/books/[id]/chunk`, **When** the backend verifies the JWT signature against `https://id.undrlla.network/.well-known/jwks.json`, **Then** the request is authorized locally without making a network roundtrip to the IdP server for every request.

---

### User Story 2 — Book Purchase & Entitlement (Priority: P1)
As a customer on `undreading.com`,  
I want to purchase the digital book bundle for **$12.99 USD** via Paddle MoR,  
So that I instantly gain access to the web reader, downloadable PDF/EPUB, and 1 month of Telegram Citizen Club.

**Acceptance Scenarios**:
1. **Given** a customer clicking "Buy Book ($12.99)", **When** the Paddle Checkout overlay completes, **Then** a secure webhook hits `/api/webhooks/paddle`, records the entitlement in Postgres, and links it to the user's Undrlla `sub` ID.
2. **Given** an authorized user who purchased the book, **When** they open `/reader/sanitary-engineering-of-being`, **Then** the reader streams book chapters with dynamic watermarks containing their transaction ID and email.

---

## 3. Requirements

### Functional Requirements

- **FR-001 (Undrlla Identity & SSO)**: System MUST authenticate users exclusively via **Undrlla IdP (`https://id.undrlla.network`)** using native Directus OIDC PKCE flow and validate RS256 JWT access tokens against the public JWKS endpoint (`/.well-known/jwks.json`) per `undrlla/specs/005-sso-jwt-contract.md`.
- **FR-002 (Ebook Fixed Pricing)**: The retail price for the Ebook (PDF/EPUB bundle on `undreading.com` and Kindle Edition on Amazon KDP) MUST be fixed at **$12.99 USD**.
- **FR-003 (Paddle MoR Integration)**: System MUST process direct fiat sales via Paddle Merchant of Record, routing payouts SWIFT to Georgia IE 1% (NACE 62.01) or Payoneer.
- **FR-004 (Amazon Open KDP Compliance)**: Book MUST be published under Open KDP (non-exclusive) to preserve concurrent direct sales on `undreading.com`. KDP payouts MUST route to Payoneer US Checking Account with 0% US withholding tax via Form W-8BEN (US-USSR Treaty 1973).
- **FR-005 (Web Reader Engine)**: Web Reader MUST be built on a fork of `foliate-js` (MIT) / `react-reader` (MIT/BSD). Chapter content MUST be served chapter-by-chapter via an API gateway behind entitlement verification (`HasUserPurchased`).
- **FR-006 (Digital Watermarking)**: Server MUST inject dynamic digital watermarks (hidden Unicode sequences, opacity micro-tags with buyer transaction ID and e-mail) into chapter HTML prior to rendering.
- **FR-007 (IndexedDB Offline Cache)**: Reader Service Worker MUST cache paid chapters into browser IndexedDB using `crypto.subtle` AES encryption for offline PWA reading.
- **FR-008 (AI Translation Pipeline)**: System MUST integrate with UndeRoute / OmniRoute API (`/v1/chat/completions`) for AST-aware chapter translation, entity glossary preservation, and role-based translation modes (`Accurate`, `Naruto`, `Geralt`, `Valera`).
- **FR-009 (Persona Themes Engine)**: Reader MUST support custom CSS/WebGL themes injected into Shadow DOM: `Default Clean`, `Shinobi Scroll` (parchment, scroll snap), `Arcane Gazette` (newspaper columns, WebM loops), and `Vault Terminal CRT-3000` (phosphor text glow, scanlines, barrel distortion).
- **FR-010 (IP & Trademark Safety)**: Theme names, UI labels, and assets MUST use generic/parody branding (`Shinobi Scroll`, `Arcane Gazette`, `Vault CRT-3000`) and custom SVG icons to avoid trademark infringement.

---

## 4. Key Entities

- **BookEntitlement**: User book access record (`id`, `user_sub` (from Undrlla JWT), `book_id`, `purchased_at`, `channel` (paddle|kdp|crypto), `transaction_id`, `status`).
- **ChapterChunk**: Server-side chapter payload (`book_id`, `chapter_index`, `title`, `xhtml_content`, `watermark_hash`).
- **UserReaderState**: Reader progress sync (`user_sub`, `book_id`, `current_cfi`, `selected_theme`, `selected_language`, `persona_id`, `updated_at`).

---

## 5. Success Criteria

- **SC-001**: User login via `id.undrlla.network` completes and issues a valid RS256 JWT in < 3 seconds.
- **SC-002**: 100% of `/api/books/[id]/chunk` requests validate the RS256 JWT via local JWKS verification without making outgoing HTTP auth calls to IdP.
- **SC-003**: Reader streams requested chapters in < 500ms while injecting dynamic watermarks.
- **SC-004**: Offline reading mode functions seamlessly in PWA via IndexedDB cache when internet connection is disabled.
