CORRECTIONS

# hcp-1273 – review of the stamp-box message (2026-11-03)

Reviewer: Claude Opus 5.5, independent re-read. The message reading and the type change are confirmed. The corrections below are minor and only about wording: one sentence describing the physical evidence, and one point of literal-transcription consistency. Neither changes the message or the type.

## What I checked and how

- Original: `work/hires/cpc_1912-05-04_HU__HU_Jasz-Arokszalas_jolanka-18_adr.jpg` (3445x2210). I made my own crops with PIL (`python3 -I`) into `review/work/stamp-2026-11-03/`:
  - `ov.png` (whole address side), `box_context_1x.png` (x 2400-3250, y 200-950), `box_2x.png` (stamp box)
  - `line1_G_3x.png`, `lines123_sep_3x.png`, `line4_4x.png`, `line5_4x.png`, `l45_sep_3x.png` / `l45_G_3x.png`
  - `word4_sep_6x.png` / `word4_G_6x.png`, `line5_sep_6x.png` / `line5_G_6x.png`, `sig_G_5x.png`
  - `*_sep_*` crops keep pixels where R-G > 100-110 and G < 120-135, which drops the pale pink printed emblem. `*_G_*` crops show the stretched green channel.
- I read the box sign by sign before comparing my reading with the solver's section.

## My reading

| Line | Signs as seen | Notes |
|---|---|---|
| 1 | c s o k o l ? m | The vowel before m is a closed round sign with a connecting stroke. In this hand a and o are not kept apart (line 2 looks like "szomtolon" at 1x). Normalized: *csókolom*. |
| 2 | s z a m t a l a n | t is a stem with a bar at the top. |
| 3 | s z o r · s i r i g | r is n-like. The dot of the first i is visible. |
| 4 | h ű · s z e r e | ű has two strokes. Writer's s (short rising stroke), z crossed (x-like, no descender), e, r (n-like hump, same as in *szor*), e. The first sign is not p: there is no descender. |
| 5 | t e t j e | 1st: a stem with a long top bar to the left, no ascender loop, so not k (compare the looped k of *csokolom*). 3rd: a stem with a top bar, the same shape as the t in *szamtalan*. 4th: a short hook with a long descender looping down to the left, and a separate dot above it (visible in `line5_G_6x.png`), so j. |
| 6 | F e r i | The F has a top bar and a crossbar. The r is n-like. The last stroke runs into a stain. |

Lines 4 and 5 run on as one word, literally *szeretetje*. I find no Hungarian word that fits all of these letters. *szeretője* would need ő in place of "e + crossed t", and the pixels do not show that. *kedvese*, the family formula, does not fit line 4: there is no k ascender and no d or v. I would therefore leave the word unread, as the solver did. Nothing should be restored here: the gap is more than one hidden sign, and the signs are not physically hidden at all.

**Comparison with the claim:** my letters match the solver's literal reading `csokolom / szamtalan / szor sirig / hű szere / tetje / Feri` exactly for lines 2 to 6. The normalized text "Csókolom számtalanszor. Sírig hű szere[…]je(?), Feri." and the decision not to adopt *szeretője* are confirmed. The withdrawal of round 1's "pene / ketse" is also confirmed: the first sign of line 4 has no p descender, and the first sign of line 5 has no k loop.

## Type change: MASC + Steganography

This is justified. `box_context_1x.png` shows the following:
- The six cursive lines lie inside the printed dotted stamp frame, which is empty of any stamp.
- The cancel ring (black) is struck on the card around the box, but its top arc and the inner date lettering are missing over the written area. That is the area the lifted stamp covered.
- Green stamp-paper remnants with gum stains remain, one at the bottom edge of the frame.

The message was therefore under the stamp. It is in plain Hungarian cursive, not in the cipher signs. The register entry (`type: "MASC + Steganography"`), SOLUTION.md and report.md all state this consistently.

## Differences (corrections)

1. **minor – location of the green fragment.** SOLUTION.md and report.md say there are two green fragments "at the left edge and bottom of the frame". In `box_context_1x.png`, the left green fragment (with its three printed green lines) lies about 40-80 px at full resolution *outside* the dotted frame, to its left, among the black postmark lettering. Only the bottom fragment is at the frame edge. Suggested wording: "one green fragment at the bottom edge of the frame and one just outside its left side". The conclusion that the writing lay under the stamp still rests on the missing cancel ink over the writing and is unaffected.
2. **minor – a/o in the literal transcription.** The writer's a and o are near-identical (line 2 looks like "szomtolon"). The literal line `csokolom` and the line `szamtalan` therefore already contain editorial vowel choices. A note such as "a and o are not distinguished in this hand; vowels are given as normalized" would make the literal line honest. The normalized text is unaffected.

No other differences.

## What I could not verify

- The meaning of *szere|tetje*. I agree it stays unread.
- Whether a few more letters were written under the parts of the stamp paper that are still attached. No ink of the writing is visible under the bottom green fragment.
