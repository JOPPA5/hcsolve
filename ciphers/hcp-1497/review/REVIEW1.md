REVISE

# Review 1 — HCP 1497 / pc_hcp_178 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the key is right, and 30 of the 32 claimed cipher words are right.** I re-read every Pigpen word on `source/address-large.jpg` myself. One claimed word is wrong: the card has `WAITING` (7 signs), not `LOVING` (finding 1). The transcription also leaves out one whole cipher word in the PS (finding 2). The verdict is REVISE, not REJECT: the cipher type and key stand, and the fixes are local, but the plaintext as handed over says something the card does not.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1497/work/decode.py` exits 0, the source hashes match, and the output is byte-identical to `work/plaintext.txt` (`diff` empty). 147 letters, 32 words.
2. **Independent decoder.** `review/work/decode_review.py` builds the standard interleaved Pigpen key from grid geometry (cells 1–9 row by row, dot = second letter of the pair, X wedges v > < ^ = S/T, U/V, W/X, Y/Z). It does not use the solver's code. `review/work/convert_solver.py` maps the solver's stroke names to my cell numbers by geometry. Decoding the solver's transcription this way gives exactly the solver's 32 words (`solver_decoded_by_reviewer.txt`, `diff` empty). The key is a fixed 26-letter table, so no sign can take two values. Every token in the transcription is covered.
3. **Independent reading of the scan.** I cropped the address side with `sips` (`review/work/crop.sh`; strips `c_*.png` at 3–4×, details `z_*.png` at 5–16×) and read every cipher word sign by sign before comparing my reading with the solver's. My reading is in `review/work/reading_review.txt`, and its decoding is in `reading_review_decoded.txt`:

   | Place on card | My reading | vs. solver |
   |---|---|---|
   | body: "written or … to … before" | BEEN ABLE / SEE YOU | same |
   | "not at all …" / "to the …" / "have my …" | WELL / DR / EYE | same (the middle wedge of EYE is crossed by the `y` of *Monday*, `z_eye.png`) |
   | "I shall … as soon" | COME OUT | same |
   | "do not get … of … ," | TIRED / **WAITING** / DARLING | **differs**, see finding 1 |
   | "as I am so …" | LONELY | same |
   | "if you will … me the other … of my …" | SEND / HALF / LETTER | same |
   | last line "Wednesday if … cannot" | YOU | same |
   | top line 1 | MANAGE (it) DEAR … WAIT … YOU, then a struck-out word | same apart from the struck-out word, see finding 4 |
   | top line 2 | NEXT | same |
   | closing above *Maud* | YOUR EVER LOVING GIRL | same |
   | PS line 1 | ABSENCE / HEART / FONDER | same letters (see finding 3 for the 6th sign of ABSENCE) |
   | PS line 2 "I wonder if it is so with you …" | **?EAR** (probably DEAR) | **missing from the solver**, see finding 2 |
   | PS line 3 | MY DARLING SWEETHEART | same |

4. **Language and context.** This is natural Edwardian English, and the cipher words fit the cursive around them exactly. My reading of the cursive frame, enough to place every cipher word, is: *"Thanks for P.C. am so sorry I have not written or BEEN ABLE to SEE YOU before, but I am not at all WELL, had to go to the DR Monday evening to have my EYE seen to … I shall COME OUT as soon as possible, so please do not get TIRED of WAITING DARLING. Now I am afraid as I am so LONELY I must ask you once more if you will SEND me the other HALF of my LETTER by the 9.15 post in Dulwich Wednesday; if YOU cannot MANAGE it DEAR, well then I will ask you to WAIT until I see YOU NEXT time, which I hope will be Thursday or Friday … YOUR EVER LOVING GIRL Maud. P.S. 'ABSENCE makes the HEART grow FONDER' I wonder if it is so with you [D]EAR. MY DARLING SWEETHEART."* The portal date 1904-11-22 was a **Tuesday**. That fits "Monday evening" (yesterday) and a reply by "Wednesday". The postmark shows `NO … 04` and `S.E`. The picture side is "Dulwich Park", which matches "post in Dulwich".
5. **Address.** I read `Mr E. R. Mobsby, 9 Carden Road, Peckham, S.E.` (`z_address.png`), see finding 5.
6. **Prior solutions.** The files show no sign that a published solution was used. The register snapshot check is documented.

## Findings

