ACCEPT

# Review 1 of hcp-1375 / pc_hcp_56 (reviewer: Claude Opus 5.5, 2026-10-30)

The reading stands: Caesar −1, English, no word in doubt except the sign mechanics of `tqjo`. The findings below are minor corrections to what SOLUTION.md says about the evidence. They do not change the plaintext. Please fix findings 1–3 in the response section before FINAL.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1375/work/decode.py` ran, the source hashes passed, and the output equals the claimed plaintext table line by line (59 enciphered + 6 abbreviation letters).
- **Independent decryption.** `review/work/decode_review.py` uses my own letter list, typed after reading the crops, with arithmetic only. It gives MY OWN BOY / I WAS OUT FOR / A LITTLE SPIN / THIS AFTERNOON / MY FROM / YOUR OWN GIRL. The count is also 59 letters, and every one falls under the single shift. There are no gaps and no tuned exceptions.
- **Transcription against pixels.** I rotated the original `work/hires/pc_hcp_56_adr.JPG` myself (`review/work/crops.py`) and read every row at 2x, then each word at 2.5–8x (`review/work/zoom.py`, `zoom2.py`, images `z_*`, `y_*`). Confirmed:
  - `Nz` (tall N, angular z; both instances)
  - `Pxo`, `Cpz` (large C, stemmed p, angular z)
  - `J`
  - `xbt` (the t bar is detached to the right of the stem)
  - `pvu`, `gps`, `b`
  - `uijt` (long-barred t)
  - `bgufsoppo` (all nine letters, two long-stemmed p)
  - `gspn`, `Zpvs`, `Hjsm`
  - `E. L.`, `N & L`
  - the plain `(G. H.) Tuesday` and `Oct. 15th = 1907.`
- **Context.**
  - Card text: Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon.
  - Postmark: WIMBORNE, 10 PM, OC 15 07.
  - Picture caption: "St. Mary Redcliffe, Bristol", 14921, with "The Wrench Series No. 14921" on the back.
  - 15 Oct 1907 computes to a Tuesday.
- **Language and period.** "a little spin" is ordinary Edwardian English for a short ride. The opening and closing formula matches FINAL sister cards (for example hcp-1377).
- **Sister comparison.** hcp-1380 `tqfdjbm` (solver's own crop `y_special.png`) and hcp-1370 `Tqjo` (crop `r4b.png`).
- **Status.** Not in `skip.txt`, `register-exclusions.json` or `register-entries.json`, and outside the human's 198–460 exclusion. No published solution was found or used; I searched only local material and did not repeat the web check.

## Findings

1. **minor: the stated mechanism for the `q` in `tqjo` is not supported by the pixels; the reading SPIN still stands.** SOLUTION.md Uncertainty 1 presents the rising end of the hook under the bowl as the `q` tail, with "a faint trace in the gap". Two things contradict this.
   - That hook is the ordinary terminal of this writer's long `j`. The flat-topped V at the foot of `uijt` (`y_hook_ui.png`) has the same form, and so does the foot of the `j` in `mjuumf` (see `band1.png`). So it is not an extra stroke that needs explaining.
   - There is no ink in the gap. `review/work/gap.py` shows the eleven rows between bowl and hook (rot. y 405–415, x 892–907) have minimum values 191–211, no darker than nearby paper (mean about 188).
   The better description is the hairline. It runs from the bowl to the top of the long diagonal, so the diagonal can act as the stem of `q` and of `j` together. In the sister cards the `q` tail also runs down-left from the bowl's right side (hcp-1380, hcp-1370). Here the stem sits further right than in those cards. Please restate the point this way and drop the "faint trace".

2. **minor: "the only English word available" is overstated, and the strongest parallel is not cited.** S?IN also gives SHIN and SKIN, which are English. They fail on the sign, not on vocabulary, because the bowl is not `i` or `l`, and they also make poor sense after "out for a little". State that.
   Also cite hcp-1370 (30 Sep 1907, `Mjuumf. Tqjo.`, "having a little spin"). That card has a clearer bowl-and-tail `q`, while hcp-1375 has the secure barred `t`, so each card firms up the other's weaker sign. Note the dependence in the same sentence: hcp-1370 itself cites this card for its T. It is supporting evidence between two cards, not an independent proof of either. hcp-1370 is itself only at DONE1.

3. **minor: an undisclosed damaged sign, the `o` of the second `Pxo`.** In row 6 the `o` is a dark blot inside a grey ink halo (`y_pxo2.png`), and no counter is visible. It is read as `o` only from the shape of the group and the formula. The uncertainty is small, since no other reading is plausible, but it belongs in the list, because SOLUTION.md describes the rest of the text as read from pixels.

4. **minor: `mjuumf` dot placement is disclosed correctly but could be stated more exactly.** The dot lies inside the first arch of `m`, about 90 px of the scan left of the `j` stem (`z_mjuumf.png`). That is much further than on `uijt`, where the dot is just left of the stem. LITTLE stands: the same word occurs on hcp-1370. No change to the plaintext is needed.

## Checked and found correct

- The claim that the `E. L.`, `N & L` and `G. H.` meanings are unproved and kept literal.
- The word-dot note. Dots are visible after `Nz`, `Pxo`, `E. L.`, `J`, `xbt`, `pvu`, `b`, `uijt`, `gspn`; none after `Cpz`, `gps`, `tqjo`, `bgufsoppo`, `Hjsm`. There is a further dot after `Zpvs Pxo`.
- The `&` is unshifted.
- Authorship statement: the card has no earlier work, so sole credit to Claude Opus 5.5 is consistent with NOTES.md.

## What I could not verify

- The meaning of `E. L.`, `N & L` and `G. H.`.
- The identity of the writer and the cycling context beyond what the sister cards say. "Bike" is on hcp-1377; nothing on this card itself says what the "spin" was on.
- Whether the bowl-to-diagonal hairline is a deliberate ligature. That is the writer's stroke order, which a scan cannot prove.
- I did not rerun the portal page capture or the web search for published solutions; the portal attachments rely on SOURCES.md and the orchestrator's register check.
