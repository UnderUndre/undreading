# Tasks: 001-daddys-boomer-mommys-sasuke-kun — «Сантехника Бытия»

**Input**: Design documents from `specs/001-daddys-boomer-mommys-sasuke-kun/` (`spec.md`, `plan.md`, `research.md`, `data-model.md`, `quickstart.md`)  
**Prerequisites**: `plan.md` (complete), `spec.md` (complete)

---

## Agent Tags & Roles

| Tag | Agent / Skill | Domain |
| :--- | :--- | :--- |
| `[SETUP]` | orchestrator | Scaffolding, shared configs, Makefile, toolchain setup |
| `[DOCS]` | documentation-writer | Monograph text authoring, chapters, P0 matrix, appendices |
| `[FE]` | frontend-specialist | VitePress / Astro Starlight web-reader, CSS themes, UI |
| `[OPS]` | devops-engineer | Build automation, Pandoc/Typst pipelines, Cloudflare Pages deploy, packaging |
| `[SEC]` | security-auditor | Fact-checking, zero-trust audit Level 1/2, legal compliance (NACE 62.01, W-8BEN) |
| `[E2E]` | test-engineer | Build verification, epubcheck, PDF geometry audit, link linter |

---

## Phase 1: Setup & Build Scaffolding

**Purpose**: Scaffolding directories, Makefile targets, and build toolchains.

