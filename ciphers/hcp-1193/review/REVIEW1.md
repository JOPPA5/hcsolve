ACCEPT

# Review 1 — HCP 1193 (numbered-Pigpen postcard to Helen, Kingston NY, Dec 1906)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-30. The reviewer's files are in
`review/work/`.

## What I verified and how

1. **Solver command.** I ran `python3 -I ciphers/hcp-1193/work/decode_full.py`. It reports
   "source hashes OK (5 files)". Its 13 output lines match the plaintext in SOLUTION.md exactly,
   and so does the count it prints: 223 cipher signs, 4 restored, 4 ambiguous and 1 outside the key.
2. **My own decoder.** `review/work/mydecode.py` does not use the solver's ordered SHAPES list.
   It rebuilds the key from the geometry of the # grid. A cell has a top stroke if it is not in
   the top row, a left stroke if it is not in the left column, and so on. The cell index plus
   9×(numeral−1) gives the letter. I ran it on `work/transcription-full.txt` and got the same text
   letter for letter. The key is the standard Pigpen # grid, read in row order, with the numeral
   selecting the block A–I, J–R or S–Z. The 27th cell is the only one left over.
3. **Coverage.** I counted the tokens myself and got 223 signs. Every token belongs to the key
   except one, the disclosed `TL3`. The frequency profile is what English text would give: C1 (E)
   27, L2 (O) 21, B3 (T) 21, TL1 (I) 20, BL2 (L) 19, BR3 (S) 17.
4. **Transcription against the pixels.** I made my own crops of `source/picture-original.jpg`:
   grey-scale, light blur, autocontrast and 1–5× enlargement.
   - Sample of ordinary rows. Line 1 HELEN and MY (`r1L.jpg`, `tl3.jpg`). Line 4 IST LOSDENN MIT
     DIR? — WELL (`l4L.jpg`, `l4.jpg`). Line 5 SWEE(THEART). Line 6 THERE. Line 9 YOU & HOW. All
     of them agree with the transcription sign by sign, numerals included.
   - Line 1, sign after MY (`tl3.jpg`). It is a clean top+left outline with a clear "3" and no
     other strokes, so the solver's TL3 is correct. Leaving it outside the key, rather than
     forcing it into a word, is the right decision.
   - Line 11, SO (`r11R.jpg`). A BR3 with underline is followed by a clear L2, and then
     TR1 L2 L2 R1 = GOOD. The added SO is real. The GPT transcription had missed it.
   - Line 12 (`r12L.jpg`, `r12R.jpg`, `l12K.jpg`). The signs read TL1 TR1 T1 B3 , BL2 L2 R3 C1,
     then a cursive "&", then B2 TL1 BR3 BR3 C1 BR3, then TR3 L2 BL3 TL2. Apart from the two
     points in findings 1 and 2, this confirms NIGHT, LOVE & KISSES YOUR.
   - Line 13, the signature (`r13a.jpg`, `r13b.jpg`, `s13.jpg`). I see the following signs:
     - L1, F. Its top stroke is short but present.
     - C1, E.
     - B3, T.
     - B3, T.
     - BR3?, S. The numeral is loose, like a "7" or a "3".
     - A left+bottom outline with numeral 2. Its "top" stroke merges with the long underline that
       comes down from line 12.
     - BL1, C.
     - A left+bottom outline with numeral 2, whose right side runs into the stamp.

     After these come marks under the stamp. My reading matches the solver's literal FETTSOCK with
     its four disclosed alternatives. I agree that the signature cannot be pinned down further.
