# HCP 1529 - corrected Czech postcard report

Human solver: Tomáš Pavuk

Independent Review1 by Claude Opus5.5 returned REVISE. The local findings have been addressed and checked against the source. The reviewer explicitly permits closure after these corrections without a further round. The original review verdict is preserved; no new ACCEPT verdict is invented.


Visible-text solver candidate with localized source-reading uncertainty, revised after **REVISE** review1 by claude-opus-5-5. Root has checked this response; the original REVISE verdict is preserved, with no invented ACCEPT verdict. This applies the known Anna Tichá postcard family key supplied at the outset. It is **known-key transfer**, not independent key discovery or a historical-priority claim.

## Source and provenance

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1529 . Root inspected rendered General, Description and Attachments on 2026-10-28 UTC: **Not solved**, Czech, Substitution, private collection, date 1903-12-01, unknown sender, recipient Anna Tichá. No attached target transcription or solution. Immutable captures are in `source/`; full original image URLs and generic-publication provenance are in `SOURCES.md`. The unencrypted address calls Anna Tichá a teacher in Žirovnice near Počátky. Ordinary picture-edge date reads 1/XII/1903. Sender identity is not established.

Root's initial rendered AI-register check, preserved in this candidate's source capture, found 158 contributions/124 HCP IDs, this target absent. That is a bounded check, not worldwide novelty evidence. Maxim Egorov / Cipher-Atelier previously published a generic partial family key and eleven partial readings; root's indexed public list did not include pc210. The exact source reference and saved public generic key provenance are recorded in `SOURCES.md` and the batch files. No published target plaintext or initial target-transcription seed was supplied. Later source-derived comparisons with root are solver collaboration, not prior published target plaintext. HCP1520's key and HCP1527's solution were available from the beginning. The tentative shallow v/F from another card is not used here.

SHA-256 of immutable sources (also checked by the reproduction command):

| File | SHA-256 |
|---|---|
| picture.jpg | bb65111ea39a9d2e49e4c71687f51c50af7254a0e6df1366d3d34b6053aae96b |
| address.jpg | bf0f6fa8589a94b16f4aaccdcf9c874923eff3db1dd1f83099cabb2e8572ff74 |
| metadata.md | 520e6e6bed27d126e011c8617e438fb510be2d07845b0e9137414b12f3de59d2 |

## Cipher, key and reproduction

Monoalphabetic substitution of handwritten digits/Latin-looking glyphs, with CH as one cipher unit. Labels describe glyph classes conventionally, not diplomatic reproductions of their handwriting. `H` is a neutral label for the special CH glyph, not an ordinary plaintext H. `m` and `n` are distinct family labels.

| Glyph | Plain | Glyph | Plain | Glyph | Plain | Glyph | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | 8 | L | y | J |
| q | Z | g | K | f | V | h | R |
| t | D | r | H | c | S | s | C |
| n | M | m | N | p | B | b | P |
| d | T | H | CH | | | | |

For the shared family notation, the following are aliases for existing classes, not new key assignments. The fixed local transcription/key are unchanged; this avoids confusing shape label H with plaintext H.

| Family plaintext unit | HCP1529 shape label | HCP1526/1527 shape label | Meaning |
|---|---|---|---|
| J | y | 7 | same J class under different transcription names |
| CH | H | ř | marked/capped special CH unit |
| H | r | r | ordinary H unit, distinct from CH |

Single command from repository root:

```sh
python3 ciphers/hcp-1529/work/decode.py
```

This standard-library command is **read-only by default**. It verifies the three preserved original hashes and twelve record hashes, decodes the manual source transcription using `work/key.json`, checks every ordinal against `work/positions.csv`, checks exact plaintext/inventory equality and re-encodes each entire printed plaintext row through the fixed inverse alphabet, matching CH before C, then prints all eight rows, the localized PRI source limit and deterministic weekday checks. The inversion uses the full printed text rather than a tokenwise key identity. The source image is the immutable visual input; the intermediate transcription is manual, not OCR. These checks establish reproducibility and internal consistency, not independent visual proof.

`work/transcription.txt` preserves the manual glyph-label transcription; `work/transcription.json` links each row to its source box and records its base plaintext/count; `work/positions.csv` inventories every cipher unit by global ordinal, row ordinal and word ordinal. `work/indexed.png`, `R01-native.png`-`R08-native.png` and `focused-controls.png` provide source-pixel checks. Coordinates use the original upright 1024×674 image, with no image rotation. The ordinal inventory does not claim per-glyph pixel segmentation. Explicit `build-record.py` and `make-controls.py` generate records/crops and require PIL; they are not invoked by the default decoder.

