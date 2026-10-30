# HCP 1382 (pc_hcp_63): an English Caesar love postcard, Bournemouth, 24 September 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (40 of 40 enciphered letters, one key); two abbreviation groups (`M-L.`, `E.L.`) kept literal; one plain word ("Dear") only probable. Independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30 (UTC).

## Origin and context

The cryptogram is record 1382 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1382), portal name pc_hcp_63, part of the HCPortal collection of cryptographic postcards. When captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and HCPortal collection, category Substitution, date 1907-09-24, language Unknown (the text is English), sender Unknown, recipient "W. Abboú" (a catalogue spelling of Abbott). No transcription or solution was attached.

The picture side is a printed view, "Christchurch Priory. Norman Turret.", no. 23241. It carries no handwriting. A small dark mark in the sky at the lower left (a blob, two rings and short strokes) looks like set-off from a postmark and holds no message text; its origin is not proved.

The address side has a halfpenny Edward VII stamp and the postmark BOURNEMOUTH SP 24 07, with an hour consistent with 12.45 PM. The plain address reads **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon**. Christchurch lies next to Bournemouth, so the view fits the postmark. The message runs sideways along the left half of the address side, so the scan must be turned 90° counter-clockwise. The circular A–Z disc on the scans is an overlay, not part of the card.

The card belongs to a run of cards to W. Abbott that share the same key and closing formula. The closest is HCP 1383, written the day before from the same town. Other sisters are HCP 1381, 1386, 1387 and 1402. The same words on those cards were treated as hypotheses only, and each word here was read on this card's own pixels.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![Message turned 90 degrees counter-clockwise (work/crops/rot.png)](../work/crops/rot.png)

## Method

