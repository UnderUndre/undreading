# Data Model & Content Schema: 001-daddys-boomer-mommys-sasuke-kun («Сантехника Бытия»)

**Feature**: `001-daddys-boomer-mommys-sasuke-kun`  
**Date**: 2026-09-27  
**Status**: Phase 1 Artifact

---

## 1. Сущности Контента и Архитектуры Книги

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            MONOGRAPH MASTER VOLUME                          │
│  - version: String (e.g. "18.0")                                            │
│  - title: String                                                            │
│  - authors: Array<{ name: String, role: "Author N=1" | "AI Copilot" }>      │
│  - license: "MIT (Code) / CC-BY-NC-ND 4.0 (Text)"                           │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
         ┌─────────────────────────────┼─────────────────────────────┐
         ▼                             ▼                             ▼
┌───────────────────┐        ┌───────────────────┐        ┌───────────────────┐
│     CHAPTER       │        │   P0 DIRECTIVE    │        │  FORENSIC CONCEPT │
│ - number: 1..12   │        │ - id: 1..70       │        │ - id: 1..220+     │
│ - title: String   │        │ - name: String    │        │ - title: String   │
│ - echelon: L1..L5 │        │ - echelon: L1..L5 │        │ - domain: String  │
│ - wordCount: Int  │        │ - param: String   │        │ - proofLevel: 1..2│
│ - epigraph: Track │        │ - rule: String    │        │ - status: Enum    │
└───────────────────┘        └───────────────────┘        └───────────────────┘
```

---

## 2. Спецификация Сущностей

### Entity 1: `MonographVolume` (Мастер-Том Монографии)
* `version`: `String` (семантическое версионирование рукописи: `v17.5`, `v18.0`);
* `wordCount`: `Int` ($\ge 120\,000$ слов);
* `lineCount`: `Int` ($\ge 4\,000$ строк);
* `chapters`: `Array<Chapter>` (12 глав);
* `appendices`: `Array<Appendix>` (Приложения A–G);
* `p0Matrix`: `Array<P0Directive>` (70 директив);
* `concepts`: `Array<ForensicConcept>` (220+ концептов).

### Entity 2: `P0Directive` (Ключевая Задвижка P0)
* `id`: `Int` (1..70);
* `name`: `String` (название артефакта, например, *TCCC MARCH PAWS*, *Post-Finasteride Gate*);
* `echelon`: `Enum` (`L1_LIFE`, `L2_LIBERTY`, `L3_RESOURCES`, `L4_SOVEREIGNTY`, `L5_HARDWARE`);
* `technicalParameter`: `String` (точный физический/нормативный порог: дозировка, статья закона, протокол);
* `mechanism`: `String` (физиологический или алгоритмический принцип);
* `actionableDirective`: `String` (конкретная инструкция для оператора в стиле «Правило Валеры»).

### Entity 3: `ProductSKU` (Коммерческий Продуктовый Пакет)
* `skuId`: `String` (`supporter-zta-kit`, `amazon-paperback-pod`, `founding-citizen`);
* `name`: `String`;
* `naceCode`: `String` (`NACE 62.01` — Computer programming activities);
* `priceUsd`: `Float` ($12.99 PWYW / $24.99 / $199.00);
* `distributionChannel`: `Enum` (`PADDLE_MOR`, `AMAZON_KDP_PRINT`, `TELEGRAM_CRYPTOBOT`);
* `bundlePayload`: `Array<String>` (перечень файлов в комплекте: EPUB 3, Typst PDF, Terraform ZTA, Docker Compose, Audio MP3).

---

## 3. Схема ZTA Architecture Kit Bundle

```text
zta-architecture-kit-v18.0.zip
├── README.md
├── LICENSE (MIT)
├── book/
│   ├── sanitary-engineering-of-being.epub
│   └── sanitary-engineering-of-being-paperback.pdf
├── infrastructure/
│   ├── docker-compose.prod.yml (Traefik v3 + SSL + Restic S3)
│   ├── terraform/ (Hetzner CPX41 automation)
│   ├── wireguard/ (Sovereign mesh configs)
│   └── scripts/ (Hardened backup 3-2-1-1-0)
└── templates/
    ├── decision-journal-type1.md
    ├── cpa-audit-checklist-llc.md
    └── emergency-0300-runbook.md
```
