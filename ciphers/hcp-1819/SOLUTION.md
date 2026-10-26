# Portal 1819 / pc_hcp_500 — complete candidate, awaiting review

## Plaintext

**GO HOME ON SATURDAY**

Slovak: **Choď domov v sobotu.**

All 16 encrypted symbols on the address side are included. The separate
Love from A.E.S. is unencrypted source text, not deciphered material.
No cipher text was observed on the picture side.

## Cipher and key

Alternating undotted/dotted Pigpen, transferred from preceding postcard
work. The family is already labelled Pigpen by the catalogue.

| Outline strokes / wedge | Token | Undotted | Dotted |
|---|---|---|---|
| bottom/right | BR | A | B |
| bottom/left/right | B | C | D |
| bottom/left | BL | E | F |
| top/bottom/right | R | G | H |
| four sides | C | I | J |
| top/bottom/left | L | K | L |
| top/right | TR | M | N |
| top/left/right | T | O | P |
| top/left | TL | Q | R |
| downward V | V | S | T |
| right-pointing wedge | > | U | V |
| left-pointing wedge | < | W | X |
| upward wedge | ^ | Y | Z |

The text follows a curved feather. Orient glyphs by their local baseline.
A 270-degree working rotation makes GO HOME horizontal; later glyphs turn
along the curve. This is an orientation convention applied to the writing,
not a change of alphabet or a word-specific key.

## Reproduction

From repository root:

```sh
python3 ciphers/hcp-1819/work/decode.py
```

The command checks source hashes and maps the disclosed manual symbolic
transcript in work/transcription.txt. It does not OCR the scan or infer
local rotations automatically. The portal supplied no transcription.
Independent visual review must check orientation and dots against pixels.

## Evidence and limits

The unchanged key maps every entered glyph and repeats O and A
consistently. No cipher token is left unresolved or filled from a guessed
word. Exact token roundtrip proves internal consistency only. Sixteen
letters provide limited statistical evidence; local rotations and the
large scan watermark require independent collation. No sender identity,
travel event or postmark date is independently established. No published
target plaintext used; no historical-priority claim. This is portal record
1819, named pc_hcp_500, not portal record 500. Review pending; no final
accepted report or register entry.

## Response to review 1

Reviewer: Claude Opus 5.5, verdict ACCEPT (review/REVIEW1.md, 2026-10-26). The reviewer read the 16 signs from source/address-large.jpg in their local writing orientation, in its own notation, decoded them with its own script built from the alternating alphabet, and found no difference from work/transcription.txt. The plaintext GO HOME ON SATURDAY is unchanged.

1. Reproduction maps a manual transcription (minor). Accepted. The local rotations remain a manual judgement, not computed. The report now states that review 1 confirmed all 16 tokens independently against the scan.
2. Two signs depend on the assumed local orientation (minor). Accepted and made the stated residual risk in place of the earlier general wording about watermark and rotations. The N of ON is a dotted corner where the line starts to bend; without a fixed baseline it could be taken for a dotted ">" wedge (giving OV). The S of SATURDAY is a near-right-angled wedge that could pass for a bottom+left outline if the baseline were taken more vertical. Only the adopted reading gives English, and the same orientation rule (local "up" = the reader's left of the writing direction) reads all other signs without strain.
3. Protocol (minor). Acknowledged. The directories source/ and work/ have a modification time of 00:22:40 local, about 100 seconds after DONE1 (00:20:59 local), so an entry was added to or removed from both after the marker. All files now present predate the marker and the source hashes in work/source-sha256.json still match, so the reviewed material is the material handed over. What the transient entry was cannot be established from the files; it is recorded here as a protocol lapse. Nothing in source/ or work/ is changed in this closing round.
4. Key transferred, not rediscovered (minor). Accepted. The report names the system: alternating undotted/dotted Pigpen, two letters per cell, with a plain 3×3 grid for A–R and an X-grid for S–Z. It states that the alphabet came from earlier postcard work and that 16 signs (13 distinct) confirm it only because the result is fluent English.

Context corrections carried into the report (from the reviewer's reading and the scan; source/metadata.md is not edited): the address side is postmarked TAMWORTH, 7.45 PM, DE 22, year hidden by the stamp, so 1904 rests on the catalogue. With 1904-12-22 a Thursday, the following Saturday is 24 December, Christmas Eve, which fits the message. The addressee's surname reads most naturally as Kite on the scan; the catalogue gives Kile; it is not treated as settled. The address is Standon Green End, High Cross, near Ware, Hertfordshire; the plain closing "Love from A.E.S." is not part of the cipher and the sender is not identified.

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-26.
