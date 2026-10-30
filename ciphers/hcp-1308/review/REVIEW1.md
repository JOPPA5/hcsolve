REVISE

# Review 1 of HCP1308 (Claude Opus 5.5, reviewer, 2026-10-30)

The key, the language, the addressee and the content of the letter stand. The ledger is not yet right: it has six wrong signs, all checkable on the pixels, and one of them hides a real misreading of the text. Rows 20-21 name the town **Árokszállás**, not "Szállás", and the emendation *meg a[ka]rom* is not needed. The solver's "weakest word" is resolved by the card itself. Several "spelling normalizations" were the solver's misreadings, not the writer's spellings.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1308/work/decode.py`: all four SHA-256 checks OK, 627 signs, output matches the literal block and normalized text in SOLUTION.md.
- Key: compared with `ciphers/hcp-1216/SOLUTION.md` and its `work/graphic-key.json`. Same family; every ledger token decodes and no sign is unassigned.
- Independent decode: `review/work/own_decode.py` holds my own glyph-class reading of all rows, typed from my crops, with its own key table, and diffs against `work/ledger.txt`. Run from the repository root with `python3 -I ciphers/hcp-1308/review/work/own_decode.py`. It reports 9 rows differing: 6 real (rows 6, 14, 16, 20, 25, 26) and 3 (rows 24, S1, S5) that are only my script's handling of `X:d` in the solver's tokens, not disagreements. My reading was made after seeing the ledger, so it is not blind.
- Pixels: crops of `work/hires/...adr.jpg` by `review/work/crop.py`. Rows 1-26 at 1.2x, then 2-6x on each point below (`a06`, `a14`, `a16`, `a25`, `a26`, `c20`, `z17`, `z18`, `z23`, `z25`, `b08`, `b14`, `b27end`, `r1`, `r2`, `t1`, `stamp`). All rows, the right edge, the top edge and the stamp field were read sign by sign.
- Counts in "Why I believe": *édesem* 5, *hogy* 4, *Feri* 2 confirmed.

## Findings

1. **major: rows 20-21 are mis-segmented; the text reads *meg Árokszállásba*.** `c20.png` shows, after *me*: reversed-s (g), two bars, F, loop, S (k). The ledger's `K~` at that first position is wrong: it is the reversed-s, the key's g, so no sense choice is needed. The final S is k. Rows 20-21 then run *mert meg·arok·szalasba·is·latni·akarom*, the same town name the writer spells in row 25. Correct normalization: *mert meg Árokszállásba is látni akarom egyszer legalább*, "because I also want to see you in Árokszállás, at least once". Remove the emendation *meg a[ka]rom* (uncertainty 11) and the "Szállás / lodging" discussion (uncertainty 12), and correct the English and Slovak ("at Szállás", "v Sálláši"). The sentence no longer has a doubled *akarom*.

2. **major: five two-bar signs (a) are transcribed as three bars (e).** Enlarged, each has exactly two strokes, unlike neighbouring three-bar signs in the same crops.
   - Row 6, `F ) E K K`: two bars with an acute tick above (`a06.png`). Literal *vetejtarsakkal*, so *vetélytársakkal*; "*vetélytársékkal*" is not what is written.
   - Row 14, `6 6 E N`: two bars (`a14.png`). *gyakrabban* is spelled correctly.
   - Row 16, `M E J D`: two bars (`a16.png`). *majd* is spelled correctly.
   - Row 25, `L E 6`: two bars (`a25.png`, `z25.png`). Literal *arokszalabol*, so only the s is dropped, not the *-ás-* (uncertainty 13 is wrong). Uncertainty 5's statement "Row 25 *arokszalebol* has a clear e" is false; rows 21 and 25 agree on a.
   - Row 26, `Z E J`: two bars with a mark above (`a26.png`). *muszáj* is spelled correctly.
   Fix the ledger, and delete *gyakrabben*, *mejd* and *muszej* from uncertainty 16.

3. **minor: uncertainty 1 should drop row 20.** After finding 1 neither S-type sign in *meg arok* needs word sense. The other g/k calls (rows 14, 17, 18) are properly disclosed.

4. **minor: *hónapában* is not obviously a stray letter.** Uncertainty 16 calls the a stray, but the signs `P A 6 A N` are clear and *hónapában* is a real form ("in the month of"). Report it as the writer's form, or at least as an alternative.

5. **minor: normalization of *Árokszállásból* should say "s dropped"**, and the "Why I believe" point about the town should cite both rows 20-21 and 25.

## Points checked and upheld

- Row 17: the H-like sign, two heavy joined strokes, cannot be confirmed as n by shape alone. *enyhébb* is disclosed as a sense reading.
- Row 8: the two blots remain unreadable alone; *egy* is contextual and disclosed. Row 5: the g is heavily inked but the descender fits.
- Row 14: the overstruck *c-z-z* cluster (`b14.png`) is disclosed; *perczet* is reasonable but the correction is not fully legible.
- Row 23: the sign under the stain has at least two strokes (`z23.png`); the false-start treatment is disclosed.
- Row 25 *nagyon*: bars under the collector's stamp, disclosed.
- Edges: rows 27-28 are as ledgered. The last sign before the corner has three strokes (`b27end.png`), so *szere* stands, and the completion [tő] is marked as editorial. *Feri* on the top edge: the f is a smeared closed cross, disclosed.
- Stamp field: all rows agree, including *sírig hű*; the first sign is a blot with dots, so the ü restoration is disclosed correctly.
- Bracketed restorations are all visibly bracketed. No published solution was found used; the portal attaches none.

## What I could not verify

- The plain pen note beginning *Sze…* left of the Rákospalota box stays unread (partly under the box), and the cancellation date is illegible, so the card remains undated.
- I do not have a native speaker's judgement on the regional forms *mejért*, *vetéjtárs-*, *e forgalom*.
- Accent ticks elsewhere were not audited individually; the solver says they were not transcribed.

Required before FINAL: fix findings 1 and 2 in the ledger, literal block, normalized text, English, Slovak and uncertainties. The content changes only in the Árokszállás clause, so no second full round should be needed unless the solver finds more.
