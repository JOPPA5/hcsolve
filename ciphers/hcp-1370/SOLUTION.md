# HCP 1370 / pc_hcp_51 — Caesar −1 English love postcard, Monday 30 September 1907

Status: **whole message read: 58 of 58 enciphered letters; review 1 verdict REVISE, findings addressed, no decoded letter changed.** Two abbreviation groups are kept literal. The remaining doubts are listed under Uncertainties. All work on this number by Claude Opus 5.5 as solver, 2026-10-30. No earlier work exists; no published solution was found or used (portal status Not solved, no attached transcription or solution; AI register has no record, per the orchestrator's check).

## Origin

Picture side: printed view "Cliff Gardens, Boscombe", no handwriting. Address side: Max Ettlinger "Royal Series", Bournemouth Series 1089 (same series as sister card hcp-1383); plain address **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon** (portal spelling "W. Abboú"); halfpenny Edward VII stamp; postmark WIMBORNE, day 30, the month is not legible. The message runs up the left half of the address side (turn the card 90° counter-clockwise, `work/crops/reading.png`). The grey wheel is the portal's watermark, not part of the card.

## Cipher and key

Monoalphabetic Caesar shift, the key of the W. Abbott family (hcp-1375, 1383, 1386…1407): each plaintext letter is written as the **next** letter. Decrypt by subtracting one (A→Z). The key was taken from those cards as a hypothesis and holds for every enciphered word here.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

`G. H. Monday.` and `Sep 30th 07.` are ordinary writing. `E-L.` (twice) and `M & L.` are abbreviations kept literal, as on the sister cards; the `&` is unshifted.

## Transcription and plaintext (all ciphertext on the card)

| Ciphertext | Plaintext |
|---|---|
| G. H. Monday. | (plain) |
| Nz. Pxo. E-L. Cpz. | MY. OWN. [E-L.] BOY. |
| kvtu dpnf Cbdl. | JUST COME BACK. |
| gspn. ibwjoh. b. | FROM. HAVING. A. |
| Mjuumf. Tqjo. Nz | LITTLE. SPIN. MY |
| M & L. gspn. zpvs Pxo | [M & L.] FROM. YOUR OWN |
| E-L. Hjsm. | [E-L.] GIRL. |
| Sep 30th 07. | (plain) |

English (the plaintext language; the portal lists Unknown): *"G. H. Monday. My own E. L. boy, just come back from having a little spin. My M & L from your own E. L. girl. Sep 30th 07."*

Slovak: *„G. H. Pondelok. Môj vlastný E. L. chlapec, práve som sa vrátila z malej vyjažďky. Moje M & L od tvojho vlastného E. L. dievčaťa. 30. sept. 1907."*

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1370/work/decode.py
```

It checks the SHA-256 of both `source/` images and both originals in `work/hires/`, prints ciphertext and plaintext from `work/transcription.json`, checks the inverse shift, counts letters and prints the weekdays used for the date.

## Uncertainties

1. **`ibwjoh` = HAVING, the faint word.** The start `ibw` is dark and has the same shapes as `ibwf` on hcp-1405 (`work/line3.jpg` there; compare `work/crops/have_ing.png` here). The ending is written with a nearly dry pen and lies partly on the watermark: a long pale descending stroke with its dot above, ending in a hook that rises on the left with a darker head (`j`, as in `Mjuumf` and `Hjsm`; review/work/z_jhook.png), a thin narrow loop (`o`), a tall stem with a small arch ending in a dot of ink (`h`). The hook excludes `f`, whose loop closes on the right of the stem (`dpnf`, `Mjuumf`, `ibwf` on hcp-1405), so HAVE plus something else is ruled out on the pixels. The head of the hook stands directly above the T of `Tqjo` and belongs to the line below. These three signs are read from very pale ink, but they are not restorations: strokes exist for each. A blurred grey mark on the extension of the first stem (review/work/z_dpnf.png, lower centre) may be the faint dot of `i`, as on hcp-1405; this cannot be proved. The first attempts (Tennis, Dentist, a place name) were rejected because they do not account for the final `h` shape, nor for the match with `ibwf`.
2. **`Tqjo` = SPIN.** Bowl left of a descending stem, then the hooked `j` with its dot, then `o`. The second sign is `q`: its tail reaches the foot, turns right and rises as a dark stroke into the `j` (review/work/z_q.png), while the `g` of `gspn` hooks left and does not do this. The first sign is a curved stroke with a short top flag, not the long-barred T of `Tpssz` (hcp-1384) and close to this writer's C (`Cqjo`, "BPIN", not a word). T is chosen because it alone gives a word; the same hand has a c-curved t with a top stroke as the last sign of `mfuufst` on hcp-1383. The same words `b. mjuumf tqjo` are read on hcp-1375, 15 Oct 1907, but that card cites this one for its own `q`, so the two support each other and neither proves the other. The first sign stays a sense-supported reading by shape.
3. **`Mjuumf`.** Capital M with lead-in loop, long hooked `j` (same form as in `Hjsm`), its dot on the extension of the slanted stroke, then an unbroken run of minims for `uum`, then `f` with a long loop closing right of the stem. Seven feet are compatible with `uum`, but they cannot be assigned letter by letter; the same run appears in `mfuufs` on hcp-1386.
4. **`b.`** resembles the digit 6; it is read as the writer's tall lower-case `b`, which gives A and completes the phrase.
5. **Date.** The dateline is read as **Sep**, same form as "Sep 23rd" on hcp-1383, not Jly. The heading says Monday: 30 Sep 1907 was a Monday and 30 Jul 1907 a Tuesday (the command prints this). So the portal date 1907-07-30 is probably wrong. The postmark shows the day 30, but the month is not legible, so it does not settle this independently. `source/metadata.md` is left unchanged.
6. **`E-L.`, `M & L.`, `G. H.`** are not expanded; their meaning is not proved. The closing group has an M, not an N: three feet (long, medium, short), against two in both `Nz` on this card (review/work/z_ml.png, z_nz.png, z_nz2.png). This is the same contrast as `M-L.` on hcp-1383. Shifted, the group would give L & K, the form hcp-1383 reports for hcp-1395, so it may be enciphered; this card cannot decide that, and neither the shifted value nor D. K. for `E-L.` is adopted. The join in `E-L.` is a dash in line 2 and a long hairline in line 7.
7. Word-dots are the writer's habit and carry no meaning; only scattered specks stand after the second `Nz`, so no dot is transcribed there. The first word is transcribed `kvtu` as on hcp-1383, though its initial could be a capital.

## Why it is correct

One fixed shift, not tuned to this card, turns all 58 letters into a grammatical English sentence. The non-formula words (`kvtu dpnf Cbdl`, `ibwjoh`, `Mjuumf`, `Tqjo`) decode without adjustment and the phrases `kvtu dpnf cbdl` and `b. mjuumf tqjo` recur on the reviewed cards hcp-1383 and hcp-1375 to the same addressee. That recurrence is not independent proof, since hcp-1375 leans on this card for `tqjo`; the case rests on this card's pixels and the fixed shift. Opening and closing are the couple's usual formula. Addressee, Wimborne postmark, the Bournemouth Series card (as hcp-1383, one week earlier) and the Monday heading fit the correspondence.

## Response to review 1

Verdict REVISE. I re-read the reviewer's zooms before answering each finding.

1. **Major, `M & L`: fixed.** The enlargement shows three feet against two in both `Nz`, so the group is M. Changed in work/transcription.json, the table, both translations and uncertainty 6, which now gives L & K as the unadopted shifted value. The group is literal, so no decoded letter changes.
2. **Minor, `ibwjoh`: fixed.** Uncertainty 1 now cites the left-rising hook, says it excludes `f`, and replaces "no dot visible" with a possible faint dot, stated as unproved.
3. **Minor, `Tqjo`: fixed.** Uncertainty 2 now identifies `q` by the tail that turns right into the `j`, and cites the c-curved t of `mfuufst` on hcp-1383. The first sign stays disclosed as sense-supported.
4. **Minor, "independently attested": fixed.** Removed from Why it is correct. Since the review, hcp-1375 and hcp-1383 have both reached FINAL, but the circularity remains, so the case rests on this card.
5. **Minor, transcription details: fixed.** `E-L.` now has its join as a dash (line 7 a long hairline, noted), no dot after the second `Nz`, and the `Mjuumf` dot described correctly.

`python3 -I ciphers/hcp-1370/work/decode.py` re-run after the changes: hashes OK, 58 letters, same plaintext.

## Credits

Key family established on the sister cards by earlier solvers (OpenAI GPT and Claude Opus 5.5). All reading of this card by Claude Opus 5.5, 2026-10-30.
