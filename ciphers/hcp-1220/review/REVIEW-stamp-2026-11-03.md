CORRECTIONS

# Review of the stamp-box message, HCP1220 (2026-11-03)

Reviewer: Claude Opus 5.5, independent check of SOLUTION.md section "## Stamp-box message (2026-11-03)" and the type change to "MASC + Steganography". No solver file was changed.

## What I checked and how

- Original: `work/hires/cpc_-12-27_HU__HU_Jasz-Arokszalas_jolanka-97_adr.jpg` (3445 x 2210). Stamp box located on my own quarter-size overview (`review/work/stamp-2026-11-03/ov.png`); box at x 2640-3140, y 170-800.
- My own crops, all in `review/work/stamp-2026-11-03/`: `box1x.png` (whole box), `r0..r4.png` (3x colour row bands), `r0_g..r4_g.png` (green channel, autocontrast; purple ink dark, blue imprint pale), `row3_c..row6_c.png` (3x colour), `remeny_4x.png`, `es_5x.png`, `row4mid_5x.png` (+`_g`), `row5_4x.png`, `lastrow_5x.png` (+`_g`). A purple-minus-green ink map (`row*_pur.png`) did not separate the ink usefully and was not used.
- I did not use the solver's crops.

## My sign-by-sign reading

| row | what I see | read |
|---|---|---|
| 1 | h, i (dot), t, r, e, m, e, n, y with long descender; **no acute over either e** | `hit remeny` |
| 2 | e, s (**no acute**), s, z (over wreath), e, r, e, hyphen | `es szere-` |
| 3 | t with long lead stroke, e, large heavy t-cross over the imprint "R", then tall-looped k, o, s, hyphen; no dots over o seen; a loose ink dot left of k | `tet kos-` |
| 4 | s, e clear; middle is a run of up-strokes and arches under the wreath, not legible alone; then z (its descender runs into row 5) and e | `se ???ze` |
| 5 | s, z, i, v; then a bowl joined to the descender from row 4 (looks like d), a heavy downstroke into row 6, n, thick hyphen dot | `sziv??n-` |
| 6 | a peak (Λ), a small speck, then a t/k-like form with a cross-foot, joined to the heavy downstroke coming from row 5 | not legible |
| cipher | plain cross x, two bars, F-like, dotted sign at the edge | `feri` (literal `fari`, as disclosed) |

## Comparison with the claim

The claimed text `Hit, remény és szeretet kösse [öss]ze szív[ünket]. Feri.` and the English/Slovak translations agree with what I see. Every letter I can read from the pixels matches the solver's; every place I cannot read is already bracketed by the solver. The supplied letters (öss, ün/ü, ket) are compatible traces only and rest on the HCP1234 formula, which is disclosed. No forced word found. The cipher name `feri` with the two-bar e is disclosed as uncertainty 2.

## Findings

1. **Literal accents not on the card (minor).** The literal line (SOLUTION.md literal block, stamp section, `work/plain-note.txt`, report line 70) prints `hit remény / és szere-`, and the stamp section says `hit remény` and `és szere-` were "read from the pixels". On `remeny_4x.png` and `es_5x.png` there is no acute over any e in `remeny` or in `es`. The literal should read `hit remeny / es szere-`, with the accents supplied in the normalized text (as is done for `sziv` → `szív`, and as HCP1234's literal `hit remeny` does). Also `kös-`: no dots seen (the solver says so in uncertainty 1), so the literal is strictly `kos-`.
2. **Description of the last row is inconsistent (minor).** The stamp section (and the claim summary) says the last row is "a peak and a k-like trace, merged with the strokes of the cipher name"; uncertainty 1 and the report say "a peak, a small speck and a letter compatible with a cursive t, merged with the heavy strokes above it". On `lastrow_5x.png` the t/k-like form lies left of the cipher x and is joined to the heavy downstroke coming from row 5, not to the cipher name. One description should be used: peak, speck, t/k-like form merged with the row-5 downstroke.
3. **The n of row 5 (minor, conservative).** The stamp section lists "the n of -ün-" as read from the pixels, yet the literal brackets it in `sziv[ün]-`. I also see the n clearly on `row5_4x.png`. Either print `sziv[ü]n-` (with `[ket]`) or drop the n from the "read from the pixels" list; at present the two statements disagree. This does not change the wording.

None of these changes a word of the reading.

## Type change "MASC + Steganography"

Justified. `box1x.png` shows six rows of purple handwriting plus the cipher name inside the printed stamp frame (blue dotted border, blue "P. R. A." wreath imprint), with a green remnant of the stamp's border and its `FIL` strip still at the bottom and a green corner remnant at the top left. The writing fills the area the stamp covered, so a message was hidden under the stamp. The type is set consistently in SOLUTION.md (type note), `register-entry.txt` and `report/report.md` line 37.

## Not verified

- Whether ink remains under the surviving green FIL strip (not visible on the scan).
- The HCP1234 formula itself was taken from that card's SOLUTION.md (`Hit, remény és szeretet kösse össze szívünket`), not re-read from its scan.
- `report/report.pdf` was not re-rendered or opened; only `report.md` was checked.
