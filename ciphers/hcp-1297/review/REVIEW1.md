REVISE

# Review 1 of HCP1297 (Claude Opus 5.5, 2026-10-30)

The card is correctly identified and the reading stands: Jolánka key, Hungarian, a love letter from Feri. Two signs must be corrected, and one of them changes the meaning of the closing sentence.

## What I verified and how

- **Solver command.** `python3 -I ciphers/hcp-1297/work/decode_opus.py`: all 4 SHA-256 hashes OK; the output equals the Literal decipherment in SOLUTION.md; 459 signs.
- **Independent decoder.** `review/work/decode_review.py` has its own key table written from the key description and shares no code with the solver. It gives the same rows as the solver (`diff` empty; outputs in `review/work/decode_review.out`, `review/work/solver.out`). No token is unmapped, so the key covers the whole ledger. With `--fix` it applies findings 1 and 2 (`review/work/decode_review_fix.out`): 460 signs.
- **Transcription against the scan.** I read all 25 rows and the stamp block from my own crops of `work/hires/..._adr.jpg` (`review/work/crop.py`, `review/work/crops/`), not from the solver's crops. Disputed places were enlarged 3–7x: rows 4, 5, 6, 7, 8, 9, 20, 22, 23, 24, 25 and the stamp block.
- **Family key.** Compared with HCP1216: same sign classes. Language, formulas (*Isten vele*, *számtalanszor*, *hű kedvese*, *Feri*) and addressee agree.
- **Portal.** `source/metadata.md`: no attached solution or transcription. Nothing suggests a published solution was used.

## Findings

1. **major: row 25 `föt be` is misread; the first sign is j, not f. Read *nem jött be*.**
   Evidence: `review/work/crops/fot.png` (6x). The bar of the sign sits low on the stem, at about four fifths of its height, with only a tiny foot below. That is the inverted T, compare j in `mamat.png`. True f has its bar at mid-height: `row25.png`-row +, row 12, row 24 *Feri*, s4 *Feri*. Decoded: j ö t b e = *jött be* (writer's single t, as with many doubles on this card).
   - *Sajnálom, hogy nem jött be* = "I am sorry that you did not come in": ordinary Hungarian, every sign accounted for, and the two marks over the o are then correct as ö.
   - The solver's *fért be* ("it did not fit") needs an f, a vowel change and an inserted r, and SOLUTION.md itself says *föt* "is not a word that fits". It was an interpretation forced from context.
   - The foot below the bar is why I say j on shape plus sense, not on shape alone; this call should be disclosed that way. The loop's right stroke is also straighter than a typical o, close to the i-sign, but with j the marks support ö.
   - Fix: ledger, literal text, normalized text, three translations, Uncertainty 3, title if wanted.

2. **major: row 20 has a final wave the ledger omits, so the row ends *szóval*, not *szova*.**
   Evidence: `review/work/crops/r20w.png` (5x) and `r20b.png`: after chevron and a comes a clear, separate wave (l) on the same line. The solver's crop `z20` stops at about x = 1359 in the hires scan, and the wave lies at about x = 1420–1485, so it was simply outside the crop.
   - Consequences: `szoval` is fully written; `szóva[l]` loses its brackets; *szova* must leave the omitted-letters list in Uncertainty 9; the count becomes 460 signs.
   - Note: this a-sign has a tiny third dash under its two bars (a/e, read a by sense).

3. **minor: unbracketed additions in the normalization of row 20.** The ledger has `...E J M A J E F O:d L...`. "ünnepély, **a** majerről" adds an article and an r that are not on the card, neither in brackets. SOLUTION.md says square brackets mean "not on the card"; apply that here.

4. **minor: row 22 alternative not disclosed.** I confirm the signs: b e l a, a single thick slash, a, k (`r22z.png`). Add the alternative *vasárnap a Bélának* ("on Sunday, to Béla"), which would need no omitted r and would take the slash as a reduced n. It is not proven; the sign is a single stroke, unlike n everywhere else. Keep the point open, but list it.

5. **minor: punctuation of rows 4–5.** "köszönök, kedves jó Ön. Nagyon rosszul értette" gives the unnatural "dear good you". *Ön* is more naturally the subject of the next sentence: "…köszönök. Kedves Jó[lánkám]! Ön nagyon rosszul értette…" (or "Kedves jó, Ön…"). The letters do not change; the three translations should follow.

6. **minor: rows 9–10 translation.** "this is what you think [of it]" hides the fact that the clause gives no good sense as written. Signs confirmed: e z t a i gy (`r9z.png`). The expected sense is probably "do not think of it this way", but no negation is on the card. Say that the sense is unresolved, and do not put a smooth rendering in the translations.

7. **minor: ledger layout and legend.** Label `s1` merges two physical lines: the washed-out *csokolom* line and the lower `?zamta` line (`s.png`). The stamp block has five lines, not four. The token `S` (rows 1, 4) is missing from the ledger legend; it decodes to s.

## Solver calls I confirm on the pixels

- Row 3 `angyon`: a, n, gy as stated.
- Row 6: the third cross-topped sign is gamma; I see at most a small bump where a bar of F would be, and it is retouched, so t by sense is fair (`r6y.png`). Last sign on the postmark: thin flag, no middle bar visible, disclosed. Sign group e-m-e as stated.
- Row 7: H A A Z, the z with a small hook (`r7.png`).
- Row 8: `maga`, three strokes with a curved third, not h. The final a carries an accent tick (`r8a.png`), which supports *magá[ra]*; this may be added to Uncertainty 6. The supplied *[ra ha]* remains the solver's restoration and is disclosed.
- Rows 14, 20, 23, 24: blots and overstrikes as disclosed.
- Row 23 ending *mamajat*; row 25 *sajnalom hogy*; stamp block `zamta / lanszor / hükedve / senferi`. The two strokes of s4 are equal, so n, not d. The *csokolom* line is a blur; *csók-* fits but is rightly declared unfirm.

## What I could not verify

- That a "Népszava-ünnepély" took place around 1912 in this region: context not checked, and the solver marks it as inference.
- What *majer* means.
- The identity of Feri and the date on the postmark; the date is from the portal.
- The washed-out first line under the stamp, sign by sign.
