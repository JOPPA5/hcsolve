# HCP 1828 / pc_hcp_509 — Ade to Mr G. L. Serry (surname as read by the portal), Haywards Heath, January 1906

**Status: complete reading, reviewed (review 1: ACCEPT).** All 98 signs are read from the scan. There are no restorations.

Solved by Claude Opus 5.5 (claude-opus-5-5), 2026-10-30. There is no earlier work on this number. The portal shows "Not solved" and attaches no transcription or solution. The orchestrator's AI-register check found no record, and no published solution turned up in this repo or on the portal. No dedicated web search is recorded for this card. The transcription is my own, as the portal has none.

## Cipher type and key

Monoalphabetic substitution with 21 invented, brush-drawn pseudo-Chinese signs, one sign per letter. There are no homophones or nulls. The message is written **upside-down relative to the printed card**: turn the card 180 degrees and it reads normally. As the scan stands, that means last row first, each row right to left.

Signs are described as they appear in the scan, unrotated.

| Token | Sign | Letter |
|---|---|---|
| star | eight-rayed star | A |
| bar1 | cross, one bar | B |
| bar2 | two bars, stem runs past both ends | C |
| bar3long | three bars, stem clearly below the bottom bar | D |
| lparen | left arc `(` | E |
| rparen | right arc `)` | F |
| cup | low arc opening upward | G |
| cap | arc opening downward | H |
| cross | two strokes crossing, at most a slim gap, no pupil | I |
| legs | top bar on two legs | K |
| horned | prongs above an arc, tail below | L |
| spectacles | long diagonal with loops | M |
| grid | three-by-three lattice | N |
| crescent | crescents above and below, one bar | O |
| eye | wide eye with pupil, bar or filled centre | R |
| box | square with diagonals | S |
| bar3short | three bars, stem stops at the bottom bar | T |
| wave | wave, three dashes, mirrored wave (one sign) | U |
| dashcrescent | three dashes, crescent sign, three dashes (one sign) | V |
| hh | two crescent signs joined by a bar | W |
| dots | nine dots | Y |

J, P, Q, X and Z do not occur.

## Plaintext

Rows in reading order; every card row ends on a word boundary.

```
THANKS FOR
CARD A BEAUTY
SEND ANYTHING
IN THE CASTLE OR
RUIN LINE WHEN
YOU CANT GET ANY
MORE ACTRESSES
WITH LOVE
FROM
ADE
```

**English (punctuated):** Thanks for card, a beauty. Send anything in the castle or ruin line when you can't get any more actresses. With love from Ade.

**Slovak:** Ďakujem za pohľadnicu, je krásna. Pošli čokoľvek s hradmi alebo zrúcaninami, keď už nezoženieš ďalšie herečky. S láskou, Ade.

The sense is an exchange between picture-postcard collectors: views of castles or ruins are welcome once no more actress cards can be had. That is my interpretation of the plain words.

## Command

Run from the repo root. It checks the source hashes, decodes, and asserts that the word division matches the letters.

```bash
python3 -I ciphers/hcp-1828/work/decode.py
```

Files: `work/transcription.txt`, `work/key.json`.

## Context

