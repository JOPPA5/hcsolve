# HCP 1094 (cpc_1912-03-0_AT_Schneegattern_AT_Schneegattern_): an Easter greeting from Johann in numbers

Human solver: Tomáš Pavuk

**Status: deciphered in full (all 20 number groups read, 20 letters); independent review 1 verdict ACCEPT, one correction (the umlaut of "wünscht").** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1094 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1094), part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Fanny Rauchenschwandner, with no transcription or solution attached. The portal file name dates the card to March 1912.

The picture side is a photographic Easter card (publisher R&K, number 4630/4): a young couple in front of a large broken egg, with a lamb and pussy-willow branches, and the printed greeting **"Fröhliche Ostern!"** ("Happy Easter!"). There is no handwriting on the picture side.

The address side is written in plain Latin cursive: **"An Wohlg. Fräul. Fanni Rauchenschwandner / beim Wallner in / Geretsek(?) Post / Schneegattern"** ("To the well-born Miss Fanni Rauchenschwandner, at Wallner's in Geretsek (?), post office Schneegattern"). Schneegattern is a village in the Kobernaußer Wald in Upper Austria. The card carries an Austrian 5-Heller Franz Joseph stamp cancelled SCHNEEGATTERN (date illegible). The cipher stands on the left half of the address side: three short columns of numbers separated by dots, written sideways (the card turned 90 degrees).

![Address side: three columns of numbers on the left, plain address on the right (source/address-large.jpg)](../source/address-large.jpg)

![Picture side with the printed greeting "Fröhliche Ostern!" (source/picture-large.jpg)](../source/picture-large.jpg)

Other marks on the card, none of them cipher: a large pencil "4" below the columns (a later dealer's or collector's mark), the HCPortal collection stamp on both sides, the printed stamp and the postmark.

## Method

The numbers were read manually from enlarged crops of the full-resolution address scan (the un-converted original from the portal, kept in work/hires/). The columns are read top to bottom with the card turned, starting with the column nearest the address divider and moving leftwards. Dots separate letters; a wider gap in the middle column separates two words.

The values form an obvious place-value pattern: units 1–9, tens 10–90 and hundreds 100–400. This is the classical "Greek numeral" style alphabet in which the letters are counted off in groups of nine: a–i are 1–9, k–s are 10–90, t–z are 100–700, with i and j sharing one value. Applied to the card it gives German at once; no other order of the columns gives language.

## Key

| a | b | c | d | e | f | g | h | i/j |
|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |

| k | l | m | n | o | p | q | r | s |
|---|---|---|---|---|---|---|---|---|
| 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 |

| t | u | v | w | x | y | z |
|---|---|---|---|---|---|---|
| 100 | 200 | 300 | 400 | 500 | 600 | 700 |

Only the values 1, 3, 4, 5, 8, 9, 40, 50, 80, 90, 100, 200 and 400 occur on the card. The values 500–700 (x, y, z) are the natural continuation of the scheme but are not attested. The umlaut is written as two dots above the number: ü = 200 with dots.

## Transcription and plaintext

| Column | Numbers | Letters |
|---|---|---|
| 1 (next to the divider) | 400. 200 (with umlaut dots). 40. 90. 3. 8. 100. | w ü n s c h t |
| 2 | 4. 9. 80. / 4. 5. 9. 40. | d i r / d e i n |
| 3 (leftmost) | 9. 50. 8. 1. 40. 40. | i o h a n n |

German: **"wünscht dir dein Johann"** (written Iohann, since i and j share the value 9). Together with the printed greeting on the other side it forms the sentence **"Fröhliche Ostern wünscht dir dein Johann."**

- English: "Your Johann wishes you a happy Easter."
- Slovak: "Veselú Veľkú noc ti želá tvoj Johann."

The plaintext can be reproduced from the repository root with `python3 -I ciphers/hcp-1094/work/decode.py`, which checks the SHA-256 hashes of the source images and prints `wünscht dir dein iohann`.

## Uncertainties

- The "1" in column 3 is a continental 1 with a lead-in stroke; the shape and the word "Iohann" agree on a.
- The values for x, y and z are inferred from the pattern, not seen on the card.
- The stamp is still attached; writing under it, which occurs on some other postcard series, cannot be checked from the scans. No writing shows at its edges and the picture side carries no handwriting, so no hidden message was found.
- The place name in the address ("Geretsek", possibly Geretseck) and the postmark date are not fully legible; neither affects the cipher.

## Review and what changed

An independent Claude Opus 5.5 reviewer reran the solver's command, rebuilt the key from scratch in its own script, re-read all three columns from its own 2x and 4x crops and checked the stamp corner and the picture side. Every number matched and every value is covered by the key. Verdict: **ACCEPT**, with three minor findings:

1. The ü of "wünscht" is written: two short strokes stand above the 200 group. The first version had said the umlaut was not marked and printed "wunscht". Fixed: the transcription now carries the mark and the script prints "wünscht".
2. The transcription line for column 1 should show that mark. Fixed.
3. The name rendered as "Iohann" is correct for the merged i/j value; explained above, no change.

The reading of the card did not change otherwise.

## Credits

Transcription, key identification and decipherment by Claude Opus 5.5 (Anthropic); independent review by a separate Claude Opus 5.5 agent. No earlier work on this card and no published solution were found.
