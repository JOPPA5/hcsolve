# HCP 1453 (pc_hcp_134): a postcard in American Morse from Washington, D.C., 1906

Human solver: Tomáš Pavuk

**Status: deciphered in full as far as the card is legible (137 of 137 main-text letters, plus a two-letter terminal item read R S; one cancelled box illegible and unread); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1453 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1453), portal name pc_hcp_134, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection and Morse code, category Substitution, date 1906-06-11, language Unknown, location North America, sender Unknown, recipient Carl Schmitt, with no transcription or solution attached.

The picture side is a real-photo postcard of the **Treasury Building** in Washington (handwritten caption "Treasury Building"). Across the top the writer added in plain hand **Washington, D.C., June 11 '06**. The right-hand margin carries the message: three narrow ruled columns filled with rows of dots and dashes, each column headed by a curved arrow pointing down. The address side is to **Carl Schmitt, Warren, Ohio**, with a Washington postmark (its date digits are only partly legible at the available resolution).

A writer in the United States in 1906 who knew "Morse" would have known the **American (railroad, landline) Morse** code used on US telegraph lines, not the International (Continental) code used in radio and in Europe. American Morse has letters made of dots separated by an internal space (O, R, C, Y, Z) and a long dash for L, and it is these features that unlock the card.

![Picture side (source/picture.jpg). The cipher columns are on the right; the grey alphabet wheel and other overlays are the HCPortal watermark, not part of the card.](../source/picture.jpg)

![The three cipher columns, enlarged (work/cipher-large.jpg). Read each column top to bottom, left column first; ruled lines separate words. The six large dots at the bottom right are the terminal item R S.](../work/cipher-large.jpg)

![Address side: Carl Schmitt, Warren, Ohio (source/address.jpg)](../source/address.jpg)

Other marks on the card, none of them cipher: the plain heading and caption, the arrows heading each column, the ruling between words, the printed postcard text, the address, stamp and postmark, and the HCPortal watermark on both sides.

## Method

The transcription is **manual**. Each column was cropped and enlarged from the scan, and every word box was transcribed as a sequence of rows, one horizontal row of marks per letter, keeping the internal spaces inside spaced-dot letters and distinguishing the long dash (L) from the ordinary dash (T). The 137 letters are frozen in work/transcript.json. No OCR was used and the portal supplied no transcription.

Ordinary International Morse does not give text (a spaced `. .` would be two Es, and the long dash would have no meaning). With the American Morse alphabet the first box reads `..` = I, the second `--. / . . / -` = G O T, and one fixed key then reads all three columns as continuous English with no unmapped row. Diagnostic letters are visible on the scan: the spaced dots of O, R, C and Y (for example ORCHESTRA beginning `. . / . .. / .. .` and YESTERDAY beginning and ending with `.. ..`), the long dash of L in HOLE, SELL, DOLLAR, BROOKLAND and SKULL, about twice the length of the T dashes of GOT, IT and AT, F `.-.` in FOR, P as five dots in PM and CAP, and K `-.-` in BROOKLAND and SKULL. Early visual guesses (BROOKLYN, AM HERE) were rejected on enlarged crops in favour of the readings the marks actually give (BROOKLAND, AT HOME).

Two places needed separate treatment:

- **The terminal dots.** After HOME, at the bottom of the third column, stand six larger dots in two rows: upper one dot, a gap, two dots; lower three evenly spaced dots. Their spacing was measured on the original pixels (connected components at several thresholds) and compared with ordinary R and S letters on the same card: the upper row's gap ratio (about 2.2) matches the R in WEARING and WEAR (2.1–2.3), the lower row's (about 1.1) is near-equal like the S in SKULL. Under the same key, `. ..` / `...` = **R S**.
- **The cancelled box.** In column 1, between A and HOLE, one box is struck through with dense diagonal hatching over a short row of marks. At 8× enlargement only a dot or two and a dark dash run can be seen under the hatching; nothing is legible, and nothing is read from it.

![The terminal dots, enlarged (work/agent-terminal-large.jpg)](../work/agent-terminal-large.jpg)

![The cancelled box between A and HOLE, enlarged (work/agent-cancelled-large.jpg)](../work/agent-cancelled-large.jpg)

In review, a separate agent made its own 5× crops of all three columns and 8× crops of the two special places, read every box against the transcript, and decoded the transcript with its own independently written American Morse table (review/work/indep_decode.py). It obtained the same 137 letters.

## Key

American Morse (railroad/landline Morse). A space inside a code is part of the letter; `=` marks the long dash of L, `-` the ordinary dash.

| Letter | Code | Letter | Code | Letter | Code | Letter | Code |
|---|---|---|---|---|---|---|---|
| A | `.-` | H | `....` | O | `. .` | V | `...-` |
| B | `-...` | I | `..` | P | `.....` | W | `.--` |
| C | `.. .` | J | `-.-.` | Q | `..-.` | X | `.-..` |
| D | `-..` | K | `-.-` | R | `. ..` | Y | `.. ..` |
| E | `.` | L | `=` (long dash) | S | `...` | Z | `... .` |
| F | `.-.` | M | `--` | T | `-` | | |
| G | `--.` | N | `-.` | U | `..-` | | |

