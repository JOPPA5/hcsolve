CORRECTIONS

# HCP 1243 – review of the stamp-box message (2026-11-03)

Reviewer: Claude Opus 5.5 (independent; tried to refute). Scope: only the section "## Stamp-box message (2026-11-03)" of SOLUTION.md and the type change to `MASC + Steganography`. The main cipher message was not re-reviewed.

## What I checked

- Original: `work/hires/adr.jpg` (3445×2210). Stamp box located at about x 2650–3120, y 220–760.
- My own crops in `review/work/stamp-2026-11-03/`: `overview.png`; `box2x.png` (colour); `box_green2x.png`, `strip0-6.png` (green channel, 3×); `box_redness.png`, `red_line1-7.png`, `red_l2/l4/l5/l67.png` (R−G red-ink separation, which suppresses the blue printed globe emblem, 3–5×); `line1_full3x.png`, `line1_tail5x.png`, `line2_3_4x.png`, `line4_5_4x.png`, `line4_color4x.png`, `line4_end6x.png`, `line6_color4x.png` (colour, 3–6×).
- I read the box sign by sign before comparing with the claim.

## Existence of the hidden writing / type change

Confirmed. The stamp is gone (lifted). The dashed stamp frame contains seven lines of red-ink ordinary Hungarian cursive, written across the printed blue globe emblem (with its letters "P", "B.A."). A stamp stuck in the frame would have covered all of it. So there is writing under the stamp, and the label `MASC + Steganography` is justified. The hidden part is plain text, not cipher signs. The solver says so correctly.

## My reading (literal)

1. `Isten?ön-` – I s t e n, then a **separate closed loop (a/o-shaped)**, then ö (two clear dots above a tall-peaked loop), n, hyphen
2. `nel cso-` – n e l; c s o under the emblem ring, hyphen visible
3. `kolom` – k o l o m; o and m are partly overlaid by the emblem "P"
4. `szamta…` – s(3-form) z a m t a, then a final arch that looks like `n` (or an exit flourish); the t is crossed by the emblem
5. `lanszor` – l a n s z o r; s and z are under the emblem but readable
6. `szeretet` – the last t ends in a descending tail. I see no separate hyphen stroke
7. `tel Deri` – t e l, then D e r i with the i dot. Clear

Normalized: *Isten önnel! Csókolom számtalanszor szeretettel, Deri.* This agrees with the solver's normalized text and translation. The signature `Deri` is confirmed letter by letter.

## Differences from the claim

1. **Line 1 extra sign (minor, undisclosed).** Between `Isten` and `ön` there is a distinct closed loop (`line1_full3x.png`, `line1_tail5x.png`, `red_line1.png`). It is separate from the dotted ö that follows. The literal line therefore reads `Isten[a/o]ön-`, not `Isten ön-`. It is most likely a slip or a start of `o` corrected to `ö`. The normalized reading `Isten önnel` is not affected. But the claim that "all letters were read from the pixels" and "nothing in the box remains unread" should be qualified. The literal transcription should record this extra loop.
2. **Line 4 ending (minor, uncertain).** The claim gives the literal line as `szamta`. At 6× (`line4_end6x.png`, `line4_color4x.png`), the last sign after `ta` is an arch that reads more like `n` than a bare exit stroke. That would make the line `szamtan` (with `lanszor` following, a likely dittography of the syllable). I cannot decide between `szamta` + flourish and `szamtan`. The literal line should be marked as uncertain at its end rather than stated firmly as `szamta`. The normalized `számtalanszor` is unaffected.
3. **Line 6 hyphen (minor).** The literal transcription gives `szeretet-`. I see no separate hyphen, only the tail of the final t (`line6_color4x.png`). Write `szeretet` (or note the hyphen as not visible).

No difference affects the normalized message, the translations, the signature or the type change.

## What I could not verify

- Whether `Deri` is a name or a nickname, and who the sender is. The solver correctly leaves this open.
- Accents on `csókolom` and `számtalanszor` are not visible in the ink. They are only normalizations, as the solver states.
