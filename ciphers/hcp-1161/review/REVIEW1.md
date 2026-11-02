REVISE

# Review 1 of hcp-1161 (reviewer: Claude Opus 5.5, 2026-11-02)

The decipherment stands. All 217 cipher signs agree with my own reading, and the plaintext is real, coherent Hungarian. One open word on the card is missing from the transcription, so the claim that nothing is unread is false and must be fixed before FINAL.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1161/work/decode.py` ran: 4 scan hashes OK, 217 signs (212 by table, 5 by sense), output equals the claimed plaintext.
- **Independent decode.** `review/work/verify.py` holds tokens I typed row by row from my own 4x to 6x crops of `work/hires/...adr.jpg` (`review/work/rows.py`, `open.py`, `c3.py`, `c4.py`; outputs `r*.png`, `o*.png`, `kab.png`, `ert.png`, `igy.png`, `kam.png`). It uses a key I took from the hcp-1174 table plus the four signs from hcp-1170, hcp-1179 and this card. Result: 217 signs, `diff positions []` against the solver's token list (normalising his ODD labels to what is seen). As written the key gives `oltam` with an unknown first sign, `ig`, `ú` + blot, `árzád`; all other words decode directly. Every sign on the card was viewed, not a sample.
- **Key coverage.** No sign falls outside the table apart from the two blotted ones. `1'` = á and `.1` = u are consistent everywhere (`.1` left dots clear in tudom, kábulva, elutasítanál). `-1` left dash is clear in both úgy. `1,` in kábulva: same shape as this writer's 1 with lead-in, no cross bar, confirmed. `6.` in anyám is a blotted but present dot. hcp-1173 and 1174 do have `1' 3, 9 1' 3` for Árpád, as stated.
- **Marginal marks.** The marks that fall in rows of figures are all accounted for: the ticks under Róza and írtak, and near the end of that row, are the acute accents and dots of the open row below (és, én, még). The closing line's final blob belongs to the ruled line round the date, not to the `7` of ölellek.
- **Language and context.** Period colloquial Hungarian, grammatical across every open/cipher boundary (meg + tenném, nem tudnám + elviselni). Date 1915. XII/18 Mezőkövesd reads as stated in `date.png` and agrees with the file name. Recipient and address read correctly. The picture side has no writing.
- **Published solution.** None found or attached; SOURCES.md states so.

## Findings

1. **major: an open word is omitted.** The sixth line ends after `volt` with a separate word that the plaintext does not have: card `hogy volt aba / a levélbe`, solution `hogy volt a levélbe`. See `review/work/o6b.png`: three letters a-b-a, right at the margin rule, with ink spread around the last letter. It is the colloquial `abba(n)`, "in that": "that there was in that letter". This falsifies "Everything else on the card, the open text included, is read: there is no unread word". Fix the plaintext in SOLUTION.md, the hard-coded line in `work/decode.py`, both translations (English "in that letter", Slovak "v tom liste"), and list the spelling under "Spellings as written". The cipher is untouched.

2. **minor: the low dot in kábulva is not stray: it is the i-dot of the open `mi` in the next row.** `review/work/kab.png` shows it directly above and right of the i of `mi`, which has no other dot, in the same slant as the writer's other i-dots; the é accent of `én` sits beside it at the same height. So the sign is a clean `1'`, and á needs no appeal to word sense. Uncertainty 1 can be replaced by this explanation and the count becomes 213 by table, 4 by sense.

3. **minor: wording of the two blot restorations.** In `voltam` (`r08b.png`) and the second `úgy` (`r16c.png`), the blot has a tail running lower left, like a comma. So "the dot is taken to be under the blot" claims more than can be seen: the mark may be a dot or a comma, and `v` and `gy` rest purely on word sense (`rolt`, `úg` give nothing). Both are disclosed as restorations and I accept the readings; say that the mark itself is unreadable.

4. **minor: translation drops `még`.** `és én még már két lapot írtam nekik` is "and I have even written them two cards already"; the English and the Slovak omit "even" (`ešte`/`dokonca`). Sense unchanged.

5. **minor: `.1` is not new.** "New here: `.1` = u" is out of date: hcp-1135 and hcp-1160 list `.1` too and cite hcp-1172. Credit it as confirmed here. The `így` tick is also close in form to the short tick on `2.` in `érted` (`ert.png`, `igy.png`), which the solver counts as clean; both are fine as read, and I leave this one in the sense list.

## Assessed and accepted

- `Árpád` with a clear comma on the 9 (`r24b.png`): the comma is there, so table gives `Árzád`. Writer's slip, disclosed; name secure from sister cards.
- `Márgitkám`, `aszt`, `se-mi`, `mer`, `bár mikor`, `tud nám`: read as stated. The open row breaks the word as `tud / nám` with a gap; harmless.
- Second `úgy` versus `így`: the left mark is present. Disclosed.
- `Róza`: `3, 0 9, 1.`, clean; identity unknown, disclosed.

## Could not verify

- The postmark, beyond a 5 (same as the solver).
- Whether the HistoCrypt article discusses this card; I did not open it.
- Who wrote the date line at the foot. The hand is smaller and it may be a later note.
- The meaning of `azt` ("that") in `én azt bár mikor megtenném`; the card alone does not say what he would do.

## For the solver

After finding 1 is fixed the card has no unread word and can go to FINAL without another round, since the cipher reading does not change.
