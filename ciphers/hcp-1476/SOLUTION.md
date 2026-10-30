# HCP 1476 / pc_hcp_157 — Pigpen closing on a postcard to W. Pooley (1907)

Status: **complete reading of all 22 cipher letters; review 1 verdict ACCEPT.**

Credit: the 22-letter transcription and reading were made by the OpenAI GPT
solver (GPT-6 Astra) on 2026-10-26, which left the end mark open. Claude Opus
5.5 completed the work as solver on 2026-10-29 (end mark, DONE1) and wrote the
response to review 1 below on 2026-10-30.

The portal listed the card as Not solved on 2026-10-26, with no transcription
or solution attached. No published solution was found or used.

## Plaintext

```text
MY, OWN
DARLING, SWEETHEART
[end mark: probably a printed ornament of the card's divider, not cipher]
```

Editorial: "My own darling, sweetheart."
Slovak: „Môj vlastný miláčik, zlatko.“

Language: English (the catalogue says Unknown). The cipher closes an ordinary
English cursive message (about the printed "Wife's Commandments" on the
picture side and about Charlie) right after "Bye Bye".

## Key

Standard interleaved Pigpen, undotted/dotted pairs:
BR A/B; B C/D; BL E/F; R G/H; C I/J; L K/L; TR M/N; T O/P; TL Q/R;
V S/T; > U/V; < W/X; ^ Y/Z.

Labels name the strokes present: BR = bottom and right, B = bottom, left and
right, BL = bottom and left, R = top, bottom and right, C = all four sides,
L = top, bottom and left, TR = top and right, T = top, left and right,
TL = top and left. Suffix 0 = no dot, 1 = dot. V, >, <, ^ name the wedge by
where its point is (V points down). Shapes are read on the address side
rotated 90 degrees clockwise (work/upright.jpg).

Transcription (work/transcription.txt, own manual reading, no supplied
transcription):

```text
TR0 ^0 , T0 <0 TR1
B1 BR0 TL1 L1 C0 TR1 R0 , / V0 <0 BL0 BL0 V1 R1 BL0 BR0 TL1 V1
END_MARK
```

## Reproduce

From the repository root:

`python3 -I ciphers/hcp-1476/work/decode.py`

The script checks the SHA-256 hashes of the files in source/, decodes the
transcription with the key, checks an inverse-key roundtrip for each of the
22 letters, and prints the plaintext. It does not read the image; the
transcription is manual. `python3 -I ciphers/hcp-1476/work/terminal-audit.py`
prints a position-by-position inventory (add `--crop` with Pillow to
reproduce the end-mark enlargement).

## Uncertainties

- **W of OWN is malformed.** Line 1, glyph 4 is drawn as a 7-like acute
  angle with its point at the upper right (literally `>`, i.e. U, giving
  "MY OUN"). The W of SWEETHEART is drawn correctly as `<`. It is read as W
  from context; the small tick above it at the right is taken as a stray
  stroke, not a dot (a dot would give X). See review/work/own.png.
- **Dot of the first T of SWEETHEART.** The dot position is crossed by a
  cursive descender from the line above; without a dot the glyph would be S.
  T is read from context. See review/work/eth.png.
- **End mark.** `—(•)—` after the last T is not a Pigpen glyph. It is
  probably a printed ornament of the card's divider (see response to F3); in
  any case it is not a letter. This rests on a JPEG scan, not on the card.
- W. Pooley and Charlie are not historically identified.

## Why it is right

All 22 glyphs decode under the unmodified standard Pigpen key into an
idiomatic English closing that fits its position after "Bye Bye". No glyph
is left over and no second key is needed. The reviewer decoded the glyphs
independently from its own reading of the scan and got the same 22 letters.

## History (condensed)

- 2026-10-26, OpenAI GPT (GPT-6 Astra): download, rotation, manual
  transcription, standard Pigpen reading of all 22 letters; end mark kept as
  unresolved; terminal audit script. Status then partial; no marker.
- 2026-10-29, Claude Opus 5.5: end mark judged not a letter; DONE1.

## Response to review 1

Verdict ACCEPT; four minor findings, all accepted. No letter of the reading
changed.

- **F1 (malformed W) — agreed, disclosed.** I looked at review/work/own.png
  and line1-zoom.png: the glyph is a top bar with a stroke running down-left
  from its right end, point at the upper right, unlike the clean `<` of
  SWEETHEART. It is now listed under Uncertainties as malformed and read as W
  from context, with the tick treated as a stray stroke. The transcription
  keeps the intended token `<0` and the note explains it.
- **F2 (dot of T) — agreed, disclosed.** In review/work/eth.png the loop of
  a cursive descender passes through the dot position of the T. Listed under
  Uncertainties.
- **F3 (end mark printed) — agreed.** review/work/endmark-color.png shows a
  crisp symmetric `—(•)—` with tapered ends, as dark as the printed divider
  and legend (darkest-pixel mean 83 vs. 97–103 for the cipher glyphs), set by
  the printed divider. The wording "decorative full stop" is replaced by
  "probably a printed ornament of the card's divider". decode.py and
  terminal-audit.py now print that instead of "uninterpreted".
- **F4 (documentation) — fixed.** Title and status updated; the outdated "no
  DONE1/FINAL/register entry" text is gone (history condensed above); the
  comma after MY is added to work/transcription.txt; run-together words
  fixed; credit to GPT-6 Astra and Claude Opus 5.5 stated at the top.
  Re-run of `python3 -I ciphers/hcp-1476/work/decode.py` on 2026-10-30 (also
  saved as work/plaintext-check.txt):

  ```text
  MY,OWN
  DARLING,/SWEETHEART
  [END MARK: probably printed ornament of the card divider, not cipher; see work/end-mark-large.jpg]
  22 Pigpen letters; end mark is not a letter (printed ornament, see SOLUTION.md).
  Source hashes and all 22 inverse-key roundtrips passed; not OCR.
  ```
