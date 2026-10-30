# HCP 1395 (pc_hcp_76): a Caesar-shift love postcard to Mr Abbott, Chudleigh, 1907

Human solver: Tomáš Pavuk

**Status: all 44 enciphered letters deciphered with one fixed shift (Caesar −1); independent review 1 verdict REVISE, findings addressed, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1395 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1395), portal name pc_hcp_76, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, category Substitution, date 1907-04-24, language "Unknown", recipient "W. Abboú", with no transcription or solution attached.

The picture side is a printed view, "Branksome Chine, Bournemouth", with no handwriting. The address side is in ordinary writing: **Mr Abbott, Stokelake Farm, Chudleigh, Devon**, postmarked **WIMBORNE, AP 24, 07**. The portal's "W. Abboú" is a misreading of "Abbott". The message stands in the left half of the address side and is read after turning the scan 90° counter-clockwise. It opens with the ordinary heading "G. H. Wednesday" and ends with the ordinary date "April 24th 07.", which agrees with the postmark (24 April 1907 was a Wednesday).

The card belongs to a correspondence of 1907–08 from a young woman to Mr W. Abbott at Chudleigh (HC Portal cards 1386–1407), several of which use the same shift and the same closing formula; the nearest parallel is HCP 1397, "Mpwf gspn Zpvs Pxo Hjsm" = "Love from your own girl".

![Picture side (source/picture.jpg)](../source/picture.jpg)

![Address side as scanned: address to Mr Abbott, Chudleigh, Devon; message in the left half (source/address.jpg)](../source/address.jpg)

![The message, turned 90° counter-clockwise (work/message.png)](../work/message.png)

## Method

The transcription is manual: the scan was rotated and the message read letter by letter on 3–6× enlargements; no OCR was used and the portal supplied no transcription. Long words identify the key at once: *Efbsftu* becomes DEAREST and *Hpjoh* becomes GOING when every letter is moved back one place in the alphabet. That single shift was then applied to every enciphered letter by a script, which also checks the hashes of the source images and re-enciphers each line to confirm the round trip.

Reproduction, from the repository root:

```sh
python3 -I ciphers/hcp-1395/work/decode.py
```

## Key

Monoalphabetic shift (Caesar): each plaintext letter was written as the next letter of the alphabet. To decipher, shift back by one.

```text
cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

Dots and the ampersand are written by the hand and are not enciphered. The heading, date and address are in ordinary writing.

## Plaintext

| Ciphertext (as written) | Literal plaintext |
|---|---|
| Nz. Efbsftu. | MY. DEAREST. |
| J bn. kvtu | I AM. JUST |
| Hpjoh up qptu | GOING TO POST |
| M. & L. gspn. | L. & K. FROM. |
| Zpvs. pxo | YOUR. OWN |
| Hjsm *(inside an ornamental outline)* | GIRL |

Reading: **My dearest, I am just going to post. L. & K. [probably "love & kisses"] from your own girl.**

English (the card is in English): "My dearest, I am just going to post [i.e. going to the post, or to post this]. L. & K. [probably "love & kisses"] from your own girl."

Slovak: „Môj najdrahší, práve idem na poštu. L. & K. [pravdepodobne „love & kisses“ = láska a bozky] od tvojho vlastného dievčaťa.“

The bracketed expansion is editorial; only the letters L. & K. are deciphered.

![Closing initials enlarged (work/closing-initials.png)](../work/closing-initials.png)

## Uncertainties

- **The closing initials before FROM.** Three questions remain open here:
  - *Letter identity.* The first initial has a hooked stem and two descending legs and is wider than the one-arch N of *Nz* (MY) on the same card, so it is read as M; but in this hand M and N differ by only one short leg. Read as N, the group would decipher to **M. & K.**, which matches HCP 1388 (enciphered `N yy` = M xx, "M" and kisses) and the reading proposed for the same group on HCP 1399 (`N & Lt` → M & Ks).
  - *Enciphered or not.* The writer enciphers everything except heading, date and address, and on sister cards she enciphers the closing formula (HCP 1397 "Mpwf" = LOVE, HCP 1388 `N yy`). This supports, but does not prove, that the initials are enciphered too. If they were left in clear, the group simply reads "M. & L.".
  - *Expansion.* "Love & kisses" is the usual sense of L. & K. but is interpretation. The sister cards HCP 1399 and HCP 1407 keep the same group literal and unclassified; this card classifies it with somewhat more confidence only because the enlargement shows two legs.
  - A small raised tick and a dash after "L." are taken as a flourish (the same tick follows the L on HCP 1407).
- **"going to post"** has no object on the card; nothing is added to the deciphered text.
- **Cursive shapes.** In *kvtu* the v is open and the u ends in a flourish; *kvtu* = JUST is the only reading giving a word. The j of *Hjsm* is a long slanted descender, as in *Hpjoh*.
- **Heading "G. H."** (possibly "C. H.") is in clear, not part of the cipher, and its meaning is unknown. The writer's identity is not established.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. The reviewer ran the reproduction command, decoded its own transcription with its own script (identical output, 44 letters, no unknowns), checked every line against enlarged crops of the scan, compared the closing initial with the N of *Nz* and preferred M, confirmed the address, date and postmark and found no published solution. Its findings and what changed:

1. **Expansion shown as read text (major).** The headline and the translations now show "L. & K." with the expansion in brackets as editorial.
2. **N-reading not disclosed (major).** The alternative N. & L. → M. & K., with the evidence of HCP 1388 and 1399, and the fact that HCP 1399 and 1407 keep this group literal, are now stated.
3. **HCP 1397 argument overstated (minor).** It is now presented as supporting evidence only.
4. **Unspaced notes entry (minor).** Reformatted.
5. **"going to post" (minor).** Glossed in the translation.

No deciphered letter changed as a result of the review.

## Credit

Cipher identification, transcription of the body and a first decoder: OpenAI GPT solver (GPT-6 Astra), 2026-10-26, left partial because of the closing initials. Re-verification on the scan, classification of the initials, the rewritten decoder, the response to review and this report: Claude Opus 5.5, 2026-10-29/30. Independent review: a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1395, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1395 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4245/conversions/pc_hcp_76_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4246/conversions/pc_hcp_76_adr-large.jpg (source/address.jpg).
- Sister cards in this repository: ciphers/hcp-1388, hcp-1397, hcp-1399, hcp-1407.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no entry for this card.
