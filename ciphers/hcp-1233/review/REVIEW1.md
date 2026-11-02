REVISE

# Review 1 of HCP1233 (reviewer: Claude Opus 5.5, 2026-11-02)

Summary: the key, the writing order and nearly all of the card are confirmed. The card is not yet a "complete reading". One clause (row 18 tail to row 19, "de ha [m]ost annak nem tanultam hiába") is not established: it rests on a doubtful sign, an inserted letter and a vowel change, and its meaning is not settled. The rule for this run says a whole unread clause makes a card partial and gets no register entry, so either that clause is established or the card goes out as partial.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1233/work/decode.py`: all four hashes OK. The literal rows match the SOLUTION.md listing exactly. The normalized text prints.
- `review/work/indep.py` applies the key separately to the ledger: 349 tokens, 22 sign classes, no unknown token. The concatenated plaintext agrees with the solver's rows.
- The key agrees with the HCP1216 table (read in its SOLUTION.md). The solver's "open loop = g, section mark = k" matches this hand (k = large S, g = small descending curve).
- Pixels: `review/work/crops.py` makes all crops from the hires address scan, plain and with my own purple-ink mask.
  - Rows 1 to 17: I read them sign by sign on L1 to L4.png (2x) and got the same literal text as the solver. *nagyin* (i rather than o), *éjszahig* (h) and *beletnéznem* (t) are on the card as stated.
  - Rows 18 and 19: B1, B2m, z18*, z19*, y1 to y3 (3x to 5x).
  - Row 20: r0, r1m, c1 to c3, q20. Row 21: T, t1, t2. Stamp box: Sm, sb.
- Reading order: I confirm the turn from the bottom edge up the right edge and along the top edge upside down.
- I tested a possible refutation on the top edge. Past *vela* there seem to be more signs (`t1.png`), but they are row 1 (*olan*) seen upside down. The top-edge row does end at *vela*.
- Bar counts: the last sign of row 14 (`q14.png`) and the sign in row 20 *na* (`q20.png`) both have two bars, so a is right.
- Published solution: none used as far as I can tell. The portal capture shows no attachment.
- Language and context: the rest is natural period Hungarian. The address, signature and formula fit the Jolánka family.

## Findings

1. **major: row 18 tail / row 19 clause is not established, and "complete reading" is overstated.**
   Evidence, four separate points:
   (a) The sign read h in *ha* is not like the h/p of this hand. `review/work/cmp_h_y.png` shows, left to right: the disputed sign, y of row 14, an unrelated control panel of row 14 without the sign, h of row 19, h of row 17. The h signs are a stem plus a tick, with no hook. The disputed sign has a left hook, a long diagonal and a stroke leaving the crossing to the right, which is the structure of y. The stamp cannot explain the hook, because black stamp ink is largely removed by the mask and the hook remains strong in it. SOLUTION item 8 mentions the hook but does not say that it points to another sign. *de ha* therefore rests on sense, not on shape.
   (b) *most* needs a letter that is not written. I agree there is no room for an m: the gap between a and o is about 40 px, and m in row 19 takes about 120 px.
   (c) *annek* needs a vowel change to *annak*.
   (d) The translations do not follow from the Hungarian. "if I did not study for it now, it would be in vain" has no logic in context, and no conditional is written. A different parse of the same emended text is "de hát most annak nem tanultam hiába" (but now I did not study for it in vain), which fits the passed exam better and gives the opposite sense for *hiába*.
   Clearly on the card: *nem tanultam hiaba* and *d e*. Not established: everything between them.
   Fix: either establish a reading, or mark the clause as unresolved, give literal signs with the y/h alternative, drop the invented sense from both translations and set the status to partial, with no register entry.

2. **minor to major (ledger misrepresents the pixels): row 20, restoration "[e][m]".**
   SOLUTION says the signs are "physically hidden" under the stamp, but the stamp letters E and U are thin and the purple pencil shows through them (`c2.png`, `c3.png`). What is there, between z and the clear lll of *mert*, is a dash, a purple curve mixed with the address flourish, and a distinct purple sign: bar, stem and closed loop. That last sign is visible and is not an m. No three-stroke m is present and it could not be hidden. So the token `[M]` is unsupported.
   Fix: transcribe what is there. Either one m is shared by *lefekszem|mert*, or a dialect form applies, with the loop sign marked unresolved. The sense "I am going to bed, because" is safe from *lefek-* and *mert*, so the normalized word can stand as an editorial reading.

3. **minor: rows 12 and 13, a second elliptic clause.**
   *nagyin utanna beletneznem* has i for o, a doubled n and an unexplained t, and no finite verb. "és nagyon utána bele néznem" is not grammatical without *kellett*. The solver discloses all of this. But the normalized text prints it as if it were a sentence and the status says "complete". State plainly in the status line that this sentence is an emended, elliptic reading. It is short and the words are visible, so I do not count it as an unread clause on its own.

4. **minor: row 26, f.**
   The sign in *Feri* is a nearly equal-armed tilted cross, close in form to plain X = u. This value rests on the name, and is not listed among the word-sense calls (compare the fog point of HCP1216). On the positive side, `sb.png` shows a stem and arm for r and a long curve running through the stamp residue for i, so *Feri* is somewhat better supported than "partly restored" suggests.

5. **minor: row 21 *vela*.**
   `t1.png` shows two bars plus a smudge at the very card edge, where a third bar may be cut. So *vele* may be what was written, rather than a slip. Item 10 can say so.

6. **minor: Slovak translation.**
   "ma zastihla takú nepripraveného" mixes genders; it should be "takého nepripraveného". Revise the Slovak with finding 1.

7. **minor: "Why it is correct".**
   The bullet "every sign of the whole card" turns into consecutive Hungarian is too strong, given findings 1 and 2. Reword it. The bullet on *nem* "×3–4" should give an exact count.

## What I could not verify

- Rows 24 and 25 in the stamp box: the signs across the printed triangle are only partly visible. m, a stem and l are seen, and z right of the triangle, but I could not confirm each sign of *szá-m-ta-lan-sz*. *számtalanszor* is the family formula and fits; the solver discloses this.
- Unenciphered note "Szigorúan magán": plausible on `note.png`, with the first word uncertain as disclosed. Postmark: only the letters PAL and part of a place name; no date. No identification claimed.
- The identity of Feri with the sender of HCP1216, which the solver also does not claim.
- Picture side: the solver's description of it was not re-read in detail by me; I looked only at the address side.
- What the disputed sign in row 18 really is. I show it looks like y but have no sound reading built on y.
