ACCEPT

# Review 1 — HCP 1471 / pc_hcp_152 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the reading ARE WE DOWNHEARTED? is correct.** I read all 16 letters and both carets from the scan myself and get the solver's transcription exactly. The two places the solver flagged (v/w, final c/e) resolve in favour of its reading. Findings are minor.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1471/work/decode.py` exits 0; output byte-identical to `work/plaintext-check.txt`.
2. **Independent reading of the scan.** Body cropped from `source/address-large.jpg`, upscaled 3×, rotated 52° clockwise (`review/work/body-rot.png`); words cut out at higher zoom (`w12.png`, `w3a.png`, `w3b.png`) and the two doubtful letters at ~15× (`first.png`, `final.png`). My reading, made before comparing: `a̭qd vd cnvmgda̭qsdc?` (a̭ = a with a small caret written under it). Identical to `work/transcription.txt`.
3. **Independent decoder.** `review/work/review_decode.py` (own code; plaintext = cipher letter + 1, a̭ = A):

   ```
   $ python3 -I ciphers/hcp-1471/review/work/review_decode.py
   ARE WE DOWNHEARTED?
   letters: 16
   aqd vd cnvmgdaqsdc?      -> BRE WE DOWNHEBRTED?
   a^qd vd cnwmgda^qsdc?    -> ARE WE DOXNHEARTED?
   a^qd vd cnvmgda^qsde?    -> ARE WE DOWNHEARTEF?
   a^qd vd envmgda^qsde?    -> ARE WE FOWNHEARTEF?
   ```

   One shift covers all 14 ordinary letters; the two marked a's are the only exception and are the same mark both times. Every letter of the card is used.
4. **The doubtful letters.**
   - *v vs w* (3rd letter of word 3): `w3a.png` shows `n` (one arch) followed by a single `v` with a looped top-right flourish, the same form as the `v` of `vd`. There is no second v-stroke. **v**.
   - *Initial c* of word 3 (`first.png`): an open `c`, no eye. **c**.
   - *Final c* (`final.png`): heavily inked and overprinted by the printed word UNION, so the shape is blurred into a loop; nothing in it requires `e`. Since it must encode the same letter as the clear initial `c` (D…D), **c** is the right reading. The solver was right to flag it.
5. **Context.** "Are we downhearted?" — answered "No!" — was a well-known British catchphrase of exactly this time, popularised by Joseph Chamberlain in 1906. The card is postmarked `5.30 PM MY 16 06` (Wednesday 16 May 1906), local delivery in Swanley. A short political-catchphrase joke on a postcard is entirely plausible. I name the phrase from my own knowledge as confirmation; it was not needed to obtain the reading.
6. **Disclosure.** Both alternatives and the caret exception are stated openly; no published solution used.

## Findings

1. **minor — describe the key more simply.** The system is "write each letter as the one before it in the alphabet". For A that would be Z; the writer wrote `a` and put a caret under it instead — evidently a marker that this letter is not shifted (or "wraps"). Calling this a "Caesar+1 with an exception" is correct but the report should say plainly that the writer used a mark for exactly the one letter that would wrap round, which explains the exception rather than leaving it as an ad-hoc rule.
2. **minor — catchphrase not mentioned.** `SOLUTION.md` avoids connecting the text to the 1906 slogan "Are we downhearted? No!". The connection is well known and strengthens the case (date, British, period). Mention it in the report as context, clearly marked as context and not as part of the decipherment.
3. **minor — recipient name.** The card reads *Miss Puplett, Beulah, Birchwood Avenue, Swanley Junct., Local*; the portal has "Puklett". Note the card reading in the report (do not edit `source/metadata.md`).
4. **minor — text quality of `SOLUTION.md`/`NOTES.md`.** Spaces missing between words and numbers ("full16-letter", "Finalc", "markedA"). Fix before the PDF.

## What I could not verify

- The writer's identity and whether the question refers to the slogan, a private event, or both.
- The exact form of the last letter beneath the overprint (see 4 above); its value rests on the matching initial `c`.
- Whether a decipherment is published elsewhere; I relied on the solver's statement and did not repeat a web search.
