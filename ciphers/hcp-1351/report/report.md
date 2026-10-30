# HCP 1351 (pc_hcp_32): an English love postcard from Loo, Wimborne 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (70 of 70 cipher letters; 69 read on form, 1 on form plus context); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1351 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1351), portal name pc_hcp_32, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-02-16, language Unknown, location Europe, sender Unknown, recipient W. Abbott (catalogue spelling "W. Abboú"), with no transcription or solution attached.

The picture side shows the interior of Wimborne Minster, with the printed caption "Wimborne Minster, Nave East" and no handwriting. The address side is a Frith's Series card (F. Frith & Co. Ltd., Reigate, No. 43708) with a halfpenny Edward VII stamp and a postmark reading (WIM)BORNE, 1 PM, FE 16, 07. That agrees with the portal date, 16 February 1907, which was a Saturday, as the plain heading on the card says. The card is addressed to Mr W. Abbott, Stokelake Farm, Chudleigh, Devon.

The card belongs to a correspondence between a couple, addressed to W. Abbott, in which the woman signs herself Loo. Several cards of the same group are deciphered in this repository (for example HCP 1350, 1352 and 1386 to 1407). The shift used here and the recurring groups `Nz` = MY, `Hjsm` = GIRL and `Mpp` = LOO were taken from those cards as a hypothesis and then tested on this one. This is therefore a **known cipher applied to a new card**, not a blind key recovery. No published solution of this card was found or used.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg). The grey disc and building logo are a scanner overlay, not part of the card](../source/address-large.jpg)

Other marks, none of them cipher: the plain heading, the address, the printed text, the stamp and postmark, and a pencil "3" at the top left of the address side, which is not in the writer's ink and is treated as a later or sequence mark.

## Method

The transcription is **manual**. The solver turned the high-resolution original of the address side (work/hires/pc_hcp_32_adr.JPG) 90° anticlockwise and read the six lines of the message sign by sign from enlarged crops. No OCR was used and the portal supplied no transcription. Caesar −1 from the sister cards was then tried and gave English on all six lines. Doubtful signs were compared with other occurrences of the same shapes on this card.

The reviewer made its own crops at 4 to 8 times enlargement, read the card independently and decoded it with its own script. Its 70 letters are identical to the solver's.

![The message turned upright (work/crops/reading.png)](../work/crops/reading.png)

## Key

Monoalphabetic Caesar shift: each plaintext letter is written as the next letter of the alphabet, so decryption subtracts one.

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

| Ciphertext | Plaintext |
|---|---|
| G. H. Saturday (plain, underlined) | G. H. Saturday |
| Nz. Efbsftu Cpz. | MY. DEAREST BOY. |
| uxfmwf. Xfflt. up ebz. | TWELVE. WEEKS. TO DAY. |
| uijoht. Xjmm. Cf. | THINGS. WILL. BE. |
| Mppljoh. Vq. | LOOKING. UP. |
| Gspn. Zpvs. Mpwjoh. | FROM. YOUR. LOVING. |
| Hjsm. Mpp. | GIRL. LOO. |

The dots after words are the writer's habit and are not significant. The plaintext language is English; the portal lists it as Unknown.

English: **G. H. Saturday. My dearest Boy, twelve weeks to-day things will be looking up. From your loving Girl, Loo.**

Slovak translation: **G. H. sobota. Môj najdrahší chlapče, o dvanásť týždňov odo dneška sa veci obrátia k lepšiemu. Od tvojho milujúceho dievčaťa, Loo.**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1351/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the two scans in source/ and the two originals in work/hires/, decodes the manual transcription in work/transcription.json, checks the inverse round trip and prints the six lines with the count of 70 letters. It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **Second sign of `Xjmm`.** This is the one sign that does not read on pixels alone. A looped descender with its return stroke is visible, which fits this writer's j, but the tails of `Xfflt` from the line above run into the same spot and no dot of its own can be seen. The blotch inside the loop lies over the stem of the j of `Mppljoh` below and is not claimed as the dot. An f cannot be strictly excluded, but `Xfmm` = WELL gives no sentence, and WILL is the only reading that does.
- **`Mpp` = LOO.** The p has its eye to the right of the stem, as in `Zpvs` and `Mpwjoh`, whereas f has its eye to the left, so this is not `Mfp` (LEO). The capital has three downstrokes, as the M of `Mpwjoh`, where the N of `Nz` has two. `Mppljoh` needs the same pair of signs for the checked word LOOKING, and the signature is the same as on HCP 1398. Whether Loo is a pet name, and for what, is not established.
- **"Twelve weeks to-day".** `up ebz` is written as two words and read as "to-day". The phrase is taken as twelve weeks from the day of writing, which would be Saturday 11 May 1907 (computed), perhaps a wedding or a reunion. Nothing on the card says what the event is.
- **G. H.** The initials are taken as plain by inference, not tested on their own. They stand in the same line as the plain "Saturday", Caesar −1 would give the meaningless F. G., and HCP 1352 has the same form, "G. H. Friday". Their meaning is unknown.
- **Publication search.** No web search for a prior publication of this card was made in the solving or the review. The check rests on the portal status (Not solved) and the AI Decipherment Register (no record for this card, checked 2026-10-30).

![The second sign of `Xjmm`, enlarged (work/crops/will_second_sign.png)](../work/crops/will_second_sign.png)

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, read the card independently and decoded it with its own script. It checked every word on the scan, confirmed that shifts 0 and 2 give nothing readable, that one shift covers all 70 letters, that the picture side has no further text, and that 16 February 1907 was a Saturday. Its four findings were minor and are reflected here:

- **`Xjmm`.** The claim that the key holds on every word now carries the exception: 69 letters on form, 1 on form plus context.
- **`Mpp`.** The argument for M against N was missing and has been added.
- **Slovak.** "chlapec" was corrected to the vocative "chlapče".
- **G. H.** The plain status is now stated as an inference.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1351, all three tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1351 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4113/conversions/pc_hcp_32_pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/4113/pc_hcp_32_pic.JPG
- Address side: https://api.hcportal.eu/media/4114/conversions/pc_hcp_32_adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/4114/pc_hcp_32_adr.JPG
- Sister cards in this repository: ciphers/hcp-1350, hcp-1352, hcp-1386 to hcp-1407.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.
