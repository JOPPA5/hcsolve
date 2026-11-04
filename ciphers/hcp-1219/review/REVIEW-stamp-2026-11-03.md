CONFIRMED

# Review of the stamp-box message, hcp-1219 (2026-11-03)

Reviewer: Claude Opus 5.5, independent check. Solver files and source/ not changed.

## What I checked and how

- Original: `work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-65_adr.jpg` (3445x2210). Stamp box at about x 2630-3100, y 190-720.
- My own crops are in `review/work/stamp-2026-11-03/`: `overview.png`, `box2x.png` (whole box at 2x), `rv_row1..7.png` (each row at 4x) with `rv_rowN_rg.png` (red minus green, which removes the blue printed circle and wreath), and close-ups at 5-8x (`z_r5s4.png`, `z_r4s2.png`, `z_r6.png`, `z_r7.png`, `z_r2end.png`). Each close-up shows the colour crop with the channel crop below it.
- Sign shapes compared with the main text of the same card (row 1 "szeretett edes jolan": small open bowl = s, closed loop with a tail = o, two short strokes = n) and with the key table of hcp-1216.

## Sign-by-sign reading (mine, made before comparing)

```
S1  i s t e n v e l e            dotted crossed curve, open bowl, gamma, three bars, two strokes, chevron, three bars, wave, three bars
S2  h ű k e d v e s              long stroke + short tick, X with a double mark, section mark, three bars, short+long, chevron, three bars, open bowl with a separate tick
S3  s e f e r i                  open bowl, three bars, upright cross, three bars, F, crossed curve
S4  j o m u l a                  inverted T, closed loop (o, not the open s bowl), three pink strokes over the blue "IRIA", X, steep wave, two bars
S5  t a s t k i                  gamma, two bars, open bowl, gamma with a hooked end, section mark, crossed curve
S6  v a n o k v a                chevron, two bars, short + slightly longer stroke, loop with a tail (o), section mark, chevron, two bars
S7  s a r n a p                  open bowl, two bars, F, two short strokes, two bars, long + short stroke
```

This is the same as the claimed literal in every row and sign: seven rows, no plain-language writing in the box. The normalized text "Isten vele! Hű kedvese, Feri. Jó mulatást kívánok vasárnap." is natural Hungarian, and it fits the family's closings ("hű kedvese, Feri" also appears under the stamp of hcp-1216).

## The disclosed weak points

1. **S5, 4th sign (t or r).** In `z_r5s4.png` the pink sign is one vertical stroke with a top bar that turns down at its right end. There is no middle bar in either the colour crop or the channel crop. The marks that make it look F-like are blue wreath lines, and the channel crop removes them. The pixels therefore support **t**, not just the context. The solver's disclosure is more cautious than it needs to be. This is not an error.
2. **S6, 3rd sign (n or d).** In `z_r6.png` the second stroke is only slightly taller than the first, so it sits between the n form (two short strokes) and the d form (short + long). I agree that n is a context choice, and it is correctly disclosed.
3. **S2/S3 line break, "kedves|se".** Confirmed: an s ends S2 (`z_r2end.png`, an open bowl with a separate tick) and another s starts S3. The disclosure is correct.
4. **S4, m.** The channel crop shows three pink strokes that are separate from the blue printed lettering. m is confirmed.
5. **S7, last sign.** It is long + short, the h/p homograph, read p for "vasárnap". This is correct.

## Type change to "MASC + Steganography"

Justified. The stamp has been lifted, and the box holds seven rows of cipher signs in the same pink ink, hand and key as the main text. They were written where the stamp would cover them, inside the printed stamp frame and across the printed stamp circle. The card has no register entry (status PARTIAL), and none should be created. That is consistent with the README.

## Editorial notes (no change to the reading)

- In SOLUTION.md, the "Cipher and key" paragraph still says the stamp-box block "is NOT transcribed (see below)". Open point 6 still describes "about 6 rows ... not transcribed" and says it blocks completeness. The new section says it "supersedes open point 6", but these two older lines now contradict it: the box has 7 rows and it is now read. The solver should update or strike them so that the file does not contradict itself.

## Not verified

- No reproduction script covers the stamp box. The reading was checked by eye only, as the solver's was.
- The main-text open points (rows 3, 9-10, 12, 21-23) were outside the scope of this review.
