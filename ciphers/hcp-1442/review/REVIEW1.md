ACCEPT

# Review 1 — HCP 1442 / pc_hcp_123 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the decipherment is correct and complete.** I read all 46 Pigpen signs on `source/address.jpg` myself, sign by sign, and got exactly the same letters with the same three-count Pigpen key. I found no Pigpen text that the solver missed. The findings below are minor: one interpretive point that actually *removes* a claimed date problem, and some things to record.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1442/work/decode.py` runs (exit 0), the source checksums pass, and it prints the 7 rows claimed in `SOLUTION.md` (46 letters). The output is identical to `work/plaintext-check.txt`.
2. **Independent decoder.** `review/work/pigpen_review.py` (my own code, nothing imported from the solver). It builds the key from the grid geometry: cell (r,c) has a top stroke if r>0, bottom if r<2, left if c>0, right if c<2, and letter = A + 9·(dots−1) + 3r + c. Tokens are written as the strokes I *see* plus a dot count. `review/work/my-transcription.txt` is my own reading, made from my own crops. Output in `review/work/my-output.txt`:
   ```
   MON / IF YOU DONT GO / TO NIGHT CALL / ME UP / SAT / AFTERNOON / NANCY   (46 glyphs)
   ```
   A letters-only comparison with the solver's output is **identical** (46 = 46).
3. **Independent reading of the scan.** I made ffmpeg crops of the card, rotated and upscaled 3–9× (`review/work/main.png`, `l1z.png`, `l2a.png`, `l2b.png`, `l2c.png`, `l3a.png`, `l3b.png`, `l4.png` for the main block, card rotated 90° clockwise; `centerwide.png`, `cz1.png`, `cz2a.png`, `cz2b.png`, `cz3.png` for the centre block, rotated 90° counter-clockwise). I checked every sign for its outline and dot count:

   | Line | Signs as seen | Reading | vs. solver |
   |---|---|---|---|
   | main 1 | ]2 [2 □2 , | MON, | same |
   | main 2 | ┌1 [1 , ┐3 [2 └3 , ]1 [2 □2 ⊔3 , ┐1 [2 | IF, YOU, DONT, GO | same |
   | main 3 | ⊔3 [2 - □2 ┌1 ┐1 ⊓1 ⊔3 , └1 ┘1 └2 └2 | TO-NIGHT, CALL | same |
   | main 4 | ]2 □1 (underlined) └3 ┐2 . | ME UP. | same (underline not noted, finding 3) |
   | centre 1 | ┘3 ┘1 ⊔3 . | SAT | same |
   | centre 2 | ┘1 [1 ⊔3 □1 ┌2 □2 [2 [2 □2 . | AFTERNOON. | same |
   | centre 3 | □2 ┘1 □2 └1 ┐3 , | NANCY, | same |

   The two signs the solver flagged agree with its reading: the 2nd sign of MON has a faint but present top stroke and no right stroke (`l1z.png`), so it is [2 = O. In SAT the third sign has left, bottom and right strokes and three dots (`cz1.png`). The diagonal lines crossing it are the grey watermark wheel, not ink.
4. **Missed cipher text.** I looked over the whole address side: the area between the two blocks, the area under the stamp, and the edges. I also looked at the picture side. The only other handwriting is the plain-text address (`Ray E. Bartley / Rutland, / Iowa`), the cursive `Dec. 16-07 / Received your / card Sat morn[ing] / this is` that leads into the centre block, and a two-sign cursive mark at the lower left of the picture side (`review/work/picmark_cw.png`, something like "23" or "JB"; not Pigpen). The large grey wheel and the symbols on both sides are the portal's watermark. **No Pigpen signs are left untranscribed.**
5. **Key consistency.** One fixed key with no exceptions. Each letter that repeats uses the same sign every time (counted by script over my transcription): O = [2 (×7), N = □2 (×7), T = ⊔3 (×5), A = ┘1 (×4), and ×2 each for C, E, F, G, I, L, M, U, Y. No letter needs two different signs and no sign needs two different letters.
6. **Context.** The postmark reads `RUTLA[ND] DEC 16 … IOWA`. The address is Rutland, Iowa, so this is local mail. That fits the request "call me up" (by telephone). **16 December 1907 was a Monday** (`python3 -c "import datetime;print(datetime.date(1907,12,16).strftime('%A'))"` → Monday). See finding 1. The plaintext is natural colloquial American English of the period (`call me up`, `to-night`, `dont` without an apostrophe).
7. **Prior solutions.** The portal status is Not solved. The name/URL does not appear in the solver's register snapshot (`ciphers/hcp-1450/work/register-snapshot.json`), and the cipher is not in `skip.txt`. Nothing in the files suggests a published solution was used.

## Findings

1. **minor — the "date/day mismatch" is mostly not a mismatch.** `SOLUTION.md` says "The apparent date/day mismatch between MON, SAT and the written/postal date is retained, not repaired." But the written date and the postmark are both **Monday** 16 December 1907, so the heading `MON` agrees with them exactly. Only the centre note ("Received your card Sat morning / this is SAT AFTERNOON") points back to Saturday 14 December. A simple reading is that the centre part was written on Saturday afternoon and the main part on Monday, when the card was dated and mailed. Please correct the statement and add the weekday check as positive evidence. Do not change any glyph.
2. **minor — context from the card not recorded.** `SOLUTION.md` gives the recipient only as "Ray Bartley, North America" from the portal. The card itself says `Ray E. Bartley, Rutland, Iowa`, and the postmark is Rutland, Iowa, DEC 16. Record both. They place the card more precisely than the portal does and support the local "call me up".
3. **minor — underline not recorded.** In main line 4, a pen stroke runs under the two signs of `ME` (`review/work/l4.png`), which most likely emphasises the word ("call ME up"). It is not a cipher sign and does not change the reading. A diplomatic transcription should note it.
4. **minor — protocol.** `work/plaintext-check.txt` has the same timestamp as `DONE1` (15:38:04), and the `work/` directory's mtime (15:38:06) is two seconds later than the marker, so something in `work/` was created or removed after `DONE1`. The source hashes still match, so this has no effect on the result. No watcher was started (`NOTES.md` says so). The translation is in Slovak. If the report is meant for an English-speaking reader, an English one would be useful, but the README does not require either language.

## What I could not verify

- The cursive context lines are only partly readable ("morn…" is cut by the watermark). I checked only that they lead naturally into `SAT AFTERNOON`.
- The year on the postmark is not legible. 1907 comes from the handwritten `Dec. 16-07` and the portal.
- Who "Nancy" is. I did not search outside the repo for a published decipherment; I relied on the portal status and the register snapshot.
