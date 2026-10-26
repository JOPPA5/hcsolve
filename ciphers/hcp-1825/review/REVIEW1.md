REVISE

# Review 1 — HCP 1825 / pc_hcp_506 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the key and the body of the message are right, but the transcription has three errors, and they change the closing.** The card is signed **KIND LIVE MARY** (most likely meant as "Kind love, Mary"), not `KIND LIUE CRY`. The literal text also has `YOW` where the solver prints `YOU`. All three errors are in the transcription and none is in the key, so the fix is small. But the closing and its translation are currently wrong, and the signature, the only name on the card, is missing.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1825/work/decode.py` reports matching hashes and prints the eight lines claimed in `SOLUTION.md`, ending `KIND LIUE CRY.`, from 94 letter glyphs.
2. **Independent reading of the scan.** I made crops of `source/address-large.jpg` with `sips` (`review/work/crop.sh`):
   - `body.png` is an overview of all eight rows at 3×.
   - `r1-a.png` … `r8-b.png` show each row in two halves at 7×.
   - `z*.png` are 12–14× details of every sign I disputed.

   I read every sign before comparing with the solver's file. My reading is in `review/work/my-reading.txt`, using my own notation (grid cell or wedge by the direction of its point, `*` = dotted).
3. **Independent decoder.** `python3 -I ciphers/hcp-1825/review/work/review_decode.py ciphers/hcp-1825/review/work/my-reading.txt ciphers/hcp-1825/work/transcription.txt`. It builds the key from `ACEGIKMOQSUWY` / `BDFHJLNPRTVXZ` and aligns the two transcriptions with difflib:
   ```
   I HOPE YOU ARE
   A GOOD DEAL BETTER.
   WHAT KIND OF
   WEATHER ARE YOW
   GETTING?VERY
   WET HERE ANY
   MORE MARRIAGES?
   KIND LIVE MARY.
   95 signs; distinct 21
   letters written with >1 sign: none
   solver signs: 94
     replace: solver[48:49]=['wR'] -> reviewer[48:49]=['wL']  (U -> W)
     replace: solver[89:90]=['wR'] -> reviewer[89:90]=['wR*']  (U -> V)
     replace: solver[91:92]=['2'] -> reviewer[91:93]=['7', '1']  (C -> MA)
   ```
   Apart from these three places, all 91 other signs agree with the solver's, including every dot.
4. **Key consistency.** No letter is written with two signs, and no sign needs two values. Several features make this a real key rather than one forced onto the text:
   - The writer marks the "dot" as a short dash. It is visible in H (∃), L (⊏ with dash), B, F, N and D.
   - The two T's of BETTER and GETTING are filled or dotted downward wedges.
   - The pair ⅂⅃ = MA appears in MARRIAGES and again in the signature.
5. **Context.**
   - Above the cipher is the plain-text line "Both puzzles correct", and a later pencil note at the top reads "Coded Message".
   - The address reads **Miss Stirling, Islay House Square, Bridgend, Islay**. `source/metadata.md` has "Stay House Square". Islay House Square is the actual square in Bridgend, Islay.
   - The picture side shows "Kilbarchan from the Public park" and no cipher. The cancel at top right shows "KIL…", consistent with Kilbarchan.
   - The body is natural, informal British English of the period: a get-well wish, weather talk ("very wet here" fits west Scotland) and gossip ("any more marriages?").
6. **Prior solutions.** No solution was attached on the portal. The solver checked the 110-record register snapshot and found no match. I found nothing undisclosed.

## Findings

