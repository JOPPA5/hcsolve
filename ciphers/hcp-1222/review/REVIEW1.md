REVISE

# Review 1 of HCP1222, Claude Opus 5.5 (reviewer), 2026-11-02

The card is the Jolánka/Feri key and the message as a whole stands: arrival at Gyöngyös, a missed train, job hunting, closing formulas. The sign ledger is not a complete record, though. It drops four written signs at row ends or in mid-row. Three of those gaps were then explained as writer's omissions. The normalization of the key clause also counts three signs twice, which distorts its meaning. These are concrete fixes, so the verdict is REVISE, not REJECT.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1222/work/decode.py`: all four SHA-256 checks pass and the output matches the literal text in SOLUTION.md.
- Wrote `review/work/decode_review.py` with my own glyph names and my own sign-by-sign reading, mapped through the HCP1216 family key. It runs the solver's command and compares row by row (accents ignored).
  Result: 390 letters (mine) against 386 (solver); 22 of 26 rows identical; rows 5, 6, 11 and 18 differ.
- Read all 20 rows and the stamp corner on my own enlargements of the hi-res address side: `review/work/b0_0.png` to `b7_2.png`, `corner.png`, and `z_*.png` for the disputed places (made by `bands.py`, `z.py`).
- Key: no new sign value is needed anywhere; every sign on the card maps to the family key. The h and d signs are visibly distinct on this card (row 11 d against row 12 h).
- Picture side: photo only, no writing, confirming the solver's statement.
- Plain address: I confirm *Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás*.
- No published solution appears to be used; portal status and SOURCES.md agree, and the key is credited to the family cards.

## Findings

1. **major: rows 12/13, the normalization counts `hol` twice and the translation rests on that.**
   Row 12 ends `h o g y h o l` and row 13 begins `g o z ? k`. Uncertainty 2 says the three signs `hol` are to be read `dol` of *dolgozzak*. That gives *hogy dolgozzak*, "that I should work". But `normalized.txt` prints *hogy hol dolgozzak*, using the same three signs both as *hol* and as *dol*. The English ("that I should find where to work"), the Slovak and the title ("father's order to find work") carry the extra *hol*.
   The sense also improves without it: "the word is out that I should work, for he will not feed me".
   Fix: normalize *hogy dolgozzak* and correct all translations and the title. If the solver prefers *hogy hol [dol]gozzak*, it must be stated as a restoration of an unwritten syllable (a skip from *hol* to *dol*); that is the less economical reading and it contradicts item 2 as written.

2. **major: row 11, a whole sign is missing from the ledger, in the weakest clause.**
   See `review/work/z_r11b.png`. After `k i a d t a` the card has a further bar sign before `d e a p a m`: bars at three levels, the lowest heavy and slanted, and a separate tick at upper right (possibly an acute, possibly stray). So the literal row is `esmerkiadta` + e/é + `deapam`, not `...kiadtadeapam`.
   The solver's *Kiadta de apám*, with *de* as an "emphatic particle", is built on a text one sign short. I cannot confirm the phrasing. The -e question particle (*kiadta-e*) is one possibility to test, not a reading I propose. Even if this stays open, it must be listed as an unresolved sign and the emphatic-particle gloss reconsidered. The overall sense (father has given out the word) is not affected.

3. **major: row 18 end, final `s` missing and the first vowel misread; uncertainty 9 is false.**
   See `review/work/z_r18end.png`. After `k` the sign has three bars (e), not two. After `v e` a clear right-bowl s stands beyond the printed divider line. The row reads `...k e d v e s`, literally *kedves*. Uncertainty 9 asserts "two bars ... and no final s at the end of the row". Fix the ledger and delete the claim of *a for e, s omitted*.

4. **major: rows 5 and 6 ends, signs under the postmark were dropped and explained away as writer's omissions.**
   Row 5, `review/work/z_r5end.png`: past the ö stand two strokes at baseline height, in the script's brown ink, partly over the postmark: n, so `gyön|gyösre`. They are not "ticks to its upper right"; the diaeresis is separate, above. Written *Gyöngyösre* is regular, so "n omitted on both sides of the row break" is wrong.
   Row 6, `review/work/z_r6end.png`: past the final e stands a long stroke and further strokes running into the postmark block: m (at least two are clear, a third is partly hidden), so `...megnem`. "m omitted" is wrong. Say which strokes are obscured.
   The normalized text is unchanged by both, but they are false statements about the writer's spelling.

5. **minor: claim "Every letter was read from the pixels except where stated" does not hold**, given findings 2 to 4. The four dropped signs should be recorded in NOTES.md and the statement reworded. All row ends should be rechecked; I found no further drops.

6. **minor: row 15 `este rá bővebben`.** The sign after r is two bars (`review/work/z_r15.png`), so `a` is right; the tick below belongs to the é of row 16. But *rá* is not explained, is not listed as uncertain, and is silently absent from the English and Slovak. *estére* ("by evening") suits the sense but would need e, so it is a spelling-level emendation. List this as an uncertainty and translate it consistently.

7. **minor: row 7 `sors`.** The last sign (`review/work/z_r7sors.png`) has the k shape of rows 5 and 8. Item 6 discloses this; I agree that *sors* is by sense only and the only sensible word.

8. **minor: stamp-corner `feri`.** The f sign is a blotted star shape and is not listed in the uncertainties. The name is safe from the family, but the blot should be stated.

9. **minor: key description.** SOLUTION.md says "key unchanged", but its d description (short + long) differs in wording from HCP1216's table (long stroke + short tick). The row-by-row result supports the solver's d/h contrast on this card; state it as this hand's form.

10. **minor: Slovak** *Pozdravujem aj Manczika* needs the accusative (*Manciku* / *Manczikovú*).

11. **minor: postmarks are more legible than stated.** A date with *13* and *JAN* is readable on the left mark, and a letter G begins the right mark's rim text. This may support Gyöngyös, but it is only an initial, so check it and do not over-claim.

## Checks that held up

- Blotted sign, row 13 (`goz?k`): an arc above and a heavy blot, a bar sign. a is reasonable, and the disclosure is fair.
- Row 14 first sign: heavy doubled strokes, *De* by sense, disclosed.
- Row 11 `apam`: the p is a long stroke + tick under the cross of row 10, and it is distinct.
- Rows 19 and c5, r without mid bar: visible as described and disclosed.
- Row 3 overwritten t, row 8 `hel`, and rows 15 to 17 (`majd`, `este`, `Isten vele`, `vigyázzon egésségére`): all confirmed.

## What I could not verify

- The word intended by the extra row 11 sign, and whether its tick is an acute.
- The exact stroke count of the row 6 m under the postmark block.
- The identity of Manczika or Feri beyond the family cards; I did not re-check the claims about HCP1303/1310 and later Gyöngyös references.
- I made no attempt to confirm a date beyond the postmark reading above.

## Consequence for the register

The card should go forward only once findings 1 to 4 are fixed. If the row 11 sign remains unexplained, it is a single sign in a clause that otherwise reads, so it does not by itself make the card partial, but the solver must say so explicitly.
