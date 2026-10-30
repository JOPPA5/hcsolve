# HCP 1347 (pc_hcp_28): solution

Status: **whole message read (57 of 58 enciphered letters legible, 1 restored); review 1 verdict ACCEPT, closed.** Solver: Claude Opus 5.5, 2026-10-30. There is no earlier work on this number. Portal status *Not solved*; no attached transcription or solution; no published solution of this card met (no web search was run).

## The card

Picture side: printed "Lady Chapel, Wimborne Minster", series number 14276, no handwriting. Address side (The Wrench Series No. 14276): halfpenny Edward VII stamp, postmark WIMBORNE 10 PM AU 9 07; addressed in clear to Mr W. Abbott, Stokelake Farm, Chudleigh, Devon. The portal's "W. Abboú" is the writer's barred tt. The message is on the left half, written along the card (rotate 90 degrees anticlockwise). The large disc and building logo are a scanner overlay. 9 August 1907 was a Friday, matching the clear heading "G. H. Friday." There is no written date beyond the heading.

## Cipher and key

Caesar shift: each plaintext letter is written as the next letter of the alphabet. Decrypt by subtracting one (A→Z).

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The key was taken as a hypothesis from the W. Abbott cards (hcp-1386…1407, hcp-1355, hcp-1365, hcp-1368) and tested on this card's own pixels. Heading and address are in clear. The initials `M- L` / `M. L.` are kept literal, as on those cards (shifted they would be L. K.).

## Transcription and plaintext

| Line | On the card | Literal reading |
|---|---|---|
| 1 (clear) | G. H. Friday. | G. H. Friday. |
| 2 | Nz. Pxo M- L Cpz. | MY. OWN [M-] [L] BOY. |
| 3 | J. bn. hpjoh up | I. AM. GOING TO |
| 4 | uif Njotufs | THE MINSTER |
| 5 | Tvoebz. Ojhiu | SUNDAY. NIGHT |
| 6 | "Opu. bmpof" | "NOT. ALONE" |
| 7 | Zpvs. Pxo. M. L. Hjs[m] | YOUR. OWN. [M.] [L.] GIR[L] |

The quotation marks around line 6 are on the card, written in clear. The writer's punctuation dots carry no meaning. Brackets inside a word mark a restored letter (uncertainty 1); whole bracketed tokens are initials kept literal.

**English (original language; the portal says Unknown):** *G. H. Friday. My own M. L. boy, I am going to the Minster Sunday night, "not alone". Your own M. L. girl.*

**Slovak:** *G. H., piatok. Môj vlastný M. L. chlapec, v nedeľu večer idem do Minsteru, „nie sama". Tvoje vlastné M. L. dievča.*

(`M. L.` is left unexpanded: its meaning is unknown.)

## Command (from the repo root)

```
python3 -I ciphers/hcp-1347/work/decode.py
```

It checks the SHA-256 of the four image files, decodes every token of `work/transcription.json` (my own transcription), checks the inverse, and prints the plaintext and counts: 58 enciphered letters (57 read, 1 restored) and 4 literal initial tokens.

## Uncertainties

1. **Final `m` of `Hjsm` is a restoration.** `Hjs` is clear. The last sign is largely covered by a smear (`work/crops/z_blot.png`): a doubled stem and traces of further downstrokes are visible, which is compatible with a smeared m but does not prove it. The doubled stem is taller than a normal minim of this hand (about 33 hires px against about 23 for the `u` of `Opu`, measured by the reviewer), so the pixels alone neither show nor confirm an m. GIRL rests on the visible `Hjs` and the formula: it is the only word that fits this closing formula, which recurs on the sister cards (`Zpvs Pxo … Hjsm`).
2. **The `e` of `Tvoebz` is written without a visible loop.** It looks like a c with a thick head (`work/crops/z_e.png`). Read as c it would give SUNBAY, so I take it as the writer's e with the loop filled. The same word appears on hcp-1355 (`Tvoebz`).
3. **`M. L.`:** unexpanded, and whether it is shifted is unproved. The first initial has a hook, a stem and two further downstrokes in both places (`work/crops/z_m2.png`, `z_m7.png`), against one in the `N` of `Nz` (`z_n2.png`), so I read M, as on hcp-1365. N remains possible: other sister cards are read `N. L.` by other solvers. `M. L.` here and `N. L.` on hcp-1402 are probably one group, not two different pairs of initials. The second sign is a stem with a small foot on this card, and hcp-1368 transcribes the same slot `h` (`M. h`), with similar forms reported on hcp-1349, 1366 and 1369; L is my reading, h is possible, and the literal form printed here is a choice. The second initial in line 7 shares its stem with the descender of the `p` of `bmpof` above (the doubled stroke), so the sign is read from the stem and foot only. In line 2 a dash stands after M, and no dot is visible after L.
4. **`Ojhiu`:** after `h` the card has three small minims and one i-dot set slightly right of its place. That count fits i + u. The final strokes are shallow (`work/crops/z_hiu.png`).
5. **`Pxo` in line 7:** the arc of the P runs into the blotted descender of the `p` of `Opu`, and the P's stem is thin (`work/crops/l7a.png`). The form matches line 2.
6. **Heading initials:** read `G. H.`; the G could be a C (hcp-1355 reads C. H. and hcp-1386 and hcp-1397 discuss the same doubt).
7. **`hpjoh`:** the stem of `p` is heavily blotted, the arch of the final `h` is swallowed by a blot that leaves a dark spot at the foot, and the `j` has no visible dot (`review/work/z_hpjoh.png`, `z_pj.png`). The word is still GOING: no other word fits the letters that are legible and the same phrase stands on hcp-1355.
8. "Sunday night" was presumably 11 August 1907, inferred from the Friday postmark, not stated. Who accompanies the writer is not stated.

## Why it is correct

One fixed shift, with no card-specific tuning, turns all 58 letters into grammatical English (one letter restored, item 1), including the long words MINSTER, SUNDAY, NIGHT, GOING and ALONE. MINSTER was not on any sister card I searched, and it agrees independently with the picture side and the Wimborne postmark. The salutation and close repeat the couple's formulae, and I AM GOING TO echoes hcp-1355. The weekday in the clear heading matches the postmark date.

## Response to review 1

Verdict ACCEPT, four minor findings. All are accepted and addressed. No decoded letter changed. `python3 -I ciphers/hcp-1347/work/decode.py` was re-run after the changes: hashes OK, 58 letters (57 read, 1 restored), 4 initials.

1. **`GIRL` printed as fully read: fixed.** The table, `work/transcription.json` and the decoder output now give `Hjs[m]` / GIR[L], and `work/decode.py` reports the split. The running English and Slovak stay unmarked as translations, and the status line states the restoration.
2. **Smudged signs in `hpjoh`: fixed.** Now uncertainty 7. I looked at `review/work/z_hpjoh.png` and agree: the blot covers the p stem and the end of the h.
3. **`M. L.` / `N. L.` across the family: fixed, and taken slightly further.** Uncertainty 3 now says the two are probably one group. It also records that hcp-1368 reads this slot `M. h`. `review/work/z_m7.png` shows a stem with a small foot here too, so L is not secure. I keep L, as the group stays unexpanded and outside the cipher reading.
4. **Stem height of the restored `m`: fixed.** Uncertainty 1 now says this, using the reviewer's measurement, and "fits" is replaced by "is compatible with".
