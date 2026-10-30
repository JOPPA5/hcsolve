# HCP 1828 (pc_hcp_509): a collector's thank-you from "Ade", January 1906

Human solver: Tomáš Pavuk

**Status: deciphered in full (98 of 98 cipher signs); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1828 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1828), portal name pc_hcp_509, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1906-01-12, language Unknown, location Europe, sender Unknown, recipient G. L. Serry, with no transcription or solution attached.

It is a British picture postcard: Raphael Tuck & Sons "Oilette", series "Quaint Corners", printed number read as 6404, showing "Ye Dolphin Inn", Derby, a timber-framed building. The message and the address share the back of the card.

The address is in plain handwriting: **Mr G. L. Serry, Queens Road, Haywards Heath, Sussex.** "Serry" is the portal's reading. The first letter has a looped top and differs from the S of "Sussex", so "Terry" or "Jerry" cannot be excluded. The card has a halfpenny Edward VII stamp and a postmark reading FARN… (the rest is not legible), 11.15 AM, JA 12, 06. A handwritten note reads "Jan 11th", with a heavy diagonal stroke through it. So the card was probably written the day before it was postmarked.

The cipher text is written in ten rows of brush-drawn signs that look like pseudo-Chinese characters. It stands **upside-down relative to the printed card**.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![Address side turned 180 degrees, the direction in which the message reads (work/address-turned.jpg)](../work/address-turned.jpg)

Other marks on the card, none of them cipher: the ink spatters near rows R6 and R7, the handwritten date, the address, the printed card text, the stamp and the postmark. A long looped pen flourish runs above R1 in plain pen style. It lies next to ADE when the card is turned, so it may be a sign-off flourish, but that is a guess. The grey wheel across the card is a watermark of the scan collection.

## Method

The portal supplied no transcription, so the solver transcribed the card by hand from enlarged crops of the original scan, at 3x to 8x. Rows are numbered R1 to R10 from the top of the scan as delivered. No sister card in the repository uses these signs, so the key was recovered from this card alone.

1. A first pass grouped the signs by shape. It merged some look-alike signs and took a dash group as separate signs.
2. Simulated annealing with an English quadgram model was run on the sign sequence (`work/sa.py`). The forward direction gave nonsense. The reversed direction gave clear English: THANKS, WHEN, CANT GET ANY.
3. The English exposed the wrong merges, such as "ANOTHING" for ANYTHING. The solver then compared the signs on the pixels and split them. Three-bar signs divide by the stem below the bottom bar (D against T), and hourglass signs by the eye (R against I). The dash-crescent-dash group is one sign, V, which gives LOVE.

The final transcription has 98 signs of 21 kinds. Every row ends on a word boundary, which was not imposed.

The direction is explained by the card itself. Turned 180 degrees, the message reads as ordinary left-justified text, left to right, top to bottom, with WITH LOVE / FROM / ADE as short closing rows. In the scan as delivered, that means last row first, each row right to left.

The reviewer cut its own crops, read all 98 signs independently in its own labels, and ran a blind annealing from those labels. Its language model excluded this card. Results of the four possible reading orders:

| Reading order | Best score | Result |
|---|---|---|
| Turned 180 degrees | -973.3 | exactly the claimed text |
| Rows in place, each right to left | -975.5 | same key and letters, rows out of order |
| Scan order | -1067.1 | nonsense |
| Rows reversed, left to right | -1076.9 | nonsense |

Scores settle the direction within rows. Sense settles the row order.

## Key

Monoalphabetic substitution with one invented sign per letter and no homophones or nulls. Signs are described as they appear in the scan, unrotated.

| Sign | Plain | Sign | Plain |
|---|---|---|---|
| eight-rayed star | A | prongs above an arc, tail below | L |
| cross, one bar | B | long diagonal with loops | M |
| two bars, stem runs past both ends | C | three-by-three lattice | N |
| three bars, stem clearly below the bottom bar | D | crescents above and below, one bar | O |
| left arc `(` | E | wide eye with pupil, bar or filled centre | R |
| right arc `)` | F | square with diagonals | S |
| low arc opening upward | G | three bars, stem stops at the bottom bar | T |
| arc opening downward | H | wave, three dashes, mirrored wave (one sign) | U |
| two strokes crossing, at most a slim gap | I | three dashes, crescent sign, three dashes (one sign) | V |
| top bar on two legs | K | two crescent signs joined by a bar | W |
| | | nine dots | Y |

