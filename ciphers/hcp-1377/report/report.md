# HCP 1377 (pc_hcp_58): a Caesar-shifted English postcard to W. Abbott

Human solver: Tomáš Pavuk

**Status: whole message read (41 of 41 enciphered letters); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1377 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1377), portal name pc_hcp_58, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-12-06, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (the catalogue's spelling), with no transcription or solution attached.

The picture side is a printed view, "Dyserth Waterfall", with no handwriting. The address side, printed "Valentine's Series", is addressed in plain writing to **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon**. It carries a halfpenny Edward VII stamp and a circular postmark reading WIMBORNE, a time line with 10, DE and a day digit that may be 5 or 6; no year is legible. The message stands on the left of the address side, turned 90° counter-clockwise.

The card belongs to a correspondence with the same recipient, hand and cipher: cards hcp-1386 to hcp-1407 in this repository, written by a woman to W. Abbott in 1907–08. On those cards the key was already known, so this card was read with a **transferred key, tested afresh**, not a new key recovery. No earlier work on this number exists in the repository, and no published solution of this card was found or used.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![Message block turned upright (work/reading.png)](../work/reading.png)

![Postmark turned upright and contrast-stretched: WIMBORNE, 10, DE and a digit that may be 5 or 6 (work/stamp_up.png)](../work/stamp_up.png)

## Method

The transcription is manual. The solver rotated the un-converted original scan, enlarged each row, and read it sign by sign, comparing doubtful signs with the same hand on hcp-1386. A shift of −1, known from the sister cards, was then tested and turned every enciphered word into English. Only some of the text is enciphered: the heading, the place name, the day and the initial groups are ordinary writing.

Alternatives tried and rejected: the first word of row 2 as `Gjlf` (FIKE) or as G plus tail, j, f (FIE); `npsspx` as `npssfpx`; final `n` of `bn` and `Gspn` as u (AT, FROT).

In review, all 26 shifts were tried on part of the text, and only −1 gave English.

## Key

Caesar substitution: each plaintext letter is written as the next letter of the alphabet, so decipherment is shift −1 (A becomes Z).

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

Square brackets mark text that is not enciphered.

| Ciphertext | Plaintext |
|---|---|
| [G. (or C.) H. Friday.] | G. (or C.) H. Friday. |
| J. bn. hpjoh up. | I. AM. GOING TO. |
| Cjlf up. [Wimborne] | BIKE TO. Wimborne |
| up. npsspx. [Sat:] | TO. MORROW. Sat: |
| Nz. [N. & L.] Gspn. Zpvs | MY. N. & L. FROM. YOUR |
| Pxo. [E. L.] Hjsm. | OWN. E. L. GIRL. |

The dots between words follow the manuscript and are not significant.

English (the original language): **"G. (or C.) H. Friday. I am going to bike to Wimborne to-morrow, Sat. My N. & L. from your own E. L. girl."**

Slovak translation: **„G. (alebo C.) H. Piatok. Zajtra, v sobotu, idem na bicykli do Wimborne. Moje N. & L. od tvojho vlastného E. L. dievčaťa."**

"N. & L." and "E. L." are left unexpanded in both versions; their meaning is not known.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1377/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the two scans and the two originals, shifts the manual transcription in work/transcription.json by −1, tests the inverse on every token, and prints the rows and the count of 41 letters. It does not read the image; the transcription step is manual and was checked independently in review.

## Uncertainties

- **`Cjlf` = BIKE is the least secure word.** The first sign is a C body. The stroke beside it could be taken for a G tail, but it is read as a separate j because the dot lies on the extension of its stem. The l is short, with a thin loop. The reading is chosen partly by sense; no other English word fits, and removing it would affect no other word.
- **`N. & L.` and `E. L.`** are kept literal, as on sister cards, and match hcp-1386 closely. Their meaning, and whether they are enciphered at all, are undecided (shifted, they would be M. & K. and D. K.).
- **Heading initial.** The sign is a C body with a short stroke below, the same construction that hcp-1386 reads as "C. H."; it differs from the G of `Gspn`. It is therefore printed "G. (or C.)". The initials are not expanded and the writer is not identified.
- **Close signs.** Final n of `bn` and `Gspn` is close to u. The v of `Zpvs` is close to an o (literal `Zpos` = YONR), but the same form occurs on hcp-1386 and YOUR is certain. The z of `Nz` is a short hooked form, as on hcp-1386.
- **Row 1 `J`** could equally be the writer's capital plain I. The plaintext is I either way, but the enciphered count would be 40.
- **Date.** The date 6 December 1907 rests on the portal. That day was a Friday, which fits the heading, but the postmark digit may be 5 or 6 and the year is illegible; 5 December 1907 was a Thursday. The reading of the message does not depend on the date.
- **People and places.** The writer's identity is not known. The link with Wimborne rests on the postmark and the clear word on the card.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, decoded the text with its own script from its own reading of the card (same plaintext, 41 letters), read every token from its own 4–8× crops, and tried to break the reading on BIKE, on the minim letters and on the date without success. It confirmed that Wimborne, Sat: and Friday are in clear. Its four findings were minor and all were accepted:

- **Heading initial.** The plaintext stated G flatly; it now reads "G. (or C.)".
- **Postmark.** The day digit is now given as 5 or 6, and the Friday heading is no longer counted as outside confirmation of the date.
- **`v` of `Zpvs`.** Now disclosed.
- **`J` of row 1.** The possible capital plain I is now disclosed.

No decoded letter changed. The reviewer could not verify the postmark's day and year, the meaning of the initial groups, or the writer's identity, and did not search separately for a published solution.

## Credits and sources

Capture, transcription, decipherment, response to review and this report: Claude Opus 5.5, 2026-10-30, with a separate Claude Opus 5.5 agent as reviewer. The key was first found on sister cards of the correspondence.

- HC Portal record 1377, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1377 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4191/conversions/pc_hcp_58_pic-large.jpg and original https://api.hcportal.eu/media/4191/pc_hcp_58_pic.JPG
- Address side: https://api.hcportal.eu/media/4192/conversions/pc_hcp_58_adr-large.jpg and original https://api.hcportal.eu/media/4192/pc_hcp_58_adr.JPG
- Sister cards in this repository, chiefly ciphers/hcp-1386.
