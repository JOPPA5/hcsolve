# HCP 1348 (pc_hcp_29): a Caesar-shifted love note signed Loo

Human solver: Tomáš Pavuk

**Status: all 28 enciphered letters decoded with one fixed key; two words carry a disclosed one-letter restoration. Independent review 1 verdict REVISE; the findings are addressed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1348 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1348), portal name pc_hcp_29, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1904-02-08, language Unknown, location Europe, sender Unknown, recipient "W. Abboú", with no transcription or solution attached. No published solution was found in this repository's sources; no separate web search was run.

The picture side is a coloured view printed "Rowlands Hill, Wimborne", with no handwriting. The address side carries a halfpenny Edward VII stamp, the postmark WIMBORNE 10 PM FE 8 with no year struck, and the plain address Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon. "Abboú" on the portal is a misreading of Abbott.

The card belongs to a correspondence of cipher postcards to W. Abbott in this repository, sent from Wimborne and mostly dated 1907–08. Several of those cards are signed `Mpp` = Loo, for example HCP 1350, 1351, 1353 and 1398. Whether "Loo" is a pet name, and for what, is not known.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned; the grey wheel is the portal's watermark, not part of the card (source/address-large.jpg)](../source/address-large.jpg)

![Message area turned 90° counter-clockwise, with the plain date below (work/crops/msg.png)](../work/crops/msg.png)

## Method

The message was read by hand from enlarged crops of the un-converted original scan (work/hires/pc_hcp_29_adr.JPG), sign by sign, and the words were compared with the same words on sister cards. The Caesar shift was known from those cards and was tested here as a hypothesis. It was not recovered from this card, which at 28 letters is too short for that. The reviewer's trial of all 26 shifts on its own transcription found English only at this one.

The script work/decode.py checks the hashes of the source files, decodes the transcription and checks the round trip:

```text
python3 -I ciphers/hcp-1348/work/decode.py
```

## Key

Each plaintext letter is written as the next letter of the alphabet; to decrypt, subtract one (A→Z). The same fixed key is used for every letter. The date and address are ordinary writing and are not shifted.

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

| Ciphertext | Literal decode | Reading |
|---|---|---|
| Xjui Mpwf. boe. | WITH LOVE. AND. | With love and |
| jttft gspn x pvst | ISSES FROM W OURS | [k]isses from [y]ours |
| M.p.p. | L.O.O. | Loo |

Square brackets mark an editorial restoration, not a deciphered letter. Below the cipher stands the plain date Feb 8th 1907.

**English:** "With love and kisses from yours. Loo. Feb 8th 1907."

**Slovak:** „S láskou a bozkami od tvojej. Loo. 8. februára 1907."

The feminine "tvojej" follows the sister cards signed "your loving girl, Loo"; this card does not state the writer's sex.

## What remains uncertain

- **[K]ISSES.** The tail `ttft` is secure and matches `Ljttft` on HCP 1362, but no separate L is visible. The first sign is closer to this writer's g than to the j, and a literal g would give FSSES. The word rests on the tail and the sister card.
- **[Y]OURS.** The sign before `pvst` is a plain cross, identical to the X of `Xjui`, so literally W. It may be a slip for z, a shift in the wrong direction (Y−1 = X) or a kiss cross followed by OURS. "From yours" is probable, not proved.
- **The capital of M.p.p.** It has three strokes, like the M of the `Mpp` signature on HCP 1351, but on this card alone a two-hump N (giving M.O.O.) is not fully excluded.
- **The year.** The postmark has no year. The year 1907 rests on the writer's digit form and the correspondence, and it disagrees with the portal's 1904-02-08.
- **Small signs.** The v of `pvst` looks r-like at this size and rests on the word. The w of `Mpwf` rests on the sister outline. A small tick above `ui` is probably the dot of the final i.
- **Length.** With 28 letters the card is confirmed by its formula and hand rather than by statistics. The sender's identity rests on hand and signature comparison, not on a statistical test of the hand.

## Review and what changed

An independent Claude Opus 5.5 reviewer ran the command, decoded its own transcription and checked every word on 4–5× crops. It confirmed the key, the words WITH LOVE AND … FROM … and the address, and returned **REVISE** with five findings:

- **The closing (major).** The first version read initials N. P. P., unexpanded. The reviewer showed that this is the writer's signature `Mpp` = LOO. Corrected.
- **The year (major).** The first version read 1904 with "a clear final 4", following the portal. The digit is this writer's 7, the same form as in "1907" on HCP 1353, whose postmark reads 07 (image below). Corrected: 8 February 1907 was a Friday, the day after HCP 1353. The card is not an outlier from the series.
- **The first sign of `jttft` (minor).** Now stated to be nearer g than j.
- **The cross before `pvst` (minor).** It cannot be a misread z; the wrong-direction shift was added as an explanation.
- **Punctuation (minor).** Dots after `Mpwf`, after `boe` and in the closing were added to the transcription; they do not affect the reading.

The key and the letters of the first two lines did not change.

![Date on HCP 1353, postmarked 07 (top), and on this card (bottom): the same final digit (review/work/cmp_seven.png)](../review/work/cmp_seven.png)
