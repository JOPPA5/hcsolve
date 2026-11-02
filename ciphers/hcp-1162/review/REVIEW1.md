REVISE

# Review 1 of hcp-1162 (Claude Opus 5.5, reviewer, 2026-11-02)

The reading stands: whole-card digit cipher, Hungarian, Árpád to Margitka Sziber, with no unread word. One sign is wrong in the transcription, which changes one plaintext letter and removes a claimed misspelling. The handling of the last lines needs small fixes. I tried to refute the text and could not. Every line reads, and I found no forced word.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1162/work/decode.py` passes: hashes OK, 388 signs, 31 distinct, 1 by sense. Its first output line agrees with the plaintext letter for letter, except that the comparison strips spaces, so it hides `ölelés` against `ölel és` (finding 2).
- **Independent decoder.** `review/work/decode_review.py` has its own key table and keeps the card's line breaks: `python3 -I decode_review.py ../../work/transcription.txt`. Same text. All 31 signs in the transcription are in the key, and no key sign is unused. The sign counts match the solver's. The `8{t}` sign gives `mölt-` under the table, as disclosed.
- **Key.** It agrees with hcp-1174 and with the notes in hcp-1179 (`1,` b, `:1` ü, `1'` á, 4 probably f). The whole table is regular: 2 to 9 plain are c d f h j k m p; comma gives cs r g l n s t z; dot gives é v gy ly ny sz. That regularity is good evidence for the signs that occur only once or twice (`2`, `5.`, `6.`, `:1`). hcp-1179 lets `5.` act as l, but `olyan` here needs ly, as the solver says. One occurrence only.
- **Pixels.** I read all 22 lines sign by sign on my own 2x strips of the hires scan (`review/work/crops/L0-6, R0-6`, tool `crop.py`) and 3 to 4x zooms (`tolt`, `ertunk`, `utan`, `compare`, `kedv`, `oleles`, `l19end`, `date`). Apart from findings 1 and 2, every sign agrees with `work/transcription.txt`, including the dot positions of all `1.` / `1'` / `1:` and the left dots of `.1` and `:1`.
- **The sense calls.**
  - `tölthettem`: first sign is a clean 8 with no comma (`tolt.png`). Agreed, a slip of the writer's for `8,`; nothing else makes a word. The next sign has its stroke starting at the bowl, so it looks like 9, but the long stroke matches his commas. Agreed.
  - `értünk`: the comma of `3,` runs out of the lower curve (`ertunk.png`). Agreed.
  - `filért`: `5,` with tilde and closed loop. Agreed.
  - `és` under the red figures: the `2.` and `7,` show through. Agreed.
- **Language and content.** Real Hungarian of the period and a coherent story. The carter's 2 crowns against 1 crown 60 fillér is right for the currency. The English and Slovak translations match. Uncertainties on `édesanyám`, `pokol`, the destination and the month are disclosed.
- **Published solution.** The portal page capture shows no attachment; the solver says the linked article was not checked. Disclosed.

## Findings

1. **Major: `utan` is `után`; the sign is misread.** Line 19, the a of the word after `az`. The solver has `1.`; the card has `1'`. On `review/work/crops/compare.png` the dot of `1. 9,` (az) sits at the foot of the stroke, and the dot before the `6,` of this word sits in the upper third, beside the top of the 1, the same place as the a-acute of `koronát` and `három`. So the sign decodes to á and the word is normal `után`. The solver's `az utan [= után]`, and its listing among forms "as written", wrongly gives the writer a misspelling. Sister cards spell `után` normally.
   Fix: line 19 of `work/transcription.txt` to `.1 8, 1' 6,`; the plaintext and `PT` in `decode.py` to `után`; drop `[= után]` and the mention in Uncertainties; update counts (`1.` 32, `1'` 14; total unchanged).

2. **Minor: three hyphens in the transcription are not on the card, and one word break comes out wrong.**
   - Line 19 ends in `7,` with no stroke after it (`l19end.png`; the line below it is the ruling of finding 3).
   - Line 20 ends in `5,` with its tilde only (`oleles.png`).
   - The stroke after `1:` on line 21 is the foot of the address bracket `(` of `(Borsodm.)` running in from above, not a pen stroke of the message (`kedv.png`).
   
   `édesanyám` and `kedvesed` still join across the line breaks by sense. Because of the invented hyphen on line 20, `decode.py` prints `ölelés csokol` while the claimed text has `ölel és csókol`, and the normaliser hides the disagreement. Remove the three hyphens, make the script join those two words explicitly, and compare with spaces where the card spaces.

3. **Minor: a ruling on the card is not disclosed.** A long pen line runs under most of line 19, turns down in a hook before `számtalanszor` on line 20, and continues left under `anyám` with a second stroke there (`L5.png`, `L6.png`). It sets off the closing from the body. SOLUTION.md does not mention it, although it says the layout is editorial. Add one line under Uncertainties or the plaintext note.

4. **Minor: the sense count is narrower than the text behind it.** "Only one sign out of table" is true by the script's rule, but item 2 of Uncertainties already concedes that some `0,` are called by sense. The list is also short: the comma of `többet` is close to the bowl too. Say that the 1 is a count of signs off the table, and that a few signs on the table rest partly on word sense.

## Could not verify

- The month. The overwritten blot on the date line fits `III` but does not prove it (`date.png`). The postmark dateline is mostly under the stamp. A letter that may be R and an 8 show on it; that is weakly consistent with March and not enough to confirm it. `1916` and `28` read.
- Whose mother `édesanyám` is, what `pokol` refers to, and where they travelled to. The card does not settle these.
- Whether the linked HistoCrypt article discusses this card. I did not check it.
- The red figures (`3613.`, and `0.` further right). Their meaning is unknown; they are not part of the message.
