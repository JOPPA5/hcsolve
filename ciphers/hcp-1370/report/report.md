# HCP 1370 (pc_hcp_51): an English Caesar sweetheart postcard, Monday 30 September 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (58 of 58 enciphered letters); two abbreviation groups (`E-L.`, `M & L.`) kept literal. Independent review 1 verdict REVISE, findings addressed, no change to the decoded letters.** Report dated 2026-10-30 (UTC).

## Origin and context

The cryptogram is record 1370 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1370), portal name pc_hcp_51, part of the HCPortal collection of cryptographic postcards. When captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-07-30, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (catalogue spelling), with no transcription or solution attached.

The picture side is a printed view, "Cliff Gardens, Boscombe", with no handwriting. The address side is a Max Ettlinger "Royal Series" card, Bournemouth Series 1089. It is addressed in plain writing to **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon**, and has a halfpenny Edward VII stamp and a WIMBORNE postmark showing day 30; the month is not legible. The message runs up the left half of the address side, so the card must be turned 90° counter-clockwise to read it. The grey wheel on the scans is the portal's watermark.

The card belongs to the W. Abbott correspondence in this repository (HCP 1375, 1383, 1386–1407), a couple's love messages of 1907–08 in a simple letter shift.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![The message turned to reading position (work/crops/reading.png)](../work/crops/reading.png)

## Method

The solver worked from the high-resolution original of the address side, rotated it and read every word by hand from enlarged crops; no OCR was used. The key was taken as a hypothesis from the sister cards and then tested here, where it held for every enciphered word.

Two words needed most work. `ibwjoh` is partly written with a nearly dry pen and lies on the watermark. First attempts (Tennis, Dentist, a place name) were rejected, because they do not account for the final signs or for the start `ibw`, which matches `ibwf` (HAVE) on HCP 1405. `Mjuumf` was recognised from its long hooked j, its run of minims and its final f. The word after it was then read as `Tqjo`.

The reviewer rotated and enlarged the scan independently, read every line and decoded a separately typed text with its own script. The result agreed in all 16 words and 58 letters.

## Key

Caesar shift: each plaintext letter is written as the **next** letter of the alphabet, so decryption subtracts one (A→Z). This is the key of the W. Abbott family.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

`G. H. Monday.` and `Sep 30th 07.` are ordinary writing. `E-L.` (twice) and `M & L.` are abbreviations kept literal, as on the sister cards.

## Plaintext

| Ciphertext | Plaintext |
|---|---|
| G. H. Monday. | (plain) |
| Nz. Pxo. E-L. Cpz. | MY. OWN. [E-L.] BOY. |
| kvtu dpnf Cbdl. | JUST COME BACK. |
| gspn. ibwjoh. b. | FROM. HAVING. A. |
| Mjuumf. Tqjo. Nz | LITTLE. SPIN. MY |
| M & L. gspn. zpvs Pxo | [M & L.] FROM. YOUR OWN |
| E-L. Hjsm. | [E-L.] GIRL. |
| Sep 30th 07. | (plain) |

English: *"G. H. Monday. My own E. L. boy, just come back from having a little spin. My M & L from your own E. L. girl. Sep 30th 07."*

Slovak: *„G. H. Pondelok. Môj vlastný E. L. chlapec, práve som sa vrátila z malej vyjažďky. Moje M & L od tvojho vlastného E. L. dievčaťa. 30. sept. 1907."*

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1370/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the four scans, decodes the manual transcription (work/transcription.json), checks the inverse shift, counts the letters and prints the weekdays of the two candidate dates.

## Uncertainties

1. **`ibwjoh` = HAVING.** The last three signs are in very pale ink, but strokes exist for each. The left-rising hook marks the j and excludes f, so HAVE plus some other word is ruled out. A blurred grey mark may be the dot of the i; this cannot be proved.
2. **`Tqjo` = SPIN.** The q is firm: its tail turns right into the j, unlike the g of `gspn`. The first sign is a curved stroke with a short top flag, nearer this writer's C than the barred T. T is chosen because only it gives a word; the same hand has a c-curved t in `mfuufst` on HCP 1383. The words `b. mjuumf tqjo` also occur on HCP 1375, but that card leans on this one for its q, so the two are mutual support, not independent proof.
3. **`Mjuumf` = LITTLE.** Seven feet are compatible with `uum`, but they cannot be assigned letter by letter.
4. **`b.` = A.** The sign looks like a 6; it is read as the writer's tall b.
5. **Date.** The dateline reads Sep. The heading says Monday: 30 September 1907 was a Monday and 30 July 1907 a Tuesday, so the portal date 1907-07-30 is probably wrong. The postmark month is not legible and does not settle this independently.
6. **Abbreviations.** `E-L.`, `M & L.` and `G. H.` are not expanded, and their meaning is not proved. The closing group has an M with three feet, against two in both `Nz` on this card. Shifted, it would give L & K, a form reported for HCP 1395, so it may be enciphered; this card cannot decide that.
7. **Word-dots** are the writer's habit and carry no meaning.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. The reviewer ran the reproduction command, recomputed the source hashes, read every line of the rotated scan at high enlargement and decoded its own typed text with its own script. It confirmed the reading, the key and the weekday argument. Its findings and what changed:

- **Major: closing group.** First transcribed `N & L`; corrected to `M & L` on the count of feet. The group is literal, so no decoded letter changed.
- **`ibwjoh`.** The evidence was strengthened: the hook excludes f, and "no dot visible" became a possible faint dot.
- **`Tqjo`.** The q is now identified by its tail, and the c-curved t on HCP 1383 is cited.
- **"Independently attested".** Withdrawn, because HCP 1375 and this card support each other. The case rests on this card's pixels and the fixed shift.
- **Transcription details.** `E-L.` now has its dash, the doubtful dot after the second `Nz` is dropped, and the dot of `Mjuumf` is described correctly.

No decoded letter changed as a result of the review. All work on this number was done by Claude Opus 5.5.

## Sources

- HC Portal record 1370, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1370 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4170/pc_hcp_51_pic.JPG and its large conversion (source/picture-large.jpg).
- Address side: https://api.hcportal.eu/media/4171/pc_hcp_51_adr.JPG and its large conversion (source/address-large.jpg).
- Sister cards in this repository: HCP 1375, 1383, 1386, 1395, 1405.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.
