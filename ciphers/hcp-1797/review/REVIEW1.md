REVISE

# Review 1 of hcp-1797 / pc_hcp_478 (Claude Opus 5.5, reviewer, 2026-10-30)

The Caesar −1 reading stands: 38 of 38 enciphered letters outside `Wbn` are confirmed against the pixels. One concrete fix is needed: the last sign of the unresolved group is better read m than n, so the default shifted value is VAL, not VAM, and the statement that the watermark hides the end of the group is not true. The group stays unresolved, so this is a partial solution.

## What I verified and how

- **Solver command.** `python3 -I ciphers/hcp-1797/work/solve.py`: four hashes OK, output equals the SOLUTION.md table, 38 letters, 1908-01-29 is a Wednesday.
- **Independent decode.** `review/work/indep.py`, with my own reading typed in, not taken from `work/transcription.json`. The same plaintext comes out: MY OWN BOY / I AM SENDING / ... FOR / MY FROM / YOUR OWN / GIRL. Letter count by hand: 2+3+3+1+2+7+3+2+4+4+3+4 = 38.
- **Transcription against the scan.** I rotated `work/hires/pc_hcp_478_adr.JPG` 90° CCW (`review/work/rot.png`). Every line was checked at 3x (`a1`–`a4.png`), and `Wbn`, `bn`, `Gspn`, `Hjsm`, `Nu. & L.`, `El.`, `Cpz` and `Tfoejoh` at 4–10x (`wbn.png`, `wbn_tail.png`, `m_*.png`). There are no restorations or later completions; the solver's single section is one reading.
- **Whole-card coverage.** Nothing else is written on the address side, and the picture side has only printed captions. Address, stamp, postmark (WIMBORNE, 10 PM, JA 29, 08) and Tuck's Oilette 7016 caption all agree with SOLUTION.md.
- **Language and context.** Period English. The heading, salutation and closing formulas match the sisters. Checked in their SOLUTION.md: hcp-1402 (28 Jan, `Nz. Pxo. N. L. Cpz.`), hcp-1404 (30 Jan), hcp-1405 (`Nz. Pxo. El Cpz.`, `Mu`), hcp-1407 (`N.-1`), hcp-1377 (`J. bn`, clear `Wimborne`, `Sat:`), hcp-1403 (`J. bn`), hcp-1392 (`Tfoejoh`).
- **Published solutions.** None is disclosed or apparent. Portal status is as recorded in `source/metadata.md`. The number is not in `skip.txt` or `register-exclusions.json`.

## Findings

1. **major – last sign of the unresolved group is m-like, not n; the watermark claim is wrong.** Uncertainty 1 says the group "runs into the watermark ring, so n or m cannot be settled", and Uncertainty 5 says the disc "hides the end of `Wbn`". In `wbn_tail.png` the ink is visible through the ring: three separate legs, then a long exit stroke. Nothing is hidden. The writer's n on this card has two small humps (`bn` on line 3 in `m_bn.png`; `Gspn` in `m_gspn.png`), while his m in `Hjsm` has three (`m_hjsm.png`). So the reading is `Wbm`, shifted VAL, with `Wbn`/VAM as the weaker alternative. Fix: change the transcription and the `solve.py` output (which prints only VAM), and correct both uncertainty notes. I found `Wbm` in no sister SOLUTION.md. I do not propose a meaning: VAL could be a name, but nothing on the card proves it, and it must not be substituted into the plaintext.

2. **minor – one piece of evidence for W is missing.** My own reading agrees with W for the first sign, and the case is stronger than stated. A pale long bar starts left of the second stem's top and runs right over the whole group, ending near its last leg (`wbn.png`), like the bar on the W of "Wednesday" (`a1.png`). The small spur on the first stem matches the W's connector. Add this. The HAM, MAM and JAM rejections stand on the first sign. A reader might still take the bar as a T-cross on the second stem, so W stays the best reading, not a certainty.

3. **minor – second sign not settled.** The solver says b, with d possible. At 7x the base loop lies close to the stem line and the incoming ligature from the W closes it, so I could not decide either. Disclosed correctly; `Wdm` gives VCL, which is no word, so b is preferred on sense only.

4. **minor – description of `Nu.`.** Uncertainty 2 calls the u-like sign "raised-looking". In `m_nul.png` it stands on the baseline after the N stem. The literal `Nu.` is fine; fix the wording.

5. **minor – undisclosed weak sign.** The z of `Cpz` on line 2 is a faint flat stroke (`m_cpz.png`). BOY is the only sense and matches the sisters, but add it to Uncertainty 4.

6. **minor – sister claim too broad.** "Salutation and closing match hcp-1402, 1405 and 1407": hcp-1407's salutation is `Nz. Pxo. Efbsftu.`, so only its closing matches.

7. **note for the register step – this is a partial solution.** The object of the only sentence is unread. README step 7 allows no entry for a partial solution, so the solver must label the status as partial in `SOLUTION.md` and the report and write no `register-entry.txt` unless the group is resolved and re-reviewed.

## What I could not verify

- The meaning of the `Wb?` group, and whether it is enciphered or a clear name. I tested no external reference beyond a grep of the sister SOLUTION.md files.
- The meaning of `E. L.`, `Nu. & L.`, `El.`, and of the heading `G. H.` (or C. H.).
- Sign 2 of the group (finding 3). The scan's resolution (300 dpi, JPEG) is the limit.
- That the three-leg count is decisive: this writer's minims vary, so m is the better reading, not a proven one.
