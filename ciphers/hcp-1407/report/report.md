# HCP 1407 (pc_hcp_88): an English Caesar sweetheart postcard, 14 May 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (49 of 49 enciphered letters). Two short initial groups in the closing are kept literal. Independent review 1 verdict ACCEPT; no decoded letter changed.** Report dated 2026-10-30 (UTC).

## Origin and context

The cryptogram is record 1407 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1407), portal name pc_hcp_88. It is part of the HCPortal collection of cryptographic postcards (private collection). When the card was captured on 2026-10-26, the portal listed it as follows:

- status **Not solved**;
- tags Postcard and HCPortal collection;
- category Substitution;
- date 1907-05-14;
- language Unknown, location Europe;
- sender Unknown, recipient "W. Abboú".

No transcription or solution was attached.

The picture side is a printed Tuck's "Oilette" card from the Dartmoor series II, *The River Lyd*. It carries no handwriting.

The address side has a halfpenny Edward VII stamp. The postmark reads **WIMBO[RNE] / 6.30 PM / MY / 07**; the day digits lie mostly under the stamp edge and cannot be read on their own. The address is written in plain to **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon**. The portal's "Abboú" is a misreading of Abbott.

The short message stands sideways on the address side; turn the scan 90° counter-clockwise to read it. It has two plain-written parts:

- a heading, **"G. H. Tuesday."**;
- a dated foot, **"May. 14th 1907."**

14 May 1907 was indeed a Tuesday.

The card belongs to a group of Caesar-shifted English cards from one couple in 1907–08 (HC Portal 1386–1407). All of them go to W. Abbott at Stokelake Farm and use the same key and the same formulae: "My own …", "to-day", and "from your own … girl". Several of these cards are deciphered in this repository, among them 1386, 1397, 1399, 1403 and 1406.

![Picture side (source/picture.jpg)](../source/picture.jpg)

![Address side as scanned: stamp, WIMBORNE postmark, address to Mr W. Abbott, Stokelake Farm, Chudleigh, and the message written sideways (source/address.jpg)](../source/address.jpg)

![The message turned upright (work/reading.jpg)](../work/reading.jpg)

## Method

The transcription is manual; no OCR was used.

An earlier OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol, 2026-10-26) did the first stage:

- captured all three portal tabs and both scans;
- identified the Caesar shift;
- transcribed the 49 cipher letters.

That solver resolved the group `up-Ebz` as TO-DAY by comparing it with the same group on the sister card HCP 1406. This was an internal handwriting comparison; no published solution was used.

Claude Opus 5.5 (2026-10-29) did the second stage:

- re-checked every sign on 2–5× enlargements;
- read the postmark;
- classified the two closing initial groups as literal, following the convention of the sister cards;
- wrote the final transcription (work/transcription-v2.json) and decoder (work/solve.py).

The key was found from whole words. Moving every letter back one place turns `uibolt` into THANKS, `gspn zpvs` into FROM YOUR and `Hjsm` into GIRL. The same shift then decodes every other word.

In review, a separate Claude Opus 5.5 agent worked independently:

- cropped the scan itself;
- transcribed the five cipher rows without using the solver's files;
- decoded them with its own script.

Its 49 letters agreed with the solver's reading letter for letter.

## Key

The cipher is a Caesar shift: each plaintext letter is written as the **next** letter of the alphabet. To decrypt, move back one (A→Z).

| Cipher | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z |
|---|---|
| Plain | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y |

The heading, the date and the address are in plain writing.

## Plaintext

| Line | Ciphertext (as written) | Literal decode |
|---|---|---|
| heading (plain) | G. H. Tuesday. | G. H. Tuesday. |
| 1 | Nz. Pxo. Efbsftu. | MY. OWN. DEAREST. |
| 2 | Nboz. uibolt. gps | MANY. THANKS. FOR |
| 3 | dbse: up-Ebz. | CARD: TO-DAY. |
| 4 | M. & L.' gspn. zpvs | [M. & L.'] FROM. YOUR |
| 5 | Pxo. N.-1 Hjsm | OWN. [N.-1] GIRL |
| date (plain) | May. 14th 1907. | May 14th 1907. |

