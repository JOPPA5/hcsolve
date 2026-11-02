REVISE

# Review 1 of hcp-1142 (reviewer: Claude Opus 5.5, 2026-11-02)

The cipher reading stands: I found no wrong sign, and all 15 cipher rows read. Three concrete fixes are needed. Two are in how the solution states its evidence (findings 2, 3). One is the printed form of the open word at the foot (finding 1). No blocker.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1142/work/decode.py` from the repo root. Hashes OK (4 files), 210 cipher signs, 30 distinct, lines match the stated reading, and this agrees with the plaintext in SOLUTION.md.
- Own decoder `review/work/decode_own.py`, with a table typed separately from FINAL hcp-1174/1178/1179 and the 7 new values kept apart and bracketed. Same text, same counts. 11 of 210 signs use the new values: `2` 1, `4` 1, `4.` 3, `5.` 2, `6` 2, `6.` 1, `8.` 1.
- Checked `work/transcription.txt` against `work/hires/..._adr.jpg` for **every** row, not a sample, using my own crops (`review/work/crop.py`; r01-r11, x10b, x13a/b, x14, x15a/b at about 5x, `ty.png` and `end.png` at about 17x). All marks agree with the transcription: comma against dot against colon, the high dot of `1'`, the two left dots of `:1`, and all 5 `1'` signs. The foxing spot on the `3.` of `verése` (row 7) sits on the dot, but a dark dot is visible in it.
- Each new value is forced by a plain word: `felmegyek`, `nagyon`, `jó`, `mondja`, `piciny`, `kártyán`, `hely`. A wrong value gives no word in these places. The two rhyming pairs and the running sense hold across the whole card. This is real Hungarian of the period, with the writer's dialect form `üdő`, which also stands on hcp-1160 and 1170.
- `8.` in `kártyán` (uncertainty 2): at 17x (`ty.png`) a round dot head stands beside the 8 and a thin pale tail runs from it under the next sign. So it is a dot with a pen drag, not a comma. Plain `8` gives `kármyán`. Accepted, and correctly disclosed.
- Last sign of `maradok` (uncertainty 1): see finding 4.
- Open text, address and signature read from crops: `Számtalanszor`, `csókollak`, `Sz. A.` in a loop, `Tek.`, `Szépreményü`, `Sziber Margitka`, `kisasszonynak`, `(Szomolya.)`, `u. p. Bogács`, `(Borsod m.)` all stand. The last word of the foot is finding 1.
- Picture side (`review/work/pic.png`): printed tinted photograph with publisher's marks, no writing, as claimed.
- Family claims checked in the SOLUTION files: `Számtalanszor csókollak mindnyájatokat` is on hcp-1172; `mindnyájatokat csókollak` on 1152, 1154, 1157; `üdő` on 1160, 1170; `aszt` on 1151, 1161, 1172; `A lapodat megkaptam, melnek nagyon megörültem` on 1160.
- English and Slovak translations are faithful, and the alternative sense of `mindenik verése` is disclosed. Portal status Not solved and no attached solution are recorded in the captured metadata. No sign of an undisclosed published solution.

## Findings

1. **minor (concrete fix needed). The printed word at the foot is not what the card shows.** SOLUTION.md prints `mindnyájatokat` in the plaintext, and only uncertainty 3 says the card may differ. On `review/work/word.png` the letters after `mind` are a clear `a`, then `n`, then a descender letter. So the card has `mindany...` or similar, and the strokes are not `mindny...`. After that come an a-like letter, an open c-like letter under an acute, a descender with a tick above and right, then `-tokat`, with the crossbar of t long. The word is written the writer's own way and is not a blot, so the normalised form should not stand as the reading. Fix: print the seen form with its doubt, for example `mindanyájatokat (?)`, gloss it as a form of `mindnyájatokat`, and use the same form in the translations' note and the report. It stays one word with an assured sense, so under the run's rule the card is still complete.

2. **minor (concrete fix needed). `5.` = ly conflicts with FINAL cards, and this is not disclosed.** SOLUTION.md lists `5.` among the signs "not on those tables, or tentative there". That is wrong for this sign: FINAL hcp-1178 (decode.py, and its review response) and hcp-1179 (`key.json`, `a legszeb`) give `5.` = l firmly. hcp-1149, 1166 and 1168 also use l. The solver's words remain right, because `amelnek` and `hel` would be the same words spelled as this writer spells (`melnek` on hcp-1160). But the card itself cannot separate l from ly, so the "regular pattern" of palatal dots is not proved for this sign. Fix: state the conflict and say that `amelynek` and `hely` are normal spellings of what could be written `amelnek`, `hel`.

3. **minor (concrete fix needed). The independence claims are slightly too strong.** "Neither rhyme was used to set a key value" is true of key values, but uncertainty 1 says `maradok` rests on the rhyme. So the pair `írhatok / maradok` cannot also count as independent support for that sign. Only `verése / teremtése` is fully independent. Also, hcp-1152, 1154 and 1157 are called unreviewed, but they now carry REVIEWED1, and only hcp-1172 has no marker. Reword both.

4. **minor. The last sign of `maradok` is less like a flourish than the solution suggests.** On `end.png`, the right arm of the wedge under the 7 runs from upper right to lower left, the direction of this writer's commas, and it sits at the foot of the 7, where a comma sits. Compare the large hooked `7,` in `teremtése` (row 9). A second arm from the left makes a V, which a comma does not have. The tail from the 0 does not join it. So the graphic evidence is open. `marados` remains no word, so `maradok` stands on sense alone. Uncertainty 1 can say that plainly, without "points towards a flourish".

5. **minor. Date and seal.** The purple seal year 1906 is confirmed (`review/work/stamp.png`). Inverted lower arc letters look like `...GYE`, so the seal may be `BORSOD VÁRMEGYE ...`. That fits a seal year and not a posting date, which supports the solver's caution. I could not read the grey postmark either: ring letters show outside the stamp at lower right, but no place or date can be made out. "No date established" is correct. Optional: add the seal note.

## What I could not verify

- The HistoCrypt article and any source for the couplet (the solver did not check them either, and says so).
- The grey postmark and the middle of the purple seal.
- Whether the capital in the signature is A rather than K. It looks like A on `foot3.png`, and I accept the disclosed reading.
- The exact letters of the middle of the foot word (finding 1).
- The sister cards' pixels; I checked only their SOLUTION files and key files.
