REVISE

# Review 1 of HCP1223 (Claude Opus 5.5, reviewer, 2026-11-02)

The reading stands: Hungarian, Jolánka-family MASC, and the normalized text and translations can stay as they are. The ledger must be corrected at two places. One of them contains a sign that is not on the card, and the literal text and uncertainty 4 are built on it.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1223/work/decode.py`: all four hashes OK, 415 signs, no unvalued sign. I compared its literal rows and normalized text with SOLUTION.md by eye; they agree.
- Independent decoder `review/work/decrypt.py` (own mapping written from the hcp-1216 sign table, run on the ledger): same letters, 415 signs, no unknown token. This tests the key application only; the reading test is the pixels below.
- Read all 22 rows and the 6 stamp rows sign by sign from my own crops of the hires scan: `review/work/crop.py`, `crop2.py`, `crop3.py`, output in `review/work/crops/` (2x bands; 3-4x zooms on rows 19, 20, 21, 22, signature).
- Because the row 19 error sits where the solver's left and right crops overlap (x 780-860), I checked the same seam on every other row, comparing coordinates in my own L and R bands. No other sign is doubled.
- Key coverage: all signs fall in existing classes; no new value was introduced.
- Picture side: printed photograph, no. 1012, no writing. Address side reads as claimed; postmark shows GY and 913.
- Published solution: no sign of one. `source/metadata.md` shows Not solved and no attached solution.
- Context: hcp-1301 has the same writer's fire-brigade duties (tűzoltógyakorlat) and the same "imádója" and "nem mehettem le" phrases, so the unexpected fire-brigade content and *imádójára* fit the family.

## Findings

1. **major: row 19 ledger has a sign that is not on the card (`malen` is wrong).** The ledger gives `T E M M A L E N M E R T ...`, which needs five strokes between the e of *le* and the e of *mert*. There are three. See `review/work/crops/row19.png` and `z19.png`: wave (x about 625-700), three bars (732-777), exactly three strokes (805-890), three bars (912-950), F. The three strokes straddle the seam of the solver's overlapping crops (L ends at 860, R starts at 780), so two were probably counted twice; the notes record the same kind of slip for B3/B4. Literal row 19 is `temmalemertatüz`, that is *ma le mert*, with nothing irregular. Fix: delete the N token; the count becomes 414; correct the literal table; withdraw uncertainty 4 and the "ma len" line in NOTES.md (add, do not erase). The normalized text already has *ma le* and does not change, but the claimed "slip or dialect form" never existed.

2. **minor: row 21 `gondolt` is a third d written in the h/p shape, not disclosed.** See `crops/z21d.png`: long stroke with a separate short tick on its right, the h/p form. The usual d on this card has the short stroke on the left of the long one (rows 1, 8, 14 *gondol*, 22). The ledger writes plain D. Uncertainty 6 says the h-shape for d occurs only in *de* (rows 10, 14). Fix: mark it HD and add it to uncertainty 6. The word itself is safe, since *gonhol-* gives nothing. The solver's key summary, "long stroke joined to a short one", should also state the distinguishing point actually seen here: which side the short stroke is on.

3. **minor: inconsistency on the signature.** The title says "Feri to Jolánka Tóth", while uncertainty 5 rightly says only `fr` is on the card and that Feri is not restored. Say "Fr… (probably Feri)" in the title or equivalent. I confirm the reading f, r: upright cross with a tail, then F against the stamp remnant; what lies under the remnant cannot be seen.

4. **minor: wrong descriptions in SOLUTION.md uncertainty 10 and "Why it is correct".**
   - `oltottestület` is described as "one t shared between the words". The row has two t's (`o l t o t t e s t`), where *oltó testület* needs two t's only with o between them, written `oltotestület`; so one t is extra, not shared.
   - `vessefr → vese` should say *kedvese*.
   - "*nem* ×5": as a word it occurs three times (rows 9, 15, 18); the others are substrings such as *mindenem*. Correct the count. The other repeat counts are right.

## Points tested and upheld

- Row 22 `néhrm`: confirmed at 4x (`z22a.png`, `row22a.png`). e, n, é, h/p shape, r, m, with no bars between them. The two vowels are supplied, and the solver says so. The strokes of the m are unusually heavy and the first has a small spur, which might be a rewrite, but nothing readable lies under them. *néh[a] r[á]m* is by sense only and is correctly labelled. It is a short contracted phrase in an otherwise clear sentence, so it does not make the card partial.
- Row 21 `vana` (`z21L.png`): two bars, and the dash lies below them, directly above the é of row 22 and slanted like the accent ticks elsewhere. *van a* is right.
- Rows 10 and 14 `de`: h/p shape confirmed; disclosed. Row 22 `imádójára`: the sign after j has two bars (`z22b.png`), so a.
- Row 20: the blot in *testület* is the third bar of e (`z20.png`), so e is right; row 19 ends t ü z with a tailed cross.
- Row 9 dot, row 7 dot, row 21 dot: present. Rows 1 to 18 otherwise match sign for sign.
- Under the stamp: isten, vele, édesem, csokol, jahüked, vessefr all confirmed; the second sign of S6 has a faint top bar and is e. *Isten vele édesem* is written twice on its own signs.
- Grammar and language: period Hungarian with formal Ön address, not forced.
- Other uncertainties (3, 7, 8, 9, 11, 12, 13) are accurate.

## What I could not verify

- Whether anything follows `fr` under the stamp remnant.
- Accents not visible in the ink; the solver's supplied accents are editorial.
- The postmark place beyond GY, and the date beyond 913.
- The ledger review is not blind: I had seen the solver's text before reading.
