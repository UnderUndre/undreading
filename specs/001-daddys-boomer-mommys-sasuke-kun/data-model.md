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

---

## Print Layout & POD Production Entities

### `VendorPrintProfile`
- `vendor_id`: Enum (`"amazon_kdp"`, `"ingram_spark"`, `"lulu_direct"`)
- `paper_stock`: Enum (`"white_50lb"`, `"cream_60lb"`, `"groundwood_45lb"`)
- `spine_multiplier`: Float (e.g., `0.002252` for KDP white, `0.0025` for KDP cream)
- `ppi`: Optional Integer (e.g., `474` for Ingram 50# white, `454` for Ingram 60# cream)
- `min_spine_text_pages`: Integer (`79` for KDP, `48` for Ingram)
- `spine_text_safety_margin`: Float (`0.0625` in or `0.03125` in for narrow spines)
- `barcode_box_width`: Float (`2.0` in for KDP, `1.75` in for Ingram)
- `barcode_box_height`: Float (`1.2` in for KDP, `1.0` in for Ingram)
- `barcode_spine_clearance`: Float (`0.25` in minimum clearance from spine fold)

### `PrintLayoutSpec`
- `trim_size`: String (`"6x9_in"` / `152.4x228.6 mm`)
- `interior_bleed`: Float (`0.0` in strictly No-Bleed for interior PDF)
- `cover_bleed`: Float (`0.125` in on all outer cover spread edges)
- `gutter_margin`: Float (dynamic: `0.500` in to `1.000` in depending on page count)
- `outer_margin`: Float (`0.500` in to `0.625` in)
- `top_bottom_margin`: Float (`0.625` in to `0.750` in)
- `color_space_interior`: String (`"DeviceGray_100_K"`)
- `color_space_cover`: String (`"CMYK_FOGRA39_TAC_300"`)
- `dpi_floor_halftone`: Integer (`300`)
- `dpi_floor_lineart`: Integer (`1200`)
- `max_ascii_line_length`: Integer (`68` characters)
- `terminal_blank_verso`: Boolean (`true` for KDP barcode allocation)

### `PreFlightAuditReport`
- `file_path`: String
- `pdf_version`: String (`"PDF/X-1a:2001"`)
- `verapdf_status`: Enum (`"PASS"`, `"FAIL"`)
- `verapdf_rule_violations`: List of Strings
- `all_fonts_embedded`: Boolean
- `min_raster_dpi`: Integer
- `has_rgb_in_interior`: Boolean (`false` required)
- `trim_box_matches`: Boolean
- `total_pages_multiple_of_two`: Boolean

### `ReaderThemePalette`
- `theme_id`: Enum (`"default_light"`, `"default_dark"`, `"shinobi_scroll"`, `"vault_terminal_3000"`)
- `background_color`: Hex String (e.g. `"#F4ECD8"` for Shinobi Scroll, `"#0D1117"` for Dark, `"#0A0F0D"` for Vault Terminal)
- `text_color`: Hex String (e.g. `"#2C221E"` for Shinobi Scroll, `"#00FF66"` for Vault CRT Terminal)
- `wcag_contrast_ratio`: Float (strictly $\ge 4.5:1$ meeting WCAG 2.1 AA compliance)
- `font_family_body`: String
- `font_family_code`: String

### `ZtaEngineArtifact`
- `binary_name`: String (`"ztacheck"`)
- `source_language`: Enum (`"Go"`, `"Rust"`, `"Python"`)
- `supported_targets`: List of Strings (`["linux_amd64", "linux_arm64", "darwin_arm64", "windows_amd64"]`)
- `nace_code`: String (`"62.01"`)
- `license_type`: String (`"Commercial Software License with Documentation"`)
