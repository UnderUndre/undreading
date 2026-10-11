# Quickstart: Platform & Publishing Pipeline

**Feature**: `002-publishing-pipeline-and-platform`  
**Target Repo**: `undreading`

---

## 🚀 1. Prerequisites

```bash
# Node.js & npm/pnpm
node -v # >= 20.x
pnpm -v # >= 9.x

# Pandoc (EPUB 3 generation)
pandoc --version # >= 3.1.x

# Typst (Paperback 6"x9" PDF rendering)
typst --version # >= 0.11.x

# PDF Pre-Flight & ISO Validation
gs --version
cpdf -version
verapdf --version
```

---

## 📦 2. Build Commands

```bash
# 1. Full build of all artifacts (Docs, EPUB, Typst PDF, ZTA Kit)
npm run build

# 2. Build static Web Reader for undreading.com
npm run build:docs

# 3. Compile EPUB 3
npm run build:epub

# 4. Compile Typst Paperback PDF
npm run build:pdf

# 5. Split chapters and validate books integrity
npm run split:chapters
npm run validate:books
```
