ACCEPT

# Review 1 — HCP 1190 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the decipherment is correct.** I read all 38 signs on the address side myself, independently of `work/transcription.txt`, and my reading agrees with the solver's sign for sign, dot count for dot count. The key is a clean three-dot Pigpen and the plaintext is natural English that fits the card. The findings below are all minor.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1190/work/decode.py` runs, the source hashes match, and it prints
   `I - SHALL - BE - / THINKING - OF - / YOU - TONIGHT - / RUTH, / BE - GOOD`, 38 glyphs and 17 distinct ones. This is the same as the plaintext claimed in `SOLUTION.md`.
2. **Independent reading of the scan.** I cut `source/address-large.jpg` into 8× crops with `sips` (`review/work/crop.sh`, `z1a…z5.png`) and added 10–14× details for the faint dot groups the solver flagged (`z3-tonight-t.png`, `z3-you-u.png`, `z4-ruth.png`, `z4-ruth2.png`). I recorded what I saw in `review/work/my-reading.txt`, using my own notation (grid cell plus dot count), before I compared it with the solver's file.
3. **Independent decoder.** `python3 -I ciphers/hcp-1190/review/work/review_decode.py ciphers/hcp-1190/review/work/my-reading.txt ciphers/hcp-1190/work/transcription.txt`. It builds the key from the alphabet rows `ABCDEFGHI / JKLMNOPQR / STUVWXYZ` (one, two or three dots), not from the solver's code:
   ```
   I SHALL BE / THINKING OF / YOU TONIGHT / RUTH, / BE GOOD
   38 signs; distinct 17
   letters written with >1 sign: none
   solver signs: 38 | sign-level differences vs reviewer: none
   ```
4. **Signs the solver called weak.** I checked each of them:
   - SHALL: both L's are bottom+left outlines with **two** dots. The second has a tall left stroke but no top stroke, so it is not an open square.
   - TONIGHT, final T: bottom+left+right with **three** dash-like dots. There is no top stroke.
   - RUTH: R = top+left with 2 dots, U = bottom+left with 3, T = bottom+left+right with 3 (faint but countable), H = top+left+right with 1.
   - YOU: the Y has three dots, written to the *left* of the top+right outline, not inside it. U has 3.
   - THINKING, final G: one dot, possibly with a faint speck below it. Reading it as two dots would give P (`THINKINP`), so G stands.
5. **Key consistency and coverage.** Every one of the 38 signs decodes, and none is left over. No letter is written with two different signs, and no sign has two values. Repeated letters are drawn the same way each time: I (×4), N (×3), T (×3), O (×5), H (×3), B, E, G, U (×2).
6. **Context.** The card was posted at Carthage on SEP 14, 4:30 PM, and backstamped at DENMARK on SEP 14. It is addressed to "Miss Ruth …, Denmark, New York", and RUTH in the plaintext matches the addressee. The picture side shows Kings Falls near Carthage and carries no cipher. 1907-09-14, the catalogue date, was a **Saturday**, so "I shall be thinking of you tonight" sent mid-afternoon fits. Same-day delivery between Carthage and Denmark, about 10 miles apart, is plausible. The initials "W.D.M." under the cipher are in plain writing.
7. **Prior solutions.** `SOURCES.md` records the Schrödel 2021 HistoCrypt paper. I grepped `work/schroedel-2021.txt` for `ruth`, `tonight` and `carthage`: none of them occur. The solver says it got the reading before consulting the paper and claims no priority. I found nothing in the files suggesting an undisclosed published solution.

## Findings

1. **minor — the reproduction command decodes a manual transcription, not the image.** The solver says so plainly in `SOLUTION.md`. Because I read the scan independently and got the same 38 tokens, the transcription is now verified externally. The report should say that the transcription was checked sign by sign in review, rather than leaving it described as "needing independent collation".
2. **minor — the key was transferred, not derived.** The alphabet was taken over from the solver's HCP 1193 work, with dot counts in place of numerals. This is disclosed. The key is a standard Pigpen variant (grid order A–I with one, two or three dots for the three blocks, no J omission), and here it is confirmed by the decoded text, not assumed. The report should name it as a dotted three-block Pigpen variant.
3. **minor — editorial punctuation.** The written separators are hyphens plus one comma after RUTH. The full stops and capitals in the normalized text are editorial, which the solver says in `NOTES.md`. `SOLUTION.md` should say it too.

## What I could not verify

- The year. The Carthage cancel shows no year, and the Denmark backstamp is mirrored and faint ("SEP 14 …"). 1907 rests on the catalogue only.
- The recipient's surname and the sender behind "W.D.M.".
- The faint pencil marks under OF in row 2 (`review/work/z2-pencil.png`). They are illegible, are not part of the cipher, and do not affect the reading.
- Whether this card has been deciphered elsewhere. I relied on the solver's bounded checks and did not repeat a web search.
