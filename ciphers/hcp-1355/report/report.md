# HCP 1355 (pc_hcp_36): an English Caesar sweetheart postcard, 30 March 1907

Human solver: Tomáš Pavuk

**Status: deciphered in full (81 of 81 enciphered letters). Two spellings of the writer are kept as written, and a few weak signs are disclosed. Independent review 1 verdict ACCEPT; no decoded letter changed.** Report dated 2026-10-30 (UTC).

## Origin and context

The cryptogram is record 1355 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1355), portal name pc_hcp_36. It is part of the HCPortal collection of cryptographic postcards. When the card was captured on 2026-10-30, the portal listed it as follows:

- status **Not solved**;
- tags Postcard and HCPortal collection;
- category Substitution;
- date 1907-03-30;
- language Unknown, location Europe;
- sender Unknown, recipient "W. Abboú".

No transcription or solution was attached. No published solution of this card is known or was used. The AI Decipherment Register had no record of it on 2026-10-30, but no separate web search was made.

The picture side is a printed view, "English Lakes. Honister Crag" (the last word of the caption looks like "Cray" at this size). It carries no handwriting.

The address side has a halfpenny Edward VII stamp and the postmark **WIMBORNE / 10 PM / MR 30 / 07**, which matches the portal date. The address is written in plain to **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon**. The portal's "Abboú" is a misreading of Abbott.

The message stands sideways on the left half of the address side; turn the scan 90° counter-clockwise to read it. Line 6 begins in the far left margin, beyond the printed text. A plain heading, "C. H. Saturday evening.", comes first. The rest is enciphered.

30 March 1907 was a Saturday, as the heading says, and a 10 PM postmark fits "evening". The next day, 31 March 1907, was Easter Sunday. Both dates are computed.

The card belongs to a series of Caesar-enciphered postcards addressed to W. Abbott, with the same hand, addressee and Wimborne postmarks. Other cards of the series are deciphered in this repository (for example HCP 1386 and 1407).

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![Address side turned 90° counter-clockwise for reading (work/reading.png)](../work/reading.png)

![Picture side, no handwriting (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual. The solver rotated the original scan (work/hires/pc_hcp_36_adr.JPG) and read each line from 4–7× enlargements. No OCR was used.

The sister cards suggested a shift of one, and that shift fitted at once. Letter frequency confirms it without relying on the sister cards: scoring all 26 shifts against English gives this shift 6.09 and the next best 4.87.

Some first readings were corrected on the enlargements before handover, always by rereading the signs and never by altering the key:

- The first word of line 2, first taken as a three-letter group, is `Cffo` (BEEN) once the two long f's are separated.
- The left-margin group, first taken for initials, is `Xjui` (WITH).
- The start of line 4 first looked like `Gbsmz`, but its stem matches `f`, not the `G` of `Gspn`.

The sequence in the reproduction script is: check the file hashes, decode the transcription with the fixed shift, and print each line and the letter count. Run it from the repository root:

```text
python3 -I ciphers/hcp-1355/work/solve.py
```

## Key

Caesar shift. Each plaintext letter is written as the next letter of the alphabet; decipher by subtracting one, with A going to Z.

```text
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The one shift applies to every letter, with no exception. Cipher letters a, l, q, r and y do not occur, which is normal in 81 letters. The heading is ordinary writing and is not shifted.

## Plaintext

| Line | Ciphertext | Plaintext |
|---|---|---|
| heading (clear) | C. H. Saturday evening. | C. H. Saturday evening. |
| 1 | Nz. Efbsftu. kvtu | MY. DEAREST. JUST |
| 2 | Cffo. gps. b. tuspmf | BEEN. FOR. A. STROLE |
| 3 | J. bn. hpjoh. up | I. AM. GOING. TO |
| 4 | Fbsmz. Tfswjdf. | EARLY. SERVICE. |
| 5 | Tvoebz. Npsjoh | SUNDAY. MORING |
| 6 | Xjui Mpwf. Gspn. zpvs | WITH LOVE. FROM. YOUR |
| 7 | Hjsm. | GIRL. |

The original language is English. With spelling normalised:

*C. H. Saturday evening. My dearest, just been for a stroll. I am going to early service Sunday morning. With love from your girl.*

Slovak translation:

*C. H., sobota večer. Môj najdrahší, práve som bola na prechádzke. Idem na rannú bohoslužbu v nedeľu ráno. S láskou tvoje dievča.*

## Uncertainties

The writer's spellings are kept in the literal plaintext and normalised only in the reading above.

- **MORING (`Npsjoh`).** The syllable NI is missing. After `s` come the long `j`, then `o` and `h`, with no room for an `o` before the `j`. This is read as the writer's slip for MORNING.
- **STROLE (`tuspmf`).** One `m` is read. The strokes are cramped, but the reviewer counted three downstrokes at 8×, and six would be needed for `mm`. Either way the word is "stroll".
- **Final `s` of `gps`.** Only a dark blob survives where the pen ran dry. It is read as `s` because FOR is the only fit, so treat it as close to a restoration.
- **`w` of `Mpwf`.** A pale smudge and one short dark stroke, read partly from fit. LOVE is safe, since `M`, `p` and `f` are clear.
- **Capital `F` of `Fbsmz`.** No sister card gives this capital for comparison. The stem runs through and past the bowl like the `f` of `Cffo`, unlike the `G` of `Gspn`. A G would give FARLY, which is not a word.
- **Heading.** The initial may be G rather than C, and the meaning of the initials is unknown. They are not expanded. The last word is dark but cramped, so "evening" is probable, supported by the 10 PM postmark. The heading is clear text, outside the 81 letters.
- **Identity.** The writer is not named on this card. The early service fits Easter Sunday, but the card does not say so.

## Review

An independent Claude Opus 5.5 reviewer tried to refute the reading. It ran the reproduction command, typed its own transcription from its own crops, built the key separately and decoded with its own script: all seven lines and all 81 letters agree. It reread every line at 4× and the doubtful places at 6–8×, checked the stops and the scan's hash, and judged the English natural for the period.

Verdict **ACCEPT**, with four minor findings about how the uncertainties were worded:

- The `w` of `Mpwf` is weaker than first stated. It is now listed as a weak sign.
- The hook under the `X` of `Xjui` was first described as part of the `X`. It is the tail of the following `j`, so the word has no unusual form. The note was corrected.
- The heading's last word was called faint. It is dark but cramped, and is now called probable.
- A note in the transcription file gave the wrong line number for the left-margin line. It now says line 6.

No decoded letter, line or stop changed because of the review. The reviewer could not settle the heading's initial or the meaning of "C. H.", and it made no web search for a published solution.
