ACCEPT

# Review 1 - hcp-1057 (M. Zwick to his parents, Aulendorf, 12 July 1917)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-11-03.

## What I verified and how

1. **The solver's command.** `python3 -I ciphers/hcp-1057/work/decode.py` (from the repo root): all four source/hires
   hashes OK. The output matches the claimed plaintext line by line ("Hatte gerade nicht mehr die Zeit mich zu bedanken,
   da mußte Gefangene ich gleich ab holen mit einem Transport. Bis zur Stunde ist noch alles beim Alten. Sende
   nächstens einen Brif").
2. **Independent decryption.** `review/work/my_decode.py` builds the key only from pattern words (23727/23728 =
   einen/einem, b238 = beim, 16620 = alles, z59 = zur, 74ch = noch, T917sp49t = Transport, 85ßt2 = mußte), asserting
   no conflict, and then applies it to my own reading of all ten cipher rows. Result: the same key
   1-5 = a e i o u, 6-0 = l n m r s, no unmapped digit, no conflicting assignment, the same German text.
   92 digit signs in all (91 plus the dotted 1 = ä); every one decodes into an ordinary word.
3. **Sister card.** The FINAL-track sister hcp-1056 (same Zwick family) has exactly the same key, reached
   independently, and notes the same on hcp-910. Consistent.
4. **Transcription against the hires scan.** Crops in `review/work/` (r1-r5, z829, znicht, zlast, znebst, z1000b,
   zsend2, zsend34). I checked every cipher row sign by sign:
   - 829 (mehr): the middle 2 carries a long descending loop below the line (z829.jpg) - a Kurrent h fused with the 2,
     as the solver discloses. Reading is visible, not forced.
   - 73cht (nicht): end of the row runs over the divider line; ch and a short t are visible (znicht.jpg). The 3 is
     written with a nearly closed top, close to an 8, but "nmcht" is not a word; the call rests partly on sense
     (the solver does not single this one out - minor).
   - z23t, z5, z59: the first sign has the Kurrent z descender, clearly distinct from the small digit 3. OK.
   - 85ßt2: a u-bow stands over the 5, which agrees with 5 = u. OK.
   - S27d2, 71"ch0t270, 23727 B93f: read as transcribed (r4, zlast). The dots over 1 in 71" are clear.
   - B3s, Transport: plain Kurrent s as the solver says; the inconsistency (0 vs plain s) is real and disclosed.
5. **Plain parts.** Header "Aulendorf, den 12.7.17. Liebe Eltern! Habe Eure werte Postkarte mit Freuden erhalten,
   meinen besten Dank dafür." and closing are legible plain Kurrent and read as given. Address: Feldpost, Herrn
   Georg Zwick, Erbenschwang, Post Ingenried b. Schongau (Bay.) - OK.
6. **Steganography check** (the human's note about writing under stamps): the stamp box on the address side is the
   printed dotted frame (with "21352") and holds only the Aulendorf postmark; no stamp was ever affixed (Feldpost),
   so there is nothing under a stamp. The picture side (Aulendorf, Kirche und neues Schloss; Atelier E. Felle, Isny)
   carries no handwriting at all (pic_small.jpg). No hidden writing along the edges either. Type MASC is right.
7. **Language and context.** Natural 1917 German (dialect-tinged word order "da mußte Gefangene ich gleich abholen",
   spelling "Brif"); Ersatz-Bataillon 247 was a Württemberg reserve unit, Aulendorf is in Württemberg, POW escort duty
   fits. No published solution found by me either; the portal attaches none.

## Findings

1. **minor - closing number.** The closing number looks like 1 followed by four zero loops (z1000b.jpg), i.e.
   "10000 Grüße", not "1000". The strokes run together, so it is not certain; SOLUTION.md should say "1000 (or 10000)".
2. **minor - unread last word.** The plain word after B93f (znebst.jpg) shows n-like humps, a small e, a b-loop and
   tall strokes running above and below the line; "nebst" fits the strokes but leaves the sentence hanging. It is a
   single word, the sentence is complete without it, and the solver marks it as a guess - acceptable under the
   one-word rule. Keep it marked as uncertain in the report.
3. **minor - sender lines 3-4.** Two sender lines are partly under the postmark (zsend34.jpg, contrast-enhanced):
   line 3 begins with a Kurrent K, line 4 begins "zur Zeit" and ends in something like "...Kr./Kdo. 1". I could not
   read them either. They are address details hidden physically by the postmark, not message text, and the solver
   discloses them; the report should say so plainly.
4. **minor - the 3 in 73cht** is formed almost like an 8; add it to the list of calls that rest partly on word sense.

## What I could not verify

- The two sender lines under the postmark and the last plain word (see findings 2-3).
- The identity of M. Zwick beyond the card itself.

Conclusion: the key is consistent, covers every digit sign, the reading is visible in the pixels and is real German of
the period. Only minor wording/disclosure fixes remain.
