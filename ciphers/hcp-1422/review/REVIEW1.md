ACCEPT

# Review 1 – HCP 1422 (pc_hcp_103), Ivy to Carl Wieler, Mt. Carmel, Illinois

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-30. Round 1 (marker DONE1).

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1422/work/decode_v2.py` runs from the
   repo root, passes the SHA-256 check of `source/`, and prints exactly the 18-line
   plaintext given in SOLUTION.md ("374 glyphs read, 2 restored").
2. **Independent decoder.** `review/work/my_decode.py` uses a key I retyped from the
   SOLUTION.md table (not `work/key.json`) and its own tokenizer. Run as
   `python3 -I review/work/my_decode.py work/transcript_v2.txt`. Output (`review/work/mine.txt`)
   is identical letter for letter to the solver's output (diff empty). 376 glyph tokens
   (374 read + 2 restored), all 22 key classes used, no unknown token, no class mapped
   twice. Letter frequencies (E 49, O 37, T 33, I 31, A 27 ...) are normal English.
3. **Transcription against the scan.** I made my own enlarged crops of `source/address.jpg`
   (`review/work/crop.py`, `crop2.py`; 3–8x, some contrast-stretched) and checked:
   - all 18 lines at about 3x (`l1_2.png`, `l3_4.png`, `l5_6.png`, `l7_9.png`,
     `l10_12.png`, `l13_15.png`, `l16_18.png`): the overlined word groups and glyph
     counts match the transcript; HOW, YOUR, COLD, HOPE, BETTER, IN MT. CARMEL SATURDAY,
     NIGHT, CYNTHIANA, BEFORE THEN, DEPOT, HAV (three glyphs only), CANADISH,
     SATURDAY, CITY, ARRIVE, SKELTON, LOVINGLY, IVY read glyph by glyph.
   - **Line 9 "IN" (solver's correction of the GPT transcript):** a stroke with a dot below
     and a dash with comma-like dot stand after HER under their own overline. The
     correction is right; the earlier "{comma}" was wrong.
   - **K vs B** (both 2-like shapes, a possible confusion): at 5–8x (`kid.png`,
     `better.png`, `line6.png`, `skelton.png`) the K (KID, LIKE x2, SKELTON) ends in an
     upward v-hook, the B (BETTER, BE, BEFORE) has a flat foot. The split is consistent;
     SKELTON's second glyph is the K form.
   - **SAT[U]RDAY, line 3** (`l3span.png`, `l3_4R.png`, `pm.png`): over/among the stamped
     "FEB-8" I can see a pen v over the F, two dots inside the E, a pen cross over the B,
     a comma stroke right of the 8, then a small cross, two dots and a chevron at the
     edge of the circle. The U position is covered by the "-8". The restoration is
     forced by the visible neighbours and the two clear SATURDAYs, and is disclosed.
   - **[H]ER, line 4** (`l4full.png`, `l4b.png`, `l4c.png`): after FROM (wavy F, comma R,
     O, ÷ M are visible) the area is crossed by the postmark's time line. I see a dark
     vertical pen stroke reaching below the line, then a dark slanted hash (E) and a
     4-shaped R, darker than the grey postmark letters around them. Whether the
     stroke carries a dot above (H) cannot be seen. HER (as in clear HER on line 9) is the
     only sensible word; it is disclosed as a restoration. I agree with the
     solver's treatment.
4. **Language and context.** The text is fluent, informal early-20th-century American
   English and hangs together (cold, not going home Saturday, "her" is coming,
   meet in Cynthiana, the depot, "the city", Skelton). Mt. Carmel matches the
   address and the postmark ("MT CARMEL ... FEB 8"); Cynthiana, Posey County, Indiana,
   is a real town in the same area. Repeated words decode the same everywhere.
5. **Sources/credit.** SOURCES.md and metadata say the portal status was "Not solved"
   with no transcription or solution; I found no sign that a published solution was
   used. The GPT and Claude parts of the work are credited separately. 1422 is not
   in `register-exclusions.json`.

## Findings

1. **minor – the postmark year is partly readable and argues against the portal date.**
   SOLUTION.md (uncertainty 8) says the year digits are "too faint to read". In my
   crops `year.png` / `year2.png` (x 360–470, y 170–215, 7–8x) the grey postmark digits
   under the pen writing show "…9 1 3" (the first digit is lost under ink). With
   the 1-cent green Washington stamp of the 1908–1922 design, 1913 is far more likely
   than the portal's 1943-02-08 (by 1943 a different 1-cent stamp was current). The
   solver should say this in SOLUTION.md and the report (e.g. "postmark FEB 8, year
   probably 1913, last three digits seen as 913; portal says 1943") instead of
   leaving the date wholly open. It does not change the reading.
2. **minor – punctuation marks are interpretive.** The `/` after COMING and the "full
   stop" at the end of line 4 (a dark oval-and-stroke mark just outside the postmark
   circle) are labelled guesses. The disclosure is enough; the report should say that
   these are the solver's readings of pen marks, not cipher letters.
3. **minor – CANADISH and SKELTON are left unexplained.** Both are clearly written as
   decoded (I confirmed C-A-N-A-D-I-S-H and S-K-E-L-T-O-N on the pixels). Keeping them
   literal is right. The report could add that Skelton may be a local place or station
   near Mt. Carmel/Cynthiana (not identified), so a reader does not take it for a
   decoding error.

No blocker or major findings.

## What I could not verify

- The exact pixels of the hidden U (line 3) and of the dot on the H (line 4): they lie
  under the cancellation at 1024 px resolution. Both restorations rest on context and are
  disclosed as such.
- The identity of Ivy, of "her", and of the place Skelton; the first digit of the year.
- Whether the portal page has changed since 2026-10-26 (I did not re-open it).
