REVISE

# Review 1 of hcp-1311 (reviewer: Claude Opus 5.5, 2026-10-30)

**Summary.** The 26 message rows are correct: my own transcription agrees with the ledger on every sign but one, and the Hungarian is coherent and in period. The key is the family key. What needs fixing is the closing under the stamp, which is printed with more confidence than the pixels allow (findings 1 and 2), plus several small errors and undisclosed sense calls. The solver's overall honesty is good: the main sense calls were all disclosed.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1311/work/decode.py` ran. All 4 SHA-256 checks passed (I also recomputed them with `shasum -a 256`). It printed exactly the rows claimed in SOLUTION.md, 511 tokens.
- **Independent reading.** `review/work/rc.py` cuts the whole card into overlapping 3x strips from the hires address scan (`review/work/crops/r*.png`). I read all 26 rows from those strips. `review/work/ind.py` holds my transcription in my own glyph names with my own key, and compares it with the ledger: 25 rows identical, row 25 differs by one sign (finding 3). My reading was not blind, because I had read SOLUTION.md first.
- **Key and coverage.** Every sign in rows 1-26 falls in a family sign class (hcp-1216 legend) or the two disclosed extras (S-hook k, y for i). No sign needed a new value. The S-hook k and the ς g are clearly different shapes in every row I checked (for example rows 1, 8, 13, 19, 24).
- **Disclosed sense calls checked on the pixels (`review/work/z.py`, `z2.py`; `review/work/crops/z_*.png`).**
  - Row 8 *kaptam*: left-tick (d) form, as stated.
  - Row 12 *de*: right-tick (h/p) form, as stated.
  - Row 22 *írok*: no dot, as stated. The sign has the long straight arm of the i forms rather than the hooked top of o, so the shape supports i as well as the sense. The solver can say so.
  - Row 6: after *t e* there are three strokes under a thick overwrite with bars, then v o l. m is reasonable.
  - Row 15 *ami már*: dot and three strokes present.
  - Row 23 *mit ir irjon*: M/R strip overlap checked, no double count.
  - Row 27: y m a, then a tall stroke in the smudge, a big loop, a slanted inverted T, a. *imádója* is well supported.
- **Language and context.** The text is real Hungarian of the family's period, with the writer's known habits (dropped doubles, *hogy* clauses, *Isten vele*). Pest, Árokszállás, Feri and the third-person closing all fit (hcp-1213 *Imádja Feri*, hcp-1301 *Csókolja a távolból imádója*). Translations checked; no material errors.
- **Plain parts.** Address and railway box read as stated. The picture side has only the printed verse and number.
- **Published solutions.** No sign of one being used. The portal capture shows none; I did not search further.

## Findings

1. **major: S6 is printed as *imád* but the signs do not support it, and the ledger shows no doubt.** Line `S6 Y M A D` has no `?` on any token, and the output `ymad` is literal, whereas the text calls it "not a secure one".
   - Sign 1 is not the y of row 27. In `crops/cmp_y.png` it has a closed or near-closed head with a hooked right arm, while row 27 has an open zigzag with a left flick. A loop-type sign (o or i, no dot visible) is not excluded, and that reopens *szerető*, which NOTES.md rejected because "the y-sign does not give it". The strokes after S5 *szere* must then be rechecked.
   - Signs 2-3: only two strokes are clear, and the third lies in the brown smudge. m is possible, n is not excluded.
   - The next sign shows three bars, not two (`crops/z_s6.png`: about y=350, 435, 525; the top one is at the triangle edge). The reading a is therefore unsupported; e is the better read. The tall left-tick d after it is clear.
   - Fix: mark all of S6 uncertain in the ledger, and remove *imád* / "adores" / "zbožňuje" from the firm output, or give them as one option beside *szerető*. The "about 5 sense-based" count must rise accordingly.
2. **major: the last signs of S7 are less "unresolved" than stated, and a signature is probably there.** Line S7 lists "two bars, an r-like sign with a hook, a loop" as unresolved (`crops/z_s7.png`).
   - The final two signs are clean: the r sign F, then a loop with a dot above it at upper right (`z_s7`, dot about x=1345, y=265). That is literally **r i**.
   - The sign before them has a possible third bar in the mask (`z_s7_m`), so e is possible.
   - Before that, a long diagonal with a low left stroke runs into the tear. That is the same layout as the tilted cross of row 28.
   - So the end of the block may read **…esem [F]eri**. This is my hypothesis, not a proved reading, because the f is under the tear. It matches the family habit of signing under the stamp (hcp-1216 *kedvese Feri*, hcp-1212, and the abbreviated stamp signature on hcp-1213).
   - Fix: record at least the literal *r i*, test the hypothesis, and revisit the claim that *[éd]esem* is "shared" with S6.
3. **minor: row 25 blotted sign looks like e, not a.** `crops/z_row25.png` shows a long top bar, a shorter middle bar with an ink blob, and two pieces at the third level. That is three levels, so ≡ rather than =. The literal is more likely *val{e}szolni*, a slip or blotted correction, with *válaszolni* still the only sense. Item 6 says only "the bars are blotted". State that this is a sense call against the sign.
4. **minor: row 26 first sign is an undisclosed sense call.** `crops/z_row26.png` shows no loop and no dot, only a compressed crossing at the card corner. The ledger has plain `I`, which the header defines as "loop with dot". *Isten* is certain from sense, but the token should be `?I` and listed.
5. **minor: row 28 first sign is an undisclosed sense call.** `crops/z_end.png` shows a low, tilted cross, not the upright + of row 14 *feljön*. It is the same tilted-cross case that hcp-1216 item 5 disclosed. Literal u gives no word; f is by sense. Item 8 also implies the card edge cut the name off. In fact there is clear blank paper to the right of the r, so the i is simply not written (or it is at the end of S7, see finding 2).
6. **minor: wrong counts in "Why it is correct".** The ledger has *hogy* ×6, not ×7, and *mulat-* ×5, not ×6 (`review/work/ind.py`). The same section says "all 26 message rows" while the header says 28 main rows.
7. **minor: item 9 "*nap|pal* is split with one p" is wrong.** Row 8 ends with the h/p sign and row 9 starts with it, so both p are written. *nappal* is spelled correctly across the row break.
8. **minor: row 18 struck group is under-described.** `crops/z_row18b.png` shows, after *irjo*, two strokes, then a short third stroke and a dot, then the blotted cross, then one tall stroke with no visible right tick before the loop. *irjon hogy* stands on sense, but the ledger's clean `N ~x~ H` hides that the third stroke is unaccounted for and that the h has no clean tick.
9. **minor: the command does not apply a key.** `decode.py` maps letter-named tokens to letters, so it prints the solver's reading, and the normalized text comes from a stored file. There is no sign-to-letter table in this card's SOLUTION.md, only a pointer to hcp-1216. This matches the family's practice, but add a short sign table or say plainly that the ledger is the reading.

## What I could not verify

- S1 after *üdvö*: the blot, the next stroke and the two marks at the right edge. Those marks sit one above the other at the level of S2, so they may not belong to S1 at all.
- S5 final sign (*t* is plausible only by sense; the sign is in the teal smudge at the triangle edge).
- The green cursive word above the cancellation. It runs to about ten letters and under the box, so it is not as short as stated, but I could not read it either. It is not ciphertext.
- The date. Nothing on the card fixes it.
- Whether any restoration is true beyond the scan: the torn stamp hides strokes for good.

## Note for the solver

The message itself stands. The closing is a real residue of roughly 15 signs that are damaged or uncertain, so the status line should keep saying the closing is only partly read.
