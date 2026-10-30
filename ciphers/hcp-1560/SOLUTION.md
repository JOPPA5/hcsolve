# HCP1560 / pc_hcp_241 — complete known-key reading (round 2, after review 1)

**Current claim: see "Current solution (round 2)" at the end of this file.** It supersedes the
round-1 sections below, which are kept unchanged as history. Those sections describe an earlier
*partial* state (509 units, three opaque spans, BICH/BIL/LISOVAL) that review 1 corrected. The
current transcription is `work/transcription-r2.txt`, decoded by `work/decode2.py`: 514 cipher
units, 521 letters, no opaque span, 5 damaged-but-read signs.

## Round-1 record (historical, superseded)


Manual solver candidate for root QA, **not an accepted or complete decipherment**. All 15 visible cipher rows are represented. There are **509 known cipher units / 516 known base letters / seven CH units**, plus three ink spans of unasserted length. The total original cipher-unit count and percentage coverage are unknown.

## Sources, scope and attribution

Root captured rendered General, Description and Attachments: Czech postcard, 17 March 1903, recipient Anna Tichá, status Not solved, no attached target transcription or solution. Its current captured register observation is 337 contributions / 303 HC IDs, this target absent. These are bounded observations, not a worldwide novelty claim. The current explicit exclusions file has no 1560 entry; no submission or discovery credit is asserted here. Original source files and `SOURCES.md` remain immutable.

The family key from `ciphers/hcp-1520/work/key.json`, the preserved published partial Anna Tichá research/key, the photographic pc199 reference and expanded public work on other cards were available before this transcription and are credited in `SOURCES.md`. This is **known-key transfer**, not independent key discovery or blind review. No target-specific plaintext was supplied or consulted. Photographic pc199 was available as a reference; no new rare-F identification is needed here, because the target has no confidently transcribed use of that class.

Both original faces and all margins were inspected. The picture must be rotated **90° clockwise**, losslessly, giving the native upright 674×1024 image. R01–R12 occupy the upper field; R09 begins to the right of the printed **FORTE**. R13–R15 are the three shorter ending/signature rows on the right. No detached marginal cipher was found. `FORTE`, the illustration and the gray collection watermark are ordinary print/overprint, not cipher units.

The picture-side date reads **17.III.1903**, ordinary numerals. The address reads **Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek**. Diagonal strokes cross the destination area and a lower-left addition reads **v Kamenici nad Lipou**. These are ordinary address alterations; no reason, forwarding history or sender identity is inferred. Postal headings, stamp, postmarks and printer code are outside the cipher. Exact postmark dates are not asserted. Full field inventory is in `work/field-inventory.json`.

## Fixed key and manual record

Shape labels are mnemonics rather than literal Latin characters on the postcard. `H` labels the special capped h-family **CH** unit. Ordinary `h`/R and `r`/H remain distinct. Tall-looped `f` is V; shallow `v` is F and is unused here. The fixed table has no G plaintext value; none is invented.

| Cipher labels | Plaintext units |
|---|---|
| `1 2 3 4 5 6 8` | `Y U O I E A L` |
| `q g f h t r c s` | `Z K V R D H S C` |
| `n m p b d y H v` | `M N B P T J CH F` |

Twenty-two of 23 fixed classes are used. No key change was made to improve grammar. Source `4`/I is retained in **BICH** (R08/R09/R10) and **BIL** (R08); editorial *bych/byl* is separate. Same-card controls compare these with I in DIK and Y in VYHOVETI/DLOUHYCH. The initial q/Z in ZANETU has an open terminal hook, like ZA/ZPRAVOU; g/K in LISTEK/CHRIPKA has a long returning loop. It was decided by those shapes, not the expected word. R02 VSAK uses round c/S.

`rows.json` records orientation, native row-context boxes, all label strings and tokens. `positions.json` assigns every known glyph a global **known-glyph index**, row-known ordinal and text column. Those are not measured per-glyph image coordinates, and after unknown-length spans they are **not original absolute cipher positions**. Raw nearest-neighbor crops R01–R15 and three indexed panels locate the rows. Context rectangles may include adjacent ascenders/descenders; they are not exclusive glyph segmentation. R09's final crop starts at native x244 and includes the full U TEBE, rather than clipping its first signs.

