ACCEPT

# Review 1 — HCP 1450 / pc_hcp_131 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the decipherment is correct and complete.** I read all 118 Pigpen signs in the seven rows of `source/picture.jpg` myself, checking the heavy and blotted ones at 8–14×, and got the same letters with the same three-count Pigpen key. No cipher text is missing. The solver disclosed the uncertainties honestly. I add one sign whose dot count is open (finding 1), and none of my findings changes the reading.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1450/work/decode.py` runs (exit 0), the hashes pass, and it prints the seven claimed lines (`118 cipher letters`), identical to `work/plaintext-check.txt`.
2. **Independent decoder.** `review/work/pigpen_review.py` (my own code, which builds the key from the grid geometry; see the HCP 1442 review for the definition) applied to my own sign-by-sign transcription `review/work/my-transcription.txt`. I wrote that transcription from my crops, recording the strokes present and the dot count for each sign. Output (`review/work/my-output.txt`):
   ```
   DEAREST EMMA / WELL SWEETNESS / HOW BE YOU? I DONT THINK / I CAN COME HOME UNTIL /
   AFTER EXAMINATIONS DR won't / EXCUSE US CAN YOU READ / THIS? WITH LOVE DEAREST EDW   (118 glyphs)
   ```
   A letters-only comparison with the solver's output is **identical** (118 = 118).
3. **Independent reading of the scan.** Row strips at 4× (`review/work/r1.png` … `r7d.png`), plus detail crops at 7–14× for the hard signs: `z3you.png` (YOU: ┐3 [2 └3), `z3think.png` (end of THINK: K = ⊔2), `z4come.png` and `z4home.png` (O = [2 under a large blot, M = ]2), `z5after.png`, `z5a.png`, `z5b.png`, `z5c.png`, `z5ons.png`, `z5dr.png`, `z5d.png` (EXAMINATIONS and DR), `z6x.png` (X of EXCUSE), `z6you.png`, `z7edw.png`. My reading agrees with `work/transcription.txt` in **every one of the 118 signs**, including the word divisions (the slashes on the card) and the two plain `?`.
4. **Key consistency.** One fixed key with no exceptions (counted by script over my transcription). No letter needs two different signs and no sign needs two different letters. The frequent letters behave consistently: E = □1 ×19, T = ⊔3 ×10, A = ┘1 ×9, S = ┘3 ×9, I = ┌1 ×8, N = □2 ×8, O = [2 ×8, D = ]1 ×6.
5. **Missed cipher text.** I looked at the whole picture side, including the bed and kittens area and the margins. The only other handwriting is the plain heading `Warrenton, Mo. / May. 26, '05.` and the cursive `won't` in row 5. On the address side, the faint pencil strokes at the left (`review/work/pencil.png`) are loose lines and one or two scribbled letter-like loops. They contain no grid signs or dots, so I agree they are not cipher. The plain address is `Miss Emma Alwin, New Ulm, Minn.`. **No Pigpen signs are left untranscribed.**
6. **Context.** The postmarks are `WARRENTON MAY 26 … PM 1905 MO.` and the receiving mark `NEW ULM MINN. MAY 2? 9- 1905` (`review/work/pm.png`), next to a machine `RECEIVED` cancel. Together with the heading, they give Friday 26 May 1905. The decoded salutation `DEAREST EMMA` matches the addressee. End-of-term examinations in late May fit the message ("I don't think I can come home until after examinations"). `HOW BE YOU`, `DONT` and the abbreviated `EDW.` (period after it on the card) are kept literally, which is correct.
7. **Prior solutions.** The portal status is Not solved. The register snapshot has no `pc_hcp_131` or `cryptograms/1450` (I re-grepped it), and the cipher is not in `skip.txt`.

## Findings

1. **minor — the D of `DR` has an oversized dot; `MR` should be listed as an alternative.** In `review/work/z5d.png` (14×) the dot inside the ] outline is a continuous elongated blob. Its grey values are ≤ 135 over about 8 × 4 px with no light gap (`review/work/dr-dot-pixels.txt`). That is roughly twice the length of a single dash-dot elsewhere. It runs diagonally from upper right to lower left, which is exactly the arrangement of the two dots of M in `EMMA` (`zr1m.png`). So ]1 = D or ]2 = M cannot be settled from pixels alone. `DR` is still the better reading: a bare title without a name ("Dr won't excuse us") is natural for a school's head, while a bare "Mr" is not, and the single-dot D in row 1 is also dash-shaped (`zd_r1.png`). The solver's `NOTES.md` considers DR vs IS but not DR vs MR. Add `MR` to the list of visual uncertainties. The reading does not need to change.
2. **minor — confirmation of the other flagged signs.** The X of `EXAMINATIONS` and of `EXCUSE`, both A's of EXAMINATIONS and the E of `EDW` are, as the solver says, heavy blots whose dot count cannot be counted. For each of them the outline is clear: [ for X, ┘ for A, □ for E. Every alternative dot count gives a non-word (`EFAMINATIONS`, `EOCUSE`, `EJAMINATIONS`…), except for the E of EDW, where N (`NDW`) or W (`WDW`) would be possible in principle. `EDW.` with its full stop is the usual abbreviation of Edward, so E is the natural reading. These are disclosed correctly.
3. **minor — context not recorded.** `SOLUTION.md` does not mention the two postmarks (Warrenton MAY 26 1905 PM; New Ulm received MAY 2? 1905) or that 26 May 1905 was a Friday. Both support the date and route and belong in the report.

## What I could not verify

- The day on the New Ulm receiving mark (`MAY 2?`) is not legible.
- Who "Edw." and "Dr" were. Warrenton, Mo. had a college at the time, which would fit "examinations" and "Dr", but I did not check this and the solution need not rely on it.
- Whether a decipherment has been published elsewhere beyond the register snapshot. I did not search the web.
