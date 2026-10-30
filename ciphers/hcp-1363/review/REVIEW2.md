ACCEPT

# Review 2 of hcp-1363 (pc_hcp_44), reviewer Claude Opus 5.5, 2026-10-30

The revised reading stands: Caesar -1, MY OWN LOVING BOY / MANY THANKS / FOR CARDS OF / WINDSOR. LOVE / & [Lt..] FROM / Y. O. [M. h.] GIRL. The change from `Mpwfs` to `Mpwjoh`, the reason for round 2, is right on this card's pixels. I tried to refute it and could not. Only minor points of record remain, and none changes a word.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1363/work/decode.py` ran, the hashes passed, and it reported 55 enciphered + 4 literal letters. The output equals the SOLUTION.md table.
- **Independent decode.** `review/work/r2/my_decode2.py` holds my own retyping from my own crops, with `Mpwjoh` retyped as the review-1 response asked, and does not read the solver's JSON. It gives the same plaintext. I count 55 enciphered letters. Over all 26 shifts only shift 1 yields target words (13 of 13 distinct-token hits, all others 0). No per-word adjustment is needed; the key covers every enciphered sign.
- **Pixels.** I rotated `work/hires/pc_hcp_44_adr.JPG` 90 degrees counter-clockwise and enlarged every line 3-7x, with a blue-minus-red ink filter and a contrast boost for the pale strokes (`review/work/r2/L*.png`, `z_*.png`). I read every word, not only a sample.
- **`Mpwjoh` (line 1; `L1b.png`, compared with `work/review1/cmp_mpwjoh_1363.png`).** Dark, unforced ink. After M, p and a compressed w there is a long stroke up to a sharp top and straight down below the line to a thick foot that hooks back up: the j of `Xjoetps` (`L4a.png`). It has no closed foot loop, unlike the f of line 4 `Mpwf` (`L4b.png`), so `Mpwf` is excluded here. Then a thin lens on the baseline (o), and a rise, sharp turn and fall to a low blob (h). The outline matches accepted line 1 on hcp-1361 and hcp-1367. My one attempted objection was that the lens plus rise is an f or s form; neither fits, since the f loop hangs below the line and this hand's s has a rounded arc. LOVING also gives an attested line 1 with no invented form. The word now agrees across hcp-1360, 1361, 1366 and 1367 (grep of their SOLUTION.md).
- **Rest of the transcription.** Confirmed on the pixels: Nz, Pxo, Cpz, Nboz, uibolt, gps, dbset, pg, Mpwf, gspn, Z., P., M., h., Hjsm. A dot above the `b` area of `uibolt` (`L2b.png`) is a displaced i-dot or stray; no letter depends on it. The narrow slit-loop in the lower stem of the p of `gps` and `pg` is a habit of this hand and does not make another letter.
- **Weak spots, judged on the pixels.**
  - `Xjoetps`, end (`z_windsor.png`): t with detached bar, then pale p with bowl and a pale reduced stroke rising right for s. Real ink, correctly called the weakest sign of the word.
  - `& L` (`z_amp_L.png`): real pale ink, and the disclosure that it is identified by shape and slot from sisters is accurate.
  - `pg` (`z_pg.png`): g is pale but complete, with a dark dot at the start of its tail and a dash-like dot after it.
  - The `-` after `uibolt` and the barless final t strokes are as disclosed.
- **Non-text marks.** The streak under `gps` and the line under `Hjsm` running to the card edge are as described.
- **Date.** 19 July 1907 was a Friday (computed), matching the plain heading and postmark.
- **Language and context.** Ordinary period English, in this couple's formula. "Many thanks for cards of Windsor" is the one fresh sentence and is sensible. No other SOLUTION.md in the repo has WINDSOR, so it is not borrowed from a sister.
- **Review 1 findings 2-5.** All addressed in SOLUTION.md as stated. The sister parallels and the source of the `Mpwjoh` idea are disclosed.
- **Other.** Target is outside `skip.txt` and not in `register-exclusions.json`.

## Findings

1. **minor: uncertainties 1 and 2 are out of date.** Uncertainty 2 says hcp-1366 is read `Mpwf.` and hcp-1360 `Mpwf h.`. Both SOLUTION.md files now read `Mpwjoh`, and hcp-1360 is FINAL (hcp-1366 is at DONE2, not yet accepted). Uncertainty 1 says the word has not been re-checked by a reviewer; it now has. Update both when closing. "Why it is correct" could also cite hcp-1360.
2. **minor: separator dots in lines 1 and 5 are not transcribed as they stand on the card.** SOLUTION.md says the dots follow the card.
   - `Pxo.`: no dot after the o (`z_pxo.png`); the next ink is the M. Make it `Pxo`.
   - `& L t..`: there is a dot after the & area and another after the L (`z_amp_L.png`), plus a wedge at the L's foot. Neither is in the transcription or discussed. `L. t..` would match the form recorded on hcp-1361. Note them, in the table or uncertainty 3. No letter is affected.
3. **minor: "two dots" in `t..` understates the first mark.** In `z_tdots.png` the first mark is about twice the width of the second, with a tail to the lower left. It may be a dot run into a stroke. It should be described that way in uncertainty 3; the group is literal and stays unexpanded either way.

## What I could not verify

- The meaning of `Lt..` and `M. h.`, and the expansion of `Y. O.`.
- The postmark town, which is not legible.
- That the Windsor cards existed; I found no sister text mentioning them.
- Whether a published solution exists. I ran no web search; this rests on the solver's statement, the orchestrator's register check and a grep of this repo.