## Exact literal base-letter reading

Word spacing, punctuation and row division are manually represented. Unknown markers are opaque, not letters or presumed single units. Accents are not restored in this layer.

```text
SRDECKO MOJE ROZMILE, TISICERY DIK ZA DRAHY LISTEK
TVUJ. ZARMOUTIL JSEM SE, VSAK VELICE ZPRAVOU, ZE MOJE JEDINA,
VRELE MILOVANA ANUNKA JE OPET TAK CHURAVA ZE ⟦U1⟧ELA U-
LEHNOUTI. MUSIS SE DRAHOUSKU, VZHLEDEM K TOMU, ZE BYLA
JSI JIZ LETOS VAZNE S NEBEZPECIM ZANETU PLIC CHURAVA,
CO NEJDRIVE A CO NEJVICE SETRITI. CHRIPKA J⟦U2⟧ ZAKERNA
NEMOC, JEZ SE NESMI PODCENOVATI A JIZ JEST NEJLEPE
IHNED V POCATKU VYHOVETI. KEZ BICH BIL, ZLATO MOJE
U TEBE! PRIVINUL BICH TE TAKTO VRELE
K SOBE ⟦U3⟧ TAK DLOUHO BICH TE VASNIVE LISOVAL, AZ BY
ANUNKA REKLA, ZE JIZ JE UPLNE ZDRAVA. PROSIM O
BRZKOU ZPRAVU, JAK SE MEMU SRDECKU DARI, ANO?
TISIC DLOUHYCH PUS POSI-
LA VECNE TVUJ
PEPOUS.
```

## Unresolved ink and source limits

| ID | Location / native upright context box | Retained evidence and limit |
|---|---|---|
| U1 | R03 `[532,80,568,113]` | Blotted prefix after clear q5 and before clear 586, hence `ZE ⟦U1⟧ELA`. Sequence and length unasserted. Context may suggest *musela*, but that is not the decoded prefix. |
| U2 | R06 `[514,160,536,193]` | Blotted span after clear y/J and before clear q6g5hm6/ZAKERNA. Sequence and length unasserted. Completing J… as *je* is editorial. |
| U3 | R10 `[137,262,163,293]` | Heavy ink between SOBE and TAK over printed halftone. It may conceal cipher signs, punctuation, correction or no additional active unit. No cancellation, missing word or unit count is asserted. |

These are context boxes, not exact segmentation of overlapping ink. `uncertainties.json` preserves all lengths as null. No span is silently counted as one symbol. No total or coverage percentage can follow from the 509 known units. No active letter is assigned beneath the blots. R11/R12 left-side words over halftone are transcribed from visible stems/loops and remain appropriate places for root visual checking. Larger scans or physical-card inspection could change individual classifications.

Seven transcribed capped units expand to CH; the remaining small accent-like marks have not been established as an encoded diacritic system. Restoring Czech accents below does not prove their source ownership. The decoded signature PEPOUS does not establish a civil identity.

## Editorial Czech reading

Accents, joined line endings and paragraphing are editorial. Every I→Y repair and possible ink completion is marked. Proposed words inside brackets do not set the length of the unknown source spans.

Srdéčko moje rozmilé, tisícerý dík za drahý lístek tvůj. Zarmoutil jsem se však velice zprávou, že moje jediná, vřele milovaná Anunka je opět tak churavá, že **[snad musela; doslova ⟦U1⟧ELA]** ulehnouti. Musíš se, drahoušku, vzhledem k tomu, že byla jsi již letos vážně s nebezpečím zánětu plic churavá, co nejdříve a co nejvíce šetřiti. Chřipka **[snad je; J⟦U2⟧]** zákeřná nemoc, jež se nesmí podceňovati a jíž jest nejlépe ihned v počátku vyhověti.

