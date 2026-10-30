# HCP 1403 (pc_hcp_84): an English Caesar postcard from "Girl" to "Boy", 1908

Human solver: Tomáš Pavuk

**Status: message deciphered in full (41 shifted letters in the body, 10 in the closing). Two short groups, E. L. and N. & L., are reported literally, and one faint word in the closing is restored from context. Independent review: round 1 REVISE (two words reread), round 2 ACCEPT.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1403 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1403), portal name pc_hcp_84. It belongs to the HCPortal collection of cryptographic postcards (private collection). When the record was captured on 2026-10-26, the portal listed it as **Not solved**: Postcard, HCPortal collection, category Substitution, date 1908-02-07, language Unknown, location Europe, sender Unknown, recipient "W. Abboú". No transcription or solution was attached.

The picture side is a Tuck's "Oilette" card (Scottish Rough Seas, Series II), showing **The Ladies Tower, Elie, N.B.** It carries no handwriting.

The cipher is written on the address side, under the address and across the printed publisher's text. The card is scanned sideways; turned 90° counter-clockwise it reads normally. The plain heading is **C. H. Friday**. The address reads, as far as it can be made out, **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon**. The portal's "Abboú" is kept unchanged in the metadata file. The half-penny Edward VII stamp is cancelled **WIMBORNE 10 PM FE 7 08**. 7 February 1908 was a Friday, so the postmark matches the heading.

The card belongs to a series of cipher postcards (HCP 1386 to 1407) sent between one couple in 1907–08 and written in the same Caesar shift. Several of them are deciphered in this repository, for example HCP 1386 and 1406. Like those cards, this one is signed "Girl" and addressed to "Boy". The key was taken as a hypothesis from those sister cards and then checked word by word on this card.

![Picture side: The Ladies Tower, Elie (source/picture.jpg)](../source/picture.jpg)

![Address side turned upright: heading C. H. Friday, five cipher lines and a two-line closing under the address (work/reading.jpg)](../work/reading.jpg)

![Enlarged closing (work/closing.jpg)](../work/closing.jpg)

## Method

The transcription is **manual**. The address side was rotated, enlarged and read word by word; no OCR was used, and the portal supplied no transcription. Every letter is shifted one place forward in the alphabet. The writer kept the dots between words, the apostrophe in *can't* and the quotation marks around *to-night*. Decryption subtracts one from each letter.

The first-round reading had two errors: the greeting was read as `Efbs` (DEAR), and line 4 as `npsf` (MORE). The reviewer showed on 6× enlargements that the greeting is a capital E with a dot, a separate l with a dot, then `Cpz` (BOY), and that line 4 is `mfuufs` (LETTER). Both corrections were confirmed by the solver and then confirmed again in the second review on fresh crops. No sign needs a value other than the −1 shift.

## Key

Caesar shift: each written letter is the plaintext letter + 1.

```
Written: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain:   ZABCDEFGHIJKLMNOPQRSTUVWXY
```

Two short groups are **not** treated as cipher and are kept as written: **E. L.**, which comes before both BOY and GIRL, and **N. & L.** in the closing. Under the shift they would become D. K. and M. & K., neither of which means anything obvious. The same groups are written the same way on the sister card HCP 1386. Their meaning is not known.

## Plaintext

Ciphertext and plaintext, line by line (the writer's dots kept):

| Ciphertext | Plaintext |
|---|---|
| Nz. Pxo. E. l. Cpz. | MY. OWN. [E. L.] BOY. |
| J. bn. tp. Tpssz. | I. AM. SO. SORRY. |
| J. dbo'u. xsjuf. | I. CAN'T. WRITE. |
| mfuufs. | LETTER. |
| "up-ojhiu." | "TO-NIGHT." |
| Nz. N. & L. Zpvs. [Pxo] | MY [N. & L.] YOUR [OWN] |
| E. l. Hjsm | [E. L.] GIRL |

English (normalized; the dots between words are dropped):

> **C. H. Friday. My own E. L. Boy, I am so sorry I can't write letter "to-night". My N. & L. Your [own] E. L. Girl.**

The missing article in "can't write letter" is the writer's own usage. The same writer has "thanks very much for letter" on HCP 1386.

Slovak translation:

> **C. H. piatok. Môj vlastný E. L. chlapec, veľmi ma mrzí, že dnes večer nemôžem napísať list. Moje N. & L. Tvoje [vlastné] E. L. dievča.**

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1403/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the source files and decodes the manual transcript in `work/transcription.json` with the −1 shift. Literal groups (marked `{…}` in the transcript) are left unshifted. For every closing word it checks that re-encoding gives back the written word. It prints each line and the counts (41 shifted letters in the body, 10 in the closing), then a reading assembled from the transcript, checked against the expected text: `MY OWN [E. L.] BOY I AM SO SORRY I CAN'T WRITE LETTER "TO-NIGHT" / MY [N. & L.] YOUR [OWN] [E. L.] GIRL`. The script does not read the image; the transcription step is manual and was confirmed independently in review.

## Uncertainties

- **E. L. and N. & L.** are reported literally. Whether they are plain initials or shifted letters, and what they stand for, is not established. No expansion (for example "many kisses and love") is inserted.
- **[OWN]** after YOUR is a restoration, not a reading. Only a faint P-like diagonal and a long thin stroke are visible. OWN follows the body's "My own" and the closing of the sister cards ("Your own E. L. Girl" on HCP 1386).
- **MY** at the start of the closing (`Nz`) is probable, not certain. The second stroke could also be read as r.
- **E. L. in the closing**: the dots after E and l are not clearly visible there. The group is read by its letter shapes and by analogy with line 1.
- **C. H.** in the heading is plain text, probably a place or house abbreviation. It is not explained.
- The address is partly overwritten and is read only as context. The identities of "Boy" (W. Abbott) and "Girl" are not established beyond the address.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent (Anthropic), two rounds.

- **Round 1, verdict REVISE.** The reviewer reread the card on its own enlarged crops. It found that the greeting `Efbs` (DEAR) was really `E. l. Cpz` ([E. L.] BOY), and that line 4 `npsf` (MORE) was really `mfuufs` (LETTER). It also asked for the faint word after YOUR to be marked as a restoration, for the first closing token (`Nz`) to be marked probable, for the comparison with HCP 1386 to be corrected, and for literal groups to be marked in the transcript. All six findings were accepted, and the reading was resubmitted.
- **Round 2, verdict ACCEPT.** The reviewer ran the reproduction command and its own independent Caesar −1 decoder; both gave the same 41 + 10 letters. It checked every corrected sign on new 4–6× crops and confirmed that 7 Feb 1908 was a Friday. It found only presentation issues: superseded early text in SOLUTION.md, a hard-coded final line in the decoder, and inconsistent notation of E. L. In response, the decoder now builds its reading from the transcript, E. L. is written as one literal group everywhere, and this report uses only the round-2 reading.

What changed because of the review: the salutation (DEAR → [E. L.] BOY), one body word (MORE → LETTER), the status of [OWN] (restored, not read) and of the closing MY (probable).

Credit: download, metadata capture, key identification from the sister cards, and a first partial transcription were made by the OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) on 2026-10-26. The closing reading, the round-1 corrections and this report are by Claude Opus 5.5 acting as solver (2026-10-29/30). The review was made by a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1403, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1403 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4269/conversions/pc_hcp_84_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4270/conversions/pc_hcp_84_adr-large.jpg (source/address.jpg).
- Sister cards of the same couple in this repository, HCP 1386–1407 (in particular ciphers/hcp-1386 and ciphers/hcp-1406).
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no record for this card.
