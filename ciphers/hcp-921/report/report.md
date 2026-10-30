# HCP 921: a Pigpen postcard to Miss Larkin, Horsmonden (1912)

Human solver: Tomáš Pavuk

**Status: deciphered in full (11 of 11 intact cipher signs; one sign struck out by the writer). Independent review 1 verdict ACCEPT; the only change after review was one punctuation dot.** One sign value (the dotted right-pointing wedge = S) is contextual and is explained below. Report dated 2026-10-30.

## Origin and context

The cryptogram is record 921 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/921), portal name `cpc_1912-12-06_UK_Horsmonden_UK_Horsmonden_`. It belongs to Tobias Schrödel's collection of cryptographic postcards (private collection). The portal page was captured on 2026-10-25. At that time it listed the card as **Not solved**, with the tags Postcard, T. Schrödel Collection and Pigpen, category Substitution / Monoalphabetic, date 1912-12-06 and language Unknown. The sender is unknown and the recipient is given as Miss Larkin. No transcription or solution was attached.

The picture side is a comic Bamforth-style card showing children, captioned "Two's company, three's none." It carries no cipher. The address side is addressed in plain writing to **Miss Larkin, Hoath Hatch, Horsmonden**, a village in the Weald of Kent, and has a Horsmonden postmark. Beside the cipher the writer added the plain date **4-12-12** (4 December 1912). The catalogue date is 6 December 1912. The message itself is two short lines of Pigpen, written sideways on the message half of the address side.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned; the cipher runs sideways on the left half (source/address-large.jpg)](../source/address-large.jpg)

![The cipher turned upright and enlarged (work/message-large.jpg, a crop of the address side)](../work/message-large.jpg)

## Method

The transcription was done **by hand** from enlarged crops of the address side; no OCR was used. The card was turned so that the cipher lines run horizontally. That orientation was fixed by the punctuation dots, which then sit on the baseline. Turned the other way up, the signs decode to nonsense. Each sign was recorded by the strokes of its outline (for example TR = top and right strokes, C = closed square) or, for the V-shaped signs, by the direction in which its point faces. A suffix of 0 or 1 marks whether the sign has a dot:

```text
TR0 C0 [blot] >1 >1 .   TR0 BR0 ^0 .
B1 C0 BL0 B1 .
```

Cards from the same collection in the same cipher family (HCP 1188, 1187, 1497, 1498, all finished in this repository) use an *interleaved* Pigpen. Each grid cell holds two consecutive letters, undotted for the first and dotted for the second. That key was applied unchanged. It decodes nine of the eleven intact signs into M I, M A Y and D I E D. The remaining sign type, a right-pointing wedge with a dot, occurs twice in a row. Under the family key it would be V, giving "MIVV", which is not a word.

## Key

Interleaved Pigpen, as on the sister cards:

| Outline / wedge | Undotted | Dotted |
|---|---|---|
| bottom+right (BR) | A | B |
| bottom+left+right (B) | C | D |
| bottom+left (BL) | E | F |
| top+bottom+right (R) | G | H |
| closed square (C) | I | J |
| top+bottom+left (L) | K | L |
| top+right (TR) | M | N |
| top+left+right (T) | O | P |
| top+left (TL) | Q | R |
| wedge pointing down (V) | S | T |
| wedge pointing right (>) | U | V |
| wedge pointing left (<) | W | X |
| wedge pointing up (^) | Y | Z |

**Card-specific exception: the dotted right-pointing wedge (>1) is read as S.** This value is **not** derived from the key. It is inferred from the word: with M, I, A, Y, D and E fixed by the key, the first word is MI followed by a doubled letter, before a name. The only natural English completion is MISS. In none of the regular Pigpen layouts checked by solver and reviewer would S come out as a dotted right wedge. Those checks were the standard non-interleaved layout, interleaved layouts with other quadrant orders, and an alphabet with one letter left out. The writer therefore either placed S/T differently in the X or dotted the sign by mistake. A sign heavily struck out in ink stands directly before the two wedges. That fits a writer who was unsure of exactly this letter.

## Plaintext and translation

Literal decipherment (the writer puts a dot after every word):

```text
MI[struck-out sign]SS. MAY.
DIED.
```

English (original language): **Miss May died.**

Slovak translation: **Slečna May zomrela.**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-921/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the files in `source/`, then decodes the manual transcription `work/transcription.txt` with the family key plus the one exception. It prints `MISS. MAY. / DIED.`, the count of 11 intact signs with one struck-out sign omitted, and, for comparison, the unchanged family-key reading `MIVV. MAY. / DIED.`. It does not read the image.

## Uncertainties

- **The S value is contextual.** It covers 2 of the 11 signs and rests on the word fit alone. The writer's own placement of S in the X cannot be checked, because the card shows no other wedge letters except Y.
- **The struck-out sign** after MI is solid ink, and its original outline cannot be recovered. It is read as the writer's own cancellation and is not restored.
- **The message is very short**, so its statistical support is small. The reading rests on the externally established family key and on the coherence of the sentence.
- **"May"** may be a forename or a surname. Nobody's identity is established, nor whether the death took place. No genealogical sources were consulted.
- **Date.** The handwritten 4-12-12 (4 December 1912) and the catalogue date of 6 December 1912 are not reconciled. The postmark day is not legible enough in the scan to decide between them.
- No published solution of this card was found. The portal status was Not solved, and the AI Decipherment Register had no entry for it (checked 2026-10-25 and 2026-10-29).

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command and got the claimed output. It then wrote its own decoder that rebuilds the interleaved key from first principles and decoded **its own** sign-by-sign reading of the scan, made from fresh crops in both orientations at 4–16× enlargement. Its reading agreed with the solver's in every sign. It confirmed the orientation, the dots inside both wedges, and that the struck-out sign cannot be recovered. It also confirmed that no regular layout yields S for the dotted wedge, and that MISS is the only natural completion. It made three minor findings:

1. **A missing dot.** A baseline punctuation dot after the doubled wedge had been recorded as a plain word space. This was fixed in the transcription; the literal reading is now `MISS. MAY. / DIED.` and the meaning is unchanged.
2. **S is contextual.** The reviewer agreed with how this was disclosed and asked that the report and register entry keep the same wording. They do.
3. **Date bookkeeping.** The handover marker is in UTC, while the notes used the local date. The two card dates are left unreconciled, as above.

No decoded letter changed as a result of the review.

## Credit

The source capture, the first transcription and the candidate reading MISS MAY DIED were made by an earlier OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) on 2026-10-25. Claude Opus 5.5 re-verified the signs on the scan, rewrote the decoder with the full family key, wrote the solution and, after review, this report (2026-10-29/30). The independent review was made by a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 921, General, Description and Attachments tabs, captured 2026-10-25: https://crypto.hcportal.eu/dashboard/cryptograms/921 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/2824/conversions/cpc_1912-12-06_UK_Horsmonden_UK_Horsmonden__adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/2823/conversions/cpc_1912-12-06_UK_Horsmonden_UK_Horsmonden__pic-large.jpg (source/picture-large.jpg).
- Sister-card key: ciphers/hcp-1188, hcp-1187, hcp-1497, hcp-1498 in this repository.
- Tobias Schrödel, cryptographic postcards (HistoCrypt): https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
- AI Decipherment Register: https://ai.hcportal.eu/register/
