REVISE

# Review 1 of hcp-1150 (reviewer: Claude Opus 5.5, 2026-11-02)

The decipherment stands: one digit-plus-mark key turns the whole card into coherent Hungarian. Concrete fixes are needed: one word is wrong (`várva` should be `zárva`), one name is probably wrong (`[B]erzon`), one listed uncertainty is false (`leszek`), and the translations need changes.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1150/work/decode.py`. Hashes OK, 420 signs, "413 by the table, 7 against it", and the output is identical to the plaintext in SOLUTION.md.
- Wrote `review/work/decode_review.py`: my own row-by-row sign stream, with the key taken from the hcp-1135 and hcp-1174 tables, not from the solver's script. It diffs the stream against the solver's tokens. 420 signs, none outside the table. It differs from the solver at only the 8 signs discussed below, and the output runs as continuous Hungarian. Limit: this was not a blind reading. I read the crops with the solver's text available, so it shows agreement, not independent discovery.
- Read the whole address side from the hires scan at 2x (`review/work/crop.py`, left panel, then the right panel for the rows that cross the divider), and at 3x to 7x for the doubtful signs (`z_*.png`; `mask.py` removes postmark ink). Rows 7 and 8 were traced to the end under the stamp ring: `hadi` ends there as `1. 3 1`.
- Key coverage: every sign falls in the table. The new values `4`, `4.`, `6`, `6.` are each repeated in several unrelated words.
- Language: real period Hungarian. The single-consonant spellings `inet`, `fényeségre` match this writer's habit on sister cards (`ünepeket`, `kapot`, `adig`).
- Context: 12 June 1916 was a Monday (computed) and Pentecost 1916 was 11 June (Easter 23 April + 49 days), so `Az ünnepek` and `hétfőn` fit. The KISTERENYE postmark fits the open place name. `nefelejcs` fits the forget-me-nots on the picture side.
- Published solution: the card is Not solved on the portal with nothing attached, and I saw no sign of an undisclosed source.

## Findings

1. **major: `várva` is wrong; the word is `zárva`.** SOLUTION calls this "the weakest point" and reads `0~v`. In `review/work/z_zv.png` (also `z_varva.png`) the sign is a loop with a tail running down-left, plus a separate parallel comma to its right. That is `9,` = z by the table. The stem rising from the loop through the pencil rule is not part of it; it runs up to the row above. The `0` reading missed both tail and comma. `Soraimat zárva` ("closing my lines") is this writer's closing formula: hcp-1135 `Soraimat zárva`, hcp-1167 `Soraimat bezárva`, hcp-1164 `Zárva soraimat` (those three are not FINAL, so they are support; the pixels carry the reading). This also removes the solver's puzzle of `my lines` versus expected `soraidat`, and I confirm the sign is 8 (`z_m.png`). Fix: token `9,`, plaintext, English "Closing my lines, ... embraces", Slovak "Zakončujúc svoje riadky ..." (the Slovak "Čakajúc na moje riadky" also has the wrong sense), and remove the uncertainty entries.

2. **major: `[B]erzon` should probably be `Gerzon` (Gerzson, a Hungarian given name).** In `z_g.png` the sign is only touched by the ring and is well visible, not hidden as SOLUTION implies. The bar meets the main stroke at mid-height and crosses it, with a short upstroke at its left end, the open form of `4`, and the comma ends in a hook like the `4,` of `Drága` in row 1. `4,` gives g. Limit: the curled `1.` of `Soraimat` (finding 5) has a similar form, so `1,` cannot be fully excluded. Nothing outside the card confirms either name, and `zs` written with `9,` z is itself an inference. Fix: print `Gerzon` with the reading flagged, give `Berzon` as the alternative, and correct the claim that the comma suggests `1,` (a comma does not separate the two).

3. **major: `hat hadi szabadságra` is translated as nonsense.** "on six military leave" and "na šesť vojenskej dovolenky" are not meaningful. Signs `5 1. 8,` are clear, but `1.` also stands for unmarked á on this card (`számtalanszor`). `hát hadi szabadságra` ("so he came home on military leave") is grammatical and needs no missing unit. Fix: prefer `hát` in the text and translations, with `hat` plus a missing unit as the alternative, and say that the choice rests on sense.

4. **minor: uncertainty 4 (`leszek`) is false.** SOLUTION says the 5 shows no comma. `review/work/z_l.png` shows the comma clearly below the 5, crossed by the postmark ring. The sign is `5,` by the table. Fix: token `5,`, delete entry 4.

5. **minor: an unlisted sense reading.** In `Soraimat` the second a has the shape of `4.` (`z_m.png`). NOTES calls it a curled `1.`, but decode.py counts it as by-the-table and SOLUTION does not mention it. The reading is right (`gy` gives nothing), but it must be listed as read by sense. Update the sign count after findings 1, 4 and 5; the count of signs against the table changes from 7.

6. **minor: overclaims in "Why I believe it is correct".** `fényeségre / nézve` is listed as a rhyme, but it is only assonance, and the second stanza rhymes in lines 2 and 4 alone. `várva` is no longer an exception once finding 1 is applied. `4` "suggested by hcp-1175" points to a card with no SOLUTION.md. I could not find `1,` stated on hcp-1179 by a quick search, though it is in hcp-1135.

7. **minor: `Ez a virág tolmácsolom lányka` is under-translated.** The rendering drops the difficulty. It can stand as a parenthesis, "this flower, I interpret it, girl: do not forget me". Give this or say that the syntax is unresolved. Keep the plaintext as written.

8. **minor: date.** After `VI/` a further `1` and a round digit are visible at the stamp edge (`z_day.png`), so "not read" undersells it, though I cannot fix the digit. The day-of-week can be stated as computed: 12 June 1916 was a Monday, Whit Monday itself. So `hétfőn` is not necessarily "the Monday night after".

## What I could not verify

- `nagyon`: whether the first 6 has a comma. The head of the sign below may hide it, and I kept the sense reading `6,` in my stream. `Az`, `ünnepek`, `szabadságra` and `Egyéb`: as disclosed by the solver; my stream normalises them and they rest on word sense.
- The postmark date in full. It appears to be 916, JUN, 12, but is not cleanly legible, and the same applies to the day on the card.
- The source of the verses, the HistoCrypt article, and who Gerzon was.

After the fixes the card has no unread clause, so a register entry (type MASC) would be in order. The changes are bounded word-level corrections, so they do not by themselves call for another full round.
