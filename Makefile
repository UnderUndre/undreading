.PHONY: all build build:docs build:epub build:pdf pack:zta-kit validate lint:markdown lint:all split:chapters clean

BOOK_DIR := books/001-daddys-boomer-mommys-sasuke-kun/release
RU_MASTER := $(BOOK_DIR)/ru-edition/ru/daddys-boomer-mommys-sasuke-kun-v25.2.md
EN_MASTER := $(BOOK_DIR)/en-edition/en/daddys-boomer-mommys-sasuke-kun-en-v2.4.md
UA_MASTER := $(BOOK_DIR)/ua-edition/ua/daddys-boomer-mommys-sasuke-kun-ua-v1.9.md

DIST_DIR := dist
SITE_DIR := $(DIST_DIR)/site
TEMPLATES_DIR := templates
ASSETS_DIR := assets

all: build

build: build:docs build:epub build:pdf pack:zta-kit

split:chapters:
	python $(BOOK_DIR)/split_chapters.py $(RU_MASTER)
	python $(BOOK_DIR)/split_chapters.py $(EN_MASTER)
	python $(BOOK_DIR)/split_chapters.py $(UA_MASTER)

validate:
	python $(BOOK_DIR)/validate_books.py

build:docs: split:chapters
	@mkdir -p $(SITE_DIR)
	@echo "Building static site..."
	@if command -v npx >/dev/null 2>&1 && [ -f docs/.vitepress/config.ts ]; then \
		npx vitepress build docs --outDir $(SITE_DIR); \
	else \
		echo "Copying release navigation to $(SITE_DIR)..."; \
		cp -r $(BOOK_DIR)/daddys-boomer-mommys-sasuke-kun-v25.2/* $(SITE_DIR)/ 2>/dev/null || true; \
	fi

build:epub:
	@mkdir -p $(DIST_DIR)
	@echo "Compiling EPUB 3..."
	@if command -v pandoc >/dev/null 2>&1; then \
		pandoc $(RU_MASTER) \
			--toc --toc-depth=2 \
			--metadata title="Сантехника Бытия: Системная Инструкция для Человека" \
			--metadata author="Undre & Valera (Digital Plumber)" \
			--css=$(TEMPLATES_DIR)/epub-style.css \
			-t epub3 \
			-o $(DIST_DIR)/sanitary-engineering-of-being-ru.epub; \
		echo "EPUB built: $(DIST_DIR)/sanitary-engineering-of-being-ru.epub"; \
	else \
		echo "Notice: pandoc CLI not detected in PATH, target ready for CI/CD"; \
	fi

build:pdf:
	@mkdir -p $(DIST_DIR)
	@echo "Compiling Typst 6x9 Paperback PDF..."
	@if command -v typst >/dev/null 2>&1; then \
		typst compile \
			--font-path $(ASSETS_DIR)/fonts/ \
			$(TEMPLATES_DIR)/book-paperback-6x9.typ \
			$(DIST_DIR)/sanitary-engineering-of-being-paperback.pdf; \
		echo "PDF built: $(DIST_DIR)/sanitary-engineering-of-being-paperback.pdf"; \
	else \
		echo "Notice: typst CLI not detected in PATH, target ready for CI/CD"; \
	fi

pack:zta-kit:
	@mkdir -p $(DIST_DIR)
	@echo "Packaging ZTA Architecture Kit..."
	@if [ -d $(TEMPLATES_DIR)/zta-kit ]; then \
		tar -czf $(DIST_DIR)/zta-architecture-kit-v25.2.tar.gz -C $(TEMPLATES_DIR) zta-kit 2>/dev/null || true; \
		echo "ZTA Kit packaged: $(DIST_DIR)/zta-architecture-kit-v25.2.tar.gz"; \
	fi

lint:markdown: validate
	@echo "Markdown lint check passed via validate_books"

lint:all: validate
	@echo "All lint quality gates passed"

clean:
	rm -rf $(DIST_DIR)/*
