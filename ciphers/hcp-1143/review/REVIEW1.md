REVISE

# Review 1 of hcp-1143 (reviewer: Claude Opus 5.5, 2026-11-02)

The decipherment stands: the key, the cipher type and the sense of the whole card are right. Two words are mistranscribed, and in both the pixels give normal Hungarian where SOLUTION.md reports a writer's oddity. One word is rated weakest for a reason I think is wrong. The fixes are small but they change the plaintext and retract claims, so this is REVISE.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1143/work/decode.py`: hashes ok, all word assertions pass, 579 table signs + 7 by sense, 586 in all. Its output matches the claimed plaintext, apart from the spacing of `le értem`, `paraszt boltba`, `tavasz kor`, which the claimed text joins.
- Wrote `review/work/indep.py`, my own table typed from the grid and my own parser, which does not fill in the `{sign|x}` readings. It gives the same text, with the 7 flagged signs showing as `[i]zt`, `ellátá[k]`, `sir[a][?]`, `lil[f]om`, `margi[?]ká[?]`. Every other sign decodes by the table, so the key covers the whole ciphertext. Its 7 exceptions are exactly the 7 the solver declares.
- Read the whole card against the transcription, row by row, on the solver's 4x crops of the hires files (a1L to a5R, aR1, aR2, pr1 to pr7), and made my own enlargements in `review/work/`: `alk.png`, `alk2.png`, `lanyka.png`, `sirig.png`, `liliom.png`, `szer.png`, `ezt.png`, `nem.png`, plus full views `adr.png`, `pic.png`. Apart from findings 1 to 3, I agree with every sign.
- All 7 flagged signs and all the "read with a note" items were checked on the pixels. Blots in `Margitkám`: real, comma of the t shows, restoration correctly labelled. `ezt`: a clean plain `1`, the pale wash lies left of and over the stem, and the paper right of the stem has no dots, so "read by sense" is honest. `ellátás`: no comma on the last 7, as disclosed. `nem` (A16): filled loop, but the top is one continuous stroke with no detached flag, unlike every `5` on the card, so `6,` is right. `.1` in `után`: one dot, left of the stem. `5.` in `oly`: the dot is real in both places. `szeretettből`: all commas seen on `szer.png`.
- `1,` = b is not listed as new, and rightly: it is on hcp-1179 and other sister cards.
- Date: 4 May 1916 was a Thursday (computed), so the Tuesday/Wednesday remark holds as stated inference.
- Language: real Hungarian of the period throughout; the letter has a coherent practical content, the poem has stanzas and rhyme, and name, recipient and place fit the family. No published solution appears to have been used; the portal attaches none.

## Findings

1. **`alkalmazesba` is a misreading of `alkalmazásba` (major).** A7, the second-to-last sign of the word, is transcribed `1:`, but it has one high dot and no lower dot. See `review/work/alk.png` and `alk2.png`: the paper right of the foot of the stem is clean, while every true `1:` on the row above and below shows a clear lower dot. The sign is `1'` = á. SOLUTION.md's statement "`alkalmazesba` (`1:` not `1'`)" is false and must go. Fix the transcription row, the plaintext, and the `[= alkalmazásban]` note; the -ba remark stays.

2. **`lenyka` is a misreading of `lányka` (major).** Stanza 3, the second sign of the word, is transcribed `1:`, but it again has only the high dot, with nothing under it (`review/work/lanyka.png`, also visible on the solver's pr6). The row is `5, 1' 6. 7 1.` = lányka, a normal word for "girl", which also occurs on sister card hcp-1151 by that solver's report. So the signs need no `[= leányka]`, and "this is the card's oddest form" and "has no sign for á" are wrong. Also change the rhyme claim to lányka/boldogsága. The translations do not change.

3. **`sírig` is not the weakest word; the "dot" and the "dot and comma" are very likely stem feet (minor).** On `review/work/sirig.png` the upper strokes are pale and the feet dark, as on the neighbouring `3.` and across the poem where the pen ran dry on the printed sheet. The dark spot under the `1` lies on the line of its stem, and the one under the `4` likewise, so they read as the lower ends of the stems, not as marks. The `4`'s comma is separate and real. So the signs are most likely plain `1` and `4,`, and the table gives `sírig` directly. Re-examine this and, if you agree, change `{1.|i} {4.,|g}` to `1 4,`, which gives 581 table signs and 5 by sense, and rewrite uncertainty 4. If you keep it as is, say why the spots are marks.

4. **The "why correct" section needs to follow the fixes (minor).** "One fixed table gives 579 of 586" and "no forced word" are fine in substance, but the counts change if finding 3 is taken. The list of writer's forms loses two entries.

5. **`5.` wording (minor).** The note says "This card alone cannot decide". It can be firmer about the family: hcp-1142, 1151, 1153 and 1162 list `5.` = ly and hcp-1149, 1178, 1179 list it as an l variant, so the note should cite that split, and the key cell can stay ly here.

6. **Translation slips (minor).** Slovak "iná adresa netreba" is ungrammatical: use "inú adresu netreba" or "iná adresa nie je potrebná". English "as this flower is white, so fair is your soul" adds a comparison that `s szép a lelked neked` does not have ("and your soul is fair"); the same holds for the Slovak "taká krásna". Both are small.

7. **The command does not print the clear text (minor).** `decode.py` prints only the enciphered parts, not the address or dateline, and SOLUTION.md does not state this. Add one line saying so.

## What I could not verify

- The HistoCrypt article linked by the portal was not checked by me either; the solver discloses this.
- `liliom`, third letter: the Y-shaped sign is neither a clean `1` nor a clean `4` (`review/work/liliom.png`). The solver's disclosure is fair; the word is safe by sense.
- `ezt`: I cannot exclude that the pale wash hid part of something, but no dots show where the dots of `1:` would stand.
- What the two ink blots in the salutation cover; they are restorations only.
- The postmark date was not read; the stamp cancel is too faint for me to use.
- Whether `parasztbolt` was a usual term; "peasant shop" is a plausible but literal rendering.
