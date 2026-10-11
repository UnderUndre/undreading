# Feature Specification: 002-publishing-pipeline-and-platform — Undreading Web Reader, Publishing Pipeline & ZTA Kit Platform

**Feature Branch**: `002-publishing-pipeline-and-platform`  
**Created**: 2026-10-11  
**Updated**: 2026-10-11 (Post-Analyze Remediation: Full Gherkin Criteria & NFR Matrix)  
**Status**: Approved (Executable Spec)  
**Input**: Business Plans (`undreading-business-plan.md` v2.0/v13.0, `undrlla-business-plan.md` v15.1, `undreseller-business-plan.md` v18.0), Feature Spec `001-daddys-boomer-mommys-sasuke-kun` (v25.2 Release & 9-Edition Matrix)

---

## 📖 1. Context & Architectural Overview

`undreading` (`undreading.com`) — открытая цифровая издательская платформа, веб-читалка и инфраструктурный хаб монетизации для фундаментальной монографии **«Сантехника Бытия»** и сопутствующего софтверного пакета **ZTA Security Architecture Kit**.

Данная спецификация консолидирует все платформенные, веб- и сборочно-издательские задачи экосистемы:

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

## 🎯 2. Prioritized User Stories & Gherkin Acceptance Scenarios

### User Story 1 — Instant 9-Edition Web Reader & P0 Matrix (Priority: P1)

Посетитель переходит на `undreading.com/read`, выбирает любое из 9 изданий библиотеки (3 оригинала: RU v25.2, EN v2.4, UA v1.9 + 6 прямых перекрестных переводов), мгновенно читает полный текст без задержек и пейволлов, пользуется локальным поиском и переходит к нужному разделу по клику на любую из 110 задвижек матрицы P0.

**Why this priority**: Фундаментальный открытый лид-магнит экосистемы: свободное чтение формирует доверие к компетенциям автора и направляет поток на коммерческий Supporter Kit.

**Independent Test**: Доступен по маршрутам `GET /read/ru-edition/ru`, `/read/ru-edition/en`, `/read/ru-edition/ua`, `/read/en-edition/en`, `/read/en-edition/ru`, `/read/en-edition/ua`, `/read/ua-edition/ua`, `/read/ua-edition/ru`, `/read/ua-edition/en`. Все 110 задвижек `[P0-01]`–`[P0-110]` кликабельны и скроллят к соответствующему якорю.

**Acceptance Scenarios (Gherkin)**:
1. **Scenario: Переключение между региональными изданиями и переводами**
   - **Given** читатель находится на странице `undreading.com/read/ru-edition/ru` (канонический русский оригинал),
   - **When** читатель выбирает в селекторе перевода `English Translation (ru-edition/en)`,
   - **Then** ридер мгновенно отображает полный английский перевод монографии Валеры без перезагрузки рантайма и с сохранением относительной позиции главы.
2. **Scenario: Интерактивный переход по матрице задвижек P0**
   - **Given** читатель просматривает сводную матрицу P0 на лендинге или в Разделе 1,
   - **When** читатель кликает на плашку `[P0-74: 115-FZ Predatory AML Tariff Shield]`,
   - **Then** интерфейс плавно скроллит документ к подразделу `10.13.1` с разбором судебных прецедентов ВС РФ.
3. **Scenario: Оффлайн-чтение через Service Worker PWA**
   - **Given** читатель открыл монографию в веб-ридере,
   - **When** устройство теряет интернет-соединение (режим полета),
   - **Then** страница продолжает открываться и отдавать все 9 глав из кэша Service Worker без ошибок сети.

---

### User Story 2 — EPUB 3 & Multi-Vendor Print Production Pipeline (Priority: P2)

Читатель приобретает физическую бумажную книгу на Amazon KDP или через DTC-дропшиппинг Lulu, либо скачивает оффлайн EPUB 3 для ридеров (Kindle/Apple Books).

**Why this priority**: Физическая печать — ключевой осязаемый артефакт доверия и коллекционный продукт ($24.99), а EPUB 3 — стандарт оффлайн-чтения без привязки к браузеру.

**Independent Test**: Выполнение `npm run build:epub` производит валидный EPUB 3 файл, проходящий `epubcheck` с 0 ошибками; `npm run build:pdf` компилирует Typst PDF с полями 0.875" и пустой финальной страницей Verso; `scripts/validate-print-pdf.sh` подтверждает соответствие стандарту PDF/X-1a:2001 (veraPDF).

**Acceptance Scenarios (Gherkin)**:
1. **Scenario: Компиляция и валидация EPUB 3**
   - **Given** мастер-монолит книги в формате Markdown,
   - **When** запускается таргет сборки `make build:epub`,
   - **Then** Pandoc компилирует `dist/sanitary-engineering-of-being-ru.epub` со встроенными стилями `templates/epub-style.css`, обложкой и валидным оглавлением NCX/Nav.
