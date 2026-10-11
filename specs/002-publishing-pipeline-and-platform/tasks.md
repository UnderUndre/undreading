# Tasks: 002-publishing-pipeline-and-platform — Undreading Platform & Publishing Pipeline

**Input**: Design documents from `specs/002-publishing-pipeline-and-platform/` (`spec.md`, `plan.md`)  
**Prerequisites**: Release artifacts from `specs/001-daddys-boomer-mommys-sasuke-kun/` (9-edition monograph matrix)

---

## Agent Tags & Roles

| Tag | Agent / Skill | Domain |
| :--- | :--- | :--- |
| `[SETUP]` | orchestrator | Scaffolding, shared configs, deployment setup |
| `[FE]` | frontend-specialist | VitePress / Astro Starlight web-reader, CSS themes, UI |
| `[OPS]` | devops-engineer | Pandoc/Typst pipelines, Cloudflare Pages/R2, packaging |
| `[SEC]` | security-auditor | Paddle MoR compliance, NACE 62.01, zero-trust storage |
| `[E2E]` | test-engineer | epubcheck, veraPDF ISO 15930-1, print pre-flight checks |
| `[DOCS]` | documentation-writer | Templates, business plans sync, release notes |

---

## Phase 1: Open-Source Static Web Reader Platform (undreading.com)

**Goal**: Readers can access, search, and read all 9 monograph editions on `undreading.com` with zero server latency and custom themes.

- [ ] T001 [FE] [US1] Initialize VitePress 1.x documentation site under `docs/` with chapter routing for all 9 editions (RU/EN/UA)
- [ ] T002 [FE] [US1] Implement landing page `docs/index.md` with Executive TL;DR, 5 Echelons overview, and interactive 110-valve P0 Matrix jump
- [ ] T003 [FE] [US1] Implement custom CSS theme presets («Свиток Шиноби», «Терминал Убежища CRT-3000»)
- [ ] T004 [FE] [US1] Add non-intrusive callout banner on web chapters with link to Supporter & ZTA Architecture Kit ($12.99 PWYW)
- [ ] T005 [OPS] [US1] Configure Cloudflare Pages automated deployment pipeline with custom domain `undreading.com`
- [ ] T006 [FE] [US1] Implement PWA Service Worker for offline in-browser reading cache

---

## Phase 2: EPUB 3 & Multi-Vendor Print Production Pipeline

**Goal**: Seamless offline reading on e-readers and physical print-on-demand via Amazon KDP, Lulu, and IngramSpark.

- [ ] T007 [OPS] [US2] Automate Pandoc compilation script for EPUB 3 generation with cover image, styling, and metadata
- [ ] T008 [OPS] [US2] Develop multi-vendor cover geometry engine `scripts/generate-covers.py` with spine calculation formulas (KDP, Ingram, Lulu)
- [ ] T009 [OPS] [US2] Build two-stage PDF/X-1a transcoding script `scripts/transcode-pdfx1a.sh` using Ghostscript and `cpdf` (FOGRA39 / DeviceGray 100% K)
- [ ] T010 [E2E] [US2] Develop automated pre-flight quality verification script `scripts/validate-print-pdf.sh` integrating `veraPDF` ISO 15930-1 validation
- [ ] T011 [E2E] [US2] Validate generated EPUB 3 files via `epubcheck` (0 errors, 0 warnings)
- [ ] T012 [SEC] [US2] Verify Amazon KDP account settings: Paperback PoD only ($24.99), Payoneer US ACH payout, Form W-8BEN 0% withholding
- [ ] T013 [OPS] [US2] Setup Lulu Print API webhook integration for Russian paperback dropshipping ($24.99, margin 64.2%)

---

## Phase 3: Supporter & ZTA Architecture Kit Packaging (Paddle MoR)

**Goal**: Commercial processing of the software bundle under NACE 62.01 with 1% tax protection and secure digital delivery.

- [ ] T014 [OPS] [US3] Assemble ZTA Architecture Kit bundle structure in `templates/zta-kit/` (Terraform, Docker Compose, Traefik v3 SSL, WireGuard)
- [ ] T015 [DOCS] [US3] Include Markdown templates in ZTA Kit: Decision Journal Type 1, 8-Point CPA LLC Checklist, Emergency 03:00 Runbook
- [ ] T016 [OPS] [US3] Automate packaging script producing `dist/zta-architecture-kit-v25.2.zip`
- [ ] T017 [SEC] [US3] Configure and verify Paddle MoR product descriptor (*"ZTA Security Architecture Specification & Infrastructure Implementation Kit (NACE 62.01)"*) and Cloudflare R2 24h Signed URLs

---

## Phase 4: Expat Marketplace & Ecosystem Business Plans Sync

**Goal**: Align `undreseller` and `undrlla` master business plans with released book editions and platform architecture.

