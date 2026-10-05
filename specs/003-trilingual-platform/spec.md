# Feature Specification: Undreading Trilingual Open Publishing Platform & Store

**Feature Branch**: `003-trilingual-platform`  
**Created**: 2026-10-05  
**Status**: Approved (Executable Spec)  
**Input**: Business Plan `undreading-business-plan.md` v2.3 & Trilingual Release Artifacts (RU v25.0, EN v2.2, UA v1.7, 86-Valve P0 Matrix, Paddle MoR, Lulu Print API)

---

## 📖 Executive Summary & Core Concept

**Undreading** (`undreading.com`) — открытая международная издательская платформа и флагманский лидогенератор доверия суверенной инженерной экосистемы.
Платформа решает две ключевые задачи:
1. **100% открытое и бесплатное чтение онлайн** фундаментальной монографии *«Сантехника бытия: Архитектура суверенитета, телеметрии и выживания в эпоху цифрового хаоса»* на трех языках (RU, EN, UK) через статический веб-ридер с мгновенным переключением 86 задвижек матрицы P0.
2. **Коммерческий процессинг и дистрибьюция**:
   - Покупка *Supporter & ZTA Architecture Kit* (PWYW $5 min / $12.99 rec) через Paddle MoR с мгновенной отдачей EPUB 3, Typst PDF и ZTA-шаблонов под льготный налог 1% IT в Армении (NACE 62.01).
   - Direct-to-Consumer (DTC) печать бумажной версии на русском языке ($24.99) через вебхук в **Lulu Print API** (дропшиппинг по всему миру с чистой маржой 64.2% / $16.04).
   - Прямые ссылки на Amazon Prime для англо- и украиноязычных печатных изданий.

## 📌 Clarifications

### Session 2026-10-05
- **Q:** Какой движок использовать для статического веб-ридера? → **A:** **VitePress 1.x SSG** с нативным i18n (`/ru/`, `/en/`, `/ua/`), встроенным локальным поиском и развертыванием на Cloudflare Pages (0ms задержка, 0 токенов).
- **Q:** Как организовать защищенное хранение и выдачу платных файлов книги и ZTA-шаблонов? → **A:** **Cloudflare R2 приватный S3-бакет** с генерацией 24-часовых временных подписанных ссылок (Signed URLs) через Cloudflare Serverless Function после подтверждения оплаты Paddle.

---

## 🎯 User Scenarios & Testing (Prioritized User Stories)

### User Story 1 - Instant Trilingual Web Reader & P0 Matrix Jump (Priority: P1)

Посетитель переходит на `undreading.com/read`, выбирает язык (RU / EN / UA), мгновенно читает полный текст книги без блокировок и регистрации, ищет термины через `Ctrl+F` или кликает на любую из 86 задвижек в P0-матрице для быстрого перехода к соответствующему разделу.

**Why this priority**: Фундаментальный уровень бесплатного лид-магнита: открытость и удобство чтения формируют 100% доверие к экспертизе автора и питают B2B-воронку.

**Independent Test**: Доступен на `GET /read/ru`, `/read/en`, `/read/ua`. Все 86 задвижек [P0-01]–[P0-86] кликабельны и скроллят страницу к соответствующему якорю.

**Acceptance Scenarios**:
1. **Given** читатель на `undreading.com/read/ru`, **When** переключает селектор на English, **Then** язык книги мгновенно меняется на `en` с сохранением позиции скролла.
2. **Given** читатель кликает на `[P0-79: Crush Extrication]`, **Then** ридер плавно скроллит к разделу 2.1 с описанием протокола декомпрессии.
3. **Given** читатель закрывает вкладку и открывает снова в оффлайн-режиме (в самолете), **Then** PWA Service Worker отдает закэшированный текст из IndexedDB.

---

### User Story 2 - Supporter & ZTA Architecture Kit Checkout via Paddle (Priority: P2)

Читатель хочет поддержать проект или получить оффлайн-файлы книги и инфраструктурный код. На `/buy` он выбирает сумму (PWYW: $5, $12.99 или $50), оплачивает через встроенный оверлей Paddle и получает мгновенную страницу скачивания EPUB 3, Typst PDF 6"x9" и архива с ZTA Terraform/Docker шаблонами.

**Why this priority**: Основной цифровой генератор дохода от книги с чистой маржой $>88\%$ и 100% налоговым комплаенсом по NACE 62.01 в Армении (1% налог).

**Independent Test**: На `/buy` нажатие на «Get Supporter Bundle» открывает Paddle Checkout с валидным Product ID, после успешной оплаты срабатывает редирект на `/success?token=...` с одноразовыми ссылками на скачивание.

