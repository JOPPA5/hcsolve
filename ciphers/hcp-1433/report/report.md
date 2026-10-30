# HCP 1433 (pc_hcp_114): an English Morse code postcard of 2 August 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (39 of 39 Morse letters); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1433 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1433), portal name pc_hcp_114, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection and Morse code, category Substitution, date 1907-08-02, language Unknown, location Europe, sender Unknown, recipient G. Groves, with no transcription or solution attached.

The picture side shows Northborough Church and carries no cipher. The address side is a British "POST CARD" with a green Edward VII halfpenny stamp. As scanned, the address half is upright and the message half is upside down: the card was turned round before the message was written. The address, to G. Groves in Banbury, is in plain cursive. The message half holds ordinary cursive (it opens "My A. G. Thank you for your letter of this a.m. also for the pretty P.C." and later speaks of someone being back safely). Between the cursive lines is **Morse code** in pen dots and dashes: five rows in the upper part of the message half and two rows at the bottom.

![Address side as scanned (source/address.jpg)](../source/address.jpg)

![Address side rotated 180 degrees so that the message reads upright (work/reading.jpg)](../work/reading.jpg)

## Method

The scan was rotated by 180 degrees and the Morse area enlarged 3-5x (work/main.png, work/last-main.png, work/bottom.png). Each letter is a group of dots and dashes closed by a long slanted stroke, which serves as the letter separator. No word spaces are marked. The marks were read by eye, mark by mark, and written down as a dot-dash transcript (work/transcription-full.txt). No OCR was used. The fifth main row crosses the red printed line "(Post Office Regulation.)". For it, a colour screen was used that separates dark pen ink from the red-brown print and the grey background (work/final-row-color-screen.png, work/final-row-mark-map.png).

The transcript is decoded with the standard International Morse alphabet by a short script. Every group is a valid Morse letter and no pen mark in the Morse area is left unassigned.

![Enlarged Morse rows of the main passage, upright (work/main.png)](../work/main.png)

![Colour screen of the fifth main row (work/final-row-color-screen.png)](../work/final-row-color-screen.png)

![The bottom Morse passage (work/bottom.png)](../work/bottom.png)

## Key

Standard **International Morse code**, letters only. Each letter is closed by a slanted stroke (`/`). The letters that occur are:

| Morse | Plain | Morse | Plain | Morse | Plain |
|---|---|---|---|---|---|
| .- | A | -.. | D | . | E |
| ..-. | F | .... | H | .. | I |
| .-.. | L | -- | M | -. | N |
| --- | O | .-. | R | ... | S |
| - | T | ..- | U | ...- | V |
| .-- | W | -.-- | Y | | |

## Transcript and plaintext

```text
row 1   ... / .... / .- / .-.. / .-..             SHALL
row 2   .. / ... / . / . / -.-- / --- / ..-       ISEEYOU
row 3   - / --- / -- / --- / .-. / .-. / ---      TOMORRO
row 4   .-- / . / ...- / .                        WEVE
row 5   .-.. / --- / ..- / .. / .                 LOUIE
bottom  ..-. / --- / -. / -.. / . / ... / -       FONDEST
bottom  .-.. / --- / ...- / .                     LOVE
```

Main passage: SHALLISEEYOUTOMORROWEVELOUIE. Bottom passage: FONDESTLOVE. 39 letters in all.

With word division and punctuation added (editorial):

**Shall I see you tomorrow eve, Louie? … Fondest love.**

English: **Shall I see you tomorrow evening, Louie? … Fondest love.** ("Eve" is the usual period short form of "evening".)

Slovak: **Uvidím ťa zajtra večer, Louie? … S najvrúcnejšou láskou.**

LOUIE is a name. The text does not show whether it addresses the recipient by a pet name or signs the Morse part. The card is addressed to G. Groves and the cursive opens "My A. G.". Both readings are left open.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1433/work/decode_full.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the files in source/ (work/source-sha256.json), decodes work/transcription-full.txt with the Morse table, and prints the seven rows, the count (39 letters) and the joined main and bottom passages. It does not read the image. The transcription step is manual and was confirmed independently in review.

## Uncertainties

- **Row 5, first letter (L).** A long separator stroke coming down from row 4 ends between `.-` and `..` of row 5. It is longer than the other row-4 separators. This writer sometimes lets one stroke separate letters in two rows (rows 1 and 2; FONDEST and LOVE). So the geometry alone would allow a split into A and I, giving AIOUIE. L is chosen because AIOUIE is not language.
- **Row 5, O.** The third dash of O sits on the red printed line "(Post Office Regulation.)". On the colour screen it is dark pen ink, like the two dots of U next to it, so the group is O, not M.
- **Row 5, a small blob on the separator after U** (about 12 px above the dot line). It is read as a pen hook on the stroke. If it were a dot, it would give either LOUSE (S instead of I) or LOFIE (F instead of U). Neither fits.
- **Row 1, H.** One dot of H is crossed by a cursive descender from the line above. The dot spacing requires four dots.
- **Row 3.** One dash of the second O is short, but it has the size and shape of the other dashes, not of a dot.
- The scan is only 1024x674 pixels, so dots are about 6-8 px across. No higher-resolution original was available.
- The people (G. Groves of Banbury, "A. G.", Louie) are not identified. The cursive text was used only as context and was not transcribed in full.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command and wrote an independent decoder with its own Morse table and its own transcript. It read every group mark by mark on its own 4-7x crops and on a pixel map separating pen ink from the red print. Its 39 letters are identical to the solver's. It found four minor issues, all about how the evidence was described:

- **Row-5 L.** The solver had said the long stroke has "the same length" as the other row-4 separators. It is in fact longer, and the writer shares separators between rows elsewhere. The argument now rests openly on language: AIOUIE is not English.
- **Blob after U.** LOFIE is now listed as a rejected alternative beside LOUSE.
- **LOUIE.** Left open as addressee or signature, as before.
- **Provisional coordinate file.** The earlier rough mark map (work/final-row-observations.json) is not relied on. The current transcript is authoritative.

No decoded letter changed as a result of the review.

## Credit

The portal capture (all three tabs, both scans, hashes), the 180-degree orientation, and the reading of the first four main rows and of the bottom passage were done by an earlier solver, OpenAI GPT (GPT-6 Astra), on 2026-10-26. It left the fifth main row unresolved. Claude Opus 5.5 re-checked all rows on 2026-10-29, read the fifth row as LOUIE, and wrote the full transcript and decoder. It also answered the review and prepared this report. The independent review was made by a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1433, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1433 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4360/conversions/pc_hcp_114_adr-large.jpg (source/address.jpg).
- Picture side: https://api.hcportal.eu/media/4359/conversions/pc_hcp_114_pic-large.jpg (source/picture.jpg).
- No published solution of this card was found. The AI Decipherment Register (https://ai.hcportal.eu/register/) had no record for it on 2026-10-29.
