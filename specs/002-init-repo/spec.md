# Feature Specification: 002-init-repo — Undreading Astro Starlight Reader & Open Digital Publishing Platform

**Feature Branch**: `specs/002-init-repo`  
**Created**: 2026-08-18  
**Updated**: 2026-08-20 (Post-Audit Patch: Astro Starlight SSG Engine & Supporter Bundle Architecture)  
**Status**: Approved / In Execution  
**Input**: Business Plan `undreading-business-plan.md` (v2.0), Adversarial Review `gemini-flash-3.7.md`, Single Sign-On Contract (`undrlla/specs/005-sso-jwt-contract.md`), Astro + Starlight Architecture Decision.

---

## 1. Context & Architectural Overview

`undreading` — это автономное цифровое книжное веб-приложение, опенсорсная база знаний и Headless-платформа для монетизации книги **«Сантехника Бытия»** и сопутствующего **ZTA Security Architecture Kit**.

По результатам состязательного аудита `gemini-flash-3.7.md` сложный DRM-ридер на `foliate-js` демонтирован в пользу открытого статического генератора **Astro + Starlight**.

```
┌─────────────────────────────────────────────────────────────────────────────┐
1. ОТКРЫТЫЙ ВЕБ-РИДЕР (undreading.com)                                        │
│    • Движок Astro + Starlight (0ms latency, zero JS runtime overhead)       │
│    • Статически пре-генерированные локализации и ролевые переводы           │
│    • Кастомные темы (Свиток Шиноби, Терминал CRT-3000, Магический Вестник)  │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. ПОДДЕРЖКА И КОММЕРЧЕСКИЙ БАНДЛ (Paddle MoR)                              │
│    • Модель PWYW ($5.00 min / $12.99 rec / $50+ sponsor)                    │
│    • Supporter Kit: EPUB 3 + Typst Print PDF + ZTA Templates + AI Audio     │
│    • Квалификация: NACE 62.01 (ИП Грузия 1% - 0% GAAR риск)                 │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. ФИЗИЧЕСКАЯ ПЕЧАТЬ (Amazon KDP Print)                                     │
│    • Trade Paperback 6"x9" ($24.99) ➔ Payoneer US ACH                      │
│    • Исключён ценовой демпинг Amazon Price Matching (Kindle Ebook omitted)  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Ключевые Технологические Столбы

1. **Astro + Starlight SSG Web Reader:**  
   Веб-читалка строится на статической платформе **Astro + Starlight** (MIT). Текст книги хранится в открытом Маркдауне (`/src/content/docs/`). Страницы генерируются в статический HTML, обеспечивая мгновенный отклик, оффлайн-кэширование через Service Worker (`@vite-pwa/astro`) и встроенный полнотекстовый поиск `Pagefind`.
2. **Пре-генерация ролевых переводов и локализаций (Static Pre-generation):**  
   Для устранения расходов на живой LLM API ($0.80–$1.50 на пользователя), все ролевые языковые темы (*Валера-Сантехник*, *Шиноби*, *Геральт*, *Academic*) пре-генерируются скриптом на этапе CI/CD сборки и раскладываются по i18n-папкам Starlight (`/ru/`, `/en/`, `/shinobi/`, `/valera/`).
3. **Визуальные Темы Читалки (Starlight Component Overrides):**  
   Инжектируются через CSS-переменные и переопределение компонентов Starlight:
   - 📜 `Shinobi Scroll`: текстура рисовой бумаги, вертикальный/горизонтальный скролл.
   - ☢️ `Vault Terminal CRT-3000`: фосфорное зеленое свечение моноширинного шрифта, сканлайны, дугообразные искажения.
   - 🧙♂️ `Arcane Gazette`: многоколоночная газетная вёрстка (`column-count`).
4. **Единый провайдер авторизации (Undrlla IdP / Single Sign-On):**  
   Авторизация на сайте `undreading.com` для доступа к Supporter Kit, личным заметкам и закрытому клубу выполняется через **Undrlla IdP (`id.undrlla.network`)** по стандарту **Directus 12.x Native OIDC PKCE flow** с валидацией RS256 JWT через JWKS (`/.well-known/jwks.json`).
5. **Коммерческий Фиатный Контур (Paddle MoR & Supporter Kit):**  
   Продажи ведутся в модели Pay-What-You-Want ($5.00 min / $12.99 rec / $50+ sponsor). Продукт квалифицируется как *"ZTA Security Architecture Specification & Infrastructure Implementation Kit (NACE 62.01)"* (ИП Грузия 1% налог, 0% GAAR риск по ст. 73.9).
6. **Физическая печать Amazon KDP Print:**  
   На Амазоне продаётся **только печатная версия (Trade Paperback 6"x9" за $24.99)**. Версия Kindle Ebook исключена для предотвращения принудительного демпинга цен (Price Matching) ботами Amazon до $0.00.

---

## 3. User Scenarios & Testing

### User Story 1 — Instant Open Reading on Astro Starlight (Priority: P1)

As a reader visiting `undreading.com`,  
I want to instantly read the book manifesto in my browser without login or paywalls,  
So that I get immediate value and friction-free user experience.

**Acceptance Scenarios**:

1. **Given** any visitor opening `undreading.com/chapters/ch01`, **When** the page loads, **Then** static HTML is delivered in < 200ms with 0 Token/API costs.
2. **Given** a reader switching theme to "Vault CRT-3000", **When** toggled in UI, **Then** CSS variables and scanline overlays apply instantly without reloading the page.
3. **Given** a reader offline in airplane mode, **When** they navigate previously loaded chapters, **Then** Service Worker PWA cache serves content from IndexedDB/CacheStorage seamlessly.

---

### User Story 2 — Purchase Supporter & Architecture Kit via Paddle (Priority: P1)

As a technical supporter on `undreading.com`,  
I want to purchase the Supporter Kit ($5–$50 PWYW) via Paddle MoR,  
So that I get downloadable EPUB/PDF, ZTA Terraform/Docker templates, AI Audio, and Telegram Club access.

**Acceptance Scenarios**:

1. **Given** a user clicking "Supporter Kit ($12.99)", **When** the Paddle Overlay completes checkout, **Then** a webhook hits `/api/webhooks/paddle`, grants `BookEntitlement` for user `sub` ID, and unlocks digital downloads.

---

## 4. Functional Requirements

- **FR-001 (Astro Starlight Core)**: Web Reader MUST be built on **Astro + Starlight** (MIT), compiling Markdown chapters into static HTML with Pagefind search.
- **FR-002 (Static Pre-generated i18n)**: All persona translations (Valera, Shinobi, Geralt) MUST be pre-compiled during CI/CD build into Starlight i18n routing folders.
- **FR-003 (Undrlla Identity & SSO)**: System MUST authenticate users via **Undrlla IdP (`https://id.undrlla.network`)** using Directus OIDC PKCE flow and validate RS256 JWT access tokens against public JWKS (`/.well-known/jwks.json`).
- **FR-004 (Supporter Kit Pricing & PWYW)**: Product MUST be sold under Pay-What-You-Want model ($5 min / $12.99 rec) via Paddle Merchant of Record under NACE 62.01 ("ZTA Implementation Kit").
- **FR-005 (Amazon KDP Print Exclusive)**: Amazon distribution MUST be restricted to **Paperback Print-on-Demand ($24.99)** via KDP Print. Standard Kindle Ebook MUST NOT be listed to avoid Price Matching to $0.00.
- **FR-006 (PWA Offline Reading)**: System MUST integrate `@vite-pwa/astro` for offline reading support.

---

## 5. Success Criteria

- **SC-001**: Static page load for any chapter completes in < 200ms globally via Cloudflare CDN.
- **SC-002**: 0% LLM API token leakage during user reading sessions (all translation assets served statically).
- **SC-003**: 100% compliance with Georgian NACE 62.01 1% tax rate (0% GAAR risk).
