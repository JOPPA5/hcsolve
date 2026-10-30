REVISE

# Review 1 of HCP1293 (reviewer: Claude Opus 5.5, 2026-10-30)

The decipherment stands: Jolánka family key, Hungarian, Feri to Tóth Jolánka, layout and reading order as claimed. Fixes are needed before FINAL: one ledger token has no written sign behind it, so the "no sign is restored" statement is false; one dot-count error; the stated h/p/d graphics are wrong for this card; and one sentence (row 23) has a better reading that removes the "meaningless sign".

## What I verified and how

- `python3 -I ciphers/hcp-1293/work/decode.py` from the repo root: all four SHA-256 hashes OK; output equals the literal table and the normalized text in SOLUTION.md.
- Own crops of the un-converted address side: `review/work/crop.py`, output in `review/work/crops/` (all 23 rows in strips at 2.2x; row 11 blot; rows 21-23; ruled box in both orientations; right edge; top margin; stamp block, also on a blue-minus-green image).
- Own transcription by sign class, from those crops, key typed from the class table in `ciphers/hcp-1216/SOLUTION.md`: `python3 -I ciphers/hcp-1293/review/work/review_decode.py`. 523 signs in 33 rows, all mapped. It differs from the ledger in four rows only (Findings 1, 2, 3; the two h/d lines decode literally as the shapes stand, and are read by sense):
  - 04 `tattamheijen...` against ledger `...de ijen` (disclosed, Uncertainty 1)
  - 14 `esedenbeledtem` against ledger `esepenbeleptem` (Finding 3)
  - 23 `maletaleni...` against ledger `maletalenni...` (Finding 1)
  - B1 `közbe` against ledger `kozbe` (Finding 2)
- Key covers the whole text: every sign falls in a class of the family table; no value was changed for this card. I confirmed the claim that gy is two signs here (rows 1, 3, 10, 19, 23).
- Layout confirmed on the pixels: row 23 runs to the corner, up the right edge (reads when the card is turned clockwise), the arrow at the top right leads to the upside-down top margin, which ends on the box line; `közbe` / `nemjön` sit in the box turned 90 degrees. Stamp block `csoko lom szam talan szor feri` readable, also under the triangle (st1, st3).
- Language: real, natural early 20th-century colloquial Hungarian; not noise. Counts in "Why it is correct" check: 33 rows, hogy ×4 (rows 3, 10, 19, 23), édesem ×3 (7, 10, 21). The closing formula matches HCP1216.
- Sources: portal status Not solved, no solution attached, per SOURCES.md and metadata; no published solution used so far as I can see. No earlier work on this number, so nothing to credit.

## Findings

1. **major: row 23 ledger has an N with no written sign.** Ledger `L E N N I`; the card has one pair of strokes between e and the following i (crops `n23.png`, `blob.png`, `r21b.png`): wave-with-hook, three bars, two strokes, smudged i with its tick above, then k. A pair of strokes is one n (the class is "two short strokes"), and the smudged sign is the width of an ordinary i (about 50 to 60 px) and leaves no room for a second pair. The literal is *leni*. *Mellette lenni* is still right, but the n belongs in brackets like the writer's other single-for-double spellings (*szeretet*, *alat*, *viszontlatasra mikora*). This contradicts "No sign is restored; every letter in the ledger corresponds to a written sign". Fix the ledger, the literal table and that sentence.

2. **minor: B1 has its ö dots.** Uncertainty 16 says *közbe* has no visible dots. Two short ticks stand directly above the loop, just below the ruling (crop `box.png`, near x 380 to 420, y 430 to 500). Ledger should be `O:diaeresis`; this makes the reading firmer.

3. **minor: the h/p/d statement is wrong for this card.** The ledger header and Uncertainty 1 say the p of row 14 is the h sign. On this card h is tall stroke with a short tick on the RIGHT (rows 3, 5, 10, 11). Both p of row 14 have the short tick on the LEFT and are the same shape as the d of row 10 (crops `p14.png`, `d10.png`). So *épen*/*beléptem* are read by sense against a d-shaped sign, not from an h-shaped one, and the only sign where h and d shapes collide the other way is row 4 *de* (crop `d4.png`, right tick). The reading stands, the basis must be stated correctly.

4. **major: row 23 *kerjek i bocsanatomat*: a better division is available; "no value makes a word of it" is false.** The letters run `k e r j e k i`, and *kérje ki bocsánatomat* needs no meaningless sign: "ask (obtain) my pardon", with 3rd-person formal imperative, like *ne haragudjon* in row 2. It also explains the possessive *-omat*: with the solver's "let me ask your forgiveness" the object would have to be *bocsánatát/bocsánatodat*, and "my pardon" is unexplained (the solution just calls it "the writer's form for bocsánatot"). He would then be asking her to apologise for him to the people he did not say goodbye to, which fits plural *hazamentek* (Uncertainty 7: "plural/formal-odd"). I hold this as a strong hypothesis, not a certainty, as *kikér* with *bocsánat* is not the usual phrase. Give it as the main or at least an equal reading, update Hungarian, English, Slovak, and the "one meaningless sign" line in "Why it is correct".

5. **minor: row 11 *desenis*: alternative not disclosed.** *De s én is* is weak. *Mentek* is followed by `d e s e n i s`, and the sign before d is the most damaged on the card (crop `blot.png`): a dark S shape with a wet halo. The sign d and the next three-bar sign are overlaid with faint stray strokes, and the following bowl is faded. *Hazament, édes, én is hazamentem* ("went home, sweet, I too went home") would fit if the blot is a cancelled or overwritten sign (*édes* is his word in row 1). Equally, *hazamentek* with a dropped e. I cannot decide this; the s-bowl and k readings as signs are defensible. Add the alternative to Uncertainty 7.

6. **minor: *vezénylés* adds a y without brackets.** Literal is row 5 `vezen` + row 6 `les`, no y on the card (the sign to the right of row 5 is the ö of `nemjön`, I agree). Every other supplied letter is bracketed: write *vezén[y]lés* or say so in the uncertainties.

## Agreed with the solver on the hard spots

*mikor* row 6 (closed k, Uncertainty 2); row 8 k-e-r-e-s-t-e-m in the stain and blotted d; row 16 *eluttam* (plain cross u clear, no f); row 22 *idő*; *maleta* a-signs (first has clearly two bars, spacing of an a, not an e with a lost bar; Uncertainty 13 is fairly worded); E1 *mikora* and T1 *mikor* both really written; final wave of T1 really there, against the box line; visszajöjjék/-jek undecidable as disclosed.

## What I could not verify

- Row 21 end (crop `r21e.png`): rubbed. I can confirm *ez ala-*, a final faint two-bar a; the number of gamma signs in *-tt-* cannot be fixed, there may be two or three stems. Ledger TT is a sense reading here; Uncertainty 4 should say so.
- Accents throughout, as the solver says.
- The date. The postmark fragment is cut by the torn stamp; I did not read it.
- The plain address's last line (*ház…*, seems *házfelügyelő*), not needed for the cipher.
- Period idiom of *kérje ki bocsánatomat* (Finding 4) and *a nevem* (row 15) by a native reader.
