# HCP 1362 (pc_hcp_43): a Caesar-shifted English love postcard to W. Abbott

Human solver: Tomáš Pavuk

**Status: deciphered in full (53 of 53 enciphered letters); independent review 1 verdict ACCEPT, no word changed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1362 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1362), portal name pc_hcp_43, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date Unknown, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (the catalogue's spelling), with no transcription or solution attached.

The picture side is a printed Frith's Series view with the caption "Raglan Castle"; it has no handwriting. The address side is plain: **Mr W. Abbott, Stokelake Farm, Chudleigh, Devon.** It carries a halfpenny Edward VII stamp. The postmark shows BORNE (the end of an office name; sister cards show WIMBORNE), 10 PM, day 10, a faint AP left of the stamp edge, and 07 below it.

The message runs up the left half of the address side, so the card must be turned 90° counter-clockwise to read it. The grey wheel across the scan is the portal's watermark, not part of the card.

The card belongs to a correspondence of Caesar-shifted English postcards to W. Abbott from about 1907–08, several of which are finished in this repository (HCP 1386–1407). The key was therefore **transferred from those cards**, not recovered blind from this one. All the work on this card was done by Claude Opus 5.5 on 2026-10-30.

![Picture side, Raglan Castle (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![Address side turned so that the message is upright (work/crops/all.png)](../work/crops/all.png)

## Method

The transcription is **manual**. The solver rotated the full-resolution original (work/hires/pc_hcp_43_adr.JPG), read every word from enlarged crops, and recorded the result in work/transcription.json. Sign shapes were read first. Two first readings were dropped on the shapes before handover: line 2 as `Njdf wfsz` (NICE VERY) and line 3 as `Uipvtf` (HOUSE). No key was tuned to the card: one fixed shift decodes all of it.

In review, a separate agent made its own crops, typed its own transcription, and decoded it with its own script. It got the same 53 letters, and of the 26 possible shifts only this one gives English.

## Key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet, so decryption subtracts one (A→Z). The closing "G. H. April 10th" is ordinary writing.

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

```text
Ciphertext             Plaintext
Nz. Efbsftu J ibwf     MY. DEAREST I HAVE
pof. Mjlf. uijt        ONE. LIKE. THIS
Mpwf boe. Ljttft.      LOVE AND. KISSES.
gspn. Zpvs. pxo.       FROM. YOUR. OWN.
Hjsm.                  GIRL.
(plain) G. H. April 10th
```

These are all the enciphered letters on the card: 53, with no abbreviation groups. The writer's dots are a habit, placed irregularly, and carry no meaning.

English (the plaintext language): **My dearest, I have one like this. Love and kisses from your own girl. G. H., April 10th.**

Slovak translation: **Môj najdrahší, mám jednu takúto. Láska a bozky od tvojho vlastného dievčaťa. G. H., 10. apríla.**

"One like this" presumably means another card of the same view; the card does not say so.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1362/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of both scans in source/ and both originals in work/hires/, decodes work/transcription.json with the shift, re-encodes each word as a round-trip check, and prints the plaintext and "53 enciphered letters decoded by one key". It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **`Mjlf`, capital.** The least clean sign on the card, crossed by the watermark. At 10× it has three elements, against two in the N of `Nz`, so the shape leans to M; the third element is faint, so N (giving MIKE) is unlikely rather than excluded. The third sign is a plain stem with a foot, read `l`, not `d`.
- **`uijt`, first signs.** Pale and partly under the watermark. The reading rests on two dots above the word, the long j and the final barred t, whose crossbar runs to the card edge.
- **`Efbsftu`, fourth sign.** A blot. Read `s` because the other six signs are clear, a top curl remains, and the word is this writer's usual greeting. This is a restoration, not an independent reading.
- **`boe`, last sign.** Its loop is filled with ink, so it looks c-shaped. The notes on sister card HCP 1363 record a c-shaped e for this hand.
- **`Ljttft`, last two signs.** Very pale, with the pen running dry, but legible.
- **Year.** The handwriting gives no year. 1907 rests on the postmark (a faint 0 and a plain 7) and on the same-day card HCP 1397, which is dated in clear "April 10th 1907" and opens with the same `Nz. Efbsftu`. 10 April 1907 was a Wednesday.
- **`G. H.`** is left unexpanded. The G could be taken for a C, and sister card HCP 1386 reads C there; a second stroke at the foot of the capital favours G on this card. The sender's identity is not established.
- **Prior publication.** The portal lists no solution, and the AI Decipherment Register had no record of this card on 2026-10-30. The reviewer did not search further afield.

## Review summary

Reviewer: Claude Opus 5.5, a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, decoded its own transcription, and read every word at 3× to 10× from its own crops of the original. It also checked the disclosed sign points, the address, the postmark and the date, and found no other handwriting on either side. Its four findings were minor and changed no word:

- **`Mjlf` capital.** The shape evidence was understated; the uncertainty now says the shape leans to M.
- **Postmark month.** The solver had said the month was not visible. A faint AP is there, so the month is supported independently of the handwriting.
- **Same-day card.** HCP 1397 is now cited as evidence for the year.
- **Status count.** The summary said three sign points where five are listed; corrected.

## Sources

- HC Portal record 1362, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1362 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4146/pc_hcp_43_pic.JPG
- Address side: https://api.hcportal.eu/media/4147/pc_hcp_43_adr.JPG
- Sister cards in this repository: HCP 1386–1407 (key), HCP 1397 (same-day card), HCP 1366 (comparison of `Mpwf`), HCP 1363 (the c-shaped e).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.