- [ ] T018 [DOCS] [US4] Update `undreplans/docs/projects/undreseller/undreseller-business-plan.md` with Expat Refurbished Marketplace model
- [ ] T019 [DOCS] [US4] Update `undreplans/docs/projects/undrlla/undrlla-business-plan.md` with 7-node project topology and utility return model
- [ ] T020 [SEC] [US4] Verify unit economics, margin floors (>88%), and GAAR compliance across all business plans

---

## Phase 5: Final Quality Gates & Public Launch

**Goal**: End-to-end build verification, snapshotting, and public launch.

- [ ] T021 [E2E] Run complete build pipeline `npm run build` and verify all artifacts in `dist/`
- [ ] T022 [E2E] Automated health-check verification: assert 200 OK across all 9 web reader routes and Cloudflare Pages rollback readiness
- [ ] T023 [SEC] Perform constitution compliance check against all principles
- [ ] T024 [DOCS] Update release notes, changelog, and documentation index
- [ ] T025 [SETUP] Tag stage snapshot `snapshot-stage platform-launch 002-publishing-pipeline-and-platform`

---

## Dependency Graph & Execution Matrix

```text
T001 (VitePress Init) ──► T002 (Landing & P0 Jump) ──► T003 (Themes) ──► T004 (Banner) ──► T006 (PWA SW) ──┐
                                                                                                            │
T007 (Pandoc EPUB) ────┬──► T011 (epubcheck Gate) ──────────────────────────────────────────────────────────┼──► T021 (Build All)
                       │                                                                                    │      │
T008 (Cover Engine) ───┼──► T009 (PDF/X Transcode) ──► T010 (veraPDF Gate) ─────────────────────────────────┤      ▼
                       │                                                                                    │    T022 (Health Check)
                       └──► T012 (KDP Account Audit) ──► T013 (Lulu API Webhook) ───────────────────────────┤      │
                                                                                                            │      ▼
T014 (ZTA Structure) ──► T015 (MD Templates) ──► T016 (Pack Zip) ──► T017 (Paddle MoR & R2 Gate) ───────────┤    T023 (Constitution)
                                                                                                            │      │
T018 (undreseller BP) ──► T019 (undrlla BP) ──► T020 (Unit Econ Audit) ─────────────────────────────────────┘      ▼
                                                                                                                 T024 (Docs Index)
                                                                                                                   │
                                                                                                                   ▼
                                                                                                                 T025 (Tag Snapshot)
```

### Textual Dependency Relationships

- `T001 → T002`
- `T002 → T003`
- `T003 → T004`
- `T004 → T006`
- `T001 + T002 → T005`
- `T007 → T011`
- `T008 → T009`
- `T009 → T010`
- `T007 + T008 → T012`
- `T012 → T013`
- `T014 → T015`
- `T015 → T016`
- `T016 → T017`
- `T018 → T019`
- `T019 → T020`
- `T005 + T006 + T010 + T011 + T013 + T017 + T020 → T021`
- `T021 → T022`
- `T022 → T023`
- `T023 → T024`
- `T024 → T025`

### Critical Path

`T001` (VitePress) $\to$ `T002` (Landing) $\to$ `T008` (Covers) $\to$ `T009` (PDF/X) $\to$ `T010` (veraPDF) $\to$ `T016` (Pack ZTA) $\to$ `T017` (Paddle MoR) $\to$ `T021` (Build All) $\to$ `T022` (Health Check) $\to$ `T023` (Constitution) $\to$ **Public Launch**

---

## Parallel Execution Lanes

| Lane | Focus | Assigned Agent | Tasks | Sync Barrier |
| :--- | :--- | :--- | :--- | :--- |
| **LANE 1** | Web Platform & UI | `[FE]` | T001, T002, T003, T004, T006 | Unlocks T005 & T021 |
| **LANE 2** | Print & PDF/X Pipeline | `[OPS]` / `[E2E]` | T007, T008, T009, T010, T011, T013 | Unlocks T021 |
| **LANE 3** | Commercial Bundle & MoR | `[OPS]` / `[SEC]` | T014, T015, T016, T017 | Unlocks T021 |
| **LANE 4** | Business Plans Alignment | `[DOCS]` / `[SEC]` | T018, T019, T020 | Unlocks T021 |
| **LANE 5** | Quality Gates & Launch | `[E2E]` / `[SEC]` / `[SETUP]` | T005, T012, T021, T022, T023, T024, T025 | Final Gate |

---

## Agent Dispatch Summary

| Agent Tag | Specialist Role | Total Tasks | Task Identifiers |
| :--- | :--- | :---: | :--- |
| `[FE]` | frontend-specialist | 5 | T001, T002, T003, T004, T006 |
| `[OPS]` | devops-engineer | 7 | T005, T007, T008, T009, T013, T014, T016 |
| `[SEC]` | security-auditor | 4 | T012, T017, T020, T023 |
| `[E2E]` | test-engineer | 4 | T010, T011, T021, T022 |
| `[DOCS]` | documentation-writer | 3 | T015, T018, T019 |
| `[SETUP]` | orchestrator | 2 | T024, T025 |
| **Total** | | **25** | |
