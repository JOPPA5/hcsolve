CONFIRMED

# HCP1222 – review of the stamp-box message (2026-11-03)

Reviewer: Claude Opus 5.5 (independent pass, solver's crops not used). Claim checked: SOLUTION.md "## Stamp-box message (2026-11-03)", literal `csoko / lom / szam / talan / szo{t>r} / feri`, "Csókolom számtalanszor. Feri", unread: nothing.

## What I did

- Cropped the stamp box myself from `work/hires/cpc_1913-01-_HU__HU_Jasz-Arokszalas_jolanka-113_adr.jpg` (3445x2210), box x 2700–3120, y 120–580, with `review/work/stamp-2026-11-03/crop.py` (run with the codex-runtime python3 -I): `box_2x.png` (colour), `box_2x_blue.png`, `half0_4x_blue.png`, `half1_4x_blue.png` (blue channel, autocontrast).
- 6x zooms of the doubtful signs (`zoom.py`): `z6_row1end.png`, `z6_row4start.png`, `z6_row5end.png`, `z6_row6.png`.
- Reference shapes from the main text (`ref.py`, `ref2.py`): `ref_r1jolan.png` (o, wave l, n in *jolan*), `ref_r17vig.png` (v, i, gy, a, z, o, n in *vigyazon*).

## Physical evidence for "under the stamp"

The colour crop shows the stamp box with lifted-stamp traces: glue/paper residue top left and a torn paper fragment with a green printed line at the top of the box; the six rows sit exactly in the area the stamp covered, and a faint postmark arc crosses rows 2–5 on the left. Writing under the stamp exists, in the cipher signs, no plain-Hungarian text in the box. The type **MASC + Steganography** is justified (and already in `register-entry.txt` and `report/report.md` §30, §83).

## My sign-by-sign reading (made before comparing)

| row | signs as seen | letters |
|---|---|---|
| c1 | opposed bowls · cursive loop · S/5-shape · cursive loop | cs o k o |
| c2 | wave (same "a"-like wave as l in *jolan* r1) · cursive loop · three short strokes | l o m |
| c3 | right bowl · tall crossed sign · two bars · three short strokes | s z a m |
| c4 | corner (diagonal stroke + top bar) · two bars · wave · two bars · two strokes | t a l a n |
| c5 | right bowl · tall crossed sign · cursive loop · rounded corner, no mid bar | s z o t(>r) |
| c6 | blotted star/cross · three bars · F-like · looped stem with crossbar | f e r i |

Result: identical to the claim, `csoko / lom / szam / talan / szo{t>r} / feri` → *Csókolom számtalanszor. Feri*. No sign unread, no sign added.

## Remarks (none changes the reading)

1. **c5 last sign, t>r (already disclosed).** `z6_row5end.png`: a single rounded arc with left leg, no mid bar – literally the corner sign t; *szot* is no word, *számtalanszor* needs r. One-letter restoration on word sense, disclosed in SOLUTION.md – acceptable under the standard.
2. **c4 first sign.** `z6_row4start.png`: the diagonal stroke and the top bar nearly touch (tiny gap); with the two bars below, the group could in principle be split as stroke + three bars (e). Read as corner t + two bars (a): the top bar sits higher and is shorter-spaced to the stroke, and *talan* is the only word. Agreement with the claim; the alternative is not a word.
3. **c6 last sign, i.** `z6_row6.png`: looped stem with crossbar, matching i in *vigyazon* (r17), not the o shape (bowl with the top curling right, as in *jolan*). The dot of i is not visible (possibly in the blot/residue); minor, not mentioned in SOLUTION.md.
4. **c1, mark above the last sign.** `z6_row1end.png`: a short faint grey dash above/right of the 4th sign – possibly an acute or a stray mark. The ledger records no accent in c1; it has no effect on *csókolom* (normalized ó is on sign 2 anyway). Could be noted as a possible accent.
5. **c6 f.** A blotted star with ink smear running down from c5; read as the upright cross f, consistent with the claim's disclosure.

## Not verified

- I did not re-run `work/decode.py` (the stamp rows c1–c6 in the ledger match the claim as printed; ledger lines checked directly).
- The Slovak translation was not re-judged beyond a glance (it renders the sense).

Verdict: **CONFIRMED** – the stamp-box reading and the MASC + Steganography type stand. Optional minor additions: mention the invisible i-dot (c6) and the possible acute in c1.
