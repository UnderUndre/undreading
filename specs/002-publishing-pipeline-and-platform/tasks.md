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

- [ ] T001 [FE] Initialize VitePress 1.x documentation site under `docs/` with chapter routing for all 9 editions (RU/EN/UA)
- [ ] T002 [FE] Implement landing page `docs/index.md` with Executive TL;DR, 5 Echelons overview, and interactive 110-valve P0 Matrix jump
- [ ] T003 [FE] Implement custom CSS theme presets («Свиток Шиноби», «Терминал Убежища CRT-3000»)
- [ ] T004 [FE] Add non-intrusive callout banner on web chapters with link to Supporter & ZTA Architecture Kit ($12.99 PWYW)
- [ ] T005 [OPS] Configure Cloudflare Pages automated deployment pipeline with custom domain `undreading.com`
- [ ] T006 [FE] Implement PWA Service Worker for offline in-browser reading cache

---

## Phase 2: EPUB 3 & Multi-Vendor Print Production Pipeline

**Goal**: Seamless offline reading on e-readers and physical print-on-demand via Amazon KDP, Lulu, and IngramSpark.

- [ ] T007 [OPS] Automate Pandoc compilation script for EPUB 3 generation with cover image, styling, and metadata
- [ ] T008 [OPS] Develop multi-vendor cover geometry engine `scripts/generate-covers.py` with spine calculation formulas (KDP, Ingram, Lulu)
- [ ] T009 [OPS] Build two-stage PDF/X-1a transcoding script `scripts/transcode-pdfx1a.sh` using Ghostscript and `cpdf` (FOGRA39 / DeviceGray 100% K)
- [ ] T010 [E2E] Develop automated pre-flight quality verification script `scripts/validate-print-pdf.sh` integrating `veraPDF` ISO 15930-1 validation
- [ ] T011 [E2E] Validate generated EPUB 3 files via `epubcheck` (0 errors, 0 warnings)
- [ ] T012 [SEC] Verify Amazon KDP account settings: Paperback PoD only ($24.99), Payoneer US ACH payout, Form W-8BEN 0% withholding
- [ ] T013 [OPS] Setup Lulu Print API webhook integration for Russian paperback dropshipping ($24.99, margin 64.2%)

---

## Phase 3: Supporter & ZTA Architecture Kit Packaging (Paddle MoR)

**Goal**: Commercial processing of the software bundle under NACE 62.01 with 1% tax protection and secure digital delivery.

- [ ] T014 [OPS] Assemble ZTA Architecture Kit bundle structure in `templates/zta-kit/` (Terraform, Docker Compose, Traefik v3 SSL, WireGuard)
- [ ] T015 [DOCS] Include Markdown templates in ZTA Kit: Decision Journal Type 1, 8-Point CPA LLC Checklist, Emergency 03:00 Runbook
- [ ] T016 [OPS] Automate packaging script producing `dist/zta-architecture-kit-v25.2.zip`
- [ ] T017 [SEC] Configure and verify Paddle MoR product descriptor (*"ZTA Security Architecture Specification & Infrastructure Implementation Kit (NACE 62.01)"*) and Cloudflare R2 24h Signed URLs

---

## Phase 4: Expat Marketplace & Ecosystem Business Plans Sync

**Goal**: Align `undreseller` and `undrlla` master business plans with released book editions and platform architecture.

- [ ] T018 [DOCS] Update `undreplans/docs/projects/undreseller/undreseller-business-plan.md` with Expat Refurbished Marketplace model
- [ ] T019 [DOCS] Update `undreplans/docs/projects/undrlla/undrlla-business-plan.md` with 7-node project topology and utility return model
- [ ] T020 [SEC] Verify unit economics, margin floors (>88%), and GAAR compliance across all business plans

---

## Phase 5: Final Quality Gates & Public Launch

**Goal**: End-to-end build verification, snapshotting, and public launch.

- [ ] T021 [E2E] Run complete build pipeline `npm run build` and verify all artifacts in `dist/`
- [ ] T022 [SEC] Perform constitution compliance check against all principles
- [ ] T023 [DOCS] Update release notes, changelog, and documentation index
- [ ] T024 [SETUP] Tag stage snapshot `snapshot-stage platform-launch 002-publishing-pipeline-and-platform`