1. **major — the signature is MARY, not CRY.** Detail: `review/work/z8-mary.png`, compared with `z7-ma.png`.
   - The last word of row 8 consists of a top+right sign (⅂: top bar running left from a vertical), then a bottom+right sign (⅃), then a dotted top+left sign, then an upward wedge.
   - The first two signs are drawn exactly like the M and A of MARRIAGES in row 7. The only difference is that here the foot of the ⅃ runs left until it touches the foot of the ⅂. That is what turned it into one "⊔" (C) in the solver's transcription.
   - A ⊔ reading cannot explain the top bar sticking out to the *left* of the left upright. Undotted ⊔ (C) occurs nowhere else on the card.
   - So the word is TR0 BR0 TL1 ^0 = **MARY**, which makes 95 signs, not 94.
   - Consequences: the closing is "Kind l(o)ve, Mary". The sender's name is Mary, and "CRY [možné iniciály]" must go from the plaintext, the translation and the uncertainty list.
2. **major (transcription) / minor (meaning) — the V of the closing word is dotted, so the literal reading is LIVE, not LIUE.** Detail: `z8-love.png`.
   - There is a clear short dash-dot in front of the ">" wedge, the same as the dotted ">" of VERY in row 5 (`r5-b.png`). So it is >1 = V.
   - The word therefore needs **one** departure from the key, not two. The second sign is a closed box (I) where LOVE needs ⊓ (O, T0). The box has its bottom stroke, so I agree the literal letter is I.
   - The writer most likely drew the box instead of ⊓. Present it as "LIVE (for LOVE, one sign: box for ⊓)" and drop the "two entered glyph values" argument.
3. **major (transcription) / minor (meaning) — the end of row 4 is "<", not ">", so the literal reading is YOW.** Detail: `z4-you.png`, compared with `z1-you.png`.
   - In row 1, YOU ends with a right-pointing wedge.
   - In row 4, the wedge points unmistakably to the **left**. It is drawn the same as the W that opens rows 3, 4 and 6.
   - The intended word is obviously YOU, but this is a writer's slip, like LIVE. The solver's transcription silently normalises it, and the literal decoded output therefore hides it. List it with the other anomalies.
4. **minor — the "small overwriting after GETTING" is a question mark.** Detail: `z5-q.png`. Between the G of GETTING and the dotted V of VERY there is a heavy hook with a dash below it. It has the same form as the "?" after MARRIAGES in row 7. So the writer punctuated "What kind of weather are you getting? Very wet here." The `?` is source punctuation, not editorial, and should be in the literal text.
5. **minor — a stray mark after the M of MORE.** Detail: `z7-more.png`. There is a dot at the baseline between ⅂ and ⊓. It sits outside the TR outline and touches the foot of the ⊓, whereas this writer puts dots inside the sign at mid-height. So I read it as a pen touch and the letter as M (undotted). Taken as a dot it would give NORE, so English confirms M. It is worth one line in the uncertainties.
6. **minor — record keeping.**
   - Correct the address observation in `source/metadata.md` and `SOURCES.md` from "Stay House Square" to "Islay House Square". The README forbids changing `source/`, so a note in `SOURCES.md` is enough.
   - The commas between words are the writer's word separators. The full stop after BETTER and the closing full stop are written, so not all punctuation is editorial.

## Required for closing

- Fix the transcription to 95 signs: row 4 `… ^0 T0 <0`, row 8 `L1 C0 >1 BL0 | TR0 BR0 TL1 ^0`, plus the `?` after GETTING.
- Literal text: `… ARE YOW / GETTING? VERY … / KIND LIVE MARY.` Normalized text: "… are you getting? Very wet here. Any more marriages? Kind love, Mary." List the two writer's slips (YOW→you, LIVE→love), one sign each.
- Update the translation and the uncertainties to match (sender "Mary"; remove the CRY/initials discussion).

After these corrections I see no need for another review round. The changes affect the record and the closing, not the key or the body text.

## What I could not verify

- The date. The Kilbarchan cancel is partly under the stamp and I cannot read its date. The catalogue gives none.
- Who Mary and Miss Stirling were. The "puzzles" mentioned on the card suggest a regular exchange of puzzle cards, but nothing in the source confirms it.
- Whether this card has been deciphered elsewhere. I did not repeat a web search.
