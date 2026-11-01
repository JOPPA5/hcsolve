REVISE

# Review 1 of HCP1276 (reviewer: Claude Opus 5.5, 2026-11-01)

The reading stands: Jolánka key, Hungarian, cipher text coherent from row 1 to the stamp box. Four concrete errors must be fixed first. Three sign-ledger entries do not match the card, and one plain-script phrase is attached to the wrong text.

## What I verified and how

- **Solver's command** `python3 -I ciphers/hcp-1276/work/decode_opus.py`: all four SHA-256 checks OK, and the output equals the literal and normalized text in SOLUTION.md. The script only maps ledger tokens to letters, so this proves consistency, not correctness.
- **Independent decode** `review/work/indep.py` (run from the cipher directory): my own sign-by-sign transcription with sign-class names, made from my crops and compared token by token with `work/ledger-opus.txt`. 17 of 21 rows are identical. The differences are rows 9, 10 and 16 (findings 2-4) and row 11, which is only the disclosed h/p homograph.
- **Pixels**: I read the whole cipher text at 2.4x on the hi-res address scan (`review/work/b*.png`, `a*.png`). Contested spots were read at 3-4.5x (`r9`, `r10start`, `r13blot`, `r14end` with its green-channel version, `r15blots`, `r16s`, `r8e`, `vele`, `stamp`, `w1`, `plain3`). I also checked the bar counts of a/e on every row.
- **Key**: the sign classes match the `ciphers/hcp-1216/SOLUTION.md` table. Every sign has a value except the row 9 stroke and the row 14 2-shaped sign.
- **Context**: 1912-08-11 is a Sunday and the postmark reads 12 AU 11. 7 September 1912 is a Saturday, which suits a harvest ball. Recipient and signature fit the family. The language is real period Hungarian with the family's spelling habits (*akor*, *evel*). No published solution was found; the portal attaches none.

## Findings

1. **major: *Szép reményű* is part of the address, not of the message.** The word stands right of the printed divider, directly above *Tóth Jolánka* (`plain3.png`, source overview). Sister cards give the same address in clear: HCP1245, 1252, 1259 and 1261 have *Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás*, and HCP1260 explicitly assigns the word to the address. The left-hand script is complete without it: *…megkaptam, melyért fogadja köszönetemet.* The solver spliced it into that sentence in the Hungarian, English and Slovak texts, in `work/normalized-opus.txt` and in uncertainty 7, where it is called odd "in that position". The postmark cover is real, but the word reads *Szépreményű* with reasonable confidence. Fix: remove it from the message and add an address line in all languages (*Szépreményű Tóth Jolánka úrleánynak, Jászárokszállás*).

2. **major: row 10, first sign is a, not e.** `r10start.png` and `b4L.png` show two bars and no third, a clear contrast with the three-bar e signs on the same row. Ledger token `E` should be `A`, so the literal is `akorestereokvet`. This changes uncertainty 2 and the normalization: *akor* = *akkor* (the family spelling on HCP1216, 1258, 1262), so the editorial bracket *[ak]kor* and the *ekkor* option go. It also removes the letters the solver used for *-ék*, so row 9-10 is literally `menn | akor`. *Menn[ék]* then has a supplied ending, which must be marked as such. The sense improves: "if I went in the afternoon, then by evening for certain".

3. **major: row 9, the ledger has two strokes the card does not have.** Between the a of *-uta-* and the e of *menn* the card has exactly 4 strokes: one with a curled foot, then three (`r9.png`). Ledger `N | M` claims 2+1+3 = 6. *Délután* + *menn* needs 5, so the n of *délután* and the "isolated stroke" cannot both be there. The card allows `|`+m (*délutá{|}m…*, n short by one stroke) or n+n; neither gives clean *délután menn*. The reading is still the only sensible one, but it rests on word sense here. Fix: correct the ledger to the strokes present, rewrite uncertainty 2, and say that the writer ran *délután* and *menn* together or dropped a stroke. The later four strokes are uneven (tall + short + two short), so nn is a sense-based choice as well.

4. **major: row 16, the ledger has a phantom sign.** Between the wave l and the chevron v there is one sign of two bars (`vele.png`, `b6R.png`). The ledger has `L E A V`, two signs. The literal is `istenvelaviszontlatasra`, as the writer's merge of *vele a*. The E looks supplied from the family formula (HCP1216 row 22). The normalization *Isten vele, a viszontlátásra* stays, but the e is editorial and must be listed. Findings 3 and 4 contradict the ledger header ("One token = one written sign") and the statement that the key decodes "without adjustment".

5. **minor: row 14 ledger marking and description.** The blotted sign read gy is the same kind of case as `*Z` and `*X`, but it has no `*`; mark it `*GY`. Uncertainty 1 is otherwise honest and I could not improve it. The 2-shaped sign and the blot remain unidentified, so *na*, *hogy* and *kan* are all unconfirmed. "Only row 14's end group" must stay the headline caveat in the report. The group is about 9 signs but sits within one clause whose sense is carried by the rest (*de szeretném … feljönne*).

6. **minor: row 15, *az*.** The blot has a closed loop on the left, a heavy vertical and an arm rising right (`r15blots.png`, `work/crops/blots_g.png`). The crossed arm suits z, but the loop is not part of z. It may be an overwritten or struck sign, in which case the text is plain *a mulatságba* and no writer's slip is needed. Uncertainty 3 should allow this instead of asserting a slip.

7. **minor: blots not marked.** Row 11 p is overwritten with thick ink and is token `P` with no `*`. It is disclosed in uncertainty 4; align the ledger with the header convention.

8. **minor: "Why it is correct".** Update the bullet "Only row 14's end group and a single stroke have no firm reading" after findings 2-4, and drop "without adjustment".

## Checked and not disputed

Rows 1-8 and 12-13 match my reading, including *keresztlányunkat*, *összedőltek* (two strokes over o in row 6), *lemegyek*, the digit 7 and *szüreti*. Row 13's overwritten s stays a disclosed word-sense call. Row 16's s of *viszontlátásra* is a right bowl (`r16s.png`). The stamp box reads as claimed, with the third row's b rounded open like ε (word sense helps) and with the `kedves | ce` oddity honestly disclosed. The translations are otherwise faithful.

## What I could not verify

- The value of the row 14 2-shaped sign and the blotted sign, or any meaning for *na … kan*.
- Who the goddaughter was, and what the *mulatság* of rows 7-8 was.
- Whether *menn* was meant as *mennék* or something else.
- The small blotted row 15 sign under the ink, which a higher-resolution or multispectral scan might settle.
- The first letters of *Szépreményű* under the postmark, read by shape and by the sister cards.
