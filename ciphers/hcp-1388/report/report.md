# HCP 1388 (pc_hcp_69): an English love note to W. Abbott, Chudleigh, 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (51 of 51 cipher letters); two dark non-alphabetic marks reported literally; independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1388 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1388), portal name pc_hcp_69, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tag Postcard HCPortal collection, category Substitution, date 1907-04-15, language Unknown, location Europe, sender Unknown, recipient "W. Abboú", with no transcription or solution attached.

The picture side is a Frith's Series view captioned "Nottingham Castle" and carries no handwriting. The address side, written sideways, is in plain English: **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon**. It has a halfpenny Edward VII stamp postmarked "…MBORNE / 10 PM / AP 15 / [0]7". Below the address, a plain heading "G. H. Monday" is followed by four enciphered lines and the plain date **April 15th 1907** (a Monday), which agrees with the postmark and the portal date.

The card belongs to a run of postcards to W. Abbott in the same hand and the same cipher (HCP 1386–1407, 1907–08); the sister cards HCP 1390 and 1397 are deciphered in this repository with the same key and the same closing formula ("… from your own Girl").

![Picture side: Nottingham Castle, no handwriting (source/picture.jpg)](../source/picture.jpg)

![Address side turned upright: address to Mr W. Abbott, heading G. H. Monday, four cipher lines, plain date April 15th 1907 (work/address-rotated.jpg)](../work/address-rotated.jpg)

## Method

The scan was turned 90° counter-clockwise and the four cipher lines were transcribed **by hand** from enlarged crops (3–10×); no OCR was used and the portal supplied no transcription. Common short words immediately give a shift of one: `Nz` → My, `Zpvs` → Your, `pxo` → own, `gps` → for, and long words confirm it (`Efbsftu` → Dearest, `mfuufs` → letter). The same key had already been established on the sister card HCP 1397.

Two places needed close work:

- **Line 3, first word `gjof` → fine.** A 9-shaped g, a j with a heavy dot above it, a small o and a looped f.
- **Line 3, the group before `gspn`.** Most of its ink belongs to line 2: a long diagonal runs without a break from the j of `ju` above. Once that stroke is set aside, a capital N (built like the N of `Nz`) and two y-signs remain: `N yy` → **M xx**, i.e. M and two kisses.

![Line 3, gjof = fine (work/c-l3-gjof.png)](../work/c-l3-gjof.png)

![Line 3, the N yy group with the line-2 j descender running through it (work/c-l3-nyy-and-j-descender.png)](../work/c-l3-nyy-and-j-descender.png)

The reviewer made its own rotation and crops, read every word itself and decrypted with its own script; its reading agrees with the solver's in all 51 letters.

## Key

Caesar shift. Each plaintext letter is written as the **next** letter of the alphabet (encryption +1); to decrypt, subtract one. Case is kept; dots and dashes are not enciphered.

```text
cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Plaintext

| Cipher (manual transcription) | Plaintext |
|---|---|
| `Nz. Efbsftu. uibolt -` | My. Dearest. thanks - |
| `gps. mfuufs ju. Xbt` | for. letter it. Was |
| `gjof [blots] N yy gspn` | fine [blots] M xx from |
| `Zpvs. pxo. Hjsm` | Your. own. Girl |

`[blots]` (two asterisks in brackets in SOLUTION.md and the script) marks two small, dense, dark blots on line 3 that have no letter form and are not deciphered.

Full card (plain parts in italics): *G. H. Monday* — **My dearest, thanks for letter, it was fine. [blots] M xx from your own girl.** — *April 15th 1907*

English: **My dearest, thanks for your letter, it was fine. [blots] M, kisses, from your own girl.**

Slovak: **Môj najdrahší, ďakujem za list, bol pekný. [blots] M, bozky, od tvojho vlastného dievčaťa.**

Punctuation and capitals of the readings are editorial. "xx" is the usual written sign for kisses.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1388/work/decode_full.py
```

The script checks the SHA-256 hashes of both scans and the metadata, decrypts the manual transcription in work/transcript_full.json with the shift −1, asserts the expected plaintext line by line and prints the four lines with "cipher letters decrypted: 51". It does not read the image; the transcription is manual and was confirmed independently in review.

## Uncertainties

- **The two marks [blots] on line 3.** Dense, star-shaped blots in ink darker than the message, with no letter form: heavily inked crosses (kisses), blotted or cancelled letters, or later stains are all possible. Not deciphered.
- **"M".** Cipher N = plain M, standing alone before the kisses. It may be the writer's initial or pet name, or an abbreviation; it is not expanded. On sister card HCP 1390 a capital also stands before two kisses, but there it is left undecided whether that capital is enciphered or plain; HCP 1390 supports the kisses, and is only consistent with (not proof of) N → M here.
- **The N yy group.** The stem of the first y merges with the line-2 j descender. A closed oval left of the diagonal is taken as that j's descender loop; it could instead be a separate line-3 sign (it resembles the writer's 9-shaped g), giving four signs (N ? y y). The reading "M … xx" does not depend on it, but the exact sign count is not certain.
- **Outside the cipher.** The heading initials (G. H., C. H. not excluded) are not expanded; the writer's identity is not established; the farm name is read as Stokelake, as on HCP 1397. The postmark year digits are faint.
- No prior publication of this card was found: the portal status is Not solved and the AI Decipherment Register had no record for it when checked on 2026-10-29.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), decrypted its own transcription with its own script (same 51 letters, one key, no exceptions), checked every word on its own enlargements of the scan, and confirmed the date against the postmark. Its four minor findings and what changed:

- **HCP 1390 parallel overstated.** The solution had said the 1390 group "confirms" N → M. It now says 1390 supports the kisses and is only consistent with N → M, which rests on the capital's shape on this card.
- **The oval in the N yy group.** Now listed as an uncertainty (possible fourth sign).
- **Heading initial.** Now given as G. H. (C. H. not excluded), matching HCP 1397.
- **Literal "M".** Kept unexpanded, as the reviewer agreed.

No decoded letter changed as a result of the review.

## Credit

The first, partial work (2026-10-26) was done by OpenAI GPT (GPT-6 Astra / GPT-6.1 Sol): it downloaded the sources, identified the shift, made the rotation and crops, and read lines 1, 2 and 4 plus `gspn`. Claude Opus 5.5 (2026-10-29) completed the reading (`gjof` → fine; separation of the line-2 j descender; `N yy` → M xx), rewrote the transcription and command, and on 2026-10-30 answered the review and wrote this report. The review was made by a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1388, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1388 (source/metadata.md, SOURCES.md).
- Picture side and address side scans as attached on the portal (source/picture.jpg, source/address.jpg).
- Sister cards in this repository: ciphers/hcp-1390, ciphers/hcp-1397.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.
