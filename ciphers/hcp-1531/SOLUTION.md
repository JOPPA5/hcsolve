# HCP 1531 — pc_hcp_212

**Complete reading after review 1 (verdict REVISE, findings addressed).** All 383 cipher positions are assigned; one of them (R12, PSAN[I]) is a contextual restoration of a shadowed sign, shown in brackets. This is application of the known Anna Tichá / Pepouš family key, not independent key recovery. The letter (11 Nov 1903) apologises for a late reply, reports a headache and flu on Sunday and Monday, and work piling up, says a letter is being written, and closes with kisses from Pepouš.

Credit: initial transcription, controls and partial decipherment (two units open) by an OpenAI GPT solver (GPT-6 Astra) with root collaboration on 2026-10-28; completion and handover by Claude Opus 5.5 on 2026-10-29; review 1 by a separate Claude Opus 5.5 agent; corrections after review by Claude Opus 5.5 on 2026-10-29. Sections below "Root verification" are kept as history; the current state is given in this header, in "Literal Czech base text" and in "Response to review 1".

## Sources and context

Root inspected rendered General, Description and Attachments on 2026-10-28: [portal HCP 1531](https://crypto.hcportal.eu/dashboard/cryptograms/1531), name pc_hcp_212, **Not solved**, Czech, Substitution, private collection, unknown sender, recipient Anna Tichá, date 1903-11-11. No target plaintext or transcription was attached. The picture has a handwritten ordinary date `11./XI.1903`; the address side calls Anna Tichá a teacher in Žirovnice near Počátky. Neither date nor address is cipher text. The sender's civil identity is not established by the nickname PEPOUS/PEPOUSE.

Root captured both originals and metadata before this solver began; their exact URLs and provenance are in `SOURCES.md`. Sources were not changed or downloaded again. Both sides were inspected. All cipher text is on the picture side: nine upper/right rows and eight lower/right rows. The lower rows curve/extend leftward; these are included rather than treating the opening block as the complete message.

The HCP 1520–1527 family key was supplied at the start. A generic partial key was already published by Maxim Egorov / Cipher-Atelier, [Anna Tichá postcards](https://maxim-egorov.dev/research/anna-ticha-postcards/); root's source record and `batches/easy-2026-10-28/published-anna-ticha-key.txt` document this. Root's recent index check listed eleven partial card readings, but pc210–212 were absent. No published target plaintext was supplied. The rendered AI register check found 158 contributions / 124 HC IDs, target absent. These bounded observations do not establish worldwide novelty. Root subsequently compared this target's original-pixel controls as solver collaboration; that was not an independent blind review.

## Cipher and key

Monoalphabetic substitution with handwritten digit and Latin-like forms, including one special unit for CH. Labels below are conventional shape-class names, not a diplomatic typeface. In particular `m` means N, `n` means M, and `ř` is a neutral label for the special CH shape, not plaintext Ř. The tentative shallow-v/F inference from HCP 1526 was not needed or imported.

| Shape | Plain | Shape | Plain | Shape | Plain | Shape | Plain |
|---|---|---|---|---|---|---|---|
| 1 | Y | 2 | U | 3 | O | 4 | I |
| 5 | E | 6 | A | 7 | J | 8 | L |
| b | P | c | S | d | T | f | V |
| g | K | h | R | m | N | n | M |
| p | B | q | Z | r | H | s | C |
| t | D | ř | CH | | | | |

The key is stored in `work/key.json` and is identical to the family key in `ciphers/hcp-1545/work/key.json`.

## Reproduction and image evidence

Single reproduction command from repository root:

```sh
python3 ciphers/hcp-1531/work/decode.py
```

This command is read-only by default and uses only Python's standard library. It verifies all three immutable source hashes and three record hashes, reads the manual shape transcription in `work/transcription.json`, applies the key to every assigned unit, marks the one contextual restoration (R12 PSAN[I]) in brackets, verifies the entire ordinal inventory in `work/positions.csv`, and checks an exact tokenwise inverse-key round trip for every assigned unit. It prints the final literal plaintext below. It does not OCR the image or derive the manual transcription automatically. A round trip establishes internal consistency, not that each shape was visually identified correctly.

The original 1024×674 picture is used without rotation. Each JSON row has a source-image bounding box; `work/indexed.png` locates all 17 rows, and `work/R01.png` through `work/R17.png` are enlarged original-pixel row crops. `work/focused-controls.png` and especially `work/side-by-side-controls.png` compare the questionable source forms with local forms. Their JSON files state exact original coordinate boxes. Glyph ordinals within a row do not claim individual pixel bounding boxes. `build-record.py` and `make-controls.py` are explicit generators, not part of the default read-only command; the latter uses Pillow. Brightened diagnostic images are supplementary only, while the controls use original pixels.

| Row | Original box (x0,y0,x1,y1) | Positions |
|---|---|---:|
| R01 | 580,37,973,79 | 26 |
| R02 | 584,69,973,104 | 25 |
| R03 | 585,94,975,132 | 28 |
| R04 | 582,120,970,157 | 24 |
| R05 | 578,148,975,185 | 25 |
| R06 | 576,176,972,211 | 25 |
| R07 | 576,202,972,239 | 23 |
| R08 | 575,231,968,268 | 22 |
| R09 | 573,254,970,291 | 21 |
| R10 | 673,425,954,464 | 18 |
| R11 | 669,459,956,495 | 17 |
| R12 | 662,485,958,522 | 19 |
| R13 | 662,515,960,549 | 18 |
| R14 | 567,539,959,576 | 22 |
| R15 | 517,568,955,603 | 28 |
| R16 | 478,590,950,629 | 30 |
| R17 | 479,613,720,642 | 12 |

Immutable SHA-256 values:

```text
picture.jpg  9db971666a79344768c3dfd93c9d0f08a95f9606e6224033abbec074054855f4
address.jpg  0c12d46820b3ccd146cc2436d2b38dcd28b4bcd9d57f415bb30e690589d82fa0
metadata.md  eab04eb78b61e103ab54cf9d7f6b926ba0d49cec979f89ddf9f2eb22f837064d
```

## Literal Czech base text

Output of the command. Line breaks and the PRO-/MIN division are retained; accents are not encoded. `[I]` is a restoration from context, not a visual reading.

```text
VRELOU PUSU ZA DRAHY LISTEK. PRO-
MIN, ZE NEODPOVEDEL JSEM SVEMU
SRDECKU DOSUD. V SOBOTU ROZBOLELA
SE MI HLAVA A TRAPILA MNE AZ DO
VCEREJSKA. BYLA TO MALA CHRIPKA,
NASLEDKEM KTERE JSEM V NEDELI
A V PONDELI MUSIL ULEHNOUTI.
PRISLO MI TO VELICE NEVHOD,
PONEVADZ PRAVE NYNI JSEM
ZAHRNIT PRACI, KTEROU
NIKDO ZA MNE NEUDELA.
PSAN[I] JE JIZ ROZEPSANO,
ODESLU JE CO NEJDRIVE.
CO DELA MOJE SRDECKO? TISIC
VRELYCH POZDRAVU OD PEPOUSE, KTERY
V DUCHU NEOSISLNE KRATE DRAHOU TVOJI
HLAVINKU LIBA.
```

## Editorial Czech with accents

Accents, capitals and the PRO-/MIN join are editorial. Two literal anomalies are normalised and marked: ZAHRNIT → *zahrnut* and NEOSISLNE KRATE → *nesčíslněkráte*.

> Vřelou pusu za drahý lístek. Promiň, že neodpověděl jsem svému srdéčku dosud. V sobotu rozbolela se mi hlava a trápila mne až do včerejška. Byla to malá chřipka, následkem které jsem v neděli a v pondělí musil ulehnouti. Přišlo mi to velice nevhod, poněvadž právě nyní jsem zahrnut [ZAHRNIT] prací, kterou nikdo za mne neudělá. Psan[í] je již rozepsáno, odešlu je co nejdříve.
>
> Co dělá moje srdéčko? Tisíc vřelých pozdravů od Pepouše, který v duchu nesčíslněkráte [NEOSISLNE KRATE] drahou tvoji hlavinku líbá.

## English translation

> A warm kiss for your dear card. Forgive me that I have not yet answered my sweetheart. On Saturday I got a headache, and it tormented me until yesterday. It was a mild flu, because of which I had to lie down on Sunday and Monday. It came at a very bad time, since just now I am swamped with work that nobody will do for me. The letter is already begun; I will send it as soon as possible.
>
> How is my sweetheart? A thousand warm greetings from Pepouš, who in spirit kisses your dear little head countless times.

## Slovak translation

> Vrúcny bozk za drahý lístok. Prepáč, že som svojmu srdiečku doteraz neodpovedal. V sobotu ma rozbolela hlava a trápila ma až do včera. Bola to malá chrípka, kvôli ktorej som musel v nedeľu a v pondelok ležať. Prišlo mi to veľmi nevhod, pretože práve teraz som zavalený prácou, ktorú za mňa nikto neurobí. List je už rozpísaný, odošlem ho čo najskôr.
>
> Čo robí moje srdiečko? Tisíc vrúcnych pozdravov od Pepouša, ktorý v duchu nespočetnekrát bozkáva tvoju drahú hlávku.

## Remaining uncertainty

1. **R12 PSAN[I]** (global ordinal 259): after `m` the photograph's shadow covers a closed bowl with a long descender reaching into R13 and a further faint oval before `75`. The form looks more like `q`/`g` than the writer's `4`, and two signs may stand there. PSANÍ is restored from context (a neuter noun is required by *je již rozepsáno*), not read.
2. **R16 NEOSISLNE**: the 4th sign is the open `c` (S) as in TISIC; the 3rd is 3-like (O) but may be the hooked `s` (C). Either way the intended word is *nesčíslněkráte*, as on sister card hcp-1532 (`m5cs4c8m5` NESCISLNEKRATE). Literal kept with 3/O.
3. **R10 ZAHRNIT**: the prefinal sign matches `4` (I), not `2` (U); literal kept, editorial *zahrnut*. Confirmed by the reviewer.
4. **Shadow-affected signs**: R13 ODESLU 3rd sign (looks 6-like, read E from context), parts of R07 ULEHNOUTI and the R12 opening.
5. Word boundaries, punctuation and accents are editorial. The sender's civil identity (Pepouš, a pet form of Josef) is not established.

## History: root verification of partial record (2026-10-28, superseded)

Root inspected both originals, the complete upper/right and lower/right blocks, both unresolved source positions and the side-by-side original-pixel controls on 2026-10-28. R05's peaked second shape remains 1/Y versus s/C; R12's final PSAN□ unit is obscured and remains unknown. The literal ZAHRNIT and NEOCISLNE KRATE remain, and final LIBA is a verb, not a newly identified sender. The read-only command passed three original hashes, three record hashes, 383 indexed positions (381 assigned, two unresolved), three CH expansions and tokenwise checks. This is a second solver check of the partial manual transcription, not independent provider review. No marker created.

## History: completion and handover — Claude Opus 5.5 as solver, 2026-10-29 (superseded by Response to review 1)

Status: **complete reading, handed to review (DONE1).** Decision on the two
open units:

1. **R05 pos. 2 (`f□5h57cg6`).** In work/side-by-side-controls.png (top row)
   the sign has the same peaked shape as the `1` in BYLA `p186` on the same row
   and in DRAHY `th6r1`. It differs from the round `c` of NEOCISLNE. So the
   literal is **VYEREJSKA**, the writer's slip for *do včerejška* (“until
   yesterday”), since *vyerejška* is not Czech. Literal: Y. Editorial
   reading: *včerejška*. The slip is the writer's and is disclosed.
2. **R12 pos. 5 (`bc6m□`).** The last unit lies under the photo's shadow. A
   short descending stroke after `m` is still visible, consistent with the
   writer's `4` (I) as in ZAHRNIT `m4d`. The phrase “psan□ je již
   rozepsáno, odešlu je co nejdříve” needs a neuter noun, and only
   **PSANÍ** (“letter”) fits. Reading: I. The stroke is too faint to prove
   the sign on its own, so this one sign is partly a restoration from
   context.

(The editorial Czech and Slovak given here at handover are superseded by the sections above. Decision 1 was wrong and decision 2 was overstated; see Response to review 1.)

## Response to review 1

Review 1 (separate Claude Opus 5.5 agent, 2026-10-29), verdict REVISE. Addressed by Claude Opus 5.5 as solver, 2026-10-29.

1. **[major] R05 pos. 2 is `s` (C), not `1` (Y). Accepted and fixed.** I re-examined `review/work/panel-R05.png`. The disputed sign is a peaked Λ with a left leg and no foot stroke. It is the same as the writer's `s` in VELICE (R08) and PRACI (R10). The `1` of BYLA and DRAHY is an upright stem with a flag and a flat foot. My earlier comparison was against the R16 sign, which is actually `c` (finding 4). `work/build-record.py` now has `fs5h57cg6`, and the reading is VCEREJSKA (*do včerejška*), read directly. The "writer's slip" claim is withdrawn.
2. **[major] Inconsistent deliverables. Fixed.** I regenerated `work/transcription.json`, `work/positions.csv` and `work/record-sha256.json` with `work/build-record.py`. `□` no longer occurs. `work/decode.py` now accepts `[ ]` as a restoration marker and prints the final literal text with `PSAN[I]`. It asserts 383 positions, 0 unresolved, 1 restoration, 3 CH and 386 base letters. The stale PARTIAL header, the old partial literal, editorial and Slovak blocks and the duplicated completion text were replaced with one current version. Re-run with `python3 -I ciphers/hcp-1531/work/decode.py` (exit 0, all hash, round-trip and inventory checks pass); its output equals the literal block above.
3. **[minor] R12 PSAN□ is a restoration. Accepted.** `review/work/R12-open-localnorm.png` shows a bowl with a long descender into R13 and a faint further oval, more `q`/`g`-like than `4`. My handover phrase "short descending stroke … consistent with 4" is withdrawn. The unit is now encoded as `[4]` and labelled a contextual restoration in `transcription.json` (`restorations`), the decoder output and the uncertainty list, with the possible second sign noted.
4. **[minor] R16 sign labels. Accepted.** In `review/work/panel-R16.png` the 4th sign is the open `c` with a closed top, as in TISIC. The 3rd looks like `3`. The transcription is now `m53c4c8m5` = NEOSISLNE, with the 3rd sign noted as possibly the hooked `s`. Sister card hcp-1532 (`m5cs4c8m5`, NESCISLNEKRATE) is cited. The invented editorial "neočíslně" is replaced by *nesčíslněkráte*.
5. **[minor] R13 ODESLU 3rd sign. Accepted.** It is listed among the shadow-affected signs and read as E from context (uncertainty item 4, and `marks` in `transcription.json`).
6. **ZAHRNIT. No change needed.** The reviewer confirmed it.

The meaning of the letter is unchanged. The corrections fix two sign labels (R05, R16) and relabel one unit as a restoration. Only the literal form of R05 changes (VYEREJSKA → VCEREJSKA); the editorial reading *včerejška* stays the same.
