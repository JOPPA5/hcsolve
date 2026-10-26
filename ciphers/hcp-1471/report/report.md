# HCP 1471 (pc_hcp_152): a shift-by-one postcard question, "Are we downhearted?"

**Status: deciphered in full; independent review 1 verdict ACCEPT.** Report dated 2026-10-26.

## Origin and context

The cryptogram is record 1471 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1471), portal name pc_hcp_152, in the HCPortal cryptographic postcards collection (private collection). When it was acquired on 2026-10-26 the portal listed it as **Not solved**, category Substitution, language Unknown, date 1906-05-16, recipient "Miss Puklett", with no transcription or solution attached.

The picture side shows "Lodge and Drive, Parkwood, Swanley" and carries no cipher. The address side is postmarked 5.30 PM, MY 16 06 (Wednesday 16 May 1906) and addressed, for local delivery, to Miss Puplett, Beulah, Birchwood Avenue, Swanley Junct. The card clearly reads Puplett; the portal's "Puklett" is a misreading (the captured source file is left unchanged). The cipher is a single line of 16 cursive letters and a question mark, written diagonally across the left half of the address side. Collector's pencil marks and a red 9 are not part of it.

![Address side; the cipher runs diagonally up the left half (source/address-large.jpg)](../source/address-large.jpg)

## Method

The transcription is **manual** (work/transcription.txt); the portal supplied none. The solver rotated a working copy by 45 degrees to read the diagonal handwriting and transcribed it as

```text
a^qd vd cnvmgda^qsdc?
```

where a^ is an a with a small caret written beneath it. Shifting every ordinary letter one place forward (q→R, d→E, v→W, c→D …) gives _RE WE DOWNHE_RTED?, and the two marked a's, identical to each other, fill the gaps as A. One fixed shift thus accounts for all 14 ordinary letters and one consistent mark for the other two; every letter on the card is used and nothing is supplied.

In review the line was read independently from rotated, enlarged crops of the scan before comparison, with an identical result, and decoded with an independently written script.

## Key

Each plaintext letter is written as the letter before it in the alphabet: a Caesar shift of −1 for encryption, +1 for decryption. The single letter that would wrap round, A (which would become z), is instead written as a with a caret beneath it; the mark thus flags the one letter to which the shift is not applied.

| Plaintext | A | B | C | D | E | … | H | … | N | O | … | R | S | T | … | W | … | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Written | a with caret | a | b | c | d | … | g | … | m | n | … | q | r | s | … | v | … | y |

Mappings actually observed on the card: a with caret→A, c→D, d→E, g→H, m→N, n→O, q→R, s→T, v→W.

## Plaintext

As written (with the literal decoded letters beneath):

```text
a^ q d   v d   c n v m g d a^ q s d c ?
A  R E   W E   D O W N H E A  R T E D ?
```

Normalized English: **Are we downhearted?**

Slovak translation: **Sme skľúčení?**

Context, not part of the decipherment: "Are we downhearted? – No!" was a well-known British catchphrase of the time, associated with Joseph Chamberlain around 1906 and later a familiar soldiers' chant. A postcard dated May 1906 asking the question fits that period. The attribution is given from general knowledge and was not checked against an external source; the phrase played no part in obtaining the reading.

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-1471/work/decode.py
```

The script checks the SHA-256 hashes of the source files, decodes all 16 letters of the manual transcription in work/transcription.txt, checks the inverse mapping and both caret exceptions, and prints the two rejected alternative readings. It does not read the image.

## Uncertainties

- Third letter of the last word: read v (as in "vd"); a w would give DOXNHEARTED. Solver and reviewer both read a single v with a looped flourish and no second stroke.
- Last letter: heavily inked and overprinted by the printed word UNION, so its shape is blurred; it is read c because it must encode the same D as the clear initial c of the word. An e would give DOWNHEARTEF.
- The meaning of the caret is inferred from where it occurs (only on the wrapping letter A); the writer's intention is not documented.
- The writer is not identified, and it is unknown whether the question alludes to the slogan, to a private matter, or both.
- The prior-solution check was limited to the portal attachments and an export of the AI Decipherment Register; earlier publication elsewhere cannot be excluded.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the stored check file), read all 16 letters and both carets from its own rotated crops before comparing, decoded them with its own script, examined the two flagged letters at about 15× enlargement and resolved both in favour of the solver's reading. Its four findings were minor and are reflected here:

- The key is now described plainly as a shift by one, with the caret explained as the marker for the single wrapping letter A.
- The 1906 catchphrase "Are we downhearted? – No!" is mentioned as context, clearly separated from the decipherment.
- The recipient's name is given as written on the card, Miss Puplett, not the portal's "Puklett".
- The missing spaces in the solver's working text are not carried into this report.

No change to the plaintext resulted from the review. The closing steps (response to review, this report, the register entry) were prepared by Claude Opus 5.5 on the solver's behalf at the human's request; the decipherment itself was made by the solver, OpenAI GPT (GPT-6 Astra).

## Sources

- HC Portal record 1471 (pc_hcp_152), General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1471 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4474/conversions/pc_hcp_152_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4473/conversions/pc_hcp_152_pic-large.jpg (source/picture-large.jpg).
- AI Decipherment Register export, 2026-10-26: https://ai.hcportal.eu/register/?format=json (no matching entry; not a plaintext source).
