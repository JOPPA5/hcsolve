CONFIRMED

# HCP1233 stamp-box review, 2026-11-03 (Claude Opus 5.5, reviewer)

Claim under review (SOLUTION.md, "Stamp-box message (2026-11-03)"): the stamp box holds rows 22–26, `csokol | jasza | mta | lansz | orfe[r][i]` = "Csókolja számtalanszor Feri.", in cipher signs, under a lifted stamp; type changed to MASC + Steganography.

## What I did

Own crops from `work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-67_adr.jpg` (3445x2210), in `review/work/stamp-2026-11-03/`:

- `adr_quarter.png`: whole address side, to place the box (card x about 2600–3060, y 220–780).
- `context_postmark_1x.png`: box with the postmark and the stamp remnant.
- `box_2x.png`, `r22_3x.png` … `r26_3x.png`: colour crops per row.
- `mask_box_2x.png`, `mask_minRB_3x.png`: purple-ink masks (B−G; min(R,B)−G).
- `tri_color_5x.png`, `tri_purple_5x.png`: the printed triangle at 5x, with an R+B−2G mask that keeps the purple pencil and drops the teal print.
- `ref_rows1_3.png`: rows 1–3 of the open text, as shape references for o, z, s, l, a.

I read the box sign by sign before opening the ledger rows 22–26, then compared.

## Sign-by-sign reading (mine)

| row | signs seen | value |
|---|---|---|
| 22 | opposed bowls with a dot; crossed loop (same as the o-loop of *jolan*, *hogy* in rows 1–2); section-mark S; crossed loop again; small wave | cs o k o l |
| 23 | leaning inverted-T; two bars; right bowl (upper "3" shape); crossed curve with hook; two staggered short bars | j a s z a |
| 24 | three short strokes (clear, left of the triangle); inside the upper triangle a slanted stem with weak top, then two short bars at right (only on the R+B−2G mask) | m [t] [a] |
| 25 | wave (clear, left of the triangle); inside the lower triangle two bars at left, two slanting strokes, a small right hook; right of the triangle a crossed curve with hook | l a n [s] z |
| 26 | crossed loop; F-like; plain-looking tilted cross; two bars plus a small stroke below; F-like (stem and right arm) through residue; a long curve through residue down to the dotted line | o r [f] [e] [r] [i] |

Result: `csokol jasza mta lansz orferi` = *csókolja számtalanszor Feri*. **Identical to the claim, letter for letter.** No extra sign and no missing sign in the box.

## Differences / remarks (none change the reading)

1. Row 24 *t* and *a*, row 25 *s* (minor, disclosure only). These three lie inside the printed triangle and are visible only on the purple mask (`tri_purple_5x.png`); the t has a stem but the top bar is not clear, and the s is a small hook at the lower right of the triangle. The claim mentions "m, a stem of t, and bars" for row 24, which matches; it does not name the row 25 s as faint. The word *számtalanszor* fits all traces and nothing else is suggested, so no correction is needed. The solver may add "s of row 25 faint" to uncertainty 11.
2. Row 26 *e* (already disclosed): two bars are clear and the third is only a small stroke, so the bare shape is closer to a (two bars). *Feri* rests on the name, as disclosed. Same for f vs plain u and for r, i in the residue.

## Steganography / type change

Justified. On `context_postmark_1x.png`: (a) a green stamp corner with perforations and the "FI…" value remains at the lower left of the box and carries the black cancellation stroke; (b) the postmark ring (PAL… / SO…) stops at the left edge of the box, i.e. its right half was on the stamp that is now gone; (c) torn-paper scars sit at the upper-left and lower-right of the box, where the stamp's other corners were glued. All writing in the box is cipher signs in the same purple pencil; there is no plain Hungarian there. The writing lies where the stamp was, so it was hidden under it. MASC + Steganography is the right label; register-entry.txt and report.md already carry it.

## Could not verify

Whether the pencil was written before the stamp was stuck on is inferred from position, not proved physically: in the lower-right residue the i stroke shows faintly through the torn paper, which is consistent with the writing lying under the stamp, but a scan cannot show layer order with certainty.