The transcription is **manual**. The solver turned the original high-resolution scan (not the portal's smaller conversion) by 90°, flattened the overlay by dividing each pixel by a local background, and read eight rows from enlarged crops. No OCR was used and the portal supplied no transcription.

The first half of the message is in plain English: "I am enjoying myself Dear". The rest looked like letter groups with no sense. The key step was row 4: `pomz` shifted back one letter gives ONLY, the word already known from HCP 1383. The repeated f-s-f of row 5 then gave `Xfsf Ifsf` = WERE HERE, followed by `Xjti zpv` = WISH YOU and `bt Xfmm` = AS WELL. Two first readings were dropped on the enlargements: the long stroke at the start of row 4 is the stem of the p, not a separate letter, and the three X's are capitals, not kiss marks.

## Key

Caesar shift: each plaintext letter is written as the next letter of the alphabet (decrypt −1, with A going back to Z). Case and dots are kept. There are no exceptions among the 40 enciphered letters.

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

| Row | On the card | Reading | Kind |
|---|---|---|---|
| 1 | Tues. Morning G. H. | Tues. Morning G. H. | plain |
| 2 | I am enjoying | I am enjoying | plain |
| 3 | myself Dear[?] | myself Dear[?] | plain |
| 4 | pomz. Xjti zpv. | only. Wish you. | cipher |
| 5 | Xfsf Ifsf. bt. | Were Here. as. | cipher |
| 6 | Xfmm. M-L. Gspn | Well. M-L. From | cipher, `M-L.` literal |
| 7 | Zpvs Pxo E.L. Hjsm | Your Own E.L. Girl | cipher, `E.L.` literal |
| 8 | 24th Sep 07 | 24th Sep 07 | plain |

The dots are the writer's and often fall mid-sentence. The punctuation below is editorial.

English (the original language): **"Tuesday morning. G. H. I am enjoying myself, Dear [probable]. Only wish you were here as well. M-L. From your own E.L. girl. 24th Sep 07."**

Slovak translation: **„Utorok ráno. G. H. Dobre sa bavím, drahý [pravdepodobné]. Len by som si želala, aby si tu bol aj ty. M-L. Od tvojho vlastného E.L. dievčaťa. 24. sept. 07."**

## Why the reading is correct

- One fixed shift turns all 40 enciphered letters into ordinary English.
- The plain opening and the cipher run on as one sentence: "I am enjoying myself … only wish you were here as well". This fits a holiday card.
- `Xjti zpv Xfsf Ifsf bt Xfmm` was not expected in advance. It came from the letter shapes, and the repeated f-s-f and the double m agree with it.
- `pomz` occurs on HCP 1383, and `Zpvs Pxo … Hjsm` on HCP 1381 and 1386, with the same values.
- 24 September 1907 was a Tuesday, which matches "Tues." and the postmark date.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1382/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the four image files, decodes the manual transcription with shift −1, keeps the plain parts and the two abbreviations literal, prints the text and the count of 40 enciphered letters, and confirms the weekday. It does not read the images; the transcription step is manual and was checked independently in review.

## Uncertainties

- **"Dear" (row 3, plain writing, not enciphered).** It is faint and crossed by the overlay. A large initial, about three low letters and a tail are visible, with no ascender. D-e-a-r fits and the enciphered form `Efbs` does not, but the pixels alone do not prove it. It is probable, not certain.
- **`M-L.` and `E.L.`** are kept literal and their meaning is not established. It is open whether either is enciphered. `M-L.` shifted gives L-K, and HCP 1395 reads `M. & L.` as `L. & K.`, probably "love & kisses". That would fit here before "from", but it is not proved on this card, and the joining sign here is a dash. `E.L.` shifted gives D.K, and the sister form `E.h` gives D.g; neither means anything evident. The first sign of `M-L.` has three feet, so M; its top is tangled with the descender of the f above, so N is not wholly excluded. The second letter of `E.L.` could be an h, as recorded on HCP 1387; L and h cannot be separated here.
- **Letters under the overlay.** The z of `zpv.` lies under the printed R and the band. Its shape supports z, with the two strokes of its top and foot visible; the sense "you" is a separate argument. The z of `pomz` lies on the band but is clear.
- **The i of `Xjti`** is a low hump. The small heavy mark above it stands where its dot belongs and is probably that dot.
- **"G. H."** in row 1 is flourished plain writing. It matches the heading on the sister cards, but G and C cannot be separated here.
- **The postmark hour** is consistent with 12.45 PM; the minute is not certain.
- **Identities.** The writer is known only as "your own E.L. girl". Neither she nor the meaning of "G. H." is established.
- No search for a prior publication of this card was made beyond the portal status (Not solved) and the AI Decipherment Register (no record for this number on 2026-10-30).

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command and recomputed the hashes, made its own overlay filter and 3–7× crops, read all eight rows sign by sign, and decoded its own transcription with its own script. It confirmed 40 enciphered letters, the weekday, the postmark and the sister-card groups, and found no sign of a published solution being used. Its own text differed from the solver's in two places only, the first two findings below.

All five findings were minor. Each was rechecked on the scan and accepted:

- **`N-L.` became `M-L.`** The first sign has three feet, the form read on HCP 1383. Neither form is deciphered, so no sense changes.
- **A dot was added after `Ifsf`.** Row 5 is now `Xfsf Ifsf. bt.`.
- **The address now reads S. Devon.**
- **The picture-side mark is now stated** and set aside as probable postmark set-off.
- **Wording.** The shape evidence for the z of `zpv` is now kept apart from the sense argument, and the report says it is open whether the two abbreviations are enciphered. The pointer to HCP 1395 was added by the solver when closing the card, after the review.

No deciphered letter changed. All work on this number, including transcription, decipherment and review, was done by Claude Opus 5.5 on 2026-10-30; there was no earlier work.

## Sources

- HC Portal record 1382, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1382 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4206/conversions/pc_hcp_63_pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/4206/pc_hcp_63_pic.JPG (work/hires/).
- Address side: https://api.hcportal.eu/media/4207/conversions/pc_hcp_63_adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/4207/pc_hcp_63_adr.JPG (work/hires/).
- Sister cards in this repository: ciphers/hcp-1381, hcp-1383, hcp-1386, hcp-1387, hcp-1402.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.
