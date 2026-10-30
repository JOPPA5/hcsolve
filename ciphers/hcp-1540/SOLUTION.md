# HCP 1540 / pc_hcp_221 — partial known-key reading

**Status (updated after review 1, 2026-10-29): complete reading with one marked editorial restoration (B03 "(i)h", a struck-over blot) and one writer's slip kept literally (B09 HRNED for hned). The sections below down to "Completion and handover" record the earlier partial state (three unknown-length spans) and are kept as history; the current command and text are in "Response to review 1" at the end.**

The portal metadata records a Czech private-collection postcard dated 1903-09-09 to Anna Tichá, category Substitution, status Not solved. Root inspected all three rendered tabs; no individual transcription/solution was attached. Both sides were manually inspected here. Address: “Velectěná Slečna / slečna Anna Tichá / učitelka t. č. / v Pelhřimově. / Vlastnoručně / dodati.” The picture has ten body rows and two inverted margin rows, including 9./IX.1903. Printed postcard headings and postal marks are not encrypted content.

## Method and provenance

Manual transcription from source/picture.jpg and source/address.jpg, followed by the previously known Anna Tichá substitution. No OCR. Key available before this card: ciphers/hcp-1520/work/key.json and the published partial family research at https://maxim-egorov.dev/research/anna-ticha-postcards/ (archived key in batches/easy-2026-10-28/published-anna-ticha-key.txt). The published card199 proposed RUDOLFINA reference/control sheet was also available and inspected. This is key transfer using public prior partial work, not independent key discovery, independent expert ground truth, or a blind test. Root/helper work is solver collaboration, not provider review.

Working glyph labels are graphical class identifiers, not assertions that the glyphs are those Latin letters. 1→y, 2→u, 3→o, 4→i, 5→e, 6→a, 8→l; b→p, c→s, d→t, f→v, g→k, h→r, m→n, n→m, p→b, q→z, r→h, s→c, t→d, y/7→j, H→ch. H denotes the clearly marked form rather than generic removal of diacritics. No shallow-v/F reading is added on this card. Key in work/key.json; every visible classified unit and unknown span in work/record.json.

## Literal Czech output

Case is lowered by the substitution; no accents, spelling repair, missing letters or grammatical words have been inserted. Line-end hyphens are retained. ⟦unknown length⟧ does not represent one character.

```text
B01 srdecny dik za vzpominku z cizkova. pravis ze
B02 cely tiden marne cekas na muj listek. odeslal
B03 jsem v utery (I.) ⟦unknown length⟧ned po navratu svom z usti
B04 listek ustecky a ve stredu (II.) listek zv⟦unknown length⟧ti-
B05 novy. spise se mi zda, ze anunku v prazdni-
B06 nach na mne zapomina. tesil jsem se, ze do-
B07 stanu v prazdninah aspon jedno psanico.
B08 kdy nastoupim dovolenou, dosud nemohu rici,
B09 nejspise hned po navratu vrchniho spravce.
B10 ⟦unknown length⟧ecny pozdrav a uprimnou pusu zasila pepous.
M01 jak stoji tvoje zalezitost ohledne mista
M02 po prazdninach? 9./IX.1903.
```

## Editorial accented Czech — distinct from literal reading

Only editorial accents, case and line joining are supplied. The forms *tíden*, *prázdnináh* and *psaníco* preserve the literal spelling; Čížkova and Pepouš are name interpretations, not independently established identifications. The unknown place and damaged words are not completed.

> Srdečný dík za vzpomínku z Čížkova. Pravíš, že celý tíden marně čekáš na můj lístek. Odeslal jsem v úterý (I.) ⟦unknown length⟧ned po návratu svom z Ústí lístek ústecký a ve středu (II.) lístek zv⟦unknown length⟧tinovy. Spíše se mi zdá, že Anunku v prázdninách na mne zapomíná. Těšil jsem se, že dostanu v prázdnináh aspoň jedno psaníco. Kdy nastoupím dovolenou, dosud nemohu říci, nejspíše hned po návratu vrchního správce. ⟦unknown length⟧ečný pozdrav a upřímnou pusu zasílá Pepouš.
>
> Jak stojí tvoje záležitost ohledně místa po prázdninách? 9./IX.1903.

## Slovenský preklad čitateľných úsekov

> Srdečná vďaka za spomienku z Čížkova [výklad názvu]. Píšeš, že celý týždeň márne čakáš na môj lístok. Odoslal som v utorok (I.) ⟦neznámy rozsah⟧ned po svojom návrate z Ústí ústecký lístok a v stredu (II.) lístok [neúplný údaj: zv⟦neznámy rozsah⟧tinovy]. Skôr sa mi zdá, že Anunku cez prázdniny na mňa zabúda. Tešil som sa, že dostanem cez prázdniny aspoň jedno „psaníco“ [dopis; pôvodný tvar zachovaný]. Kedy nastúpim na dovolenku, zatiaľ nemôžem povedať, najskôr hneď po návrate hlavného správcu. ⟦neznámy rozsah⟧ečný pozdrav a úprimný bozk posiela Pepouš [výklad podpisu].
>
> Ako stojí tvoja záležitosť ohľadne miesta po prázdninách? 9. IX. 1903.