- [ ] T001 [SETUP] Verify and configure project directory layout per `plan.md` (`books/`, `docs/`, `templates/`, `assets/`, `dist/`)
- [ ] T002 [SETUP] Configure root `package.json` with scripts (`build:docs`, `build:epub`, `build:pdf`, `lint:markdown`)
- [ ] T003 [OPS] Create `Makefile` with targets `build`, `build:docs`, `build:epub`, `build:pdf`, `pack:zta-kit`, `validate`
- [ ] T004 [OPS] Setup Typst template `templates/book-paperback-6x9.typ` with proper margins (0.125" bleed, inner gutter 0.75", outer 0.5") and open fonts
- [ ] T005 [OPS] Setup clean CSS stylesheet `templates/epub-style.css` for EPUB 3 rendering

---

## Phase 2: Foundational Monograph Release Volume (v18.0)

**Purpose**: Finalization of the master volume text (`v18.0`) incorporating the Remote Income Atlas, 7 Undrlla Projects, and all 70 P0-Directives.

- [ ] T006 [DOCS] Compile master text file `books/001-daddys-boomer-mommys-sasuke-kun/daddys-boomer-mommys-sasuke-kun-v18.0.md` on base of `v17.5.md`
- [ ] T007 [DOCS] Author and integrate the **Remote Income Atlas (6 Digital Crafts & Financial Rails)** into Chapter 7.5 and Chapter 8
- [ ] T008 [DOCS] Author and integrate the **7 Undrlla Ecosystem Projects Topology** (`underoute`, `undevops`, `undreading`, `undreplanning`, `undreposts`, `undreseller`, `unet`) into Chapter 8.2 and Chapter 12
- [ ] T009 [SEC] Perform Level 1/2 forensic verification of all 70 P0-directives, formulas, drug dosages, and legal statutes
- [ ] T010 [DOCS] Verify strict boundary between Undre personal biography (N=1) in Prologue and AI Valera external research in chapters

---

## Phase 3: User Story 1 (US1: Open-Source Static Web Reader Platform)

**Goal**: Readers can access, read, and search the 100% open text on `undreading.com` with zero latency and responsive design.

- [ ] T011 [FE] [US1] Initialize VitePress / Astro Starlight documentation site under `docs/` with chapter routing
- [ ] T012 [FE] [US1] Split master monograph `v18.0.md` into static web chapters under `docs/chapters/`
- [ ] T013 [FE] [US1] Implement landing page `docs/index.md` with Executive TL;DR, 5 Echelons overview, and P0-Matrix interactive search
- [ ] T014 [FE] [US1] Implement custom CSS theme presets («Свиток Шиноби», «Терминал Убежища 3000»)
- [ ] T015 [FE] [US1] Add non-intrusive callout banner on web chapters: link to Supporter & ZTA Architecture Kit ($12.99 PWYW)
- [ ] T016 [OPS] [US1] Configure Cloudflare Pages / GitHub Pages automated deployment pipeline

---

## Phase 4: User Story 2 (US2: EPUB 3 & Amazon KDP Paperback Print Pipeline)

**Goal**: Readers can read offline on e-readers (EPUB 3) or buy physical 6"x9" trade paperbacks on Amazon KDP with zero price matching issues.

- [ ] T017 [OPS] [US2] Automate Pandoc compilation script for EPUB 3 generation with cover image and metadata
- [ ] T018 [OPS] [US2] Automate Typst compilation script for Amazon KDP Paperback PDF (6"x9" Trade Paperback format)
- [ ] T019 [E2E] [US2] Validate generated EPUB 3 via `epubcheck` (0 errors, 0 warnings)
- [ ] T020 [E2E] [US2] Validate generated PDF geometry via `pdfinfo` and visual check against Amazon KDP print specifications
- [ ] T021 [SEC] [US2] Verify Amazon KDP account settings: Paperback PoD only ($24.99), Payoneer US ACH payout, Form W-8BEN 0% withholding

---

## Phase 5: User Story 3 (US3: Supporter & ZTA Architecture Kit Packaging)

**Goal**: Supporters can purchase the complete ZTA Architecture Kit & e-book bundle through Paddle MoR under NACE 62.01 with 1% tax protection.

- [ ] T022 [OPS] [US3] Assemble ZTA Architecture Kit bundle structure in `templates/zta-kit/` (Terraform, Docker Compose, Traefik v3 SSL, Restic S3, WireGuard)
- [ ] T023 [DOCS] [US3] Include Markdown templates in ZTA Kit: Decision Journal Type 1, 8-Point CPA LLC Checklist, Emergency 03:00 Runbook
- [ ] T024 [OPS] [US3] Automate `make pack:zta-kit` producing `dist/zta-architecture-kit-v18.0.zip`
- [ ] T025 [SEC] [US3] Verify Paddle MoR product descriptor: *"ZTA Security Architecture Specification & Infrastructure Implementation Kit (NACE 62.01)"*

---

## Phase 6: User Story 4 (US4: Expat Marketplace & Business Plans Sync)

**Goal**: Align `undreseller` marketplace and `undrlla` master business plans with the released monograph.

- [ ] T026 [DOCS] [US4] Update `undreplans/docs/projects/undreseller/undreseller-business-plan.md` with Expat Refurbished Marketplace model (6-month warranty, certified stock)
- [ ] T027 [DOCS] [US4] Update `undreplans/docs/projects/undrlla/undrlla-business-plan.md` with 7-node project topology, investment tranches ($10k/$50k/$150k), and utility return model
- [ ] T028 [SEC] [US4] Verify unit economics, margin floors (>88%), and GAAR compliance across all business plan files

---

## Phase 7: Polish & Release Verification (Quality Gates)

**Purpose**: Final end-to-end verification, stage snapshotting, and public launch.

- [ ] T029 [E2E] Run complete build pipeline `make build` and verify all artifacts in `dist/`
- [ ] T030 [SEC] Perform constitution compliance check against all principles
- [ ] T031 [DOCS] Update version tags, release notes, and documentation index
- [ ] T032 [SETUP] Tag stage snapshot `snapshot-stage plan 001-daddys-boomer-mommys-sasuke-kun` and `tasks`

---

## Dependency Graph & Parallel Execution Lanes

```text
LANE 1 (Monograph & Content - [DOCS]/[SEC]):
  T006 (v18.0) ──► T007 (Remote Atlas) ──► T008 (7 Projects) ──► T009 (Fact-Check) ──► T010 (Demarcation)
                                                                                               │
LANE 2 (Tooling & Pipelines - [OPS]/[SETUP]):                                                  │
  T001 ──► T002 ──► T003 ──► T004 (Typst) & T005 (EPUB CSS) ───────────────────────────────────┼──► T029 (Build All)
                                                                                               │
LANE 3 (Web Platform - [FE]):                                                                  │
  T011 (VitePress Init) ──► T012 (Split Chapters) ──► T013 (Landing) ──► T014 (Themes) ──► T015 (Banner) ──► T016 (Deploy)
                                                                                               │
LANE 4 (Publishing & Commerce - [OPS]/[SEC]):                                                  │
  T017 (EPUB Pandoc) & T018 (PDF Typst) ──► T019 (epubcheck) & T020 (pdfinfo) ──► T021 (KDP)  │
  T022 (ZTA Bundle) ──► T023 (Templates) ──► T024 (Zip) ──► T025 (Paddle MoR)                  │
  T026 (undreseller BP) ──► T027 (undrlla BP) ──► T028 (Unit Eco Audit)                        │
                                                                                               ▼
                                                                                  T030 (Constitution Check) ──► T031 ──► T032
```

---

## Critical Path

`T006` (Compile v18.0) $\to$ `T007` (Remote Atlas) $\to$ `T008` (7 Projects) $\to$ `T012` (Split Web Chapters) $\to$ `T018` (Typst PDF) $\to$ `T024` (ZTA Zip) $\to$ `T029` (Full Build) $\to$ `T030` (Gate Check) $\to$ **Public Release**

---

## Agent Dispatch Summary

- **[SETUP] Orchestrator**: T001, T002, T032 (3 tasks)
- **[DOCS] documentation-writer**: T006, T007, T008, T010, T023, T026, T027, T031 (8 tasks)
- **[FE] frontend-specialist**: T011, T012, T013, T014, T015 (5 tasks)
- **[OPS] devops-engineer**: T003, T004, T005, T016, T017, T018, T022, T024 (8 tasks)
- **[SEC] security-auditor**: T009, T021, T025, T028, T030 (5 tasks)
- **[E2E] test-engineer**: T019, T020, T029 (3 tasks)

**Total Tasks**: 32 tasks | **Suggested MVP Scope**: Phases 1, 2, 3, 4, 5

### Phase 4.1: Multi-Vendor Print & Layout Production Pipeline

- [ ] **T033**: Develop multi-vendor cover geometry and spine calculation engine `scripts/generate-covers.py` with parameterized targets `build:cover:kdp`, `build:cover:ingram`, and `build:cover:lulu` implementing exact vendor paper caliper and barcode clearance formulas.
- [ ] **T034**: Implement Typst 6"x9" master book print layout `templates/book-paperback-6x9.typ` featuring dynamic gutter curve scaling (0.500"–1.000"), 100% DeviceGray color profiles, automatic recto chapter opening with blank verso suppression, ASCII diagram 68-char constraint, and repeating table headers.
- [ ] **T035**: Build two-stage PDF/X-1a transcoding script `scripts/transcode-pdfx1a.sh` utilizing Ghostscript and `cpdf` for OutputIntent color profile embedding and layer flattening.
- [ ] **T036**: Develop automated pre-flight quality verification script `scripts/validate-print-pdf.sh` integrating `veraPDF` ISO 15930-1 validation, deep PostScript operator color scanning (`pdftops -level2` catching vector RGB), `pdffonts` embedding audit, and `pdfinfo` boundary box checks.
- [ ] **T037**: Implement micro-typography linter `scripts/lint-typography.py` utilizing Markdown AST parsing to enforce non-breaking space placement (`~`) strictly within `Text` AST nodes while completely ignoring `CodeBlock`, `InlineCode`, `HtmlBlock`, and `Table` nodes.
- [ ] **T038**: Enforce Amazon KDP factory barcode protocol by appending an explicit blank terminal Verso page to the Typst template, verifying page count stability and spine alignment across production builds.
