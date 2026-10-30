# HCP 1358 (pc_hcp_39): an English Caesar sweetheart postcard on a hymn card, March 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (74 of 74 enciphered letters); two one-letter writer's slips kept literal and disclosed. Independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30 (UTC).

## Origin and context

The cryptogram is record 1358 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1358), portal name pc_hcp_39, part of the HCPortal collection of cryptographic postcards. When captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-03-18, language Unknown, location Europe, sender Unknown, recipient "W. Abboú", with no transcription or solution attached. No published solution of this card turned up in the portal or in this repository; no separate web search for one was made.

The picture side is a Raphael Tuck "Illustrated Hymns" card, Series 5534. It shows a church with a spire beside a river and prints the verse beginning "We love the place, O God", credited on the card to W. Bullock and Sir H. W. Baker. There is no handwriting on that side.

The address side has a green halfpenny Edward VII stamp, cancelled **WIMBORNE, 10 PM, MR 1?**, where the second digit of the day is broken and the year cannot be seen. It is addressed in plain writing to **Mr W. Abbott, Stokelake Farm, Chudleigh, Devon**. The portal's "Abboú" is a misreading of Abbott.

The card belongs to the group of Caesar-shifted English cards between one couple in 1907–08, sent to W. Abbott at Stokelake Farm, several of them deciphered in this repository (for example HCP 1386, 1397 and 1398). The writer signs "Girl" and uses the same formulae and the same key.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned: stamp, postmark, address and the message written sideways (source/address-large.jpg)](../source/address-large.jpg)

![The message turned 90 degrees counter-clockwise (work/crops/all_ccw.png)](../work/crops/all_ccw.png)

## Method

The transcription is manual, with no OCR. Claude Opus 5.5, as solver, turned the un-converted original scan of the address side 90° counter-clockwise and read all six rows from 3–6× enlargements (work/crops/). There was no earlier work on this number. Doubtful signs were compared with the same writer's signs on this card and on the accepted sister card HCP 1386.

The key was tried from the sister cards and then tested on this card alone. Subtracting one letter turns `Efbsftu` into DEAREST, `Tpnfuijoh` into SOMETHING and `Hjsm` into GIRL, and the same shift reads every row. The decoder work/decode.py checks the SHA-256 of the image files, decodes the transcription and checks the round trip:

```text
python3 -I ciphers/hcp-1358/work/decode.py
```

In review, a separate Claude Opus 5.5 agent cropped every row itself, typed its own transcription and decoded it with its own code. All 74 letters and the word divisions agreed with the solver's. Across all 26 shifts, shift 1 puts 63 letters into recognised words and the next best shift puts 2; the other 11 letters under shift 1 are the two words carrying the slips.

## Key

Caesar shift: each plaintext letter is written as the **next** letter of the alphabet. Decrypt by moving back one (A→Z).

| Cipher | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z |
|---|---|
| Plain | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y |

The address and the date are in plain writing. The dots between words follow the manuscript and are not significant.

## Plaintext

| Ciphertext (as written) | Literal decode |
|---|---|
| Nz. Pxo. Efbsftu Cpz. | MY. OWN. DEAREST BOY. |
| uijt jt Tpnfuijoh ofx. | THIS IS SOMETHING NEW. |
| boe. pof. pg. oz. | AND. ONE. OF. NY. [MY] |
| gpwpvsjuf. Iznot | FOVOURITE. [FAVOURITE] HYMNS |
| Mpwf. Gspn. Zpvst. | LOVE. FROM. YOURS. |
| Hjsm. | GIRL. |

74 enciphered letters, all decoded by the one key. Row lengths are 15, 18, 10, 14, 13 and 4 letters.

English: **My own dearest boy, this is something new and one of my favourite hymns. Love from yours, Girl.**

Slovak: **Môj vlastný najdrahší chlapec, toto je niečo nové a jedna z mojich obľúbených piesní. S láskou tvoje dievča.**

In plain writing at the foot, beside `Hjsm`: "March 8th" (or 18th; see below), then a year that could not be read.

## Uncertainties

- **`oz` = NY, not MY.** The first sign is a closed hollow loop, the same form as the o of `Pxo`, not this writer's n. MY is plainly intended (compare `Nz` at the start). It is treated as a slip and the literal decode is kept.
- **`gpwpvsjuf` = FOVOURITE.** The second sign has a bowl with a stem above and below the line, the writer's p; the b of `boe` and `Efbsftu` has an ascender only. FAVOURITE is intended. Also a slip, kept literal.
- **Signs settled by context.** At least three signs are decided by the word, not by form alone: the final sign of `Tpnfuijoh` and the first sign of `uijt` (h and u are close in this hand), and the third sign of `Iznot`, which fits n only on the word. The dots over the i and j of `uijt` support that word.
- **Other difficult signs.** Row 1 descenders cross `Tpnfuijoh`, but all nine signs can be separated. In `Zpvst` the t has a detached bar and is followed by a stop. In `Hjsm` the long stroke is taken as j, not as part of the date.
- **The day.** The hand alone reads 8th: the stroke before the 8 joins it as a lead-in, and no separate 1 is visible. The postmark shows MR, a 1 and a broken digit, and the portal gives the 18th. So 18th is possible, but neither the card nor the postmark confirms it.
- **The year.** Year not read; 1907 comes from the portal. The strokes after the date overlap the printing and the j of `Hjsm`, and the postmark year falls off as a bare arc.
- **Source search.** The portal attaches no solution, but no web search was run, so a printed solution elsewhere cannot be ruled out.

Context only: HCP 1357, postmarked MR 22 07 on the same Tuck series, opens the same way and says "this will make the pair for album", which fits "something new" here. That card had not been reviewed when this report was written.

## Review and what changed

Review 1, by a separate Claude Opus 5.5 agent, tried to refute the reading on the pixels of all six rows, and returned **ACCEPT** with four minor findings. No decoded letter changed.

- The claim of correctness overstated how independent the letters are. It now names the three signs settled by context.
- The date wording was tightened. The hand alone reads 8th, and the "19[07]" in the transcription was replaced by "year not read, 1907 from portal".
- One citation in the notes on the `b` was corrected (`boe` is on row 3).
- The HCP 1357 remark was added, marked as context only.

The reviewer could not verify the day or the year from the card, the portal's reason for its date, or whether a solution exists outside the portal. The hymn attribution rests on the printed credit on the card.

## Credits

Capture, transcription and decipherment by Claude Opus 5.5, with independent review by a separate Claude Opus 5.5 agent. The hand comparison and the hypothesis for the key came from accepted sister cards in this repository, on which earlier solvers worked.
