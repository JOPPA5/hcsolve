# HCP1556 / pc_hcp_237 — known-key solver reading

The photograph carries a Czech private letter to Anna Tichá, dated **26. IV. 1903**. This is a manually transcribed, fixed-family-key reading; it is not a new key discovery or an independent review. No target-specific published plaintext was supplied or consulted. The portal source/status and prior public family-key exposure are recorded in `SOURCES.md`.

**Status:** complete solver candidate, no reviewer acceptance and no claim of `FINAL`. The human override forbids watchers and reviewers. The delegated collaborator created no markers, PDF or register entry; root alone handles handover. All 336 transcribed cipher positions have assignments (including two CH positions); this coverage does not establish that every visual classification is correct. In particular the anomalous M01 `tik` is retained below.

## Physical scope and transcription

Both complete source photographs, including all margins, were visually inspected. There was no attached target transcription, and no OCR was used.

| Region | Orientation and treatment |
|---|---|
| Picture, main handwritten block | Rotate original image **90 degrees clockwise**. Read M01–M16 top to bottom, left to right. Flowers constrain the progressively wider left margin. |
| Picture, independent two bottom lines | Keep original image orientation. Read B01–B02 left to right, after the main block. |
| Picture, date | Ordinary writing, **26. IV. 1903.**, adjacent to the main signature. It is not passed through the cipher key. |
| Picture, remaining field/margins | Floral print, card border/background and collection watermark; no additional handwriting seen. The stroke crossing the floral stem in B01 is retained, not cancelled. |
| Address, handwriting | Ordinary address: “Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek.” Capitals/line division are diplomatic observations. No substitution applied. |
| Address, postal/printed regions | Stamp and overlapping postmarks; some postal numerals/letters are indistinct and are not asserted as plaintext. Multilingual postcard headings, printer/publisher text and number 563, background watermark. No additional cipher block seen. |

`work/rows.json` records the manual class string, literal output, orientation and `[x0,y0,x1,y1]` row box for every physical cipher row. Coordinates use the 674×1024 clockwise image for M rows and the 1024×674 original for B rows. Boxes overlap where ascenders/descenders or sloping baselines require it; neighbouring ink is not a second transcription. Row crops M01–M16 and B01–B02, `row-contact.png`, `coordinate-grid.png`, and the full `picture-clockwise.png` make the positions inspectable. `positions.json` gives each cipher position's row, one-based glyph index, column in the manual class string, class and exact literal expansion.

## Cipher and fixed key

Monoalphabetic family substitution, transferred from the existing `ciphers/hcp-1520/work/key.json`. No new assignment was inferred from grammar. Identifiers are graphical transcription conventions, not a claim that the writer penned Latin ciphertext letters.

| Classes | Literal values |
|---|---|
| `1 2 3 4 5 6 8` | `y u o i e a l` |
| `q g f h t r` | `z k v r d h` |
| `c s n m p b d y H` | `s c m n b p t j ch` |

`H` records the marked/capped G10 family form with value CH, here at M14 positions 6 and 14. It is not an inferred extra letter added by Czech grammar. The rare shallow-v/F class is absent; tall-loop `f` retains V. No secondary accent rules were applied, and no extra marks were automatically removed. Letter accents in the editorial text below are linguistic restoration, separate from the fixed-key literal.

The older local hcp-1520 line01, g/q and m/n photograph controls were consulted to calibrate class appearance. Its pre-existing transcript was also opened; it belongs to a different card, not this target. These references, the public family-key record and available pc199 photographic reference are hash-recorded. The pc199 image was not needed to assign F in this card, which has no F-class occurrence.

## Exact literal Czech

Case is normalised to lowercase; row division, internal line-end hyphens, the anomalous `tik` and spelling are retained. Date and ordinary address remain outside this block.

<!--literal-begin-->
```text
M01 vrely tik, dusin-
M02 ko moje jedina,
M03 za drahy listek.
M04 nezanedbava mne moje
M05 anunka take ve svem
M06 srdecku? mam te, anusko
M07 tolik rad a touzim po tobe
M08 nesmirne! - je p. ridici
M09 sedivy tyz, jemuz nedavno
M10 zemrela pani? - sejdeme se
M11 anunko predraha, behem
M12 kvetna? - tesi se na
M13 drahe radky tve a tisic
M14 vrelych, vasnivych pus ti
M15 posila tvuj stale vzpomi-
M16 najici pepous.
B01 ztratil se jiz nekolikaty muj listek
B02 tobe zaslany. kde vezi toho asi pricina?
```
<!--literal-end-->

## Editorial accented Czech — interpretation

