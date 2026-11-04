CONFIRMED

# Review of the stamp-box message, HCP 1282 (2026-11-03)

Reviewer: Claude Opus 5.5, independent. I did not use the solver's crops in `work/stamp-2026-11-03/`. I made my own crops from `work/hires/cpc_-04-11_HU__HU_Jasz-Arokszalas_jolanka-94_adr.jpg` (3445x2210) and put them in `review/work/stamp-2026-11-03/`:

- `ov_adr.png`, `ov_pic.png`: both sides at 1/3 scale, used to find the box (full-res x 2800-3260, y 180-700).
- `box2x.png`, `box2x_redink.png`: the whole box at 2x, plain and with the red ink isolated (R-G, inverted). The R-G channel suppresses the teal print.
- `L2_5x*`, `L3_5x*`, `L4_5x*`, `L4w_6x*`, `L5w_6x*`, `L6_5x.png`, `L6w_6x*`: the individual lines at 5-6x, plain, `_red` and `_G`.
- `F_6x.png`: the initial of the signature. `addrT_3x.png`: the address T, for comparison.

## Type change: justified

The stamp is gone. The box shows the printed dotted frame, the teal P.R.A. wreath, and part of the postmark ring at its lower right. Six lines of the same red ink as the card are written across the wreath, inside the frame where the stamp sat. A message hidden under the stamp is present, so **MASC + Steganography** is justified. The register-entry type field reads `MASC + Steganography`. That is the only field I checked.

## My own reading, sign by sign

| line | my reading | solver | agree? |
|---|---|---|---|
| 1 | c s o k o l o m | csokolom | yes |
| 2 | s z [a, under the wreath] m t a | szamta | yes |
| 3 | l a n s z o r | lanszor | yes |
| 4 | h ű (two marks over u) · s-like rising stroke, then 2-3 signs on the wreath, unread · **clear hyphen** | hű s?.. - | yes |
| 5 | [entry stroke + two arches: m/n-like] e [tall looped ascender, l-like] [three minims: m] e s | ?e?[m/n]es | yes (see note) |
| 6 | [s-like sign, same shape as the s that opens line 2] [ascender letter with a loop] · F e r í | ?? Feri | yes |

- `Csókolom számtalanszor` and `Feri` are secure. The initial in `F_6x.png` has a top bar, a stem and a mid-height crossing loop. That is a handwritten F, not a T or a J. *Feri* is also the signature on the other cards in this series (hcp-1207, 1208, 1211, 1216 and others).
- The hyphen at the end of line 4 is an isolated, clear dash (`L4_5x_red.png`, `L4w_6x_red.png`). So lines 4-5 are one word ending in `-es`. I confirm this.
- Line 5, first letter: it has an entry stroke and two arches, and it does not look like this writer's r. Compare the final r of `lanszor` in `L3_5x_red.png`: one tall stroke with a hook. The solver was right not to adopt *sze-relmes*. The shape r-e-l-m-e-s fits the letter count, but the first letter does not. The hidden letters of line 4 also sit on the wreath, so its middle cannot be read.
- Line 6: the two letters before *Feri* are an s-like sign and a looped ascender (l or k). I see no dots, so *s.k.* has no support in the pixels. The solver labels it unproven, which is correct.

## Differences

None that change the claim. One addition for precision, which the solver need not act on: in line 5 the third sign is a tall looped ascender (l-like), and the fourth has three minims, so it reads as m rather than n. This is consistent with the *-elmes* pattern the solver mentioned. It does not resolve the first letter, so the word stays unread.

## Not verified

- The word on line 4 after *hű*: it is overprinted by the teal wreath, and channel separation does not recover its middle letters.
- The identity of the two letters on line 6.
- I did not re-check the register entry beyond its type field, or the report PDF.
