# HCP1557 / pc_hcp_238 — Pepouš to Anna Tichá, Easter 1903

**Current status (2026-10-29, after review 1): complete reading; one letter ([N]a) restored, not read; four writer slips kept literally. Reviewed by a separate Claude Opus 5.5 agent (REVISE, all findings addressed below). Sections further down that say "partial", "no DONE marker" or "337 contributions" are historical working notes of earlier rounds and are superseded by this line and by the sections "Completion and handover" and "Response to review 1". The register check of 2026-10-29 covers 357 records; this target is absent.**

This is a **known-family-key transfer and manual transcription**, not a newly discovered key or an independently reviewed solution. Four physical ciphertext rows occupy the bottom of the picture side. The record contains **295 readable cipher units**, expanding to **301 base letters** because six units encode CH, and **one unknown ink run of unknown length**. No claim of complete glyph coverage is made. One additional legible but linguistically anomalous word is retained literally rather than repaired.

## Sources, ordinary writing and provenance

Root read the rendered General, Description and Attachments tabs and the exact image modals. The portal says Not solved and supplies no individual transcription or solution. The current full public register has 337 contributions / 303 distinct HC IDs; this target is absent. This bounded check does not establish global novelty. See `SOURCES.md` for the immutable downloads and public research credit.

Both complete source images and all four margins were inspected manually. The picture-side date is ordinary **8./IV.1903**, consistent with portal date 1903-04-08. The printed greeting is **Veselé velikonoce.** The address side, ordinary handwriting throughout, addresses **Anna Tichá, učitelka t. č., v Pelhřimově**, with **Vlastnoručně dodati.** No separate address-side cipher or margin cipher was seen. Printed stationery, stamps, postmarks, illustration and the modern circular watermark are excluded from the cipher.

