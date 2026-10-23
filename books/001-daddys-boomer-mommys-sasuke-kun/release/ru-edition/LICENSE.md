# Лицензирование проекта / Project Licensing

Данный репозиторий использует раздельное лицензирование (Dual / Split Licensing) для контента книги и исполняемого программного кода:

---

## 1. Текст книги, монографии и документация (`books/`, `docs/`)

Весь текстовый и графический контент книги «Сантехника бытия» (включая все издания, переводы и сопутствующие материалы), находящийся в директории `books/` (а также любые материалы документации в `docs/`), распространяется под международной лицензией **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**.

* **Вы можете:** свободно читать, скачивать, форкать, сохранять локально и делиться данным материалом в некоммерческих целях при условии обязательного указания авторства (Undre).
* **Запрещено:** коммерческое использование (продажа текста, включение в платные курсы, продажа электронных или печатных копий на маркетплейсах), а также распространение производных/измененных версий (переделок) текста без прямого письменного согласия автора.
* **Исключительные права коммерческой дистрибуции:** Публикация и продажа официальных версий в PDF, EPUB, а также физических печатных изданий (Paperback Print-on-Demand на Amazon KDP и других площадках) на 100% сохраняются за автором.

Полный юридический текст лицензии:  
https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode

`SPDX-License-Identifier: CC-BY-NC-ND-4.0`

---

## 2. Исходный код, веб-ридер, скрипты сборки и утилиты (`scripts/`, кодовая база)

Весь исполняемый программный код веб-ридера, скрипты автоматизации сборки (Pandoc/Typst/Makefile/Bash/Python/CI) и примеры кода, находящиеся в директории `scripts/`, а также в корневых файлах интерфейса, распространяются под лицензией **MIT License**:

Copyright (c) 2022 John Factotum (Foliate-js core reader engine)  
Copyright (c) 2026 Undre (Custom extensions, build pipeline, and monograph integration)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

`SPDX-License-Identifier: MIT`

---

## 3. Сторонние библиотеки (Vendored Libraries)

* **zip.js** ([github.com/gildas-lormeau/zip.js](https://github.com/gildas-lormeau/zip.js)) — лицензия BSD-3-Clause.
* **fflate** ([github.com/101arrowz/fflate](https://github.com/101arrowz/fflate)) — лицензия MIT.
* **PDF.js** ([mozilla.github.io/pdf.js/](https://mozilla.github.io/pdf.js/)) — лицензия Apache-2.0.
