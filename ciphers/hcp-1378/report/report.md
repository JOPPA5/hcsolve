# HCP 1378 (pc_hcp_59): an English Caesar sweetheart postcard, 14 November 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (31 of 31 enciphered letters); one abbreviation (E. L.) kept literal, the rest of the card is in clear. Independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30 (UTC).

## Origin and context

The cryptogram is record 1378 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1378), portal name pc_hcp_59, part of the HCPortal collection of cryptographic postcards. When captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-11-14, language Unknown, location Europe, sender Unknown, recipient "W. Abboú", with no transcription or solution attached.

The picture side is a printed view, "Sea Front, Herne Bay", The Wrench Series No. 13590, with no handwriting. The address side carries a halfpenny Edward VII stamp postmarked **WIMBORNE / NO 14 / 07**, a receiving mark **NEWTON ABBOT, NO 15 07**, and the plain address **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon** (the portal's "Abboú" is a misreading of Abbott). The circular alphabet disc on both scans is a collection overlay, not part of the card.

The card belongs to a correspondence to W. Abbott, signed "girl", in which other cards of the same couple (for example HCP 1386, 1397 and 1398, dated 1907–08) use the same shift and the same formulae. The message here is short: the writer asks whether she has already sent a card of the Martyrs' Memorial in Oxford, while the card itself shows Herne Bay.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![Message area turned 90 degrees counter-clockwise (work/crops/rot.png)](../work/crops/rot.png)

## Method

The solver read the original scan (work/hires/pc_hcp_59_adr.JPG), turned it upright and read each line on enlarged crops. The transcription is manual. The Caesar shift was taken as a hypothesis from the accepted Abbott sister cards and then tested on this card alone, where it decodes every enciphered word. Only part of the card is enciphered. The heading, the date and the name of the monument are in clear, and shifting them gives nonsense (SGD LZQSXQR LDLNQHZK).

Two first readings were corrected on 6× enlargements before handover: `dbse` had been read as "Abse", and `Tfou` as "Gou" or "Ifou".

## Key

Monoalphabetic Caesar: each plaintext letter is written as the **next** letter of the alphabet, so decryption subtracts one.

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

| On the card | Reading | Mode |
|---|---|---|
| G. H. Thursday. | G. H. Thursday. | clear |
| Nz. Pxo. E. L. Cpz. | MY OWN E. L. BOY | cipher, E. L. literal |
| Ibwf. J. Tfou | HAVE I SENT | cipher |
| dbse. pg. | CARD OF | cipher |
| The Martyrs Memorial | The Martyrs Memorial | clear |
| Oxford. | Oxford. | clear |
| Nov. 14th 07. (left) | Nov. 14th 07. | clear |
| Zpvs Hjsm (right, same physical line) | YOUR GIRL | cipher |

The long underline below `Hjsm` is a flourish, not text.

**English:** *G. H., Thursday. My own E. L. boy, have I sent card of The Martyrs Memorial, Oxford? Your girl. Nov. 14th 07.*

**Slovak:** *G. H., štvrtok. Môj vlastný E. L. chlapec, poslala som pohľadnicu Pamätníka mučeníkov v Oxforde? Tvoje dievča. 14. nov. 1907.*

The question mark is editorial: none is written, and the inverted word order makes the sentence a question.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1378/work/decode.py
```

The script checks the SHA-256 of the source images, decodes every token of work/transcription.json, tests the inverse round trip, and prints the plaintext, the letter counts (31 enciphered, 2 literal) and the weekday check.

## Why the reading is believed

One fixed shift turns all 31 enciphered letters into English with no exception. MY OWN, BOY, YOUR and GIRL are the couple's recurring formulae (`Nz. Pxo. E. L. Cpz.` is identical on HCP 1386). "Thursday" and "Nov. 14th 07" agree with the postmark and the portal date, and 14 November 1907 was a Thursday. The Martyrs' Memorial is a real monument in Oxford.

## Uncertainties

- **`Tfou` (SENT).** The T and the f run together and share the top bar. Two signs are read because a single-sign reading gives no word. The scan cannot prove the stroke order.
- **`dbse` (CARD).** The first sign is long and slanted and does not match the short d of "Thursday"; A is excluded by the word (Z-ARD), and a capital D would decode the same. The last sign is open with a notch and could be e or c by shape; `dbsc` would give CARB, so the word decides.
- **u/v/w signs.** The middle sign of `Pxo` is a blot, so `x` is plausible but not positively seen; `w` would give OVN, and OWN rests on the sister formula. The third sign of `Ibwf` hardly differs from the `v` of `Zpvs`. In these tokens the choice rests on the word, not the pen shape.
- **E. L. and G. H.** are not expanded. E. L. is kept literal as on the sister cards; a shifted value (D. K.) or an expansion such as "ever loving" is not proved.
- **The clear words.** In "Martyrs" the t-bar is taken to be the long stroke above "yr", which could instead underline `pg`; no apostrophe is visible. The final l of "Memorial" sits high at the card edge.
- **The Oxford card.** It is unknown which card is meant or whether it survives. A search of the solutions and notes of HCP 13xx and 14xx found no other mention of Oxford or the Martyrs' Memorial.
- **Prior publication.** The portal attaches no solution and the AI Decipherment Register has no record, but no general web search was made.

## Review summary

Reviewer: Claude Opus 5.5 (a separate agent), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, made its own crops from the original scan, read all the written lines and decoded them with its own script and explicit table; all 31 enciphered letters agreed. It confirmed the clear lines, the postmarks, the weekday and the sister formulae. Its four minor findings and what changed:

1. **u/v/w signs.** The uncertainty was disclosed only for `Pxo`; it now covers `Ibwf` and `Zpvs` too.
2. **`dbse`.** The claimed match with the d of "Thursday" and the "filled" last sign were overstated; the wording is corrected, and CARD rests on the word.
3. **`Pxo`.** Confirmed as context-supported, now stated outright.
4. **Layout.** The date and the signature are now recorded on one physical line, date at the left, and the underline is noted as not being text.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1378, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1378 (source/metadata.md, SOURCES.md).
- Picture and address sides: source/picture-large.jpg, source/address-large.jpg, originals in work/hires/ (URLs and hashes in SOURCES.md).
- Sister cards of the same couple in this repository: ciphers/hcp-1386, 1397, 1398.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30: no record for this card.
