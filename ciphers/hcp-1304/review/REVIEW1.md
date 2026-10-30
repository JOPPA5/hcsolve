REVISE

# Review 1 of HCP1304 (reviewer: Claude Opus 5.5, 2026-10-30)

The decipherment stands: the family key is right and the transcription agrees with mine on every sign except the row-25 ending. Three concrete fixes are needed. The "one real residual" at the end of row 25 is readable, and with it two other disclosed oddities resolve.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1304/work/decode.py` ran; all four SHA-256 checks passed; 603 tokens; its output equals the literal block and the normalized text in SOLUTION.md.
- **Independent decode.** `review/work/my_decode.py` has its own key table and my own sign-by-sign reading of the card, made from fresh crops (`review/work/*.png`, 2.2x to 7x, of the hires address side) in a separate stroke notation. It then diffs against the solver's output. Run from the repo root: `python3 -I ciphers/hcp-1304/review/work/my_decode.py`. Result: 26 of 32 lines identical. Of the other six, four differ only in notation (the two written stops, `{i}`, and `h` where the solver writes `{n}`); `ir{ja}a` is my literal `iroa`; the only substantive difference is the end of row 25 (finding 1).
- **Transcription against the scan.** I read all 26 rows, the whole right-edge run and the stamp box, not a sample. Every disclosed sign call was checked at 4x or more: rows 3, 8, 14, 18, 20, 22, 24, 25, the corner, and the margin end. Rotated margin crops: `m1r.png`, `m2r.png`; corner: `corner.png`, `end25.png`.
- **Layout.** Rows 25 and 26, the corner turn and the stamp box are as the solver describes. The picture side was not re-examined beyond the solver's statement (see below).
- **Key.** Agrees with HCP1216's table. Every ledger token is in the key; the key was not altered. *gy* is written here as two signs (open-loop g + y), visible on the card, so the family's joined gy sign is not used. Harmless.
- **Language and context.** Natural early-20th-century Hungarian in the family's formal *Ön* style. Moczár also occurs on HCP1295. The recurrence counts in "Why it is correct" check out (Jolánka ×4, hogy ×3, Moczár ×3, sztrájk ×2, restel- ×2). The closing *sírig hű kedvese Feri* is on HCP1216.
- **Sources.** The portal capture shows no solution attached, and the card has no earlier work here. Nothing suggests an undisclosed published solution.

## Findings

1. **major: the end of row 25 is readable: `volta tö|meg` = *volt a tömeg|sztrájk miatt*.** SOLUTION.md item 1 calls `a {h|t}o` the one real residual and says no reading gives a word. The evidence points to a reading.
   - The "stroke + separate arc" is a t. The arc is long, nearly horizontal and hooked down at its end (`end25.png`), which is the top bar of the gamma, drawn with a pen lift. The tick of the h/p sign is short and steep (compare `/ '` in rows 22 and 24). This is not an h.
   - The ledger misses two marks: a stroke and a small tick to the upper right of the loop (`corner.png`, above and right of the loop). They are the double mark of ö. The ü of *gyülés* in the same row has the same pattern, a heavy mark plus a small tick (`c3.png`, top right). The solver does not transcribe these marks at all.
   - The result is `a tö` + row 26 `meg sztrajk miatt`, which is *a tömegsztrájk*, the same compound written on row 18. The sentence becomes *mert gyűlés volt a tömegsztrájk miatt*, "because there was a meeting on account of the mass strike". The row break falls inside a compound, as at *Mo|czárék* and *rest|ellem*.
   - Fix: ledger `T=H?O` to `T = T O"`, literal, normalized text, all three translations, uncertainty item 1 and the "Why it is correct" sentence. The `ahol` alternative falls away, and the corner wave stays with *ha va|lamit*. The solver should confirm the two marks on the pixels and may state that the dot assignment rests partly on sense. The status line should drop "one end-of-row fragment".

2. **minor (fix with finding 1): `miattamazt` is *miatt, ám azt*, not *miatt. Amazt*.** All the signs are clear and the transcription stands, but the division is wrong. *Ám azt hiszem, kedden kezdődik* ("but I believe it starts on Tuesday") is ordinary Hungarian and removes the odd accusative of uncertainty item 8. Together with finding 1 the referent also becomes clear: the strike is the only subject in the clause before it. Rework English and Slovak ("That other one…" should go). Keep the referent marked as an inference.

3. **minor: row 14 `ugyen` is *úgy én*, not an emended *ugyan*.** The signs are `X G Y 3 II` and no a is written. *Úgy én elmennék a városból, ha sorozás nem lenne* ("So I would leave the city…") needs no spelling correction, and it follows *mintha messze volnék* better than concessive *ugyan*. Item 10 should drop `ugyen → ugyan`.

4. **minor: row 20 `hazudn{i}` has a dot.** Item 4 says the final sign has no dot of its own and that the dot below it belongs to row 21. The dot below does belong to row 21, but there is also a dark mark directly above the sign (`r20b.png`, near the red line). That mark is not part of row 19's e. Most likely it is this i's dot, so ledger `I>i` can become plain `I`, and item 4 should say so.

5. **minor: row 22 j is undisclosed.** The j of `hejzetem` has its crossbar set low with a short tail below it (`r22.png`), closer to a cross than the other j's; f is excluded only by word sense. Row 14 gets this note (item 7) and row 22 does not. Add a clause.

6. **minor: `vasár` has an open alternative.** *Vasár[nap]* is fine, and *vasár* is itself an older form of the word for Sunday. But accents are unwritten, so *vásár[ra] lemegyek* ("go down to the fair") is possible with an assumed omission. Item 10 should say so briefly; the translation may keep Sunday.

7. **minor: postmarks are understated.** SOLUTION.md says they give no clear place. The cancel at the stamp box shows the legible letters GYÖ, probably followed by N (`pm.png`, overview `full.png`). The other shows …ÁS and fits the destination Jászárokszállás. Record the partial legend without claiming a town. Gyöngyös is a possible but unproved reading, and it would fit *lemegyek*. No date is readable; I agree with that.

8. **minor: margin end `ir{ja}a`.** Disclosed correctly, and I confirm no inverted-T sign is there. The sign is the undotted loop, so the literal is `iria`/`iroa`. Writing `{ja}` in the literal block slightly overstates it; a marker such as `ir{o|i}a` would be more exact. *Írja meg* remains the reading.

## Confirmed as disclosed

- Row 3: blot over the h/p sign; tall + short is visible.
- Row 8: two bars and a separate spot; a is right.
- Row 24: `tala{n}` is a tall + short sign and is sense-only. The disclosure is honest. I see no better word.
- Writer's spellings in item 10, apart from finding 3.

## What I could not verify

- The date, the sender's town and any identification of Feri or Moczár; which strike is meant. The solver claims none of these, correctly.
- The two ö marks in finding 1 are small. Their assignment rests on the matching shape in the same row and on the resulting word, not on an isolated clean sign.
- Whether the mark above row 20's last sign is pen-made rather than accidental, though it matches the ink.
- I did not search independently for a published solution, and relied on the portal capture and the orchestrator's register check.
- The picture side: taken from the solver's statement only.
