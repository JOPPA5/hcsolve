# HCP 1438 / pc_hcp_119 — solver candidate

## Source and scope

The portal was freshly observed as **Not solved** on 2026-10-26. General,
Description and both attached scans were captured by the coordinating
solver; no supplied transcription or solution was attached. The postcard
is dated 1908-05-28, addressed to Ray Bartley in Laurens, Iowa. Portal
language is Unknown; the decoded text is English.

This claim covers **all 36 observed Pigpen glyphs**, in two narrow margin
lines on the address side. Rotate the address scan 270 degrees clockwise
to read them horizontally. `P.S.` is ordinary Latin script, not encrypted.
The main address-side message is ordinary cursive. The cat picture and its
printed caption contain no observed encrypted continuation.

The geometric transcription is manual, made directly against the original
scan and enlarged crops. The decoder is not OCR. No published decipherment
was used.

## Cipher and key

Three-count Pigpen: the same nine tic-tac-toe outlines are reused with one,
two or three dots. The nine outline cells, read row by row, are:

| Dots | BR `┘` | B `∪` | BL `└` | R `]` | C `□` | L `[` | TR `┐` | T `∩` | TL `┌` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A | B | C | D | E | F | G | H | I |
| 2 | J | K | L | M | N | O | P | Q | R |
| 3 | S | T | U | V | W | X | Y | Z | unused |

The `∪`/`∩` signs here describe three straight sides, not curved glyphs.
All letters use the one fixed table; no word-specific reassignment is made.

## Literal plaintext

```text
RLEAS BRING MY LETTERS
WITH YOU SAT IF U COME
```

Commas/dot separators occur between some groups; they are represented as
spaces above. The five-letter opening is retained **RLEAS**, exactly as
the manual outline/dot transcript decodes. It has not been silently
corrected to PLEASE. `SAT` and `U` remain the source's abbreviations.

Slovak translation, with the opening interpreted explicitly:

> „RLEAS“ [pravdepodobne zamýšľané „prosím“], prines so sebou moje listy
> v sobotu, ak prídeš.

## Reproduction

From the repository root:

```sh
python3 ciphers/hcp-1438/work/decode.py
```

The command reads `work/transcription.txt`, checks all immutable source
hashes, applies the full table and prints all 36 letters. Its roundtrip
checks prove consistency between tokens and key; they do not independently
prove that every ink mark has been transcribed correctly.

## Uncertainties and assessment

- The opening glyph visibly resembles `┌` with two dots, hence **R**.
  Reading P would require a top-right corner `┐`. The word has five
  observed glyphs, so PLEASE would also require a final E absent from the
  line. An author's outline mistake and omitted E are plausible, but not
  established. The literal reading is therefore RLEAS, not PLEASE.
- The opening's third glyph is a somewhat slanted closed box with one
  central dot (E). Its right edge is heavy/angled; no additional central
  dot is counted. The fourth glyph has one dot, and the fifth three.
- Some dot clusters and outlines are small and slanted in the supplied
  scan. In particular, the three-dot TR shapes in MY/YOU may look like
  right brackets at reduced scale; their top-right two-stroke angles are
  used consistently here. Enlarging adds no source resolution.
- `SAT` is interpreted as Saturday in the translation and U as you; these
  expansions are not additional deciphered letters.
- All 36 cipher positions receive a literal reading. Coherent continuation
  after the anomalous opening and repeated identical letter shapes support
  the candidate. Independent image-to-token review remains necessary.

This is a solver handoff candidate, not a review-accepted FINAL solution.

## Response to review 1

Reviewer: Claude Opus 5.5, verdict ACCEPT (review/REVIEW1.md, 2026-10-26). The reviewer transcribed all 36 Pigpen signs from source/address.jpg independently, by the strokes seen plus dot count, and decoded them with its own script; the comparison with work/transcription.txt gives 0 differences out of 36. The reviewer confirmed at 10× that the opening sign is `┌` with two dots (R), the same shape as the R of BRING and LETTERS. The plaintext is unchanged.

1. No normalized English reading (minor). Accepted. The normalized English reading, with editorial additions in brackets, is: "P.S. [Please] bring my letters with you Sat[urday] if [yo]u come." The literal opening RLEAS is retained in the literal text; [Please] is an interpretation (most probably a horizontally mirrored corner, ┌ written for ┐, with the final E omitted), not a deciphered reading. The full stop after COME is on the card and is kept in the literal text in the report: `WITH YOU SAT IF U COME.` The commas between groups are represented by spaces.
2. Plain-text context unused (minor). Accepted. The main message on the address side is in plain cursive, headed "Rutland Iowa May-28-08" and signed **Ethel Pattee**; the postmark reads RUTLAND MAY 28 1908 IOWA; the address is Ray Bartley, Laurens, Iowa. The portal entry "Sender: Unknown" is therefore supplemented by the plain signature as written; no further identification of the writer is attempted. 1908-05-28 was a Thursday, so "SAT" most probably means Saturday 30 May, two days later. The related card HCP 1440 (also to Ray Bartley, also postmarked Rutland) mentions "Mrs P." and "Ethel"; this is consistent but proves nothing. These additions are made here and in the report; source/metadata.md is unchanged.

Remaining uncertainties carried into the report: what the writer intended by the opening `┌` (only the shape is certain); dots touching outlines on signs about 10 px wide in a 1024 px scan (solver and reviewer counted all 36 the same way); a wider search for an earlier published decipherment was not made (the portal showed Not solved and the same-day register snapshot has no entry for 1438 / pc_hcp_119).

Closing steps (this response, report, register entry, FINAL) prepared by Claude Opus 5.5 on the solver's behalf at the human's request, 2026-10-26.