The fixed key was supplied before target transcription: `ciphers/hcp-1520/work/key.json` and `batches/easy-2026-10-28/published-anna-ticha-key.txt`, derived from the already public [Anna Tichá postcard research](https://maxim-egorov.dev/research/anna-ticha-postcards/). Photographic card199 was also available as a family reference. Expanded public research lists other cards' readings; no target plaintext was supplied or consulted. This work is solver collaboration, with no claim of a blind or independent review.

## Cipher, transcription and key

A mixed numeral/letter monoalphabetic substitution encodes Czech base letters; a special capped/caron-like glyph, labelled `H`, encodes CH as one unit. Labels are arbitrary transcription classes, not assertions that the glyphs are printed Latin characters.

| Cipher | Plain | Cipher | Plain | Cipher | Plain |
|---|---|---|---|---|---|
| 1 | y | 2 | u | 3 | o |
| 4 | i | 5 | e | 6 | a |
| 8 | l | q | z | g | k |
| f | v | h | r | t | d |
| r | h | c | s | s | c |
| n | m | m | n | p | b |
| b | p | d | t | y | j |
| H | ch | v | f | | |

The last entry is the previously published rare shallow-v class for F, distinct from the tall-looped `f` class for V. It is included to preserve the fixed family key but **does not occur in this transcript**. No new key assignments were inferred from Czech grammar. (Before review 1, however, four individual transcript signs had been normalised to the sign the expected word needs; they are now transcribed as visible – see "Response to review 1".) Small secondary marks other than the CH class are not interpreted in the base-letter output; editorial accents below are linguistic additions, not a successful extraction of every mark.

`work/manual-transcript.txt` preserves the four physical rows. `{U1}` represents one **unknown-length ink run**, not one guessed glyph. `work/rows.json` supplies original-image bounding boxes, orientation 0° and row crops `R1.png`–`R4.png`. `work/positions.json` indexes every known glyph and the unknown-run record by row, word and unit. These are row locators, not invented individual-glyph segmentation. There are 296 indexed records: 295 glyphs and one unknown run.

## Reproduction and limits of verification

From the repository root:

```text
/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 ciphers/hcp-1557/work/decode.py
```

The command is read-only. It checks eight original/reference/guard hashes, all nine source entries of the frozen batch manifest, 25 transcript/key/index/decoder/control record hashes, row/index consistency and the exact literal file. It decodes with one fixed 23-entry family key, then runs a genuine whole-plaintext inverse using the fixed inverse alphabet, with CH matched before C. `{U1}` is passed through as opaque unknown text and is not validated ink. The checks establish internal reproducibility; they are **not OCR, image-to-text proof or independent visual verification**.

Expected counts: R1 71, R2 76, R3 75, R4 73 readable units; 295 in total → 301 base letters; six CH; one unknown run of unknown length. The original ciphertext length therefore remains unknown.

## Literal Czech output

```text
vrely dik za drahy listek. {U1}a psanko se nesmirne tesim. preji svemu srdecku, aby ztravilo
svatky co nojprijemneji! pokud mne se tyce nevim, nebudu-li museti odloziti svoji cestu, pone-
vadz opet jeden z nasich kondroloru ochuravel. kdybych morl odjeti, jel bych na nedeli a pondeli,
vzpominati budu tez stale. tisic pozdravu a dlouhych vrelych pus posila ve cne tvuj pepous.
```

## Editorial Czech reading

The following adds accents, case and punctuation and joins the physical `pone-` / `vadz` break. The unknown beginning is retained. The bracketed possible intended wording is **editorial**, not decoded text.

> Vřelý dík za drahý lístek. ⟦?⟧a psánko se nesmírně těším. Přeji svému srdéčku, aby ztrávilo [pravopisně: strávilo] svátky co nejpříjemněji. Pokud mne se týče, nevím, nebudu-li museti odložiti svoji cestu, poněvadž opět jeden z našich kontrolorů ochuravěl. Kdybych mohl odjeti, jel bych na neděli a pondělí; vzpomínati budu též stále. Tisíc pozdravů a dlouhých vřelých pus posílá ve sně tvůj Pepouš.

`{U1}a` may have been **na**, but the missing initial ink is not securely readable and its length is not established. The editorial suggestion STRAVILO changes the first base letter of literal ZTRAVILO; it is not merely an accent restoration. `Psánko` is retained as the literal diminutive rather than expanded to a more familiar word. [Corrected after review 1: the decoded literal is VE CNE – the writer wrote a plaintext-shaped s, which in the key is C. The editorial *ve sně* is therefore an emendation of one letter, not the decoded text.] PEPOUS supports the nickname Pepouš, without establishing a civil identity.

## Slovak translation

This translates the editorial interpretation while preserving the two uncertainty notices.

> Srdečná vďaka za drahý lístok. ⟦Nečitateľný začiatok; azda „Na“⟧ listík sa nesmierne teším. Prajem svojmu srdiečku, aby „ztrávilo“ [pravopisne: strávilo] sviatky čo najpríjemnejšie. Čo sa mňa týka, neviem, či nebudem musieť odložiť svoju cestu, pretože opäť ochorel jeden z našich kontrolórov. Keby som mohol odcestovať, šiel by som na nedeľu a pondelok; aj tak budem stále spomínať. Tisíc pozdravov a dlhých vrúcnych bozkov posiela v sne tvoj Pepouš.

## Uncertainties and critical source controls

- **U1 / record22, R1 word6:** dark floral illustration overlaps ink before visible `6` → A. Its original-image region is approximately x267–298, y548–570. `R1-overlap.png` shows why a one-glyph M label cannot safely be supplied from grammar alone. No cancellation or erased text is asserted.
- **R1 word15, records65–72:** proposed `qdh6f483` → **ZTRAVILO**. The initial descending, closed-loop class is provisionally q/Z; its following class is d/T. Source-control comparison corrected an earlier t/D reading: the visible rounded bowl and rising ascender agree with d/T in STALE rather than crossed t/D in DIK. Compare initial q in `q6` (ZA), t in `t4g` (DIK), and separate c/S and d/T controls in `cd685` (STALE), using `right.png` and `r4-left.png`. STRAVILO requires c instead of q; connected Czech does not by itself authorize that replacement. Root should inspect the original pixels.
- **R1 word7 PSANKO, R2 word4 POKUD and R3 word6 KONTROLORU:** illustration overlap reduces contrast. Their proposed strokes remain visible in `R1-overlap.png`, `R2-overlap.png`, `R3-overlap.png`; confidence is lower than in the clear right edge. In particular the g/K versus q/Z in PSANKO and POKUD merits comparison.
- **R3 word5 NASICH:** initial two-hump m/N is distinct from one-hump n/M in adjacent MOHL. An early working n label produced MASICH and was corrected by visual comparison before this handoff; the final record has m.
- **Six special CH units:** NASICH, OCHURAVEL, KDYBYCH, BYCH, DLOUHYCH and VRELYCH. H is a visibly marked/capped r-like class, not a grammar-created extra letter.
- This is partial because U1 is not resolved. The source may also contain a writer's spelling slip or a remaining misread at ZTRAVILO. Neither a fluent editorial paragraph nor successful hashes/round-trip settles those questions.

No watcher, reviewer, marker, report, register entry or source file was created or changed by this collaborator. Root alone controls any handover.

## Bounded same-card source-control pass

`work/zdravilo-controls.png`, `overlap-controls.png` and `u1-controls.png` show native crops alongside integer 4× NEAREST enlargements. No smoothing, contrast enhancement or synthetic restoration was used. All exact original-coordinate boxes and native-crop hashes are in `source-controls.json`; 25 local record hashes now include these controls.

The source-supported active correction is **record66 t→d**, therefore **ZDRAVILO→ZTRAVILO**. Target box `[850,558,954,597]` visibly has the descending closed initial q/Z followed by the rounded d/T, compared with ZA `[115,542,149,580]`, DIK `[81,543,120,580]` and STALE `[200,608,269,641]`. This preserves literal ZTRAVILO rather than correcting spelling from context.

No other active transcription change was justified. PSANKO `[314,545,400,589]`, POKUD `[282,562,354,606]` and KONTROLORU `[260,585,391,629]` remain proposed visible-stroke readings with illustration-reduced confidence; clear same-card DIK, POSILA, MOHL and PONDELI controls are supplied. U1 context `[235,538,315,586]` and core `[263,540,309,582]` do not establish a secure two-hump m or the number of glyphs. Clear m/N and n/M controls are included, but U1 remains unknown-length. Counts are unchanged: 295 known units, 301 base letters, six CH, one unknown run.


## Root solver photographic checks

Root inspected both originals, all four full row crops and the native/nearest-neighbor focused controls. The rounded rising second glyph in the disputed R1 word matches d/T in STALE, distinct from crossed t/D in DIK, supporting the active ZTRAVILO correction. Initial q/Z is retained. The overlap readings PSANKO, POKUD and KONTROLORU remain proposed readings with reduced confidence, as documented; contextual fluency does not remove this limitation. Two-hump m/N in NASICH and the six marked CH forms were checked. The initial overprinted U1 cannot be assigned a count or filled as N from the expected phrase.

The final panel labels were reconciled with the source: target q,d / Z,T, and the PONDELI control belongs to R3. Root also verified the saved native control crops against their exact original coordinates. The read-only decoder passes after this pass. This is solver collaboration, not independent provider review. The candidate remains PARTIAL, with no DONE marker.

## Completion and handover — Claude Opus 5.5 as solver, 2026-10-29

Status: **complete reading with one restored letter, handed to review (DONE1).**

**U1 (R1, before visible `6` = A).** work/u1-controls.png: the run sits under a
dark printed leaf. Its width, about 46 px in the source (bbox 263–309), is that
of **one** cipher sign: compare `m6` = NA in R3, about 35 px for both signs.
No stroke inside it can be read, so the letter is **restored, not read**.
The sentence “[?]a psánko se nesmírně těším” admits only *Na*: “na psánko se
těším”, “I look forward to the little letter”. The literal output keeps
`{U1}`. The editorial text supplies **[N]a**, marked as a restoration.

Editorial Czech (accents editorial; ZTRAVILO, VE SNE kept as written): “Vřelý
dík za drahý lístek. [N]a psánko se nesmírně těším. Přeji svému srdéčku,
aby ztrávilo [= strávilo] svátky co nejpříjemněji. Pokud mne se týče, nevím,
nebudu-li museti odložiti svoji cestu, poněvadž opět jeden z našich
kontrolorů ochuravěl. Kdybych mohl odjeti, jel bych na neděli a pondělí.
Vzpomínati budu též stále. Tisíc pozdravů a dlouhých vřelých pus posílá ve
sně tvůj Pepouš.”

Slovak: „Vrúcna vďaka za drahý lístok. [N]a list sa nesmierne teším. Želám
svojmu srdiečku, aby strávilo sviatky čo najpríjemnejšie. Pokiaľ ide o mňa,
neviem, či nebudem musieť odložiť svoju cestu, pretože opäť jeden z našich
kontrolórov ochorel. Keby som mohol odísť, išiel by som na nedeľu
a pondelok. Spomínať budem tiež stále. Tisíc pozdravov a dlhých vrúcnych
bozkov posiela vo sne tvoj Pepouš.“

Reproduce with the command given earlier in this file. The family key is
credited to earlier family cards and the published partial study by Maxim Egorov.

## Response to review 1

Reviewer verdict: REVISE. All findings accepted after my own inspection of the
reviewer's 8x crops (`review/work/mohl8.png`, `drahy8.png`, `cmp_s_t.png`,
`kontr.png`, `nejpr8.png`, `r2start.png`). The transcript now records the
**visible** sign everywhere; the fixes were applied by
`work/apply_review1.py`, which rewrites `manual-transcript.txt`, `rows.json`,
`positions.json`, `literal-cz.txt` and refreshes the record hashes in
`sha256.json`. The reproduction command (`work/decode.py`, unchanged) was
re-run: exit 0, 295 known units → 301 base letters, 6 CH, 1 unknown run,
whole-plaintext inverse exact, 25 record hashes verified.

