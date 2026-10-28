# HCP 1532 — pc_hcp_213

Solver candidate accounting for all visible ciphertext, revised after **REVISE** review1 by claude-opus-5-5. Of 497 visible units, 496 have asserted readings and one is explicitly ambiguous, with D selected by context. The review remains REVISE; root has checked and addressed its findings under README's review-addressed closure path. No new ACCEPT verdict is invented. The body and the tiny right-edge continuation are read with the supplied Anna Tichá family substitution key. This is **known-key transfer**, not a newly discovered key or a historical-priority claim.

## Source, context and provenance

Source: https://crypto.hcportal.eu/dashboard/cryptograms/1532 . Root inspected rendered General, Description and Attachments on 2026-10-28 UTC. Portal status was **Not solved**; Czech, Substitution, private collection, date 1903-11-02, unknown sender, recipient Anna Tichá. No individual target transcription or solution was attached. Both immutable original sides and the rendered metadata are in `source/`; URLs are in `SOURCES.md`. The picture shows flowers with the ordinary handwritten date `2.XI.1903`. The address calls Anna Tichá a teacher in Žirovnice near Počátky. The cipher closing contains TVEHO PEPOUSE, interpreted as the nickname Pepouš; no civil identity is established.

Root's initial rendered register check, preserved with this candidate's source capture, found 158 contribution rows and 124 HC Portal IDs, with this target absent. This is a bounded check, not worldwide novelty evidence. Maxim Egorov / Cipher-Atelier's earlier published partial generic family key and eleven partial readings are acknowledged in `SOURCES.md`; their exact public reference and provenance are preserved in `batches/easy-2026-10-28/`. The public index did not list pc213 in root's check. The existing HCP1520–1527 key was supplied before transcription started. No published target plaintext or target transcription seed was supplied at commencement. Root was subsequently sent this solver's source-derived draft and ambiguity descriptions; any later root checking is solver collaboration, not blind or independent review.

## Cipher and key

Monoalphabetic substitution with digit/Latin-looking handwritten shapes and a special CH glyph. Labels below are conventional shape labels, not facsimile typography. In particular `n` means M, `m` means N, and `ř` names the marked CH glyph rather than plaintext Ř. The 7/J label follows HCP1527's convention for the writer's y-like form. No F-class extension is needed.

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | 7 | J | 8 | L |
| b | P | c | S | d | T | f | V |
| g | K | h | R | m | N | n | M |
| p | B | q | Z | r | H | s | C |
| t | D | ř | CH | | | | |

## Exact procedure and reproduction

Manually transcribe the eight sloping body rows and the small marginal row from `source/picture.jpg` using `work/transcription.json`'s source-coordinate row boxes. M01 runs bottom-to-top along the right edge; rotate its crop 90° clockwise for reading. Replace every shape label through `work/key.json`; preserve source row breaks and the DORU-/CEN and ZDA-LI hyphens. Spaces and punctuation are visually recorded, not cipher units. No automatic OCR or blind decipherment is claimed.

Run this single command from the repository root:

```sh
python3 ciphers/hcp-1532/work/decode.py
```

It is read-only and uses only Python's standard library. It checks three source hashes and nine record hashes, decodes every row, validates each CSV ordinal and its ambiguity metadata, checks the literal file and class inventory, and re-encodes the complete printed row through the fixed inverse alphabet (CH before C). It prints the full selected literal text below, the t/d ambiguity and counts. The inverse is a whole-row plaintext operation, not a per-token restatement of key entries. This reproduces a documented image transcription; hash/roundtrip success does not independently prove the glyph readings. `work/index.csv` has row/global ordinals and row boxes, plus status, candidate glyph/plaintext labels, visible observation and reading basis for the ambiguous unit. It does not claim per-glyph pixel segmentation. `work/inventory.json` distinguishes 496 unambiguous units from one ambiguous unit; selected-label counts include that conditional t/D. `work/indexed.png`, `work/R01.png`–`R08.png`, `work/M01.png` and `work/focused-controls.png` support image checking. The explicit crop/record generator is `work/build-record.py`; it is not invoked by the reproduction command.

Original SHA-256 values:

- picture.jpg: `9a21af5a11b7413c3902affad13a24cf84dfb13604aa056ebb484375454cd0d0`
- address.jpg: `73b2142f10f0264ce383f18f376b5e140bf912dd59d0c687bbdb127f2fb7554a`
- metadata.md: `f1c4083a56a440aad8437f314469e8ffdf6b8e33e2e9692348f50a60f082568d`

## Literal base plaintext

No missing letter or grammatical repair is inserted in this selected literal text. The first TEBRVE is retained exactly; the second occurrence is TEPRVE. R08 OD uses an explicitly **selected D**, while the visible sign also permits T, giving the bounded alternative OT. See the ambiguity record below; OD is not claimed as a secure clean glyph reading. Accents are excluded. The final line is the right-edge continuation, not a ninth horizontal body row.

