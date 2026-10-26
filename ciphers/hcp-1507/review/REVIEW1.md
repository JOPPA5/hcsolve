ACCEPT

# Review 1 — HCP 1507 / pc_hcp_188 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the decipherment is correct, and so is the transcription.** I read all 93 numeric signs from the scan without looking at the solver's file, and my reading agrees with `work/transcription.txt` token for token. The one awkward word, DOR, really is written that way on the card, and the solver reported it literally. The findings below are all minor.

## What I verified and how

1. **The documented command.** `python3 ciphers/hcp-1507/work/decode.py` runs without error. The hash checks pass, and the output is byte-identical to `work/plaintext.txt` (`diff` is empty): "Encrypted numeric positions: 93".
2. **Independent decoder.** `review/work/review_decode.py` is my own script and imports nothing from `work/`. Numbers missing from the key print as `[n]`. Run on `review/work/my_transcription.txt` (my reading), it gives:
   ```
   M Y DEAR LEAH / I EXPECT TO / SEE YOU IN / TOWN Sat. Eve. DEAR / DOR ME /
   A RIDE W ILL DO / YOU GOOD HONEY / I WILL LOOK FOR / YOU SWEETHEART / Good. N IGHT
   -- cipher tokens: 93; distinct numbers: 21; unmapped tokens: []
   ```
   The number-use histogram is identical to the one from the solver's file. A `diff` of the two transcriptions is empty once I normalize one word boundary: the writer puts a dash between `1` and `26` in MY, the same kind of break as W-ILL and N-IGHT.
3. **Independent reading of the scan.** I rotated `source/address-large.jpg` by 270° (`review/work/msg_r.jpg`) and cut 4× half-line strips (`review/work/crops.sh`). I also made 7–8× details of the critical signs: `l5dor.jpg` (DOR), `l8for.jpg` (FOR/HONEY), `l6do.jpg` (DO), `l3see.jpg` (SEE) and `l9sw.jpg` (SWEETHEART).
4. **Key consistency.** It is the same key as HCP 1506. One number gives one letter, and no number needs a second value. 18=D occurs in DEAR (×2), RIDE, DO and GOOD, and 11=F in FOR. The `1ß` of DOR is the writer's two-stroke 18, which differs clearly from the two plain strokes of 11 in FOR on line 8. So DOR is what the card says, and no key change can turn it into FOR.
5. **Language and context.** Natural American English: "My dear Leah, I expect to see you in town Sat. eve. … A ride will do you good, honey. I will look for you, sweetheart. Good night." It fits the card. The address is Miss Leah Doane, Little Marsh, Pa. The postmark reads KNOXVILLE MAY 10 1913, and the written date `5-10-13` (10 written over 9, or the reverse) matches it and the portal date of 1913-05-10. The plain note at the top reads "Please come to the store first thing". The picture side carries only the printed caption "VHEN VILL VE MEET TO SHVEET NODINGS SHPEAK" and has no cipher.
6. **Prior solutions.** The portal shows Not solved, with no attachment; this is recorded. I found nothing in the files suggesting that an outside solution was used.

## Findings

1. **minor: SEE is not certain at sign level.** See `review/work/l3see.jpg`. The second digit of the first token on line 3 is a small closed loop with a curl on top. It sits between this writer's `0` (as in `10.21…` SWEETHEART) and the top-loop `8`. As 18 the word would read DEE. Context fixes it as SEE, and the solver's note "SEE starts 10" shows the sign was looked at. It belongs in the uncertainty list in `SOLUTION.md` all the same.
2. **minor: DOR, a possible reading.** I agree with the literal DOR and with the solver's refusal to emend it. The line ends after `1.3` (ME) with a cross mark. One further possibility to mention is that the writer began `18.7` (DO) and the stray `4` is a slip, giving "Dear, do me…". That reading is no better than FOR. Both are guesses, and the report should present them as such.
3. **minor: header date.** The solver says the date was "not confidently transcribed". I read `5-10-13`, with one digit of the day overwritten, and it agrees with the postmark. It can go in the report as the date of the card.
4. **minor: cross-card evidence.** HCP 1506 uses the same key and has the same recipient. Its header group `24.24.24` decodes to XXX with this card's 24=X. Saying so in the report would strengthen both cards.

## What I could not verify

- The cursive signature under the last line (`review/work/signature.jpg`) looks like an "E" monogram with "t." or "r." I could not read it, as the solver could not.
- Whether the "xx×" marks at lower right are kisses or something else (they are not cipher numbers).
- Whether the solution has been published elsewhere. I relied on the solver's portal capture and register snapshot.
