# HCP 1406 (pc_hcp_87): a Caesar −1 love note to Mr. Abbott, Chudleigh

Human solver: Tomáš Pavuk

**Status: deciphered in full (64 of 64 enciphered letters, one key); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1406 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1406), portal name pc_hcp_87, part of the HCPortal collection of cryptographic postcards (private collection). When captured on 2026-10-26 the portal listed it as **Not solved**, category Substitution, language Unknown, location Europe, sender Unknown, recipient "W. Abboú", with no transcription or solution attached.

The picture side is a Raphael Tuck & Sons "Oilette" postcard 7280, *Scottish Rough Seas*, showing Barra Head; it carries no handwriting. All the writing is on the address side. The address, in plain writing, reads **Mr. Abbott, Stokelake Farm, Chudleigh, S. Devon**. The card has a green halfpenny Edward VII stamp cancelled **WIMBORNE … 10 PM**; the day, month and year of the postmark cannot be read.

The message is written to the left of and below the address, sideways to the printed text (it reads upright after a 90° counter-clockwise turn of the scan). It opens with a plain heading **"C. H. Sunday."** followed by seven lines in cipher.

The card belongs to a run of cards to Mr. W. Abbott in this repository (HCP 1386–1407, 1907–08) written in the same hand with the same Caesar shift and the same set phrases, for example on HCP 1386 "My own E. L. boy … My N. & L. from your own E. L. girl" and on HCP 1397/1407 the quoted "to-Day". No published solution of this card was found.

![Picture side (source/picture.jpg)](../source/picture.jpg)

![Address side with the cipher message (source/address.jpg)](../source/address.jpg)

![Message area turned upright for reading (work/reading.jpg)](../work/reading.jpg)

## Method

The transcription is **manual**, from enlarged crops of the rotated address side (work/crops/), not OCR. Each enciphered word was shifted back by one letter. Because the writer's family of cards is known to use this shift, the key was tested first and immediately gave English for every group; long words such as `joeppst` → INDOORS and `npsojoh` → MORNING leave no room for another key.

An earlier GPT pass (2026-10-26) identified the key and read 49 letters, but guessed the greeting as `Efbs` (DEAR) and left MORNING and the closing open. Claude Opus 5.5 re-read the whole card from the pixels on 2026-10-29, read the greeting as `E. L. Cpz` and the closing as `Nz. N. & L. gspn.` / `Pxo. E. L. Hjsm.` by comparison with HCP 1386, and corrected the address ("Stokelake", not "Whiteway").

In review, a separate Claude Opus 5.5 agent rotated and enhanced the scan itself, read all eighteen groups by hand and decoded them with its own script (review/work/indep.py); its result agreed with the solver's in all 64 letters.

## Key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet; decipherment subtracts one.

```text
cipher: ABCDEFGHIJKLMNOPQRSTUVWXYZ
plain:  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

Punctuation, the hyphen and the quotation marks are written in clear. The abbreviations `E. L.` and `N. & L.` are kept as written (see Uncertainties).

## Plaintext

| Ciphertext (as written) | Plaintext |
|---|---|
| C. H. Sunday. *(plain)* | C. H. Sunday. |
| Nz. Pxo. E. L. Cpz. | MY. OWN. [E. L.] BOY. |
| Mfuufs uijt npsojoh | LETTER THIS MORNING |
| wfsz ojdf. | VERY NICE. |
| J. bn. joeppst | I. AM. INDOORS |
| bmm "up-Ebz." | ALL "TO-DAY." |
| Nz. N. & L. gspn. | MY. [N. & L.] FROM. |
| Pxo. E. L. Hjsm. | OWN. [E. L.] GIRL. |

**English (normalized):** "C. H., Sunday. My own E. L. boy, letter this morning very nice. I am indoors all 'to-day'. My N. & L. from own E. L. girl."

**Slovak translation:** „C. H., nedeľa. Môj vlastný E. L. chlapec, list dnes ráno veľmi pekný. Celý ‚dnešok' som doma. Moje N. & L. od tvojho vlastného E. L. dievčaťa."

Notes: the writer leaves out "your" in the closing ("from own E. L. girl"); on HCP 1386 the formula is "from your own E. L. girl". "C. H." in the heading is plain and unexplained (perhaps a place or house name).

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1406/work/decode_v2.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the files in source/, decodes the manual transcription in work/transcript-v2.json with the shift −1, asserts that the result equals the expected text and prints it, ending with `-- source hashes OK; 64 enciphered letters decoded with one key (shift -1); abbreviations E. L. / N. & L. kept literal`.

## Uncertainties

- **E. L. and N. & L.** are kept literal. Shifted back they would be D. K. and M. & K.; whether they are enciphered at all, and what they mean (for example "ever loving"), is not established. They are treated the same way on the sister cards.
- **The `z` of `Cpz` (BOY)** lies under the printed grey "O" of the portal's cipher-wheel watermark; only a short ink stroke and a dot are visible. The reading BOY rests partly on the identical greeting `Nz. Pxo. E. L. Cpz.` of HCP 1386.
- **`Pxo` (OWN)**: the `x` is a small cross on the stem of a large flourished P, so the group can look like "Fo"; the same construction occurs on HCP 1386.
- **`Ebz` (DAY)** resembles "E62"; with `up-` and the quotation marks it reads "to-Day", as on HCP 1397 and 1407.
- **Small marks.** Two slanted ticks before `wfsz` at the start of line 3 look like an opening quotation mark ("very nice" may have been meant as a quotation), but no closing mark is visible after `ojdf.`. A "V"-shaped mark below the end of line 2 is the turned-up descender of the j in `npsojoh`, and a tiny dot next to it is its dot or a stray mark. None of these is a letter.
- **Date.** Only "Sunday" is written and the postmark date is illegible, so no year is claimed; the series is dated 1907–08.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), decrypted its own hand-typed transcription with its own script (64 letters, same result), and checked every line against 3–5× enlargements of the rotated scan. It confirmed that no group is a forced restoration and that the address, postmark and formulas fit the Abbott series. Its three findings were minor:

- **Marks near lines 2/3** (possible opening quotation mark before "very nice", a tick near the j-descender): now recorded in SOLUTION.md and in the uncertainties above; no letter changed.
- **Weak `z` in `Cpz`**: the wording now says plainly that the letter is barely visible and that BOY depends partly on the sister-card formula.
- **E. L. / N. & L.**: kept literal and disclosed, as before.

No decoded letter changed as a result of the review.

## Credit

Download, metadata capture, key identification and a 49-letter partial transcription by the OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol), 2026-10-26. Completion of the transcription and decipherment, the response to review and this report by Claude Opus 5.5 acting as solver, 2026-10-29/30. Independent review by a separate Claude Opus 5.5 agent.

## Sources

- HC Portal record 1406, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1406 (source/metadata.md, SOURCES.md).
- Picture and address side scans from the portal (source/picture.jpg, source/address.jpg).
- Sister cards to W. Abbott in this repository: ciphers/hcp-1386, hcp-1397, hcp-1407.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29: no entry for this card.
