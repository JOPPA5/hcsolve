# HCP 1354 (pc_hcp_35): a sharp little question to W. Abbott, 5 March 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (68 of 68 cipher letters); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1354 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1354), portal name pc_hcp_35, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-03-05, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (a catalogue spelling of Abbott), with no transcription or solution attached.

The picture side is a coloured view from Frith's Series, with the faint caption "[Par]kstone From Constitution Hill". It carries no cipher. Parkstone lies in Dorset, close to Wimborne.

The address side is in plain writing: **Mr W. Abbott, Stokelake Farm, Chudleigh, Devon.** It has a green halfpenny Edward VII stamp and the postmark WIMBORNE, 10 PM, MR 5, 07. That agrees with the portal date and with the date written in clear on the card. 5 March 1907 was a Tuesday. The message is written sideways in the left half of the address side.

The card belongs to a correspondence with W. Abbott that this repository has met before: the cards HCP 1386–1407 are in the same cipher, and HCP 1398 has the same recipient farm and the same signature. The sender's name is not known; the cards are signed Loo. "Your girl" on HCP 1398 suggests a woman, which is why this report says "she", but that is not proved.

![Picture side: "[Par]kstone From Constitution Hill" (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned: Mr W. Abbott, Stokelake Farm, Chudleigh, Devon; WIMBORNE postmark, and the message sideways on the left (source/address-large.jpg)](../source/address-large.jpg)

![The message turned 90° counter-clockwise (work/reading_full.png)](../work/reading_full.png)

Other marks on the card, none of them cipher: the printed headings, the publisher's line of F. Frith & Co., the postmark, the plain address, the plain date, the HCPortal watermark on both sides, and a small circled sorting mark at the top left of the address side. With POST CARD upright that mark is a tall stem with a closed lower loop, so it is probably a 6. A rust-brown blot lies over the word for MONDAY.

## Method

The transcription is **manual**. The solver rotated the original full-size scan of the address side 90° counter-clockwise, cut 4× enlargements of each line, read the message sign by sign, and recorded it in work/transcription.json. No OCR was used and the portal supplied no transcription.

The cipher was tested as a Caesar shift because the sister cards use one. Of the 26 possible shifts only −1 gives English. The doubtful signs were settled by comparing shapes on this card. For example, the second word of line 3 was first taken as a repeat of the day name in line 5. The initial N and the long p show it is a different word, MONDAY rather than SUNDAY.

In review the reviewer rotated the scan independently, cut its own crops, typed its own transcription and decoded it with its own explicit table (review/work/decode_review.py). The plaintext and the letter count agree with the solver's. The only difference was one extra full stop, a dot discussed below.

## Key

Caesar shift: each plaintext letter is written as the **next** letter of the alphabet, so decipherment subtracts one. The date line is in clear.

```text
Cipher  ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain   ZABCDEFGHIJKLMNOPQRSTUVWXY
```

Twenty different cipher letters occur on this card and all fall under this one rule; the letters a, c, k, l, r and y do not occur in the ciphertext. Capitals and lower case are kept as the writer used them.

## Plaintext

Ciphertext as transcribed, line by line, with the literal decoding:

| Ciphertext | Plaintext |
|---|---|
| Tveefo. dibohf | SUDDEN. CHANGE |
| Jo. ifbejoh pg | IN. HEADING OF |
| mfuufs Npoebz | LETTER MONDAY |
| up. qptu dbse | TO. POST CARD |
| sfdfjwfe Tvoebz | RECEIVED SUNDAY |
| ? Gps XIZ ! Mpp. | ? FOR WHY ! LOO. |
| *in clear:* March 5th = 07 | March 5th 1907 |

Dots after words are separators, as on sister cards. The capitals of WHY are the writer's.

**English (the language of the plaintext):**

> Sudden change in heading of letter Monday to post card received Sunday? For WHY! Loo. March 5th 07.

**Slovak translation:**

> Náhla zmena v oslovení listu z pondelka oproti pohľadnici prijatej v nedeľu? Prečo! Loo. 5. marca 1907.

"Heading" most naturally means the salutation. Other cards in this correspondence vary theirs ("My own dearest boy" on HCP 1350, 1356 and 1357; "My own E. L." on HCP 1374 and 1376). She seems to be asking why his Monday letter opened differently from the card she received on Sunday. That is an interpretation; it is not stated on the card. Sunday 3 and Monday 4 March fit the Tuesday postmark.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1354/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the files in source/ and work/hires/, decodes work/transcription.json with the shift, and prints the six lines with the count of 68 letters. It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **HEADING.** Read from the signs, not guessed. The first sign is a dotted hooked minim of the same form as the i of `dibohf`; the fifth is a dotted descending j, like the j of `hjsm` on HCP 1398. READING is excluded because the writer's s is a different form, and LEADING because her m has two arches.
- **The second D of SUDDEN.** After the T come a thick minim with a thin rising tick, a solid black wedge with no visible eye, and one clear looped e. The wedge is taken as a filled e. It could instead be the second stroke of the v, which would leave one e (SUDEN, 67 letters). The word is not in doubt, only whether that letter was physically written. It is the one letter of the reading not cleanly seen on the scan.
- **POST.** The first sign of `qptu` is very like the capital G of `Gps`. It is taken as q because `gptu` gives no word.
- **MONDAY.** The blot lies over the e and the foot of the b, but both remain visible, and the word is clearly not `Tvoebz`.
- **LETTER and CARD.** The minims of `mfuufs` run together, though four can be counted. The third sign of `dbse` is a weak compact hump. Each is the only word that fits.
- **Punctuation.** The `?` stands at the left margin before `Gps`. It is attached here to the sentence before it, but it could belong with "For WHY".
- **Dot and line near XIZ.** A heavy round dot lies just below the end of `sfdfjwfe`, directly above the I of `XIZ`. It is either a separator or a dot on the I. A thin line runs from the X through the feet of the I and Z. It is either the Z's foot carried back or an underline, which would suit the emphasis. Neither changes a letter.
- **LOO.** The signature `Mpp` is read as on HCP 1398. That it is a pet name is conjecture, and the writer's identity and sex are not established.
- **Date.** The mark over the "=" is read as a raised "th" with a long bar. The bar runs under `Mpp` and could be a separate underline.
- **Language.** The portal says Unknown. English is established here by the decipherment.
- **Prior publication.** The portal shows Not solved and the AI Decipherment Register had no record on 2026-10-30. No wider search was made.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent from the solver, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, decoded its own independent transcription, confirmed that only shift −1 gives English, and checked every line on its own crops, the doubtful signs at 6× to 8×. It tried to break the reading on HEADING, the day names, the signature and the letter count, and none of these changed a word. It also confirmed the postmark, the weekday and the caption. Its four findings were all minor and are reflected here:

- **SUDDEN was less clean than first presented.** The first claim that no letter had been restored overclaimed. The filled sign and the 67-letter alternative are now disclosed.
- **An undisclosed dot and line near XIZ.** Both are now described.
- **A wrong statement about HEADING.** The first write-up said the card had no isolated lower-case i and called HEADING the weakest word. The card has such an i, and both dots support the reading, so HEADING is now given as read.
- **The sorting mark.** It was first given as 5; it is probably 6, and is not part of the message.

No decoded letter changed as a result of the review. Capture, transcription, decipherment, the response to review and this report were all done by Claude Opus 5.5; there was no earlier work on this number.

## Sources

- HC Portal record 1354, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1354 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4122/conversions/pc_hcp_35_pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/4122/pc_hcp_35_pic.JPG (work/hires/).
- Address side: https://api.hcportal.eu/media/4123/conversions/pc_hcp_35_adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/4123/pc_hcp_35_adr.JPG (work/hires/).
- Sister cards in this repository: ciphers/hcp-1386 to hcp-1407, in particular hcp-1398 for the signature; hcp-1350, 1356, 1357, 1374 and 1376 for salutations.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked by the orchestrator on 2026-10-30.
