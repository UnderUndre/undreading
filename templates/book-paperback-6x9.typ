// ==============================================================================
// Typst Template: Amazon KDP & Multi-Vendor Print-on-Demand (6" x 9" Trade Paperback)
// Specification: 152.4mm x 228.6mm (6.000" x 9.000"), No-Bleed Interior
// Gutter: 0.875" (22.2mm) for perfect-bound book (>400 pages)
// Outer Margin: 0.625" (15.9mm), Top/Bottom: 0.750" (19.0mm)
// Color Profile: 100% DeviceGray / Pure Black (Zero Rich Black)
// ==============================================================================

#set document(
  title: "Сантехника Бытия: Системная Инструкция для Человека",
  author: ("Undre", "Valera (Digital Plumber)"),
)

// 6x9 Trade Paperback Dimensions
#set page(
  paper: "us-trade", // 6" x 9" (152.4mm x 228.6mm)
  margin: (
    inside: 22.2mm,  // 0.875" inner gutter
    outside: 15.9mm, // 0.625" outer margin
    top: 19.0mm,     // 0.750" top margin
    bottom: 19.0mm,  // 0.750" bottom margin
  ),
  header: locate(loc => {
    let page-num = counter(page).at(loc).first()
    if page-num > 2 {
      if calc.even(page-num) {
        align(left, text(size: 8pt, fill: luma(60), font: "PT Serif")[Сантехника Бытия: Системная Инструкция для Человека])
      } else {
        align(right, text(size: 8pt, fill: luma(60), font: "PT Serif")[Undre & Valera])
      }
    }
  }),
  footer: locate(loc => {
    let page-num = counter(page).at(loc).first()
    if page-num > 2 {
      if calc.even(page-num) {
        align(left, text(size: 9pt, font: "PT Serif")[#page-num])
      } else {
        align(right, text(size: 9pt, font: "PT Serif")[#page-num])
      }
    }
  }),
)

// Base Typography
#set text(
  font: ("PT Serif", "Liberation Serif", "Linux Libertine", "Times New Roman"),
  size: 10pt,
  fill: luma(0), // 100% K / pure black
  lang: "ru",
  spacing: 120%,
)

#set par(
  justify: true,
  leading: 0.65em,
  first-line-indent: 1.25em,
)

// Heading formatting
#show heading.where(level: 1): it => {
  pagebreak(weak: true, to: "odd") // Recto chapter opening
  v(2cm)
  text(size: 18pt, weight: "bold", font: ("PT Sans", "Liberation Sans", "Arial"))[#it.body]
  v(1cm)
}

#show heading.where(level: 2): it => {
  pagebreak(weak: true, to: "odd") // Part opening
  v(1.5cm)
  text(size: 15pt, weight: "bold", font: ("PT Sans", "Liberation Sans", "Arial"))[#it.body]
  v(0.8cm)
}

#show heading.where(level: 3): it => {
  v(1cm)
  text(size: 12pt, weight: "bold", font: ("PT Sans", "Liberation Sans", "Arial"))[#it.body]
  v(0.5cm)
}

#show heading.where(level: 4): it => {
  v(0.6cm)
  text(size: 10.5pt, weight: "bold")[#it.body]
  v(0.3cm)
}

// Blockquotes styling
#show quote: it => {
  rect(
    width: 100%,
    stroke: (left: 2pt + luma(80)),
    inset: (left: 10pt, top: 6pt, bottom: 6pt, right: 6pt),
    fill: luma(250),
    text(style: "italic", size: 9.5pt)[#it.body]
  )
}

// Code blocks styling (monospace, max 68 chars per line)
#show raw: set text(font: ("DejaVu Sans Mono", "Liberation Mono", "Courier New"), size: 8pt)
#show raw.where(block: true): it => {
  rect(
    width: 100%,
    stroke: 0.5pt + luma(120),
    fill: luma(248),
    inset: 8pt,
    radius: 2pt,
    it
  )
}

// Tables styling
#show table: set text(size: 8.5pt)

// Amazon KDP Factory Barcode Protocol: blank terminal verso page
#let kdp-terminal-page() = {
  pagebreak(weak: true, to: "even")
  v(50%)
  align(center, text(size: 7pt, fill: luma(180))[/* Intentionally blank for Amazon KDP barcode */])
}

// Entrypoint content hook
#let book-content(body) = {
  body
  kdp-terminal-page()
}
