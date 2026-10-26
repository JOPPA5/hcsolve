# HCP 1463 (pc_hcp_144): a numeric love note from Walt to Ada, 1904

**Status: deciphered in full; independent review 1 verdict ACCEPT.** Report dated 2026-10-26.

## Origin and context

The cryptogram is record 1463 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1463), portal name pc_hcp_144, in the HCPortal cryptographic postcards collection (private collection). When it was acquired on 2026-10-26 the portal listed it as **Not solved**, category Substitution / Monoalphabetic, language Unknown, with no transcription or solution attached. The portal names the recipient as Miss Nicholls and dates the card 1904-11-12.

It is a British picture postcard; the picture side shows Dartford Heath and carries no cipher. The address side is addressed to Miss Ada Nicholls, 41 Welbeck Street, Cavendish Square, London W., and postmarked 10 AM, NO 12 04. At the top left the writer dated the message 11/xi/04 9.15 pm. The portal date is therefore the posting date; the message was written on Friday evening, 11 November 1904. The portal capture made at acquisition (source/metadata.md) misread the street as "14 Melleek Street" and the date line as "12/11/04, 9.35pm"; the readings above were corrected in review and are used here (the captured source file itself is left unchanged).

The message fills the left half of the address side: thirteen rows of numbers separated by dots, with hyphens between words, and one ordinary time "7.30 & 8" written in plain figures.

![Address side with the numeric message on the left (source/address-large.jpg)](../source/address-large.jpg)

## Method

The transcription is **manual** (work/transcription.txt); the portal supplied none. All numbers lie between 1 and 25, and the first row 13.25-4.5.1.18-1.4.1 reads MY DEAR ADA under the direct alphabet-position code A=1 … Z=26 (A1Z26), matching the addressee. The same key, without any change between rows, gives the whole message: 149 numeric letter positions, signature and final row of 11s included. The time "7.30 & 8" is ordinary text and is kept out of the letter count.

The transcription was checked number by number in review against enlarged strips of the scan, and decoded with an independently written script; the sequences agree.

## Key

Direct numeric substitution, the letter's position in the 26-letter alphabet:

| A | B | C | D | E | F | G | H | I | J | K | L | M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |

| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

Values occurring on the card: 1–9, 11–15, 18–23 and 25.

## Plaintext

Row by row as on the card (numbers as written, then the literal decoded letters; the last row is given in physical order, Ks on the left):

```text
13.25-4.5.1.18-1.4.1                        MY DEAR ADA
20.8.1.14.11.19-6.15.18-12.5.20.20.5.18     THANKS FOR LETTER
20.8.9.19-13.15.18.14.9.14.7                THIS MORNING
23.9.12.12-3.15.13.5-1.14.5                 WILL COME ANE
19.5.5-25.15.21-20.15.13.15.18.18.15.23     SEE YOU TOMORROW
14.9.7.8.20-4.5.1.18-23.9.12.12             NIGHT DEAR WILL
3.15.13.5-2.5.20.23.5.5.14                  COME BETWEEN
7.30&8-7.15.15.4.14.9.7.8.20                7.30 & 8 GOODNIGHT
4.5.1.18.5.19.20-9.20-23.9.12.12            DEAREST IT WILL
19.15.15.14-2.5-8.5.18.5                    SOON BE HERE
23.9.20.8-13.21.3.8-12.15.22.5              WITH MUCH LOVE
6.18.15.13-25.15.21.18-15.23.14             FROM YOUR OWN
11.11.11.11.11.11-23.1.12.20                KKKKKK WALT
```

The literal spelling ANE (1.14.5) is kept; AND would need a 4, which is not on the card.

Normalized English (punctuation editorial; AND for the literal ANE is an interpretation): **My dear Ada, thanks for letter this morning. Will come and see you tomorrow night, dear. Will come between 7.30 & 8. Goodnight, dearest, it will soon be here. With much love from your own Walt.** The row KKKKKK is left as written.

Slovak translation: **Moja drahá Ada, ďakujem za dnešný ranný list. Prídem ťa zajtra večer pozrieť, drahá. Prídem medzi 7.30 a 8. Dobrú noc, najdrahšia, už to bude čoskoro. S veľkou láskou tvoj Walt.** (KKKKKK left untranslated.)

Written on Friday 11 November, "tomorrow night between 7.30 & 8" refers to Saturday 12 November 1904, the day the card was posted in the morning.

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-1463/work/decode.py
```

The script checks the SHA-256 hashes of the source files, decodes every number of the manual transcription in work/transcription.txt, keeps the time group separately and checks the inverse key for each position. It does not read the image. In that file the signature row is listed above the row of 11s; the card has both in one row, Ks first (see above).

## Uncertainties

- ANE is literal; AND is an interpretation of a probable slip by the writer.
- KKKKKK (six 11s) is not interpreted; kisses is possible but not established by the key.
- Hard-to-read numbers, all resolved by the same values in solver's and reviewer's readings: the initial 13 (resembles 18 at small size), the 5 at the end of ANE, the row of 11s, and the second 18 of TOMORROW (20.15.13.15.18.18.15.23), which closely resembles 15; reading 15 would give TOMOROOW.
- Walt and Ada Nicholls are not identified.
- The address and date-line readings (41 Welbeck Street; 11/xi/04 9.15 pm) come from the scan and review, not from the portal capture, which misread them.
- The prior-solution check was limited to the portal attachments and an export of the AI Decipherment Register; earlier publication elsewhere cannot be excluded.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the stored check file), re-read all 149 numbers from its own crops before comparing, decoded them with its own script, and checked the context (addressee Ada, date line, postmark, Friday/Saturday timing). Its four findings were minor and are reflected here:

- The doubtful second 18 in TOMORROW is now listed among the uncertainties.
- The portal capture's date line and street were misread; the corrected readings 11/xi/04 9.15 pm and 41 Welbeck Street are used in this report, and 1904-11-12 is identified as the postmark date.
- The last row is shown in physical order (KKKKKK WALT); the working transcription lists WALT first, which does not affect decoding.
- The missing spaces in the solver's working text are not carried into this report.

No change to the plaintext resulted from the review. The closing steps (response to review, this report, the register entry) were prepared by Claude Opus 5.5 on the solver's behalf at the human's request; the decipherment itself was made by the solver, OpenAI GPT (GPT-6 Astra).

## Sources

- HC Portal record 1463 (pc_hcp_144), General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1463 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4450/conversions/pc_hcp_144_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4449/conversions/pc_hcp_144_pic-large.jpg (source/picture-large.jpg).
- AI Decipherment Register export, 2026-10-26: https://ai.hcportal.eu/register/?format=json (no matching entry; not a plaintext source).
