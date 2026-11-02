REVISE

# Review 1 of hcp-1230 (reviewer: Claude Opus 5.5, 2026-11-02)

The reading stands: Hungarian, Jolánka key, and the story of the card is right. But the sign ledger is not a faithful transcription. I found 8 sign-level errors in 477 signs, and six of them are presented in SOLUTION.md as "writer's spellings, none in doubt". One changes a word of the normalized text (ez -> az). The ledger, literal text, spelling list and sign count must be corrected before FINAL.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1230/work/decode.py`: all 4 SHA-256 checks OK, 477 signs, exit clean. Its 26 rows match the literal block in SOLUTION.md exactly (scripted comparison, 0 mismatches).
- Independent script `review/work/verify.py`: own class-to-letter table, decodes the solver's ledger (no unknown tokens), applies my pixel corrections and prints the differences. Run from the repo root: `python3 -I ciphers/hcp-1230/review/work/verify.py`.
- Pixels: whole text block read in 12 3x tiles (`review/work/tiles.sh`, crops `t00`...`t23`), 2x bands (`bands.sh`, `a00L`...`a08R`), and 5x to 7x zooms of every disclosed call and every doubtful sign (`crop.py`, blue-minus-red/green `violet.py`). All from `work/hires/*_adr.jpg`. Crops are in `review/work/crops/`.
- Key: sign classes agree with hcp-1216; all letters on this card occur in that key, nothing was fitted to this card. Letter c is simply not used here. The `H` token is in the key script, but the table in SOLUTION.md lists h/p only under d (see finding 9).
- Language and context: period Hungarian, coherent throughout. *stikli*, *személyvonat*, *előléptetés*, *bejegyez* fit a man under service discipline. Address in clear: Tóth Jolánka, úrleánynak, Jász Árokszállás. Close *sírig hű kedvese* as on hcp-1216. Picture side: printed only.
- No published solution used, as far as I can tell; portal status and SOURCES.md agree. hcp-1230 is not in skip.txt or register-exclusions.json.

## Findings

1. **major. Row 7, *mert ez csak* is literally *mert az csak*.** The sign after `mert` has two bars, not three (crop `t02`, row 7; `a01R`). A = az, "that one". This changes the normalized text and the English/Slovak ("this one" -> "that one"). Ledger row 07 index 14: E -> A.

2. **major. Row 3 *talelja* is a misread: the card has *talalja*.** Crop `r3tal`: the sign between the two waves has two bars, like the A before it. So the word is spelled correctly on the card and the entry in the "writer's spellings" list is false. Row 03 index 6: E -> A.

3. **major. Row 7 *mitotottem* is literally *mitotottam*.** Crops `r7end`, `t01`: after T T only two bars at y≈552 and 572. The third bar above them (y≈517) is the bottom bar of row 6's e. The ending is correct -am, so "e for a" in the spelling list is false. Row 07 index 8: E -> A.

4. **major. Row 8 *orável* is *orával*.** Crop `oravel`: two bars, no third down to the crop edge at y=680. Row 08 index 7: E -> A. Spelling-list entry is false.

5. **major. Row 15 opens with a faded sign the ledger omits: a six.** Crop `r15L`, `t10`: at x≈80 to 120, y≈1130 to 1175 a rubbed 6 (rising stroke and bowl) stands before the faded e, in the same rubbed pencil as that e and t. So the card has *töb|bet*, not *tob|et*. The row reads `betnem...`. "b dropped" in the spelling list is false, and the count becomes 478. Insert `6` at the start of row 15.

6. **major. Row 21 *romt|ja* is *ront|ja*.** Crops `ront`, `t23`: after the o stand two strokes, then the stem of t with its bar slightly detached. M + T would need four strokes before the bar, and there are three. Row 21 index 16: M -> N. The spelling-list entry and the literal row are wrong; no oddity exists.

7. **major. Row 26 *seríg* is *sirig*, and uncertainty item 9 is wrong.** Crops `s26z`, `r26b`: the sign is a loop crossed by a long bar, the same form as the second i of the word. The three bars just above it at y≈2025, 2050, 2072 belong to row 25's e. No e stands for í. Row 26 index 8: E -> I.

8. **major. Row 17 *sanélom* is *sanálom*.** Crops `r17`, `t10`: two heavy bars joined by a short connecting stroke, with the accent dot above, and no third bar. Token should be A:acute. This is the least clean of the eight, because the connector gives it a slightly E-like look at low zoom, so say so. Spelling-list entry to change: only j is dropped.

   The pattern in 1 to 8 matters more than any one sign: SOLUTION.md says "every sign is transcribed as written" and "none in doubt", and the list of oddities was largely produced by misreading. After correction the writer's spelling is much cleaner: dropped letters (`szereret`, `aljob egezeg`, `sanálom`, `orakkor`, `regel`), not swapped vowels. The claim "drops, repeats and swaps letters" should be revised to what remains.

9. **minor. Undisclosed shape calls in the d/h family.** On this card d has its tick left of the long stroke (rows 1, 11, 22, 25, 26) and h has it right (rows 2, 5, 9, 10, 17, 19, 21, 22, 26). Row 23 first sign has the tick clearly to the right (crop `r23L`), i.e. the h shape, so *de* there rests on word sense and is not listed. Row 19's "p" has the left tick, the d shape; say that plainly in item 5. Add h and p to the key table.

10. **minor. Other undisclosed word-sense calls.** Row 21 first sign is a heavy chevron with extra strokes across it (crop `r21L`), v only by word sense. Row 2, g of *egezeg*: under the postmark, closed bowl, nearer the six than this card's open g (crop `r2g`); g by word sense. Add both to the uncertainty list.

11. **minor. Row 8, the supplied word is not established, and the note's reasoning is weak.** *[később]* ("later") is a guess presented as "the natural sense". "Later" does not explain arriving late on a different train; *[előbb]* / *[korábban]* ("that train went an hour earlier than I reckoned", so he missed it) fits at least as well. Give both options, and the English/Slovak should not commit to one without saying so. The word order remains a gap in the writer's text, as stated.

12. **minor. Row 26 final [i] is supplied, not restored.** Solution item 3 mentions a faint smudge and the ledger header says restorations are hidden or rubbed signs. Crops `end26`, `end26v`: blank paper after the r, no violet trace at all, only a brownish foxing spot further right; the neighbouring faint signs are all still legible. Literal is *fer*. Call [i] an editorial supply; he may simply have stopped there.

13. **minor. Marks not transcribed, while the ledger records others.** Row 16 last e has a clear acute; row 13 a has a mark above; row 14 has two ticks over the o/b junction (crop `t13`), probably the ö of *többet*. Harmless, but add them or say the ledger is selective.

14. **minor. Dating note.** SOLUTION.md says the date comes only from the file name. The Budapest postmark visibly reads `913 DE`, which supports December 1913. Use it. Its full day digits I could not read.

## Calls I checked and accept

- Row 1 k: blot, no shape recoverable, disclosed; fine. Row 1 sixth sign is r (`r1six`, with middle bar), so *szereret* is genuine.
- Row 2 first sign: clear six, *bivanom* correct as literal, disclosed.
- Row 2 end: signs past `egezeg` are not violet, so postmark, agreed.
- Rows 3, 4 ends (e, m under the stamp): agreed with violet crops. Row 6 end ) Z Á: agreed, the s is angular but fits.
- Row 14 *elsimulj*, rows 15/18 *ijesmit*, row 18 `bejegyzi és`, row 22 *előrhaladast*, row 24 *almos*: agreed on pixels.
- **Row 25 `dak`:** I confirm the literal. One heavy rising stroke plus a very faint left tick, two faint bars, clear k. No chevron leg and no room for a sign before it. *[va]gyok* is sense only, correctly disclosed. It is a single word alone in a reading text, so under the batch rule the card can count as complete. One alternative worth a line: colloquial *vok* would need o, and the second sign is a, so it does not read either.

## What I could not verify

- The sign under the row 1 blot, and the actual word behind `dak`.
- Whether row 8 meant later or earlier.
- The second postmark at top left (`...16`), and the wording of the address under the postmark.
- Identity of Feri.
- Family key was compared by sign classes with hcp-1216's table; I did not re-review the other family cards.

## Required before FINAL

Correct `work/ledger.txt` as in findings 1 to 8 (`review/work/verify.py` holds the exact edits and the resulting 26 rows), update the literal block, 478 signs, normalized text, translations, spelling list, uncertainties and "why correct". Address 9 to 14. No new DONE round is needed if the changes are limited to these, since the reading stands.
