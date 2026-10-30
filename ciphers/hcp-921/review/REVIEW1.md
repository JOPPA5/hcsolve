ACCEPT

# Review 1 — HCP 921 (Pigpen postcard to Miss Larkin, Horsmonden, 1912)

Reviewer: Claude Opus 5.5, 2026-10-30. Claimed reading: `MI[blot]SS MAY. / DIED.` = "Miss May died."

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-921/work/decode.py` was run from the repo root.
   The source hashes pass. Output: `MISS MAY. / DIED.`, plus the line
   `[sister key unchanged would give: MIVV MAY. / DIED.]`. This matches SOLUTION.md.
2. **Independent decoder.** `review/work/indep_decode.py` rebuilds the interleaved
   Pigpen key from first principles. Grid cells in reading order hold A/B .. Q/R, and the
   X quadrants top/left/right/bottom hold S/T, U/V, W/X, Y/Z. The script decodes **my
   own** sign reading, not the solver's file. The output is `MI?VV.MAY. / DIED.` with the
   unchanged key, and `MI?SS.MAY. / DIED.` with the single exception >1=S. The key is the
   same as the one on sister cards HCP 1188/1187 (checked against
   ciphers/hcp-1188/SOLUTION.md).
3. **Transcription against the scan.** I made my own crops from
   `source/address-large.jpg` (x 290–420, y 220–470), rotated in both directions and
   enlarged 4x. A further 4x crop covers the blot and the wedges, and others cover MAY and
   DIED (`review/work/cipher_rot90.png`, `cipher_rot270.png`, `blot_wedges_x16.png`,
   `may.png`, `died.png`). Rotated 90 degrees CCW, the cipher reads upright and the
   punctuation dots sit on the baseline. In the 270-degree view the dots float above the
   line, which confirms the solver's orientation. Sign by sign:
   - Line 1: top+right corner (TR0 = M), closed square without a dot (C0 = I), a heavy
     blot, then two right-pointing wedges (`>`). Each wedge has a clear dot in its opening,
     to the left of the vertex. Then a baseline dot, then TR0 (M), bottom+right corner
     (BR0 = A), undotted up-wedge (^0 = Y) and a dot. All of these signs agree with the
     solver's reading.
   - Line 2: U-shape with a dot (B1 = D), closed square without a dot (C0 = I), bottom+left
     corner without a dot (BL0 = E), U-shape with a dot (B1 = D), and a dot. These agree
     with the solver's reading.
   - The blot is solid ink with stroke ends sticking out. Its underlying sign cannot be
     recovered. The solver is right to leave it unrestored.
4. **Key coverage.** All 11 intact signs are decoded. Nine of them (M, I, M, A, Y, D, I, E,
   D) use the unchanged sister key. The one deviation (>1 = S, two tokens) is declared
   openly as a card-specific contextual value. In the solver's file this override is
   marked as such and is not passed off as part of the sister key.
5. **Alternatives to the S value.** I checked whether a regular layout could produce MISS:
   - Under the standard (non-interleaved) Pigpen, ^0 would be V. MAY would then fail.
   - Under an interleaved X with a different quadrant order, the dotted left quadrant
     would give T, V or X ("MITT", "MIVV", "MIXX").
   - Omitting one letter of the alphabet after M would push S into the grid (TL1), not
     onto a wedge.
   So S cannot come from any regular layout, exactly as the solver says. Even so, MI_ _ +
   MAY + DIED leaves "MISS" as the only natural English completion. The two consecutive
   identical signs fit a doubled letter, and the struck-out sign just before them fits a
   writer struggling with that letter. The reading stands, with the stated caveat.
6. **Language and context.** "Miss May died." is ordinary period English. It fits a 1912
   inland postcard between Horsmonden addresses (Miss Larkin, Hoath Hatch). No person or
   event is asserted beyond the text, and the solver says so.
7. **Sources and honesty.** The portal status was Not solved, with no solution attached.
   SOURCES.md and SOLUTION.md say that no published solution was used. Earlier GPT work and
   the Claude completion are both credited.

## Findings

1. **minor — Missing punctuation dot after the doubled wedge.** A clear baseline dot
   follows the second `>1`, at the same height and size as the dots after MAY and DIED
   (`review/work/blot_wedges_x16.png`, lower right). `work/transcription.txt` writes `|`
   (a word space) there instead of `.`. The literal reading should be `MI[blot]SS. MAY. /
   DIED.` The interpretation does not change. Fix the transcription and plaintext
   literally, or say why the dot is ignored.
2. **minor — S value is contextual (already disclosed).** The only non-key value covers
   2 of 11 signs and rests on the lexical fit alone. It is disclosed properly. The PDF
   report and register entry should keep the same wording and not present MISS as
   key-derived.
3. **minor — Date bookkeeping.** DONE1 carries `2026-10-29T23:04Z`, while the NOTES entry
   for the same session is dated 2026-10-30. The handwritten "4-12-12" and the catalogue
   date 1912-12-06 are also not reconciled. The second point is disclosed. I could not
   read the postmark day with confidence in the scan, so the report should leave it open
   rather than pick one date.

## What I could not verify

- The writer's own placement of S in the X (only Y and the dotted `>` appear on the
  card). Because of this, the S value cannot be confirmed by a second occurrence.
- The original sign under the blot.
- The identity of "May", or whether the death actually happened. No genealogical sources
  were consulted.
- The postmark date, which is only partly legible at this resolution.
