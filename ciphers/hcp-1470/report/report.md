# HCP 1470 (pc_hcp_151): a numeric signature on a French birthday postcard, 1909

Human solver: Tomáš Pavuk

**Status: deciphered in full (14 of 14 numbers); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30 (UTC).

## Origin and context

The cryptogram is record 1470 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1470), portal name pc_hcp_151, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1909-03-30, language Unknown, location Europe, sender Unknown, recipient Valentine, with no transcription or solution attached.

The picture side is a printed birthday card ("Anniversaire", picture no. 1158, a man with a bouquet); it carries no handwriting. The address side has a French 10-centime Semeuse stamp and a railway postmark **TOURS A VIERZON, 30-3-09** (30 March 1909). The address is in plain French: *Mademoiselle Valentine P[o/a]udechat, aux Caves, Commune de Lacroix (Indre et Loire)*; the surname is read only loosely and plays no part in the cipher. The left (correspondence) half of the card is empty except for one curved line of dash-separated numbers running across it, under the postmark and over the printed dividing line.

![Address side, rotated so that the number line is legible: postmark TOURS A VIERZON 30-3-09, the plain French address, and the numbers along the bottom (work/reading.jpg)](../work/reading.jpg)

![Address side as delivered by the portal (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, "Anniversaire" (source/picture-large.jpg)](../source/picture-large.jpg)

The grey A–Z disc and logo over both scans are the HCPortal watermark, not part of the card. Numbers standing for letters by their position in the alphabet (1 = A … 26 = Z) are the commonest system on the cipher postcards of this collection; the same key was found on several other cards of the period deciphered in this repository (HCP 1098, 1463, 1492 and 1496).

## Method

The transcription is **manual**. The earlier solver, OpenAI GPT (GPT-6 Astra), captured the portal record, recorded SHA-256 hashes of the scans, made rotated and enlarged crops of the number line and wrote a provisional 14-number reading, with a doubt (12 or 13) at position 5. It also screened the numbers with plain A1Z26, all 26 cyclic shifts and the reversed alphabet (work/numeric-attempts.txt); only the unshifted alphabet gave anything pronounceable. Claude Opus 5.5 then re-read the line on crops rotated by about 30° and enlarged 3–10× (work/crop-line-start-rot30.png, work/crop-line-tail-rot30.png, work/crop-14-4-zoom.png), resolved position 5 as 13 (the same flat-topped cursive 3 as in position 1), wrote the final transcription to work/transcription.txt and decoded it with work/decode.py.

![Enlarged crop of positions 9–11, "1-14-4", with the printed double divider crossing the second 4 (work/crop-14-4-zoom.png)](../work/crop-14-4-zoom.png)

In review a separate Claude Opus 5.5 agent made its own crops (4–8×, some rotated 22–25°, autocontrast), read all fourteen numbers itself and decoded them with its own script. Its reading agrees with the solver's in **all 14 positions**.

## Key

Simple numeric substitution, **A1Z26**: each number is the position of the letter in the 26-letter Latin alphabet, with no offset.

| Number | 1 | 4 | 5 | 9 | 13 | 14 | 15 | 18 | 20 |
|---|---|---|---|---|---|---|---|---|---|
| Letter | A | D | E | I | M | N | O | R | T |

Only these nine values occur. Every number on the card is in the range 1–26 and is decoded by the same key; nothing is left over.

## Plaintext

Ciphertext as transcribed (dashes as on the card; there is no word separator):

```text
13-1-18-9-13-1-18-18-1-14-4-5-15-20
```

Decoded, number by number:

```text
13 1 18 9 | 13 1 18 18 1 14 4 5 15 20
 M A  R I |  M A  R  R A  N D E  O  T
```

Literal plaintext: **MARIMARRANDEOT**. Editorial segmentation: **MARI MARRANDEOT**.

Interpretation (not proven): a first name and a surname, i.e. the sender signing the card in code. *Mari* may be *Marie* written without its final e; the alternative gloss French *mari* "husband" is speculative. The repetition of 13-1-18 = MAR at the start of both parts is internal support for the direct key. The surname *Marrandeot* is not attested anywhere the solver or the reviewer could check; similar surnames (Marandeau, Marandet) exist in central France, and the writer may have misspelt or mis-encoded one of them, but no such correction is applied here. The result is reported as the literal decode, not as an identified person.

- **English:** "Mari(e) Marrandeot" [the sender's signature].
- **Slovak:** „Mari(e) Marrandeot" [podpis odosielateľa].

The language is French by context (French card, stamp, postmark and address); a personal name is not tied to a language.

## Reproduction

From the repository root:

```bash
python3 -I ciphers/hcp-1470/work/decode.py
```

The script checks the SHA-256 hashes of the files in source/ against work/source-sha256.json, reads the manual transcription in work/transcription.txt and prints:

```text
source hashes OK
cipher : 13-1-18-9-13-1-18-18-1-14-4-5-15-20 (14 numbers)
literal: MARIMARRANDEOT
segmented (editorial): MARI MARRANDEOT
```

The transcription is manual; the script does not read pixels.

## Uncertainties

1. **The name is unverified.** *Marrandeot* is not a known surname; the decode is reported literally and not corrected to Marandeau or similar.
2. **Position 11 (4 = D or 7 = G).** The sign lies under the printed double divider line. It is a long diagonal stem with a crossbar and no visible top bar, so 4 is preferred by both solver and reviewer; the crossed French 7 cannot be fully excluded at the available resolution (1024-pixel portal scan) and would give MARRANGEOT.
3. **Segmentation and language** (MARI | MARRANDEOT, French) are editorial; the card has no word divider.
4. The recipient's surname in the plain address (Poudechat or Paudechat) is a loose reading and irrelevant to the decoding.
5. The identity of the sender is not established.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), re-computed the image hashes, read the number line itself on its own enlargements, and decoded its own transcription with its own A1Z26 table; its reading agreed with the solver's in all 14 positions. It confirmed that position 5 is 13 (rejecting the earlier doubt 12), that position 11 is better read 4 than 7, that the picture side carries no handwritten cipher, that the key is the same one accepted on sister cards, and that no published or attached solution was used. Its four findings were minor and are reflected here:

- **Unverified name.** The report frames "Mari(e) Marrandeot" as a literal decode and possible signature, not an identified person, and mentions Marandeau/Marandet only as a possibility.
- **Position 11.** The alternative 7 = G (MARRANGEOT) is kept among the uncertainties.
- **Date consistency.** SOLUTION.md now gives the UTC time of the handover (2026-10-29T23:17Z) instead of the local date; this report uses UTC.
- **Segmentation and the *mari* gloss** are labelled editorial and speculative.

No decoded letter changed as a result of the review. Credit: initial capture, provisional transcription and the shift screen by OpenAI GPT (GPT-6 Astra), 2026-10-26; final transcription, decipherment, response to review and this report by Claude Opus 5.5.

## Sources

- HC Portal record 1470, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1470 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4471/conversions/pc_hcp_151_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4470/conversions/pc_hcp_151_pic-large.jpg (source/picture-large.jpg).
- Sister cards with the same A1Z26 key in this repository: ciphers/hcp-1098, hcp-1463, hcp-1492, hcp-1496.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no record for this card.