Vřelý **[dík?; doslova „tik“]**, dušinko moje jediná, za drahý lístek. Nezanedbává mne moje Anunka také ve svém srdečku? Mám tě, Anuško, tolik rád a toužím po tobě nesmírně! — Je p. řídící Šedivý týž, jemuž nedávno zemřela paní? — Sejdeme se, Anunko předrahá, během května? — Těší se na drahé řádky tvé a tisíc vřelých, vášnivých pus ti posílá tvůj stále vzpomínající Pepouš.

Ztratil se již několikátý můj lístek tobě zaslaný. Kde vězí toho asi příčina?

Editorial decisions: joining `dušin-ko` and `vzpomí-nající`; adding Czech accents, capitalisation, punctuation and possible surname capital Šedivý. `p.` is retained as an abbreviation, not silently expanded. Anunka/Anuška and Pepouš are readings of the affectionate names, not independently established identities. The candidate `dík` is a linguistic emendation, not the literal key output.

## Slovak translation — based on the editorial reading

Vrelá **[vďaka?; v doslovnom čítaní je „tik“]**, dušička moja jediná, za milý lístok. Nezanedbáva ma moja Anunka aj vo svojom srdiečku? Mám ťa, Anuška, tak rád a nesmierne po tebe túžim! — Je p. riadiaci Šedivý ten istý, ktorému nedávno zomrela manželka? — Stretneme sa, predrahá Anunka, počas mája? — Na tvoje milé riadky sa teší a tisíc vrúcnych, vášnivých bozkov ti posiela tvoj stále spomínajúci Pepouš.

Stratil sa už niekoľký môj lístok poslaný tebe. Kde asi väzí príčina?

## Reproduction and limits

From repository root, one read-only command:

```sh
/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 ciphers/hcp-1556/work/decode.py
```

It verifies hashes for the exact two source photographs and metadata; checks this target's three entries in the now-fixed nine-entry batch source guard; verifies the fixed key equals the older key; decodes all 18 manual rows; performs the actual inverse substitution on the full literal strings, with CH as the only multiletter value; and checks exact row/position/literal equality. The command performs no file writes. It consumes the manual transcription tied by hashes and row crops to the source; it does not derive characters automatically from pixels.

Result: **336 assigned cipher positions, 2 CH expansions, 338 literal letters, 0 unassigned positions**, excluding spaces, punctuation, date and address. Fixed-key inverse and hash equality are mechanical checks, not proof of glyph truth. Evidence for the reading is broad continuous Czech coherence across both separate writing regions, unchanged family assignments and a visible position-level transcript. That coherence is supporting evidence, not permission to repair anomalies.

Remaining visual/interpretive cautions:

- M01 second word `d4g` gives **tik**. Its first glyph has a bowl and rising stroke, unlike the crossed `t` beginning the following `t2c4m-`. A d/t class alternative would give `dik`; it is not substituted into the literal. Root visual control requested.
- g/q classification uses bowl/descender geometry and is especially worth checking at M02 first glyph, M03 first glyph, M09 `d1q`/`y5n2q`, M10 initial `q`, M12 initial `g`, M15 `fqb3n4`, and B01/B02. The assignments are explicit, not unconstrained unknown spans. Root controls can revise an observed class if the photograph warrants it.
- The final B01 glyph of `qdh6d48` crosses the green printed stem; 8/L is retained from its visible lobes. Neither overprint nor a crossing stroke cancels it.
- Two marked G10 forms in M14 are recorded as H/CH. No general diacritic recovery is claimed. The exact intended modern accents, surname spelling, and sender identity remain editorial/contextual questions.
- Postmarks and tiny printer details are outside the cipher claim; no uncertain postal date was invented. No independent human or separate-provider review has occurred.

## Root solver source control

Root inspected both complete originals, all sixteen main rows and both independent bottom rows, then compared the final focused controls against the original pixels. M01's bowl and rising stroke support class d/T, distinct from the crossed t/D beginning DUSIN; literal TIK is retained, and DIK remains editorial. Same-card closed-loop g/K versus open-hook q/Z controls support M02 KO, M03 ZA, M09 TYZ/JEMUZ, M10 ZEMRELA and M12 KVETNA. Both M14 CH caps are visible. B01's final 8/L in ZTRATIL has visible lobes despite its crossing of the printed green stem; no deletion is inferred. The complete B01/B02 continuation is included.

The final panel is `work/focused-controls.png`; an early scratch panel with misregistered labels was replaced before handover and is not evidence for the final records. The documented command passes after these documentation corrections. Root/helper checking is solver collaboration, not independent provider review. Handover does not establish acceptance or authorize a FINAL report or register entry.

## Response to review 1

