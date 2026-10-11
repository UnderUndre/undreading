# Research & Decision Log: 001-daddys-boomer-mommys-sasuke-kun («Сантехника Бытия»)

**Feature**: `001-daddys-boomer-mommys-sasuke-kun`  
**Date**: 2026-09-27  
**Status**: Resolved / Completed

---

## 1. Архитектурные и Технические Решения (Decision Records)

### DR-01: Отказ от самописного DRM в пользу Open-Source SSG (VitePress / Astro Starlight)
* **Контекст:** Ранее рассматривался самописный e-reader на базе `foliate-js` с поглавной нарезкой через API Gateway и JWT-авторизацией.
* **Проблема:** Высокая стоимость разработки, медленный cold start, риск сбоев в БД при наплыве читателей, бессмысленность DRM против скрапинга и скриншотов.
* **Решение:** Текст монографии 100% открыт на `undreading.com` через быстрый статический генератор (**VitePress / Astro Starlight**) с хостингом на Cloudflare Pages / GitHub Pages. Монетизация перенесена с закрытия текста на продажу сопутствующего софтверного бандла (*Supporter & ZTA Architecture Kit*).
* **Последствия:** Нулевая стоимость серверного инференса, мгновенный отклик (0 ms latency), идеальное SEO и виральный охват.

### DR-02: Дистрибуция на Amazon KDP: Исключительно печать Paperback PoD
* **Контекст:** Попытка продавать электронную книгу Kindle Ebook за $12.99 при наличии открытого текста на сайте.
* **Проблема:** Политика Amazon KDP Price Matching при обнаружении бесплатного открытого текста в сети принудительно сбрасывает цену электронной книги до $0.00 или блокирует аккаунт.
* **Решение:** На Amazon KDP выставляется **СТРОГО печатный физический формат Paperback Print-on-Demand (6"x9" Trade Paperback)** по цене **$24.99**.
* **Последствия:** Исключен ценовой демпинг, роялти ~$10.86–$11.00 за экземпляр выводятся на Payoneer US Checking Account с 0% налогом у источника в США (W-8BEN).

### DR-03: Юридическая опрессовка дескриптора Paddle MoR под NACE 62.01
* **Контекст:** Продажи цифрового комплекта через Paddle Merchant of Record и уплата налога 1% для малого бизнеса в Грузии / Армении.
* **Проблема:** Налоговая служба может попытаться переквалифицировать продажу «книги» в роялти (литературная деятельность) с потерей льготного 1% режима по правилам GAAR (ст. 73.9 НК Грузии).
* **Решение:** Продукт в Paddle MoR регистрируется строго как: *"ZTA Security Architecture Specification & Infrastructure Implementation Kit (NACE 62.01)"*. Покупатель приобретает пакет инфраструктурного кода (Terraform, Docker, Ansible), к которому книга приложена как техническая спецификация.
* **Последствия:** 100% защита льготного налогового режима 1% с оборота.

### DR-04: Статическая пре-генерация переводов и ролевых тем
* **Контекст:** Предоставление читателю переводов в разных стилях (Валера, Шиноби, Геральт).
* **Проблема:** Живые запросы к LLM API во время чтения сжигают $0.80–$1.50 на пользователя, обнуляя маржу.
* **Решение:** Все локализации и стилистические варианты компилируются заранее на этапе сборки через Pandoc-пайплайн и отдаются в виде готовых статических HTML/Markdown файлов.

---

## 2. Финансовая Модель и Тарифная Сетка

| Продукт / SKU | Формат | Канал / Процессинг | Стоимость (USD) | Чистая маржа |
| :--- | :--- | :--- | :--- | :--- |
| **Open-Source Web Reader** | Статический сайт (HTML/MD) | `undreading.com` / GitHub | **$0.00 (Free)** | Лидогенератор |
| **Supporter & Architecture Kit** | EPUB 3 + Typst PDF + Terraform ZTA | Paddle MoR (NACE 62.01) | **PWYW ($5 min / $12.99 rec / $50+)** | **>88%** ($11.51 на $12.99) |
| **Amazon Paperback (PoD)** | Физическая печать 6"x9" | Amazon KDP Print $\to$ Payoneer | **$24.99** | **~43.4%** (~$10.86 роялти) |
| **Founding Citizen Bundle** | Полный комплект + 6 мес клуба | Paddle / `@CryptoBot` | **$199.00** | **>90%** |

---

## DR-07: ZTA Engine CLI Software Bundling for NACE 62.01 Substance Protection

- **Context**: Under Georgian Tax Code Art. 73.9 (GAAR / Substance over Form) and Government Decree No. 415, the 1% Small Business flat tax rate is strictly available for IT software development (NACE 62.01/62.09). Literary royalties and consulting fees are categorically barred from the 1% regime and subject to 20% standard personal income tax with 50% penalties.
- **Decision**: The Supporter Kit sold via Paddle MoR ($12.99 PWYW) is legally and technically structured as a software product: *"ZTA Security Automation CLI & Engine License (NACE 62.01)"*. The kit bundles a compiled standalone security scanning binary (`ztacheck`) auditing host ZTA compliance. The monograph «The Plumbing of Being» is included as technical architecture documentation.
- **Consequences**: Provides 100% defensible physical substance against tax reclassification during revenue audits, preserving the 1% flat tax status on all e-commerce checkouts.
