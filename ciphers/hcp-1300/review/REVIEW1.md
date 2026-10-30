REVISE

# HCP1300, review round 1 (Claude Opus 5.5, reviewer, 2026-10-30)

**Bottom line.** The solution's message stands: Hungarian, Jolánka family key, Feri to Jolánka Tóth, no leave before spring. I found no wrong word in the normalized sense. The literal transcription, however, is not what the card shows in several places: it drops three written signs, misreads a two-bar sign twice, and misdescribes the row 24 crux. Concrete fixes are needed before FINAL.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1300/work/decode.py` ran; all four SHA-256 values OK; output agrees with the literal and normalized text in SOLUTION.md; 638 tokens.
- **Independent decode.** `review/work/rev_decode.py` (output `rev_decode.out`) carries my own class-by-class transcription of all 27 rows and 6 box rows, decoded by a table built from the sign classes in `ciphers/hcp-1216/SOLUTION.md`. It does not use the solver's decoder. It compares with the ledger only afterwards. Differences are in findings 1 to 5; the only others are the disclosed class/sense calls (tilted cross as f in rows 16 and B6, upright cross as z in row 27).
- **Pixels.** Every row read on 2.5x panels of the hi-res scan (`review/work/crops/A` to `N`, `BOX`), with 3.5x to 7x crops of rows 1, 12, 13, 14, 15 and the box, plus colour crops of the seal area (`c24`, `c25a`, `c25b`, tool `colcrop.py`), which separate grey-violet pencil from olive seal ink. The picture side has only the printed verse and no handwriting.
- **Key coverage.** Every sign falls into an existing family class; no new value was invented. 659 letters by my count, IC 0.070, letter ranking e a m o s t n g, which suits Hungarian. Every key class occurs on the card.
- **Normalization audit.** A diff of the literal text against `normalized.txt` listed every editorial change; see finding 7.
- **Honesty.** SOURCES.md and SOLUTION.md agree: no published solution claimed or used. Key source is credited. The solver's phrase "recognised, not read" for row 13 is candid.
- **Language and context.** Period Hungarian love-letter prose in the family register. The closing has a closer parallel than the two cited: HCP1292 *sírig hű imádója, Feri*.

## Findings

1. **major: row 1 omits two written signs.** The card has s z e r e t e t e t t e d e s, i.e. `szeretetett édes`: after `szeret` come e-t, e-t, t, e. Ledger and SOLUTION give `szeretett edes`, which is the wording of sister card HCP1216 row 1. Evidence: `crops/A.png` row 1 and `r1.png`: three-bar signs at panel px 370, 720, 1040, 1360 of `A.png` alternating with gamma t, then two t's before the next e. The normalization *Szeretett* is unaffected, but the literal row is wrong, and this is the one place that looks read from expectation. The writer's repeat must be recorded as a dittography.

2. **major: row 15 omits a sign.** After `le` there are two s-type bowls before the z: `lesszek`, not `leszek`. Evidence: `crops/r15.png`, bowl at px 1270 and a second, flat-topped bowl at px 1470, then the z at 1680 (`G.png` confirms). Normalized *leszek* stands, but the ledger's header "one token = one written sign" is false for rows 1 and 15, and the count of 638 is three short.

3. **minor: row 13 last sign is a, not e.** It has exactly two bars (`crops/e13.png`, 7x). So the card reads `sza|momomra`. SOLUTION point 4 and the "e for á" explanation of *számomra* are wrong for this word and `szemomra` should be withdrawn from the list of writer's habits at the top. The dittography (`mo` repeated) stands. Ledger token, literal row, points 4 and the sign-behaviour note need correcting.

4. **minor: row 12 `mega` is `maga` on the pixels.** The sign has two bars, crossed by the printed rule (`crops/e12.png`); no third bar is visible. Point 2 says it is undecidable and the ledger chooses E; the evidence favours a.

5. **minor: row 24 `{sz?}` is misdescribed.** The colour crop (`crops/c24.png`) shows that the "hook on top" is seal ink (olive, the s of *Tobias* in the seal's inner text; compare `N.png`) and that the "heavy bar with a curve" is the seal's R, very dark where it may overlap pencil. The only clearly pencil sign is a plain upright cross. So the reading should be recorded as one visible upright cross, possibly with a sign hidden under the R. The upright cross is the same z-use the solver accepts in row 27, so `zeh|n` for *szépen* (s dropped or hidden) is a tidier basis than "two tangled signs", and it remains inferred from sense. Row 24 *szépen* stays the weakest word; the solver was right to say so.

6. **minor: row 13 `szerelmem` tokens overstate.** Point 3 admits the word is recognised, but the ledger gives plain tokens E L M E M. In `crops/r13.png` I can see e, l, a three-stroke m, an extra heavy stroke, and a boxed three-bar e; then a thin tail before the v. I find no distinct second m, so *szerelmem* and *szerelem* cannot be separated. Mark these tokens uncertain in the ledger and give both in the point. The sense is the same apart from "my".

7. **minor: undisclosed normalizations.** Point 13 and the others do not list: `soraim` → *soraimat* (an added suffix, the only one affecting grammar), `higyje` → *higgye* (g added, j dropped), `magamert` → *magam mert* (shared m). Add them.

8. **minor: address not recorded.** The card's plain pencil address is not transcribed in SOLUTION.md. It reads *Szépreményű / Tóth Jolánka / úrleánynak / Jász Árokszállás*; the first word, above and left of the stamp and running into the cancel (`crops/hand.png`, `addr.png`), could be mistaken for an unexplained plain message and should be stated. The same form is in HCP1287. The final letters of *Szépreményű* are cut by the cancel: my reading rests on that parallel.

9. **minor: row 25 `nom`, point 5 says no ő mark is seen.** A short pencil tick stands at the upper left of the o (`crops/c25b.png`, px 1450). It may be the ő mark, which supports *nőm*, or the tick of an h-type sign. Mention it. *nőm maga vagy senki* remains a sense reading, as disclosed.

## Checked and upheld

- Rows 2 to 11, 14, 16 to 23 and 25 to 27: sign by sign agree with the ledger, apart from the items above. In rows 8 and 10 some signs are heavily overwritten (`d`, `r`, `b`) but readable. Row 14: three-stroke m, o, m, o, m as claimed; the second n stroke of `ny` is blotted.
- Row 25 under the seal, `megmondom nom`: pencil is traceable in the colour crops (m, o, n, d, o, m, n, o, m). The d and first m are the least clean.
- Row 26 `sikert kivanok`: readable through the seal.
- Box rows: read as claimed with ink suppression. B3 `dokoksi`: the k-sign with a foot loop matches row 7 k, but the signs `c`+`ɔ` are close to the cs pair of row 13; *cs* gives no word, so k + s is preferable, and the extra `ok` stays unexplained as disclosed. B5 hook-only o is as stated.
- Disclosed uncertainty points 1 and 5 to 15 are otherwise fair. No restoration is presented as a reading.

## Could not verify

- The sign or signs hidden under the seal's R in row 24.
- The second m of row 13 under the overwriting.
- The date: only day 26 on the left postmark; a figure 11 appears on the stamp cancel, month or hour not established.
- Whether Feri is the same person as on the other cards, or the place of writing; no wider literature search was made.

## Required before FINAL

Correct the ledger and literal rows 1, 12, 13, 15 and 24 (decode.py count follows), revise points 2 to 5 and the *szemomra* note, add the missing normalizations and the address. No DONE2 is needed if the changes stay within these points, since the reading and translations do not change.
