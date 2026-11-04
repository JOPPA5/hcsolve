ACCEPT

# Review 1 — hcp-1036 (reviewer: Claude Opus 5.5, 2026-11-03)

## What I verified and how

1. Solver command. `python3 -I ciphers/hcp-1036/work/decode.py` from the repo root: hashes OK, output
   `NASSOW / HERZLICHEN GRUSZ / SENDET IHNEN / FRIDA MISCHKE`, identical to the plaintext claimed in SOLUTION.md.
2. Independent transcription. I cropped the pencil block from the hi-res scan
   `work/hires/cpc_1906-08-13_DE_Stolp_DE_Koslin__pic.jpg`, rotated it 90 degrees and enlarged it 2x on top of the
   2.17x hi-res factor (`review/work/seg0.png`, `seg1.png`, `seg2.png`). I read every one of the 44 numbers myself
   before comparing. My reading is identical to `work/transcription.txt` (checked with `diff`, result
   TRANSCRIPTION_MATCH), including the word gaps:
   - line 1 (on the printed "Gruss aus ......" dotted line): 13.1.18.18.14.22.
   - line 2: 8.5.17.25.11.9.3.8.5.13.  7.17.20.18.25. (the final "18.25." is written cramped against the right edge, but separate digits are clear)
   - line 3: 18.5.13.4.5.19.  9.8.13.5.13.
   - line 4: 6.17.9.4.1  12.9.18.3.8.10.5.
3. Doubtful signs the solver named:
   - 19 in SENDET: the second digit has a closed loop with a descending tail, the same 9 shape as in 9.8.13 (IHNEN) and 12.9 (MISCHKE). The 4s on the card (13.4.5, 9.4.1, 14) have an open, angular top. 9 is clear on the pixels, not only on word sense.
   - 12 in MISCHKE: the second digit has a flat base stroke, a clear 2, distinct from 9. Reading rests on the pixels.
4. Independent decoder. `review/work/indep_decode.py` uses my own transcription and two alphabets. The 25-letter
   alphabet without J gives the claimed text; the 26-letter alphabet gives `MARRNV / HEQYKICHEM GQTRY / REMDES IHMEM /
   FQIDA LIRCHJE`, so the J-less alphabet is confirmed by the text, not chosen arbitrarily. 44 numbers, all decoded,
   none left over; numbers used max 25.
5. Plaintext. "Herzlichen Grusz sendet Ihnen Frida Mischke" is standard German postcard phrasing of the period
   (sz for ß is common). "Gruss aus Nassow" fills the printed "Gruss aus" line with a place name. Nassow is a village
   in Kreis Köslin, Pomerania (today Nosowo), consistent with the Cöslin arrival postmark (13.8.06) and the plain
   address "Fräulein Anna Schulz, Köslin". Translations (English, Slovak) are correct.
6. Steganography / hidden writing. I inspected the stamp box on the address side (`review/work/stamp.png`): the 5 Pf
   Germania stamp is intact, nothing written around it or along the edges; the address side is plain Kurrent. The
   picture side has only the printed caption "Wie gerne dir zu Füssen." besides the number block. Writing under the
   stamp cannot be seen in a scan; the solver says so and claims nothing. (The note about hidden messages under the
   stamp concerns the Hungarian Jolánka series; this card is a German card from Pomerania and shows no sign of it.)
7. Sources. Portal status Not solved, no attached solution; SOLUTION.md credits all work truthfully to Claude Opus 5.5.

## Findings

1. (minor) `work/transcription.txt` omits the full stop the writer put after each word (e.g. "13.1.18.18.14.22.",
   "...5.13."). The two-space word gaps carry the same information, so the decryption is unaffected; one sentence in
   SOLUTION.md stating that word-final dots are dropped would make the transcription exact.
2. (minor) Register type: the cipher is plain number substitution (A1...Z25 without J), which in the allowed labels is
   `MASC`. Not `MASC + Steganography`: no hidden message is visible on this card.
3. (minor) SOLUTION.md gives the posting place as "Stolp (Bahnpost / Zug, 12.8.[06])". The partly covered postmark
   on the address side shows only "STOLP ... BAHN ... ZUG ... 12 8"; the year comes from the Cöslin arrival stamp.
   That is what the bracket implies, and it is acceptable.

## What I could not verify

- Whether anything is written under the stamp (cannot be seen in the scans).
- The surname Mischke and the recipient's street (Gärtnerstraße 5) cannot be checked against outside records; the
  surname is fully determined by clear numbers, so it does not affect the decryption.
- I did not run a web search for a published solution of this exact card; the portal attaches none and lists it as Not solved.
