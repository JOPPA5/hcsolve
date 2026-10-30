# HCP 1364 (pc_hcp_45): a shift-by-one love postcard from Wimborne, 17 July 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (38 of 38 enciphered letters); two short abbreviation groups are kept literal, as on the sister cards; independent review 1 verdict REVISE, findings addressed, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1364 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1364), portal name pc_hcp_45, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-07-17, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (a catalogue misspelling of Abbott), with no transcription or solution attached.

The picture side is a printed coloured view, "Hotel Majestic, Harrogate", with no writing; a dark blot in the sky is damage, not a sign. The address side is a Boots Cash Chemists "Pelham" Series card with a halfpenny Edward VII stamp, postmarked **WIMBORNE / 10 PM / JY 17 / 07**, and addressed in plain writing to **Mr W. Abbott, Stokelake Farm, Chudleigh, Devon**. The message is on the address side and is read with the card turned 90° anticlockwise. The large grey alphabet disc over the scan is the portal's watermark.

17 July 1907 was a Wednesday, which agrees with the plain heading "G. H. Wednesday". The card has the same recipient, formulae and apparent hand as the shift-by-one cards hcp-1386…1407 in this repository, which come from one couple in 1907–08. The same-hand judgement was made by eye. Harrogate on the picture and Wimborne on the postmark are not connected by anything on the card.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![Message turned upright (work/reading.png)](../work/reading.png)

## Method

The transcription is **manual**. The solver rotated the original scan and enlarged each line 4–5×. Every sign was read from the enlargements. No OCR was used and the portal supplied no transcription.

The key was not recovered blind. A shift of one was taken as a hypothesis from the accepted sister cards and tested on this card's pixels: all 38 enciphered letters give English with no exception and no adjustment for this card. The reviewer read every word sign by sign from its own enlargements and decoded its own reading with its own modular script. It got the same 38 letters, and shifts of 2 and 3 gave gibberish.

## Key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet. To decrypt, subtract one (A→Z).

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading "G. H. Wednesday" is ordinary writing, not shifted. The groups `M. L` and `M-L.` are kept literal (shifted they would be L. K.).

## Plaintext

| Ciphertext | Plaintext |
|---|---|
| G. H. Wednesday | (plain heading) |
| Nz. Pxo. M. L Cpz | MY. OWN. [M. L] BOY |
| Mfuufs. wfsz. | LETTER. VERY. |
| ojdf. up Ebz. | NICE. TO DAY. |
| Zpvs. Pxo M-L. | YOUR. OWN [M-L.] |
| Hjsm | GIRL |

The dots follow the card and carry no meaning; the writer dots nearly every word.

English: **G. H. Wednesday. My own M. L. boy, letter very nice to-day. Your own M-L. girl.**

Slovak translation: **G. H., streda. Môj vlastný M. L. chlapec, list dnes veľmi milý. Tvoje vlastné M-L. dievča.**

The sentence has no verb on the card ("letter very nice to-day"); no word is missing from the pixels.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1364/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the files in source/, decodes every token of the manual transcription in work/transcription.json, checks the inverse round trip, and prints the plaintext with the count: 38 enciphered letters and 4 abbreviation letters kept literal. It does not read the image; the transcription step is manual.

## Uncertainties

- **The initial of `M. L` / `M-L.`** Read M, N not excluded. In both places it has hook, stem and two further short legs, one leg more than the N of `Nz` and the same build as the M of `Mfuufs`. The extra leg is short and the legs run together in ink, and sister cards hcp-1402 and hcp-1368 keep N for this group, while hcp-1347 and hcp-1383 read M.
- **The second sign of the groups.** A slanted stem with a small foot, close to a plain l or a 1. L is the reading from the sister groups; 1 is not excluded, and hcp-1349 and hcp-1366 report `h` in this slot.
- **Meaning and status of the groups.** Not expanded and not known. Whether they are shifted at all cannot be decided from this card. In the closing group a dash stands where the salutation has a dot; on hcp-1402 such a stroke is taken as the L's lead-in stroke.
- **Capital of `Mfuufs`.** A compact three-stroke M, the writer's form for this word (compare hcp-1386). N would give METTER, so the word shape helps decide it.
- **`Pxo` on line 4.** At low zoom it looks like "Bo", because the foot of the P and the x run together. At 4× the x's crossing strokes and the o are visible.
- **The heading initials G. H.** Plain, also on hcp-1397 and hcp-1402, meaning unknown. The form with a descending tail fits G; C is not wholly excluded.
- **Writer.** Not stated. "Girl" comes only from the signature formula.
- **Prior publication.** The portal shows no solution, and the AI Decipherment Register had no record of this card on 2026-10-30. No wider web search for this card was made.

![Capitals, left to right: Nz, salutation group, closing group, Mfuufs (work/crops/cap_compare.png)](../work/crops/cap_compare.png)

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. The reviewer ran the reproduction command, rechecked the source hashes, decoded its own sign-by-sign reading with its own script, and confirmed the 38 enciphered letters, the date and weekday, the address and postmark, and that neither side has other cipher text. It found no hidden restorations. It could not establish the meaning of the groups or the writer's identity. Its five findings were all accepted:

- **Initial of the groups (major).** The solver had read N "as in `Nz`"; the pixels show the three-stroke form of the `Mfuufs` capital. Changed to M, N not excluded.
- **Punctuation (minor).** No dot after `Cpz` and none after the L of the first group. Corrected.
- **Sister citation (minor).** hcp-1384 was wrongly cited for this group. Replaced.
- **Unsupported citation (minor).** hcp-1383 was wrongly cited for the word shape of `Mfuufs`. Removed.
- **L caveat (minor).** The doubt about 1 and `h` is now stated.

No enciphered letter changed. Only the four literal abbreviation letters and the punctuation of the first row did.

## Sources

- HC Portal record 1364, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1364 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4152/conversions/pc_hcp_45_pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/4152/pc_hcp_45_pic.JPG.
- Address side: https://api.hcportal.eu/media/4153/conversions/pc_hcp_45_adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/4153/pc_hcp_45_adr.JPG.
- Sister cards in this repository: ciphers/hcp-1386 and hcp-1402 (key, formula), hcp-1347, 1349, 1366, 1368, 1383 (abbreviation groups).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.

Credits: capture, transcription, decipherment, response to review and this report by Claude Opus 5.5, 2026-10-30; there was no earlier work on this number.