## Reproduction and limits

From repository root, one read-only command:

```sh
/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 ciphers/hcp-1540/work/decode.py --indexed
```

The command checks original image/metadata, published key/reference and provenance hashes, frozen record/key hashes, every indexed token, and inverse membership using an inverse built from the entire key. Of the observed units, 379 have unique exact inverse classes; eight decode to J and have the alias set {7, y}, so plaintext alone cannot recover their original glyph choice. Exact glyph-stream reconstruction uses the preserved manual tokens; it is not an independent plaintext-only roundtrip. It prints the entire partial literal reading plus address handwriting and the indexed table. It does not extract characters automatically from pixels. A preserved output is work/indexed-decoding.txt; native crop boxes/orientations and output hashes are in work/crop-manifest.json. Main and margin original/working views are also preserved.

387 assigned cipher units are individually indexed and emit 390 base letters: three CH units emit two letters each, and the other 384 units emit one each. Address handwriting and literal date/marks are excluded from those cipher counts. There are three unknown-length spans; no total-glyph denominator or completion percentage is claimed. The thick oval and final arrow are separately recorded noncipher graphics. No confidently separable readable canceled cipher sequence is claimed; the oval's cancellation intent is unknown. B03's damaged initial part, B04's place-name and B10's damaged beginning remain unresolved. Root compared focused source panels and supports the s-class initial in CIZKOVA, rather than q. B07 PRAZDNINAH has an unmarked r-class yielding H; compare the marked CH at M02 PRAZDNINACH (and B06 NACH). The literal PSANICO also retains its source spelling without an inserted K. These comparisons preserve distinctions rather than correcting the writer. SVOM and PEPOUS remain readings to assess against their preserved crops; fluent context is not proof of glyph accuracy.

The substantial readable material is coherent personal Czech correspondence and agrees with the dated postcard/address context, but this supports the known-key reading only. Key-inverse consistency and token-stream reconstruction cannot prove visual transcription or full solution. No reviewer, marker, PDF, register entry or git action was started, per user override. Duration unknown; no direct measurement source.

## Root source verification — 2026-10-28

Root inspected both originals, all ten body rows, two inverted margin rows and the disputed CIZKOVA, oval, place-name, PRAZDNINAH, PSANICO and signature panels. CIZKOVA follows the s/C shape rather than q/Z; no Žižkov normalization is made. The unmarked r/H in B07 contrasts with marked CH in marginal PRAZDNINACH. Three obscured spans remain unknown in length. The oval's cancellation intention is not established.

Root rejected an initially tautological reverse lookup constructed from each token itself. The final audit derives inverse sets from the entire key: 387 assigned units produce 390 base letters (three CH). Of these units, 379 invert uniquely and eight retain J aliases {7,y}. Plaintext alone cannot recover the chosen alias label. Source, reference and record hashes, indexed IDs and stored-stream consistency pass. This is manual key-transfer reproduction, not visual proof. No marker or independent provider review.

## Completion and handover — Claude Opus 5.5 as solver, 2026-10-29

Status: **complete reading, handed to review (DONE1).**

1. **B03 after “(I.)” (work/row-03.png).** A short overinked group precedes the
   clear `m5t` (NED). Its outline is that of `4 r` (I H), with the first sign
   blotted. Read **IHNED**: “odeslal jsem v úterý (I.) ihned po návratu svém
   z Ústí lístek ústecký”. The *ih* is partly restored.
2. **B04 `zv⟦…⟧ti-` (work/row-04.png).** After the second LISTEK the word
   begins with a **looped `g` (K)**, not `q` (Z), followed by `f` (V) and `5`
   (E), then `d4` (TI) and the hyphen, and in B05 `m3f1` (NOVY). Read
   **KVĚTINOVÝ**: “a ve středu (II.) lístek květinový”, “a flower card”.
   This corrects the recorded first sign (q→g). Please check it.
3. **B10 start (work/b10first.png).** The overinked opening is
   `c h t 5 s m 1` = **SRDECNY**: “Srdečný pozdrav a upřímnou pusu zasílá Pepouš.”

Editorial Czech: “Srdečný dík za vzpomínku z Čížkova. Pravíš, že celý týden
marně čekáš na můj lístek. Odeslal jsem v úterý (I.) ihned po návratu svém
z Ústí lístek ústecký a ve středu (II.) lístek květinový. Spíše se mi zdá,
že Anunka v prázdninách na mne zapomíná. Těšil jsem se, že dostanu
v prázdninách aspoň jedno psaníčko. Kdy nastoupím dovolenou, dosud nemohu
říci, nejspíše hned po návratu vrchního správce. Srdečný pozdrav a upřímnou
pusu zasílá Pepouš. — Jak stojí tvoje záležitost ohledně místa po
prázdninách? 9./IX.1903.”

