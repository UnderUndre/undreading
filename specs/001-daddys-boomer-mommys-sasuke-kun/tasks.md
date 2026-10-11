# Tasks: 001-daddys-boomer-mommys-sasuke-kun — «Сантехника Бытия» (Книги и Матрица Переводов)

**Scope**: Авторский текст монографии «Сантехника Бытия», канонические оригиналы и матрица из 6 перекрёстных переводов (всего 9 изданий).  
**Platform / Publishing Scope**: Задачи веб-ридера, генерации EPUB 3, вёрстки Typst PDF, ZTA Kit и Amazon KDP перенесены в спецификацию `specs/002-publishing-pipeline-and-platform/`.

---

## Agent Tags & Roles

| Tag | Agent / Skill | Domain |
| :--- | :--- | :--- |
| `[SETUP]` | orchestrator | Scaffolding, directory hierarchy, validation toolchains |
| `[DOCS]` | documentation-writer | Monograph authoring, cross-translations, style guards |
| `[SEC]` | security-auditor | Fact-checking Level 1/2, legal compliance, P0 directives |
| `[E2E]` | test-engineer | Automated chapter splitting, byte-exact concatenation audit, linting |

---

## Phase 1: Setup & Monograph Directory Architecture

**Purpose**: Scaffolding directory structure and cross-platform verification tooling.

- [x] T001 [SETUP] Verify and configure hierarchical directory layout (`ru-edition/`, `en-edition/`, `ua-edition/` with subfolders for each language)
- [x] T002 [SETUP] Configure root `package.json` scripts (`split:chapters`, `validate:books`, `lint:all`)
- [x] T003 [SETUP] Create `Makefile` & cross-platform `scripts/build.py` with targets `split:chapters`, `validate`, `clean`
- [x] T004 [DOCS] Setup style guards `STYLE-GUARD-EN.md` and `STYLE-GUARD-UA.md` with persona voices and taboo calques
- [x] T005 [E2E] Develop automated validation suite `validate_books.py` ensuring byte-for-byte concatenation integrity

---

## Phase 2: Foundational Master Volumes (3 Canonical Originals)

**Purpose**: Finalization and pressure-testing of the 3 culturally adapted master volumes.

- [x] T006 [DOCS] Finalize Russian Master Volume `v25.2` (`ru-edition/ru/daddys-boomer-mommys-sasuke-kun-v25.2.md`) — Persona: Валера (Digital Plumber), 110 P0 valves, Remote Income Atlas, 7 Undrlla projects, post-Soviet legal hydraulics (115-FZ, 572-FZ, 127-FZ)
- [x] T007 [DOCS] Finalize English Master Volume `en-v2.4` (`en-edition/en/daddys-boomer-mommys-sasuke-kun-en-v2.4.md`) — Persona: Bob the Gray, Anglo-Saxon US/UK dual-jurisdiction (IRC § 864, UK Non-Dom, PACER, Scottish aquamation)
- [x] T008 [DOCS] Finalize Ukrainian Master Volume `ua-v1.9` (`ua-edition/ua/daddys-boomer-mommys-sasuke-kun-ua-v1.9.md`) — Persona: Дядя Толя, Ukrainian wartime legal hydraulics (Diia, FOP Group 3, military levy, Art. 206 CPCU, Art. 42 CPCB)
- [x] T009 [SEC] Level 1/2 forensic verification across all 110 P0 directives, medical dosages (aspirin 300mg, NAC, Ramack-Matthew nomogram), and statutory citations
- [x] T010 [E2E] Eliminate structural defects: fix chapter transpositions (8.4-8.6, 10.13-10.17, 14-15, Appendix E 13-19), deduplicate 10.5.3, normalize headings to H2-H5, fix mixed alphabets

---

## Phase 3: Trilingual Cross-Translation Matrix (6 Targeted Cross-Translations)

**Purpose**: Direct, authentic cross-translations of each regional edition into the other two languages, creating a complete 9-book master library.

### Lane A: Russian Edition Translations (Валера's Post-Soviet Blueprint)
- [x] T011 [DOCS] Translate Russian Edition into English (`ru-edition/en/daddys-boomer-mommys-sasuke-kun-ru-en-v25.2.md`) — preserving Valera's voice, Soviet/post-Soviet institutional analysis (115-FZ, 572-FZ, housing orders), and 110 P0 valves in English
- [x] T012 [DOCS] Translate Russian Edition into Ukrainian (`ru-edition/ua/daddys-boomer-mommys-sasuke-kun-ru-ua-v25.2.md`) — preserving Valera's full monolithic text with Ukrainian linguistic idiom

### Lane B: English Edition Translations (Bob's Anglo-Saxon / US / UK Blueprint)
- [x] T013 [DOCS] Translate English Edition into Russian (`en-edition/ru/daddys-boomer-mommys-sasuke-kun-en-ru-v2.4.md`) — preserving Bob's cynical voice, US/UK common law analysis, PACER, Departure Tax, and US SMLLC hydraulics in Russian
- [x] T014 [DOCS] Translate English Edition into Ukrainian (`en-edition/ua/daddys-boomer-mommys-sasuke-kun-en-ua-v2.4.md`) — rendering Bob's US/UK legal and cognitive blueprint into authentic Ukrainian

### Lane C: Ukrainian Edition Translations (Дядя Толя's Wartime & Digital Diia Blueprint)
- [x] T015 [DOCS] Translate Ukrainian Edition into Russian (`ua-edition/ru/daddys-boomer-mommys-sasuke-kun-ua-ru-v1.9.md`) — translating Uncle Tolya's wartime engineering, Diia.City, FOP 3, NBU #18, and Art. 206 CPC into Russian
- [ ] T016 [DOCS] Translate Ukrainian Edition into English (`ua-edition/en/daddys-boomer-mommys-sasuke-kun-ua-en-v1.9.md`) — translating Uncle Tolya's complete Ukrainian defense and business blueprint into English for international expats, volunteers, and researchers

---

## Phase 4: Automated Split, Quality Gates & Library Verification

**Purpose**: Generate static navigation and verify mathematical integrity across all 9 editions.

- [ ] T017 [E2E] Run `split_chapters.py` across all 9 monograph files, generating `chapters/*.md`, `00-front-matter.md`, and clean `index.md` for each edition
- [ ] T018 [E2E] Execute comprehensive `validate_books.py` audit across all 9 books (byte-exact concatenation, P0 directive preservation, monotonicity)
- [ ] T019 [SEC] Final terminology and constitution compliance audit for all 9 books
- [ ] T020 [SETUP] Tag stage snapshot `snapshot-stage books-9-matrix 001-daddys-boomer-mommys-sasuke-kun`

---

## Dependency Graph & Execution Matrix

```text
3 ORIGINALS (Complete [x]):
  RU Original (v25.2) [x] ──────┬──► T011 (RU ➔ EN) ──┐
                                └──► T012 (RU ➔ UA) ──┤
                                                      │
  EN Original (v2.4)  [x] ──────┬──► T013 (EN ➔ RU) ──┼──► T017 (Split All 9) ──► T018 (Validate All 9) ──► Release
                                └──► T014 (EN ➔ UA) ──┤
                                                      │
  UA Original (v1.9)  [x] ──────┬──► T015 (UA ➔ RU) ──┤
                                └──► T016 (UA ➔ EN) ──┘
```

**Total Tasks**: 20 tasks | **Completed**: 10 tasks (50%) | **Pending**: 10 tasks (6 translations + 4 verification/release)