```text
VRELY DIK ZA DRAHY LISTEK SOBOTNI, KTERY MNE VSAK BYL TEBRVE DNES RANO DORU-
CEN. ZASILAM TUDIZ ZADANOU ODPOVED TEPRVE DNES. TESI MNE ZE SE MAZLIKOVI MEHO
SRDECKA VEDE JIZ LEPE A ZE TUDIZ I ME SRDECKO JE OPET KLIDNEJSI. PTAS SE, ZDA-LI
JIZ O TVOJI PUSU NESTOJIM? - ZAJISTE O NI STOJIM A DAM TI JI NEJEN JAKO
REVANZ ZA TVUJ DAREK, NYBRZ PRIMO OD SRDCE, PONEVADZ TO MAM Z CELE DUSE
RAD A PONEVADZ PO TVE PUSE VELICE TOUZIM. BYL JSEM VCERA OPET CELY DEN
V URADE A MUSIL JSEM PROTO JESTE ODLOZITI PSANKO SLIBENE, JEZ VSAK ZASLU CO
NEJDRIVE. ZATIM VRELY POZDRAV OD TVEHO PEPOUSE, JENZ V DUCHU NESCISLNEKRATE TVOU DRAHOU
HLAVINKU LIBA.
```

## Editorial Czech reading

This reading adds accents, capitalization, paragraphing and the joining of DORU-/CEN. It also explicitly corrects the first literal TEBRVE to **teprve** (B→P); the second TEPRVE needs no repair. OD keeps the declared contextual D selection from ambiguous t/d ink. The archaic MUSIL, NESČÍSLNĚKRÁTE and zda-li remain. These editorial choices are separated from the literal transcription.

> Vřelý dík za drahý lístek sobotní, který mne však byl teprve dnes ráno doručen. Zasílám tudíž žádanou odpověď teprve dnes. Těší mne že se mazlíkovi mého srdéčka vede již lépe a že tudíž i mé srdéčko je opět klidnější. Ptáš se, zda-li již o tvoji pusu nestojím? – Zajisté o ni stojím a dám ti ji nejen jako revanž za tvůj dárek, nýbrž přímo od srdce, poněvadž to mám z celé duše rád a poněvadž po tvé puse velice toužím.
>
> Byl jsem včera opět celý den v úřadě a musil jsem proto ještě odložiti psánko slíbené, jež však zašlu co nejdříve. Zatím vřelý pozdrav od tvého Pepouše, jenž v duchu nesčíslněkráte tvou drahou hlavinku líbá.

The source base MNE in the first sentence is retained as *mne*, even though modern grammar would normally expect *mně*. That is an accent choice only; the letter sequence is unchanged.

## Slovak translation

This translates the editorial Czech: first TEBRVE is interpreted as *teprve* (až) and ambiguous OD is selected as *od*, rather than claiming an additional secure source reading.

> Vrelá vďaka za drahý sobotný lístok, ktorý mi však doručili až dnes ráno. Žiadanú odpoveď teda posielam až dnes. Teší ma, že sa miláčikovi môjho srdiečka už darí lepšie a že je preto aj moje srdiečko znovu pokojnejšie. Pýtaš sa, či už nestojím o tvoj bozk? – Pravdaže oň stojím a dám ti ho nielen ako odplatu za tvoj darček, ale priamo od srdca, pretože to mám z celej duše rád a pretože po tvojom bozku veľmi túžim.
>
> Včera som bol zasa celý deň v úrade, a preto som musel ešte odložiť sľúbený lístok, ktorý však pošlem čo najskôr. Zatiaľ vrúcny pozdrav od tvojho Pepouša, ktorý v duchu nespočetne veľakrát bozkáva tvoju drahú hlavičku.

## Coverage, controls and limits

- **497 visible cipher units**, including **1 CH unit**, yield **498 selected base letters**. There are **496 unambiguous readings and one ambiguous t/d unit** with contextual t/D selected. Body R01–R08 counts are 61, 63, 62, 54, 56, 56, 61, 72; marginal M01 contains 12. No visible unit is omitted, but this does not claim 497 certain glyph identities. No cancellation is asserted for the bowl-plus-crossbar sign or elsewhere. Ordinary date/address, punctuation and diacritic pen marks are outside this denominator.
- R03 `qt6-84` is ZDA-LI. The first shape's bowl and hooked descender match q/Z in ZA and ZAJISTE; g/K in KTERY has a crossing loop. The third shape is tall hooked 6/A, not 3/O. Initial KDO-LI/KDA-LI drafts were discarded after source comparison and remain logged in `NOTES.md`.
- R08 `m5cs4c8m5gh6d5` gives NESCISLNEKRATE. Its closely joined c/S, s/C and 4/I are kept as separate units. No extra E is inserted to regularize the spelling. The same-card C in CELY is a focused shape comparison.
- The marked family glyph in `t2ř2` gives DUCHU; the ordinary unmarked H in marginal HLAVINKU supplies a visible comparison. The margin is completely included as `r86f4mg2 84p6.`.
- Punctuation, spaces and editorial accents are less mechanically constrained than base letters. Complete base coverage does not claim exact recovery of every original accent mark. Sender identity beyond the nickname and any biographical implications remain unknown.