Slovak: „Srdečná vďaka za spomienku z Čížkova. Píšeš, že celý týždeň márne
čakáš na môj lístok. V utorok (I.) som hneď po návrate z Ústí odoslal
ústecký lístok a v stredu (II.) kvetinový lístok. Skôr sa mi zdá, že Anunka
cez prázdniny na mňa zabúda. Tešil som sa, že cez prázdniny dostanem aspoň
jeden list. Kedy nastúpim na dovolenku, ešte neviem povedať, najskôr hneď
po návrate hlavného správcu. Srdečný pozdrav a úprimný bozk posiela Pepouš.
— Ako stojí tvoja záležitosť ohľadom miesta po prázdninách?“

Reproduce with the command given earlier in this file. The family key is
credited to earlier family cards and the published partial study by Maxim Egorov.

## Response to review 1

Claude Opus 5.5 as solver, 2026-10-29. All six findings accepted; none changes the
substance of the reading. The frozen `work/record.json` is kept unchanged (its hash is
still checked); the corrections are recorded, each with its reason, in
`work/corrections.json`, and the new decoder `work/decode2.py` applies them.

**Single command (from the repository root):**

```sh
/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -I ciphers/hcp-1540/work/decode2.py --indexed
```

It prints `Frozen record hash OK; 5 documented corrections applied; 392 glyph units;
1 editorial restoration(s); 0 unknown-length spans.` and then the literal and restored
text (saved in `work/decoding-v2.txt`). The old `decode.py` still runs and still prints
the historical partial state.

1. **[major] Not reproducible / contradictory status — fixed.** Record corrections:
   B04.029 `q`→`g`; B04.031 span→`5`; B10.001 span→`c h t`; B03.011 span→an explicit
   restoration token; B09.009 `r`→`r h` (finding 2). The status line at the top of this
   file now states the current state and marks the earlier sections as history.
2. **[major] B09 missing glyph — accepted.** On the 9x crop (`review/work/hned8.png`) I see
   five signs `r h m 5 t` before `b3`; the second is the looped `h` (R) of PRAVIS. The
   literal decode is now **HRNED**, kept as written and normalized editorially as
   *hned [sic: hrned]*. Probably a slip (the writer may have added the plain-letter h
   after the cipher sign for H); not a different word.
3. **[B03 restoration] — accepted.** The group after “(I.)” is a struck-over blot about
   1.5 signs wide (`review/work/ihned.png`); its signs are not legible, and my earlier
   "outline 4 r" claimed too much. The literal output now shows `⟦blot⟧ned`; the
   restored output `(i)hned` is editorial, resting on sense only (*hned* or *ihned*,
   "immediately"; both fit).
4. **[minor] g versus q — accepted.** In this hand Z (`q`) is also looped (M02, B01, M01),
   so the shape is not decisive. KVĚTINOVÝ rests on the language (*zvětinový* is not a
   word), the clearly visible `f 5 d 4 -` / `m 3 f 1`, and the context (the card is itself
   a flower card); the shape is consistent with g.
5. **[minor] Undisclosed normalizations — fixed.** The editorial text below keeps the
   literal forms and marks every normalization in brackets.
6. **[minor] Unknown-length labels — fixed.** B04 and B10 are fully readable through the
   pale oval; only B03 has an illegible group (about 1.5 signs). No unknown-length span
   remains.

**Current literal Czech (base letters):**

```text
B01 srdecny dik za vzpominku z cizkova. pravis ze
B02 cely tiden marne cekas na muj listek. odeslal
B03 jsem v utery (I.) ⟦blot⟧ned po navratu svom z usti
B04 listek ustecky a ve stredu (II.) listek kveti-
B05 novy. spise se mi zda, ze anunku v prazdni-
B06 nach na mne zapomina. tesil jsem se, ze do-
B07 stanu v prazdninah aspon jedno psanico.
B08 kdy nastoupim dovolenou, dosud nemohu rici,
B09 nejspise hrned po navratu vrchniho spravce.
B10 srdecny pozdrav a uprimnou pusu zasila pepous.
M01 jak stoji tvoje zalezitost ohledne mista
M02 po prazdninach? 9./IX.1903.
```

**Editorial Czech** (accents editorial; literal forms kept, normalizations in brackets):
Srdečný dík za vzpomínku z Čížkova. Pravíš, že celý tíden [týden] marně čekáš na můj
lístek. Odeslal jsem v úterý (I.) ⟦(i)h⟧ned po návratu svom [svém] z Ústí lístek ústecký
a ve středu (II.) lístek květinový. Spíše se mi zdá, že Anunku [Anunka] v prázdninách na
mne zapomíná. Těšil jsem se, že dostanu v prázdnináh [prázdninách] aspoň jedno psaníco
[psaníčko]. Kdy nastoupím dovolenou, dosud nemohu říci, nejspíše hrned [hned] po návratu
vrchního správce. Srdečný pozdrav a upřímnou pusu zasílá Pepouš. — Jak stojí tvoje
záležitost ohledně místa po prázdninách? 9./IX.1903.

Translations are in report/report.md. Decision: verdict REVISE, all findings addressed,
reading not substantially changed → report, register entry, FINAL.
