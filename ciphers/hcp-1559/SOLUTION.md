# HCP1559 / pc_hcp_240 — Anna Tichá / Pepouš family, complete reading (round 2)

> **Current status (after review 1): complete reading, four smudged spans resolved with restorations marked.** The authoritative record is `work/transcription-final.txt` + `work/key-final.json`, reproduced by `python3 ciphers/hcp-1559/work/decode-final.py` (see "Final reading" below). Sections up to "Root bounded QA" are the historical round-1 *partial* record; their words "partial", "no handover", "unknown spans" and the counts 214/219 describe that earlier stage and are kept for traceability (the old `work/decode.py` still verifies that partial record against the first ```` ```text ```` block below).

## Final reading (authoritative)

Notation: plain letters are read from the scan; `[..]` = sign position(s) visible but the letters restored from context only; `(..)` = faint trace read with low confidence. The k-shaped sign is the family G (`G` in `key-final.json`, attested on HCP1541 SVAGRA, HCP1553/1554 TELEGRAM(Y), HCP1570 KOLEGY).

```sh
python3 ciphers/hcp-1559/work/decode-final.py
```

<!--final-begin-->
```plaintext
R01 promin, drahousku, ze dosud neodeslal jsem dopis. jest
R02 zde od stredy pan simulka, svag[r] meho bratra, jemuz
R03 v prazdnych chvilich delam spolecn[ost]. dnes vecernim
R04 vlakem odjede. zitra odeslu psank(o). tisic vrelych, dlouhych
R05 pus sve jedine anunce zasila stale vzpominajici pepous.
```
<!--final-end-->

CHECK line: 5 rows; 221 cipher units = 216 read + 1 low-confidence + 4 restored; no unknown spans.

Editorial Czech: „Promiň, drahoušku, že dosud neodeslal jsem dopis. Jest zde od středy pan Simulka, švag[r] mého bratra, jemuž v prázdných chvílích dělám společn[ost]. Dnes večerním vlakem odjede. Zítra odešlu psánk(o). Tisíc vřelých, dlouhých pus své jediné Anunce zasílá stále vzpomínající Pepouš.“

English: "Forgive me, darling, that I have not yet sent the letter. Since Wednesday Mr Simulka, my brother's brother-in-[law], has been here, and I keep him [company] in idle moments. He leaves by the evening train today. Tomorrow I will send a little letter. A thousand warm, long kisses to his only Anunka sends the ever-remembering Pepouš."

Slovak: „Prepáč, drahúšik, že som ešte neodoslal list. Od stredy je tu pán Simulka, švag[or] môjho brata, ktorému v prázdnych chvíľach robím spoloč[nosť]. Dnes večerným vlakom odíde. Zajtra odošlem list(ok). Tisíc vrúcnych, dlhých bozkov svojej jedinej Anunke posiela stále spomínajúci Pepouš.“

The surname is given as **Simulka** without a háček: nothing in the cipher marks diacritics, and Š would be an editorial guess (no external identification was attempted).

**Solver candidate, not independently reviewed or FINAL.** Five physical handwritten rows become upright after a lossless **90° counterclockwise** rotation. The fixed Anna Tichá family key yields 214 resolved cipher units, including five CH units, and 219 resolved base letters. Four active smudged spans remain unresolved; their original glyph counts and the whole-card denominator are unknown. They are retained, not canceled or filled from grammar.

This is **known-key transfer**, not key discovery or a priority claim. The old HCP1520 key, Maxim Egorov / Cipher-Atelier's published partial family study, and the available pc199 photograph were supplied before this target reading. Expanded public work on other family cards and older local overlaps is credited in `SOURCES.md`; no target-specific published plaintext was supplied or consulted. The pc199 shallow-v/F reference is available but was not needed to assign an F on this card; none is assigned. Root's rendered register observation (337 contributions/303 HC IDs, target absent) is bounded evidence, not global novelty. Root/helper work is solver collaboration, not independent review.

## Sources and physical scope

Root inspected all three rendered portal tabs and exact image modals: Not solved; Czech; substitution; date1903-03-29; recipient Anna Tichá; sender unknown; private collection; no attached target transcription/solution. Both immutable source images and metadata were then read by this collaborator. URLs/provenance are in `SOURCES.md`; originals were not edited. No OCR was used.

| Physical region | Inventory and treatment |
|---|---|
| Picture, lower handwritten block after CCW rotation | Five rows R01–R05, read top to bottom and left to right. All visible active writing belongs to these rows. Four smudged spans remain active unknown ink. |
| Picture, ordinary date beside red verse | `29.III.1903.`; ordinary writing, not passed through the key. |
| Picture, red printed verse | Ordinary Czech print, four lines: “V mém srdci pouze jedno přání: / by láska naše žhoucí, vřelá, / nám nikdy v prsou nevymřela / a blažila nás do skonání!” It is not a cipher block. |
| Picture, remaining field and all margins | Printed couple/children scene, umbrella, clover/floral ornament and border, blank background and collection watermark. No further handwriting identified. |
| Address, ordinary cursive | `Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek.` No substitution applied. |
| Address, remaining print/postal/marginal field | Printed `Dopisnice`, address rules, bottom-left ornamental emblem and `S.73`, stamp and overlapping PRAG / ŽIROVNICE–SEROWITZ postmarks, watermark and otherwise blank margins. Indistinct postal numerals are not asserted as dates or cipher. No additional cipher region identified. |

R04 ZITRA is underlined. The underline adds no letter and does not cancel the word. No smudged span is automatically treated as a deletion.

## Fixed key and manual procedure

The target `work/key.json` is a **byte-identical copy** of `ciphers/hcp-1520/work/key.json`; no assignment was added or changed.

| Classes | Literal values |
|---|---|
| `1 2 3 4 5 6 8` | `y u o i e a l` |
| `q g f h t r` | `z k v r d h` |
| `c s n m p b d y H` | `s c m n b p t j ch` |

These are arbitrary graphical labels, not diplomatic font replicas. In particular m/N and n/M, c/S and s/C, t/D and d/T, b/P and p/B remain distinct. `H` records the established marked G10/CH form as one complete cipher unit. It occurs once in PRAZDNYCH, twice in CHVILICH, once in VRELYCH and once in DLOUHYCH. Its value is fixed before this card; the marks were not added from an expected Czech word. Secondary accent rules were not applied. Tall-loop f retains V; no shallow-v/F or new G value was assigned.

`work/transcription.json` stores native upright row boxes, the ordered known-text/unknown-span elements, exact class strings and literal output. `positions.csv` enumerates **resolved units only**: row, known-unit index, element index, offset within the known element, class and literal value. Because unknown spans have unknown original lengths, a later known-unit index is not claimed to be its absolute physical glyph ordinal. Unknown-span IDs and context boxes are separate. Boxes overlap where sloping handwriting and descenders require it; they do not imply duplicate transcription.

`upright.png`, `indexed.png`, R01–R05 crops, `controls.png` and individual `control-*.png` retain source-linked visual evidence. `controls.json` records the exact crop coordinates and transformations. Display scaling is uniform nearest-neighbour without denoising; it adds no source evidence.

## Exact literal Czech

Lowercase is normalised. Accents are not supplied. The opaque markers denote unresolved **spans**, not one fake unknown character or a claim about their length.

```text
R01 promin, drahousku, ze dosud neodesla<UNK:U01> jsem dopis. jest
R02 zde od stredy pan simulka, sva<UNK:U02> meho bratra, jemuz
R03 v prazdnych chvilich delam spolecn<UNK:U03>. dnes vecernim
R04 vlakem odjede. zitra odeslu psank<UNK:U04>. tisic vrelych, dlouhych
R05 pus sve jedine anunce zasila stale vzpominajici pepous.
```

## Editorial accented Czech — partial interpretation

The following restores Czech accents, case and ordinary word spacing only in the resolved material. It does not complete the four unreadable spans. The string „simulka“ is retained without inferred name accents or a proposed identity. `[U01]` etc. mean the same unresolved spans as above, with unknown length.

Promiň, drahoušku, že dosud neodesla[U01] jsem dopis. Jest zde od středy pan „simulka“, sva[U02] mého bratra, jemuž v prázdných chvílích dělám společn[U03]. Dnes večerním vlakem odjede. **Zítra** odešlu psánk[U04]. Tisíc vřelých, dlouhých pus své jediné Anunce zasílá stále vzpomínající Pepouš.

ANUNCE and PEPOUS are affectionate name forms read from the fixed key. Their editorial accents/capitalisation do not establish the sender's civil identity. ZASILA retains the source I/4; no I/Y normalization was inserted into the literal.

## Slovak translation — partial

Prepáč, drahúšik, že som dosiaľ neodosla[U01] list. Je tu od stredy pán „simulka“, sva[U02] môjho brata, ktorému v prázdnych chvíľach robím „společn[U03]“ [neúplný výraz v origináli]. Dnes večerným vlakom odíde. **Zajtra** odošlem „psánk[U04]“ [neúplné slovo v origináli]. Tisíc vrúcnych, dlhých bozkov svojej jedinej Anunke posiela stále spomínajúci Pepouš.

The unresolved expressions are deliberately not translated by inventing their missing ending or a family relationship. This is a partial translation of the partial literal reading.

## Uncertainty and visual controls

| Span | What is visible, what remains unknown |
|---|---|
| U01, R01 after NEODESLA | Smudged terminal ink with possible 8/L-like lobes. A final L is not inserted into the literal. Class and original glyph count remain unasserted. |
| U02, R02 after SVA | Tall-loop ink followed by a dark smear; reliable segmentation and class assignment are unresolved. No G or any other new assignment is inferred from a possible expected word. |
| U03, R03 after SPOLECN | Terminal smudged material before a separate punctuation dot. Neither an expected word ending nor a fixed number of original letters is supplied. |
| U04, R04 after PSANK | Smudged terminal ink with a possible 3/O-like trace. It is not counted as one resolved O merely because a word would fit. |

Each span stays **active unknown ink**. Unknown units and the original total are `unknown`, so no full-card percentage or “all symbols solved” claim is made.

Root controls requested: `control-U01.png` through `control-U04.png`; `control-b-p.png` for PAN versus BRATRA and the unresolved named string; `control-t-d.png` for ODJEDE/ZITRA; `control-m-n-I-Y.png` for PRAZDNYCH/CHVILICH/DELAM; `control-small-C.png` for the small angular C in ANUNCE and I in ZASILA; and `control-closing.png` for the closing. The known small C is explicitly present in `6m2ms5`, not inserted from grammar.

Punctuation/word boundaries and restored accents remain editorial. The string SIMULKA has no verified diacritics or biographical identity. No uncertain name, surname or missing ink has been completed from context. Smear visibility may support a narrower reading during root QA; hashes and inverse checks alone cannot decide it.

## Reproduction and evidence

From repository root, one **read-only** command:

```sh
python3 ciphers/hcp-1559/work/decode.py
```

It verifies both source photographs and metadata, this target's own three entries in the frozen nine-source guard, reference and record/crop/code hashes, exact fixed-key equality, every resolved indexed unit, class counts and literal equality across JSON/text/SOLUTION. It also performs the actual inverse on each **whole literal row**, using longest-match CH; unknown span markers remain opaque and are checked by ID. It does not claim to encrypt/decrypt the unknown ink or to extract handwriting automatically from pixels. The default command writes nothing.

Current result: **5 physical rows;214 mapped cipher units;5 CH expansions;219 mapped base letters;22 observed assigned classes;4 active unknown spans. Unknown glyph count and original total: unknown.** Broad continuous Czech across the resolved text, the fixed family table, preserved physical order and the affectionate closing support the reading. They do not justify filling the four spans or treating mechanical checks as glyph truth.

This collaborator creates no watcher, reviewer, marker, review output, PDF, register entry or git action. Root owns QA and any handover/closure. There is no independent-review acceptance or FINAL claim.


## Bounded root QA correction — R02 initial

The earlier literal KDE disagreed with the editorial ZDE / Slovak “Je tu”. A fresh source-only comparison of the R02 initial against q/Z in the same card's ZE and ZITRA, and g/K in SIMULKA and DRAHOUSKU, resolves it as **q/Z**: compact bowl and an open hooked tail, rather than the looped descending g/K form. Changed R02 `gt5`→`qt5`, literal **KDE→ZDE**. The editorial Czech and Slovak now reflect the literal source reading, not an unstated grammatical repair. Comparison crops and exact native boxes are in `work/qg-root-control.png` / `.json`.

One known-position label changed K→Z. Preferred class totals are now g/K **4** (was5), q/Z **7** (was6). Counts remain214 mapped units,5CH,219 mapped letters; all four unknown spans and their unknown original lengths remain opaque and unchanged. The fixed key and original sources were not changed. Records, saved literal/index and hash manifest were regenerated; the documented read-only decoder was revalidated. This root QA is solver collaboration, not independent acceptance.

## Root bounded QA

Root inspected both complete source sides/all margins, all five row crops, the nine ambiguity/class controls and the five-panel same-card q/g comparison. R02 initial compact hooked q/Z supports ZDE; original KDE was a transcription error, now corrected in the literal, indices, class counts and controls. Editorial Czech and Slovak follow the corrected source reading, rather than silently replacing K with Z. Global known index44 is a resolved-unit index only, not an absolute whole-card ordinal after unknown spans.

All four smudged runs remain active opaque spans of unknown length. No expected L/O ending, new G mapping or inferred relationship was supplied. The documented command passes and writes no files; root independently verified original pixels in the oriented image, five 3x row crops, nine 4x controls and five 7x q/g crops. The record remains PARTIAL with no DONE, PDF, register entry or FINAL. These are solver-side checks, not independent review.

## Completion and handover — Claude Opus 5.5 as solver, 2026-10-29

Status: **complete reading, handed to review (DONE1).**

| Span | Evidence (work/control-U0n.png) | Reading |
|---|---|---|
| U01, R01 | After `…86` (…LA) a further `8` with two lobes is plainly visible (`868`) | **NEODESLAL** |
| U02, R02 | After `f6` (VA) comes the **k-shaped sign**, the family's G (SVAGRA on HCP1541, TELEGRAM(Y) on HCP1553/1554, KOLEGY on HCP1570), then a smear of one sign | **SVAGR** (*švagr*, “brother-in-law”); the last sign R is restored |
| U03, R03 | After SPOLECN, traces of three small signs before the dot: a 3-like bowl, a c-hook and a looped stem | **SPOLECNOST** (*dělám společnost*, “I keep [him] company”); three sign positions seen, their classes inferred from context (see Response to review 1) |
| U04, R04 | After `ng` (NK) a small `3`-like trace before the dot | **PSANKO** |

(Superseded by "Final reading" at the top: restorations are now bracketed and the name is kept as Simulka.) Editorial Czech: “Promiň, drahoušku, že dosud neodeslal jsem dopis. Jest zde
od středy pan Šimulka, švagr mého bratra, jemuž v prázdných chvílích dělám
společnost. Dnes večerním vlakem odjede. Zítra odešlu psánko. Tisíc vřelých,
dlouhých pus své jediné Anunce zasílá stále vzpomínající Pepouš.”

Slovak: „Prepáč, miláčik, že som ešte neodoslal list. Od stredy je tu pán
Šimulka, švagor môjho brata, ktorému vo voľných chvíľach robím spoločnosť.
Dnes večerným vlakom odíde. Zajtra odošlem list. Tisíc vrúcnych, dlhých
bozkov svojej jedinej Anunke posiela stále spomínajúci Pepouš.“

Reproduce with the command given earlier in this file. The family key is
credited to earlier family cards and the published partial study by Maxim Egorov.

## Response to review 1

Verdict REVISE (Claude Opus 5.5 reviewer). All five findings accepted and fixed; the reading itself is unchanged apart from marking restorations.

1. **[major] Command did not reproduce the claimed plaintext — fixed.** Completions are now encoded in `work/transcription-final.txt` (R01 `m53t5c868`, R02 `cf6G[h]`, R03 `cb385sm[3cd]`, R04 `bc6mg(3)`); `work/key-final.json` is the HCP1520 family key plus `"G": "g"` for the k-shaped sign (same label as HCP1554 key-v2 and HCP1570), with the attestations named in the file header. `work/decode-final.py` asserts that the key equals the family key plus G only, decodes, and prints the final text shown in "Final reading"; re-run on 2026-10-29: 221 units = 216 read + 1 low-confidence + 4 restored, no unknown spans. The status text at the top now states the current status and marks the earlier sections as the historical round-1 partial record (the old `decode.py` and its 214/219 counts belong to that record and still pass).
2. **[major] Restorations not marked — fixed.** Literal, editorial Czech, English and Slovak now show švag[r], společn[ost] and psánk(o); NEODESLAL stays unbracketed (U01 `868`, second `8` with two lobes clearly visible, confirmed on `review/work/U01b.png`).
3. **[minor] Silent Š in the name — fixed.** Kept as "Simulka"; the final section states that a háček would be editorial and is not supplied.
4. **[minor] U03 glyph classes overstated — fixed.** Re-examined `review/work/U03b.png`: three positions are visible (a 4/5/3-like stroke, a small closed loop, a stemmed 6/b/d-like form). The completion-table wording now says the positions are seen and their classes inferred; in the transcription they are fully bracketed `[3cd]` and counted as restored, not read.
5. **[minor] Stale wording — fixed** by the status banner and the authoritative "Final reading" section, which supersede the round-1 uncertainty table and the "no full-card percentage" statement. Final uncertainty: R in SVAGR and OST in SPOLECNOST are context restorations (positions visible); O in PSANKO is a low-confidence trace; the identity of Simulka and the brother is unverified; word division and accents are editorial.
