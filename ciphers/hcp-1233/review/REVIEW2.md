REVISE

# Review 2 of HCP1233 (reviewer: Claude Opus 5.5, 2026-11-02)

Summary: the key, the writing order, rows 1 to 17, *Istennek nem tanultam hiába* and the signature all hold. The solver's row 13 correction to *kelet(t)* is right, and my review 1 was wrong to accept b there. One new claim does not hold: the [l] of *hál'*. The stroke the solver counted as a separate l is, on the pixels, the upper arm of the following i/o sign. So no l is written, and "no letter is inserted" is false. *hál'* is now a restoration from sense, of the same kind as the withdrawn *[m]ost*. The sense survives, and it is one word in a clause that otherwise reads, so the reading stands. The ledger and the text about it need correcting before FINAL.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1233/work/decode.py`: all four hashes OK. Output matches the SOLUTION.md listing row for row.
- `review/work2/indep2.py`: my own token table, not imported from decode.py. 350 tokens, 22 sign classes plus `?`, 7 bracketed tokens, no unknown token. The text agrees with the solver's rows.
- `review/work2/crops.py` makes all new crops from the hires scan, with a purple-ink mask (rewritten percentile clip).
- Rows 1 to 17: read sign by sign on L1 to L4.png (2x). Same text as the ledger, including *nagyin*, *éjszahig* (h), *is* (crossed i).
- Row 13: `r13e.png` confirms three bars then m (*néznem*, not *néznam*). `work/resp/cmp_k_b.png` checked: the first sign has the k ductus, not the stem-and-bowl of b. *kelet(t) néznem* removes the problem of review 1 finding 3. Accepted.
- Row 18 tail: t1 to t4.png, b18b/b18bm, sign_join(_m).png, sign_h.png, cmp_isten.png, cmp_loop.png.
  - *d e*: stem with left tick, then three bars. Confirmed.
  - *a* after the disputed sign: two bars, under the stamp's "o" and its diaeresis. Confirmed.
  - *s t*: confirmed. `cmp_isten.png` sets row 21 *isten* above row 18: same sequence of forms (crossed loop, bowl, gamma, bars), which supports *isten* here more strongly than the solver argues.
  - [e]: my coordinate mapping of the rotated x20bm crop onto t4 gives the same three staggered bars at x 3096 to 3175, y 1858 to 1933, independently of the solver. The solver's reassignment of these dashes to row 18 is right, and [e] stands. *nek* in row 19 clear.
- Row 19: b19, b19bm: *neknemtanultamhiabamostmarlefek* confirmed to the corner (t4.png: + e k).
- Row 20: r20a/m, x20a/m, x20b/m. Rows 21 to 26: top.png, box, boxm. *csokol*, *jasza*, m, l, n, sz, o, r, f, e read as claimed. In row 26 the third bar of e is a blot at the damaged spot, so e is fair but not "clear". The m-t-a of row 24 lie on the triangle and stay as stated in uncertainty 11.
- Picture side: printed title and verse only, no pencil. Agrees with SOLUTION.md.
- Translations: English and Slovak follow the normalized text. *takého* fixed. Counts in "Why it is correct" (*hogy* ×4, *nem* ×3, *tanultam* ×2, *vizsga* ×2) agree with the ledger.
- No published solution used as far as I can see.

## Findings