Picture side: Raphael Tuck & Sons "Oilette" postcard, series "Quaint Corners", printed number read as 6404, caption "Ye Dolphin Inn", Derby. Address side, in plain handwriting: Mr G. L. Serry (portal's reading), Queens Road, Haywards Heath, Sussex. Handwritten note: "Jan 11th". Halfpenny Edward VII stamp, postmark FARN… (rest not legible), 11.15 AM, JA 12, 06. Portal date 1906-01-12.

## Uncertainties

1. **Hapax signs.** B (bar1), K (legs) and V (dashcrescent) each occur once, so they rest on one word: BEAUTY, THANKS, LOVE. All three words are fully fixed by their other letters and the sense.
2. **Sign pairs that differ by small features.**
   - R versus I: R has a wide eye with a pupil, bar or filled centre, I has two crossing strokes with at most a slim gap. In R10 (FOR) the eye's centre band lies under the printed "P" of "Printed in England", but it is visible at 8x. In R2, R4 (MORE), R7 and R9 the belly is heavily inked or filled, with no separate pupil. There the sign differs from I by its swollen belly only, and the choice leans on the words as well as the pixels.
   - D versus T: only the stem below the bottom bar separates them. All 12 three-bar signs were compared side by side. R1, R8 and R9 have the clear extension, and R5 (GET) has a long top stem but no extension below, so it is T.
3. **Composite signs.** Dashes appear only in the two composites. Reading dashcrescent as three separate signs gives no word, whereas one sign gives LOVE. This is the one segmentation decision the language forced.
4. **Touching sign.** In R8 the G (cup) touches the N grid. Both are complete.
5. **Word division and punctuation** are mine; the card has none. CANT has no apostrophe sign.
6. **Sender and recipient names.**
   - ADE is the literal reading, and it may be a short form of a name.
   - "Serry" is the portal's reading of the handwritten address. The first letter has a looped top and differs from the S of "Sussex", so "Terry" or "Jerry" cannot be excluded on this hand. I cannot decide it.
   - The sender's place is not known. The postmark reads FARN… (rest not legible), 11.15 AM, JA 12, 06, which gives only the office of posting, as far as it can be read.
7. **Marks that are not signs.** The ink spatters in R6 and R7, the handwritten "Jan 11th" with a heavy diagonal stroke through it, and the printed card text. A long looped pen flourish runs above R1 from over the royal arms to about x≈340 of the 1014-wide scan. It is in plain pen style, not one of the brush signs, and it lies next to ADE when the card is turned, so it may be a sign-off flourish, but that is a guess. The grey wheel is a watermark of the scan collection.

## Why I believe it is correct

- The key was found by annealing with an English quadgram model. Only the reversed direction gave English (`work/sa.py`, best score -1017.6 against -1081.1 forward, on an early, coarser sign list). The final key came from reading the words and then splitting the sign classes on the pixels.
- Those splits were checked against pixels independently of the language: D/T by the stem and I/R by the pupil. D/T separates cleanly on all 12 three-bar signs. I/R is less clean: the filled R signs (R2, R4, R7, R9) separate by a swollen belly, and that reading leans on the words as well. All 12 hourglass signs agree with the reading.
- The result is one-to-one, with no leftover signs and 98 of 98 read.
- All ten rows end on a word boundary, which was not imposed. The short top rows are the sign-off, WITH LOVE / FROM / ADE.
- Rows R4 to R10 end near the same right edge of the scan (x≈508–520 of 1014) and start at varying places on the left; R3 ends a little short, at x≈475. That is what a left-justified text looks like when the card is turned 180 degrees.
- The scores above came from an early sign list that was not preserved, so they are not reproducible. The reviewer's blind climb on the final signs gives the same conclusion with different numbers: -973.3 turned 180 degrees, -1076.9 for rows reversed left to right.

## Response to review 1

Verdict ACCEPT; five minor findings. None changes a letter, and `work/transcription.txt` and `work/key.json` are unchanged.

1. **Layout claim (fixed).** The argument now says R4 to R10 and gives R3's shorter end, x≈475. On `source/address-large.jpg` R3 does stop short of the others.
2. **R versus I wording (fixed).** Uncertainty 2 and the "why correct" section now name R4 and admit that the filled R signs lean on the words as well as on the pixels. The key table's `eye` row already allowed a filled centre.
3. **Unlisted mark (fixed).** Uncertainty 7 now lists the flourish and gives the note as "Jan 11th" with its diagonal stroke.
4. **Surname (fixed).** The title marks the surname as the portal's reading, and Uncertainty 6 gives the Terry/Jerry caution. On my 5x crop of `work/hires/pc_hcp_509_adr.JPG` the first letter has a looped top, and I cannot decide it either.
5. **Missing context (fixed).** A Context section was added. On my own 5x crop the postmark shows FARN, then something not legible, so I give no town. I read the Tuck card number as 6404 from the printed left edge; the reviewer did not state it.

The reviewer also could not reproduce the solver's scores, as they came from an older sign list. This is now stated in "Why I believe it is correct". The reviewer ran no web search for a published solution, and none is recorded on the solver's side, so that remains open.

Re-run after these edits: `python3 -I ciphers/hcp-1828/work/decode.py` passes the hash checks, prints the same 98 signs, none unread, and no unused key entries.
