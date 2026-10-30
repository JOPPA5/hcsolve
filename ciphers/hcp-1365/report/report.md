# HCP 1365 (pc_hcp_46): an English Caesar sweetheart postcard, July 1907

Human solver: Tomáš Pavuk

**Status: whole message read (70 enciphered letters); the initials M. L. kept literal; two letters of FOREVER rest on context, and the last letters of THANKS and CARD are forced by the word. Independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1365 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1365), portal name pc_hcp_46, part of the HCPortal collection of cryptographic postcards. When captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-07-22, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (a catalogue spelling of Abbott), with no transcription or solution attached.

The picture side is a printed view, "West Park Promenade and Prospect Hotel, Harrogate", with no cipher on it. The address side (Boots Cash Chemists "Pelham" Series) carries a halfpenny Edward VII stamp postmarked WIMBORNE, JY 22, 07, and is addressed to Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon. The hour on the postmark is hard to read; it seems to be 10 AM. 22 July 1907 was a Monday, so the plain heading "G. H. Sunday." fits a card written the day before and posted next morning.

The writer, addressee and postmark match the accepted Caesar cards HCP 1386 to 1407 in this repository, a correspondence of one couple from 1907 to 1908. The key was tested on this card as a hypothesis from those cards, not taken for granted.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned; the message lies sideways on the left half (source/address-large.jpg)](../source/address-large.jpg)

![Message turned 90° counter-clockwise, from the original high-resolution scan (work/reading.png)](../work/reading.png)

## Method

The solver turned the address side 90° counter-clockwise and read the seven cipher lines by hand from 3× to 9× enlargements of the un-converted original scan. No OCR was used, and the portal supplied no transcription. Applying the shift of the sister cards turned every enciphered word into English. Alternatives for the hard words were considered and dropped: "Fwfs" (EVER) and "gbuifs" (FATHER) for line 6, and "Nptu" for line 4. The transcription and a decoder are kept in the working files. The decoder checks the hashes of the scans and the inverse round trip.

In review, the reviewer re-keyed the ciphertext from its own crops and tried all 26 shifts. Only shift 1 gives English (20 of 20 tokens are words; the next best shifts give 1 of 20).

## Key

Caesar shift: each plaintext letter is written as the next letter of the alphabet, and decrypting subtracts one (A→Z).

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading "G. H. Sunday." is ordinary writing. `&` and the initials `M. L.` (they occur twice) are kept literal; initials are likewise left unshifted on sister cards.

## Plaintext

| Line | Ciphertext | Literal plaintext |
|---|---|---|
| Heading | G. H. Sunday. (plain) | G. H. SUNDAY. |
| 1 | Nz Pxo M. L. Cpz. | MY OWN [M.] [L.] BOY. |
| 2 | J. bn. Tpssz up | I. AM. SORRY TO |
| 3 | ifbs zpv. bsf Opu. | HEAR YOU. ARE NOT. |
| 4 | xfmm. Nboz | WELL. MANY |
| 5 | uibolt. gps. dbse. | THANKS. FOR. CARD. |
| 6 | & gpsfwfs. zpvs | & FOREVER. YOUR |
| 7 | Pxo. M. L. Hjsm. | OWN. [M.] [L.] GIRL. |

**English (the original language):** My own M. L. boy, I am sorry to hear you are not well. Many thanks for card, & forever your own M. L. girl.

**Slovak:** Môj vlastný M. L. chlapec, je mi ľúto, že počujem, že sa necítiš dobre. Veľká vďaka za pohľadnicu, a navždy tvoje vlastné M. L. dievča.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1365/work/decode.py
```

It verifies the SHA-256 of the two scans in source/ and the two originals in work/hires/, decodes work/transcription.json and prints the plaintext and the count of 70 enciphered letters.

## Uncertainties

- **FOREVER (line 6) is the weakest word.** It is tangled with the long descenders of the line above. The g, p, s, first f and final s can be seen. The `w` is only an oval with an inner hook, and the card has no other `w` to compare. The second f is a long stem with no loop, unlike this writer's looped f, and it may partly belong to the line above. No other word fits the visible start, end and sense, but these two letters are contextual. FOR EVER as two words cannot be excluded.
- **MANY (line 4).** The z is mostly visible under a blot. A heavy bar above it, where a descender from the line above lands, is unexplained.
- **THANKS (line 5), final t.** Only a short faint upstroke survives, with no crossbar and a blot beside it. The word forces the letter.
- **CARD (line 5), final e.** The sign is a compact cross shape, more like this writer's x than an e, and ciphertext `e` occurs nowhere else on the card. "Many thanks for" and the sister cards force CARD.
- **M. L.** The meaning is unknown. The first letter has more legs than the N of `Nz`, so M is preferred, but N remains possible. If shifted, the initials would be L. K.; only literal agrees with sister-card practice.
- **NOT (line 3).** O and p are joined and the u is faint, but the reading is supported on the scan and is the only sensible one in "are not well".
- **G. H.** The heading's meaning is unknown, and its first letter could be C. The dots in the text follow the manuscript and have no significance.
- The writer's and recipient's identities beyond "W. Abbott" and the sign-offs are not established. Whether this card is by the same hand as the sister cards was judged from the solver's reading of this card and the written solutions of those cards; the reviewer did not compare their scans.
- No prior solution of this card was found. The check covers the portal status (Not solved, nothing attached) and the AI Decipherment Register (no record on 2026-10-30).

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, re-keyed the text from its own crops, decoded it with its own script, checked every word on enlargements of the original scan, and confirmed the caption, postmark, address and weekday. It raised five minor findings, all accepted, and all concerning the disclosure of doubt:

- **FOREVER.** The note now states that the second f has no loop and that the word rests on context for two letters.
- **MANY.** The note now says the z is mostly visible and the bar above it is unexplained.
- **THANKS.** The weak final t is now listed.
- **CARD.** The irregular final e is now listed.
- **Evidence.** FOREVER no longer counts as evidence for the key.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1365, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1365 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4155/conversions/pc_hcp_46_pic-large.jpg (source/picture-large.jpg); original https://api.hcportal.eu/media/4155/pc_hcp_46_pic.JPG.
- Address side: https://api.hcportal.eu/media/4156/conversions/pc_hcp_46_adr-large.jpg (source/address-large.jpg); original https://api.hcportal.eu/media/4156/pc_hcp_46_adr.JPG.
- Sister cards in this repository: HCP 1386 to 1407.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-30.