1. **major — `LOVING` in the body is a misreading. The card has `WAITING`.** Detail: `review/work/z_waiting.png` and `z_tired.png`. After "do not get TIRED of" the word has **seven** signs: `<` (W), `⅃` (A), box (I), V with a dot at the apex (T), box (I), dotted `ㄱ` (N), `]` (G). The solver's line `L1 T0 >1 C0 TR1 R0` (6 signs) does not match these shapes. The 1st sign is a `<` wedge, not a `[`. The 2nd sign is `⅃`, not `⊓`. There is no `>` wedge. "Tired of waiting, darling" is also the natural sense. The transcription, decoded word list, letter count (147 → 152 with finding 2) and the combined reading in `SOLUTION.md` ("TIRED of LOVING DARLING") must be corrected. Most likely the solver carried over `LOVING` from the closing *YOUR EVER LOVING GIRL*.

2. **major — one cipher word in the PS is not transcribed.** Detail: `review/work/z_ps_knot.png`, `z_ps_dear.png`, `z_ps_line2.png`. Two Pigpen words sit directly above each other here. The upper one is `HEART` (PS line 1, after "makes the"). The lower one ends PS line 2 ("I wonder if it is so with you …") and reads `? 3 1 9.` = `?EAR`, followed by a full stop. Its first sign touches the cursive `you` and is partly hidden. It is a cell-2/4/6 form with a dot, so D, H or L, and `DEAR` is by far the likeliest. The solver's `NOTES.md` flags "PS HEART where handwriting crowds the symbols" but lists only one word there. The transcription must add this word (first sign marked uncertain), and the PS reading should become "… I wonder if it is so with you [D]EAR".

3. **minor — 6th sign of ABSENCE.** Detail: `review/work/z_ps1b.png`, `z_ps1c.png`. The sign the solver reads as `B0` (C) is V-shaped, with slanted sides meeting at a point. It looks like the 3rd sign (`V0`, S) and not like this hand's flat-bottomed `⊔` in COME, DR, DARLING, SEND. The card may therefore literally say `ABSENSE`, a common misspelling. At 1024 px I cannot decide. The solver should record the sign as seen and list it as an uncertainty, rather than silently normalising it.

4. **minor — unrecorded struck-out sign and a stray stroke.** (a) At the end of top line 1, after `YOU,` (`z_struck.png`), there is a cancelled start: a dotted `ㄱ` (N) followed by an inked-over blot. It is evidently `NEXT` begun and then rewritten on the next line. It should be noted as a cancellation, not counted. (b) In the last body line, the `ʌ`-shaped stroke between *Wednesday* and *if* (`z_wed.png`) is, in my view, the descender of the `h` of *Dulwich* and not a `^` (Y). The solver correctly does not count it, but it is worth one sentence.

5. **minor — address and identities.** `SOLUTION.md`/`metadata.md` give "9 Ewerdon Road [provisional]". The card clearly reads **9 Carden Road**, and so does HCP 1498, sent to the same addressee. The two cards share writer (Maud), recipient (E. R. Mobsby, "Ernest" on 1498), address and Dulwich context. This is useful context the report could state, while still not identifying the persons historically.

6. **minor — scope of the plaintext.** `SOLUTION.md` gives the cursive only as an elided summary. For a mixed cursive/Pigpen card, that leaves the reader unable to see where each cipher word stands. A full (even if partly uncertain) diplomatic reading of the cursive, like the one in item 4 above, would make the report self-explanatory. The solver also states that `decode.py` decodes a manual transcription, and that a correct round trip is not evidence about the pixels. That is accurate, and to its credit.

## Required for closing

- Replace the body word `LOVING` with `WAITING` (`<0 BR0 C0 V1 C0 TR1 R0`) in the transcription, the word lists and the combined reading.
- Add the PS-line-2 word `?EAR` (probably `DEAR`, first sign uncertain) and update the counts.
- Record the 6th sign of ABSENCE as uncertain (S vs C), the cancelled `N…` on the top line, and the address `9 Carden Road`.

The key and the overall reading stand. If these corrections are made exactly, I see no need for another full review round.

## What I could not verify

- The first sign of `?EAR` in the PS: it is crowded by the cursive *you*, so D/H/L cannot be settled from pixels alone.
- Dots in a few crowded places (e.g. FONDER's `D`, the `F` of HALF). They are compatible with the solver's reading but small at this resolution.
- The cursive text in full detail (e.g. the name in "tell Standly(?)") — not part of the cipher claim.
- The postmark day; I could read only `NO … 04`.
- Whether a decipherment has been published elsewhere. I relied on the solver's statement and register snapshot.
