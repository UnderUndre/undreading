# 🗡️ Арт-дирекшн и дизайн обложки «Сантехника Бытия» (Cover Art Specification)

**Проект:** Монография «Сантехника Бытия: Архитектура суверенитета, телеметрии и выживания в эпоху цифрового хаоса»  
*(Daddy's Boomer, Mommy's Sasuke-kun)*  
**Формат:** Книга 6" × 9" (152.4 × 228.6 мм), Trade Paperback & eBook  
**Стандарт промпт-инжиниринга:** На базе `undreplans/docs/how-to-prompt-nano-banana-and-grok-imagine.md` (мультимодальный семантический граф для Nano Banana, авторегрессионный FRAME для Grok Imagine, чистый синтаксис для Flux и Midjourney).

---

## 1. Концепция центрального артефакта

### «Шиноби-Кунай Сантехника» (The Plumber's Kunai)
Центральный визуальный символ книги — гибридный тактический артефакт, объединяющий эстетику 4 ключевых культурных слоёв монографии:

1. **База из «Наруто» (Мамин Саске-кун):**
   - Силуэт классического метательного кинжала шиноби (кунай) с ромбовидным клинком двойной заточки.
   - Клинок выкован из тёмной вороненой дамасской стали с едва заметными слоистыми узорами ковки.
2. **Сантехнический твист (Папин Бумер / Валера):**
   - Вместо традиционного круглого кольца на навершии рукояти куная выкован **накидной гаечный ключ на 32 мм** (магистральный калибр для дюймовых сантехнических фитингов и накидных гаек стояка).
   - На ключе чёткая рельефная гравировка: `"32 CR-V"` (хром-ванадий).
