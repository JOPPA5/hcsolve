REVISE

# Review 1 of HCP1257 (Feri to Tóth Jolánka): reviewer Claude Opus 5.5, 2026-11-01

Verdict: **REVISE**. The reading stands: the key is right, and the message, stamp rows and clear-text edge are read correctly in substance. But the ledger has four sign-level errors that I checked on the pixels. One of them (row 26) changes a disclosed uncertainty. Three normalized forms also need correcting. No finding changes the sense of the letter, and there are no blockers.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1257/work/decode_opus.py` prints four hash `OK` lines. All literal rows 01 to 30 appear verbatim in SOLUTION.md. The normalized text it prints is the same as the Hungarian section.
2. **Independent decoder.** `review/work/decode_review.py` maps ledger tokens to named graphic classes, then to letters through `ciphers/hcp-1301/work/graphic-key.json`, not through the solver's KEY table. Result: 38 rows, 821 tokens, 0 rows differ from the solver's output. Every token has a value. There are 11 special tokens, one each, and all 11 are explained in the ledger header and in SOLUTION.md. The key therefore covers the whole ciphertext, and it is the family key with no new value.
3. **Transcription against the pixels.** I made my own crops of the hi-res address side in `review/work/crops/`. `t1` to `t8` and `b1` to `b4` at 1.8 to 2x cover all 30 rows. `r5b`, `r7`, `r15b`, `r26b`, `r11`, `r11c`, `r8b`, `r24`, `r23`, `n1`, `n2`, `l1` are 3 to 6x detail crops. `st` is the stamp at 2.8x and `edge0` to `edge2` are the right edge, rotated. I read rows 1 to 30 sign by sign at 2x and at 3 to 6x for every sign the solver marks and every sign I doubted. Apart from the findings below, the sign sequence agrees with the ledger.
   - Solver's flagged points, confirmed as described: row 8 `jeel` (signs clear), row 10 blot, row 11 crowded k/o and the blotted e, row 14 Lambda-like n on the printed line, row 21 `nar`, row 24 open hook after d, row 27 name, row 30 stain over i.
   - The three small digit-like marks in row 27 really are there, in the card's green ink (`n2`): 6, 4, 6 under and after the o, not part of the portal's grey stamp. The sign after them is a dark blotted z.
   - Stamp rows S1 to S8 (`st`): all confirmed. S5 has the sign before `o` lost at the tear, so [d] is a true restoration and is disclosed as one. S1 final l and S7 final a are as faint as stated.
   - Right edge (`edge0` to `edge2`): *tisztelen Bélit és kedves mamá…* is confirmed; the end curls up the corner and is cramped.
4. **Language and context.** Natural early 20th century Hungarian love-letter prose with the formal address and the writer's usual dropped letters. Feri, *Árokszállás* and the closing formulas fit the family. The address is in clear and the picture side has no cipher, as stated. The argument is specific and continuous across row breaks; this is not noise forced into words.
5. **Honesty.** The portal status *Not solved* with no attachment is recorded. No outside plaintext is used. Solver and date are stated truthfully; there is no earlier work on this number. Uncertain calls are listed in detail.

## Findings

1. **major: row 26 is `gyaraban`, not `gyeraban`, and the sign is not e.**
   - Evidence: `r26b.jpg` (6x). After `g y` the sign has exactly two tilted bars, the same as the two-bar a that follows F. The two round dots below them are the ö-dots of row 27 *rölam*, not a third bar.
   - Effect: SOLUTION uncertainty 2 says *gyakrabban* needs "dropped k and b and e for a". That is wrong. It needs only a dropped k and a single b, the same kind of omission as *rötön* for *rögtön*. *gyakrabban* is also attested in this family (hcp-1250, 1256, 1308); *gyorsabban* no longer has support (it needs o and s).
   - Fix: ledger row 26 `G Y A F A 6 A N`; literal row; uncertainty 2; print *gyakrabban* in the normalized text as an emendation with `[k]`, `[b]`; keep it marked as read from sense, but drop the {?}-style unread status.
2. **minor: row 5 is `magat`, not `maget`.**
   - Evidence: `r5b.jpg`. After g comes a two-bar sign with an accent tick (á), clearly different from the three-bar é two signs later.
   - Fix: ledger `M A G A T`, literal row, and delete *magét → magát* from the spellings list. It is a misspelling the writer did not make.
3. **minor: row 15 has one t, not two.**
   - Evidence: `r15b.jpg`. The order is m, i, one gamma, three bars with accent, F, z.
   - Fix: ledger `M I T E F Z`, literal row, and delete *mitterzek → mit érzek (t repeated)*.
4. **minor: row 7 is `monja`: `mondja` has one sign too few on the card.**
   - Evidence: `r7.jpg`. Between the o and the inverted T there is exactly one two-stroke sign; the ledger has N and D. Row 4, by contrast, does show n, d, j.
   - Fix: ledger one sign (`N`, or state n/d), literal row, add *monja → mondja* to the spellings list. Findings 3 and 4 show the ledger was filled partly from the expected word, so the solver should re-check it for the same fault.
5. **minor: three normalized forms need correcting.**
   - `Szeret[e]tt`: the card has `szeretet`; what is missing is a t, so write `Szeretet[t]`.
   - *férfiról*: the card has `ferfi|röl`, and *férfi* takes the front ending. Normalize *férfiről*.
   - *sorára*: the card has only `sora` before `rötön`, so the added syllable needs brackets (*sorá[ra]*), or *sorai[ra]*, which better suits "your lines". The current text adds it silently.
6. **minor: row 28 sign description.** `l1.jpg` shows a washed-out Y-shaped remnant, not a "shallow wave". The dot under it is the accent of *mért* in row 29, not part of the sign. *rágalmat* stays right by sense, but uncertainty 9 should describe the shape correctly and say that the shape alone does not give l.
7. **minor: row 23 sign.** `r23.jpg`: the sign read i in `belieget` has its top on a stain and no separate dot can be seen. The bottom loop favours i over y, but the call should be listed. It makes no difference to *bélyeget*.
8. **minor (suggestion, not an error): row 8.** On hcp-1216 this writer's `higgyjeel` is *higgye el*. So `jeel` may divide as `je|el` with *el nem szerez*. I have no reading to offer. The solver may note the division; the word stays unresolved.

## Status of the residuals

After fixes, the unread items are `jeel` (row 8), one surname (row 27) with the 6 4 6 marks, and a few single signs. Each is isolated and its sentence reads, so the card counts as complete under this run's rule. Findings 1 to 5 require a change to the ledger, so the command output changes; the solver must rerun it and re-paste the literal block. Findings 1 to 7 change no meaning apart from firming up "more often". A further review round is not needed if only these points change.

## What I could not verify

- The name in row 27 and the meaning of the 6 4 6 marks.
- Who Béli is; no other family card names Béli.
- A date: the postmarks show only fragments, in agreement with the solver.
- The ledger was checked at 2x outside the detail crops, so a single further extra or missing stroke in an unflagged ordinary row cannot be excluded, though 4 of my 4 corrections came from close inspection.
- The Hungarian judgment is mine; no native speaker checked it.