5. **Stain restorations.** Each restored sign is marked `{}` in the output and listed in
   SOLUTION.md.
   - `{W}ELL`, line 1 (`w1.jpg`). A faint top stroke, a faint right stroke and a "3" are visible.
     The rest is lost in the stain. With numeral 3 the candidates are V, W, Y or Z, or S or T if
     the top is not a stroke. The solver correctly calls WELL a contextual choice, and it agrees
     with "— WELL SWEETHEART" in line 4.
   - `{T}HIS`, line 7 (`t7.jpg`). Only a right stroke and the numeral 3 are visible. THIS is the
     only word that fits.
   - `{T}ELL`, line 8 (`t8.jpg`). A faint "3" and a right stroke are visible. TELL is contextual,
     and the solver says so.
   - `{N}IGHT`, line 12 (`n12.jpg`). A top stroke, a right stroke and a small numeral are visible
     on the stain edge. N (C2) against P (TR2) is decided by the word. This is disclosed.

   None of the restorations is forced from context without saying so.
6. **Plaintext.** The text is natural English of around 1906 for a love card ("as I will be
   there almost as soon as this card", "love & kisses"). The German aside is idiomatic apart from
   the word order of LOSDENN, which is disclosed. Long words decode consistently: EXPECTED,
   SWEETHEART, ALMOST, KISSES, and HOW MUCH I twice. Random words forced onto noise do not behave
   like this.
7. **Date and place.** On the address side (`addr.jpg`) the postmark reads "KINGSTON, N.Y.
   DEC 8 7 A 1906", with a Rondout Station cancel. The receiving stamp is dated DEC 8. The
   address is Oyster Bay, New York. The header (`hdr.jpg`) reads "Friday · 9 P.M. ’06". I
   checked the weekdays: 7 Dec 1906 was a Friday, and 8 Dec 1907 (the catalogue date) was a
   Sunday. The solver's note that the catalogue year is probably one year off is supported, and
   it is worded as an observation, which is appropriate.
8. **Sources and credit.** The portal status was "Not solved", and nothing was attached.
   SOLUTION.md credits the GPT solver with the key and lines 1–11, and Claude with the 2026-10-30
   collation, SO, and lines 12–13. This agrees with NOTES.md and with the old
   `work/transcription.txt`, which stops at line 11 and lacks SO. SOURCES.md says openly that the
   HistoCrypt PDF was not examined.

## Findings

1. **minor — KISSES, sign 6: loose numeral not flagged.** The numeral in the last BR3 of KISSES
   (`review/work/k6.jpg`) is a single open hook. It is not the two-bowled "3" of the neighbouring
   signs, and it could be taken for a "2". BR2 would give J (KISSEJ), so S is safe in context.
   The transcription nevertheless gives it as a plain `BR3`, while the very similar loose numeral
   in signature sign 5 is disclosed as `BR3/BR2`. Add a one-line note, or mark it consistently.
2. **minor — line 12, signs 1 and 6 depend on context.** NIGHT depends on context (C2 against
   TR2 on the stain edge). This is already disclosed, and no change is needed beyond keeping it
   in the report.
3. **minor — provenance of `source/picture-original.jpg`.** Its download URL is not recorded
   ("presumably the portal's original conversion of media 3639"). The SHA-256 is recorded and the
   content matches `picture-large.jpg`. Record the exact URL if it can be recovered, or keep the
   "not recorded" note in the report.
4. **minor — wording of the signature interpretation.** "FETTSOCK, probably the German nickname
   Fettsack" appears in the translations. The uncertainty section rightly calls this an
   interpretation, because the pixels show O and not A. The translation lines should keep the
   same hedge ("possibly"), so that a reader of the PDF who sees only the translation does not
   take it as established.
5. **minor — check for a published decipherment is incomplete.** The HistoCrypt 2021 paper's PDF
   was not examined. SOURCES.md already says so. Repeat that in the report.

There are no blocker or major findings. The key, the transcription of lines 1–12 and the
plaintext stand.

## What I could not verify

- The signs under the collection stamp after the signature. They are not legible at the
  available resolution, and both the solver and I leave them unread.
- The recipient's surname, and whether the initials are M. R. or M. P. (address side, "Rod?mond").
  This does not affect the decipherment.
- Whether the HistoCrypt 2021 article prints a solution of this card. I did not examine its PDF.
