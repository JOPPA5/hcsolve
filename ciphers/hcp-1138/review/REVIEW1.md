REVISE

# Review 1 of hcp-1138 (reviewer: Claude Opus 5.5, 2026-11-02)

The key and most of the reading stand. The transcription does not: the solver's working image was cut at a crop boundary, which was taken for the card edge, so 12 signs at the ends of rows 9, 10 and 11 were never read. These signs give `házat`, `többet nem` and `ott a kapuba`. The one "unread word" (`oba`) and the claim "there is no `nem` on the card" are both products of that crop. One word in row 9 and one in row 14 are also misread. Everything found here is fixable by the solver from the pixels, and the sense of one clause reverses, so after the fixes the card needs `DONE2` under README step 5, not `FINAL`.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1138/work/decode.py`: all 4 hashes OK, 397 signs, 82 words, no mismatch. The printed reading agrees with the plaintext in SOLUTION.md. The script only proves that the transcription and the reading agree with each other. The bracketed text at the end is hard-coded (finding 8).
- Made my own rotations of `work/hires/..._adr.jpg` at full card width (`review/work/rot2.py`, `crops/rot51w.png`) and read all rows from enlarged crops, 1.7x to 4x (`review/work/crops/`). I had already seen the solver's transcription, so this was not a blind reading, except at the row ends, where the solver has nothing.
- Wrote `review/work/own_decode.py`, 18 rows, 409 signs, own table, no asserted reading. Output:

      édes margitkám
      értesitlek hogy má
      jusba fognak sorozni
      de csak azokat akik még
      nem voltak sor alatt tehát
      most már nyugott lehec édes de most
      már ne szedjétek le a hernyot hagyjatok
      ugy mindent aztán ugy volna jo kevesem
      ha már mostanába lejönne ángyika házat
      nézni hogy akkor ra lenne de most többet nem
      irok mert rosszul vagyok ugy veszem észre ott a kapu
      ba alaposan megfáztam
      kártyámon e kis virág
      tolmácsolja érzelmem
      minden orád a távolban jol teljen
      most üdvözöl és számtalanszor csokol
      szeretö kedvesed
      árpád

- `review/work/cmp.py` aligns my signs with `work/transcription.txt`. There are exactly five differences, findings 1 to 5 below; the remaining 392 solver signs agree with mine.
- Picture side: printed roses, C. Klein signature, no writing.
- Open text and address read as stated. Postmark shows `MEZŐ...` and a 17, partly under the stamp, which agrees with the date; the solver does not mention it.
- Key against `hcp-1174`: table agrees for all shared signs. No published solution used; portal has none attached; the HistoCrypt article was not checked, and this is disclosed.

## Findings

1. **blocker. Row 11 is truncated; `oba` is not a word on the card.** After `2. 7. 3, 1:` (észre) the row continues: `0 8, 8, 1. 7 1. 9 .1` followed by a line-end dash, then row 12 `1, 1.`. This is `ott a kapu-ba`: "there at the gate". The commas under both 8s are clear (`crops/f1.png`, `crops/f3.png`), the dot on the 1 after the 7 is low (a, not á), and `.1` has its dot to the left. The dash marks that the word runs on to the next row. SOLUTION Uncertainty 1 says "the 0 ends a row at the card edge". That is false: the card runs on for about 300 px at full scale. Cause: `work/crops/rot48.png` is 2634x2592, which is what a crop of about 1600x2100 gives at 48 degrees, and it ends in a straight diagonal at the crop edge (`review/work/crops/solver_rot48_view.png`). `strips.py` and all crops inherit it. `{oba}`, the dead end in NOTES.md, and the English and Slovak "{oba}" all go.

2. **blocker. Row 10 is truncated; "There is no `nem` on the card" is false.** After `8, 0, 1, 1, 1:` the row continues `8, 6, 1: 8` and a line-end dash: `többet nem`. Clause: `de most többet nem írok mert rosszul vagyok`, "but now I will not write more, because I am unwell". The solver's `de most többe írok` / "I write more(?)" says the reverse. Uncertainty 4 goes. Evidence: `crops/f1.png`, `crops/f3.png`.

3. **major. Row 9 is truncated and misread: `házi` is `házat`.** The last sign is not a 1 touching the edge: it is `1.` with a clear low dot, followed by `8,` (`crops/f1.png`, `crops/f4.png`). `5 1' 9 1. 8,` = házat, with the plain 9 still read z by sense. Clause: `ángyika házat nézni`, "to look at a house". Uncertainty 3's speculation about `házi` and a lost mark goes, and item 2's example `házi` needs changing. `hogy akkor rá lenne` stays tentative.