| Row | Original box x0,y0,x1,y1 | Cipher units |
|---|---|---:|
| R01 | 48,27,978,65 | 63 |
| R02 | 48,59,978,96 | 58 |
| R03 | 48,87,978,123 | 56 |
| R04 | 48,116,978,155 | 49 |
| R05 | 48,145,978,184 | 51 |
| R06 | 48,174,978,214 | 51 |
| R07 | 450,205,978,249 | 27 |
| R08 bottom margin | 48,591,978,636 | 62 |

## Literal Czech base reading

All visible cipher writing, including the bottom marginal line. Accents are excluded here. No missing grammatical words or base letters are inserted. R03 PRI has the localized ink-heavy glyph uncertainty discussed below.

```text
JSEM, ANICKO, OD CTVRTKA OPET DOMA S CHRIPKOU, KTERA SE MNE OPET SILNEJI VRATILA.
NEBYL JSEM PRESTO UPLNE ZDRAVEM A NACHLADIL JSEM SE OPET NA CESTE Z USTI
JESTE VICE VSAK PRI LICENI OHLEDNE UPADKU SVATOVACLAVSKE ZALOZNY,
KDE JSEM SE BYL PODIVATI A KDE BYL VELKY NAVAL A HROZNE VEDRO.
BOLELA MNE VELICE HLAVA A NEBYL JSEM SKORO ANI MISLENI SCHOPEN.
DOSUD LEZIM, PROTOZE VSAK DNES JIZ LEPE A VZKAZAL JSEM DO URADU,
ZE PRIJDU VE CTVRTEK NEBO V PATEK.
NA TEBE VZPOMINAM STALE JAKO NA SVE JEDINE SRDECKO A POSILAM TI VRELOU PUSU.
```

## Editorial Czech

Accents and ordinary capitalization below are editorial. The literal MISLENI is retained as *mislení*, without silently replacing I by Y; the incomplete-sounding clause *protože však dnes již lépe* is retained without adding *je* or *mi*.

> Jsem, Aničko, od čtvrtka opět doma s chřipkou, která se mně opět silněji vrátila. Nebyl jsem přesto úplně zdrávem a nachladil jsem se opět na cestě z Ústí ještě více však při líčení ohledně úpadku Svatováclavské záložny, kde jsem se byl podívati a kde byl velký nával a hrozné vedro. Bolela mne velice hlava a nebyl jsem skoro ani mislení schopen. Dosud ležím, protože však dnes již lépe a vzkázal jsem do úřadu, že přijdu ve čtvrtek nebo v pátek.
>
> Na tebe vzpomínám stále jako na své jediné srdéčko a posílám ti vřelou pusu.

Z ÚSTÍ means **from Ústí**. Which town named Ústí is meant remains unidentified. The reference to the záložna is legible text; the historical identification and date of a particular trial have not been independently verified in this response.

## Slovak translation

> Som, Anička, od štvrtka opäť doma s chrípkou, ktorá sa mi znovu silnejšie vrátila. Nebol som napriek tomu úplne zdravý a opäť som prechladol na ceste z Ústí, ešte viac však pri pojednávaní o úpadku Svatováclavskej záložne, kam som sa bol pozrieť a kde bol veľký nával a hrozné teplo. Veľmi ma bolela hlava a skoro som nebol schopný ani myslieť. Doteraz ležím, „pretože však dnes už lepšie“ [neúplné znenie originálu] a odkázal som do úradu, že prídem vo štvrtok alebo v piatok.
>
> Na teba spomínam stále ako na svoje jediné srdiečko a posielam ti vrúcny bozk.

Translation renders *líčení* as a hearing/proceeding, an interpretation of the Czech word rather than a separately verified event.

## Coverage, controls and uncertainty

Eight rows contain **417 active cipher units**, including **3 CH units**, yielding **420 base letters**. All are assigned by the supplied key. Ordinary date/address, punctuation, word spacing and diacritics are excluded from that denominator. No separate fully canceled cipher unit was identified; the heavy R03 middle glyph may have been retraced, and its earlier ink cannot be recovered reliably. No canceled-letter count is invented. This is not a claim to recover every accented feature.

- R01 ANICKO includes the small s/C between I and K; `R1-a.png` and the focused sheet preserve it. CHRIPKOU, NACHLADIL and SCHOPEN use the same supplied CH class.
- R02 final USTI is `2cd4`; the middle group is c/S then d/T. See `r2-end.png` and focused sheet. Initial UCTI draft was discarded.
- R03 PRI is `bh4`. Its middle h/R lies under heavy ink/possible retracing and is the least clear glyph in this candidate. The reading fits the visible surviving strokes and transferred key, but is less secure than neighboring units; `R3-pri.png` / focused sheet preserves the full source patch. No hidden alternative is treated as eliminated by the roundtrip.
- R05 MISLENI is `n4c85m4`: the second glyph is read as digit4/I rather than digit1/Y. See `R5-schopen.png`, the focused sheet and `I-Y-control.png`, which compares source 4/I and 1/Y in neighboring NEBYL, LICENI and ZALOZNY. No spelling repair is incorporated. Source *zdrávem* is also retained.
- R06 VZKAZAL is `fqg6q68` over dark artwork; `R6-b.png` and focused sheet show the source. The short clause PROTOZE VSAK DNES JIZ LEPE is retained as visible, without grammatical filling.
- R07 is ZE PRIJDU VE CTVRTEK NEBO V PATEK. R08 is the entire bottom marginal sentence, not an omitted postscript. Native and enlarged crops cover both.

