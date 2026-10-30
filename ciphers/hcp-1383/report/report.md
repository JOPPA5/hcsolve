# HCP 1383 (pc_hcp_64): an English Caesar sweetheart postcard, Bournemouth, 23 September 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (73 of 73 enciphered letters); two kinds of abbreviation group (`E. L.`, `M-L.`) kept literal. Independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30 (UTC).

## Origin and context

The cryptogram is record 1383 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1383), portal name pc_hcp_64, part of the HCPortal collection of cryptographic postcards. When captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and HCPortal collection, category Substitution, date 1907-09-23, language Unknown (the plaintext is English), recipient "W. Abboú" (a catalogue spelling of Abbott). No transcription or solution was attached.

The card is a Max Ettlinger "Royal Series" postcard, Bournemouth Series 1089, with a printed woodland picture and no handwriting on the picture side. The address side has a green halfpenny Edward VII stamp and the postmark BOURNEMOUTH 8 PM SP 23 07. The plain address reads **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon**. The message runs sideways along the left half of the address side, so the scan must be turned 90° counter-clockwise.

Two parts of the message are in ordinary writing: the heading **1 Cleveland Rd** and the date **Monday Sep 23rd 07**. 23 September 1907 was indeed a Monday, and the date agrees with the postmark and the portal.

The card belongs to a correspondence of cipher postcards to W. Abbott from a young woman who signs "your own E. L. girl". Several of these are deciphered in this repository (for example HCP 1386 and 1403). HCP 1381 and 1382 are further Bournemouth cards from the same week.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side turned 90 degrees counter-clockwise (work/address-rotated.png)](../work/address-rotated.png)

## Method

The solver turned the high-resolution address side upright and read every word by hand from enlarged crops; no OCR was used. The key was taken as a hypothesis from the sister cards HCP 1386–1407 and then tested on this card, where it held for every enciphered word. The transcription is in work/transcription.json.

Hard places were decided by comparing shapes on this card. The sign after the date looks like a time, "4/5 m", but it is the cipher word `Hjsm` = GIRL, the last word of the closing formula. The sign in `Pxo` looked like i plus a flourish, but it is a capital P with a thin dry connecting stroke. The initial of `M-L.` has three downstrokes against two in the N of `Nz`, so it is M.

The reviewer read the card independently and decoded a separately typed text with its own script. The result agreed in all 19 words and 73 letters.

## Key

Caesar shift: each cipher letter stands one place after its plaintext letter, so deciphering moves each letter back by one.

```text
cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

Square brackets mark groups kept literal. Dots and dashes are the writer's.

| Ciphertext | Plaintext |
|---|---|
| Nz. Pxo. [E. L.] Cpz. | MY. OWN. [E. L.] BOY. |
| kvtu dpnf. cbdl. | JUST COME. BACK. |
| J. gpvoe. mfuufst | I. FOUND. LETTERS |
| Xbjujoh. ifsf. gps | WAITING. HERE. FOR |
| pof. xffl. pomz. | ONE. WEEK. ONLY. |
| [M-L.] gspn zpvs Pxo [E-L.] | [M-L.] FROM YOUR OWN [E-L.] |
| Hjsm (written after the plain date) | GIRL |

English, with editorial sentence division: **My own E. L. boy, just come back. I found letters waiting. Here for one week only. M-L. from your own E. L. girl.**

Slovak translation: **Môj vlastný E. L. chlapec, práve som sa vrátila. Našla som čakajúce listy. Tu som iba na jeden týždeň. M-L. od tvojho vlastného E. L. dievčaťa.**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1383/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the four scans, confirms that 23 September 1907 was a Monday, decodes the manual transcription and prints each line with the count: 73 shifted letters and 6 literal letters. It does not read the image; the transcription step is manual and was checked independently in review.

## Uncertainties

- **`E. L.` (twice) and `M-L.`** are unexpanded abbreviations, kept literal as on the sister cards. Their meaning is unknown. Shifted, they would give D. K. and L-K. The second is the group HCP 1395 reads as `L. & K.`, so `M-L.` may be enciphered. This card cannot decide that.
- **First letter of `M-L.`** Read as M from its three downstrokes. Sister cards have an N in the same place, so an N/M doubt remains there. The joining sign is a plain dash.
- **Sentence division.** The writer puts a dot after nearly every word, so the dots do not mark sentences. "Here for one week only" is taken as the writer's own stay, which is the natural sense on a holiday card. The alternatives are "I found letters waiting here. For one week only" and a literal run-on, in which the letters had waited a week. The dates give only weak support: Bournemouth postmarks on 23, 24 and 26 September, then a WIMBORNE postmark on day 30 of an illegible month (HCP 1370). The heading G. H. on that card also occurs on HCP 1382 with a Bournemouth postmark. These sister cards are themselves not yet closed.
- **Final t of `mfuufst`.** It is shaped like a c with a top stroke. A cipher c would give LETTERB, which is not a word.
- **`Pxo` and `E-L.`** Parts of these signs are dry pen strokes: the link in the P, and the ascender of the last L. The L of `E. L.` is less clean than the L of `M-L.`. No meaning depends on them.
- **`Hjsm` after the date.** Its position is unusual, but the formula otherwise lacks its last word, and the word has the writer's long hooked j.
- **Unverified points.** The capital J of `J.` was not compared sign by sign with a sister card; it is a one-letter word and I is the only sensible value. "1 Cleveland Rd" was not looked up as a real Bournemouth address; it is plain text and does not affect the reading.
- **Prior publication.** The portal status is Not solved, with no attachment, and the AI Decipherment Register had no record of this number on 2026-10-30. No wider search was made.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, recomputed the source hashes, rotated and enlarged the scan, read every word itself and decoded its own typed text with its own script. It agreed on all 19 words and 73 letters, and confirmed the heading, date, postmark and address. Its three minor findings were addressed:

- **Sentence division.** The first translation ran "I found letters waiting here for one week only". It now divides the sentence and takes the phrase as the writer's stay. The solver checked the date argument offered for this and recorded that it is weak, because of the illegible month and the G. H. heading noted above.
- **Word count.** The solution said 16 enciphered words; it now says 19.
- **Citation.** The hooked-slash j is now cited to HCP 1386 instead of HCP 1398.

No decoded letter changed as a result of the review. All work on this number was done by Claude Opus 5.5.

## Sources

- HC Portal record 1383, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1383 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4209/pc_hcp_64_pic.JPG and its large conversion (source/picture-large.jpg).
- Address side: https://api.hcportal.eu/media/4210/pc_hcp_64_adr.JPG and its large conversion (source/address-large.jpg).
- Sister cards in this repository: HCP 1370, 1381, 1382, 1386, 1395, 1403.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.
