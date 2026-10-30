# HCP 1498 (pc_hcp_179): three Pigpen words on a Peckham postcard, 1905

Human solver: Tomáš Pavuk

**Status: solved, accepted in independent review 1 (2026-10-26).** The only enciphered passage on the card is three words in standard Pigpen embedded in an ordinary cursive letter. All 18 signs decode under one fixed key to LATE, TONIGHT, DARLING.

## Origin and context

The card is item 1498 of the HCPortal cryptographic postcard collection (`pc_hcp_179`, private collection), https://crypto.hcportal.eu/dashboard/cryptograms/1498. The portal gives the date 1905-01-13, region Europe, language Unknown, the tags Pigpen and Substitution / Monoalphabetic, **sender Ernest** and recipient E. Mobsby. At acquisition (2026-10-26) the portal status was **Not solved**, with no attached transcription or solution.

The card is addressed to **Mr E. Mobsby, 9 Carden Rd, Peckham, S.E.** (south-east London), with a ½d Edward VII stamp. The letter begins "Dear Ernest" and is signed at the top "Yours etc Maud". Ernest is therefore the recipient and Maud the writer; the portal's sender field appears to be wrong. The postmark could not be read well enough at this resolution to confirm the portal date. The picture side shows Court Lane, Dulwich, and carries no cipher. HCP 1497 in this collection has the same hand, addressee, address and key.

![Address side of the card (source/address-large.jpg). The Pigpen words are in the line beginning "be" in the lower left of the message.](../source/address-large.jpg)

## Method

The message is ordinary English cursive except for one line, where angular box-and-wedge signs appear between "Don't be" and "if you can help it", separated by commas into three groups (4, 7 and 7 signs). Their shapes are those of Pigpen. The standard interleaved Pigpen key (letters A–R in a dotted and undotted 3×3 grid, S–Z in dotted and undotted wedges) was tested on all 18 signs and gives three English words with no exceptions. The repeated letters T, N, I, G, L and A take the same sign every time they occur. The signs were transcribed by hand from the scan and enlarged crops (no OCR; the portal has no transcription), then decoded by a script.

![The Pigpen line enlarged five times (work/cipher-5x.jpg).](../work/cipher-5x.jpg)

## Key

Interleaved Pigpen. Each sign is named by the sides of the grid cell it shows (T top, B bottom, L left, R right; C all four sides), with 0 for undotted and 1 for dotted; wedges are named by the direction they open.

| Sign | Letter | Sign | Letter |
|---|---|---|---|
| BR0 / BR1 (bottom+right) | A / B | T0 / T1 (top+left+right) | O / P |
| B0 / B1 (bottom+left+right) | C / D | TL0 / TL1 (top+left) | Q / R |
| BL0 / BL1 (bottom+left) | E / F | V0 / V1 (wedge, opens up) | S / T |
| R0 / R1 (top+bottom+right) | G / H | >0 / >1 (wedge) | U / V |
| C0 / C1 (box) | I / J | <0 / <1 (wedge) | W / X |
| L0 / L1 (top+bottom+left) | K / L | ^0 / ^1 (wedge) | Y / Z |
| TR0 / TR1 (top+right) | M / N | | |

Only the signs that occur on the card (for A, D, E, G, H, I, L, N, O, R, T) are evidence for this key; the rest is the conventional completion.

## Plaintext

Sign by sign, as on the card:

| Word | Signs | Letters |
|---|---|---|
| 1 | L1 BR0 V1 BL0 | L A T E |
| 2 | V1 T0 TR1 C0 R0 R1 V1 | T O N I G H T |
| 3 | B1 BR0 TL1 L1 C0 TR1 R0 | D A R L I N G |

```
LATE, TONIGHT, DARLING
```

In context (the cursive around it is plain English): "… did you see L.A.? Don't be LATE, TONIGHT, DARLING, if you can help it. I think Elsie is coming with us …". Capitalization of the cipher words is editorial; the commas are on the card.

Slovak translation of the sentence: „Ak môžeš, nemeškaj dnes večer, miláčik.“

## Reproduction

From the repository root:

```
python3 -I ciphers/hcp-1498/work/decode.py
```

The script checks the SHA-256 hashes of the files in `source/`, decodes the 18 tokens of the manual transcription in `work/transcription.txt` with the key above, checks the inverse mapping, and prints LATE / TONIGHT / DARLING with "Encrypted glyphs: 18". It checks the mapping, not the pixels; the transcription was checked against the scan by the reviewer's independent reading.

## Uncertainties

- The first sign of LATE (dotted, L) touches the final e of the cursive "be". It is readable when enlarged but is the one crowded sign of the 18.
- Dots decide between paired letters. The dot on the wedge in LATE (T, not S) and the undotted G against the dotted H in TONIGHT were checked at high magnification; no other dot is doubtful.
- Only the Pigpen passage is claimed as deciphered. The surrounding cursive is plain text and is quoted only for context; it was not fully transcribed.
- The postmark date was not confirmed from the cancel; the portal date 1905-01-13 is reported as given.
- Maud and Ernest (E.) Mobsby are not identified as historical persons.
- Absence from the AI Decipherment Register snapshot of 2026-10-26 does not prove that no decipherment was published elsewhere.

## Review summary

Reviewer: Claude Opus 5.5, round 1, verdict **ACCEPT**. The reviewer reran the command, read all 18 signs from their own crops before comparing, decoded them with an independent geometric Pigpen script (token-identical to the solver's transcription), and checked the rest of the card for further cipher signs (none). Findings, all minor:

- Address: the card reads 9 Carden Rd, not the provisional "Ewerdon Rd" of the solver's notes; corrected in this report and in `SOLUTION.md`.
- Sender and recipient: Ernest is the recipient and Maud the writer; the portal's sender field is noted as apparently wrong.
- The crowded first sign of LATE is listed as an uncertainty.
- The report states that the command verifies the mapping, not the pixels.

The plaintext did not change. The closing steps (response to the review, this report and the register entry) were prepared by Claude Opus 5.5 on the solver's behalf at the human's request.

## Sources

- Portal page: https://crypto.hcportal.eu/dashboard/cryptograms/1498 (General, Description and Attachments tabs, read 2026-10-26).
- Address side: https://api.hcportal.eu/media/4555/conversions/pc_hcp_179_adr-large.jpg (`source/address-large.jpg`).
- Picture side: https://api.hcportal.eu/media/4554/conversions/pc_hcp_179_pic-large.jpg (`source/picture-large.jpg`).
- AI Decipherment Register snapshot: https://ai.hcportal.eu/register/?format=json (`work/register-snapshot.json`); no entry for this card.
- No published solution was used.
