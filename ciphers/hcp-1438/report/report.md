# HCP 1438 (pc_hcp_119): a dotted Pigpen postscript to Ray Bartley

Human solver: Tomáš Pavuk

**Status: deciphered in full; independent review 1 verdict ACCEPT.** Report dated 2026-10-26.

## Origin and context

The cryptogram is record 1438 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1438), portal name pc_hcp_119, part of the HCPortal cryptographic postcards collection (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard and Pigpen, main category Substitution (monoalphabetic), language Unknown, date 1908-05-28, sender Unknown, recipient Ray Bartley, with no transcription or solution attached.

It is a Davidson Bros. "Real Photographic Series" postcard (London & New York, printed in England). The picture side shows three cats with the printed caption "CAN YOU HEAR IT?" and carries no handwriting. The address side holds a plain cursive message headed "Rutland Iowa May-28-08", which tells of receiving a card, of visitors (Walter; Ruth and Mabe on their way to school to take exams) and of being alone all day, and is signed in plain script **Ethel Pattee**. The postmark reads RUTLAND MAY 28 1908 IOWA, and the card is addressed to Ray Bartley, Laurens, Iowa. 28 May 1908 was a Thursday. The portal's "Sender: Unknown" is supplemented here by the signature as written; the writer is not identified further.

The cipher is a postscript: a plain "P.S." followed by 36 Pigpen signs in two narrow lines written up the left margin of the address side (rotate the scan 90° counter-clockwise to read them). The related card HCP 1440, also to Ray Bartley and also postmarked Rutland, uses the same key and mentions "Mrs P." and "Ethel"; this is consistent with the same circle of correspondents but proves nothing.

![Address side; the two Pigpen lines run up the left margin after the plain P.S. (source/address.jpg)](../source/address.jpg)

## Method

The solver traced each sign manually from the scan and enlarged crops into work/transcription.txt as an outline (which sides of the cell are drawn) plus a dot count. The signs use nine tic-tac-toe outlines with one, two or three dots, a dotted three-block Pigpen (the same scheme as on HCP 1440 and, in this repository, HCP 1190). With the plain 3×3 grid read A–I and the dot count selecting the block, all 36 signs decode to English under one fixed table, with no word-specific exceptions. Repeated letters are drawn the same way each time: the three Ts of LETTERS, WITH and SAT are all the three-sided cup with 3 dots, Y in MY and YOU is the top-right corner with 3 dots, R in BRING and LETTERS is the top-left corner with 2 dots.

In review all 36 signs were transcribed again from the scan, independently, by the strokes seen plus dot count (6–16× crops of each line), and decoded with an independently written script. The comparison gives 0 differences out of 36.

## Key

A dotted three-block Pigpen. The cells of a plain 3×3 grid are taken in the order A–I; one dot selects A–I, two dots J–R, three dots S–Z. J is not omitted, so the ninth three-dot cell is unused. Solver labels from work/transcription.txt are given in brackets.

| Outline (sides drawn) | 1 dot | 2 dots | 3 dots |
|---|---|---|---|
| bottom + right (BR) | A | J | S |
| bottom + left + right (B) | B | K | T |
| bottom + left (BL) | C | L | U |
| top + bottom + right (R) | D | M | V |
| all four sides (C) | E | N | W |
| top + bottom + left (L) | F | O | X |
| top + right (TR) | G | P | Y |
| top + left + right (T) | H | Q | Z |
| top + left (TL) | I | R | (unused) |

## Plaintext

Transcription (work/transcription.txt; label = outline, digit = dot count, | = word gap):

```text
TL2 BL2 C1 BR1 BR3 | B1 TL2 TL1 C2 TR1 | R2 TR3 | BL2 C1 B3 B3 C1 TL2 BR3
C3 TL1 B3 T1 | TR3 L2 BL3 | BR3 BR1 B3 | TL1 L1 | BL3 | BL1 L2 R2 C1
```

As written, decoded (P.S. is in plain script and not encrypted; the commas and the final full stop are on the card, as recorded in review):

```text
P.S. RLEAS, BRING, MY, LETTERS
WITH, YOU, SAT, IF, U, COME.
```

Normalized English (bracketed parts editorial): **P.S. [Please] bring my letters with you Sat[urday] if [yo]u come.**

Slovak translation: **P.S. [Prosím,] prines so sebou moje listy v sobotu, ak prídeš.**

The opening word is literally RLEAS. Its first sign is a top-left corner with two dots, the same shape as the R of BRING and LETTERS, not the top-right corner of P (and of G and Y). With only five signs, PLEASE would also need a final E that is not on the card. The word is very probably the writer's slip for PLEAS(E), a horizontally mirrored corner with the final E dropped, but it is not corrected in the literal text. SAT and U are the writer's abbreviations; Saturday was 30 May 1908, two days after the postmark.

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-1438/work/decode.py
```

The script checks the SHA-256 hashes of the source files, decodes the manual transcription in work/transcription.txt with the key above and checks the token/key round trip. It prints the 36 letters with spaces for the word gaps; it does not read the image. The transcription step is manual and was confirmed independently in review.

## Uncertainties

- RLEAS is the literal reading; what the writer intended by the opening top-left corner is not certain, only its shape. [Please] is an interpretation.
- The signs are small (about 10 px in a 1024 px scan) and some dots touch their outlines. Solver and reviewer counted the dots of all 36 signs the same way; the three-dot top-right corners of MY and YOU can look like right brackets at reduced scale.
- The third sign of RLEAS is a somewhat slanted closed box with one central dot (E); its heavy right edge is not counted as a second dot.
- SAT = Saturday and U = you are expansions, not additional deciphered letters.
- Ethel Pattee is the signature as written; the writer, and Ray Bartley, are not identified further.
- No published decipherment was found: the portal showed Not solved with no attachment, and a same-day snapshot of the AI Decipherment Register has no entry for this card. No wider search was made.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output byte-identical to the solver's saved check), transcribed all 36 signs from the rotated scan in its own notation before comparing, decoded them with an independent script (0 differences), checked key consistency and the repeated letters, examined the opening sign at 10×, checked the rest of the card for missed ciphertext and checked the context. Its two findings were minor and are reflected here:

- No normalized English reading was given: it is added above, with editorial parts in brackets, and the final full stop on the card is kept in the literal text.
- The plain-text context was unused: the signature Ethel Pattee, the place Rutland, Iowa, the postmark and the weekday (Thursday, so SAT is Saturday 30 May) are now given under Origin and context.

No change to the plaintext resulted from the review. The closing steps (response to review, this report, the register entry) were prepared by Claude Opus 5.5 on the solver's behalf at the human's request; the decipherment itself was made by the solver, OpenAI GPT (GPT-6 Astra).

## Sources

- HC Portal record 1438, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1438 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4375/conversions/pc_hcp_119_adr-large.jpg (source/address.jpg).
- Picture side: https://api.hcportal.eu/media/4374/conversions/pc_hcp_119_pic-large.jpg (source/picture.jpg).
- AI Decipherment Register snapshot, 2026-10-26: https://ai.hcportal.eu/register/?format=json (saved in ciphers/hcp-1440/work/register-snapshot.json).
- Related card: ciphers/hcp-1440/ (HCP 1440, also to Ray Bartley), consulted for context only.
