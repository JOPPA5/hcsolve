ACCEPT

# Review 1 of hcp-1100 (Claude Opus 5.5 as reviewer, 2026-11-03)

Verdict: **ACCEPT**. The card is a monoalphabetic substitution with invented signs and dots between words. The key covers all 226 enciphered signs. The plaintext is coherent English of 1908, and it agrees with the plain-letter "P.C's" and "from May" and with the address (Walrow is a real hamlet near Highbridge, Somerset). I found only minor issues. None of them changes the reading.

## What I verified and how

1. **The solver's command.** I ran `python3 -I ciphers/hcp-1100/work/decode.py` from the repo root. It printed "source hashes OK" and lines B01–B12 and T01–T04, exactly as given in SOLUTION.md.
2. **Independent decoder.** I wrote `review/work/indep_decode.py`. It has its own key table (letter → shape codes), asserts that no shape code maps to two letters, counts sign use, and lists unknown or unused codes. I ran `/usr/bin/python3 -I review/work/indep_decode.py work/transcription.txt` and saved the output to `review/work/indep_out.txt`. Result: 226 signs decoded, 0 unknown codes, 0 unused key codes. A `diff` against the solver's output was **identical**. 12 shape codes occur only once: amp, bar, bb, cq, cross, dx, el, eta, sq4, tri, vt, zh. Four of these are ordinary letters that happen to occur once (J, K, Q and the & sign). The rest are variant shapes, and SOLUTION.md discloses them.
3. **Transcription against the scan.** I made my own crops of `work/hires/*_adr.jpg` with `review/work/crop.py`, rotated 90° counter-clockwise for the body and 180° for the top lines and enlarged 1.5–4x. The crops are in `review/work/`: top.png, tese*.png, bodyA.png, bodyB.png, may1.png, b06may.png, b12than.png, b12start.png, b12end.png, treasure.png, b11*.png, rather.png, mother.png, amp.png, loosing.png, think.png, b04*.png, b06.png, stamp.png.
   - Whole body, compared line by line (bodyA, bodyB): the word groups and sign counts agree with the transcription in B01–B12, for example 7-b-C-h-b-λ-u DEAREST, X-□-9-b HOPE, -N-I-Ɛ-Ɛ WILL, ▶-□-V YOU, ∇-V-I-u-b QUITE, X-C-9-9-▶ HAPPY, -N-□-V-Ɛ-7 WOULD, P-I-ſ-b GIVE.
   - **MAY (four times).** B01 has three separate signs: a hook with a bar, a thin "(" arc, and a Y pennant. MOTHER (B09) and MUST (T01) show the hook-with-bar sign alone as M. The "(" arc is A in THAN (B12). So the literal M-A-Y is correct. Reading it as "my" is an interpretation, and the solver says so.
   - **TESE (T03).** The group is u, b, then the S sign with its lower-left foot, then b, then the word dot. There is no H sign. The blob I first took for a dot is the foot of the S. TESE is as written.
   - **RATHER (B11).** The signs are hooked h, Γ-hook, u, X, b-like loop, h: R A T H E R. Four to five signs follow, crossed through with one heavy stroke. Their shapes suggest a false start of THAN, but they are struck out, and the solver neither decodes nor counts them. That is correct.
   - **TREASURE (B12).** I count eight signs: d-loop with crossbar, hooked h, b, C, S-stroke, V, hooked h, loop-e. This fits T R E A S U R E. The first sign (dx) is a single-occurrence T variant resting on word sense. This is disclosed.
   - **LOOSING (B06).** The fourth sign is the stroke-with-tick S. It is not the Л (K) sign, which appears in THINK. The solver's correction in NOTES.md is right.
   - **LINE (B02)** shows the η variant. AND shows the angular C. The & in B04 is a looped d-like sign standing alone. Unlike the other words, it has no word dot after it. It is still a natural "well & happy".
   - **Top lines (180°).** "I. MUST. SAY. TA. TA." / "WITH. LOVE." / "I. HAVE. A. SET. OF. TESE. P.C's" and "from May" in plain letters. All of these are confirmed.
4. **Stamp and picture side.** The ½d Edward VII stamp (stamp.png) is intact, and no ink is visible at its perforations or in the dotted stamp box. The picture side carries only the printed title and verse. I saw no steganographic or hidden writing on either side. The type label **MASC** is correct, and nothing seen supports "MASC + Steganography" for this card. (The team's note about stamp-box steganography concerns the Árokszállás/Jolánka series, and this card is not part of it.)
5. **Published solution.** The solver's search is recorded in SOURCES.md. I found nothing in the repo or in the notes that suggests the solver used a published solution. No sister card exists in the repo.

## Findings

1. **minor – the "under the stamp" claim is too strong.** SOLUTION.md says "nothing is visible around or under the stamp edge". A scan cannot show what lies under a stamp that has not been lifted. It should say "nothing is visible at the stamp edges; the area under the stamp could not be inspected". This matters because the team has found hidden messages under stamps on another series.
2. **minor – many shape variants rest on word sense.** 36 shape codes serve 23 symbols. Eight of the variants occur only once (cq, eta, sq4, bar, dx, vt, zh, bb). Each fits its word, and the core sign of every letter is attested several times in independent words. The bulk reading does not depend on these variants. SOLUTION.md lists them under Uncertainties 1, apart from bb (FEEL), which the table names but the single-occurrence list omits. Please add bb to that list for completeness.
3. **minor – the "&" sign has no word dot.** Every other word ends with a dot, and the ∂-like sign in B04 does not. This is consistent with a logogram rather than a letter, and it supports the solver's reading. It could be mentioned in Uncertainty 2.
4. **minor – the solver's "Γ-like hook" A (gam) and the "(" arc A (arc) look alike.** In THAN the arc has a small hook at the top, so it resembles gam. The two codes may be one A shape drawn with more or less hook. This does not affect the plaintext.

## What I could not verify

- What lies under the stamp: the scan cannot show it.
- The four to five struck-out signs at the end of B11. The strike-through obscures them, and like the solver I do not decode them.
- The exact name of the publisher in the imprint, which is partly covered. It is not relevant to the cipher.
