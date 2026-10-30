ACCEPT

# Review 1 - hcp-1475 (pc_hcp_156)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-30.
Claim under review: the margin line `ILMWAMWLM.` is an initialism for
"I love my wife and my wife loves me."

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1475/work/decode.py` (from the repo root):
   both source hashes `ok`, prints `ciphertext: ILMWAMWLM` and
   `plaintext : I love my wife and my wife loves me.` This matches SOLUTION.md.
2. **Transcription against the scan, all nine letters.** My own crops of
   source/address-large.jpg, rotated 90 deg CCW, autocontrast:
   - `review/work/line_ccw.png` (whole line, 4x) and `review/work/line_cw.png` (the other rotation, which gives mirrored letters, so CCW is the right reading direction);
   - `review/work/mid_x7.png` (x 265-340, y 90-280, 7x): **I L M W A**, all clear. Letter 3 is /\/\ (M), letter 4 is \/\/ (W); the GPT reading "Y M" for letters 3-4 is wrong, as the solver says.
   - `review/work/end_x8.png` (x 260-345, y 250-450, 7x): **A M W L M** and a full stop. Letter 6 has the same four-stroke M form as letter 3; its last stroke does come down to the baseline (shorter than the first, but there is no break that would make it "MI" or "N"). Letter 7 is a W, letter 8 an L (with a slanted upright), letter 9 an M, then a dot.
   My reading is the same as the solver's: `ILMWAMWLM.` No sign is restored and none needs to be.
   The large grey wheel with letters across the card is the portal's watermark, not part of the cryptogram.
3. **Rest of the card.** Address side: only the address "Mrs P. H. Ellis, 50 Eversley Road, Charlton S.E.", the purple "11 JUL 1910" hand stamp, pencil "£4 50" (dealer price) and the publisher imprint. Picture side (windmill): no writing. So the nine letters are the whole ciphertext and the solution covers 9/9.
4. **Independent script** `review/work/verify.py`: all 26 Caesar shifts and Atbash of the string give nothing readable (e.g. -1 HKLVZLVKL, Atbash RONDZNDON), so a letter substitution is not indicated. My own expansion with a separate word table gives the same sentence.
5. **Is the reading plausible?** Five distinct letters in nine places, with the pattern I-L-M-W-A-M-W-L-M: a sentence that turns round on "and" (X loves Y and Y loves X) fits it exactly, and "I love my wife and my wife loves me" is grammatical, idiomatic English for 1910. It also fits a card addressed to a married woman. Initial-messages like this were a common sweetheart-postcard game in that period. I could not find another expansion that is equally coherent. Possible variants ("I like my wife ...", "I love my woman ...") would only change single words and give the same meaning.
6. **Honesty / credits.** The GPT solver's provisional "ILYMAMWLM" and its "I love you" idea are credited. The portal status was "Not solved", no attachment carries a solution, and I know of no published solution. The interpretive nature of the expansion is stated openly under "Uncertainties".

## Findings

1. **minor - the command checks the expansion but does not derive it.** `work/decode.py` hard-codes the
   word list `KEY` and only asserts that the initials match. For an initialism this cannot be otherwise.
   Also, the "stem" printout is not a real consistency check: it strips "s" for L only, and for M it lists two
   different words (`['me', 'my']`). Suggested fix: state in SOLUTION.md that the script verifies the
   initials rather than producing the words.
2. **minor - one sentence in SOLUTION.md overstates the case.** "reuses the same word for every repeated letter
   (... M = my/me ...)": M is expanded as "my" twice and "me" once, so these are two words, not one. This is
   harmless (both are natural), but the wording should say "the same word or a form of the same pronoun".
3. **minor - "sent ... presumably by her husband".** The card has no postage stamp or postal cancellation, and
   the purple "11 JUL 1910" is a plain date hand stamp. Whether the card went through the post, or who wrote
   it, cannot be shown. SOLUTION.md already marks the husband as an inference; the date should be described
   as a date stamp, not a postmark, if the report says more about it.

No blocker or major findings.

## What I could not verify

- Whether the writer meant exactly these words: an initialism has no key that proves them. I consider the
  proposed expansion the most likely one, but it is an interpretation, and it is disclosed as one.
- The identity of Mrs P. H. Ellis and of the writer (no sender name on the card; no search of 1910 London
  records was done).
- The real card. I worked only from the 1024x674 JPEG scan on the portal.
