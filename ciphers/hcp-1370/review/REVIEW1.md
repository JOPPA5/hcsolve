REVISE

# Review 1 of hcp-1370 / pc_hcp_51 (reviewer: Claude Opus 5.5, 2026-10-30)

The reading stands: Caesar −1, English, 16 enciphered words, 58 letters, all checked on the pixels. No letter of the deciphered sentence changes. One literal sign is misread, though: the closing group is `M & L`, not `N & L`. That needs fixing and is not disclosed. The other findings are minor corrections to the evidence. The two weakest words, `ibwjoh` and `Tqjo`, are better supported on the pixels than SOLUTION.md says.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1370/work/decode.py` ran. Source hashes OK, and I recomputed all four with `shasum -a 256`; they match SOURCES.md. The output equals the plaintext table line by line (58 letters).
- **Independent decode.** `review/work/own_decode.py` uses my own word list, typed from the scan, and its own arithmetic. Output: MY OWN BOY JUST COME BACK FROM HAVING A LITTLE SPIN MY FROM YOUR OWN GIRL (16 words, 58 letters). It agrees with the solver. It also confirms 30 Sep 1907 = Monday and 30 Jul 1907 = Tuesday.
- **Key coverage.** One shift, no exceptions. The key table in SOLUTION.md is correct. Only the literal heading, the date and the abbreviation groups lie outside it, and these are bracketed and disclosed.
- **Transcription.** I rotated `work/hires/pc_hcp_51_adr.JPG` 90° CCW (`review/work/crop.py`, `c.py`) and read every line at 3–5x, with disputed signs at 6–8x (`review/work/l*.png`, `z_*.png`). There are no restorations or completion sections on this card; every sign has ink.
  - Clear: `G. H. Monday.`, `Nz`, `Pxo`, `Cpz`, `kvtu`, `dpnf`, `Cbdl` (partly dry pen, all four signs present), `gspn` (twice), `b` (the "6"-shaped tall b), `zpvs`, the second `Pxo` (very pale, but all strokes are there), `Hjsm`, `Sep 30th 07.`
  - `ibwjoh`: see finding 2. The match of `ibw` with `ibwf` on hcp-1405 `work/line3.jpg` is real, and it is the same stroke sequence, ending in the same dark blob and hairline.
  - `Mjuumf`: long hooked j, then six clear feet (`z_min.png`) and the join into f, so 7 feet are compatible with `uum`. The f has its loop on the right of the stem.
  - `Tqjo`: see finding 3.
- **Date and context.** The dateline reads Sep, not Jly (`l8.png`). The Monday heading fits only 30 Sep. Printed "Cliff Gardens, Boscombe", Max Ettlinger Royal Series, Bournemouth Series 1089, Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon and the postmark [W]IMBORNE with day 30 are all confirmed. I agree that the month in the postmark is not legible (`z_postmark.png`). The picture side has no handwriting (`pic_half.png`).
- **Language.** Natural Edwardian English in the couple's formula.
- **Sources.** Portal status Not solved and no attachment, per SOURCES.md and metadata. No use of a published solution is visible. I did not repeat the web check.

## Findings

1. **major — the closing group is `M & L`, not `N & L` (transcription.json line 6, the table, the translations, uncertainty 6).** On this card the sign has three feet: long, medium and a short third (`review/work/z_ml.png`). Both `Nz` on the same card have two feet (`z_nz.png`, `z_nz2.png`). It is the same contrast that gave `M-L.` on hcp-1383, where the review confirmed it. SOLUTION.md gives N with no comment, although hcp-1383 records this very N/M doubt. Fix: transcribe `M & L.`, change the English and Slovak, and say in the uncertainty that the shifted value would be L & K, the form hcp-1383 reports for hcp-1395. Do not expand it. If the third foot is judged a flourish, say so with evidence, but this needs an explicit decision.
2. **minor — the evidence for `ibwjoh` is understated and one statement is doubtful (uncertainty 1).**
   - The pale descender ends in a hook rising on the left, with a darker head (`z_jhook.png`). That is the j of `Mjuumf` and `Hjsm`. It also excludes f, whose loop closes on the right of the stem (`dpnf`, `Mjuumf`, and `ibwf` on hcp-1405). So "HAVE + something" is ruled out on the pixels. Please cite this. The head of the hook sits directly above the T of `Tqjo` and belongs to line 4.
   - "No dot is visible above the first letter" is probably wrong. A blurred grey mark, darker than the watermark, lies at about (610, 1204) in the rotated scan, on the extension of the i stem (`z_dpnf.png`, lower centre). It may be the faint dot of i, as on hcp-1405. I cannot prove it, so state it as possible.
   - The `o` + `h` structure I see: a narrow pale loop, a hairline from its top running right, then a stem turning back down, then a small arch ending in the ink dot. This agrees with the solver.
3. **minor — uncertainty 2 overstates the q/g doubt and misses a parallel.** The tail of the second sign reaches its foot, turns **right** and rises as a dark stroke into the j (`z_q.png`). The g of `gspn` hooks left and does not do this (`l4a.png`, `l6a.png`), so the sign is q. For the first sign, the disclosed doubt remains, but the same hand has a c-curved t with a top stroke: the last sign of `mfuufst` on hcp-1383, per that card's review. Cite it.
4. **minor — "independently attested" is too strong (Why it is correct).** `b. mjuumf tqjo` on hcp-1375 is not independent support. That SOLUTION.md calls `tqjo` its one real reading point and chooses it by sense, and that card's review used the `Tqjo` of this card as a comparison. So the two cards lean on each other. Neither hcp-1375 nor hcp-1383 is FINAL (both DONE1 and REVIEWED1, verdict ACCEPT). Say the phrases recur on reviewed cards, and rest the case on this card's pixels and the fixed shift.
5. **minor — small transcription details.** The join in `E. L.` is a dash in line 2 and a long hairline in line 7, not a dot (`l2.png`, `l7.png`); hcp-1383 writes `E-L`. The "dot" after the second `Nz` is doubtful: only scattered specks stand there (`z_nz2.png`). The dot of `Mjuumf` is not offset: it lies on the extension of the slanted j stroke (`l5a.png`), which is good for j. None of this affects the plaintext.

## What I could not verify

- The meaning of `E. L.`, `M & L` and `G. H.`, and whether the abbreviation groups are enciphered.
- The postmark month and year.
- The exact count of minims in `uum`, letter by letter.
- The first sign of `Tqjo` as a T by shape alone: it remains a sense-supported reading.
- That the grey mark in finding 2 is ink of the dot.
- The web status of this number beyond the orchestrator's check.

## What the solver should do

Fix finding 1 in the transcription, translations and uncertainties, address 2–5 in `## Response to review 1`, then proceed to the PDF and FINAL. The fix touches only a literal group, so no second round is needed unless the plaintext changes otherwise.