J, P, Q, X and Z do not occur.

## Plaintext

Each line is one row of the card, in reading order. The card has no word division; the division here is editorial.

```text
R10  THANKS FOR
R9   CARD A BEAUTY
R8   SEND ANYTHING
R7   IN THE CASTLE OR
R6   RUIN LINE WHEN
R5   YOU CANT GET ANY
R4   MORE ACTRESSES
R3   WITH LOVE
R2   FROM
R1   ADE
```

**English, punctuated:** Thanks for card, a beauty. Send anything in the castle or ruin line when you can't get any more actresses. With love from Ade.

**Slovak translation:** Ďakujem za pohľadnicu, je krásna. Pošli čokoľvek s hradmi alebo zrúcaninami, keď už nezoženieš ďalšie herečky. S láskou, Ade.

The sense appears to be an exchange between picture-postcard collectors: views of castles or ruins are welcome once no more actress cards can be had. That is an interpretation of the plain words. It is compatible with a card showing an old inn.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1828/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the four scans, decodes `work/transcription.txt` with `work/key.json`, checks that the key is one-to-one and that the word division matches the letters, and prints the ten rows and the line `98 signs, 21 distinct; none unread`. It does not read the image: the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **Hapax signs.** B, K and V each occur once, so they rest on one word each: BEAUTY, THANKS and LOVE. Each of these words is fixed by its other letters and the sense, and the reviewer's blind climb fixed these signs by itself.
- **R against I.** Most R signs show a clear eye. In R2, R4 (MORE), R7 and R9 the belly is heavily inked or filled, with no separate pupil, so those signs differ from I by a swollen belly only, and that reading leans on the words as well as the pixels. In R10 (FOR) the eye lies under the printed "P" of "Printed in England"; grey values confirm that the band there has the density of the ink strokes, not of the printing.
- **D against T.** Only the stem below the bottom bar separates them. All 12 three-bar signs were compared side by side, and the feature separates them cleanly.
- **One segmentation decision.** Reading the dash-crescent-dash group as three signs gives no word, whereas one sign gives LOVE. The U sign has the same dash pattern, and the group is written tightly in R3.
- **Touching signs.** In R8 the G touches the N lattice. Both are complete.
- **Word division and punctuation** are editorial. CANT has no apostrophe sign.
- **Names and places.** ADE is the literal reading and may be a short form of a name; the sender is not otherwise identified. The surname of the addressee is uncertain, as noted above. The postmark gives only FARN…, so the place of posting is not established. The Tuck number 6404 is read from small print.
- **Row order** is settled by sense and by the layout, not by the score alone (see the table above).
- **Published solutions.** The portal shows none, and the AI Decipherment Register had no record on 2026-10-30. No dedicated web search is recorded for this card, so a solution published elsewhere cannot be excluded.

## Review

The review was carried out by a separate Claude Opus 5.5 session, so it is independent of the solver's session but not from a different provider. The verdict was **ACCEPT**. The reviewer could not refute the reading: its own transcription maps one-to-one onto the solver's, and its blind climb recovered the same 98 letters. It found no sign outside the transcribed rows.

It made five minor findings. None changes a letter, and all were addressed in the wording of the solution:

1. The claim that rows end at the same right edge was limited to R4–R10, as R3 ends shorter.
2. The claim that each visible feature separates the letters was too strong for R against I. The filled R signs are now named, R4 among them.
3. The pen flourish above R1 was added to the list of non-sign marks, and the note was corrected to "Jan 11th".
4. The surname is now marked as the portal's reading, with the caution about Terry or Jerry.
5. The context in this report (card series, street, postmark) was added, with the postmark given only as far as it can be read.

The reviewer also noted that the solver's early scores came from a sign list that was not preserved, so those scores are not repeated here. The table above gives the reviewer's reproducible figures.