Readable correspondence, the fixed transferred substitution and complete body/margin accounting support the candidate. Review1 by claude-opus-5-5 independently checked the scan and decoder and returned REVISE on three local findings; its record is `review/REVIEW1.md`, with existing DONE1 and REVIEWED1 markers. The response below incorporates those findings and has passed root source and reproduction checks. There is no held-out test or OCR validation. This collaborator did not create a PDF, register entry or new state marker, and does not claim acceptance or FINAL.


## Root verification before handover

Root inspected both originals, all eight body row panels, the complete tiny marginal row and focused original-pixel controls on 2026-10-28. The first form in ZDA-LI follows the q/Z bowl and hooked descender, while its third unit is tall 6/A. NESCISLNEKRATE is retained without inserting a letter; both PONEVADZ occurrences and the single CH in DUCHU are included. The marginal HLAVINKU LIBA is fully accounted for. Root ran the documented read-only command: all original/record hashes, 497 indexed active units, one CH expansion and then-current tokenwise checks passed. The wave source manifest matched. This is a second solver source check using the known key, not independent provider review.

## Response to review 1

Review1 (`review/REVIEW1.md`, claude-opus-5-5, 2026-10-28) returned **REVISE**. It reported an independent sign-by-sign comparison of all eight body rows and the marginal continuation. The following are solver corrections after reading that review and checking the immutable originals; they are not a new independent review.

1. **R01 TEBRVE — addressed.** R01 unit/global ordinal46 is now `p`→B, so `d5phf5` literally decodes **TEBRVE**. The original sign has a descending p-like stroke like BYL, distinct from the looped ascending b/P in R02's genuine TEPRVE. Native/NEAREST4× controls are `work/review1-original-controls.png`, with boxes in its JSON: R01 target `[686,430,776,471]`, R02 comparison `[423,452,507,492]`, BYL `[631,431,683,469]`. This agrees with the reviewer's finding. The editorial reading alone substitutes B→P, an apparent writer's slip. Transcription, CSV ordinal46, literal, manifest and inventory were reconciled. Selected class counts are now b/P=17 and p/B=7, respectively one lower/higher than the reviewed record; no key mapping changed.
2. **R08 ambiguous OD sign — addressed without inventing a correction history.** R08 unit27 / global440 has a closed left bowl and a short ascender crossbar. It is recorded as **t/d ambiguous**, candidate plaintext **D/T**, with contextual t/D selected for OD TVEHO. If d/T were selected the literal alternative would be OT TVEHO. The observation, both candidates, selection and selection basis are explicit in `transcription.json`, `index.csv` and `inventory.json`; the decoder prints the ambiguity after the selected literal. No cancellation, direction of alteration or secure clean t is asserted. Source control region `[360,602,460,639]` shows OD and the following TVEHO; same-card D controls are DRAHOU `[842,607,950,643]` and DUCHU `[585,603,663,640]`. These are broad comparison regions, not precise glyph segmentations.
3. **Reproduction metadata — addressed.** Removed the stale claim that no independent-provider review or marker exists and the pre-handover instruction. The introduction, review status, literal/editorial separation and coverage now reflect review1 REVISE and this bounded response. Existing markers/review files were read only. The read-only command now validates three unchanged source hashes, nine local record hashes, all 497 index entries, explicit ambiguity metadata and exact whole-row fixed-key inversion of the selected plaintext. The generator was inspected before use; it writes only work files and first checks the preserved original hashes and fixed-key hash.

Counts remain 497 visible units = 496 unambiguous + one ambiguous selected unit; one CH expands the selected text to 498 base letters. The ambiguous D/T is not removed by successful reproduction or by coherent Czech. The collaborator stopped before closure; root subsequently checked the original-pixel controls, retained the explicit D/T alternative, and verified the documented command. No reviewer verdict has been overwritten.


## Root closure checks after review1

Root compared the original-coordinate native controls with both reviewer panels and the immutable image. The descending p/B in the first TEBRVE differs from the ascending b/P in the second TEPRVE. The R08 sign genuinely shows both bowl and crossbar; context selects D for OD, while T/OT remains explicitly preserved in the indexed record and decoder diagnostic. This is not497securely classified glyphs:496are unambiguous and one is conditional. All three review findings are addressed without changing the key or meaning. The reviewer explicitly permits FINAL after these corrections, with no further round. This is root solver QA, separate from the existing Claude Opus5.5 independent review.

The current full337-contribution/303-HC-ID register still omits this target; expanded public work on other family cards is acknowledged in SOURCES.md. This bounded check does not establish global novelty. Source/review/old marker hashes are checked against the closure-pass protected manifest. The final report and local register entry are prepared from this corrected record before FINAL; no external submission is made. Solver name is TODO because no name was supplied for these entries.
