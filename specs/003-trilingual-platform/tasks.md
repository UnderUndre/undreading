# Tasks: Undreading Trilingual Open Publishing Platform & Store

**Input**: Design documents from `specs/003-trilingual-platform/` (`spec.md`, `plan.md`)  
**Prerequisites**: `spec.md`, `plan.md`  
**Status**: Ready for execution  

---

## Phase 1: Setup & SSG Infrastructure

- [ ] `T-001` `[SETUP]` Initialize VitePress SSG setup and install dependencies (`package.json`, `@vitepress/client`, `idb-keyval`, `tailwindcss`)
- [ ] `T-002` `[FE]` Configure `docs/.vitepress/config.mts` with i18n locales (`/ru/`, `/en/`, `/ua/`), multi-language sidebar navigation and search
- [ ] `T-003` `[OPS]` Create automated build script `scripts/sync-release-to-docs.py` that parses `release/*.md` files and exports chapter Markdown files into `docs/ru/`, `docs/en/`, `docs/ua/`

---

## Phase 2: User Story 1 - Instant Trilingual Web Reader & P0 Matrix (Priority: P1)

- [ ] `T-004` `[FE]` `[US1]` Develop interactive 86-valve matrix component `docs/.vitepress/theme/P0MatrixWidget.vue` with layer filters (L1–L5) and instant jump anchors
- [ ] `T-005` `[FE]` `[US1]` Implement reading toolbar: font size slider (14–22px), theme switcher (Dark, Sepia, Light), reading progress indicator
- [ ] `T-006` `[FE]` `[US1]` Configure PWA Service Worker via Workbox for offline chapter caching in IndexedDB
- [ ] `T-007` `[FE]` `[US1]` Style custom callout blocks (`[Факт L1]`, `[Спека L2]`, `[Перевод с русского на русский]`) in `docs/.vitepress/theme/style.css`

---

## Phase 3: User Story 2 - Supporter & ZTA Kit Checkout (Priority: P2)

- [ ] `T-008` `[FE]` `[US2]` Design and build `/buy` page (`docs/buy.md`) with Pay-What-You-Want tier selector ($5 min / $12.99 rec / $50+ sponsor)
- [ ] `T-009` `[FE]` `[US2]` Integrate client-side `Paddle.js` overlay checkout with sandbox/production environment switching
- [ ] `T-010` `[BE]` `[US2]` Implement Cloudflare Function `functions/api/download/generate-token.ts` for signing temporary Cloudflare R2 download links for EPUB 3, Typst PDF, and ZTA code archive

---

## Phase 4: User Story 3 - Automated DTC Print-on-Demand via Lulu (Priority: P3)

- [ ] `T-011` `[FE]` `[US3]` Build `/print` page (`docs/print.md`) with interactive international shipping estimator and book preview 3D render
- [ ] `T-012` `[BE]` `[US3]` Implement Cloudflare Function `functions/api/shipping/calculate.ts` calling Lulu API `/print-job-cost-calculations/`
- [ ] `T-013` `[BE]` `[US3]` Implement Paddle Webhook listener in `functions/api/webhooks/paddle.ts` validating Paddle signatures and queuing print orders to Lulu Print API v4
- [ ] `T-014` `[OPS]` `[US3]` Build Typst compilation script `scripts/build-typst-pdf.sh` for generating production-ready PDF 6"x9" interiors and covers for Lulu & KDP

---

## Phase 5: User Story 4 - Amazon Prime Outbound & B2B Cross-Links (Priority: P4)

- [ ] `T-015` `[FE]` `[US4]` Add Amazon.com Prime outbound buy buttons for English and Ukrainian editions on `/print`
- [ ] `T-016` `[FE]` `[US4]` Embed native B2B audit CTA banners across technical chapters linking into `underundre.com` Tripwire SpecKit

---

## Phase 6: Quality Validation & Verification

- [ ] `T-017` `[FE]` Validate build output (`npm run build:docs`) and verify zero broken links in VitePress routing
- [ ] `T-018` `[E2E]` Run Playwright automated E2E test verifying reading navigation across RU, EN, UA and P0-matrix anchor jumps