3. **Слой «Ассасинов» (Assassin's Creed / Суверенное братство):**
   - Рукоять оплетена грубой потертой темно-коричневой кожей поверх скрытого наручного выдвижного механизма (пружины, скрытые заклепки и вороненые направляющие скрытого клинка).
   - В геометрию дола (центрального углубления клинка) лаконично вписан стилизованный треугольный силуэт ассасинского знака, переходящий в контур запорного вентиля.
4. **Слой «Ведьмака» (The Witcher / Школа Волка против системных чудовищ):**
   - Вдоль лезвия куная выгравированы **серебряные руны**, светящиеся мягким холодным неоновым светом (символы алхимических знаков Квен и Игни, переплетенные со схематическими знаками электрогидравлики: заземление `⏚`, диод, предохранитель и обратный клапан).
   - Вдоль режущей кромки видна линия хамона (ламинированная серебряная полоса: *«Сталь — для чугунных засоров, серебро — для левиафанов системы»*).

---

## 2. Цветовая палитра и атмосфера

- **Фоновый слой:** Глубокий матовый индустриальный графит (`#121316`), текстура мокрого бетона бомбоубежища или шероховатого чугуна.
- **Металл клинка:** Тяжёлая оружейная сталь холодного оттенка (`#2A2E35`) с зеркальной полировкой режущей кромки (`#E2E8F0`).
- **Свечение рун (Телеметрия / Чакра / Магия):** Холодный неоновый циан / ледяной аквамарин (`#00F2FE`) и контрастные теплые искры янтарно-оранжевого цвета (`#FF8C00`), символизирующие рабочее давление в магистрали.
- **Кожа и механика:** Состаренная темно-коричневая кожа Crazy Horse (`#3D271D`) с медными заклепками.

---

## 3. Промпты для генерации арта (Prompt Engineering Suite)

В соответствии с гайдом `how-to-prompt-nano-banana-and-grok-imagine.md` для каждой нейросети используется её родная архитектурная парадигма. Устаревшие баззворды 2022 года (`octane render`, `unreal engine 5`, `raytracing`, `8k resolution`, `hyperrealistic`) полностью исключены.

---

### 3.1. Промпт для Nano Banana (Google Gemini Image 2.5 / 3.1 Flash & Pro Image)

**Парадигма:** Мультимодальный семантический граф. Промпт оформляется как структурированный бриф арт-директора полными связными предложениями с физическим заземлением терминов и точным выделением текста в кавычках.

```text
[Format & Shot]: Vertical book cover composition with a 2:3 aspect ratio, macro product photograph, eye-level studio shot.
[Main Subject]: A hybrid tactical sovereign artifact: a forged steel ninja kunai dagger standing vertically. The circular pommel ring at the base of the handle is realistically sculpted into a heavy-duty size-32 metric box-end wrench.
[Blade & Details]: The diamond-shaped double-edged blade is forged from dark patterned Damascus steel, featuring laser-etched electro-hydraulic circuit schematics and alchemical runes that emit a soft cold cyan luminescence (#00F2FE). The central fuller subtly incorporates an angular assassin crest contour.
[Hilt & Materials]: The grip is tightly wrapped in battle-worn dark brown Crazy Horse leather cord over an oxidized steel mechanical sliding rail assembly with brass rivets.
[Text Integration]: The steel wrench pommel clearly features the embossed industrial text "32 CR-V" in sharp capital sans-serif lettering.
[Environment & Lighting]: Standing against a textured dark graphite wet concrete bunker surface. Directional cold cyan rim lighting combined with subtle warm amber sparks and atmospheric haze.
[Positive Constraints]: Sharp focus across all mechanical joints, authentic metallurgy, clean optical depth of field, strictly physically plausible tool geometry.
```

#### Мульти-тёрн итерация для Nano Banana (Conversational Patching)
Для точечной доработки сгенерированного изображения без сброса композиции используется диалоговый патч-промпт:

```text
Keep the exact dagger geometry, wrench pommel, leather grip wrapping, and concrete backdrop from the previous image, but increase the cold cyan luminescent glow inside the etched blade runes and ensure the stamped text "32 CR-V" on the wrench head is crisply legible and embossed.
```

---

### 3.2. Промпт для Grok Imagine (xAI Aurora Engine / Image 2.0)

**Парадигма:** Авторегрессионный Mixture-of-Experts трансформер. Порядок слов имеет критическое значение (первые 20–30 слов формируют геометрию). Используется фреймворк **FRAME** (Focus $\to$ Region $\to$ Angle/Optics $\to$ Mood/Light $\to$ Effect/Medium) с компактным объемом 45–55 слов и ~60% веса на свет и оптику. Полный запрет на отрицательные частицы.

```text
A heavy tactical forged Damascus steel kunai dagger standing vertically, featuring a 32mm chrome-vanadium box-end wrench forged into its pommel with crisp stamped "32 CR-V" text. Wrapped in dark brown distressed leather cord over steel mechanical rails. Glowing electric-cyan alchemical runes etched into the blade. Macro 85mm lens at f/2.8, vertical book cover composition. Scratched wet slate background, cold cyan rim light, subtle warm amber sparks, tactile steel grain, raw studio photograph.
```

#### Команда редактирования для Grok Imagine (Lead-with-Change Patch)
```text
Maintain the exact weapon silhouette, lighting, and slate background, but make the engraved alchemical runes on the blade emit a more intense cyan glow.
```

---

### 3.3. Промпт для Flux.1 Pro / Dev

**Парадигма:** Текстовая диффузия с высоким пониманием точных надписей в кавычках. Фронт-лоадинг главного объекта и чистая фактура металлургии.

```text
Macro eye-level studio photograph of a tactical ninja kunai dagger standing vertically on scratched dark slate. The ring pommel at the bottom of the handle is forged as a heavy-duty chrome-vanadium 32mm box-end pipe wrench with stamped "32 CR-V" text. The dark Damascus steel blade features etched Witcher alchemical runes glowing with cold cyan neon light, and an angular assassin crest in the fuller. The hilt is tightly wrapped in distressed dark brown leather cord over mechanical steel sliding rails. Directional cold blue rim light, subtle warm amber sparks, high optical sharpness, cinematic depth of field.
```

---

### 3.4. Промпт для Midjourney v6.1

**Парадигма:** Художественная стилизация с кинематографическим светом, соотношением сторон `--ar 2:3` и параметром `--style raw` для подавления перенасыщенного CGI-блеска.

```text
A masterfully forged hybrid tactical kunai dagger standing vertically in dramatic cinematic lighting, the circular pommel ring at the base of the handle is realistically sculpted into a heavy steel size-32 metric wrench spanner with embossed "32 CR-V" text. The double-edged diamond blade is forged from dark Damascus steel, inlaid with glowing silver alchemical runes emitting a soft cold cyan luminescence. The hilt is wrapped in battle-worn dark brown leather over a brass hidden-blade mechanical assembly. Dark industrial moody background, wet concrete bunker texture, subtle atmospheric smoke and orange hydraulic spark embers, macro 85mm product photography, studio rim lighting, cinematic poster composition --ar 2:3 --v 6.1 --style raw --q 2
```

---

### 3.5. Принцип позитивного описания (Positive Framing vs Negative Prompts)

По результатам исследований `how-to-prompt-nano-banana-and-grok-imagine.md`, классические блоки негативных промптов (`--no plastic, rust, blur`) в современных моделях вызывают **Negative Token Placebo**:
- В авторегрессионных моделях (Grok Imagine / Aurora) отрицания вроде `"no plastic"` активируют эмбеддинги слова `plastic`, провоцируя появление дешёвой пластмассы.
- Мультимодальные модели (Nano Banana / Gemini) игнорируют слепые списки табу-слов, если они не заземлены в семантическом описании сцены.

Вместо негативных промптов используется **позитивная физическая конкретизация**:
- Вместо *«no plastic, no cheap 3d render»* $\to$ `heavy industrial-grade chrome-vanadium tool steel, crisp CNC machining, authentic Damascus folding layers, tactile cold-rolled metallic finish`.
- Вместо *«no blur, no low quality»* $\to$ `macro 85mm lens at f/2.8, optical depth of field, tack-sharp mechanical edges`.
- Вместо *«no rust»* $\to$ `clean oiled gunmetal finish, pristine polished bevels`.

---

### 3.6. Сводная матрица архитектуры промптов (Prompt Architecture Matrix)

| Параметр | Nano Banana (Gemini 2.5/3.1) | Grok Imagine (Aurora) | Flux.1 Pro | Midjourney v6.1 |
| :--- | :--- | :--- | :--- | :--- |
| **Синтаксис** | Структурированный бриф / связный текст | Фреймворк FRAME | Дескриптивное описание | Художественный кинематографический |
| **Фронт-лоадинг** | Блочный (`[Main Subject]`) | Строгий (первые 20 слов) | Высокий | Умеренный |
| **Объем текста** | 80–120 слов | 45–55 слов | 60–80 слов | 70–90 слов |
| **Рендер текста** | Строгие двойные кавычки `"32 CR-V"` | Кавычки в начале промпта | Двойные кавычки | Двойные кавычки |
| **Работа со светом** | Физические параметры (`#00F2FE`) | ~60% веса на свет и оптику | Направленные rim-light | Кинематографический moody |
| **Протокол правок** | Мульти-тёрн диалог (Conversational) | Lead-with-Change команда | Перегенерация сида | Вариации / Region Inpainting |

---

## 4. Тексты для задней обложки (Back Cover Blurbs)

### 🇷🇺 Русский вариант (Голос Валеры — Цифровой Сантехник)

```text
У ТЕБЯ ТЕЧЁТ ПОДВАЛ, А ТЫ СМОТРИШЬ В ТЕЛЕФОН.

Большинство людей искренне верят, что государство защитит их права, банк спасёт сбережения, а медицина позаботится о здоровье. В реальности современный мир — это аварийная многоэтажка с гнилыми стояками. Стоит сорвать хотя бы один вентиль — налоговый рейд, блокировку счетов по 115-ФЗ, ночную адренергическую аритмию или потерю доступа к мастер-аккаунту — и неподготовленного человека смывает в отстойник за 48 часов.

«Сантехника Бытия» — это не инфобизнес и не селф-хелп. Это бескомпромиссная системная инструкция по сборке автономного суверенитета на 5 эшелонах обороны:

• L1 (ЖИЗНЬ): От протокола декомпрессии MARCH-PAWS до чистки плазмы от микропластика и стоматологического моста Cavit в полночь;
• L2 (СВОБОДА): От аппаратного сплита GrapheneOS до деконструкции СОРМ-3, отсечения рекламных шпионов и протокола «Чистого кирпича» против нацмессенджеров;
• L3 (КАПИТАЛ): От суверенного SDLC и юнит-экономики самиздата до обхода капкана 40% налога на наследство в США и защиты от дропперов;
• L4 (ПРАВО): От отмены судебных приказов ЖКХ за 10 дней и защиты кода по ст. 1295 ГК РФ до глобального налогового коллектора 14 стран СНГ и Бананового Оверрайда;
• L5 (ЖЕЛЕЗО): От LiFePO4-автаркии при блэкауте до предотвращения BLEVE-взрывов бойлеров и анти-сифонных затворов RPZ.

Физику не наебёшь, а систему не починишь абстрактными мантрами. Затягивай гайки сейчас — пока не сорвало резьбу.

[ ЗОНА ШТРИХКОДА KDP / LULU: 2.0" × 1.2" ]
```

---

### 🇬🇧 English Edition (Bob the Gray — Infrastructure Plumber)

```text
YOUR BASEMENT IS FLOODING, AND YOU'RE STARING AT YOUR PHONE.

The modern normie blindly trusts that institutions safeguard their liberty, banks shield their capital, and sovereign borders guarantee due process. In reality, civilization is a deteriorating high-rise with calcified risers and over-pressurized joints. When a systemic valve fails—a warrantless bank freeze, an algorithmic account nuke, a sudden cross-border tax audit, or a critical nocturnal arrhythmia—unhardened citizens are flushed into the municipal sewer within 48 hours.

THE PLUMBING OF BEING is neither corporate self-help nor philosophical filler. It is an uncompromised, battle-tested operational blueprint engineering five echelons of personal sovereignty:

• L1 (LIFE): From TCCC MARCH-PAWS tourniquet telemetry to ApoB lipidology, microplastics plasma clearance, and midnight dental triage;
• L2 (LIBERTY): From hardware GrapheneOS airgaps to FISA 702 deconstruction, push-gateway isolation, and counter-surveillance against state spyware;
• L3 (RESOURCES): From sovereign SDLC economics to dodging the US 40% NRA estate tax trap, Mastercard MATCH blacklists, and Coasean firm architecture;
• L4 (SOVEREIGNTY): From defeating ex parte Mareva freezing injunctions to the Anglo-Saxon fiscal water hammer across 6 first-world nations and the Clean Cut Rule;
• L5 (HARDWARE): From LiFePO4 battery autarky under blackouts to BLEVE boiler explosion mitigation and backflow RPZ hydraulic isolation.

You cannot cheat physics, and you cannot patch infrastructure with wishful thinking. Tighten the fittings now—before the pressure shears the threads.

[ KDP / BARCODE CLEARANCE BOX: 2.0" × 1.2" ]
```

---

### 🇺🇦 Українське видання (Дядя Толя / Майстер Василь)

```text
У ТЕБЕ ТЕЧЕ ПІДВАЛ, А ТИ ДИВИШСЯ В ТЕЛЕФОН.

Більшість людей щиро переконані, що держава подбає про їхній захист, банк збереже заощадження, а система вбереже родину. У суворій реальності сучасний світ — це аварійна теплотраса під тиском у двадцятиградусний мороз. Варто свиснути одній прокладці — свавільне затримання на вулиці, блокування рахунку за фінмоніторингом, ракетний блекаут або нічна фібриляція — і непідготовлену людину зносить у колектор за лічені хвилини.

«Сантехніка Буття» — це безкомпромісна інженерна інструкція з монтажу персональної автономії на 5 ешелонах захисту:

• L1 (ЖИТТЯ): Від джгутів СІЧ/Дніпро та гемостатиків Кровоспас до шкали МОЗОК, антидоту NAC та протоколу зависання у страхувальній прив'язі;
• L2 (СВОБОДА): Від апаратної ізоляції Дії та BankID до протидії Cellebrite BFU/AFU за ст. 264-2 КПК, Signal Sealed Sender та «Паляниця-SafeWord»;
• L3 (КАПІТАЛ): Від чистої гідравліки ФОП 3-ї групи та Дія.City до валютного контролю НБУ № 18, банківського захисту за ст. 1074 ЦКУ та контрактів 40/40/20;
• L4 (ПРАВО): Від процесуального розвідного ключа ст. 206 КПК проти свавілля ТЦК до захисту єдиного житла за ст. 131 КУзПБ та 5 державних реєстрів;
• L5 (ЗАЛІЗО): Від LiFePO4 блекаут-енергетики та захисту від відгорання нуля 380В до зворотних каналізаційних засувок EN 12056-4.

Фізику не наїбеш, а систему не полагодиш порожніми гаслами. Закручуй гайки зараз — поки не зірвало різьбу.

[ ЗОНА ШТРИХКОДУ: 2.0" × 1.2" ]
```

---

## 5. Геометрическая развёртка полной печатной обложки (KDP Full Wrap)

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        РАЗВЁРТКА ОБЛОЖКИ 6" × 9" (FULL SPREAD)                         │
├────────────────────┬─────────────────────────────┬─────────────────────────────────────┤
│   BACK COVER (6")  │      SPINE (1.036")         │          FRONT COVER (6")           │
│                    │                             │                                     │
│  [Текст аннотации  │  САНТЕХНИКА БЫТИЯ           │     САНТЕХНИКА БЫТИЯ                │
│   для задника      │                             │     Архитектура суверенитета,       │
│   (Back Blurb)]    │  Undre & Валера             │     телеметрии и выживания...       │
│                    │                             │                                     │
│                    │  [Логотип Undrlla           │     [КУНАЙ-КЛЮЧ НА 32 С РУНАМИ]     │
│                    │   в основании]              │                                     │
│         [ШТРИХКОД] │                             │                                     │
│         2.0"×1.2"  │                             │     Undre & Валера                  │
└────────────────────┴─────────────────────────────┴─────────────────────────────────────┘
 ◄── Bleed 0.125" ──►                               ◄── Bleed 0.125" ──►
 Общая ширина развёртки: 0.125" + 6.000" + 1.036" + 6.000" + 0.125" = 13.286" (337.5 мм)
 Общая высота развёртки: 0.125" + 9.000" + 0.125" = 9.250" (235.0 мм)
```