J, Q, X and Z do not occur in the text; all other letters do.

## Plaintext

Literal decoded text, column by column (word division follows the ruled boxes):

```text
Column 1: I GOT IN A [cancelled box] HOLE AND HAD TO SELL THAT ORCHESTRA CARTOON
Column 2: FOR A DOLLAR WENT OUT TO BROOKLAND YESTERDAY PM I HAVE
Column 3: BEEN WEARING A SKULL CAP WONT HAVE THE NERVE TO WEAR IT AT HOME
Terminal: R S
```

Normalized English (sentence punctuation, the apostrophe in won't and "p.m." are editorial; the card has WONT and PM):

**I got in a hole and had to sell that orchestra cartoon for a dollar. Went out to Brookland yesterday p.m. I have been wearing a skull cap. Won't have the nerve to wear it at home. — R. S.**

Slovak translation: **Dostal som sa do tiesne a musel som predať tú karikatúru orchestra za dolár. Včera popoludní som bol v Brooklande. Nosím priliehavú čiapku. Doma by som sa ju neodvážil nosiť. — R. S.**

Notes on the reading:

- **"Got in a hole"** is the colloquial American idiom for being in a fix, usually short of money, which fits selling the cartoon for a dollar.
- **Brookland** is a neighbourhood in north-east Washington, D.C., matching the heading, the Treasury Building picture and the Washington postmark.
- **Skull cap** is a close-fitting brimless cap; the writer jokes that he would not dare wear it at home.
- **R S** is probably the writer's initials, set apart at the end like a signature; this is an interpretation from its position, not a proven fact. The addressee is Carl Schmitt, so a family member with the initials R. S. is conceivable, but no sender is identified.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1453/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the scans, decodes the manual transcription in work/transcript.json with the American Morse key, re-encodes every word and checks it against the transcription, and prints the three columns and the line `137 mapped letters; source hashes and transcript/key roundtrips pass.`. It then decodes the two terminal rows (patterns from work/terminal-scope.json) with the same key as a separate item, printing `Signature (terminal larger dots, separate item): R. S.`, and states that the cancelled box is unread. It does not read the image; the transcription step is manual and was checked independently in review. The pixel spacing measurements of the terminal dots are reproduced by work/measure-terminal-pixels.py (needs Pillow).

## Uncertainties

- **The cancelled box** (column 1, between A and HOLE) is illegible under the hatching and unread. It is most likely a false start struck out by the writer; the message reads continuously without it ("I got in a hole").
- **R S** as a reading of the terminal dots rests on their spacing, measured against R and S elsewhere on the card; that they are initials or a signature is interpretation. Who R. S. was is unknown.
- **Editorial marks.** Word division follows the ruled boxes; sentence punctuation, "won't" and "p.m." are editorial.
- **"Orchestra cartoon"**: what cartoon was meant, and the sale, are not traced in any external record.
- The postmark date on the address side is only partly legible; the date rests on the handwritten heading June 11 '06 and the portal metadata.
- No published solution of this card was found: the portal showed Not solved and no attachment, and the AI Decipherment Register had no entry for it (checked 2026-10-29). Only a generic American Morse table was consulted.

## Review summary

Reviewer: Claude Opus 5.5 (Anthropic), a separate agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command (output identical to the claimed plaintext), decoded the transcript with its own independent American Morse table, and read every box of all three columns on its own enlargements against the transcript, with full agreement. It confirmed the diagnostic American Morse letters on the pixels, reproduced the terminal-dot measurements, agreed that the cancelled box is illegible, found the English natural for the period and consistent with the Washington context, and found no undisclosed published solution. Its five findings were minor and are reflected here:

- **Inconsistent status in SOLUTION.md.** The header now gives the current status and marks the earlier "partial" passes as history.
- **Single command.** decode.py now also prints the terminal item R S (decoded with the same key) and the status of the cancelled box.
- **R S stated too firmly.** Now given as "probably initials / a signature"; no sender is identified.
- **Cancelled box.** Stated explicitly as illegible and unread.
- **Editorial marks.** Disclosed in this report.

No decoded letter changed as a result of the review.

Credits: the transcription and decipherment of the 137-letter main text, and the pixel measurements of the terminal dots, were made by an OpenAI GPT solver (GPT-6 Astra) on 2026-10-26. Claude Opus 5.5 completed the solution on 2026-10-29 (reading of the terminal item and the cancelled box, handover), addressed the review and prepared this report.

## Sources

- HC Portal record 1453, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1453 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4419/conversions/pc_hcp_134_pic-large.jpg (source/picture.jpg).
- Address side: https://api.hcportal.eu/media/4420/conversions/pc_hcp_134_adr-large.jpg (source/address.jpg).
- American Morse alphabet: U.S. Army Extension Courses, Military Cryptanalysis Part I (1936–37), comparison table, hosted by the NSA: https://www.nsa.gov/Portals/75/documents/news-features/declassified-documents/friedman-documents/publications/FOLDER_246/41748769078795.pdf
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-10-29.
