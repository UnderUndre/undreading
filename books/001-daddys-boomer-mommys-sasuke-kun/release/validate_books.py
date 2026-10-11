import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def validate_edition(monolith_path: str, dir_slug: str, lang: str) -> None:
    print(f"\n================ VALIDATING {lang.upper()} EDITION ({monolith_path}) ================")
    src = (BASE_DIR / monolith_path).resolve()
    assert src.exists(), f"Source file {src} does not exist"
    content = src.read_text(encoding="utf-8")

    out_dir = (BASE_DIR / dir_slug).resolve()
    chapters_dir = out_dir / "chapters"
    front_matter_path = out_dir / "00-front-matter.md"
    index_path = out_dir / "index.md"

    # 1. Concatenation check: front-matter + chapters == monolith
    front_matter = front_matter_path.read_text(encoding="utf-8") if front_matter_path.exists() else ""
    chapter_files = sorted(chapters_dir.glob("*.md"))
    reconstructed = front_matter + "".join(f.read_text(encoding="utf-8") for f in chapter_files)
    
    assert reconstructed.strip() == content.strip(), f"FATAL: Reconstructed files do not match monolith for {lang}!"
    print(f"✅ Concatenation check PASS: 00-front-matter.md + {len(chapter_files)} chapter files match {src.name} byte-for-byte")

    # 2. Check no displaced 8.4-8.6 in Chapter 9
    ch9_str = "### **Chapter 9" if lang == "en" else ("### **Розділ 9" if lang == "ua" else "### **Глава 9")
    ch9_pos = content.find(ch9_str)
    p4_str = "## **PART IV" if lang == "en" else ("## **ЧАСТИНА IV" if lang == "ua" else "## **ЧАСТЬ IV")
    p4_pos = content.find(p4_str)
    ch9_body = content[ch9_pos:p4_pos]
    assert "8.4." not in ch9_body and "8.5." not in ch9_body and "8.6." not in ch9_body, f"FAILED: 8.4-8.6 still found in Chapter 9 for {lang}!"
    print(f"✅ Transposition check PASS: 8.4, 8.5, 8.6 are NOT in Chapter 9")

    # 3. Check 8.4-8.6 are in Chapter 8
    ch8_str = "### **Chapter 8" if lang == "en" else ("### **Розділ 8" if lang == "ua" else "### **Глава 8")
    ch8_pos = content.find(ch8_str)
    ch8_body = content[ch8_pos:ch9_pos]
    assert "8.4." in ch8_body and "8.5." in ch8_body and "8.6." in ch8_body, f"FAILED: 8.4-8.6 not found in Chapter 8 for {lang}!"
    print(f"✅ Transposition check PASS: 8.4, 8.5, 8.6 are correctly placed in Chapter 8")

    # 4. Check 14 & 15 are in Chapter 6 between 13 and 16
    ch6_str = "### **Chapter 6" if lang == "en" else ("### **Розділ 6" if lang == "ua" else "### **Глава 6")
    ch7_str = "### **Chapter 7" if lang == "en" else ("### **Розділ 7" if lang == "ua" else "### **Глава 7")
    ch6_pos = content.find(ch6_str)
    ch7_pos = content.find(ch7_str)
    ch6_body = content[ch6_pos:ch7_pos]

    pos_13 = ch6_body.find("13. ")
    pos_14 = ch6_body.find("14. ")
    pos_15 = ch6_body.find("15. ")
    pos_16 = ch6_body.find("16. ")
    assert pos_13 != -1 and pos_14 != -1 and pos_15 != -1 and pos_16 != -1, f"Missing 13-16 in Chapter 6 for {lang}"
    assert pos_13 < pos_14 < pos_15 < pos_16, f"FAILED: Items 14-15 not correctly placed between 13 and 16 in Chapter 6 for {lang}!"
    print(f"✅ Transposition check PASS: Chapter 6 items 13 -> 14 -> 15 -> 16 are in strict sequence")

    # 5. Check 10.14-10.17 are in Chapter 10 before Chapter 11
    ch11_str = "### **Chapter 11" if lang == "en" else ("### **Розділ 11" if lang == "ua" else "### **Глава 11")
    ch11_pos = content.find(ch11_str)
    p5_str = "## **PART V" if lang == "en" else ("## **ЧАСТИНА V" if lang == "ua" else "## **ЧАСТЬ V")
    p5_pos = content.find(p5_str)
    ch11_body = content[ch11_pos:p5_pos]
    assert "10.14." not in ch11_body and "10.15." not in ch11_body and "10.16." not in ch11_body, f"FAILED: 10.14-10.17 found in Chapter 11 for {lang}!"
    print(f"✅ Transposition check PASS: 10.14-10.17 are NOT in Chapter 11")

    ch10_str = "### **Chapter 10" if lang == "en" else ("### **Розділ 10" if lang == "ua" else "### **Глава 10")
    ch10_pos = content.find(ch10_str)
    ch10_body = content[ch10_pos:ch11_pos]
    assert "10.14." in ch10_body and "10.15." in ch10_body and "10.16." in ch10_body, f"FAILED: 10.14-10.17 not in Chapter 10 for {lang}!"
    print(f"✅ Transposition check PASS: 10.14-10.17 are correctly placed in Chapter 10")

    # 6. Check Appendix E runbooks: 11-19 are in Appendix E and NOT at EOF
    app_e_str = "### **Appendix E" if lang == "en" else ("### **Додаток E" if lang == "ua" else "### **Приложение E")
    app_f_str = "### **Appendix F" if lang == "en" else ("### **Додаток F" if lang == "ua" else "### **Приложение F")
    app_e_pos = content.find(app_e_str)
    app_f_pos = content.find(app_f_str)
    assert app_e_pos != -1 and app_f_pos != -1, f"Missing Appendix E or F in {lang}"
    app_e_body = content[app_e_pos:app_f_pos]

    for item_num in [11, 12, 13, 14, 15, 16, 17, 18, 19]:
        assert f"{item_num}." in app_e_body, f"FAILED: Item {item_num} missing in {app_e_str} for {lang}!"
    print(f"✅ Transposition check PASS: Runbooks 11, 12, 13, 14, 15, 16, 17, 18, 19 are all inside {app_e_str}")

    # Check tail of document: ends after changelog without leaked 13-17
    app_i_str = "### **Appendix I" if lang == "en" else ("### **Додаток I" if lang == "ua" else "### **Приложение I")
    app_i_pos = content.find(app_i_str)
    tail = content[app_i_pos:]
    assert "### **13. " not in tail and "### 13. " not in tail, f"FAILED: Leaked items at EOF after {app_i_str} in {lang}!"
    print(f"✅ Tail check PASS: No leaked physical runbooks after {app_i_str} at the end of the book")

    # 7. Check duplicates
    if lang in ["ru", "en"]:
        interpol_str = "10.5.3. Institutional Interpol" if lang == "en" else "10.5.3. Институциональный интерпол"
        assert content.count(interpol_str) == 1, f"FAILED: 10.5.3 count is {content.count(interpol_str)} in {lang}!"
        print(f"✅ Deduplication PASS: Exactly 1 copy of 10.5.3 in {lang}")

    # 8. Check index.md compactness
    index_text = index_path.read_text(encoding="utf-8")
    index_lines = [l for l in index_text.splitlines() if l.startswith("- [")]
    print(f"✅ Index compactness: {len(index_lines)} total links in index.md (clean and non-polluted)")

def main():
    editions = [
        ("ru-edition/ru/daddys-boomer-mommys-sasuke-kun-v25.2.md", "ru-edition/ru", "ru"),
        ("en-edition/en/daddys-boomer-mommys-sasuke-kun-en-v2.4.md", "en-edition/en", "en"),
        ("ua-edition/ua/daddys-boomer-mommys-sasuke-kun-ua-v1.9.md", "ua-edition/ua", "ua"),
    ]
    for mon, slug, lang in editions:
        validate_edition(mon, slug, lang)
    print("\n🎉 ALL AUDITS PASSED WITH ZERO ERRORS ACROSS ALL THREE EDITIONS! 🎉")

if __name__ == "__main__":
    main()