All 49 enciphered letters are decoded by the one key. The bracketed groups are initials or abbreviations kept as written.

English: **G. H. Tuesday. My own dearest, many thanks for card to-day. [M. & L.] from your own [N.-1] girl. May 14th 1907.**

Slovak: **G. H. Utorok. Môj najdrahší, veľká vďaka za dnešnú pohľadnicu. [M. & L.] od tvojho vlastného [N.-1] dievčaťa. 14. mája 1907.**

Notes on the reading:

- **Dots are not significant.** The writer puts a dot after nearly every word.
- **"My own …" and "from your own … girl"** are the couple's regular opening and closing, as on the sister cards.
- **`up-Ebz`** (TO-DAY) is written with a hyphen, as on HCP 1386, 1397 and 1406.

## Reproduction

Run from the repository root:

```sh
python3 -I ciphers/hcp-1407/work/solve.py
```

The script first checks the SHA-256 hashes of the files in source/. It then decodes the manual transcription in work/transcription-v2.json with the key above and prints the seven lines, ending with `49 enciphered letters decoded; [..] = initial groups kept literal`. It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

1. **The group before FROM, `M. & L.'`** (line 4).
   - The first capital has two arches, so it is read as M; N is not fully excluded (HCP 1399 reads the same group with N).
   - Then come a reversed-c ampersand, a capital L, and a small raised tick, possibly a reduced t.
   - Shifted, the group would give "L. & K.", which explains nothing. An expansion such as "much love & kisses" is plausible but **not claimed**.
2. **The group between OWN and GIRL, `N.-1`** (line 5).
   - Best described neutrally as a capital N or M with a short dash and a raised tick.
   - The tick may be the same reduced mark as after the L in line 4, so a reading "No. 1" ("your own No. 1 girl") is weak.
   - The group is kept literal.
3. **`uibolt` (THANKS).** The final t is only a short hook after the l, with no visible cross-bar. The same word occurs on sister cards.
4. **`up-Ebz` (TO-DAY).** The cursive b and z look like the digits 6 and 2. They are read as letters because:
   - the same E, b and z forms occur elsewhere on this card;
   - the identical group occurs on HCP 1386, 1397 and 1406.
5. **`dbse` (CARD).** The final e has a trailing flourish; only CARD makes sense.
6. **Context readings.** The heading initials "G. H." are not identified. The farm name Stokelake is read from the address and agrees with the sister cards. The postmark day is not independently legible. The date rests on three things:
   - the written foot date;
   - the Tuesday heading;
   - the portal date.

None of these points affects the key or any decoded word.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent (Anthropic), round 1, verdict **ACCEPT**.

The reviewer did the following:

- ran the reproduction command; its output matched the claimed plaintext;
- transcribed the card independently from its own 3–5× crops and decoded it with its own script; its reading agreed in all 49 letters;
- confirmed that every alphabetic sign is decoded, in plain writing, or one of the two disclosed initial groups;
- confirmed that 14 May 1907 was a Tuesday;
- confirmed that no published solution was used.

It made three minor findings, all accepted:

- **Closing initial groups.** The line-5 group is now described neutrally ("N/M with a raised tick"), and the gloss "No. 1" is called weak.
- **Farm name.** The address word, earlier left as "uncertain", is now read as **Stokelake**, as on the sister cards.
- **Postmark day.** The postmark is no longer cited as an independent witness for the day 14.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1407, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1407 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4281/conversions/pc_hcp_88_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4282/conversions/pc_hcp_88_adr-large.jpg (source/address.jpg).
- Sister cards HCP 1386–1406 in this repository, used for handwriting comparison only (notably HCP 1406 for `up-Ebz`).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no record for this card.