Kéž bych **[BICH]** byl **[BIL]**, zlato moje, u tebe! Přivinul bych **[BICH]** tě takto vřele k sobě **⟦U3⟧**, tak dlouho bych **[BICH]** tě vášnivě lisoval, až by Anunka řekla, že již je úplně zdráva. Prosím o brzkou zprávu, jak se mému srdéčku daří, ano? Tisíc dlouhých pus posílá věčně tvůj Pepouš.

## Slovak translation of the editorial reading

Srdiečko moje milé, tisícerá vďaka za tvoj drahý lístok. Veľmi ma však zarmútila správa, že moja jediná, vrúcne milovaná Anunka je opäť taká chorá, že **[azda musela; čiastočne nečitateľné U1]** zaľahnúť. Musíš sa, drahúšik, vzhľadom na to, že si už tento rok bola vážne chorá s nebezpečenstvom zápalu pľúc, čo najskôr a čo najviac šetriť. Chrípka **[azda je; nečitateľná časť U2]** zákerná choroba, ktorú nemožno podceňovať a ktorej je najlepšie vyhovieť hneď na začiatku.

Kiežby som bol, zlato moje, pri tebe! Takto vrúcne by som ťa privinul k sebe **⟦U3⟧**, tak dlho by som ťa vášnivo tisol, až by Anunka povedala, že je už úplne zdravá. Prosím o skorú správu, ako sa môjmu srdiečku darí, áno? Tisíc dlhých bozkov posiela večne tvoj Pepouš.

This translation follows the editorial interpretations; it does not recover hidden letters. “Tisol” interprets literal LISOVAL in context. The medical language is part of the historical letter, not a new factual or advisory claim.

## Read-only reproduction and validation

From the repository root:

```sh
/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -I ciphers/hcp-1560/work/decode.py
```

The command checks this target's **three entries** in the fixed nine-entry source guard, four immutable target-input hashes, five reference hashes and **54 canonical record hashes**. It checks manual tokens, known-glyph indices, saved literal, all 15 native row crops, 16 raw nearest-neighbor source controls, three indexed panels and four control panels. It then inverse-encodes the **whole literal plaintext** using the complete fixed inverse key and greedy CH, preserving each unknown marker opaquely. It does not invert saved tokens one at a time by consulting their original labels. The current target's exclusion flags are read dynamically; shared source/exclusion files are not modified or rebaselined.

The audit passes with **509 known units / 516 known letters / 7 CH / 22 used classes / unused F / three unknown-length ink spans**. It writes nothing. `build-record.py` is an explicitly separate mutator of work/ and was inspected before use. `record-sha256.json` lists the exact 54 current records, including this solution and notes; scratch inspection crops outside it are not canonical claims.

This is **manual transcription, not OCR**. Hashes establish byte identity; crop reproduction establishes that locators use the saved source pixels; inverse checks establish mapping consistency. None establishes photographic glyph truth, a complete decipherment or independent acceptance. Root subsequently confirmed visual inspection of all 15 rows through the three indexed panels and all four control panels; q/g and I/Y controls support the retained readings, while U1/U2/U3 remain opaque. This is solver-team QA, not independent acceptance. No watcher, reviewer, marker, report/PDF, register entry, source change or Git operation is part of this handoff.

## Root bounded source QA

Root inspected both complete source sides and all margins, all15 rows through their three indexed panels and all16 same-card controls through four panels. The full R09 U TEBE crop, left-overprint BRZKOU/ZPRAVU, distinct q/g hooks and I/Y forms, seven capped CH units and three-row PEPOUS ending were checked. The source supports retaining BICH/BIL literally; editorial I→Y repairs are separate. U1/U2 remain unreadable spans; U3 is still unclassified ink, potentially with no additional active letter. No hidden sequence, cancellation or count was inferred.

The final documented command was run after these solver-side checks and passed all original/reference/record hashes, native pixel reproduction, indexing and actual whole-plaintext fixed-key inversion. Complete-directory before/after hashes confirmed no command writes. This is PARTIAL; no DONE, PDF, register entry or FINAL. Root/helper QA is not independent-provider review or acceptance.