1. **major: row 18, the token [L] is not a sign. *hál'* has no written l.**
   Evidence: `review/work2/sign_join.png` and `sign_join_m.png` (hires box 2840,1855,2990,1985; 10x), `cmp_loop.png` (same scale: this sign, then ö of *könyv* in the same row, then i of row 21 *isten*).
   The ö and the i of this hand are made in one ductus: an arm rises to the right, turns at an apex, a descender runs down-left to a loop, and a tail goes up to the right and crosses the descender. In the disputed place, the descender starts at the point where the "straight stroke" ends, and there is no other arm. Separate those two and the [i] is a loop with no top, a form I find nowhere on the card, while the "l" is a stroke with no wave. All 19 other l signs are waves (row 19 end, the l of row 25). Taken as one sign, everything is accounted for: a long-armed i/o with a sharp apex and a small overshoot of about 9 px. Its only difference from the ö is the straighter arm.
   Consequence: the signs after *de* are `[?] a [i/o] s t e n`, and SOLUTION item 8 ("[l]", "No letter is inserted and no vowel changed") is wrong. *de ha Istennek* is what stands literally. That is not idiomatic, so *hál'* or *hála* needs an unwritten l, or the disputed sign must carry it.
   Not proven: the overshoot leaves a small chance of a separate stroke. But then it is still not a wave, and the loop still lacks its arm.
   Fix: remove `[L]` from the ledger, merge the stroke into [I], and state that l is unwritten and supplied. Say in the literal row and the normalized text that *hál'* is restored: for example *de h[ál]' Istennek*, with the first sign also from sense. Item 8 must drop "no letter is inserted". Drop "four sense calls" and give the real count. The sense "thank God" remains the best reading: *Istennek*, *nem tanultam hiába* and the passed exam all point to it. I found no better word (*de ha*, *de hát* do not give *Istennek* a role), and it is one word in a clause that reads, so under the run's rule this alone does not make the card partial. But it must be disclosed as a restoration.

2. **minor: the first sign of *hál'* still looks like y, and "stem runs on past the crossing" is weak evidence.**
   `sign_h.png`: part of what looks like hook and right arm lies on stamp letters S and I, but purple pencil is there at both. A long y in row 14 (L4.png) also runs well past the crossing, so this does not separate it from y. Only the short stroke to the right, about 45 px, favours h, and it is larger than the h tick in rows 14 and 17. Item 8 discloses the sense call but overstates this difference. Fix: say that h rests only on the right stroke and on sense, with y as the alternative shape.

3. **minor: row 20, the `?` dash may be the bottom bar of an e, and the text contradicts itself on the word.**
   `x20am.png` (mask): between z and the loop sign there are three short strokes at one x position, at spacing of about 20 to 27 px, which is the bar spacing of e in *mert*: one inside the flourish, one darkening the lower flourish line, and the dash. If that is e, the written word is *lefeksz-e-* and the standard *lefekszem* is available, with the loop sign left over. SOLUTION line 101 still cites *lefek|szem*, while the ledger and normalized text say *lefekszo(m)*. This cannot be settled through the flourish. Fix: give both options in uncertainty 1, make line 101 agree, and do not treat *lefekszom* as firmer than *lefekszem*. The sense is unchanged.

4. **minor: one unassigned mark at the corner.**
   `t4.png`, card x about 3195 to 3220, y about 1860 to 1873: a small v-like stroke right of the staggered bars. The solver's mapping of the corner does not mention it. It may be a stray mark or the start of row 20. Add it to the list of marks without a value.

5. **minor: "Why it is correct" and the status line need rewording after finding 1.** "Sense calls in rows 18, 20 and 26" should say that row 18 includes a supplied letter. Row 26 "e is clear" should be softened: two clear bars plus a blot.

## What I could not verify

- Whether the written word is really *hál'*, or how the writer got there. There is no sister-card instance of the word in the Jolánka cards I searched (1212, 1213, 1216, 1217, 1218, 1243, 1301).
- Sign identity under the address flourish in row 20, the value of the loop sign, and whether it is o.
- Rows 24 and 25 across the triangle: as in review 1, visible traces fit *számtalanszor* but not every sign is confirmed.
- Note "Szigorúan magán", postmark and date: not re-examined beyond review 1. No claim depends on them.
- Identity of this Feri with the HCP1216 sender, which the solver does not claim.

## Note for the solver on the register rule

The reading stays complete under the rule only with finding 1 disclosed: one restored word, the rest reads. Item fixes that change the words above do not need another round if the plaintext meaning stays as it is. A new reading of the clause does.
