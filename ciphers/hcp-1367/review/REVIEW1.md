REVISE

# Review 1 of hcp-1367 / pc_hcp_48

Reviewer: Claude Opus 5.5, 2026-10-30. Solver: Claude Opus 5.5 (same model, separate session, so this is not a cross-vendor check).

The message stands: Caesar -1, English, "My own loving boy. Very many happy returns of the day. Your own ... girl." The fixes needed are in the transcription of the closing group and in two statements about signs. None of them changes the sense.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1367/work/decode.py` ran clean: 4 hashes OK, 54 enciphered letters, output equal to the table in SOLUTION.md.
2. **Independent decode.** `review/work/indep.py` has its own table and a transcription retyped from my crops, and does not read the solver's files. Output equals the solver's for all 54 letters. Of the 26 shifts only -1 (row 25 of the output) gives language.
3. **Key coverage.** Every enciphered token decodes with the one key. No sign is skipped or treated specially apart from the plain heading, the plain date and the closing group.
4. **Pixels.** I read all rows from the un-converted `work/hires/pc_hcp_48_adr.JPG`, turned 90 degrees CCW and enlarged 3-6x (`review/work/r0..r6.png`, `z_*.png`; scripts `crops.py`, `crops2.py`, `crops3.py`). Side-by-side comparison of the capitals: `review/work/compare_signs.png`.
   - Confirmed sign by sign: `Nz`, `Pxo` (twice), `Cpz`, `Wfsz`, `nboz`, `Ibooz`, `Pg`, `uif`, `Ebz`, `Zpvs`, `Hjsm`. In `Mpwjoh`, the letters p, w, j, o, h.
   - Plain text confirmed: `G. H. Thursday.` and `July 25th 07`.
   - `j` of `Mpwjoh`: the solver is right. Its foot hooks back up into the top of the `C` below, with the same check-mark shape as the j of `Hjsm`. `Cpz` is C, not E.
5. **`Ibooz`.** Both middle signs are small closed loops without tails, joined by a top ligature, and they match the `o` of `nboz`. No q is visible. HANNY as the literal decode and HAPPY as the intended word are correct, and the emendation is disclosed.
6. **Context.** 25 July 1907 was a Thursday (computed). Postmark WIMBORNE, 10 PM, JY 25 07, and the address to W. Abbott, Stokelake Farm, Chudleigh, Devon, read correctly. The picture side is printed "Shrine of Edward the Confessor, Westminster Abbey" and has no handwriting.
7. **Language.** Ordinary period English. "Many happy returns of the day" is the fixed phrase, and "My own loving boy" recurs on hcp-1351, 1360, 1361. The plain Thursday heading fits the sister cards.
8. **Sources.** SOURCES.md matches the hashes. The solution declares its use of sister-card formulae, and no published solution appears to have been used.

## Findings

1. **major: the closing group is not `N-L`, and the stated evidence is wrong.** SOLUTION.md (uncertainty 4) says both signs are N "(same form as `Nz`)" and L. `compare_signs.png` shows otherwise.
   - The capital has three downstrokes: long stem, second leg and a short third leg before the dash. `Nz` on this card has two. The form matches the M of `Mpwjoh`, not the N of `Nz`.
   - The second sign, a tall stem with a low right hump ending in a blob, matches the final `h` of `Mpwjoh` on this card, not a plain L.
   - The sign-based reading is therefore `M-h`, which is what hcp-1361 and hcp-1369 read in this slot by the same three-downstroke criterion. hcp-1366 and hcp-1371 have `N. h.` in the slot too (hcp-1363 has `N. L.` / `N-L.`).
   - Uncertainty 4 cites only `E. L.`, `N. & L.` and `E-L.`, so the `M-h` / `N-h` family is left undisclosed.
   - Fix: transcribe `M-h` in the table, `transcription.json` and the plaintext, with `N-L` as a note if desired. State the comparison signs. The meaning remains unknown, and the message is otherwise unaffected. These sister cards are themselves only at DONE1 or under review, so cite them as parallels, not as authority.

2. **minor: `Sfuvfsot` is the less supported count of signs.** Primary reading is cups = `u v`, giving RETUERNS; SOLUTION.md gives the seven-sign reading (cups = one u) as second choice.
   - Only two minims stand between the crossed f and the pale f (`review/work/z_retu.png`).
   - On this card `u` alone is two minims (`uif`, `review/work/z_uif.png`), while `v` in `Zpvs` is a wide zigzag with a rising exit (`z_zpvs.png`). A u plus v should show about four strokes.
   - The better literal is `Sfufsot` = RETERNS, with the pale sign still f. RETERNS is also the likelier misspelling.
   - Fix: make `Sfufsot` primary, RETUERNS the alternative, and change the count to 53 letters, or give explicit reasons against. This also removes "RETUERNS" from `intended`.
   - The solver's caution is correct that the intended word is not in doubt, and that these signs are the weakest on the card.

3. **minor: the third leg of `Mpwjoh` is supported but should be stated more firmly and with better evidence.** The solver's argument rests on a merged third leg and on sense. The thick double ridge at the second leg (`review/work/z_mp.png`) is consistent with this, and the sign is the same form as the capital in the closing group (finding 1). Cite that comparison. MOVING is excluded by sense, not by pixels alone.

4. **minor: heading initial G/C is not disclosed.** Several sister solutions record that the capital of `G. H.` may be C (hcp-1355, 1386, 1397). This card's G has a large loop and a foot (`review/work/r0.png`) and G is the better reading, but the doubt should be one line in Uncertainties, as uncertainty 5 now calls G. H. settled.

5. **minor: follow-on text.** Update the status line, the "54 enciphered letters", the normalised English and the Slovak if findings 1 and 2 are adopted. The register entry and report must carry the corrected group.

## Could not verify

- The meaning of the closing group and of G. H.
- That the occasion was a birthday. The phrase implies it, and nothing else on the card confirms it.
- That no published solution exists: the solver ran no web search and neither did I. Portal status and the absence of attachments are taken from `source/metadata.md`.
- The reason for the two slips. The o-for-p explanation is a guess, labelled as such by the solver.
- The exact form of the third leg of the M in `Mpwjoh`, where it merges into the stem of p.
