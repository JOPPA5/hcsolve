REVISE

# Review 1 of hcp-1364 (pc_hcp_45) - Claude Opus 5.5, reviewer, 2026-10-30

Summary: the Caesar -1 reading of all 38 enciphered letters stands. I tried to break it and could not. One transcription claim fails on the pixels: the initial of the two abbreviation groups is not the N of `Nz`, as SOLUTION.md says. It has the same three-stroke form the solver uses to read M in `Mfuufs`. That and small transcription and citation errors need fixing before FINAL.

## What I verified and how

- **Solver command:** `python3 -I ciphers/hcp-1364/work/decode.py` ran, source hashes passed, and the output matches the claimed plaintext and the counts (38 + 4). I recomputed `source/*.jpg` and `work/hires/*` with `shasum -a 256`; they match SOURCES.md.
- **Independent decode:** `review/work/decode_review.py` uses modular arithmetic on my own sign-by-sign reading, not transcription.json. Result: MY OWN BOY / LETTER VERY / NICE TO DAY / YOUR OWN / GIRL, 38 letters. Shifts 2 and 3 give gibberish (printed by the script).
- **Pixels:** I rotated `work/hires/pc_hcp_45_adr.JPG` 90 degrees anticlockwise and enlarged every line 4x and key signs 7x (`review/work/hd.png`, `l1…l5.png`, `cap_compare.png`, `cap_end.png`, `minims.png`, `m_hjsm.png`). Every enciphered word was read sign by sign, so this is the full text, not a sample:
  - `Nz`, `Pxo` (twice), `Cpz`, `wfsz`, `ojdf`, `up`, `Ebz`, `Zpvs`, `Hjsm`: all confirmed.
  - The f of `ojdf` has a dry grey descender, visible and part of the sign, not an overlay. The same is true of the f of `wfsz`.
  - `Pxo` on line 4 looks like "Bo" at low zoom. At 4x the stem, the separate crossing strokes of x, and the o are all there, as the solver disclosed.
  - The `uu` of `Mfuufs` runs together, but its minim count is compatible with two u's (`minims.png`).
  - Final `m` of `Hjsm` is blotted. Its strokes fit m, and the word needs L.
- **Whole card:** the picture side has no writing; the sky blot is damage (`review/work/pic.png`). Nothing else on the address side is enciphered. Address (Mr W. Abbott, Stokelake Farm, Chudleigh, Devon), postmark WIMBORNE 10 PM JY 17 07 and Boots "Pelham" imprint all confirmed (`adr_rot.png`).
- **Date:** 17 July 1907 computed as a Wednesday, matching the plain heading.
- **Language:** real, terse period English in the couple's formula. hcp-1402 has the same salutation and close, and `Mfuufs` opens its message the same way. The verbless "letter very nice to-day" is disclosed.
- **Key coverage:** one key covers all 38 letters with no exceptions and no card-specific tuning.
- **Restorations:** none claimed, and I found none hidden. This is a first-pass solver card with no completion or response sections.
- **Register:** hcp-1364 is not in `register-exclusions.json` or `skip.txt`.

## Findings

1. **major - The abbreviation initial is read N on a false comparison; the pixels favour M.** SOLUTION.md (Uncertainty 1) says "The N is the card's two-arch capital (as in `Nz`)". Side by side in `review/work/cap_compare.png`, left to right, `Nz`, salutation group, closing group, `Mfuufs`:
   - The `Nz` capital is hook, stem and one arch ending in a single foot.
   - Both group initials have an extra short downstroke at the foot. It is clearest in the closing group (`review/work/l4b.png`), where a separate third leg is visible.
   - That is the same construction as the `Mfuufs` capital, which the solver reads as M because it is three-stroke (Uncertainty 2).

   The solver therefore applies two opposite criteria to one sign form on one card. Sister cards hcp-1383 (uncertainty 2) and hcp-1347 (uncertainty 3) read M on exactly this three-against-two count; hcp-1368 and hcp-1402 keep N. The extra leg could be a pen artefact on the salutation form, so N is not fully excluded.
   Fix: transcribe `M. L.` / `M-L.`, with N not excluded, or mark the initial M/N undecided. Remove "as in `Nz`". Update the shifted value (L. K. rather than M. K.), `transcription.json`, the plaintext table and both translations. The enciphered reading is not affected.

2. **minor - Punctuation in the transcription does not follow the manuscript, though SOLUTION.md says it does.** The first row is given as `Nz. Pxo. N. L. Cpz.`. On the card there is no dot after `Cpz` (`review/work/cap_end.png`, `reading.png`) and no dot after the L of the group: the only dot stands between initial and L (`review/work/l1b.png`). Dots carry no meaning here, but the row should be `… N. L Cpz` (with the initial from finding 1). Fix `transcription.json` and the table.

3. **minor - Wrong sister citation.** The cipher section says `N. L.` / `N-L.` are kept literal "as on sister cards hcp-1402 and hcp-1384". hcp-1384 has `E. L.` and mentions `N. L.` only as a comparison with hcp-1402. Cite hcp-1402 and hcp-1368 instead, or hcp-1347 and hcp-1383 if finding 1 is adopted.

4. **minor - Unsupported citation for `Mfuufs`.** Uncertainty 2 says the word shape decides the sign "as on sister card hcp-1383". A grep of that card's SOLUTION.md and NOTES.md for "compact", "word shape" and "METTER" found nothing. The sign there is lowercase-position `mfuufst`. The comparison with hcp-1386 (`work/crops/mfuufs.png`) does hold, and the capitals match in form. Keep that one and remove or justify hcp-1383.

5. **minor - L not flagged as possibly another sign.** The second sign of the groups is a slanted stem with a foot, close to a 1 or plain l. The hcp-1402 response records "N. 1 / N. l is not excluded" for this same closing form, and hcp-1349 and hcp-1366 report `h` in this slot. SOLUTION.md gives L without that caveat; add it.

## What I could not verify

- The meaning of the groups, and whether they are enciphered at all. The card cannot decide this.
- The expansion of G. H. (the form with a descending tail fits G; C is not wholly excluded) and the writer's identity.
- That no published solution exists: I did no web search of my own. The orchestrator's register check covers the AI register only. Nothing in the solver's files shows use of one, and the plain reading follows from the sister key.
- Same-hand claim: judged by eye from one crop of each sister (hcp-1386, hcp-1402), not measured.
