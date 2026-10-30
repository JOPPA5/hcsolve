# HCP 1401 (pc_hcp_82): a Caesar-shifted New Year postcard, 30 December 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (15 of 15 enciphered letters); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1401 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1401), portal name pc_hcp_82, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1907-12-30, language Unknown, location Europe, sender Unknown, recipient "W. Abboú" (a misreading of Abbott), with no transcription or solution attached.

The picture side is a printed Raphael Tuck & Sons "Oilette" view, *Bickleigh Vale, South Devon*, with the printed greeting "A Bright and Happy New Year to you"; it carries no handwriting. The address side (Tuck's Post Card, Postcard 7279) is addressed in plain writing to **Mr W. Abbott, Stokelake Farm, Chudleigh, Devon**. It bears a red ONE PENNY Edward VII stamp cancelled "…MBORN[E] / 10 PM / DE 30 / 07" (Wimborne), which agrees with the portal date: 30 December 1907 was a Monday.

The message is written sideways in the left (sender's) half of the address side: a plain heading **C. H. Monday.** followed by three short lines of cipher. The card belongs to a series of postcards to the Abbott household (HC Portal 1386–1407) written in the same hand with the same Caesar shift, several of which are already deciphered in this repository; their closing formula is the same as here.

![Address side as scanned: message at the left, address and Wimborne postmark at the right (source/address.jpg)](../source/address.jpg)

![Message area turned upright (work/c2/rot.jpg)](../work/c2/rot.jpg)

![Picture side: Bickleigh Vale, South Devon, with printed New Year greeting (source/picture.jpg)](../source/picture.jpg)

## Method

The message was transcribed by hand from enlarged crops of the rotated address side (work/c2/line1.png to line3.png, eh.png, tail.png). The cipher letters are ordinary cursive Latin letters, so the only question was the shift. Trying all 26 Caesar shifts on the four enciphered words, only one (decrypt by −1) gives language: FROM YOUR OWN GIRL. Every other shift is gibberish.

The one difficult sign is the second letter of the abbreviation `E. L.`. An earlier partial reading had left it as h / l / 1. On the enlargements it is a single rising stroke from a small loop or blot at its foot, followed by a dot, with no second stem or arch (so not h). The same writer's capital L in the identical formula "Pxo. E. L. Hjsm" on the sister card HCP 1386 has the same construction, so it is read as L.

The reviewer made its own rotated and enlarged crops, transcribed the four cipher words independently and decoded them with its own all-shifts script (review/work/indep_decode.py); its reading agrees letter for letter.

## Key

Caesar shift: every plaintext letter is written as the next letter of the alphabet (encryption +1). To decrypt, subtract one (A becomes Z).

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The heading "C. H. Monday" is ordinary writing, not enciphered. `E. L.` is an abbreviation that is kept literal, as on HCP 1386; shifted, it would give D. K., which yields nothing.

## Plaintext

| Ciphertext | Plaintext |
|---|---|
| gspn. Zpvs. | FROM. YOUR. |
| Pxo. E. L. | OWN. [E. L.] |
| Hjsm ' | GIRL ' |

The `Z` of Zpvs is written in a 2-like form, as on the sister cards. The wedge after Hjsm is a pen mark, not a letter.

Full message, with the plain heading:

**C. H. Monday. From your own E. L. girl.**

English (the plaintext language): *"C. H. Monday. From your own E. L. girl."*

Slovak translation: *„C. H. Pondelok. Od tvojho vlastného E. L. dievčaťa."*

The words are few but fit their setting: a New Year card posted on a Monday, signed with the closing formula of the sister cards ("Your own girl" on HCP 1397, "from your own E. L. girl" on HCP 1386).

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1401/work/v2/decode.py
```

The script checks the SHA-256 hashes of the three files in source/, decodes every token of the manual transcription in work/v2/transcription.json with the −1 shift, checks the round trip and the letter counts, and prints:

```text
FROM. YOUR.
OWN. [E. L.]
GIRL '
15 enciphered letters decoded, 2 abbreviation letters kept literal.
```

It does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **The L of `E. L.`** On this card alone its foot is a blotted ink mass; the reading L rests on the shape (one stem, no arch) together with the identical formula on HCP 1386 and 1404.
- **Meaning of `E. L.`** Not established (perhaps "ever loving"); it is kept literal, and whether these initials are themselves shifted is undecided.
- **Heading initials** C. H. or G. H.: the first letter is ambiguous and differs between sister cards; it is not enciphered.
- **The wedge after Hjsm** is read as a pen mark (apostrophe or comma) and not interpreted.
- **Identity of the writer** is not established beyond the closing formula and the Wimborne postmark shared with the sister cards.
- **A short text.** Four enciphered words; the key is secure because only one shift gives language and because the same key and formula are confirmed on many sister cards.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), decoded its own transcription with all 26 shifts (only −1 gives English), checked every sign on its own rotated and enlarged crops of the scan (including a ~9× zoom of `E. L.`), confirmed that the whole message area is transcribed, and confirmed that no published solution was used. Its three minor findings and what changed:

- **Farm name.** The address reads clearly "Stokelake Farm"; it is now given in full above (the solver's handover said it was not established).
- **Postmark.** The Wimborne cancellation, 10 PM, 30 Dec 1907, is now cited as independent confirmation of the date.
- **L reading.** Agreed that it partly rests on comparison with HCP 1386; this is stated in the uncertainties. No change to the reading.

No decoded letter changed as a result of the review.

## Credits

Download of the scans and metadata, identification of the Caesar key and a partial reading with one unresolved sign: OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol), 2026-10-26. Re-inspection of the scan, resolution of the sign as L, new transcription and decoder, response to review and this report: Claude Opus 5.5 acting as solver, 2026-10-29. Independent review: a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1401, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1401 (source/metadata.md, SOURCES.md).
- Scans of the picture side and address side as attached to the portal record (source/picture.jpg, source/address.jpg).
- Sister cards of the same series in this repository: HCP 1386, 1388, 1397, 1402, 1403, 1404.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no entry for this card.
