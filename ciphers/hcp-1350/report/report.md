# HCP 1350 (pc_hcp_31): a Caesar-enciphered love postcard from Loo to W. Abbott, 7 March 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (78 of 78 cipher letters); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1350 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1350), portal name pc_hcp_31, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-03-07, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (the catalogue's spelling of Abbott), with no transcription or solution attached.

The picture side is a printed colour view, "Weymouth, view from Sandsfoot Castle", with no handwriting. The address side is a Frith's Series card, No. 52870, with a halfpenny Edward VII stamp. The address is in clear: **Mr W. Abbott, Stokelake Farm, Chudleigh, Devon**. The postmark shows 10 PM, MR 7, 07. Of the town only WIM and traces under the stamp design can be read; WIMBORNE is taken from the same postmark form on cards HCP 1353 and 1354. A pencil "4" at the top left is presumably a collector's mark and is not part of the message.

The cipher text fills the left half of the address side and is read with the card turned 90° counter-clockwise. It ends with a plain date, **Thursday. March. 7th**. 7 March 1907 was a Thursday, the day of the postmark. The grey A–Z disc and building logo on the scans are an overlay added to the scan and are not part of the card.

The card belongs to a correspondence of Caesar-enciphered English postcards from one couple in 1907–08. Several are deciphered in this repository. The closest are HCP 1353 and 1354 (same weeks, same signature) and HCP 1398, which has the same opening.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![The message turned to reading position (work/reading.jpg)](../work/reading.jpg)

## Method

The transcription is **manual**. The solver worked from the un-converted original scan of the address side, turned it to reading position and read each row from enlarged crops. No OCR was used and the portal supplied no transcription.

Hand, recipient and signature pointed to the Abbott correspondence, so the shift already established there was tried first. It read all six rows directly. Cards of the same correspondence served as a source of hypotheses only; each word was read on this card. Three alternatives were settled before handover by rereading the shapes:

- The signature was first read `Npf` or `Npp` (MOE, MOO). Its last sign is an open-bowl p, and the capital has three downstrokes, so it is M.
- The word `mpwjoh` was first transcribed `npwjoh`. The decoder printed MOVING, and a stroke count showed three downstrokes against two in n and N.
- `Cpui` was tested as `Epui` (DOTH), which gives no sense here.

All the work on this card was done on 2026-10-30 by Claude Opus 5.5 as solver. There is no earlier work on this number.

## Key

Caesar substitution: each plaintext letter is written as the **next** letter of the alphabet, so decryption is a shift of −1. The date is in clear.

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The single shift has nothing to tune, and it covers every letter of the transcription. Shifts 0, +2 and −2 give no text.

## Plaintext

The dots follow the manuscript and are not significant.

| Ciphertext | Literal plaintext |
|---|---|
| Nz. pxo. efbstu. Cpz. | My. own. dearst. Boy. |
| xibu bo. vofyqfdufe | what an. unexpected |
| Tvsqsjtf. uijt | Surprise. this |
| npsojoh. Cpui | morning. Both |
| wfsz. ojdf. Zpvs. | very. nice. Your. |
| mpwjoh. hjsm. Mpp | loving. girl. Loo |
| (in clear) Thursday. March. 7th | |

English (the original language; punctuation editorial): **My own dear[e]st boy, what an unexpected surprise this morning. Both very nice. Your loving girl, Loo. Thursday, March 7th.**

Slovak translation: **Môj vlastný najdrahší chlapče, aké nečakané prekvapenie dnes ráno. Obidve veľmi pekné. Tvoje milujúce dievča, Loo. Štvrtok, 7. marca.**

Notes on the reading:

- **dearst.** The card has `efbstu`, six letters, with no f between s and t. The E is an editorial restoration. HCP 1398 has the identical opening `Nz. pxo. efbstu Cpz.`, while HCP 1356 writes `Efbsftu` in full, so this may be a habit of the writer as much as a slip.
- **Both very nice** is not explained on the card. It presumably refers to two things received that morning.
- The last e of `vofyqfdufe` is raised above the line for lack of room at the card edge.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1350/work/decode.py
```

The script checks the SHA-256 hashes of the four image files, decodes the manual transcription in work/transcription.txt with the shift, tests the round trip, and prints each row, the count of 78 letters and the plaintext. It does not read the image; the transcription step is manual and was checked independently in review.

## Uncertainties

- **The t of `Tvsqsjtf`** is the one sign on the card read from the word and not from its shape. It has a 3-shaped head and a long tail curling left below the line. It is not this writer's z, since all four z on the card are flat-topped. HCP 1353 has the same word with the same tail and foot but a barred head, so that parallel covers only the lower half of the sign. Taken as cipher z the word would be SURPRIYE. The sense SURPRISE is not in doubt.
- **Two irregular signs.** The x of `pxo` is Y-shaped with a foot and merging strokes, unlike the open crossed x of `xibu`. The w of `wfsz` opens with a tall stem and could be taken for a b at first sight. Only OWN and VERY make sense.
- **The capital of `Cpui`** has a curled head. Taken as E the word would be DOTH, which gives no sense here.
- **The signature `Mpp`.** The capital has three downstrokes against two in N and n, but the strokes are close together, so this rests on a small difference. `Mpp` is also the signature read on HCP 1353, 1354 and 1398. That Loo is a pet name is conjecture.
- **Ligatured signs.** The first sign of `vofyqfdufe` and the d of `ojdf` are somewhat ligatured, but no alternative gives a word.
- **The postmark town** is partly inferred, as stated above.
- **The writer's identity and sex** come only from the formula "your loving girl". Weymouth on the picture has no stated connection with the Wimborne postmark.
- No published solution of this card was found. The portal shows Not solved with nothing attached, and the AI Decipherment Register had no record for it when checked on 2026-10-30.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic, a separate agent), round 1, verdict **ACCEPT**. The solver was also Claude Opus 5.5, so this was not a cross-vendor check. The reviewer ran the reproduction command, decrypted with its own script (same six rows and 78 letters), and read the whole message sign by sign on its own 4× to 7× crops of the hi-res scan. It confirmed the six signs of `efbstu`, the stroke count of the capital of `Mpp`, the weekday, and the absence of writing on the picture side. It could not verify the live portal page and relied on the capture. It raised five minor findings, all accepted:

1. **The t of `Tvsqsjtf`.** The earlier description as a tailed cursive z was withdrawn, and the HCP 1353 parallel was limited to the lower half of the sign.
2. **Two irregular signs** (the x of `pxo`, the w of `wfsz`) were undisclosed and are now listed.
3. **`efbstu`.** HCP 1398 is now cited, "slip" is no longer asserted, and the English marks dear[e]st.
4. **Postmark.** The town is now stated as partly inferred from sister cards.
5. **Count of uncertainties.** The status line and the list now agree.

No decoded letter changed as a result of the review; the changes concern disclosure only.

## Sources

- HC Portal record 1350, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1350 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4110/conversions/pc_hcp_31_pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/4110/pc_hcp_31_pic.JPG (work/hires/).
- Address side: https://api.hcportal.eu/media/4111/conversions/pc_hcp_31_adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/4111/pc_hcp_31_adr.JPG (work/hires/).
- Sister cards in this repository: ciphers/hcp-1353, hcp-1354, hcp-1356 and hcp-1398.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.
