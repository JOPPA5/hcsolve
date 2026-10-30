ACCEPT

# Review 1 — HCP 1800 (pc_hcp_481), numbered-Pigpen postcard to William S. Wilson

Reviewer: Claude Opus 5.5, 2026-10-30. Reviewer files: review/work/.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1800/work/decode.py` (repo root) prints
   `source hashes OK` / `YOUR ROCKING CHAIR PLAN LOOKS` / `SAFER AND MORE COMFORTABLE`,
   identical to the claimed plaintext. The script reads only work/transcription.txt
   (manual tokens), which is disclosed.
2. **Independent decoder.** review/work/indep.py builds the key from scratch from the
   position of each cell in a 3x3 grid (row/column -> which sides are drawn) and the
   numeral 1/2/3 as block A–I / J–R / S–Z. On work/transcription.txt it gives the same
   two lines. Every token in the transcription maps to a letter; nothing left over.
   Output: `signs: 48 distinct tokens: 20`.
3. **Transcription vs. scan.** review/work/crops.py and zoom.py crop the text strip of
   source/picture-large.jpg, rotate it upright, autocontrast, and enlarge 5–12x
   (strip.png, r0–r5.png, L1_*.png, L2_*.png, z_*.png). I checked every word:
   - YOUR, ROCKING, CHAIR, PLAN, LOOKS, SAFER, AND, MORE, COMFORTABLE: sign count per
     word and outlines agree with the transcription.
   - The O/N and F/E distinction holds on the pixels: N (C2 in ROCKING, PLAN, AND)
     and E (C1) are closed boxes; O (L2) and F (L1, z_fe.png) have no right side.
     This rules out the main confusion I tried to force.
   - G of ROCKING (z_g.png): top + right stroke with a slanted numeral 1 on the left
     = TR1; not T1 (H).
   - R of MORE (z_more.png): left stroke and numeral 2 clear, top stroke not visible
     to me at all. Disclosed by the solver as weak.
   - M of COMFORTABLE (z_m.png): top+bottom+right is clear; at 12x the numeral looks
     more like a **3** than a 2 to me (flat-topped "ʒ" form). Disclosed by the solver;
     see finding 3.
   - K and S at the end of LOOKS (z_ks.png): K's numeral is indistinct and the final
     S's numeral (3) is faint against the right edge; outlines correct.
   - P of PLAN: the base of the 2 does look like a bottom stroke (disclosed).
4. **Language and context.** Nine ordinary English words forming one grammatical
   sentence, idiomatic for c. 1905–1910 American English, and a precise joke on the
   printed picture (couple kissing on a tall step-ladder, caption "Love at it's
   height"). Random fitting of a known key to noise would not produce this.
5. **Key provenance and honesty.** The key is the standard Pigpen grid with numerals,
   as on sister HCP 1193 / 1131 / 1189 / 1190; carried over and disclosed as such.
   Portal status Not solved, no attached solution; I found no sign a published
   solution was used. Credit to the earlier GPT session is stated truthfully.

## Findings

1. **minor — sign count wrong.** SOLUTION.md says 47 signs/letters ("all 47 signs",
   "decodes all 47 signs", "every one of the 47 letters"). The transcription has 48
   tokens (4+7+5+4+5 + 5+3+4+11 = 48), confirmed by indep.py. Fix the number.
2. **minor — repetition statistics and attested letters inaccurate.** In "Why this is
   correct": R = TL2 occurs **6** times (YOUR, ROCKING, CHAIR, SAFER, MORE,
   COMFORTABLE), not 5; A = BR1 occurs **5** times (CHAIR, PLAN, SAFER, AND,
   COMFORTABLE), not 4. "Letters attested (19)" omits **U** (YOUR, BL3); there are
   20 letters. The argument still holds but the figures must be corrected.
3. **minor — M of COMFORTABLE.** The numeral looks closer to 3 than 2 on my crop.
   Reading M is forced by the word (V gives COVFORTABLE) and the outline is certain,
   so the reading stands, but SOLUTION.md/report should say plainly that this letter
   is fixed by context, not by the pixels. Likewise the R of MORE (top stroke not
   visible) and the numerals of K and S in LOOKS are context-supported; the
   K/S numerals are not yet listed among the uncertainties.
4. **minor — dating.** The address side has a divided back ("This space may be used
   for correspondence"), which in US practice dates the card to after 1 March 1907;
   with the 1903-series 2 c Washington stamp this gives c. 1907–1910 (the stamp
   was replaced in 1908–09). Could be added to the context; currently only
   "c. 1903–1908 plausible" is stated. A faint postmark (".. ORK"?) is partly visible
   left of the stamp and not mentioned.

## What I could not verify

- Only the 1024-px portal scans exist; individual numerals (M, K, S) cannot be read
  with certainty at this resolution.
- The sender and exact date; the identity of William S. Wilson of Highrock, Pa.
- Whether the pencil "30- SECRET CODE" is a dealer mark (plausible, not provable).

Verdict: ACCEPT. The reading is correct and covers the whole ciphertext; only the
minor corrections above remain.
