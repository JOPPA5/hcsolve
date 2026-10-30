REVISE

# Review 1 of HCP1288 (reviewer: Claude Opus 5.5, 2026-10-30)

The cipher, the key and almost all of the reading stand. One clause in row 24 is misread, and that misreading is defended in SOLUTION.md as an awkward but unavoidable word. The fix is a one-sign ledger change plus the normalization and translations.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1288/work/decode.py` runs: 4 of 4 hashes OK, 784 signs, and the printed literal rows match the block in SOLUTION.md.
- **Independent decode.** `review/work/indep.py` uses a key retyped from the hcp-1216 table. It gives the same literal text and 784 signs, with 23 letter classes and every token mapped (1 `?`, 1 `|`). It also aligns the literal text to `work/normalized.txt`. The only differences are the 16 listed spelling edits, and all of them are disclosed or covered in findings below.
- **Pixels.** My own crops from the hi-res address scan are in `review/work/crops/`, made with `review/work/crop.py`: `a1L`-`a7R` (rows 1-22 at 2x), `b23a`-`b26d` (full-width rows at 1.9x), `stamp` (2.6x), and `z*` (2.7-3.6x) for disputed signs. I compared all 33 rows with the ledger sign by sign. The base signs agree everywhere except finding 1. Faint accents were not audited individually.
- **Key.** It is the hcp-1216 family key with no new values. The sign shapes on this card behave as in that table, including `( )` = cs, the 6 = b, the upright cross = f, and d (tick on the left of the long stroke) against h/p (tick on the right).
- **Language and context.** Period Hungarian throughout. Addressee, signature Feri, formal address and closing formulas fit the family. I found no sign that a published solution was used; the portal attaches none.
- **Register.** hcp-1288 is not in `register-exclusions.json` or `skip.txt`.

## Findings

1. **major: row 24, `amibol hog` is wrong; the card reads `a mi boldog`.** The ledger has `B O L H O G`, but the fourth sign after `A M I` is d, not h.
   - Evidence: `crops/z24.png` shows a heavy long stroke with a separate short tick on its **left**. `crops/z24row23.png` shows the undisputed *boldog* of row 23, with the same d form. The h/p sign has the tick on the right (*hogy*, row 17; `nehez`, row 24).
   - Corrected literal: `...desajnosamiboldogviszontlatasunknak...`
   - Corrected text: *de sajnos a mi boldog viszontlátásunknak mindig nehéz elválás a vége* ("but unfortunately our happy reunion always ends in a hard parting").
   - SOLUTION.md must change in the following places: `work/ledger.txt` row 24, the literal block, `work/normalized.txt`, the Hungarian, English and Slovak texts. Uncertainty 4 must be withdrawn; its statements that *amiből* "could not be replaced by a better one", that the sense "the thing is that" applies, and that "*hog* has no y" are all refuted. The `[sic]` goes too. The same miscall is the kind of d/h call Uncertainty 8 says was decided by the word, yet here the wrong call was kept against both sign and sense.

2. **minor: rows 24-25, the supplied `[a]` and *elválása* are unnecessary.** The literal `nehezel|valasavege` divides directly as *nehéz elválás a vége*, with every letter on the card and nothing added. Remove `[a]` and the *elválása* reading, and the note in Uncertainty 9 that goes with it.

3. **minor: Uncertainty 11, the green word is not faint pencil and it is readable.** It is a large word in the same green ink and hand as the address, running through the cancellation (`crops/green.png`). It reads *Szépreményű*, the first line of the address form *Szépreményű Tóth Jolánka úrleánynak* recorded on sisters hcp-1212 and hcp-1290. I read the letters as S-z-é-p-r-e-m-é-n-y-ű; the opening *Sz* is tangled with the postmark. Record the clear address in full.

4. **minor: Uncertainty 11, the second postmark is not mentioned.** Besides the boxed RÁKOSPALOTA-ÚJP. mark there is a round cancellation with rim letters reading upward at left as (…)SZ ÁRO(…), compatible with Jász-Árokszállás (`crops/pm.png`). Its date line shows partial characters ending in something like `1 3` (`crops/pmdate.png`). I do not claim a date from it. SOLUTION.md should say that a second, partly legible cancellation exists rather than only that the date is not legible.

5. **minor: row 22, the description of the `?` sign can be tightened.** In `crops/z22.png` the sign is a heavy cursive loop of the o class, directly followed by z, e, h, o, z. The literal is better described as `öszehö` followed by a restart `özehoz` (o-class sign + zehoz) than as an unreadable sign before `...ehoz`. The normalization *összehoz* is unaffected. This remains an interpretation of a sign in the ink stain.

6. **minor: row 25, the *a le[ve]lembe[n] [levő]* restoration is heavier than needed.** The signs *a l e ? e m b e* are read correctly apart from the sign before `e m`: in `crops/z25.png` it is a shortened wave with a separate tick and is not clearly l, so v is not excluded and should be named as an alternative. *a levelembe[li] kérdéseimre* needs one supplied suffix rather than *-n* plus a whole word. Either way, this is the writer's slip and the sense stands.

7. **minor: Uncertainty 10 lists *hög*→hogy.** No such form exists in the ledger; the only y-less form was the mistaken `hog` of finding 1. Delete it. The "Repeated words" and "no new value" points in "Why it is correct" stay valid, but "one unreadable sign" should be kept in step with `{|}` in S2 and the row 16 first sign, which is also only a contextual call.

8. **minor: row 17, a small undisclosed feature.** The second t of *belátta* has a heavy horizontal smear under it (`crops/z17.png`). The reading is unaffected. One clause in the uncertainties is enough.

## Items checked and upheld

- Row 16 `mentettem`: the first sign is a heavy joined N-shape, the same shape as the heavy m of S2, and the rest (e, n, t, e, t, t, e) is clear (`crops/z16.png`). The reading of the signs is acceptable, and the solver is right to flag the sense as unresolved.
- Row 12 *de azt*: the bars after *de* are two (`crops/z12.png`), so a, not e.
- Row 18 `vagyog`: the final sign is the g class, as disclosed.
- Row 22 `várok`: the r/t call is as disclosed.
- S2: heavy m-form, separate stroke, then a left bowl plus a nearly straight right element for cs, as disclosed. *kolom* is clear.
- Rows 23-25 under the portal stamp: the stated signs are consistent with what shows.
- *Hű kedvese, Feri*, *számtalanszor*, *érdekel*, *költséget*, *rossz anyagi helyzetemnek*, *kérdéseimre legyen szíves válaszolni*: all read directly from the signs.

## What I could not verify

- The year: 1913 comes only from the file name, and the date line of the round cancellation is too broken to confirm it.
- Accent marks at this scan quality; I checked base signs, not each faint acute.
- Whether this Feri is the Feri of hcp-1216 as a historical person.
- The sense of row 16 *mentettem*; neither the solver nor I found a word that fits both signs and sense.
- Portal content: I did not re-render the page and rely on `source/metadata.md`.
