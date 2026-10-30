# HCP 1476 (pc_hcp_157): a Pigpen closing on a postcard to W. Pooley, 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (22 of 22 cipher letters); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1476 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1476), portal name pc_hcp_157, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection and Pigpen, category Substitution / Monoalphabetic, date 1907-10-24, language Unknown, location Europe, sender Unknown, recipient W. Pooley. No transcription or solution was attached.

The picture side carries a printed text, "Wife's Commandments"; it has no cipher. The address side is a British "POST CARD" with a green King Edward VII halfpenny stamp. Its circular postmark shows OC 24; the town name is only partly legible. Turned upright (90° clockwise), the left half holds an ordinary message in English cursive:

> What do you say about these Charlie you see any old rule won't do I am thinking if you think it will it be a case of "but you go neck and crop" Bye Bye

The writer is responding to the printed "Wife's Commandments". Directly after "Bye Bye", and running on into the next line, comes a short passage in Pigpen. This passage is the cryptogram. The right half carries the address in cursive (Pooley, apparently in care of a Mrs Hutchings). It is not needed for the reading and is not transcribed here.

![Address side turned upright (work/upright.jpg)](../work/upright.jpg)

![The cipher passage after "Bye Bye", enlarged (work/cipher-full-large.jpg)](../work/cipher-full-large.jpg)

## Method

The cipher is the standard Pigpen ("Freemason's") cipher in its common interleaved form. Two grids (a #-grid and an X-grid) are each used once without dots and once with dots, so that consecutive letters share a shape and differ only by the dot. The shapes were read by hand from enlargements of the upright scan and written down with a label for the strokes present plus 0/1 for "no dot"/"dot". No OCR was used. A short script decodes the transcription with the key and checks the result.

The OpenAI GPT solver (GPT-6 Astra) made the transcription and reading on 2026-10-26. It left the mark at the end unexplained. Claude Opus 5.5 completed the work on 2026-10-29. A separate Claude Opus 5.5 agent then reviewed it: the reviewer read every glyph again from its own crops (8–16×) and decoded them with its own script. It obtained the same 22 letters.

## Key

| Shape (strokes present / wedge point) | Undotted | Dotted |
|---|---|---|
| bottom + right (BR) | A | B |
| bottom + left + right (B) | C | D |
| bottom + left (BL) | E | F |
| top + bottom + right (R) | G | H |
| all four sides (C) | I | J |
| top + bottom + left (L) | K | L |
| top + right (TR) | M | N |
| top + left + right (T) | O | P |
| top + left (TL) | Q | R |
| wedge pointing down (V) | S | T |
| wedge pointing right (>) | U | V |
| wedge pointing left (<) | W | X |
| wedge pointing up (^) | Y | Z |

The card uses 15 of these 26 cells. The table is the conventional one. Letters that do not occur (for example U/V and X) are filled in from the standard key, not from this card.

## Plaintext

Transcription (line 1 ends the cursive line; line 2 is the line below):

```text
TR0 ^0 , T0 <0 TR1
B1 BR0 TL1 L1 C0 TR1 R0 , V0 <0 BL0 BL0 V1 R1 BL0 BR0 TL1 V1
```

Decoded:

```text
MY, OWN
DARLING, SWEETHEART
```

English: **"My own darling, sweetheart."**

Slovak translation: **„Môj vlastný miláčik, zlatko.“**

The closing is natural English of the period and fits where it stands, as the affectionate sign-off after "Bye Bye". The catalogue gives the language as Unknown; the reading shows it is English.

After the last T there is a small symmetric mark, `—(•)—`. It is not a Pigpen shape (see below).

![The end mark after SWEETHEART (work/end-mark-large.jpg)](../work/end-mark-large.jpg)

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1476/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the files in source/, decodes the manual transcription in work/transcription.txt with the key above, checks that each of the 22 letters re-encodes to its glyph label, and prints the plaintext and a note that the end mark is not a letter. It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **The W of OWN is malformed.** The fourth glyph of line 1 is drawn as a 7-like angle with its point at the upper right. Read literally, that is the right-pointing wedge, U, which would give "MY OUN". The W of SWEETHEART is drawn correctly, pointing left. The glyph is read as W from context. A small tick above it on the right is taken as a stray stroke rather than a dot (a dot would give X).
- **The dot of the first T in SWEETHEART** is crossed by the loop of a cursive letter from the line above. Without the dot the glyph would be S ("SWEESHEART"). T is read from context.
- **The end mark** is crisp, symmetric and tapered. It is as dark as the printed divider rule and legend of the card and darker than the handwriting: the mean of the darkest 20 pixels is 83 for the mark and the printed rule, 72 for the printed text, 97–103 for the cipher glyphs and 116 for the cursive. It also stands next to the printed divider. It is therefore probably a printed ornament of the card, not something the writer drew. Either way it matches no Pigpen shape and is not a letter. This conclusion rests on a JPEG scan; the card itself was not examined.
- The writer, W. Pooley and Charlie are not historically identified. The postmark town is not fully legible. The date 1907-10-24 comes from the portal and agrees with the visible OC 24.
- Prior publication: the portal status was Not solved and no solution was attached. The AI Decipherment Register (https://ai.hcportal.eu/register/) had no record for this card when checked on 2026-10-29.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1. Verdict: **ACCEPT**. The reviewer ran the reproduction command and checked every glyph against the scan at 8–16×. It decoded its own independent glyph reading with its own script and got the same 22 letters. It confirmed that the standard key explains every glyph with none left over and that the text is natural English for 1907. It also found no undisclosed published solution. It raised four minor findings, all accepted:

- **F1, malformed W:** now disclosed as an uncertainty (above).
- **F2, the uncertain dot of the T:** now disclosed.
- **F3, end mark:** the earlier explanation, "a decorative full stop drawn by the writer", is replaced by "probably a printed ornament of the card", based on the reviewer's ink-density measurements.
- **F4, documentation:** fixed. The comma after MY is now in the transcription, the decoding script no longer calls the end mark "uninterpreted", outdated status text was removed, and credit for the earlier GPT work is stated.

No decoded letter changed as a result of the review.

## Credits

Transcription and decipherment of the 22 letters: OpenAI GPT (GPT-6 Astra), 2026-10-26. End-mark assessment, response to review and this report: Claude Opus 5.5, 2026-10-29/30. Independent review: a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1476, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1476 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4489/conversions/pc_hcp_157_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4488/conversions/pc_hcp_157_pic-large.jpg (source/picture-large.jpg).
