CONFIRMED

# HCP1290 – review of the stamp-box message (2026-11-03)

Reviewer: Claude Opus 5.5, independent of the agent that wrote the SOLUTION.md section "## Stamp-box message (2026-11-03)". Only `review/` was written.

## What I checked and how

- Original: `work/hires/cpc_-02-_HU__HU_Jasz-Arokszalas_jolanka-92_adr.jpg` (3445 x 2210). I did not look at the solver's `work/stamp-2026-11-03/` crops before reading.
- My own crops, in `review/work/stamp-2026-11-03/`:
  - `full.jpg`: whole address side, downscaled, to locate the stamp box.
  - `box.jpg`: the stamp box at full resolution (x 2680-3200, y 200-820).
  - `row1_3x.jpg` … `row6_3x.jpg`: each row enlarged 3x.
  - `row2_m_6x_red.jpg`, `row3_sz_5x_red.jpg`, `row5_sz_5x_red.jpg`, `row6_5x_red.jpg`: red channel with autocontrast, used where the ink is faint, sits on the blue triangle or is smeared green.
  - `row6_below_3x.jpg`: row 6 and the FILLÉR stamp remnant below it.
- `python3 -I work/decode.py` runs and ends with "Csók[o]lom számtalanszor. [folytatás olvashatatlan]", matching the section.
- `register-entry.txt` has `type: "MASC + Steganography"`, and `report/report.md` (line 37 and the section "Stamp-box message (audit 2026-11-03)") agree with it.

## My sign-by-sign reading (key from the SOLUTION.md table)

| row | what I see in the pixels | letters |
|---|---|---|
| S1 | opposed bowls `( )`, cursive loop, small 5/s-shaped section mark | cs o k |
| S2 | wave, cursive loop, three separate short strokes (the red channel shows three distinct strokes; the first two touch the blue triangle but do not form a chevron) | l o m |
| S3 | right bowl + crossed diagonal (smeared with green, but the same shape as S5), two bars inside the triangle, three strokes | sz a m |
| S4 | gamma, two short bars, wave (rising and then falling stroke), two bars, two long upright strokes | t a l a n |
| S5 | right bowl + crossed diagonal (a "7" crossed by a long stroke; clean in the red channel), cursive loop with a tail, F-like | sz o r |
| S6 | a slanted stroke with a short foot to the left, a separate short bar, a small upward-open curve; below them the torn FILLÉR remnant with the postmark strokes | no reading |

Literal: `csok lom szam talan szor` + S6 unread. This agrees with the claim sign for sign.

## Differences and notes

No substantive difference.

1. (minor, no change required) The first sign of S3 (z) is smeared green-black, so it is less clean than the matching sign in S5. Its shape still matches S5, and *számtalanszor* across S3-S5 confirms it. The section calls the reading firm and does not mention the smear. This could be noted, but it does not change the text.
2. (minor, no change required) In *Csók[o]lom* the bracket marks a letter the writer left out (literal `csok lom`). It is not a restored sign hidden by the stamp, and the section treats it correctly as a normalization: the literal stays unchanged and the uncertainty list gives `csók lom` as the writer's spelling.
3. S6: I agree that it cannot be read. The left foot-stroke and the short bar are separate, with a clear gap, so they do not combine into an inverted T (j). The single short bar has no value in the key, and the curve on its own matches no sign. Nothing to the right of the curve is legible above the remnant. Nothing was restored, which is correct.

## Type change

Justified. Writing under the stamp clearly exists: five full rows and a sixth fragment of cipher signs lie in the stamp box, where the lifted stamp exposed them. The stamp's torn remnant still covers the FILLÉR frame and the top-right corner, and the cipher ink is in the area the stamp once covered. "MASC + Steganography" fits.

## What I could not verify

- Whether more signs lie under the remaining stamp fragment. They cannot be seen in the scan.
- The postmark text and date were not part of this check.
