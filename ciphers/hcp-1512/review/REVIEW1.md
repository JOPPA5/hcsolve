REVISE

# Review 1 — HCP 1512 / pc_hcp_193 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the key is correct and the letter is real English, but one word is misread.** In line 8 the card says `POSTING`, not `WRITING`: the three glyphs the solver transcribes as `BQT` are on the card `8 W Y`, i.e. a new glyph (P) followed by the ordinary O and S glyphs. This changes the plaintext, so the verdict is REVISE. The other findings are minor.

## What I verified and how

1. **The documented command.** `python3 ciphers/hcp-1512/work/decode.py` runs (exit 0), prints the 13 lines in `SOLUTION.md` exactly, and reports 281 positions / 22 glyph types. Like the other postcard solutions, it decodes the solver's manual transcription. It does not read the image, so it cannot catch reading errors.
2. **Independent reading of the scan.** I did not start from `work/transcription.txt`. I cut `source/address-large.jpg` into 4× strips (`review/work/hdr.png`, `body0.png` … `body6.png`) and 8–12× details (`z-*.png`; helper `review/work/crop.sh`, sips only). Then I read every glyph, using only the shape-to-ID convention from `work/transcription-legend.md`. My reading is in `review/work/my-transcription.txt`, with punctuation kept and `%` for the Φ-shaped form (finding 2).
3. **Independent decoder.** `python3 -I review/work/decode_review.py review/work/my-transcription.txt` uses the key typed from the `SOLUTION.md` table plus `8=P`:

   ```
   I HAVE BEEN INSIDE HERE
   MY OWN DARLING OF COURSE I
   WILL WRITE TO YOU WHILEI AM
   ON MY HOLIDAY. IF I CAN GET
   AWAY FOR A TOUR I WILL WRITE
   EVERY NIGHT JUST TO GIVE
   YOU A SHORT ACCOUNT OF
   THE DAY'S DOINGS. I AM POSTING
   THIS ON TUESDAY NIGHT WECAUSE
   I WANT TO HAVE A GOOD LONG
   SNOOZE TOMORROW MORNING AND
   I WANT TO START RIDING EARLY ON
   THURSDAY, YOUR LOVING FRED
   # positions=281 glyph types used=24 unknown=[]
   ```

   Diff against the solver's transcription (punctuation stripped): line 1 `TNYT2R` vs `TN YT2R` (spacing), line 3 `B4T6RT` vs `B4T6R T` (spacing), **line 8 `8WY0TNS` vs `BQT0TNS`**, line 12 `R%Q6J` vs `RPQ6J` (glyph variant). Every other line matches glyph for glyph.
4. **Key consistency and coverage.** On the solver's transcription, the key is injective and covers all 281 positions. With my reading it still covers all 281 positions; the only addition is glyph `8` = P. P was "unobserved" in the solver's key, so `8` collides with nothing. The N/Y split (η-shaped = N, fork = S) holds everywhere I looked (`NIGHT`, `JUST`, `SNOOZE`, `INSIDE`, `DOINGS`). The C-glyph (open, hooked `q`, in `COURSE`, `CAN`, `ACCOUNT`, `BECAUSE`) and the R-glyph (closed-bowl `q`) are distinguishable, though only just, at 1024 px.
5. **WECAUSE.** I confirm it: the first glyph of `BRcPZYR` is the same B-shape used for W in `WILL`/`WRITE`, not the I-stroke used for B in `BEEN`. The solver disclosed this correctly.
6. **Language and context.** This is natural Edwardian English (`snooze`, `the day's doings`, `start riding early`). The header `I HAVE BEEN INSIDE HERE` refers to the picture: Tuck's "English Cathedrals" series, Norwich. The portal date 1905-05-23 was a **Tuesday**. The postmark (`review/work/z-postmark.png`) reads IPSWICH … MY 2? 05, and its hour looks like `11 PM`, though I am not certain. That fits "I am **posting** this on Tuesday night" better than the solver's "writing". The addressee is Miss E. Barnard, Hammersmith, as the solver says.
7. **Prior solutions.** Nothing in the files suggests a published solution was used. I did not repeat the web or register search.

## Findings

1. **major — line 8 reads POSTING, not WRITING.** Details are in `review/work/z-writing.png` (8×) and `z-posting.png` (12×). The word is seven glyphs: `8 W Y 0 T η S`.
   - The first glyph is an 8-shape with two stacked loops. Nowhere on the card is it used for W, and it is clearly unlike the flat-backed `B` of `BT66`/`BQT0R`.
   - The second glyph is the ordinary `w`-shape (O), not the `q`-shape (R).
   - The third glyph is the fork (S), not `T`.

   Compare `BQT0R` (WRITE) in lines 2 and 4, which really does look like `B q T 0 R`. Under the existing key the word reads `?OSTING`, and the only English fill is `POSTING`, which needs a new 23rd glyph type `8`=P. Corrections needed: the transcription, the plaintext, the translation (`píšem` → `posielam/odosielam`) and the glyph count. Also remove "P unobserved" from the key section.
2. **minor — the A in EARLY is a variant form.** Detail in `z-early.png`. The second glyph of `EARLY` is a Φ-like shape (a bowl with a stroke through it), heavier than every other `P`. It is probably a retraced or overwritten A-glyph. The reading is not in doubt, but this is a visual uncertainty and should be listed with the others.
3. **minor — punctuation is on the card but not in the transcription.**
   - `SOLUTION.md` says `DAYS` is written "no added apostrophe". In fact there is a raised mark between `D` (Y) and `Y` (S) in `2PJ'Y`, so the card has `DAY'S` (`z-doings.png`).
   - There are also full stops after `HOLIDAY` and `DOINGS` and a comma after `THURSDAY`.

   Punctuation is not cryptographic, but the diplomatic transcription should record it, especially since the solver explicitly claims there is no apostrophe.
4. **minor — word division `IN SIDE`.** In the header (`z-hdr.png`) the gap between `η` and `Y` is no wider than the gaps inside the word, so `INSIDE` as one word is at least as well supported. The final `R` of that word also has a vertical stroke through it (an overwrite or correction), and this is not mentioned.
5. **minor — context left unused.** The postmark is **Ipswich**, not Norwich, and the time appears to be late evening on 23 May 1905. Neither is recorded in `SOURCES.md`/`SOLUTION.md`. Both are useful evidence for the dating ("Tuesday night", "tomorrow morning", "Thursday") and for the holiday/touring context. Please state the hour as uncertain.
6. **minor — protocol.** No `.watch.log` exists for this cipher. `NOTES.md` says no watcher was launched "under prior user override". This is noted only for the record.

## Required for closing

- Fix line 8 of `work/transcription.txt` (`8WY0TNS`) and add `8`→P to `work/key.json`. Update the plaintext to `I AM POSTING THIS ON TUESDAY NIGHT`, along with the translation and the glyph-type count.
- List the Φ-form in EARLY, the header overwrite and the punctuation (`DAY'S`) in the uncertainties or diplomatic notes.

Once these are made, I see no need for another review round. The rest of the reading I confirm glyph by glyph.

## What I could not verify

- The exact postmark hour and day: the digits overlap the stamp design.
- Whether the C-glyph and R-glyph are always kept apart by the writer. At this resolution two or three instances are borderline, and context resolves them.
- Whether the gap in `WHILE I` is a space. I read `B4T6RT` as continuous; it makes no difference to the plaintext.
- Publication elsewhere: I relied on the solver's register check and did not search the web.
