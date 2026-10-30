# HCP 1386 (pc_hcp_67): an English Caesar sweetheart postcard, 26 November 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (62 of 62 enciphered letters); two abbreviation groups kept literal; one word of the closing quotation read literally as VIRED, probably meant as TIRED. Independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30 (UTC).

## Origin and context

The cryptogram is record 1386 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1386), portal name pc_hcp_67, part of the HCPortal collection of cryptographic postcards (private collection). When captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-11-26, language Unknown, location Europe, sender Unknown, recipient "W. Abboú", with no transcription or solution attached.

The picture side is a printed Frith's Series view, "Princess Gardens, Torquay", with no writing. The address side carries a green halfpenny Edward VII stamp cancelled **WIMBORNE / NO 26 / 07** and is addressed in plain writing to **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon** (the portal's "Abboú" is a misreading of Abbott). 26 November 1907 was a Tuesday, which agrees with the plain heading of the message, "C. H. Tuesday" (the first initial may be G).

The message is written on the left half of the address side, sideways (turn the scan 270° to read it). It belongs to a group of Caesar-shifted English cards between one couple in 1907–08 (HC Portal 1386–1407; several are deciphered in this repository, e.g. 1387, 1390, 1397, 1398, 1403), all sent to W. Abbott at Stokelake Farm and using the same key and the same formulae ("My own … boy", "from your own … girl").

![Picture side (source/picture.jpg)](../source/picture.jpg)

![Address side as scanned: WIMBORNE postmark, address to Mr W. Abbott, Stokelake Farm, Chudleigh, and the cipher message below (source/address.jpg)](../source/address.jpg)

![The message turned upright (work/reading.jpg)](../work/reading.jpg)

## Method

The transcription is manual. An earlier OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol, 2026-10-26) downloaded the card, identified the shift and read 54 letters, leaving the first-line BOY, the abbreviation groups and the closing quotation open. Claude Opus 5.5 (2026-10-29) re-read every line from 3–5× enlargements (work/crops/), completed the transcription and wrote a new decoder (work/v2/decode.py, work/v2/transcription.json).

The key was found from whole words: subtracting one letter turns `uibolt` into THANKS, `mfuufs` into LETTER, `gspn zpvs` into FROM YOUR and `Hjsm` into GIRL. Once fixed, the same shift was applied to every token on the card.

In review, a separate Claude Opus 5.5 agent rotated the scan itself, made its own line crops, transcribed the card independently and decoded it with its own script; its reading agreed letter for letter.

## Key

Caesar shift: each plaintext letter is written as the **next** letter of the alphabet. Decrypt by moving back one (A→Z).

| Cipher | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z |
|---|---|
| Plain | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y |

The heading ("C. H. Tuesday") and the address are plain writing. The groups **E. L.** (twice) and **N. & L.** are abbreviations and are kept literal; shifted they would give D. K. and M. & K., which explain nothing either.

## Plaintext

| Ciphertext (as written) | Literal decode |
|---|---|
| Nz. Pxo. E. L. Cpz. | MY. OWN. [E. L.] BOY. |
| uibolt-wfsz. | THANKS-VERY. |
| nvdi gps. mfuufs | MUCH FOR. LETTER |
| Up—Ebz. Nz. | TO—DAY. MY. |
| N. & L. gspn. zpvs. | [N. & L.] FROM. YOUR. |
| Pxo. E. L. Hjsm | OWN. [E. L.] GIRL |
| "wfsz. wjsfe." | "VERY. VIRED." |

62 enciphered letters, all decoded by the one key; 6 abbreviation letters kept literal.

English: **My own E. L. boy, thanks very much for letter to-day. My N. & L. from your own E. L. girl. "Very vired" (probably "very tired").**

Slovak: **Môj vlastný E. L. chlapec, veľmi pekne ďakujem za dnešný list. Moje N. & L. od tvojho vlastného E. L. dievčaťa. „Veľmi vired" (pravdepodobne „veľmi unavená").**

Notes on the reading:

- The writer separates nearly every word with a dot; the dots are not significant. "thanks-very much" is joined with a hyphen on the card.
- "My own … boy" and "from your own … girl" are the couple's regular opening and closing, as on the sister cards.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1386/work/v2/decode.py
```

The script uses only the standard library. It checks the SHA-256 hashes of the files in source/, decodes every token of work/v2/transcription.json with the −1 shift, checks the inverse round trip, and prints the plaintext above with the letter counts. It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **The last word.** The quoted closing reads `wfsz. wjsfe.` The first sign of the second word is built like this writer's w (a tall stroke closing into a loop, identical to the w of `wfsz` just before it), not like his u (tall stroke with an arch, as in `uibolt`). The literal decode is therefore **VIRED**, not an English word. The only one-letter change giving English is `ujsfe` = **TIRED**, which suits "very tired"; it is reported as the probable intended word, not as a certain reading. An earlier reading WISE (`wjtf`) does not fit the five letters on the card.
- **E. L. and N. & L.** are left unexpanded. Sister card HCP 1387 has a parallel slot ("My own D.g boy … your own D.g girl"), so the slot holds a term of endearment, but nothing on the cards proves an expansion such as "ever loving". Whether these letters are themselves shifted is undecided. The middle sign of N. & L. is an ampersand-like form; the same shorthand occurs on HCP 1403.
- The first heading initial may be C or G (HCP 1397 prefers G. H.); the heading is not enciphered.
- The sender's identity is not established beyond the signature "girl"; the postmark shows the card was posted at Wimborne (Dorset) to Chudleigh (Devon).

## Review summary

Reviewer: Claude Opus 5.5 (a separate agent), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), rotated and cropped the scan itself, transcribed every line independently and decoded it with its own script; the result matched in all 62 enciphered letters. It checked BOY, N. & L., the second E. L. and the final word on 4–5× crops, confirmed that VIRED is the literal reading and TIRED a conjecture, and confirmed that 26 November 1907 was a Tuesday. Its four minor findings and what changed:

1. **VIRED / TIRED.** Kept as read, TIRED only as probable; this report follows that wording.
2. **E. L. / N. & L.** Kept literal; the parallel D.g slot on HCP 1387 is now mentioned.
3. **Farm name.** Previously "uncertain"; re-checked on the scan and now given as Stokelake Farm, as on the sister cards.
4. **Weekday.** The Tuesday check is now stated.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1386, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1386 (source/metadata.md, SOURCES.md).
- Picture and address sides: source/picture.jpg, source/address.jpg (URLs in SOURCES.md).
- Sister cards of the same couple in this repository: ciphers/hcp-1387, 1390, 1397, 1398, 1403.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no record for this card.