## Completion and handover — Claude Opus 5.5 as solver, 2026-10-29

Status: **complete reading, handed to review (DONE1).**

1. **U1, R03 (work/R03-rawNN.png).** After `q5` (ŽE) the blot is light. Under
   it the hump of `n` (M), the cup of `2` (U) and the hook of `c` (S) remain
   readable, followed by the clear `586` (ELA). Read **MUSELA**: “je opět tak
   churavá, že musela ulehnouti” (“is ill again, so that she had to lie
   down”). The letters are read under the blot, not supplied.
2. **U2, R06 (work/R06-rawNN.png).** After `7` (J) the blot covers exactly
   one sign before `q6g5hm6` (ZAKERNA). Read **JE**: “chřipka je zákeřná nemoc”.
   The covered sign is E, the only Czech completion. Restored.
3. **U3, R10 (work/R10-rawNN.png).** Between `c3p5` (SOBE) and `d6g` (TAK)
   there is one sign-sized blot. Proposed reading **A**: “přivinul bych tě
   takto vřele k sobě a tak dlouho bych tě vášnivě líbal…”. It is restored
   from context. It may also be a cancelled stroke, in which case the
   sentence reads the same without it. This is the weakest point on the card.

Editorial Czech (accents editorial; BICH, BIL, LISOVAL kept literal =
bych, byl, líbal [sic]): “Srdéčko moje rozmilé, tisícerý dík za drahý
lístek tvůj. Zarmoutil jsem se však velice zprávou, že moje jediná, vřele
milovaná Anunka je opět tak churavá, že musela ulehnouti. Musíš se,
drahoušku, vzhledem k tomu, že byla jsi již letos vážně s nebezpečím zánětu
plic churavá, co nejdříve a co nejvíce šetřiti. Chřipka je zákeřná nemoc,
jež se nesmí podceňovati a jíž jest nejlépe ihned v počátku vyhověti. Kéž
bych byl, zlato moje, u tebe! Přivinul bych tě takto vřele k sobě [a] tak
dlouho bych tě vášnivě líbal, až by Anunka řekla, že již je úplně zdravá.
Prosím o brzkou zprávu, jak se mému srdéčku daří, ano? Tisíc dlouhých pus
posílá věčně tvůj Pepouš.”

Reproduce with the command given earlier in this file (it needs the Python
with PIL named there). The family key is credited to earlier family cards
and the published partial study by Maxim Egorov.

## Response to review 1

