# HCP 1379 (pc_hcp_60): a Caesar-shift love postcard, 9 April 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (52 of 52 enciphered letters); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1379 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1379), portal name pc_hcp_60, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-04-09, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (a catalogue spelling), with no transcription or solution attached.

The picture side is a Frith's Series coloured view printed "Loch Long. Highland Cattle", with no writing on it. The address side carries a halfpenny Edward VII stamp, the postmark WIMBORNE, 10 PM, AP 9 07, and the plain address **Mr W. Abbott, Stokelake Farm, Chudleigh, Devon**.

The message is written sideways in the left half of the address side, so the card must be turned 90° counter-clockwise to read it. It consists of five short cipher lines and one plain heading line: **C. H. Tues. April 9th**. The heading agrees with the postmark, and 9 April 1907 was indeed a Tuesday. The grey wheel over both scans is the portal's watermark, not part of the card.

The card evidently belongs to the same correspondence as the Caesar cards HCP 1386–1407, with the same recipient, the same Wimborne origin, the same plain "C. H." style of heading and the same closing formula. The reviewer compared these features, not the handwriting in detail.

![Picture side: Loch Long, Highland Cattle (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned; the message is in the left half, sideways (source/address-large.jpg)](../source/address-large.jpg)

![Message area turned 90° counter-clockwise (work/reading.png)](../work/reading.png)

## Method

Claude Opus 5.5 captured the record and did the solving; there is no earlier work on this number. No published solution was found or used.

The solver turned the un-converted original scan upright, enlarged it, and transcribed each word manually. The shift −1 was tried first because the sister cards use it, and it fitted all five lines at once. All 25 shifts were later printed by the reviewer; only this one gives language. The one hard word was the second word of line 3: first attempts (Nfbot, Nfpvh) made no sense, until the long stroke with a small loop was recognised as p, and the three-legged capital, compared with the two-legged N of `Nz`, as M. That gives `Mpwf` = LOVE.

## Key

Caesar shift: each plaintext letter is written as the next letter of the alphabet, so to decrypt, subtract one. Z would wrap to A (not used on this card).

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading "C. H. Tues. April 9th" is ordinary writing and is not shifted.

## Plaintext

| Ciphertext | Literal plaintext |
|---|---|
| Nz. Efbsftu J. ipqf | MY. DEAREST I. HOPE |
| Zpv. bsf. gffmjoh | YOU. ARE. FEELING |
| cfuufs: Mpwf | BETTER: LOVE |
| gspn Zpvs. Pxo | FROM YOUR. OWN |
| Hjsm. | GIRL. |

The writer's dots are kept in the literal text; they stand after many words, not only at the end of sentences.

English (the plaintext itself, with editorial punctuation): **My dearest, I hope you are feeling better. Love from your own Girl.**

Slovak translation: **Môj najdrahší, dúfam, že sa cítiš lepšie. S láskou tvoje vlastné dievča.**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1379/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the two scans in source/ and the two originals in work/hires/, decodes every token of the manual transcription in work/transcription.json, checks the inverse shift, and prints the five lines, the count of 52 letters and the weekday of 9 April 1907. It does not read the image; the transcription step is manual and was repeated independently in review.

## Uncertainties

- **`Mpwf`, first letter.** The least clean letter on the card. It is read as M, one leg more than the N of `Nz`; the reviewer confirmed this from the pixels. Read as N it would give MOVE, which makes no sense here.
- **`Mpwf`, third letter, and the `m` of `gffmjoh`.** These are compressed minims that cannot be counted firmly. Both letters are chosen by word sense; no other letter makes a word in either place. Nothing else is restored.
- **`Efbsftu` and `cfuufs`.** The `ftu` of the first and the `uu` of the second run together, but the outlines fit.
- **Split nib.** The ink splits into double lines on `gspn` and at the end of `Mpwf`; no letter is affected.
- **Punctuation.** The dots are as seen, and partly editorial. The mark after `cfuufs` looks like two dots and is taken as a colon. A very pale ditto-like mark between `gspn` and `Zpvs` has no letter form and is left out.
- **The heading.** "C. H." is not expanded and its meaning is unknown. The first initial could also be G: a large loop with a low finish running into a small descending stroke. This is plain text, so the decipherment is unaffected.
- **Pencil "(11)".** A circled number at the upper left of the address side, probably added later by a collector or archive. It is not part of the message.
- **Identities.** The writer signs only as "Girl", and her name is not known. It is not proved that the hand is the same as on HCP 1386–1407.
- **Prior publication.** Beyond the portal status (Not solved) and the AI Decipherment Register (no record, checked 2026-10-30), no search for an earlier reading of this card was made.

## Review summary

Reviewer: a separate Claude Opus 5.5 session, round 1, verdict **ACCEPT**. Solver and reviewer are the same model, so this is not a second-vendor check. The reviewer ran the command, typed its own transcription from its own enlargements of the original scan, decoded it with a separately built table (identical result, 52 letters), checked every word against the pixels, and tried to refute the reading through alternatives such as MOVE and FEEMING. It raised three minor findings, all addressed:

- **Heading initial.** The possible G is now disclosed.
- **Wording about restorations.** The statement that every letter was read from the pixels was too strong; it now says that `w` and `m` are chosen by word sense.
- **Pencil "(11)".** Now mentioned.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1379, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1379 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4197/conversions/pc_hcp_60_pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/4197/pc_hcp_60_pic.JPG (work/hires/).
- Address side: https://api.hcportal.eu/media/4198/conversions/pc_hcp_60_adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/4198/pc_hcp_60_adr.JPG (work/hires/).
- Sister cards in this repository: ciphers/hcp-1386 to ciphers/hcp-1407, in particular hcp-1397 (same closing formula).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.
