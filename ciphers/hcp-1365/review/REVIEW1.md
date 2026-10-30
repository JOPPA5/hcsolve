ACCEPT

# Review 1 of hcp-1365 / pc_hcp_46 (reviewer: Claude Opus 5.5, 2026-10-30)

The Caesar −1 key and the English message stand. Five minor findings remain: two letters of `gpsfwfs` are contextual (already disclosed), and the other four findings are gaps in the disclosure. None changes the plaintext, and none needs another review round.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1365/work/decode.py` ran cleanly. All 4 hashes passed (they equal those in `SOURCES.md`). It reports 70 enciphered letters, and its output matches the `SOLUTION.md` table line by line.
2. **Independent decoder.** `review/work/indep.py` uses ciphertext I re-keyed from my own crops, not `transcription.json`, and tries all 26 shifts. Only shift 1 gives English: 20/20 tokens are words. The next best shifts give 1/20. Count: 70 letters, which also matches my hand tally per line (8+10+13+8+13+11+7).
3. **Scans.** I rotated `work/hires/pc_hcp_46_adr.JPG` 90° CCW (`review/work/rot.py`) and made 3x crops of every line (`c_l1` to `c_l7b`). I made 5–6x crops of each disputed word (`z_*.png`; `crop.py`, `crop2.py`, `crop3.py`). Every token was read from these crops.
4. **Context.**
   - Picture caption: "West Park Promenade and Prospect Hotel, Harrogate".
   - Stamp and postmark: halfpenny Edward VII, WIMBORNE, JY 22, 07. The hour reads 10AM on my crop.
   - Address, printer line and the plain heading "G. H. Sunday." all confirmed.
   - 22 July 1907 was a Monday, so a Sunday heading fits.
   - The formulae `Nz Pxo … Cpz` and `Hjsm` occur on FINAL cards (hcp-1386 and others). I checked this as text in their `SOLUTION.md` files, not on their pixels.
5. **Published solutions.** The portal has no attached solution per the captured metadata. I found no sign of one being used.

## Line-by-line result

| Line | Reading | Verdict on pixels |
|---|---|---|
| 1 | Nz Pxo M. L. Cpz. | Clear. Crop `z_boyend` shows the p bowl and a flat-footed z; `Cpz` has exactly 3 signs. |
| 2 | J. bn. Tpssz up | Clear. Double s has the two-hump form. |
| 3 | ifbs zpv. bsf Opu. | First three words clear. `Opu`: see below. |
| 4 | xfmm. Nboz | `xfmm` has six minims, so mm is right. `Nboz`: see below. |
| 5 | uibolt. gps. dbse. | Readable; see F3 and F4. |
| 6 | & gpsfwfs. zpvs | `&` and `zpvs` clear; `gpsfwfs`: see F1. |
| 7 | Pxo. M. L. Hjsm. | Clear despite dry pen. H has two stems and a bar, j a hooked tail, then s and m. |

**Claimed weak points, judged on the pixels**

- **`Opu`.** The large loop runs into a long stem. A faint bowl, starting at a blot, sits at the stem, then a faint two-minim u and a dash. The solver's reading is supported.
- **`Nboz`.** The dot after N is the blotted foot of N's second leg, not punctuation. See F2 for z.
- **`M`.** In line 7 I see a stem and two further legs, against one in `Nz`, as the solver says. In line 1 the third leg is only a blob. M is preferred and N stays possible, as disclosed.

## Findings

1. **F1, minor: `gpsfwfs` rests on context for two letters. Disclosed, but the disclosure can be sharper.**
   - Evidence, `z_fv.png`: g, p (tall stem, bowl), a small s hook, an f with a looped descender and the final s are all visible.
   - The oval with an inner hook is not a recognisable w. The card has no other `w` to compare it with.
   - The long heavy stem has **no loop**, unlike the looped f of `ifbs`, `bsf` and `xfmm`, so its reading as the second f is weaker than a simple form match. `SOLUTION.md` does not state this.
   - My tracing is that the hook and loop at upper right belong to line 5 g and p, so the stem appears to be a separate line 6 stroke.
   - I also found no better word. Letters F-O-R-?-?-?-R with this sense point to FOREVER, and "& for ever your own" is natural closing idiom. Word division (FOR EVER) cannot be determined.
   - Fix: add the unlooped-stem note. Keep the word labelled contextual in the report.
2. **F2, minor: the note on `Nboz` describes the z imprecisely.** Crop `z_many.png` shows that the z's own top stroke, diagonal and long foot are mostly **visible below** the blot. The reading is therefore better than "restoration for a partly hidden sign" suggests. The heavy bar above is a separate stroke at the point where the gray descender from `Opu` lands. The solver calls this the descender of the line above, which is right, but the bar itself remains unexplained. Fix: say so.
3. **F3, minor: an undisclosed weak sign, the final `t` of `uibolt`.** `z_thanks.png` shows only a short faint upstroke rising from the foot of the l, with no crossbar and a blot by it. THANKS forces it, but the sign is not independently readable. It should be listed, like the z above.
4. **F4, minor: an undisclosed weak sign, the final `e` of `dbse`.** `z_cardend.png` shows a compact cross-shaped sign (a bar over a hooked tail), not a looped e, and resembles this writer's x more than an e. Ciphertext `e` occurs nowhere else on this card, so there is no within-card control. CARD is forced by "many thanks for" and by sister cards that give the same word (for example `dbse` on hcp-1392 FINAL; hcp-1378 notes a forked tail on it). The solution should say this in its uncertainties.
5. **F5, minor: "Why it is correct" lists FOREVER among its long words.** Since F1 makes two of its letters contextual, it should not count as evidence for the key. SORRY and THANKS are enough. This does not affect the verdict.

## Also checked, no issue

- Key coverage is complete: every enciphered token uses shift 1, and only `&` and the initials are outside it.
- The English is normal 1907 sweetheart wording; names, place and date fit the Abbott correspondence.
- Initials `M. L.` are left unexpanded, and the shifted alternative L. K. is disclosed.
- Credits claim no earlier work, and `NOTES.md` agrees.
- `SOLUTION.md` calls this "whole message read" and flags the exceptions directly below. That is acceptable.

## What I could not verify

- The two contested letters of `gpsfwfs`, on any evidence but context.
- The meaning of `M. L.` and of the heading `G. H.`.
- Whether the card's initials are literal or enciphered; only literal is consistent with sister-card practice.
- Sister-card pixels for hand identity: I compared their written solutions, not their scans.
