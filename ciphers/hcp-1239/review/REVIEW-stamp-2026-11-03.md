CONFIRMED

# Stamp-box review, HCP1239, 2026-11-03 (Claude Opus 5.5, independent reviewer)

## What I checked

- Own crops from `work/hires/cpc_1912-06-_HU__HU_Jasz-Arokszalas_jolanka-105_adr.jpg` (3445x2210), stored in `review/work/stamp-2026-11-03/`: `overview.png` (1/3), `box.png` (box x 2760-3240, y 160-700, 2x), `row1-5.png` (3x), `row3r(_g).png` (5x, green channel), `row4_g.png`, `row4r(_b).png` (5x, blue channel through the pink smear), `row5.png`, `sig(_g).png` (6x).
- Key from `ciphers/hcp-1216/SOLUTION.md` (opposed bowls cs, cursive loop o, section k, wave l, three strokes m, right bowl s, tailed cross z, two bars a, gamma t, two strokes n, F-like r, dotted i, three bars e, chevron v).
- `python3 -I ciphers/hcp-1239/work/decode.py` runs and prints S1 csokolom, S2 szamta, S3 lanszor, S4 istenve, S5 le; `work/ledger.txt` rows S1-S5 match.

## Sign-by-sign reading (mine, made before comparing)

| Row | Signs seen in the pixels | Letters |
|---|---|---|
| S1 | ( ) opposed bowls, loop, section, loop, wave, loop, three short strokes (dropped to lower right) | cs o k o l o m |
| S2 | right bowl + tailed cross, two bars, three strokes, gamma, two bars | sz a m t a |
| S3 | wave, two bars, two strokes, right bowl + tailed cross, closed loop with tail, F | l a n sz o r |
| S4 | dotted i, right bowl, gamma, three bars, two strokes, chevron, bars | i s t e n v e |
| S5 | wave, three bars, then a cursive word in plain script | l e + [cursive] |

Result: *csokolom szamta lanszor istenve le* = Csókolom számtalanszor. Isten vele. Identical to the claim. The Hungarian is idiomatic and is the standard closing formula on the sister cards (cf. HCP1216 stamp box *csokolom szamta lanszor*). Translation and Slovak are correct.

Cursive word (`sig_g.png`): a capital with a hooked top and two down-strokes (H-/K-like), then about three connected small letters (l/e, u/n, s-shape) ending in a descender, followed by a short stroke lost in the pink stain. I cannot read it either; leaving it unread is correct and nothing is forced.

## Type change

Justified. The stamp is lifted, the box is bare paper with the printed blue emblem, and five rows of cipher signs plus a cursive word are written inside the dashed stamp frame, where a stamp would cover them. `register-entry.txt` already carries `type: "MASC + Steganography"`.

## Differences / minor notes (no change to the reading)

1. minor – S4 final e: only the top bar is crisp; the lower two bars lie in the pink/magenta smear at the right edge of the box and are faint (visible in the blue channel, `row4r_b.png`). Three bars (e) is the reading consistent with *vele*, but the section does not mention the smear. Suggest a half-sentence of disclosure.
2. minor – S3 o is written as a small closed loop with a tail, close to the closed figure-8 that this card also uses for k. o is the only reading that makes *számtalanszor*; worth a note, not a correction.
3. minor (wording) – the capital of the cursive word is hooked rather than clearly looped; "like H or K" fits the pixels at least as well as "H or F". Either way it is correctly left unread.

## Not verified

- The cursive signature (unread by both of us).
