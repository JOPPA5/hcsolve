# HCP1553 / pc_hcp_234 — Pepouš to Anna Tichá, 25 May 1903

**Current position (after review 1, 2026-10-29):** the card is read in full. The current solution is stated in "Response to review 1" at the end of this file, and the current single command is `work/decode2.py` (see there). Everything between this note and that section is the earlier history: the initial partial candidate by OpenAI GPT (GPT-6 Astra / GPT-6.1 Sol), its root QA, and Claude Opus 5.5's completion note before review. It is kept for the record only. Where it disagrees with "Response to review 1" (for example "partial", "K unmapped", `[obscured:unknown-length]`, VROUCÍCH, VĚRNĚ, `work/decode.py`), the response wins.

## History (superseded) — partial known-key reading

## Claim and provenance

The eight physical picture-side rows contain Czech monoalphabetic substitution, with CH represented by one special cipher unit. This manual candidate records **324 mapped cipher units**, including **four CH units**, producing **328 mapped Latin base letters**. It also retains **one definite unmapped glyph** and **two obscured spans whose lengths are unknown**. Consequently, no exact total for all original cipher units is claimed. This is a partial solver candidate, without independent review or FINAL status.

The method is **known-key transfer**, not discovery: the family key in `ciphers/hcp-1520/work/key.json` and the already published partial [Anna Tichá research](https://maxim-egorov.dev/research/anna-ticha-postcards/) were supplied before target transcription. The photographed pc199 reference, including its published RUDOLFINA candidate, was also preknown. No target plaintext was supplied. The pc199 rare shallow-v/F class differs from tall f/V; neither grammatical expectations nor that reference supplies a mapping for the target's k-like unknown. Root inspected all three rendered portal tabs and both exact attachment modals, recorded Not solved, and found no individual attached transcription or solution. Its fresh register check found the target absent among 193 contributions / 159 distinct HC IDs. This is bounded evidence, not worldwide novelty.

## Image scope and transcription

Both complete original images and their margins were inspected. `work/picture-oriented.png` rotates `source/picture.jpg` **90° clockwise**, without changing the original. It is 674 × 1024 pixels. The encrypted text occupies the bottom eight rows; `work/row-01.png` through `row-08.png` are enlarged locators. `work/transcription.json` gives each oriented row box and focused unknown boxes; `work/inventory.json` indexes every mapped glyph, unknown locator and punctuation by row, word and token position. These are row locators, not fabricated glyph segmentation or OCR. An unknown-length span uses one record locator and does not assert one underlying glyph.

The picture-side ordinary date reads **25./V.1903.**, consistent with portal 1903-05-25. The slanted separator and Roman V are kept outside the cipher key. The address side has no observed encrypted message. Its ordinary handwriting reads:

```text
Velectěná Slečna
slečna Anna Tichá
učitelka v
Žirovnici
u Počátek.
```

`work/scope.json` inventories the printed multilingual postcard headings, green 5 Heller stamp, two postal impressions, illustration and modern alphabet watermark. The left postmark has Žirovnice / Seirovitz forms and visible V / 03; the exact day and parts of the other impression are indistinct. No complete postmark date is invented. Printed and postal text and the watermark are not substituted as if they were ciphertext. No further handwritten message was seen in the full picture margins.

## Fixed key

Cipher labels describe visual classes, not their plaintext. Uppercase H is the preknown caron-bearing special form for CH. The canonical family key is copied unchanged, with the separately published rare F class retained as a fixed reference assignment. F is unused here; K is explicitly **unmapped**.

| Cipher | Plain | Cipher | Plain | Cipher | Plain |
|---|---|---|---|---|---|
| 1 | y | 2 | u | 3 | o |
| 4 | i | 5 | e | 6 | a |
| 8 | l | q | z | g | k |
| f | v | h | r | t | d |
| r | h | c | s | s | c |
| n | m | m | n | p | b |
| b | p | d | t | y | j |
| H | ch | F (unused) | f | K | unknown |

No secondary V2 accent rule is applied. Ordinary above-line strokes do not automatically authorize an accented plaintext. Modern Czech accents below are editorial.

## Reproduction

From the repository root, the single read-only command is:

```bash
/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 ciphers/hcp-1553/work/decode.py
```

It verifies the nine selected immutable source originals against the root guard, reference and provenance hashes, and hashes of the manual records, crops, key and decoder. It checks exact indexed positions and literals, decodes all eight rows, and performs a whole-line inverse with the actual fixed key (greedy CH unit), preserving unknown locators. It does not OCR the photographs. Hashes and exact inversion establish record consistency, not handwriting truth.

## Literal base-letter output

Physical row breaks and hyphenation are preserved. `[unmapped:K]` is one visible k-like glyph; each `[obscured:unknown-length]` is an unresolved span, possibly including a separator, whose number of original characters is not known.

```text
srdecko moje jedine, tesim se na stredu nesmirne.
prijedu, jak [obscured:unknown-length]ujednano, rychlikem o tri ctvrte na [obscured:unknown-length]eset
rano. nezapomene anenka na podobenky, o jichz oka-
zani jsem prosil? tesim se, anunko, jiz touzebne, az
budu moci pri prijezdu svem tvou drahou rucku stisknou-
ti a zlibati. pro pripad nepredvidane prekazky plati
ujednane tele[unmapped:K]ramy. zatim posila ti tisic vroucich
vrelych pus touzici a verne tvuj pepous.
```

## Editorial Czech

Accents, capitalization and joined row splits are editorial. The visible base forms **ANENKA**, **ANUNKO** and **PEPOUS** are retained; Anenka is not silently changed to Anička. The unknown spans and unmapped glyph remain unresolved.

> Srdéčko moje jediné, těším se na středu nesmírně. Přijedu, jak [nečitelný úsek neznámé délky]ujednáno, rychlíkem o tři čtvrtě na [nečitelný úsek neznámé délky]eset ráno. Nezapomene Anenka na podobenky, o jichž okázání jsem prosil? Těším se, Anunko, již toužebně, až budu moci při příjezdu svém tvou drahou ručku stisknouti a zlíbati. Pro případ nepředvídané překážky platí ujednané tele[nepřiřazený znak K]ramy. Zatím posílá ti tisíc vroucích vřelých pus toužící a věrně tvůj Pepouš.

## Slovak translation

> Moje jediné srdiečko, nesmierne sa teším na stredu. Prídem, ako [nečitateľný úsek neznámej dĺžky]dohodnuté, rýchlikom o tri štvrte na [nečitateľný úsek neznámej dĺžky]eset ráno. Nezabudne Anenka na fotografie, o ktorých ukázanie som prosil? Túžobne sa už teším, Anunka, až budem môcť pri svojom príchode stisnúť a vybozkávať tvoju drahú rúčku. Pre prípad nepredvídanej prekážky platia dohodnuté tele[nepriradený znak K]ramy. Zatiaľ ti posiela tisíc vrúcnych, srdečných bozkov túžiaci a verne tvoj Pepouš.

## Uncertainties and source checks for root

- Row 2, between JAK and UJEDNANO: a short dark smudge/stroke. Its underlying extent and status as text or separator are unresolved. It is not discarded as a cancellation.
- Row 2, before visible ESET: heavy overink prevents a secure base identification and count. The expected hour is not completed from grammar.
- Row 7, TELE[K]RAMY: the tall k-like glyph is visually distinct from known h and f. Context may suggest a word, but no G assignment is inferred. `work/unknownG.png` is its crop.
- Source ink overlaps at the start of STREDU, at the 6/b region of NEZAPOMENE beneath the preceding line's descender, and at the 6 of PREKAZKY. Their visible outlines support the listed base candidates; the records do not delete any presumed cancellation. Focus crops `r1-middle.png`, `r3-over.png`, `r6-over.png` warrant root comparison.
- ANENKA and ANUNKO are the literal candidate base forms. Focused row crops preserve their evidence; editorial accents do not repair them.
- Four CH units are recorded: R2 RYCHLIKEM, R3 JICHZ, R7 VROUCICH, R8 VRELYCH. Small marks and modest resolution need visual verification.
- Root should compare the focused q/g controls, unknown/overink spans, names, all row ends and ordinary date against the full originals before handover. This collaborator supplies manual solver work, not independent review. Root alone handles any later handover. No watcher, reviewer, marker, PDF, register entry, git or source edit was made here.

The fixed key yields connected Czech through every recorded row, an arrival arrangement, photographs, affection and a contingency arrangement. That coherence supports the mapped portions; it does not resolve the three outstanding locations or certify every handwritten reading.

## Response to root source QA — row 2 suffix

Root identified a material transcription omission at row 2 end. Nearest-neighbor enlargement of original oriented pixels [565,775,646,812] shows **four** separately visible units after the heavy initial overink: **5 c 5 d**, producing **ESET**. The previous EST omitted the second 5; that was a solver transcription error. The second 5 has a top horizontal stroke, left downward bend and lower bowl matching the first 5 and same-card E controls. It is distinct from final d, whose upper bar and loop match the d/T control in R1 D5C4N. `work/r02-end-NN-boundary-controls.png` displays raw pixels, separately annotated proposed boundaries, and same-card d/5 controls. The annotation does not complete or alter any source stroke. All transcription, inventory, literal and count records were corrected to 324 mapped units / 328 base letters. The heavy initial interval remains unknown-length; neither DESET nor any hour is claimed. Unknown K and the other obscured span remain unchanged.

## Root source QA - 2026-10-28

Root inspected both original sides, all eight message rows and complete margins, and the focused name, overink, CH and date controls. ANENKA and ANUNKO remain literal base candidates; STREDU, NEZAPOMENE and PREKAZKY retain their discernible strokes despite overlaps. Four separately marked CH units are recorded. Native date enlargement supports25./V.1903; the initial June glance was rejected rather than overriding the preserved May catalogue metadata.

At row2 end, root detected the missing second5/E. The same-card controls and native-pixel panel confirm the visible suffix5c5d -> ESET, replacing EST in all active records. The final d/T is a separate unit. The preceding heavy interval remains unknown-length, so the record does not claim a complete hour. The other short dark stroke may be a separator or writing; it remains explicitly unresolved. The TELE[K]RAMY unit remains unassigned rather than adding G from context. These are solver checks, not independent review or automatic handwriting recognition.

The final read-only command passes324 mapped units ->328 base letters, four CH, one definite unmapped glyph and two unknown-length spans. The result remains PARTIAL without a marker, PDF or register entry. Original sources, fixed key and external provenance are unchanged.

## Completion and handover — Claude Opus 5.5 as solver, 2026-10-29

Status: **complete reading, handed to review (DONE1).**

1. **`[unmapped:K]` in TELE?RAMY (work/unknownG.png).** The k-shaped sign
   stands for **G**: **TELEGRAMY**. The same k-shaped sign stands where only G
   fits on HCP1541 (SVAGRA), HCP1554 (TELEGRAM) and HCP1570 (KOLEGY). Four
   cards with one consistent assignment establish the family's G sign; it is
   distinct from the looped `g` = K.
2. **First obscured span, `76g ~ 275tm6m3` (work/row-02.png).** Between JAK and
   UJEDNANO there is only a short horizontal stroke at mid-height. It has no
   letter body; it is a dash or a struck-through start. It contains no
   letters. Reading: “jak ujednáno” (“as agreed”).
3. **Second obscured span, `m6 [■]5c5d`.** A single overinked sign with a
   tall stem stands before `5c5d` (ESET). Read **DESET**: “rychlíkem o tři
   čtvrtě na deset ráno” (9:45). The time agrees with HCP1554 (“rychlíkem
   v 9:40 ráno”, the same planned meeting), and only D gives *deset*.

Editorial Czech (accents editorial; ANENKA, ANUNKO, OKAZANI kept as written):
“Srdéčko moje jediné, těším se na středu nesmírně. Přijedu, jak ujednáno,
rychlíkem o tři čtvrtě na deset ráno. Nezapomene Anenka na podobenky, o
jichž okázání [= ukázání] jsem prosil? Těším se, Anunko, již toužebně, až
budu moci při příjezdu svém tvou drahou ručku stisknouti a zlíbati. Pro
případ nepředvídané překážky platí ujednané telegramy. Zatím posílá ti tisíc
vroucích vřelých pus toužící a věrně tvůj Pepouš.”

Slovak: „Srdiečko moje jediné, nesmierne sa teším na stredu. Prídem, ako sme
sa dohodli, rýchlikom o tri štvrte na desať ráno. Nezabudne Anenka na
fotografie, ktoré som prosil ukázať? Už túžobne sa teším, Anunko, keď
budem môcť pri svojom príchode stisnúť a pobozkať tvoju drahú rúčku. Pre
prípad nepredvídanej prekážky platia dohodnuté telegramy. Zatiaľ ti posiela
tisíc vrúcnych bozkov túžiaci a verne tvoj Pepouš.“

Reproduce with the command given earlier in this file. The family key is
credited to earlier family cards and the published partial study by Maxim Egorov.

## Response to review 1

Review 1 (verdict REVISE) was addressed by Claude Opus 5.5 as solver on 2026-10-29. I re-checked every disputed place on the reviewer's crops and on the original, `source/picture.jpg`, turned 90° clockwise.

**Finding 1 (major), row 7: DLOUHÝCH, not VROUCÍCH. Fixed.** In `review/work/r7_vroucich.png` the word reads `t 8 3 2 r 1 ř`. It begins with the crossbarred t (= D), as in `275tm6m3`. Next comes a figure-eight 8 (= L), then 3 2 (O U). After that comes the short r (= H), not the backwards-6 s, then a plain 1 (= Y), and the caron-bearing CH sign. The word is *dlouhých*: "tisíc dlouhých vřelých pus". The earlier `fh32s4H` was a reading from expectation. A count correction to the review: the word has 7 units both before and after the fix, so the number of mapped units does not change. The r/H class now occurs twice.

**Finding 2 (major), row 8: VĚČNĚ, not VĚRNĚ. Fixed.** In `review/work/r8_verne.png` the fourth sign of `f5?m5` is the short backwards-6 s (= C), the same sign as in `n3s4` (MOCI). It is not the tall h (= R). The word is *věčně*: "a věčně tvůj Pepouš". This is also the sign-off of sister card HCP1554.

**Finding 3 (major), the command did not print the completed reading. Fixed.** There are new records `work/transcription-v2.tsv` and `work/key-v2.json`. The key is `key.json` plus `G` for the k-shaped sign, 24 classes. The new decoder is `work/decode2.py`, standard library only. It checks the hashes of the three source files (`work/source-sha256.json`). It checks that key-v2 is key.json plus G. It decodes the transcription and checks the output against the saved `work/literal-v2.txt`. The old `work/decode.py` and its records still audit the pre-review transcription and are superseded. The single command, from the repository root, is:

```sh
python3 -I ciphers/hcp-1553/work/decode2.py
```

(The codex-runtime python given earlier gives the same output.) Notation: `{x}` marks a sign that is read as class x but looks anomalous. `[x]` marks a sign restored from context. `~` marks a non-letter stroke, printed as `-`. Output, re-run after the fixes:

```text
R1: srdecko moje jedine, tesim se na stredu nesmirne.
R2: prijedu, jak - ujednano, rychlikem o tri ctvrte na [d]eset
R3: rano. nezapomene an{e}nka na podobenky, o jichz oka-
R4: zani jsem prosil? tesim se, anunko, jiz touzebne, az
R5: budu moci pri prijezdu svem tvou drahou rucku stisknou-
R6: ti a zlibati. pro pripad nepredvidane prekazky plati
R7: ujednane telegramy. zatim posila ti tisic dlouhych
R8: vrelych pus touzici a vecne tvuj pepous.

Rows: 8; cipher units: 326 (1 anomalous {}, 1 restored []); plaintext letters: 330; CH units: 4; G units: 1
Key classes used: 23/24; unused: ['F']
Saved literal-v2.txt: OK
```

The counts went from 324 mapped units plus 1 unmapped sign plus 2 spans to 326 units. G was added, D was restored, the dash is not a letter, and the DLOUHÝCH fix leaves the count unchanged. With brackets, braces and the dash removed, this output is identical to the reviewer's independent `review/work/decode_reviewer.txt`.

**Finding 4 (minor), how well G is supported. Wording corrected.** The earlier claim of "four cards with one consistent assignment" overstated the evidence. Here is the actual evidence. The same k-shaped sign occurs in TELE-G-RAMY here (`work/unknownG.png`, `review/work/K.png`), where it is visually distinct from the h that follows it. It occurs in SVAGRA on HCP1541, confirmed by that card's reviewer. It occurs twice on HCP1570 (SVAGROVA and one more word); that card has been reviewed and closed (FINAL). HCP1554 is still in revision. G is a **family assignment inferred from context**: no other G sign exists in the family key, and only G gives Czech words in all these places.

**Finding 5 (minor), DESET is a restoration. Labelled.** The overinked sign before ESET is now recorded as `[t]` and printed as `[d]`. It has a tall stem with a top flick and a crossbar, so it is compatible with t (= D), but it is too heavily inked to identify on the pixels alone. Only *deset* fits "o tři čtvrtě na ?eset". "Tři čtvrtě na deset" is 9:45. This is **consistent with**, not identical to, the "rychlíkem v 9:40" on HCP1554, which arranges the same Wednesday meeting.

**Finding 6 (minor), the first span is a dash. Recorded.** The stroke between JAK and UJEDNÁNO is kept in the records as `~`, a non-letter mark, printed as `-`. It is not deleted.

**Finding 7 (minor), ANENKA. Disclosed.** On `review/work/r3_anenka.png` the third sign of `6m?mg6` is a looped plaintext-style "e". It is neither the card's regular 5 nor its 2. It is recorded as `{5}` (anomalous) and printed as `an{e}nka`. The most likely explanation is that the writer slipped into plain script for one letter; the sign could also be a variant 5. ANUNKA, matching "Anunko" in row 4, cannot be excluded. Both readings are pet forms of Anna and refer to the recipient.

**Finding 8 (minor), the first sign of SRDÉČKO. Disclosed.** The first sign is a closed-loop s-form with a long lead-in. It is not the card's usual open c (= S). I take it to be a word-initial variant of S. SRDÉČKO is certain from context.

**Finding 9 (minor), the label for J. Noted.** This card's records label J as `y`. The family key in `ciphers/hcp-1545/work/key.json` labels the same 7-shaped sign `7`. The class is the same; only the label differs.

### Current reading

Czech (accents, capitals and punctuation editorial; ANENKA, ANUNKO and OKÁZÁNÍ kept as written):

> Srdéčko moje jediné, těším se na středu nesmírně. Přijedu, jak ujednáno, rychlíkem o tři čtvrtě na deset ráno. Nezapomene Anenka na podobenky, o jichž okázání [= ukázání] jsem prosil? Těším se, Anunko, již toužebně, až budu moci při příjezdu svém tvou drahou ručku stisknouti a zlíbati. Pro případ nepředvídané překážky platí ujednané telegramy. Zatím posílá ti tisíc dlouhých vřelých pus toužící a věčně tvůj Pepouš.

English: My one and only sweetheart, I am looking forward to Wednesday immensely. I shall come, as agreed, by the express at a quarter to ten in the morning. Will Anenka not forget the photographs she was to show me, as I asked? I am already longing, Anunka, for the moment when on my arrival I can press your dear little hand and kiss it. In case of an unforeseen obstacle, the telegrams we agreed on hold. Meanwhile, longing and eternally yours, Pepouš sends you a thousand long, warm kisses.

Slovak: Srdiečko moje jediné, nesmierne sa teším na stredu. Prídem, ako sme sa dohodli, rýchlikom o tri štvrte na desať ráno. Nezabudne Anenka na fotografie, ktoré som ju prosil ukázať? Už túžobne sa teším, Anunka, keď budem môcť pri svojom príchode stisnúť a pobozkať tvoju drahú rúčku. Pre prípad nepredvídanej prekážky platia dohodnuté telegramy. Zatiaľ ti posiela tisíc dlhých vrúcnych bozkov túžiaci a večne tvoj Pepouš.

### Remaining uncertainties

- D in DESET is restored from context (finding 5).
- The third sign of ANENKA is anomalous; ANUNKA is possible (finding 7).
- G is a family assignment inferred from context (finding 4).
- The postmark day is indistinct. The date rests on the plain 25./V.1903 on the card and on the portal metadata.

No decoded letter outside rows 7–8 changed. The reading is otherwise as handed over in DONE1.