The full candidate is supported by consistent known-key application across all visible rows and coherent letter correspondence, with spelling/grammar anomalies kept explicit. No blind held-out test, independent key recovery, OCR, published target solution or worldwide novelty proof is claimed. Review1 by claude-opus-5-5 performed an independent source check and returned REVISE; the numbered response below addresses its findings. Existing DONE1 and REVIEWED1 record that round. This collaborator creates no new marker, watcher, reviewer process, PDF or register entry; root retains the protocol decision after QA.

## Source-derived solver collaboration

Root inspected the PRI, MISLENI, VZKAZAL and USTI source crops before handover. Root found identifiable tall strokes in PRI but heavy overtracing, source support for digit4/I in MISLENI, and consistency of VZKAZAL and USTI. These are disclosed as second-solver source comparisons, not blind independent-provider review or pre-existing plaintext. The final 1/Y versus 4/I comparison is separately preserved in `work/I-Y-control.png` and its coordinate manifest.


## Root verification before handover

Root inspected both originals, the enlarged complete seven-row upper body, the entire bottom marginal line and all focused controls on 2026-10-28. The I/Y comparison supports literal MISLENI; the ink-heavy h/R in PRI remains a specifically disclosed weaker reading rather than an automatically verified letter. The ordinary date/address and all eight cipher rows are accounted for. Root ran the documented read-only command: original and record hashes, 417 indexed active units, three CH expansions and the then-current tokenwise inverse-key check passed. All nine wave source hashes matched. This is a second solver check using a known key, not independent provider review; the záložna reference is text evidence without an asserted independently verified historical event.

## Calendar and series context

The ordinary date and portal metadata give **1 December 1903**, a **Tuesday**, independently checked by calendar arithmetic in `work/review1-context-check.json`. Under the ordinary relative-date interpretation, OD CTVRTKA refers to Thursday **26 November**, while the intended office return VE CTVRTEK NEBO V PATEK refers to **3 or 4 December**. These dates are contextual inferences from the letter and calendar, not additional cipher characters or proof that the planned return occurred.

Preserved sibling solver records provide a compatible sequence: HCP1526 is dated **Saturday 12 December** and says the writer is back in the office ODE STREDY (naturally **9 December**) with some cold symptoms remaining; HCP1527 is dated **Saturday 19 December** and says he is now in the office all day. This agrees broadly with illness followed by a return to work. It does not prove uninterrupted illness, the exact return date, or a civil identity. Those sibling readings were known solver records, not an independent validation set; their dated source/solution hashes are recorded as snapshots in the context JSON.

The ordinary PRAHA dispatch postmark is compatible with a Prague writer. Review1 proposed, from general knowledge, a late-1903 trial following the Svatováclavská záložna collapse. That historical trial/date identification remains **unverified here**: no independent primary source was consulted for it, and it is not counted as external confirmation of the plaintext. The literal LICENI OHLEDNE UPADKU SVATOVACLAVSKE ZALOZNY stands independently of that proposed historical identification. The particular Ústí and day digits of the postmarks remain unresolved.

## Response to review 1

Review1 (`review/REVIEW1.md`, claude-opus-5-5, 2026-10-28) returned **REVISE** with one major source-reading correction and four minor agreements/presentation/context findings. It independently read 417 units and reported only the isolated preposition differed. This is the solver's response after checking the immutable originals, not a new independent review or acceptance.

