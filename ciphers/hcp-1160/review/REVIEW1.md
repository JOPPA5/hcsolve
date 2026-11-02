REVISE

# Review 1 of hcp-1160

Reviewer: Claude Opus 5.5, 2026-11-02. The solution as a reading stands: this is the real message, in the family key, and I could not refute it. Two signs are misread, though. One of them produces a misspelling the writer did not make and hides a key sign. Both should be fixed before FINAL.

## What I verified and how

- Solver command: `python3 -I ciphers/hcp-1160/work/decode.py` ran. Hashes OK, 351 signs, and the output equals the rows in `SOLUTION.md`. The asserts compare against strings typed in the same script, so they prove only self-consistency.
- Own crops: `review/work/crop.py` from `work/hires/`. All rows at about 2.2x (`r1`–`r6`, `v`), doubtful signs at 3–6x (`z_*.png`). I read every row sign by sign on these crops.
- Independent decode: `python3 -I ciphers/hcp-1160/review/work/decode_review.py`. Ciphertext retyped by card row from my own crops, key rebuilt separately. It gives 351 signs and differs from the solver in exactly two signs (findings 1 and 2), plus the three `~` tokens, where I record `:1`, `.1` and `6?`.
- Key coverage: every sign decodes; no leftover or unused value. Values agree with hcp-1174, 1178, 1179, 1170, 1172.
- Language: real period Hungarian with this writer's habits (`rosz`, `üdő`, `aszt`-type `pénszt`). The verse is genuine: I counted 8/7 syllables alternating over all eight lines, and the rhymes `szirom`/`sírom`, `hattyúdalom`/`mondhatom` hold. No sense-forcing found.
- Content: `A lapodat megkaptam, mely-nek ... megörültem` is the same formula as hcp-1151 and 1142. The open foot note `ha esetleg rosz üdő lenne és nem mehetnék` repeats the enciphered sentence. Addressee, `Sz. A.`, photographer matter fit the family.
- Open text and address read as stated. `1915. XI/11.`: X, I, then a long slash under an overline (`date.png`); not X alone. The picture side has no writing (`ov_pic`).
- Doubtful points confirmed on pixels:
  - `hattyú`: two separate dots, one after the 8 and one left of the 1 (`z_hatty.png`). `8.` `.1` is right.
  - `fiúval`: the dot sits left of the second stem at mid-low height, the same placing as `.1` in `hullok` (`z_fiu.png`, `z_hull.png`).
  - `pusztán`: one dot only (`z_pusz.png`).
  - `rózsáról`: `9.` then high-dot `1'` (`z_rozs.png`).
  - `pénszt`: dot on the 7; the grey line under it is graphite, not violet (`z_pensz.png`).
  - `külgyél`: two dots left of the 1, nearly touching (`z_kul.png`).
  - `készevan`: `7 2. 7. 1: 3. 1. 6,` exactly (`z_kesz.png`).
  - `feviszem`: no l sign (`z_fevi.png`).
- Published solution: no sign of one used. The portal attaches none. The solver disclosed that the HistoCrypt article was not checked.

## Findings

1. **`melnek` is a misread; the sign is `5.` = ly, and the word is `melynek` (major).** Last sign of the second message row (`review/work/z_mel.png`): the mark after the 5 is a round blot on the ruled margin line, with no tail. Every comma on this card has a head and a long tail down-left, and the area down-left of this mark is clean paper. `5.` = ly stands on the sister cards in this same word: hcp-1151 `Lapodat megkaptam, melynek`, and hcp-1142 `amelynek` (its key table, row `5.`). So:
   - the transcription, `READ`, the plaintext and the "Normal spellings" list must change;
   - uncertainty 8 ("no y; the writer has `5,` for ly") is wrong and should go;
   - the key table lacks `5.` = ly;
   - the "regular pattern" note should include l/ly, which this card's sign supports.
2. **`kivaltom` is a misread; the sign is `1'` = á (major).** On `review/work/z_kiv.png` the dot after that 1 stands at about 0.41 of the stem height from the top, level with the head of the following 5. The dot of `1.` in the same pencil sits at about 0.85 (`z_maj.png`, `z_kesz.png`). The high dot of `1'` in `rózsáról` is at about 0.30 (`z_rozs.png`). The cipher therefore has plain `kiváltom`. Uncertainty 6 ("the sign is `1.`, not `1'` ... a slip or omission") states as fact a scribal error that is not there. Fix `work/transcription.txt`, `READ` and uncertainty 6.
3. **"New in the family" is out of date (minor).** `8.` = ty is already on hcp-1142, 1146, 1147, 1151, 1164 and 1166 (`kártya`). `9.` = zs is on hcp-1137 and 1164. `5.` = ly is on hcp-1142, 1151 and 1164. Most of those cards are still in review, so they are not final proof, but "new" is wrong and the missed `5.` shows the cost. Cite them as agreeing sister cards. The `kartyim` remark on hcp-1179 is then not this card's own observation either.
4. **Counts and the sense-only list (minor).**
   - "34 distinct" counts the three `~` tokens as separate signs. After findings 1 and 2 the card has 32 real signs. The table has 31 and needs `5.`.
   - `fiúval` is not a sense call: the dot placing is the ordinary `.1`. Its alternative is also misdescribed: `1.` `1` gives `faival`, not `fiaiv-`.
   - `üdő`: a bump on the left of the stem sits where the upper dot of `:1` falls on `z_mego.png`, so the second dot is likely (`z_udo.png`). Your caution there is fair.
   - `könnyet`: the blot has the exact head-and-tail outline of the comma beside it (`z_konny.png`). The literal reading leans to `6,`, `könnet`. Keep the disclosure and say this. Finding 1 removes the `melnek` parallel for a dropped y, so `könnyet` remains a word-sense restoration.
5. **`kész e van` (minor).** The signs are `készevan`, and the printed spacing suggests a parsing the text does not support. Print `készevan` with the note that the sense is `készen van`, n omitted, or mark the n as a restoration. The translation "is ready" rests on that sense. This is disclosed already, so only the printed form needs care. Single word, rest reads, so it does not make the card partial.
6. **Cancelled word (minor, optional).** On `z_canc.png` and `z_canc2.png` the first two signs are `1. 5,` and the fourth is `3.`, as the solver says. The third looks like a stem with two marks right of it, which would be `1:` rather than the `1.` behind the solver's `a lav...`. That hints at `a lev...`, but I would not print it. Writer's cancellation, not part of the message.

## What I could not verify

- The verse source. I did not search it; the solver disclosed this too.
- The postmark date. KÖVES is readable on the ring; the date row is partly legible and I cannot fix month or day (`pm180.png`, `pm_date.png`). The date stands on the writer's own `XI/11`.
- The HistoCrypt article, not consulted.
- Sister cards cited in finding 3 that have no FINAL yet are unreviewed evidence.
