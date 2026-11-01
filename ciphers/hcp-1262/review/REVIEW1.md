ACCEPT

# Review 1 of HCP1262 (reviewer: Claude Opus 5.5, 2026-11-01)

The reading stands. I tried to refute it sign by sign and found no wrong word. All 25 rows read as coherent Hungarian with the Jolánka key, and the one restored letter is declared. Five minor disclosure and ledger points remain; none changes the text. The card qualifies as complete under the run's rule: no clause is unread.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1262/work/decode.py` from the repo root: all 4 SHA-256 hashes OK. Its output is identical to the literal and normalized text in SOLUTION.md.
2. **Independent decode.** `python3 -I review/work/independent.py` holds my own row-by-row transcription into sign classes, made from my crops. It maps those classes through `ciphers/hcp-1216/work/graphic-key.json`, read directly rather than through the solver's table (d and h, which that file does not hold under usable shape names for this hand, are assigned by tick side). It covers 356 signs in 25 rows. The check is not blind, because I had read SOLUTION.md first.
   22 rows agree with the ledger exactly once its `E?` and `M?` tokens are taken at face value (e and m, shape value). The 3 differences are:
   - row 2: `kadtam`, where the ledger has `kaptam` (finding 2)
   - row 18: `mamajet`, where the ledger has `mamajat` (finding 1)
   - S4: `holnah`, where the ledger has `holnap`; this is only the disclosed h/p homograph
3. **Pixels.** Crops are from `work/hires/*_adr.jpg`, in `review/work/crops/`, made by `crop.py` and `rows.py`. Enlargements were 2x for all 18 rows and 3–6x for contested signs.
4. **Each disclosed call, judged on the pixels:**
   - Row 7 *hölgyek*: smudged h, o and wave are consistent. No dots are visible, and the ledger correctly has no diaeresis. The k is an overwritten double loop (`r07sm`). All as stated.
   - Row 7 *d{ol}ja*: a pale inserted loop plus a small o stand on the bar of a clear inverted T (`r07comp`). It looks like a later insertion. "Forced" would be too strong: the signs are there.
   - Row 6 end: two short strokes and a taller one (`m2R`), as stated. The d that opens row 7 is separate.
   - Row 13 sign 2: three strokes, upper two converging (`m4L`), as stated.
   - Row 14 *ne*: heavy n with a crossbar, then three bars, as stated.
   - Row 4 extra e, row 15 end tick (`r15t`), row 17 j with a small tick: as stated.
   - Row 7 m: the third stroke sits under the postmark and is visible in dark red (`r07sm`).
   - Row 2 final m: the third stroke is very pale but real (`r02end`). The solver does not mention it, and it is correct.
   - S1: wave plus bars in the blot (`s1end`), supports *vele*.
   - S2: `s2end` shows s, z, o, n and a clear t.
   - S4: `s4end` shows a final tall stroke with a blurred tick on the right.
   - S5: the top hook of the last o is visible and the rest is under the blot (`s5end`). The m is truly unseen and is marked `[m]`.
5. **Sample of ordinary rows.** Rows 1, 3, 8, 10, 12, 16 and 17 match on every sign. Row 8 sign 1 is a pale but complete inverted T (`r08b`).
6. **Coverage.** Every sign has a value. Nothing outside the 25 rows carries cipher: no signature on either side, and the picture side has only the printed verse *Hej cigány, hallod-e?*
7. **Language and context.** The text is period Hungarian with a natural, unforced syntax, e.g. *nincs olyan órám, hogy ne gondolnék önre*. The tone, formulas and address (*Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás*) fit the family, as does the *tancz* spelling on HCP1273. I checked the English and Slovak against the Hungarian and they are faithful.
8. **Sources.** Portal capture shows Not solved and no attachment. I found no sign of an unacknowledged published solution. Number 1262 is not in `skip.txt` or `register-exclusions.json`.
9. **Date.** The postmarks show *JÁSZ…* and *…ROKS…* with no legible date (`pm1`, `pm2`), which agrees with the solver's item 15.

## Findings

1. **minor – Row 18, sign before final t, undisclosed.** The solver reads a in *mamáját*. The card has two clean bars and then an overwritten scribble (`r18endb`), so at least three bars, which is an e shape with a correction. It is an a only from word sense. The ledger has plain `A` and the Uncertainties list does not mention it. Fix: use a brace token like `E?` and add an uncertainty item.
2. **minor – Row 2 p is hidden in the "literal" output.** The sign has its tick on the left, the d class (disclosed as item 4). But the ledger token is plain `P`, so the printed "literal" says `kaptam`. Row 6, row 7 and row 13 get brace tokens for the same kind of call. The ledger header also says h stands for the h/p sign, while `P` is printed for S4 and row 2. Fix: a token such as `{d|p}` for row 2, and correct the header.
3. **minor – Item 10 overclaims.** "No other letter makes a word" is not true: *csókolok* is a word, though with *számtalanszor* and this family's formula *csókolom* remains the right restoration. Fix: justify it by the formula, not by exclusion.
4. **minor – Small undisclosed sign observations.** The i of *mikor* in row 13 has no visible dot (`r13i`), while the key table calls i "dotted" and only S2 is flagged. In row 11 the final a is overwritten (upper bar doubled, `r11endb`). At S7 the final o and r overlap (`stamp`). In row 14 the j stem runs slightly through its bar (`m4L`), which the key allows for t but not for j. None of them is in doubt; a one-line note covers them.
5. **minor – Row 5 closed bowl may not be the same sign as row 9.** Row 9 is two bowls joined at the base (`r09cs`). Row 5 is an angular left bowl with a long lower bar and a hook from above (`r05top`). HCP1273 writes c in *tancz* as a left bowl with a bar. So the row 5 sign may be a c variant, which would make the literal `tanczisko` and remove the "cs doing c's job" explanation, and "left bowl c (not used here)" would need softening. The word is unaffected. Fix: `{c|cs}` in the ledger and item 6.

No blocker or major findings.

## What I could not verify

- The S5 m, hidden under the blot. It is a restoration, correctly labelled.
- The o in *hölgyek*: whether dots existed under the smudge.
- Whether *holnap* belongs to *a viszontlátásra* or opens the next phrase (the solver's item 11). The order of the stamp text is inferred, not proved.
- Sender and date. HCP1273 has similar closing formulas and the same address form, but I did not test whether it is the same writer, and the solver rightly claims no link.
