# HCP 1819 (pc_hcp_500): an alternating Pigpen Christmas card, "Go home on Saturday"

Human solver: Tomáš Pavuk

**Status: deciphered in full; independent review 1 verdict ACCEPT.** Report dated 2026-10-26.

## Origin and context

The cryptogram is record 1819 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1819), whose portal name is pc_hcp_500 (it is not portal record 500). It belongs to the HCPortal cryptographic postcards collection (private collection). When it was acquired on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard and Pigpen, language Unknown, with no transcription or solution attached.

It is a British Christmas card (Raphael Tuck & Sons, Christmas Post Card series); the picture side carries the printed greeting "A happy Christmas to you" and no cipher. The address side is postmarked TAMWORTH, 7.45 PM, DE 22; the year is hidden by the stamp, and the portal date 1904-12-22 is taken from the catalogue. The card is addressed to Miss Kite (so the scan appears to read; the portal gives "Kile"), Standon Green End, High Cross, near Ware, Hertfordshire. The cipher, 16 signs, is written along a curved line around an embossed feather on the left half; below it the sender signed in plain writing "Love from A.E.S.". The scans carry a large portal watermark.

![Address side; the cipher runs along the curve left of centre (source/address-large.jpg)](../source/address-large.jpg)

## Method

The transcription is **manual** (work/transcription.txt); the portal supplied none. Because the writing follows a curve, each sign has to be read in its own local orientation: "up" is taken as the reader's left of the local writing direction. Turned by 270 degrees the first words lie horizontal; the later signs turn progressively along the arc. This is an orientation convention for reading the handwriting, not a change of alphabet.

Each sign was recorded as a Pigpen outline or X-grid wedge plus dotted/undotted. The alphabet was carried over from the solver's earlier postcard work rather than rediscovered here; applied to this card it gives English over all 16 signs (13 distinct), with the repeated O (×3) and A (×2) drawn consistently. With so short a text, the fluent result is what confirms the key. Dots between words are separators; a final dot ends the line.

In review all 16 signs were read independently from enlarged and rotated crops of the scan and decoded with an independently written script; the reading matched the solver's token for token.

## Key

Alternating undotted/dotted Pigpen: each cell carries two consecutive letters, the first undotted and the second dotted. A plain 3×3 grid holds A–R, an X-grid holds S–Z.

| Outline or wedge | Undotted | Dotted |
|---|---|---|
| bottom + right | A | B |
| bottom + left + right | C | D |
| bottom + left | E | F |
| top + bottom + right | G | H |
| all four sides | I | J |
| top + bottom + left | K | L |
| top + right | M | N |
| top + left + right | O | P |
| top + left | Q | R |
| downward V | S | T |
| right-pointing wedge | U | V |
| left-pointing wedge | W | X |
| upward wedge | Y | Z |

## Plaintext

Signs as transcribed (outline/wedge, 0 = undotted, 1 = dotted) and the letters they give:

```text
R0 T0 | R1 T0 TR0 BL0 | T0 TR1 | V0 BR0 V1 >0 TL1 B1 BR0 ^0
G  O  | H  O  M   E   | O  N   | S  A   T  U  R   D  A   Y
```

On the card: **GO HOME ON SATURDAY** (no punctuation besides dot separators).

Normalized English: **Go home on Saturday.**

Slovak translation: **Choď domov v sobotu.**

With the catalogue date, the card was posted on Thursday 22 December 1904, so "Saturday" would be 24 December, Christmas Eve, which fits a Christmas card. "Love from A.E.S." is plain text, not deciphered material.

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-1819/work/decode.py
```

The script checks the SHA-256 hashes of the source images and maps the manual symbolic transcription in work/transcription.txt through the key, with an exact token round trip. It does not read the scan or compute local rotations; that step is manual (and was confirmed independently in review).

## Uncertainties

- Two signs depend on the assumed local orientation. The N of ON is a dotted corner at the point where the line begins to bend and could be taken for a dotted ">" wedge (giving OV). The S of SATURDAY is a near-right-angled wedge that could pass for a bottom+left outline (E) if the baseline were taken more vertical. Only the adopted readings give English, and the same orientation rule reads all other signs without strain.
- The text is short (16 signs), so the key is confirmed by fluency rather than by statistics.
- The year 1904 rests on the catalogue; the Tamworth cancel shows only DE 22, 7.45 PM.
- The recipient's surname (Kite on the scan, Kile in the catalogue) and the identity of A.E.S. are not established.
- A check of the AI Decipherment Register export (110 records) found no entry for this card; no search beyond that was made, so earlier publication cannot be excluded.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, re-hashed both scans, read all 16 signs in local orientation from its own crops before comparing, decoded them with its own script, and checked the context (Tamworth postmark, Christmas card, Saturday = Christmas Eve). Its four findings were minor:

- The command maps a manual transcription: this report states that the 16 tokens were confirmed independently in review.
- Two orientation-dependent signs (N of ON, S of SATURDAY): now named explicitly as the residual risk.
- Protocol: the source/ and work/ directories were modified about 100 seconds after the DONE1 marker. All files present predate the marker and the source hashes match, so the reviewed material is unchanged; the lapse is recorded in SOLUTION.md.
- The key was transferred from earlier postcards: the system is now named (alternating dotted/undotted Pigpen with an X-grid for S–Z) and its origin stated.

No change to the plaintext resulted from the review. The closing steps (response to review, this report, the register entry) were prepared by Claude Opus 5.5 on the solver's behalf at the human's request; the decipherment itself was made by the solver, OpenAI GPT (GPT-6 Astra).

## Sources

- HC Portal record 1819 (pc_hcp_500), General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1819 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/5518/conversions/pc_hcp_500_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/5517/conversions/pc_hcp_500_pic-large.jpg (source/picture-large.jpg).
- AI Decipherment Register export, 2026-10-26: https://ai.hcportal.eu/register/?format=json (no matching entry).
- Internal: the alternating Pigpen alphabet of the solver's preceding postcard analyses, applied as a hypothesis.