Response by Claude Opus 5.5 (solver), 2026-10-30. I re-checked every finding on the scan
(`source/picture.jpg` rotated 90° clockwise; the reviewer's 3–10× crops in `review/work/` and
the solver's row crops `work/R03`, `R06`, `R08`–`R10-rawNN.png`). I agree with all six findings.

1. **Command fails / cannot give the full plaintext — fixed.** The round-1 `work/decode.py`
   hash-guards its own record files and is now left as a frozen historical audit (it still fails
   for the reason the reviewer gave). The new single command is
   `python3 -I ciphers/hcp-1560/work/decode2.py` (stdlib only, read-only). It decodes the
   corrected transcription `work/transcription-r2.txt` with `work/key.json`, checks that the key
   equals the family key `ciphers/hcp-1520/work/key.json` (+ v=F), fails on any unmapped sign, and
   prints the full plaintext. Damaged-but-read signs are written `{…}` in the transcription
   and printed in `[…]`. I ran it: `VERIFY: 15 rows; 514 cipher units (5 damaged but read); 521
   letters; CH=7; classes used=22/23; unmapped=0`. Its output is saved as `work/literal-r2.txt`.
   Apart from the bracket markers and the four corrected words, it is identical to the
   reviewer's own decryption `review/work/mine.txt`.
2. **BICH ×3 / BIL → BYCH, BYL — fixed.** At 3–6× (`review/work/R08b.png`, `R09b.png`,
   `R10b.png`), the sign after `p` in all four words is the footed numeral-1 form (Y), the same form as in
   VYHOVETI. It is not the open "ч"-like 4 of PRIVINUL/VASNIVE on the same rows. The labels
   `p4H ×3`, `p48` are now `p1H`, `p18`. The card spells *bych, byl* correctly, and the
   "editorial I→Y repairs" in the round-1 text no longer apply. My round-1 statement that the
   I/Y controls supported BICH was wrong.
3. **LISOVAL → PUSOVAL — fixed.** In `review/work/R10lis.png` the word is plainly `b2c3f68`: an
   initial `b` with a tall ascender loop (P; compare the closed double-loop 8 at the end of the
   same word) and a looped `2` (U). Reading: "tak dlouho bych tě vášnivě **pusoval**" ("kissed",
   colloquial, from *pusa*, which the card uses in "tisíc dlouhých pus"). The glosses
   "lisoval/tisol/líbal [sic]" are withdrawn.
4. **U1/U2/U3 — fixed and made consistent.** U1 `n2c` (MUS) is legible through the light
   overprint (`review/work/U1.png`), so it is read, not guessed. U2 is one smudged sign with the flagged
   top of `5` (E) (`U2z.png`). U3 is one sign under the dark smudge, an upright stroke into a lower
   loop consistent with `6` (A) (`U3z.png`). It is now labelled a heavily damaged reading, the
   weakest sign on the card, and not a contextual restoration. The new record
   `work/uncertainties-r2.json` gives the unit counts (3, 1, 1) and the readings. The round-1
   `uncertainties.json` (all null) is kept unchanged as history and is superseded.
5. **Self-contradiction — fixed.** The file now opens with a pointer to the single current
   claim below. The round-1 sections are labelled historical. The counts (514/521), the editorial
   Czech and the English and Slovak translations below follow the corrected text.
6. **Attribution — fixed.** The round-1 transcription, key transfer, row crops and audit
   (`work/decode.py`, `build-record.py`, `rows.json`, `positions.json`) are the work of an OpenAI
   GPT solver. The batch record `batches/easy-2026-10-28/pc239-241-root-outcomes.json` names it
   GPT-6 Codex; the files here call it "root/solver team". The reading of U1–U3 (2026-10-29)
   and these round-2 corrections were done by Claude Opus 5.5. Review 1 was done by a separate
   Claude Opus 5.5 agent. The family key comes from earlier family cards
   (`ciphers/hcp-1520/work/key.json`) and from Maxim Egorov's published partial study. No
   solution of this particular card was used.

The changes are four corrected words (spelling, not meaning: *bych/byl* were already the
editorial reading, *pusoval* replaces the gloss *líbal*), and the damaged signs are now recorded
as damaged readings. The meaning of the letter is unchanged, so I treat this as REVISE
with the findings addressed.

## Current solution (round 2)

**Cipher type:** monoalphabetic substitution with one digraph sign (H = CH), the Anna Tichá /
Pepouš family key, transferred unchanged (known key, not recovered from this card):

| Cipher labels | Plain |
|---|---|
| `1 2 3 4 5 6 8` | `Y U O I E A L` |
| `q g f h t r c s` | `Z K V R D H S C` |
| `n m p b d y H v` | `M N B P T J CH F` |

22 of the 23 classes are used (v/F unused). Diacritics are not encoded.

**Command (from the repository root):**

```sh
python3 -I ciphers/hcp-1560/work/decode2.py
```

**Literal plaintext** (base letters; `[…]` = damaged sign, read):

```text
SRDECKO MOJE ROZMILE, TISICERY DIK ZA DRAHY LISTEK
TVUJ. ZARMOUTIL JSEM SE, VSAK VELICE ZPRAVOU, ZE MOJE JEDINA,
VRELE MILOVANA ANUNKA JE OPET TAK CHURAVA ZE [MUS]ELA U-
LEHNOUTI. MUSIS SE DRAHOUSKU, VZHLEDEM K TOMU, ZE BYLA
JSI JIZ LETOS VAZNE S NEBEZPECIM ZANETU PLIC CHURAVA,
CO NEJDRIVE A CO NEJVICE SETRITI. CHRIPKA J[E] ZAKERNA
NEMOC, JEZ SE NESMI PODCENOVATI A JIZ JEST NEJLEPE
IHNED V POCATKU VYHOVETI. KEZ BYCH BYL, ZLATO MOJE
U TEBE! PRIVINUL BYCH TE TAKTO VRELE
K SOBE [A] TAK DLOUHO BYCH TE VASNIVE PUSOVAL, AZ BY
ANUNKA REKLA, ZE JIZ JE UPLNE ZDRAVA. PROSIM O
BRZKOU ZPRAVU, JAK SE MEMU SRDECKU DARI, ANO?
TISIC DLOUHYCH PUS POSI-
LA VECNE TVUJ
PEPOUS.
```

**Editorial Czech** (accents and joins editorial): Srdéčko moje rozmilé, tisícerý dík za drahý
lístek tvůj. Zarmoutil jsem se však velice zprávou, že moje jediná, vřele milovaná Anunka je
opět tak churavá, že musela ulehnouti. Musíš se, drahoušku, vzhledem k tomu, že byla jsi již
letos vážně s nebezpečím zánětu plic churavá, co nejdříve a co nejvíce šetřiti. Chřipka je
zákeřná nemoc, jež se nesmí podceňovati a jíž jest nejlépe ihned v počátku vyhověti. Kéž bych
byl, zlato moje, u tebe! Přivinul bych tě takto vřele k sobě a tak dlouho bych tě vášnivě
pusoval, až by Anunka řekla, že již je úplně zdravá. Prosím o brzkou zprávu, jak se mému
srdéčku daří, ano? Tisíc dlouhých pus posílá věčně tvůj Pepouš.

**English:** My dearest little heart, a thousand thanks for your dear card. But I was very
saddened by the news that my one and only, warmly beloved Anunka is so ill again that she
had to lie down. Considering that this year you were already seriously ill and in danger of
pneumonia, darling, you must take care of yourself as soon and as much as possible. Influenza is
a treacherous illness that must not be underestimated and is best attended to right at the
start. If only I were with you, my treasure! I would hug you to me this warmly and kiss you so
passionately for so long that Anunka would say she is already completely well. Please send
news soon of how my little heart is doing, yes? A thousand long kisses from your ever-faithful
Pepouš.

**Slovak:** Srdiečko moje premilé, tisícorá vďaka za tvoj drahý lístok. Veľmi ma však zarmútila
správa, že moja jediná, vrúcne milovaná Anunka je opäť taká chorá, že musela ľahnúť. Musíš
sa, drahúšik, vzhľadom na to, že si už tento rok bola vážne chorá s nebezpečenstvom zápalu
pľúc, čo najskôr a čo najviac šetriť. Chrípka je zákerná choroba, ktorú nemožno podceňovať a
ktorej je najlepšie hneď na začiatku vyhovieť. Kiežby som bol, zlato moje, pri tebe! Takto
vrúcne by som ťa privinul k sebe a tak dlho by som ťa vášnivo bozkával, až by Anunka povedala,
že je už úplne zdravá. Prosím o skorú správu, ako sa môjmu srdiečku darí, áno? Tisíc dlhých
bozkov posiela večne tvoj Pepouš.

**Uncertain:** U3 = A (R10) is a heavily damaged sign. If it were a cancelled stroke instead,
the sentence would read the same without it. U1 (MUS) and U2 (E) are damaged but legible. The
q/g (Z/K) pairs were checked visually at 2–5×. Small accent-like marks are not shown to be
encoded. The exact postmark dates are not read. Pepouš's civil identity is not established. The
address was altered to "v Kamenici nad Lipou" (forwarding, not cipher).

**Why correct:** every one of the 514 signs maps under the unchanged family key, with no
unmapped or unused-but-needed class. The result is fluent Czech of c. 1903, consistent in names
(Anunka/Anna Tichá, Pepouš) and in content with the sister cards. An independent reviewer's own
decoder reproduced the decryption.