2. **Scenario: Генерация печатного блока под Amazon KDP**
   - **Given** мастер-шаблон `templates/book-paperback-6x9.typ`,
   - **When** выполняется компиляция Typst в PDF,
   - **Then** итоговый файл `dist/sanitary-engineering-of-being-paperback.pdf` имеет физический размер ровно 6"x9" (152.4 × 228.6 мм), внутренний корешок (gutter) 0.875" (22.2 мм), 100% DeviceGray цвет шрифта и пустую четную страницу Verso на конце под штрихкод типографии Amazon.
3. **Scenario: Двухстадийный конвейер PDF/X-1a и veraPDF**
   - **Given** скомпилированный Typst PDF,
   - **When** запускается скрипт `scripts/transcode-pdfx1a.sh`,
   - **Then** утилита Ghostscript/cpdf внедряет профиль FOGRA39 OutputIntent и сплющивает слои, а `veraPDF` валидирует ISO 15930-1 с результатом `PASS`.

---

### User Story 3 — Commercial Supporter Bundle & ZTA Kit Checkout (Priority: P3)

Читатель переходит на `/buy`, выбирает сумму поддержки по модели Pay-What-You-Want ($12.99 rec) и оплачивает заказ через оверлей Paddle MoR, моментально получая доступ к скачиванию EPUB 3, Typst PDF и ZTA-шаблонов под защитой NACE 62.01 (1% ставка налога в Армении/Грузии).

**Why this priority**: Основной цифровой генератор дохода с чистой маржой $>88\%$ и нулевым риском переквалификации в роялти налоговыми органами.

**Independent Test**: На `/buy` клик по «Get Supporter Bundle» открывает Paddle Checkout с дескриптором *"ZTA Security Architecture Specification & Infrastructure Implementation Kit (NACE 62.01)"*; после оплаты формируются временные Cloudflare R2 Signed URLs со сроком жизни 24 часа.

**Acceptance Scenarios (Gherkin)**:
1. **Scenario: Успешная оплата бандла через Paddle**
   - **Given** покупатель выбрал бандл на сумму $12.99,
   - **When** завершается оплата картой в оверлее Paddle,
   - **Then** вебхук бэкенда валидирует криптографическую подпись Paddle, генерирует 24-часовую подписанную ссылку Cloudflare R2 на скачивание архива `dist/zta-architecture-kit-v25.2.zip`.
2. **Scenario: Сохранение безналогового статуса NACE 62.01**
   - **Given** формируется транзакционный чек и дескриптор продукта в Paddle,
   - **When** инвойс регистрируется в налоговой отчетности,
   - **Then** позиция классифицируется строго как передача прав на использование инфраструктурного ПО (NACE 62.01) со ставкой налога 1% и 0% удержания у источника по форме W-8BEN.

---

### User Story 4 — Ecosystem Business Plans Sync (Priority: P4)

Синхронизация бизнес-моделей ресейл-маркетплейса `undreseller` и экосистемы `undrlla` с выпущенными релизами монографии.

**Why this priority**: Монография питает органическим трафиком смежные сервисы экосистемы (`undreseller`, `undrlla.network`).

**Independent Test**: Проверка файлов `undreseller-business-plan.md` и `undrlla-business-plan.md` на актуальность ссылок на 9-томную библиотеку монографий и сохранение порога маржинальности $>88\%$.

**Acceptance Scenarios (Gherkin)**:
1. **Scenario: Синхронизация топологии 7 проектов**
   - **Given** обновленная Глава 8.2 монографии с описанием 7 проектов,
   - **When** бизнес-планы обновляются,
   - **Then** узлы `underoute`, `undevops`, `undreading`, `undreplanning`, `undreseller`, `unet`, `undrlla` согласованы по терминологии и инвестиционным траншам ($10k/$50k/$150k).

---

## 📐 3. Non-Functional Requirements (ISO/IEC/IEEE 29148)

- **NFR-001 (Latency)**: Время отдачи страниц веб-ридера с Cloudflare CDN Edge $\le 100\text{ ms}$ p95; 0ms при повторном открытии из кэша PWA.
- **NFR-002 (Zero-DRM)**: 0% закрытых проприетарных DRM-контейнеров; 100% открытый текст в Markdown на GitHub и в вебе.
- **NFR-003 (Print ISO Conformance)**: 100% печатных PDF-файлов для Amazon KDP и Lulu валидируются стандартом PDF/X-1a:2001 через `veraPDF` с нулевыми критическими ошибками.
- **NFR-004 (Tax & Compliance)**: 100% коммерческих продаж через Paddle MoR классифицируются под кодом NACE 62.01 с уплатой 1% налога микробизнеса и нулевым риском GAAR по ст. 73.9.
- **NFR-005 (Margin Floor)**: Чистая маржинальность цифрового бандла $\ge 88\%$ от валовой выручки после комиссий платёжного шлюза.
- **NFR-006 (Zero Token Leakage)**: Чтение книги в вебе не инициирует запросов к платным LLM API: все 9 изданий пре-рендерены статически на этапе сборки.