Reviewer: Claude Opus 5.5, verdict ACCEPT (review/REVIEW1.md, 2026-10-28). The reviewer ran the documented command (output identical to the literal block above), read all 18 cipher rows sign by sign from its own clockwise-rotated 4× crops of source/picture.jpg, and decoded its own transcription with its own statement of the key (review/work/my_decode.py): 336 positions, 338 letters, 2 CH, key one-to-one, all 22 sign classes used, no difference from work/literal-cz.txt. It specifically confirmed the D/T, S/C, B/P, M/N and I/Y pairs everywhere, every K/Z choice (including M09 TÝŽ, M10 ZEMŘELA, B01 ZTRATIL and JIŽ, B02 VĚZÍ), the literal TIK in M01 (looped d-shape = T, distinct from the crossed t-shape = D of DUŠIN- in the same row), both CH signs in M14, and the final L of ZTRATIL across the printed stem. It found no cipher text outside the 16-row block and the 2-line bottom continuation, and no prior published solution of this card. All four findings were minor; none changes a decoded letter.

1. B02 PŘÍČINA, 4th sign, is an unusual form (minor). Accepted as a disclosure. On the reviewer's enlargement (review/work/w-pricina14.png), which I re-inspected for this closing pass, the 4th sign of the last word of B02 (`bh4s4m6`) has a hook at the top left and a long lower stroke curling left; it is taller and more open than the closed angular s-shape (= C) of ŘÍDÍCÍ, TISÍC and NAJÍCÍ, and it lacks the horizontal foot of the digit-1 sign (= Y). The s/C classification is kept: it is the best match to the shape and the only one giving a word (PŘÍČINA, "cause"), which the sentence requires. It is now listed among the uncertainties in the report. No other unflagged odd form was reported.
2. The reproduction command is not portable (minor). Accepted. decode.py uses only the Python standard library. I ran `python3 -I ciphers/hcp-1556/work/decode.py` from the repository root with the system Python: exit 0, `VERIFY: 18 rows; 336 mapped cipher positions; CH=2; unknown=0; literal letters=338; ...`, and the same 18 literal rows. The report gives this portable command; the codex-runtime interpreter named above gives the same result. Note for reproduction from a fresh checkout: the script also verifies hashes of files outside this directory (ciphers/hcp-1520/work/key.json and the hcp-1520 control images, and batches/easy-2026-10-28/ files: the nine-entry source guard, the published family key text and the pc199 reference). At the time of this closing pass those files exist in the working tree but are not yet tracked by git, so they must be committed together with this cipher for the command to run from the GitHub copy. This closing pass changes nothing outside ciphers/hcp-1556.
3. ŠEDIVÝ may be an adjective, not a surname (minor, editorial). Accepted. The normalized Czech keeps the capital (Šedivý, a common Czech surname) as one reading, and the report now states both: "Is the headmaster Mr Šedivý the same one whose wife recently died?" and "Is the grey-haired headmaster the same one whose wife recently died?". The cipher writes no capitals, so the card cannot decide between them.
4. Stale wording (minor, documentation). Accepted. The statements earlier in this file that there is "no reviewer acceptance", that "the human override forbids watchers and reviewers", that "no independent human or separate-provider review has occurred", and that handover does not authorize a FINAL report or register entry describe the state at DONE1 and are left in place as a record; this section supersedes them. Independent review 1 by Claude Opus 5.5 (a separate provider from the solver) returned ACCEPT, and report/report.pdf and register-entry.txt now exist. The report does not repeat the stale wording.

Additional notes from the closing pass: 26 April 1903 was a Sunday. The address side carries an Austrian 5-heller stamp cancelled PRAHA (day and month mostly covered; "6" and "03" visible) and an inverted arrival postmark ŽIROVNICE / SEROWITZ whose visible part reads "27", a roman month ending in V, and "03"; whether the month is IV or V cannot be read, so the postmarks are not used as evidence for or against the date. The register type is recorded as MASC (monoalphabetic substitution with the known family key, including the family's single sign for the digraph CH, which occurs twice here). An English translation was added in the report (SOLUTION.md had the Slovak only).

Remaining uncertainties carried into the report: the literal TIK (a writer's slip; editorial dík); the unusual C sign in PŘÍČINA; Šedivý as surname or adjective; the editorial accents, punctuation and word joins (dušin-ko, vzpomí-nající); the civil identities of Pepouš and of the headmaster; the postmark dates; the key is a transferred family key (hcp-1520, and the published partial key by Maxim Egorov acknowledged in SOURCES.md), not recovered blind from this card; novelty rests on the bounded checks recorded in SOURCES.md and review/REVIEW1.md (portal status Not solved, AI Decipherment Register without this card, Cipher-Atelier readings without card 237).

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-28.