1. **R02 Z USTI - corrected.** R02 unit54 / global117 is now q/Z rather than g/K: `s5cd5 q 2cd4` → **CESTE Z USTI**. The original isolated sign is a compact closed bowl/9 with a short left-hook tail, agreeing with q/Z in ZDRAVEM and ZALOZNY. It differs from the longer open-loop return to the right in g/K of KDE. New native plus integer4× NEAREST source controls are `work/review1-z-usti-controls.png`, with broad original-image boxes in its JSON: target `[884,56,978,98]`, KDE `[45,112,105,154]` and `[435,114,496,154]`, ZDRAVEM `[340,54,439,96]`, ZALOZNY `[845,85,978,127]`. The selected glyph counts are g/K=17 and q/Z=12, respectively one lower/higher than the reviewed record. Cipher text/JSON, ordinal117, plaintext, editorial Czech and Slovak now consistently say **z Ústí / from Ústí**. No key assignment changed; the town remains unidentified.
2. **R03 PRI limitation - agreed and retained.** Middle h/R in `bh4` remains the specifically weaker, ink-heavy reading, with tall surviving strokes but no recoverable earlier form. It is also recorded at R03 ordinal15 in `source_reading_limits` and the inventory and printed by the decoder. The reviewer's agreement supports retaining the disclosed reading; it does not make the ink perfectly clear or authorize a canceled-letter count.
3. **MISLENI, ZDRAVEM, PROTOZE … LEPE, VZKAZAL and full coverage - agreed.** Literal I in MISLENI remains unchanged; there is no modernization to MYSLENI. ZDRAVEM and VZKAZAL remain as read, and no JE, MI or other words fill the elliptical PROTOZE VSAK DNES JIZ LEPE. ANICKO, USTI and the complete bottom row remain included. No source-reading limit was dropped because of the successful inverse or the reviewer's agreement.
4. **Family labels - clarified.** The main fixed-key table explicitly distinguishes H→CH from r→H. The alias table above relates local y/H to sibling7/ř for J/CH without changing the local record or introducing a new class. The ordinary H class remains r throughout. No unused tentative F extension is imported.
5. **Weekday/series and historical context - addressed with evidence limits.** Calendar arithmetic confirms Tuesday1December and the relative-date possibilities26November/3-4December. Dated sibling records provide the12/19December compatibility described above. The proposed late-1903 záložna trial/date remains unverified against an independent primary source, explicitly separated from literal text and calendar facts. No historical-trial assertion is used to validate a glyph or locate Ústí.

The existing generators were inspected before use. The revised work-only builder first checks preserved source digests and the unchanged fixed-key digest; it reads the manual record and cannot silently restore the former hardcoded g. The decoder is read-only and standard-library only, with three unchanged source hashes, twelve record hashes, every ordinal, exact plaintext/inventory checks and a true whole-row fixed-key inverse. Counts remain **417 units, three CH, 420 base letters**, across R01-R08 counts63,58,56,49,51,51,27,62. Hash success and calendar compatibility do not independently prove manual glyph truth. Root has checked the source comparisons and all findings before the review-addressed closure step.


## Root closure checks after review1

Root inspected the native same-card source controls and the complete review response. The isolated preposition before USTI is the compact q/Z with a left hook, contrasting with both longer returning-loop g/K forms in KDE. The literal/editorial Czech and Slovak translation consistently say Z USTI / z Ústí / from Ústí; the town remains unidentified. PRI remains ink-heavy and explicitly less secure. Calendar arithmetic and sibling-card compatibility remain contextual, not an independent historical authentication. All five findings are addressed; finding5's trial research was optional, and no trial date is claimed as verified. The reviewer explicitly allows closure after the local preposition correction without another round.

The latest complete rendered AI register contains337contributions/303distinct HC Portal IDs, with this target absent. The full IDs matched the previous snapshot; the current evidence is batches/easy-2026-10-28/register-check-review207-208-210-next.json. Expanded public work on other family cards is acknowledged; the earlier eleven-page index is a historical bounded observation. No target-specific public plaintext was consulted for this correction beyond the existing independent review. This check establishes neither worldwide novelty nor historical priority. The six human-directed exclusions in register-exclusions.json remain in force; this target is not one of them.

The final read-only reproducer passes after the correction response; source/review/old markers remain protected by the closure-pass manifest. Root/helper checking is solver collaboration, distinct from the existing independent Claude Opus5.5 review. The report and local register entry are prepared before FINAL. No watcher, new reviewer, external submission, commit or push is performed. Solver name remains TODO because no name was supplied for these entries.


## Original source photographs

![Original picture side, preserved unchanged.](../source/picture.jpg)

![Original address side, preserved unchanged.](../source/address.jpg)

## Source record and public attribution

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1529 . All three rendered tabs and both source sides were inspected; no individual attached solution or transcription was displayed.

- Original picture image: https://api.hcportal.eu/media/4647/conversions/pc_hcp_210_pic-large.jpg
- Original address image: https://api.hcportal.eu/media/4648/conversions/pc_hcp_210_adr-large.jpg

Prior generic family research and partial key: https://maxim-egorov.dev/research/anna-ticha-postcards/ . This is known-key transfer with manual transcription. Current337-contribution/303-HC-ID register does not list this target. Public work on other family cards and the six explicit local registry exclusions remain acknowledged; no worldwide novelty or historical priority is claimed. Full source history is in SOURCES.md.
