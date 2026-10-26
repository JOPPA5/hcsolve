ACCEPT

# Review 1 — HCP 1397 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-27. In short, **the reading is correct.** I re-read the four cipher lines letter by letter from `source/address.jpg` and get the same 48 letters, decoding under the same Caesar −1 key to *My dearest, this one is a Scotch view. Love from your own girl.* The only differences from the solver are punctuation, letter case and a word gap (finding 1), which do not affect any letter.

## What I verified and how

1. **The documented command.** `python3 ciphers/hcp-1397/work/decode.py` runs, the source hashes match, and it prints the four lines `MY. DEAREST THIS / ONE. IS A. SCOT CH / VIEW. LOVE FROM / YOUR. OWN GIRL.` with 48 letters, as claimed in `SOLUTION.md`.
2. **Independent decoder.** `review/work/my_decode.py` uses my own transcription and does not read any solver file. It applies a −1 shift with wrap-around. Output:
   ```
   Nz. Efbsftu uijt       -> MY. DEAREST THIS
   pof. jt.b. tdpudi      -> ONE. IS.A. SCOTCH
   wjfx Mpwf gspn         -> VIEW LOVE FROM
   zpvs. Pxo. Hjsm.       -> YOUR. OWN. GIRL.
   letters: 48
   ```
   One shift covers every letter. Thirteen of thirteen words are English, with no residue, and the long words (`Efbsftu`, `Tdpudi`) make a chance fit impossible.
3. **Reading the scan.** I rotated the message area 90° CCW (`review/work/msg1x.png`, 4× halves `half0.png`, `half1.png`) and zoomed the hard spots: `z-nz.png` (capital N: two downstrokes, not three, so N and not M), `z-efbsftu.png` (the `tu` at the end is fainter but present), `z-tdpudi.png`, `z-mpwf.png` (ornate capital M) and `z-pxo.png` (p, a looped x, a dark o on the stamp ring, then a dot). I read every letter independently of the solver's crops and agree with all 48.
4. **Search for missed cipher text.** The picture side carries only the printed caption *Trossachs Hotel & Loch Achray*. The address side holds the four cipher lines, the plain date `April 10th 1907`, the circled initials, the plain address `Mr W. Abbott, Stokelake Farm(s), Chudleigh, Devon`, the stamp and the postmark. I found no other enciphered group.
5. **Context.** The postmark reads `…ORNE / 7 PM? / AP 10 / 07` (`z-postmark.png`), which matches the written date April 10th 1907 and the portal date 1907-04-10. The office name ends in -ORNE, so the card was posted in England, not Scotland. That fits "*this one is a Scotch view*", which reads like a remark about the picture on the card rather than the sender's location. The Trossachs caption matches SCOTCH VIEW. A Caesar shift of one is a typical lovers' code on Edwardian postcards.
6. **Sources.** The −1 hypothesis came from "related correspondence" supplied by the root, and the solver discloses this in `SOLUTION.md` and `NOTES.md`. No published solution was used; the portal shows none attached.

## Findings

1. **minor: transcription details that do not affect any letter.**
   - (a) In line 2 the word is written as one cursive word, `tdpudi` (zoom `z-tdpudi.png`), with an ordinary lowercase t. I see no clear word gap, so `Tdpu di` / `SCOT CH` overstates the break. In any case it is a spacing question, which the solver handles correctly by not inserting letters.
   - (b) Punctuation: I read `jt.b.` (dot after `jt` as well as after `b`), no dot after `wjfx` (the mark there is the crossed x itself), and a dot after `Pxo`. The solver's readable sentence already treats punctuation as editorial, so nothing turns on this.
2. **minor: the circled initials are more likely `G. H.` than `C. H.`** (`z-sig.png`). The first initial has a descending tail that turns back at the baseline, like the writer's cursive G. The solver lists both readings without choosing, which is acceptable. If a preference is stated, G is the better one. The solver is right not to shift the initials or the date.
3. **minor: context not used.** The postmark date `AP 10 07` and the English office name (-ORNE) are worth one line in the report, since they independently confirm the date and explain "this one is a Scotch view". The "related correspondence" that suggested the −1 key should be named (portal numbers) in `SOURCES.md`, so a reader can follow where the hypothesis came from.
4. **minor (presentation).** The translation is given in Slovak only. The plaintext is already English, so this is harmless; just make sure the report states that the original language of the plaintext is English.

## What I could not verify

- The full name of the postmark office: only `…ORNE` is legible under the stamp.
- The identity of the sender and of the recipient beyond the written address.
- The related correspondence from which the −1 hypothesis came. It is not in this directory, and it is not needed, since the key is verified on this card alone.
