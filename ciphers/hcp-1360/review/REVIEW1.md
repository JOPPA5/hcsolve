REVISE

# Review 1 of hcp-1360 (reviewer: Claude Opus 5.5, 2026-10-30)

The key is right and four of the five lines stand. Line 1 is misread: the word is `Mpwjoh` = LOVING, not `Mpwf` + `h.`. The sign the solver keeps as a literal abbreviation is the end of that word. The card reads MY OWN LOVING BOY, the stock salutation of the series.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1360/work/decode.py` ran. Hashes OK, 54 letters decoded, 3 literal, and the output equals the claimed table. It rewrites `work/plaintext.txt`, which it did with the same text.
- **Hashes.** `shasum -a 256` of `source/` and `work/hires/` equals `SOURCES.md`.
- **Independent decode.** `review/work/mydecode.py` uses my own transcription and table and imports nothing from the solver. It gives MY OWN LOVING BOY / I FEEL VERY / DISAPPOINTED TO / DAY NO LETTER / YOUR ... GIRL. `review/work/check_fix.py` gives the same, 56 enciphered letters.
- **Pixels.** I rotated `work/hires/pc_hcp_41_adr.JPG` 90 degrees CCW (`crop.py`, `crops.py`). Every line was enlarged 2-3x in natural colour and with the blue channel divided by a local background (`l1a` ... `l5b`). The hard spots were enlarged 6-10x (`z_mpwf`, `z_sign`, `z_nh2`, `z_O`, `z_ej`, `z_op`).
- **Comparison.** `cmp_mpwjoh.png` sets this word beside accepted `Mpwjoh` on hcp-1361 and hcp-1367 and beside the disputed word on hcp-1363.
- **Signs confirmed.** `Nz`, `Pxo` (P, crossed x, clear o), `Cpz`, `J`, `Gffm`, `wfsz`, `Ejtbqqpjoufe` (12 signs, including E with hooked j and the pale second j), `up`, `Ebz`, `p` of `Op`, `Mfuufs`, `Zpvs`, `Hjsm`. The closing quotation ticks are clear. No letter other than those in findings 1-3 is in doubt.
- **Context.** Picture legend ST. PAUL'S CATHEDRAL, LONDON. Address Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon. Plain heading "G. H. Wednesday", plain date "July 3rd 07". 3 July 1907 was a Wednesday (computed). WIMBORNE postmarks, 10 PM; I also cannot read a date in them. The portal gives 1907-07-03.
- **Sources.** The solver discloses that no published solution was used and credit is truthful. I did no web search either.

## Findings

1. **major: `Mpwf` + `h.` is a misreading of `Mpwjoh` (LOVING).**
   - Evidence: `review/work/cmp_mpwjoh.png`, `z_mpwf.png`, `z_sign.png`, and the solver's own `work/crops/f_w3tail.png`.
   - After `Mpw` the ink runs in this order: (a) a long stroke to the upper right, falling down-left to a foot under the line; (b) a thin closed lens-shaped loop on the baseline; (c) from that loop, a stroke rising to the upper right, a sharp turn, and a fall to a dark blob on the baseline.
   - The accepted `Mpwjoh` on hcp-1361 (`work/crops/l2b.png`) and hcp-1367 (`work/crops/l1b.png`) has exactly this outline. There (a) is j, (b) is o, and (c) is h, with its short hump as the blob at the foot. Only the ink is paler here: the pen was failing, and part of the sign lies on a watermark band.
   - The solver's stated rejection, "no o loop and no final h" (`SOLUTION.md` uncertainty 2, `NOTES.md`), is wrong on the pixels. Uncertainty 1 itself calls the stroke "looped" and describes the turn and the fall to a blob, which are the o and the h.
   - The stroke the solver calls the long stem of f is the j. No separate `h.` exists and no literal group stands in this slot. `Nz Pxo Mpwjoh Cpz` is word for word the line 1 of hcp-1361 and hcp-1367, which also removes the oddity the solver noted ("a little odd").
   - The match rests on this card's outline, not on the formula alone. The sister text only tells me which comparison to make.
   - Fix: line 1 = `Nz. Pxo. Mpwjoh Cpz` = MY OWN LOVING BOY. Update `work/transcription.json`, the table, the reading, both translations (Slovak e.g. „Môj vlastný milujúci chlapec"), and drop uncertainties 1 and 2 or rewrite them as the pale-ink disclosure for j, o and h.

2. **major: headline and coverage claims follow from finding 1.** "Two abbreviation groups (3 letters)", "54 enciphered letters" and "3 abbreviation letters" should be one group (2 letters) and 56 enciphered letters. `NOTES.md` and uncertainties 1 and 2 need the rejection corrected. Keep the earlier attempt on record as a dead end rather than erasing it.

3. **minor: the O of `Op` is undisclosed.** `z_O.png`: the sign is pale and crosses a watermark band. It is a stem rising to a tip, a thin arch to the right, and a short return stroke, with no closed loop like the O on hcp-1366 (`work/crops/op.png`). `Op` = NO is the sense-required reading, fixed by "disappointed" and the following LETTER, and I have no better one. But the capital rests on context, and `SOLUTION.md` is silent on it. Add an uncertainty entry.

4. **minor: `N. h.` is better transcribed `M. h.` (N possible).** `l5a.png`, `z_nh2.png`: the first sign is an arched stem with two further short strokes, which the solver's uncertainty 3 itself says is one more than the N of `Nz`. That is the M build (cf. `M-h` on hcp-1369, and the same point on hcp-1363 review finding 2). Literal group, so no word changes. A round spot on the band sits on the baseline after it. It may be the dot or foxing. I see no certain dot after the h.

5. **minor: opening quotation ticks.** Part of the marks over `Op` is the foot of a j from line 3 (`z_op.png`, `z_O.png`). Two ticks remain plausible, and the solver already flags them as uncertain. Keep the entry and note the j foot.

## Note for the orchestrator (outside this directory; not changed)

The same ending appears in line 1 of hcp-1363 (`Mpwfs`) and hcp-1366 (`Mpwf.`). In `cmp_mpwjoh.png` the hcp-1363 word has the same j, o, h outline, sharp in dark ink. It looks like `Mpwjoh` too, which would also resolve the open "one shared sign" question raised in those reviews. I checked the hcp-1366 crop `work/crops/w1.png` only by eye, so a reviewer of those cards should confirm.

## What I could not verify

- The expansion of the literal group `M./N. h.`, and whether it is enciphered.
- The postmark date.
- The farm name beyond the visible "Stokelake Farm".
- Whether any publication outside the portal exists; no web search was done. The orchestrator's register check is taken as stated.
