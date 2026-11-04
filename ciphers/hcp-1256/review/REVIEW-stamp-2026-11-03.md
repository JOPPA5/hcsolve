CONFIRMED

# Review of the stamp-box message, HCP1256 (2026-11-03)

Reviewer: Claude Opus 5.5 (independent pass). Claim under review: SOLUTION.md, section "Stamp-box message (2026-11-03)":
"[Ist]en vele, édesem, a boldog viszo[n]tlátásig. {barsoka [?] ész – unread} imádója Feri." The S6–S7 stretch is left unread, and *Ist-* is a disclosed restoration.

## What I checked

My own crops come from `work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-68_adr.jpg` (3445x2210). The script is `review/work/stamp-2026-11-03/crop.py`, run with `-I` and the PIL runtime. Crops:

- `adr_small.png`: the whole address side, used to find the stamp box (about x 2560–3060, y 140–660)
- `box_2x.png`: the whole stamp box
- `s1s2_4x.png`, `s3_5x.png`, `s4s5_4x.png`, `s6s7_5x.png`, `s7s8_4x.png`: the rows
- `s6_first_8x.png`: the first sign of S6
- `main_r2_r4_3x.png`: main-text rows 2–3, as a reference for the b ("6") and h/p forms

I did not open the solver's crops before I had made my own reading.

I read each sign myself and used the key in SOLUTION.md.

| Row | My sign-by-sign reading | Claim | |
|---|---|---|---|
| S1 | stamp flap hides the start; two red stroke ends stick out below the flap edge; then e(3 bars) n(2 strokes) v(chevron) e | [i][s][t]enve | agrees |
| S2 | l(wave) e e d(long+tick) e s(right bowl) e m(3 strokes) | leedesem | agrees |
| S3 | a b("6") o l d o g | aboldog | agrees |
| S4 | v i s z(crossed diagonal) o t(corner) | viszot | agrees |
| S5 | l a t, then a 2- or 3-bar sign under the arm of the t, then s i g | lat{a/e}sig | agrees |
| S6 | b? a r(F) s o k(small "5") a | {?}arsoka / barsoka | agrees |
| S7 | short bar coming out from under the green fragment, then e s z i m a d o | {-}eszimado | agrees |
| S8 | j(inverted T) a f(cross) e r i | jaferi | agrees |

- **First sign of S6** (`s6_first_8x.png`): a tall stroke with a closed low bowl on its right. It matches the "6" of *boldog* (S3) and of *kedvében* (main row 3). It is not the h/p form, which is a tall stroke with a separate tick (main row 2, *hogy*), and not the small "5" k, which comes later in the same row. Reading it as b is justified, and *barsoka* still gives no Hungarian word. Leaving the stretch unread is correct, and I do not offer a reading either.
- **S7 start:** I see only a short horizontal bar at the edge of the green fragment, level with the middle bar of the following e. One hidden sign, or part of one, cannot be ruled out. Unread is correct.
- **Reproduction:** `python3 -I work/decode_opus.py` prints S1–S8 exactly as quoted in the claim's literal line.
- **Type change to "MASC + Steganography":** justified. The stamp has been lifted, and eight rows of cipher signs in the same red ink and the same key were written in the stamp box under it. Fragments of the green stamp frame are still glued over the start of S1, over the S6/S7 left edge and along the bottom. The text was therefore hidden under the stamp on purpose. I found no plain-Hungarian writing in the box. The type now reads the same in SOLUTION.md, report/report.md and register-entry.txt.

## Differences and notes (none change the reading)

1. **minor, consistency.** The new section reads the S6 first sign as b (`barsoka`). The ledger, the command output, the normalized text (`work/normalized-opus.txt`, SOLUTION.md lines 41/50 and the English section) and uncertainty item 1 (SOLUTION.md line 66, which says the sign is "not settled, possibly a damaged b") still have `{?}arsoka`. The report mentions both. This is acceptable as long as the stretch stays unread, but the files should either agree or state that the ledger keeps `?` on purpose.
2. **minor, normalization.** In the normalized line, the unread stretch prints the literal `esz` as `ész`. The acute accent suggests the word *ész* ("mind"), but the stretch is declared unread. The literal `esz` should be kept inside the braces.
3. **minor, restoration scope.** `[Ist]` restores three signs, not one. The flap hides at least two signs, and I can see two red stroke ends at its edge. Only the formula *Isten vele* fits, and the restoration is disclosed, so I accept it. It does go beyond the "exactly one letter" rule, though, and should stay marked as a restoration.

## What I could not verify

- The signs under the stamp fragments that are still glued down (start of S1; start of S7). Nothing can be seen through the paper on this scan.
- Whether more writing lies under the bottom frame fragment below S8. Nothing red shows at its edges.
