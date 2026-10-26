# HCP 1442 (pc_hcp_123): a dotted Pigpen postcard from Nancy to Ray E. Bartley

**Status: deciphered in full; independent review 1 verdict ACCEPT.** Report dated 2026-10-26.

## Origin and context

The cryptogram is record 1442 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1442), part of the HCPortal cryptographic postcards collection (private collection), portal name pc_hcp_123. When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard HCPortal collection and Pigpen, category Substitution / Monoalphabetic, date 1907-12-16, language Unknown, location North America, sender Unknown, recipient Ray Bartley, with no transcription or solution attached.

It is an American postcard with a one-cent Franklin stamp. The picture side is an embossed flower with no cipher (only a small cursive mark at the lower left, not Pigpen). On the address side the card is addressed in plain writing to **Ray E. Bartley, Rutland, Iowa**, and the cancel reads RUTLA[ND] DEC 16 … IOWA, with no legible year: the card was local mail within Rutland. The message is in two parts:

- a **main passage** of four lines of Pigpen along the left edge, read with the card turned 90° clockwise;
- a **centre passage**: plain cursive "Dec. 16-07 / Received your / card Sat morn[ing] / this is", continued in three lines of Pigpen, read with the card turned 90° counter-clockwise.

The year 1907 comes from the handwritten "Dec. 16-07" and the portal. 16 December 1907 was a **Monday**, which matches the heading of the main passage.

![Address side: the main Pigpen passage at the left, the centre passage below the cursive lines (source/address.jpg)](../source/address.jpg)

## Method

The cipher consists of 46 Pigpen outlines (29 in the main passage, 17 in the centre), each with one, two or three dots inside, separated by commas, a hyphen and full stops. The transcription is **manual**: each sign was recorded as the sides of the cell that are drawn plus its dot count in work/transcription.json, from rotated, enlarged crops. The portal supplied no transcription and no OCR was used.

The key was taken as a hypothesis from the conventional three-count Pigpen layout that the solver was using on the neighbouring card HCP 1440, and then checked against every sign on this card. It gives English throughout with no exceptions, and the decoded text, not the transfer, is what confirms the key. Repeated letters are drawn the same way each time (O ×7, N ×7, T ×5, A ×4, and C, E, F, G, I, L, M, U, Y twice each), and no sign needs two values. The two signs that looked doubtful at low resolution were settled on enlargements: the second sign of MON is [ with a faint but present top stroke (O, not a corner), and the third sign of SAT is ⊔ with three dots (T); the diagonal lines crossing it belong to the portal's grey watermark wheel, not to the ink.

In review the transcription was checked independently, sign by sign, against the reviewer's own crops of the scan, and decoded with the reviewer's own script; both readings agree for all 46 signs.

## Key

A dotted three-block Pigpen variant. The cells of a plain 3×3 grid are taken in the order A–I; one dot selects A–I, two dots J–R, three dots S–Z. J is not omitted, so the ninth three-dot cell is unused.

| Outline (sides drawn) | 1 dot | 2 dots | 3 dots |
|---|---|---|---|
| bottom + right (┘) | A | J | S |
| bottom + left + right (⊔) | B | K | T |
| bottom + left (└) | C | L | U |
| top + bottom + right (]) | D | M | V |
| all four sides (□) | E | N | W |
| top + bottom + left ([) | F | O | X |
| top + right (┐) | G | P | Y |
| top + left + right (⊓) | H | Q | Z |
| top + left (┌) | I | R | (unused) |

## Plaintext

Main passage, as written on the card (commas, hyphen and full stop are on the card; a pen stroke underlines the two signs of ME):

```text
MON,
IF, YOU, DONT, GO
TO-NIGHT, CALL
ME UP.
```

Centre passage, continuing the plain cursive "this is":

```text
SAT
AFTERNOON
NANCY.
```

The mark after NANCY may be a comma rather than a full stop; this affects punctuation only. DONT is literal, without an apostrophe; MON and SAT are the writer's abbreviations.

Normalized English (capitals, apostrophe and full stops editorial; the cursive context in brackets):

- Centre: **[Dec. 16-07. Received your card Sat morning; this is] Sat. afternoon. Nancy.**
- Main: **Mon. If you don't go to-night, call me up.**

Slovak translation:

- Centre: **[16. 12. 1907. Tvoju pohľadnicu som dostala v sobotu ráno; teraz je] sobota popoludní. Nancy.**
- Main: **Pondelok. Ak dnes večer nepôjdeš, zavolaj mi.**

The two parts were most likely written on different days: the centre note on Saturday afternoon (14 December), the main message on Monday 16 December, when the card was dated and posted. "Call me up" is a request to telephone, which fits a card sent within one small town.

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-1442/work/decode.py
```

The script checks the SHA-256 hashes of the source files, decodes the manual sign transcription in work/transcription.json with the key above, checks all 46 letters against the displayed text and checks the re-encoding. It does not read the image; the transcription step is manual (and was confirmed independently in review).

## Uncertainties

- Who Nancy was, and her relation to Ray E. Bartley, is not established.
- The postmark year is illegible; 1907 rests on the handwritten "Dec. 16-07" and the portal.
- The cursive context lines are only partly legible under the watermark ("morn…").
- The word divisions in ME UP and TO-NIGHT follow the card's spacing and hyphen; the editorial spaces do not affect any letter.
- The key was transferred as a hypothesis from the HCP 1440 work; it is confirmed here by the coherent result over all 46 signs.
- No search for a prior publication was made beyond the portal status (Not solved), skip.txt and a same-day snapshot of the AI Decipherment Register, none of which lists this card.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, read all 46 signs from the scan in its own notation before comparing, decoded them with an independently written decoder that builds the key from the grid geometry, and found no differences. It checked key consistency, searched both sides of the card for untranscribed Pigpen (none), and checked the postmark and weekday. Its four findings were minor and are reflected here:

- The solver had described a "date/day mismatch". The reviewer showed that 16 December 1907 was a Monday, so MON agrees with the date and the postmark; only the centre note looks back to Saturday. The report now presents the weekday as supporting evidence and the two parts as written on different days.
- The addressee and postmark on the card (Ray E. Bartley, Rutland, Iowa; RUTLAND DEC 16) are now recorded.
- The underline under ME is noted in the literal transcription.
- A protocol note (a work file changed seconds after the hand-over marker) has no effect on the result; an English normalized reading has been added next to the Slovak translation.

No change to the plaintext resulted from the review. The closing steps (response to review, this report, the register entry) were prepared by Claude Opus 5.5 on the solver's behalf at the human's request; the decipherment itself was made by the solver, OpenAI GPT (GPT-6 Astra).

## Sources

- HC Portal record 1442, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1442 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4387/conversions/pc_hcp_123_adr-large.jpg (source/address.jpg).
- Picture side: https://api.hcportal.eu/media/4386/conversions/pc_hcp_123_pic-large.jpg (source/picture.jpg).
- AI Decipherment Register, public JSON snapshot of 2026-10-26 (ciphers/hcp-1450/work/register-snapshot.json), checked in review.
- Internal: the three-count Pigpen layout used for ciphers/hcp-1440/, applied here as a hypothesis.
