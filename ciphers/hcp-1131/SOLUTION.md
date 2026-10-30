# HCP1131 — Pigpen postcard to Olive Ritter, Selden, Kansas (complete reading)

Portal: https://crypto.hcportal.eu/dashboard/cryptograms/1131
(`cpc_-04-19_USA_Hoxie, Kansas_USA_Selden, Kansas_`). Status on the portal:
Not solved; no transcription or solution attached. The transcription is the
solvers' own (work/transcription.txt), made from `source/address-large.jpg`.
No published plaintext was found or used.

## Cipher type and key

Pigpen variant (MASC) in which every letter is an outline of a square
(one of nine cell shapes of a 3×3 grid) and the **number of dots** (1, 2 or 3)
selects the block: A–I, J–R, S–Z. Same family as HCP1189/1190/1193.

| Outline strokes | Token | 1 dot | 2 dots | 3 dots |
|---|---|---|---|---|
| bottom/right | BR | A | J | S |
| bottom/left/right | B | B | K | T |
| bottom/left | BL | C | L | U |
| top/bottom/right | R | D | M | V |
| four sides | C | E | N | W |
| top/bottom/left | L | F | O | X |
| top/right | TR | G | P | Y |
| top/left/right | T | H | Q | Z |
| top/left | TL | I | R | — |

Letters attested: A C D E F G H I L M N O P R S T U W Y (19 of 25 cells);
every glyph on the card fits the key, none is left over.

## Plaintext (English, line breaks as on the card)

```text
YOU CAN NOT
WRITE SO I
CAN READ IT
I Wish I COULD
FLY HOME
DO YOU PLAY
ON THE ORGAN
I AM PRETTY
TIRED
```

Punctuated: “You can not write so I can read it. I wish I could fly home.
Do you play on the organ? I am pretty tired.”

Slovak: „Nevieš písať tak, aby som to vedel/a prečítať. Kiežby som mohol/mohla
odletieť domov. Hráš na organe? Som dosť unavený/á.“

Reading note: “You can not write so I can read it” most likely means the
recipient's own cipher writing was hard for the sender to read – a
complaint typical of postcards exchanged in a shared code.

## Reproduce

From the repository root:

```sh
python3 ciphers/hcp-1131/work/decode.py
```

It checks the SHA-256 of the files in `source/`, decodes the manual token
transcription with the key above and asserts an exact token roundtrip.
It does not OCR the scan; the pixel-to-token step is manual.

## Uncertainties and editorial decisions

1. **`W` + cursive `ish`.** After the cipher W (C3) the writer finished the
   word in ordinary handwriting (“ish”). It is shown in lower case.
2. **`COULD`.** The last cipher cell of line 4 looked like one merged box in
   the earlier pass. Enlarged (work/claude/ld.jpg) it is two glyphs written
   tight against each other: an open L-shape with two dots (BL2 = L) and a
   ⊐-shape with one heavy dot (R1 = D). Their bottom strokes do not join.
3. **`TIRED`.** The last word is written inside a curved line in the corner.
   Its I (TL1) stands *above* the line, and a small caret “^” sits between the
   T (B3) and the R (TL2) (work/claude/caret.jpg) — the writer forgot the I
   and inserted it. Literal order on the line is T-R-E-D with I inserted.
4. **Dot counts.** A few dots are heavy or blotted (M in HOME, the D after
   COUL). Each was read as the count that gives the only English word; no
   alternative count gives another word anywhere. Two further context
   decisions (added after review 1):
   - **E of PRETTY** (row 8, scan approx. x 400–430, y 590–628;
     review/work/pretty_e.png): the closed square holds **two** marks, a
     large blob touching the left stroke and a smaller dot to its right.
     Strictly counted that is C2 = N ("PRNTTY"). It is transcribed C1 = E,
     taking the blob as a blot or slip; PRETTY is the only word.
   - **Y of PRETTY, FLY, PLAY:** the dot groups are blotchy (in PRETTY one
     mark may be two merged dots), but all are clearly at least three, and
     TR3 = Y is the only reading.
5. **Date and sender.** Postmark HOXIE / KANS., APR 19, 1 PM, year “190?”
   (last digit illegible). The green one-cent Franklin stamp belongs to the
   1908 Washington–Franklin issue, so c. 1908–1909 is likely, not certain.
   Sender unsigned.
6. **Unencoded marks.** A free dot after IT at the end of row 3 (beside the
   dash) and a dot right of the vertical divider level with row 2 are full
   stops or stray marks, not cipher glyphs; they are not encoded.

## Why it is correct

- One fixed key, already established on sibling cards of the same collection,
  covers all 74 cipher glyphs with no unmapped glyph.
- The result is 25 ordinary English words in grammatical sentences; the word
  dividers (dashes) on the card fall exactly on word boundaries.
- The two previously open points (COULD, TIRED) are resolved from the
  pixels (separate glyphs; insertion caret), not filled in from context.

## History of this solution

Transcription and key transfer: GPT (earlier pass, 2026-10-25, left as
partial). Completion on 2026-10-29 by Claude Opus 5.5 acting as solver:
resolved the two open points from enlarged crops, independently collated
all eight rows against the scan, and updated the decoder.

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent) gave verdict **ACCEPT** with four
minor findings. I re-checked findings 1–3 on the reviewer's crops
(review/work/pretty.png, pretty_e.png, pretty_y.png, row3b.png).

1. **Dot discrepancy in the E of PRETTY — agreed, disclosed.** The crop
   clearly shows two marks inside the square. Added to uncertainty 4 and as
   a comment in work/transcription.txt. The token stays C1 (E): "PRNTTY" is
   not a word and every other letter of PRETTY is clean. No change of text.
2. **Blotchy Y dot groups — agreed, disclosed.** Note added under
   uncertainty 4; all are ≥3 dots, reading unchanged.
3. **Unencoded punctuation — agreed.** The free dot after IT is visible on
   row3b.png below the end-of-row dash. New uncertainty 6 and a comment in
   work/transcription.txt state that these marks are not glyphs.
4. **Reproduction is internal only — agreed, already disclosed.** No change;
   the pixel-to-token step remains manual and was collated twice (solver
   and reviewer independently).

Re-ran `python3 ciphers/hcp-1131/work/decode.py` after the edits (only
comment lines were added to the transcription): same nine lines of
plaintext, 74 glyphs, exact token roundtrip. The reading is unchanged.

Additional correction found while preparing the report: the plaintext has
**25** words, not 26 as SOLUTION.md (and review 1) stated; corrected under
"Why it is correct". Word count only; no letter changed.