4. **major. `hejönne` is `lejönne`.** The 5 has a full comma directly under it (`crops/g2.png`, at 4x; same offset as the comma on the 5 of `lenne` in the next row). So `5, 1: 6 0, 6, 6, 1:` = `lejönne`, "would come down". `hejönne` is not a Hungarian word and the solver neither flagged it nor listed it; the translations silently render it as "came here". hcp-1174 likewise speaks of going up (`felmegyek`) between the two places. The stated reading "continuous Hungarian" was carried over a non-word here.

5. **major. `tolmácsolna` is `tolmácsolja`.** The 6 in row 14 has no comma (`crops/g1.png`, 3x). The stroke at its upper right is the comma of the final `6,` of `kártámon` in the row above, and the sign below it is `1.`. So `6 1.` = ja, this card's own `6` = j. Clause: `e kis virág tolmácsolja érzelmem`, "this little flower interprets my feelings", which is also the expected definite form with an object. The translations must change from conditional to present.

6. **major. `8.` should be ty, not a variant t.** The card's other dotted forms are digraphs of the comma letter: `4,` g and `4.` gy, `6,` n and `6.` ny, `7,` s and `7.` sz. `8,` t and `8.` ty complete that pattern, so `7 1' 3, 8. 1' 8 0 6,` = `kártyámon`, correct spelling, no slip. The table entry "t (once, as on hcp-1179)", the "kártámon = kártyámon" note and Uncertainty 9 should be replaced; it is the only attestation on this card, so say it rests on one word plus the pattern. It may also help the open `kartim` on hcp-1179 (`8.` there), which is for that card's owner, not this one.

7. **minor. `üdvözölés` is two words: `üdvözöl és`.** There is a wide gap between `5,` and `2.` on the card (`crops/h4.png`). The sentence is `Most üdvözöl és számtalanszor csókol szerető kedvesed (Árpád)`: "Now your loving sweetheart greets you and kisses you countless times". SOLUTION invents `üdvözlés` and "with a greeting". No sign changes, only the division, the note on odd forms and both translations.

8. **minor. The command does not produce the plaintext.** Everything under "Reading with the card's breaks" is a hard-coded string, including `rá`, `ke(d)vesem`, `{oba}` and the capitals. Print it from the decoded rows, or say that it is hard-coded. A sign count of 409 should result (397 + 12).

9. **minor. Line-end dashes not reported.** Rows 7, 10 and 11 end in a short rule, which the solver does not mention, and the row-2 blot has the same shape, drawn heavily: a thick stroke running right from `8 1'` (`crops/a2.png`). It is more likely this dash than a "cancelled start", since `má-jusba` breaks there. Uncertainty 5 should say so as a likely reading. Rows 9 and 10 then show that the writer used the dash loosely, since `nem` is complete at its dash.

10. **minor. Consequential text changes.** "Why I believe it is correct" must drop `oba` and the claim of 397 signs in 82 words. The "Card" sentence should be updated likewise, and the new-sign evidence list adjusted: `tolmácsolja` for `6`, `kapuba` for `.1`. The plain-9 list stays at three: azokat, aztán, házat; `kapuba` has `9` = p in the table's own sense.

## Findings not made

The following stand, checked on the pixels: every word of rows 1 to 8 and 12 to 18 except as above; the new signs `6`, `6.`, `4.`, `.1`, `2`, `4`; the three plain 9s read as z (no separate comma on any of them, disclosed); `kevesem` with no d; `lehec`; `májusba`; the disclosed stray `:` after `megfáztam)`; the later violet pencil mark. Names, date and sense fit: a May call-up, 1916; picking caterpillars off in March; a soldier's cold caught at the gate, which fits guard duty but is my inference. Provenance disclosure is adequate.

## What I could not verify

- The sense of `hogy akkor rá lenne`. Every sign reads; a fair translation is still open and the solver's "(?)" should stay.
- Who `ángyika` is on this card; the gloss "aunt or sister-in-law" is the usual meaning, not checked against other cards.
- The exact postmark date, which is partly hidden.
- `kapu` as an actual guard post: the words read, the circumstance does not appear on the card.
- The HistoCrypt article, which I did not open. I also did not review the sister cards' pixels.
