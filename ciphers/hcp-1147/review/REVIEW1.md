ACCEPT

# Review 1 of hcp-1147

Reviewer: Claude Opus 5.5, 2026-11-02. Round 1. The reading stands. Three minor points remain, and none of them changes the Hungarian text.

## What I verified and how

**Command.** `python3 -I ciphers/hcp-1147/work/decode.py` ran from the repo root. Hashes OK (4 files), 475 signs, 470 by the table, 5 by sense. The printed text matches the plaintext in SOLUTION.md. The script prints from its EXPECT table but only after each decoded line has passed against it, so the check is real.

**Independent transcription and decryption.** I read every row from my own crops of the hi-res scan (`review/work/crop.py`, `z.py`, `crops/`), before comparing with the solver, and wrote it down literally with no sense corrections: `review/work/my_reading.txt`. `review/work/my_decode.py` decodes it with a separately written key and diffs it against `work/transcription.txt`.

- 479 tokens compared (475 signs and 4 Latin groups), 5 differences. All 5 are exactly the solver's disclosed `~` points: L4 `6`, L7 `8`, L7 `1:`, L8 `9`, N3 illegible. Nothing undisclosed differs.
- With no corrections the card decodes to the claimed text except `jagyon`, `mosm`, `egyeb`, `tpbbet` (L8 `tpb` + L9 `bet`), `mon?anám`. 30 distinct signs plus the one illegible spot, all covered by the key. Nothing is left over.

**The five sense readings, judged on the pixels:**

1. `egyéb` (L7): `crops/egyeb.png`. The 1 stands on the printed divider with a round dot at its foot and a high dash to the right. I read this as an ordinary widely spaced colon, so `1:` = e is the literal reading. The dash is not the flag of the next 1, which has its own. The only departure is e for é, as disclosed.
2. `most` (L7): `crops/most7.png`. The final 8 has no comma. A thin dark stroke runs through it, but that stroke is inside the figure and is not a comma. Sense reading correct and disclosed.
3. `nagyon` (L4): `crops/nagyon3.png`. The single stroke sits under the 8 of mert, and the 6 has none, as the solver says.
4. `többet` (L8): `crops/tobbet8.png`. The shape is a plain 9 with its tail. Comma-joined `0,` is a fair explanation, but it rests only on sense and the two other spellings of the word on this card. Disclosed.
5. `mondanám` (N3): `crops/mondanam2.png`. Only a low curve and part of a stem survive, among the printed "Import" letters. It does not fix the digit, and I marked it illegible. d is forced only by the word, which is the one word that fits, and the solver says exactly this.

**Sample and hard rows.** All rows were read, not sampled. The rows over print or postmark (L2 to L6, N1 to N3) agree with the solver. The end of L3 (`crops/l3rest.png`) reads `1: 5, 1. 5 ·1 7,`. The dot-left `·1` is clearly visible in húsvét, tudok, nyugaton. The two strokes near L3 are the accent of the address word Őnagysága, not cipher marks. The picture side has no writing.

**Key.** The table for the signs shared with hcp-1174 agrees with that card. Of the new signs, `6`, `6.`, `4.`, `8.` and `·1` (`.1`) are read the same way on sister cards hcp-1135, 1148, 1150 and 1160. Those cards are not all FINAL, so this is support, not proof. Here `6.` and `8.` each occur once only, in nyugaton and kártya, so they rest on one word each. The solver's "recurs" statement ("each recurs") does not hold for these two on this card, but both are the only reading of the word. The eight `4.` and six `·1` counts are correct.

**Language and context.** Natural Hungarian prose and three rhymed quatrains, at 475 signs far too long and coherent to be forced. Easter Sunday 1916 was 23 April, so a card dated IV/20 (open text in the top margin, `crops/date.png`) fits. Recipient and signature fit the correspondence. Military leave for Pista is rightly labelled as interpretation.

**Published solution.** Portal status per `source/metadata.md`: Not solved, nothing attached. The solver had not checked the linked HistoCrypt article. I fetched its page: the abstract is about a collection of more than 400 encrypted postcards and does not mention Hungary, Mezőkövesd or Margitka Sziber. I read only the abstract page, not the full text. No sign of an undisclosed source.

**Skip and register.** 1147 is not in `skip.txt` or `register-exclusions.json`. MASC is a valid label.

## Findings

1. **minor. `ablakomra` (M3): overinked sign not disclosed, and the word sits badly with its context.** The 8 in `1. 1, 5, 1. 7 0 8 3, 1.` is the most heavily blotted sign in the block (`crops/ablakc.png`, `ablakr.png`). The solver's list of doubtful points does not mention it. The middle of the sign is a solid mass, with a tick hanging into the lower loop and the comma of the row above running into it. Both loops are closed, so on the pixels it is 8 = m and I see no underlying 3. The transcription is therefore right. But the verse says the bird flies "hozzád" (to you) and "oda" (there), which makes "my window" odd, while `ablakodra` ("your window") would be the natural sense; the blot might be a correction or the writer's own slip. Fix: keep `ablakomra`, list the blot as an uncertainty, and note the tension in the translation. A web search did not find the verse, so it cannot be settled from a printed source.

2. **minor. The tally and the "all five points" statement are slightly overstated.** `4.` in légy (L2) has its dot hidden under the blot, as the solver itself says under "Other points", yet it is counted as by the table and has no `~`. Separately, the 7 of közepén (N4, `crops/n4k.png`) is abraded, leaving the foot, the bar and a piece of the top. It is still a 7, but this damage is not mentioned. Fix: mark légy with `~` so the count becomes 469 + 6, mention N4, and change "each recurs" to say that `6.` and `8.` occur once here.

3. **minor. Translation of "kis angyalom".** SOLUTION.md renders "kis angyalom, a madárka" as apposition ("my little angel, the bird"). It is more naturally a vocative to Margitka: "To you from afar, my little angel, flies the bird". Fix in the English and Slovak, or note both readings.

## What I could not verify

- The sign in N3: it is illegible, and its value rests only on the word.
- Whether the blot in M3 hides a correction; a scan cannot show ink order here.
- The postmark year, which the solver also leaves open. The date rests on the writer's own note.
- Who Pista is, and whether the verses are quoted from a known source. My one search did not find them: https://zti.hungaricana.hu/en/192190 was the nearest thing, a folk song with similar bird imagery, not this text.
- The full text of the HistoCrypt article, https://ecp.ep.liu.se/index.php/histocrypt/article/view/166.
