# HCP 1188: a Pigpen postcard signed Jesse Darrow

## Origin and material

This postcard is held in the Tobias Schrödel Collection and catalogued by HC Portal as `cpc_1913-04-02_USA_Gr_USA__` (portal 1188), dated 2 April 1913, North America. The rendered General, Description and Attachments tabs were captured on 25 October 2026. At capture the portal labelled it Not solved and Pigpen; it supplied no transcription or solution.

The address side contains an eight-line encrypted message. The picture side shows two oversized apples on a rail wagon, captioned “The Kind We Raise in Gray, N. Y.”; it has no observed encrypted continuation. The original scans and captured metadata are preserved in source/. The cursive recipient and precise postmark remain tentative. The catalogue date is reported metadata rather than an independently recovered date.

## Method and recovered key

The cipher is Pigpen with adjacent undotted/dotted letter pairs. The grid outlines carry A-R, and four wedge pairs carry S-Z. A manually read list accounts for all 114 signs; the same alphabet applies throughout. No sign receives different values to make a word fit.

| Present borders / wedge | Token | Undotted | Dotted |
|---|---|---|---|
| bottom/right | BR | A | B |
| bottom/left/right | B | C | D |
| bottom/left | BL | E | F |
| top/bottom/right | R | G | H |
| all four borders | C | I | J |
| top/bottom/left | L | K | L |
| top/right | TR | M | N |
| top/left/right | T | O | P |
| top/left | TL | Q | R |
| downward wedge | V | S | T |
| rightward wedge | > | U | V |
| leftward wedge | < | W | X |
| upward wedge | ^ | Y | Z |

## Literal plaintext

Spaces between words are editorial. The manuscript's unusual spellings are retained.

```text
DEAR FRIEND AS I
NOW TAKE TIME AND
PLEASURE OF WRITINH
TOYOU IF NOT TO
STORMY WILL BE UP
WEDNESDAY EVENING
RESPFULLY YOURS
JESSE DARROW ANS
```

The final sign of WRITINH is dotted H, not G. The second R of DARROW has a smaller dot against its inner stem. Both are actual glyph readings incorporated after review.

## Interpretation and Slovak translation

A readable English interpretation is: “Dear friend, as I now take time and pleasure of writing to you: if not too stormy, [I] will be up Wednesday evening. Resp[ect]fully yours, Jesse Darrow. Ans.”

This corrects WRITINH to WRITING and TO to TOO, supplies [I] for grammar, and expands RESPFULLY. ANS may request an answer; that gloss is not itself encoded in full.

Slovak: „Milá priateľka / milý priateľ, teraz si nachádzam čas a potešenie napísať ti. Ak nebude príliš búrlivo, prídem v stredu večer. S úctou tvoj, Jesse Darrow. Odpíš [pravdepodobný význam ANS].“

## Review and resulting corrections

Claude Opus 5.5 independently reviewed every sign and implemented a separate decoder on 26 October 2026. Review 1's verdict was REVISE: the decipherment and key were correct, but two transcription records required correction. The reviewer explicitly stated that these record corrections required no further review round.

1. The surname's second TL was corrected from undotted Q to dotted R. The small dot is visible beside the stem; the adjacent stain affects the following O. The current literal signature is JESSE DARROW.
2. The last sign of the third line was corrected from undotted G to dotted H. The literal word is WRITINH; WRITING remains an editorial correction.
3. TO/TOO, supplied [I], RESPFULLY and ANS retain the distinction between literal letters and interpretation.
4. The decoder's token-roundtrip assertion was removed. Such a roundtrip tests a mapping implementation, not the manual reading of an image. File hashes establish integrity only; the source collation and review crops provide the transcription evidence.

## Uncertainties and reproduction

The small signature dot and nearby ink stain deserve attention when consulting the scan, but the review supports DARROW directly rather than as restoration. The name is not a verified historical identity. Exact recipient, address and postmark remain tentative. No published target plaintext was used and no priority is claimed.

From the repository root, run:

```sh
python3 ciphers/hcp-1188/work/decode.py
```

The command checks preserved source hashes and prints the literal eight-line message from the manual token list: 114 signs, 22 distinct. It does not perform OCR. The immutable scan, manual transcript, independent review and this report together document the result.

Source: https://crypto.hcportal.eu/dashboard/cryptograms/1188. Review record: review/REVIEW1.md. This report source incorporates all requested record corrections; final PDF verification and state marking are separate production steps.
