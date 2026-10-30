REVISE

# Review 1 of hcp-1363 (pc_hcp_44), reviewer Claude Opus 5.5, 2026-10-30

The key and the reading of the card stand: Caesar -1, and MY OWN LOVE? BOY / MANY THANKS FOR CARDS OF WINDSOR / LOVE & Lt.. FROM Y. O. .. GIRL. One concrete fix is needed. The headline word LOVER rests on a sign that the hand's s does not support. The same sign recurs on two sister cards, where it is read differently.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1363/work/decode.py` ran, the hashes passed, and it reported 54 enciphered + 4 literal letters. The output equals the table in SOLUTION.md. I recounted 54 by hand.
- **Independent decode.** `review/work/my_decode.py` uses my own retyping from my own crops, without the solver's JSON. It gives the same text, with the disputed sign left as `?`. In a sweep of all 26 shifts, only shift 1 yields any of the 12 target words; every other shift scores 0. The whole ciphertext is covered, and no per-word adjustment is needed.
- **Pixels.** I rotated `work/hires/pc_hcp_44_adr.JPG` 90 degrees counter-clockwise and enlarged it 3-5x, with a blue-minus-red ink filter (`review/work/a1`...`g`, `h_*`, `cmp_*`).
  - Confirmed sign by sign: Nz, Pxo, Cpz, Nboz, uibolt, gps, dbset, pg, Mpwf (line 4), gspn, Z., P., Hjsm.
  - `Xjoetps` is acceptable as disclosed. The t with detached dash, the pale p with long stem and the weak final s are all there (`h_windsor_end.png`).
  - `& L t..` is real ink, not forced. The pale looped L and the c-like stroke with dash and two dots have the same geometry as the fresh `Lt..` on hcp-1366 (`work/crops/kiss.png` there), and the disclosure is accurate.
- **Dates.** 19 July 1907 was a Friday (computed). The postmark reads 10 PM / JY 19 / 07. No town letters are legible on the part of the cancel I enlarged (`pm2.png`), which agrees with the solver.
- **Language.** Apart from finding 1, this is ordinary period English in this couple's formula. "Thanks for cards of Windsor" is not a stock phrase on the sisters.
- **Disclosure.** The Caesar key and the sister-card parallels are disclosed.

## Findings

1. **major: `Mpwfs` / LOVER is not supported, and the alternatives offered are too narrow.** Solver's uncertainty 1 is honest about doubt, but it limits the doubt to LOVER/LOVED, and the headline prints LOVER as read.
   - Shape (`review/work/cmp_all.png`, first panel against the s of `gspn`, `Hjsm`, `gps`): the writer's s is a small ball with a rounded arc, ending in a curve or an exit stroke. The disputed sign is a closed loop on the baseline, a straight rise to a sharp angle at the top, and a straight fall to a heavy blob. It has no rounded arc, and the fall and blob have no counterpart in any s on the card. The blob is joined to the stroke, so "s plus a separator dot" is itself an assumption.
   - Recurrence, which is the decisive point (`review/work/slot_compare_1363_1366_1360.png`): the same construction follows `Mpwf` in the same line-1 slot on hcp-1363, hcp-1366 and hcp-1360. Three solver reports currently give it three different treatments: `s.` here, nothing (`Mpwf.`) on hcp-1366, and `h.` on hcp-1360, whose solver describes the same looped rise, top turn and fall to a blob. The solver flagged hcp-1366 but missed hcp-1360.
   - A recurring fixed form in the slot that normally holds an initial group (`E. L.`, `N. L.`, `N. h.`) points to one shared sign, not a one-off word ending. No other SOLUTION.md in the repo has `Mpwfs` or LOVER as a reading.
   - Other candidates:
     - `h.` (the hcp-1360 reading, MY OWN LOVE [h.] BOY);
     - `z` (`Mpwfz` = LOVEY). The sharp turn, diagonal and heavy foot are like the z of `Nz` and `Cpz`, though the rising entry is not. This is my hypothesis only;
     - `e` (LOVED), which the solver already notes.
     None of these is proved.
   - Fix: transcribe `Mpwf` plus one unresolved sign, and show it as LOVE[?] in the headline and in all translations. List s, h, z and e with their evidence, cite hcp-1360 and hcp-1366, and change "54 letters decoded" to 53 secure + 1 unresolved. "Every word gives English" holds only if that sign is left out of the claim. Do not edit the sister directories from here.

2. **minor: the first sign of `N. h.` has M's build on this card.** In crop `f.png` it has a long stem and two further downstrokes, three in all, like the M of `Mpwf` and unlike the two-stroke N of `Nz` and `Nboz` on this card. Uncertainty 8 says only that M is "not excluded". Transcribe `M. h.` (N possible), which matches `M-h` on hcp-1369. It is a literal group, so no word changes.

3. **minor: the t of this hand is under-described, and a dash is unexplained.**
   - The `-` token after `uibolt` is not discussed. It sits about 50 px past the last stem, against about 10 px for the detached bar of `Xjoetps`, so it is either a line-filling dash or a displaced t-bar. Say so.
   - The final tall strokes of `uibolt` and `dbset` have no bar on the stem, so they are indistinguishable from l, and the words rest on THANKS and CARDS.
   - Uncertainty 5 says no cross-bar is visible, but a dot sits up and to the right of the `dbset` stem (`c2.png`, about (505,165)), at the place of this hand's detached bar. It is a possible bar remnant and is at least worth stating.

4. **minor: `& Lt..` support should carry the parallel from the hcp-1371 review.** hcp-1395 reads `M. & L.` as enciphered (L. & K., editorially love & kisses). Add that next to "Ks" in uncertainty 3, still as a labelled hypothesis. Add r to the alternatives for the small sign, as on hcp-1371. The solver treats `Z. P.` as enciphered and L, t, N, h as literal. This is disclosed, but the reason for the split (only formula slot) should be stated.

5. **minor: two marks are not mentioned.** There is a grey horizontal streak with a dark upright blot under `gps` (`c1.png`), and a long dark line under `Hjsm` running to the card edge (`g.png`, possibly a pen flourish or a card defect). Neither bears a letter. List them under "all ciphertext on the card" as non-text.

## What I could not verify

- The meaning of the disputed sign, `Lt..`, and `N./M. h.`.
- The postmark town.
- Whether "lover boy" was idiomatic in 1907; I did not research attestations.
- Whether a published solution exists. I ran no web search; this rests on the solver's statement, the orchestrator's register check and a grep of this repo.
- That the Windsor cards existed; the sister texts do not mention them.