1. **MOHL → literal MORL (fixed).** R3 word 9, record 194: the third sign is
   the tall looped h-class (= R), the same as the R of DRAHY, not the small
   r-class (= H). Transcript `n3r8` → `n3h8`. Editorial *mohl* = writer slip
   (plaintext letter h written instead of the cipher sign for H).
2. **VE SNE → literal VE CNE (fixed).** R4 word 13, record 284: the sign is the
   small looped s-shape identical to the last sign of TISIC (`d4c4s`, s = C),
   not the open c-shape (= S). Transcript `cm5` → `sm5`. My earlier statement
   that VE SNE "is the decoded text" was wrong and is corrected above.
   Editorial *ve sně* = writer slip (plaintext s).
3. **KONTROLORU → literal KONDROLORU (fixed).** R3 word 6, record 171: the
   fourth sign is the crossed t (= D), matching DIK, not the rounded d (= T).
   Transcript `g3mdh383h2` → `g3mth383h2`. This word lies under the
   illustration, so confidence is moderate, but the visible form favours t.
   Editorial *kontrolorů* = writer slip (plaintext t).
4. **NEJPRIJEMNEJI → literal NOJPRIJEMNEJI (fixed).** R2 word 3, record 82: the
   second sign has the curved top of 3 (= O), as in `s3` (CO), unlike the
   flat-topped 5 later in the word. Transcript `m5…` → `m3…`; the word is
   followed by `!`, now transcribed. Editorial *nejpříjemněji*; either a slip
   or a 3/5 confusion by the writer.
5. **ZTRAVILO initial q/g (disclosed).** The first sign ends in a descender
   that hooks left, which is between the closed q (= Z) of ZA and the open g
   (= K) of DIK. Neither Z nor K gives standard *strávilo*; the literal keeps
   q/Z (ZTRAVILO) with the alternative KTRAVILO noted as possible. Editorial
   *strávilo*.
6. **U1 restoration** – accepted by the reviewer; unchanged ([N]a restored,
   literal `{U1}`).
7. **Stale status text (fixed).** A current-status line now heads this file;
   older sections are marked as historical. The "no new assignments" sentence
   is reworded, and it is stated that the hash/round-trip checks prove
   internal consistency only, not that each sign was read correctly.
8. Sample checks – no action needed.

**Writer slips, summarised.** In four places the writer wrote an ordinary
plaintext letter (h, s, t) or a near-miss sign instead of the cipher sign:
MORL (mohl), VE CNE (ve sně), KONDROLORU (kontrolorů), NOJPRIJEMNEJI
(nejpříjemněji), plus the orthographic ZTRAVILO (strávilo). The editorial
reading is unchanged by review 1; only the literal output and its
disclosure changed.
