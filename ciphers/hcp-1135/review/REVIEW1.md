ACCEPT

# Review 1 of hcp-1135 (Claude Opus 5.5, 2026-11-02)

The reading stands. I found no wrong word and no forced passage. All findings are minor, and none changes the plaintext. Nothing on the card is left unread, so the card counts as complete, not partial.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1135/work/decode.py` ran clean: 4 scan hashes OK, every line asserted, 301 signs (296 by table, 5 by sense), Easter 1916 = 23 April. Its output matches the plaintext in SOLUTION.md.
- **Decoder limits.** It is not a blind check. The `~` readings and the ny/j choice for `6.` come from the transcription and the reading list. See finding 1.
- **Own decoder.** `review/work/decode_review.py` has its own key table, written from hcp-1174/1178/1179. It has no `~` overrides and no `6.`=j, and drops clear letters. It decodes all 301 signs with no unkeyed sign. The raw output differs from the claim only where disclosed: `i leg` twice, `csul` (no ü), `lányki` (my strict token), `üdvözol`, `ánynyá`.
- **How independent the sign list is.** `review/work/cmp.py` shows 301 = 301 with no token differences from the solver's transcription. I typed that list with the solver's transcription in view and then confirmed it against the pixels, so it is a check of his list, not a blind second transcription.
- **Pixels.** Every row of `work/hires/*_adr.jpg` was checked at 1.2-2x (`review/work/crops/r*.png`, `b1-b3.png`, `over.png`). Every disputed sign was checked at 3-6x: `becsul`, `lanyk`, `lk2`, `szer`, `sz7`, `hely`, `zarva`, `udv`, `fog`, `endl`, `es`, `kedv`, `hus1`, `stamp`.
- **Disclosed points, judged on the pixels.**
  - `a` before `leg`, twice: plain 1, no dot. Solver is right; sense only.
  - Becsül: one low blot left of the 1, so literally `.1`. The left flag of that 1 is unusually heavy, with a downward lobe where the upper dot of `:1` would sit, so a merged dot is likely. Disclosed; I agree.
  - üdvözöl: the long stroke under the second 0 starts from the 9 and is the comma of `9,`. Solver's description is correct.
  - hozzád: the closed bottom is real, and the detached top bar is the 5-form of this hand. Agreed.
  - zárva: the blot covers the dot of `3.`. Agreed.
  - bájjá: `6.` twice is clear. Agreed.
- **Language and context.** The Hungarian is good period language with normal spellings (ünepeket, leg boldogabb, küld, helette). The verse is sensible and parallel (testté / bájjá), with rhymes virág / imád and lelkem / lelked. I checked the Hungarian against both translations and they are faithful.
- **Key coverage.** 29 distinct signs cover all 301. `1,` = b is family (hcp-1179 `legszeb`).
- **Date and picture.** 22 April 1916 is Holy Saturday; the computus is correct. The picture side is an Easter couple with eggs and catkins. The address reads as stated: Őnsg. / Szépreményű / Sziber Margitka / Kisasszonynak / Szomolya / u. p. (Bogács).
- **Postmark.** MEZŐ... with 22 visible (`stamp.png`). Month and year are not legible, as the solver says.
- **Sender.** Salutation and signature `1' 3, 9 1' 3` match hcp-1174.

## Findings

All are minor. They are worth fixing in the record but need no re-review.

1. **minor: the correctness argument overstates.** SOLUTION says the four new signs are "each confirmed in more than one word" and that the decode has "no free choices".
   - `.1` = u rests on one word, húsvét (twice), plus the unresolved Becsül blot.
   - `6.` = j rests on bájjá alone.
   - `decode.py` chooses ny or j for `6.` by looking at the expected reading, so that choice is not free of the reading. It is disclosed under "Other points", but the closing claim should be narrowed.
2. **minor: one undisclosed reading by sense.** In `szerelemmel` (`review/work/crops/sz7.png`) the first sign is transcribed `7.`, but there is no detached dot under it, unlike the other `7.` signs on the card. The crossbar's right end curls down into a blob. That is probably the dot tied in by the pen, since a hooked bar with no blob occurs on `7,` in `és` (`es.png`). Literally it could be `7` (kerelemmel) or a hooked `7,` (serelemmel). Sense fixes sz. It should be listed, or marked `~`, making the count 295 + 6.
3. **minor: a mark at line ends not reported.** After the clear `l` of szerelemmel and the `g` of virág stands a comma-shaped tick (`endl.png`, `b3.png`). It is either punctuation or the comma of the sign. If it is the comma, the l is a badly formed `5,` (same value) and the g a `4,`, which supports the solver's note on g. It changes no letter, but the note on these two letters should mention it.
4. **minor: punctuation is editorial.** SOLUTION says "Spelling as on the card", but the commas in the prose and verse (after szívből, húsvét, tündérrege, Becsül, szeret and others) are not on the card, where commas belong to signs. Only `!`, `)`, the brackets around Árpád, the final point after lelked and the date are written. State that the punctuation is added.
5. **minor: `5.` is labelled "l (in helette; ly-sound)".** The family has `5.` as plain l (legszeb, csókollak, hcp-1178/1179), so the note implies a distinction the family evidence does not support. This card has a single instance. Call it l, with a remark that the position happens to be ly.
6. **minor, in the solver's favour: lánykám is stronger than stated.** The dot sits about a quarter of the way down the stem, the same as the `1'` of hozzád and of the first á in this word (`lk2.png`, `lanyk.png`), and is not "between" the two heights. There is no low dot; the entry stroke of the m is a thin hairline at that place. It can stand as a table reading `1'`, or stay by sense if the solver prefers caution.

## Could not verify

- The HistoCrypt article linked on the portal: I did not check it, and neither did the solver. I therefore cannot exclude that it discusses this card. The solver discloses this.
- Whether the verse is printed or original.
- Whether the first word of the aside (`az igaz`) is the true start of the bracket; no opening bracket is on the card.
- The year and month of the postmark.
- Blindness of my transcription, as stated above.
