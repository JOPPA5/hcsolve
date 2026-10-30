ACCEPT

# Review 1 of HCP1131 (Pigpen dot-count postcard to Olive Ritter, Selden, Kansas)

Reviewer: Claude Opus 5.5, 2026-10-29. Reviewed state: DONE1 (GPT transcription
2026-10-25, completion by Claude Opus 5.5 as solver 2026-10-29).

## What I verified and how

1. **Solver's command.** `python3 ciphers/hcp-1131/work/decode.py` from the repo
   root: source hashes match, 74 glyphs, output identical to the plaintext in
   SOLUTION.md (YOU CAN NOT / WRITE SO I / CAN READ IT / I Wish I COULD / FLY
   HOME / DO YOU PLAY / ON THE ORGAN / I AM PRETTY / TIRED).
2. **Independent decode.** `review/work/indep_decode.py` uses my own collation
   (written from my crops, glyphs named by the sides actually drawn) and derives
   the letters from the standard Pigpen # grid (cell 1..9 = A..I) plus dot count
   for the block, without the solver's key table. Output is identical, 74 glyphs.
   The key is the same as the one accepted on HCP1189/1190 (same collection,
   same dot-count variant).
3. **Collation against the scan.** I made my own 4x row crops
   (`review/work/row1a.png` … `row8b.png`, `row7c.png`) and 7–12x crops of the
   critical spots (`ld.png`, `end.png`, `not.png`, `pretty*.png`, `home.png`)
   from `source/address-large.jpg` with PIL, and read every glyph of all eight
   rows plus the enclosed final word. Every outline matches the solver's token;
   word dividers (dashes) fall on the word boundaries.
4. **Completion points (added 2026-10-29), judged on the pixels:**
   - **COULD** (`ld.png`): two glyphs are visible — an L-shape (left + bottom)
     with two dots and a ⊐ with one heavy dot. The left glyph has no top stroke,
     the right glyph's top starts separately, and the bottom strokes leave a
     clear gap. Read as one box it would be a broken square with three dots
     (W, "COUW"), which is neither what is drawn nor a word. LD is a genuine
     pixel reading, not forced.
   - **TIRED** (`end.png`, `row7c.png`): a filled wedge/caret sits on the line
     between the ⊔ with three dots (T) and the Γ with two dots (R), directly
     below a Γ with one dot (I) written higher up. The insertion reading is
     supported; it is disclosed and encoded as `^TL1`.
5. **Context.** Hoxie and Selden are both towns in Sheridan County, Kansas, so
   the postmark and address are consistent. The green one-cent Franklin stamp is
   the 1908-type Washington–Franklin design; the solver states the year as
   uncertain (“190?”, c. 1908–09 likely), which is fair. The text is plain,
   idiomatic early-20th-century American English (26 words, grammatical), not
   words forced onto noise.
6. **Sources.** No published solution was found or used; the portal shows Not
   solved with no attached transcription. The key transfer from sister cards is
   disclosed.

## Findings

1. **Undisclosed dot discrepancy in PRETTY (minor).** The E of PRETTY
   (`review/work/pretty_e.png`, scan approx. x 400–430, y 590–628) shows **two**
   separate dots inside the square: a large blob touching the left stroke and a
   smaller clear dot to its right. Read strictly by count it is N (C2),
   giving "PRNTTY". The solver transcribes C1 (E) and NOTES claim all tokens
   were confirmed on collation, while SOLUTION.md uncertainty 4 names only the
   M of HOME and the D of COULD as heavy/blotted dots. The reading PRETTY is
   certainly right (the left blob is most likely a blot or a slip), but this
   sign is a context decision and should be listed in the uncertainties and in
   the report, like the other two.
2. **Dot counts on several Y glyphs are blotchy (minor).** The Y at the end of
   PRETTY (`pretty_y.png`) shows three ink marks, one of which may be two merged
   dots; the Ys of FLY and PLAY are similar. All are clearly ≥3 and Y is the only
   reading, so no change of text, but a short note under uncertainty 4 would be
   accurate.
3. **Unencoded punctuation not mentioned (minor).** There is a free dot after
   IT at the end of row 3 (beside the dash) and a dot right of the vertical
   divider level with row 2. They look like full stops/stray marks, not part of
   any glyph. Worth one line in the transcription notes so a reader does not
   wonder whether a glyph was skipped.
4. **Reproduction round-trip is internal only (minor, already disclosed).**
   `decode.py` round-trips the manual token list and checks source hashes; it
   does not read the image. The solver says so. Evidence for the transcription
   is the visual collation (theirs and this review's).

No blocker or major finding. The reading is correct, complete (74/74 glyphs)
and the two completions are supported by the pixels.

## What I could not verify

- The last digit of the postmark year (illegible on the scan); the sender's
  identity (unsigned).
- Whether a published solution exists outside the portal and the AI register
  (none found; absence is not proof).
- Picture side (lilies) viewed at full scan size: no cipher or writing apart
  from the portal stamp; nothing finer than the scan resolution was checked.
