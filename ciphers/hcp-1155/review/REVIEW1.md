ACCEPT

# Review 1 of hcp-1155 (Claude Opus 5.5, reviewer, 2026-11-02)

The reading stands. I tried to refute it and could not. All 527 signs decode into coherent Hungarian, and no sign I checked on the pixels changes a word. The findings below are minor and concern disclosure, not the reading.

## What I verified and how

1. Solver's command, `python3 -I ciphers/hcp-1155/work/decode.py`: exit 0, hashes OK, 527 signs, 31 distinct, 4 flagged. The output matches SOLUTION.md. Its `EXP` table is the solver's own expected reading, so its assertions only show that transcription and text agree. They are not independent evidence.
2. Own decoder, `review/work/verify.py`, with its own key table and tokeniser. It decodes `work/transcription.txt` with no unmapped sign, gives the same counts (.1 = 9, 1, = 10, 4. = 10, 6 = 7, 6. = 3, 4 = 4, 2 = 1, 5. = 1) and has 0 conflicts with the 23 signs of the hcp-1174 table. After folding accents, the plaintext in SOLUTION.md differs from the decode only by the added `y` of the Nyúllápa spelling in my folding, `jöt` > `jött` (finding 4), and the III/IV labels.
3. Scan hashes: SHA-256 of all four files recomputed with `shasum` and equal to SOURCES.md.
4. Transcription against `work/hires/*_adr.jpg`: I went through all rows in 2.2x strips (`review/work/sL*.png`, `sR*.png`, `fL.png`, `fR.png`) and found no disagreement in sign or mark. Digit and mark were compared by eye against the solver's list, so this was a check, not a blind re-transcription.
5. Sign-level crops at 3 to 5x of every flagged sign and of the hard spots:
   - `Lúbin` (`zF.png`): the second sign is a 1 with top hook and a left blob touching it, the same form as the .1 of `fúvás` (`zB.png`). The third has no crossbar, so it is 1, and not 7,. The solver's reading is the better one, and `Lúsin` remains correctly disclosed as not excluded.
   - `láttam` (`zC.png`): the loop is low and the comma is fused to it, so it is a deformed 8, and not a 9, which has its loop high. Same deformation as the first sign of `talán` (`zD.png`).
   - `arra` (`zG.png`): the third sign is a 3 with a closed top and a bottom hook, with a separate comma; see finding 3. The last sign has one low dot, so 1. = a.
   - `kérlek` (`zH.png`): the bar and comma of 5, are present under the stamp; the 1: has both dots. Read correctly.
   - `Lúbin` elsewhere: a grep of the SOLUTION.md files of hcp-1130 to 1179 (44 of 46 directories have one) finds the name only here, which confirms the solver's statement.
   - `hű` (`yC.png`): 5 without comma, then .1 with a clear left blob.
   - `kövesdre` (`zE.png`): `3` with closed top, the same form as in `arra`. The straight-tailed 9 of `üzletbe` is different.
   - `Nyúllápáig` (`zJ.png`): both 1' have a single high dot.
   - `vissza`, `ne kérd`, `azt a levelet` (`yA.png`, `yB.png`): readable under the stamp; the dot of 1. in `a` is fused to the foot.
   - `bemenni` blot and `tér-` (`sR2.png`, `yE.png`): the ink blot is not a sign, and the t is a retraced 8,.
6. Key logic: 8 values from word sense are not free fits. `1,`, `4.`, `.1` and `6` recur up to 10 times in unrelated words. Couplet rhymes `nyakam/határtalan` and `madár/rátalál` come out, and all digraphs and accents behave.
7. Language and context: real period Hungarian with a plausible informal spelling. The translations are fair. 15 Feb 1916 was a Tuesday, 20 Feb a Sunday and 22 Feb a Tuesday (computed). hcp-1174 does say `A jövő vasárnapi bátran felmegyek`, so the sequence fits, and `Árpád`, `Édes Margitkám`, Szomolya and Bogács all match it. The postmark shows `FEB 2…` (`yD.png`), which agrees with II/22 as far as it can be read.
8. Open text: address and the printed verse on the picture side match the scan where the print survives. The address actually has `(Borsod m.) u. p. Bogács` with brackets, which the solver drops; this is trivial.
9. Honesty: no solution attached on the portal, per SOURCES.md and metadata. Nothing suggests an undisclosed source. The HistoCrypt article being unchecked is disclosed.

## Findings

1. **minor. The count of "four signs read by sense" is low.** At least two more signs rest on word sense but carry no `~` and no note in SOLUTION.md:
   - L10 `tér-`: the transcription gives `2.`, but on the card (`zA.png`, `yE.png`) a wavy ligature runs from the foot of the 2 into the 3, with only a swelling where the dot should be. Strictly the sign is unmarked. `é` is clearly right from the word.
   - L14 `talán`: the sign given as 5, has a filled closed bowl (`zD.png`), unlike the open 5 elsewhere. Only its bar and comma support 5,. NOTES.md records this as the former `Marán`, but SOLUTION.md does not.
   Fix: mark both `~` and add them to Uncertainties, and adjust the counts.
2. **minor. "New on this card" overstates.** `1,` = b is already in hcp-1179's table and `4` = f is reported there from hcp-1175. Only `2`, `4.`, `5.`, `6`, `6.`, `.1` need this card alone. This helps the solution, since those two values are independently attested. The "8 new values" statement under "Why I believe it is correct" should be corrected to match.
3. **minor. The note on `arra` is too pessimistic.** "Shaped like a 9 with a comma, so the strict reading is z" does not fit the pixels. The sign has the bottom hook of the writer's closed-top 3, as in `kövesdre`, and not the straight tail of 9. The reading is therefore better supported than stated.
4. **minor. `jött` is silently normalised.** The intro says spelling is as written apart from accents, spaces and punctuation, and `rosz`, `onnat` and the like are kept, yet the card's `jöt` appears twice as `jött` in the normalised text. Keep `jöt` there or state the change.

## What I could not verify

- `Nyúllápa` and which `telep` is meant: no gazetteer checked. `Lúbin` as a person remains an inference.
- The linked HistoCrypt article was not read; I did no web search for a published solution.
- The purpose of `III`, `IV`, the underlines and the arrow, and the identity of "that letter".
- The transcription check was by eye and not blind (see item 4 above), and word breaks are the solver's.