**Acceptance Scenarios**:
1. **Given** пользователь выбирает рекомендуемую цену $12.99, **When** оплачивает картой через Paddle, **Then** вебхук Paddle валидирует подпись, фиксирует покупку в базе и генерирует подписанные Cloudflare R2 URL на скачивание EPUB/PDF/ZTA архива.

---

### User Story 3 - Automated DTC Print-on-Demand via Lulu Print API (Priority: P3)

Русскоязычный читатель хочет получить бумажную книгу 6"x9" в мягкой обложке. На странице `/print` он вводит адрес доставки (США, Германия, Грузия, Казахстан и др.), оплачивает $24.99 + доставку через Paddle $\to$ бэкенд автоматически создает заказ на печать в **Lulu Print API** с дропшиппингом до двери читателя.

**Why this priority**: Решает проблему отсутствия поддержки русского языка в Amazon KDP для Print-on-Demand и дает рекордную маржу $16.04 с каждой книги.

**Independent Test**: Заполнение адреса на `/print` отправляет запрос в `/api/shipping/estimate` (возвращает точную стоимость доставки Lulu), после оплаты в Paddle вебхук `/api/webhooks/paddle-print` отправляет POST запрос в `https://api.lulu.com/print-jobs/`.

**Acceptance Scenarios**:
1. **Given** читатель из Германии вводит адрес в Берлине, **When** оплачивает $24.99 + €5.50 доставки, **Then** в Lulu API создается `print_job` с макетом `paperback_ru_lulu.pdf` и обложкой `cover_ru_lulu.pdf`, а читатель получает трек-номер на почту.

---

### User Story 4 - Amazon Prime Direct Outbound for EN & UK (Priority: P4)

Англо- или украиноязычный посетитель нажимает «Order on Amazon» $\to$ перенаправляется на нативную карточку книги на Amazon.com с бесплатной доставкой Prime за 1–2 дня.

**Why this priority**: Использование глобальной логистической мощи Amazon для 100% охвата англо- и украиноязычной диаспоры.

**Independent Test**: Кнопки на `/print` для English Edition и Українського Видання ведут на прямые ASIN-ссылки Amazon KDP.

---

## ⚙️ Functional Requirements & Specifications

### 1. Web Reader Engine (`/read`)
* **FR-01 (Trilingual Markdown SSG):** Статический генератор ридера на базе VitePress / Next.js с поддержкой трех каталогов: `books/001-daddys-boomer-mommys-sasuke-kun/release/daddys-boomer-mommys-sasuke-kun-v25.0.md` (RU), `daddys-boomer-mommys-sasuke-kun-en-v2.2.md` (EN), `daddys-boomer-mommys-sasuke-kun-ua-v1.7.md` (UA).
* **FR-02 (Interactive 86-Valve Anchor Mesh):** Каждый тег `[P0-XX]` в тексте автоматически подсвечивается и имеет обратную ссылку на строку в P0-Матрице.
* **FR-03 (PWA Offline Caching):** Service Worker кэширует скомпилированные страницы глав в IndexedDB браузера.
* **FR-04 (Reader Settings):** Переключатель темы (Dark / Sepia / Light), размер шрифта (14–22px), моноширинный режим кода.

### 2. E-Commerce & Webhooks (`/api`)
* **FR-05 (Paddle MoR Overlay Integration):** Встраивание `Paddle.js` для цифровых бандлов ($5–$50 PWYW) и печатных заказов.
* **FR-06 (Lulu Print API Webhook Handler):**
  * `POST /api/webhooks/paddle`: парсинг `transaction.completed` $\to$ если SKU = `RU_PRINT_BOOK`, вызов OAuth2 авторизации Lulu API $\to$ создание `print_job` с параметрами: `pod_package_id: 0600X0900BWSTDPB060UW444GXX` (Trade Paperback 6"x9", Standard Black & White, 60# Cream Paper, Glossy Cover).
* **FR-07 (Shipping Rate Calculator API):** `POST /api/shipping/calculate` опрашивает Lulu API `/print-job-cost-calculations/` по коду страны и индексу.

### 3. Non-Functional & Security
* **NFR-01 (Edge Latency):** Статические страницы отдаются с Cloudflare Edge со временем ответа $< 50\text{ ms}$.
* **NFR-02 (Zero Cookie Banner):** Ридер не использует рекламных кук или трекеров (только анонимная аналитика Plausible / Cloudflare Web Analytics).
