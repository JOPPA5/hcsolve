REVISE

# Review 1 — HCP 1467 / pc_hcp_148 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the decipherment is correct, but one glyph is transcribed wrong, and the wrong reading is defended in the solution.** The closing word is **LOVE**, not LOUE: the wedge carries an internal dot, which the solver says it does not have (finding 1). Every other one of the 62 glyphs matches my own reading. Verdict REVISE because `SOLUTION.md`, `NOTES.md` and `transcription.txt` make a positive, false claim about the scan; the message itself does not change.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1467/work/decode.py` exits 0 and its output is byte-identical to `work/plaintext-check.txt`.
2. **Independent reading of the scan.** I cropped the body from `source/address-large.jpg`, upscaled it 3× and rotated it 38° clockwise (`review/work/body-rot.png`), then cut each line out (`l1.png` … `l7.png`) plus 7× details of the closing word (`love-rot.png`), the signature (`sig-rot.png`) and LOOK (`look.png`, `look2.png`). I recorded each glyph by the strokes it has and whether there is a dot inside, before comparing.
3. **Independent decoder.** `review/work/review_decode.py` builds the interleaved Pigpen key itself (each # cell = two letters, second dotted; X cells = S–Z) and decodes my own glyph list. It also converts the solver's labels to mine and compares glyph by glyph:

   ```
   $ python3 -I ciphers/hcp-1467/review/work/review_decode.py ciphers/hcp-1467/work/transcription.txt
   HOPE TO / SEE YOU WITH / LUCK SOON LOOK / OUT FOR THREE /
   COUNTRY YOKELS / LOVE / BOO[dots]BOO
   letter glyphs: 62
   solver glyphs: 62
     differs at glyph 55: reviewer >* (V) vs solver > (U)
   ```

   One key, applied to all 62 glyphs, no glyph needing two values; the key covers the whole text. 61 of 62 glyphs agree.
4. **Plaintext and context.** Plain, idiomatic English: "Hope to see you with luck soon. Look out for three country yokels. Love, Boo Boo." Addressee *Miss Adah Thompson* (card), postmark `… 1 PM JY 13 07`, matching the portal date 1907-07-13 (a Saturday). The postmark town looks like `…DERSFIELD` (Huddersfield?), which would fit a writer joking about "country yokels" coming to London (Streatham); I did not establish this.
5. **Disclosure.** Transcription declared as the solver's own, no published solution used, the dot cluster in the signature left uninterpreted. Good.

## Findings

1. **major (transcription) / minor (meaning) — LOUE is LOVE.** Line 6, third glyph. In `review/work/love-rot.png` (7×) and `l6.png` there is a clear dot inside the opening of the `>` wedge, at mid-height, touching distance from the apex. It is not a word separator: those sit at the baseline *after* a word (one follows the `L` of this word), and a separator between O and U would make no sense. Under the solver's own key `>` + dot = V. Compare the undotted `>` in LUCK, OUT, COUNTRY (`l3.png`, `l4.png`, `l5.png`), which have no such dot. So the literal text is **LOVE**. `SOLUTION.md` ("The observed wedge is undotted >0"), `NOTES.md` and `work/transcription.txt` (`>0` in line 6) must be corrected, and the "LOUE as written / LOVE as interpretation" discussion removed.
2. **minor — dot cluster in the signature.** I agree with the solver: the dots in the first BOO stand above and to the right of the third glyph (`∩`), outside its frame (`sig-rot.png`), so BOO, not BOP. Their purpose (decoration, a separator between the two BOOs) is unknown; leaving them as an unassigned mark is correct.
3. **minor — smudge in LOOK.** The first `∩` of LOOK has an ink blob at its lower-right foot (`look2.png`). It lies outside the frame and between the glyphs, so it is not a dotted P; the solver's O is right. Mention it among the scan notes for completeness.
4. **minor — text quality of `SOLUTION.md`/`NOTES.md`.** Spaces missing between words and numbers ("All62", "Fresh Not solved2026-10-26", "secondBOO"). Fix before the PDF.

## Required for closing

- Change glyph 55 to the dotted wedge (`>1`) in `transcription.txt`, re-run the command, and present **LOVE** as the literal reading in `SOLUTION.md`, `NOTES.md` and the report.

This is a correction of one letter that brings the text into line with the card; I see no need for another review round after it.

## What I could not verify

- The postmark town (partly off the stamp); Huddersfield is my guess, not a reading.
- The identities of "Boo Boo" and of the three "yokels".
- Whether a decipherment is published elsewhere; I relied on the solver's statement and did not repeat a web search.
