REVISE

# Review 1 of hcp-1163

Reviewer: Claude Opus 5.5, 2026-11-02. Round 1, solution by Claude Opus 5.5.

The Hungarian reading stands. I found no wrong word, and I confirm the plaintext, both translations and the coverage. The key as stated is wrong in one point: the claimed u/ü merger is not on the card. There are two separate signs. A few descriptive statements also need correcting.

## What I verified and how

1. Command. `python3 -I ciphers/hcp-1163/work/decode.py` ran. Hashes OK, 391 signs, reading matches the decode. Its output equals the plaintext in SOLUTION.md. The accented reading is hard-coded, but the script does compare it with the decode letter by letter, and the folding touches only accents and u/ü. It does not fold á/a or é/e.
2. Independent reading. I read all 23 rows from my own 2x panels of the hi-res scan (`review/work/panels.py`, `crops/p00` to `p41`), and typed them into `review/work/my_transcription.txt` with no word division. `review/work/check.py` compares them token by token and decodes them with its own key table. Result: 391 of 391 positions compared, row lengths equal, 4 differences. Three are finding 1. The fourth is the `5~l` the solver already disclosed, which I also read as l only by sense. My decode gives the same letters as the solver's in every row, except that it shows u where the solver's raw output shows ü.
3. Key. Every token is in the table, so the whole text is covered. No per-word exceptions exist in the script. The sister values hold: `1' 3, 9 1' 3` Árpád (hcp-1171, 1174), `7 1: 3 3. 1: 7, 1: 3` kedvesed (hcp-1173), `7. 1' 8 8, 1. 5, 1. 6, 7. 0 3,` számtalanszor (hcp-1172). New values rest on: `4.` 8 uses, `6` 2, `6.` 1, `2` 1, `4` 1. `6.`, `2` and `4` are single occurrences, each fixed by a word that leaves no alternative (enyém, cédulát, felelj).
4. Disclosed sign-level points, at 4x to 6x (`crops/l_udv.png`, `l2.png`, `u2.png`, `minden.png`, `imadod.png`). Blot in `lehetek`: dots show, reading fine. `téged` raised at the row end: correct, it overflows the row above and the rhyme needs it. Its 8 has a stroke running down into the 2. below, which is a fair `8,`.
5. Language and context. Fluent 1916 Hungarian, not words forced on noise: letter, two numbered couplets, a boxed quatrain with rhymes, closing formula. Recipient, signature and Szomolya/Bogács fit the Mezőkövesd family. 26 Feb 1916 was a Saturday, so "on Thursday" is two days earlier, which fits. English and Slovak translations are faithful.
6. Open parts checked: the date line, and the address except finding 2. `Szépreményű`: two dark marks stand above the final letter, so ű/ü is fair, though the postmark runs close by.
7. Sources. The portal status and absence of a solution are as metadata.md states. I saw no sign of a published solution used. hcp-1163 is not in register-exclusions.json or skip.txt.

## Findings

1. **major: the "u/ü merger" is false; the key lacks a sign.** The solver says `:1` stands for ü, u, ú and ű, and calls this "new evidence". The left-dot sign has two forms on this card, and they split exactly by phoneme (`crops/u2.png`, each at about 5x):
   - two left dots = ü/ű: `csütör` (row L1), `küldtem` (L2; the upper dot touches the flag of the 1, so it looks forked), `üdvözölve` (E2), `hűséges` (E2)
   - one left dot = u/ú: `cédu-` (L2), `tudom` (L3), `úgy` (V1)

   That is 7 of 7 consistent. In the three u cases the flag is clean and only the lower dot stands free. In `üdvözölve` and `hűséges` the two dots are unmistakable. The sisters attest `:1` only for ü, which agrees. The one sign needing care is `küldtem`, where the upper dot is merged with the flag; if the solver rejects that one the split is still 6 of 6 outside it.
   Fix: add a sign `.1` = u, ú; restrict `:1` to ü, ű; correct `work/transcription.txt` at L2, L3, V1; give `.1` its own entry in the decoder; remove the folding of u to ü from `norm`; rewrite the paragraph on the merger and the list of new signs (five, not four). Word readings do not change. The raw decode then gives `cédu`, `tudom`, `ugy` directly, which is a stronger result than the one claimed.

2. **minor: `Önagysága` should be `Őnagysága`.** The O carries two long parallel strokes (`crops/o.png`), and hcp-1174 has `Őnsg.` The script's open line and SOLUTION.md both need it.

3. **minor: uncertainty 1 names the wrong word.** The stroke rising towards the `5` of `üdvözölve` comes from the row below that row, E3, so it is the 7 of `kedvesed`, not of `hűséges` (`crops/l2.png`; hi-res about x 470, y 1945 to 1990). The 7 of `hűséges` is on the same row as the 5. Also, this stroke is the long tip of the 7, a shape it has elsewhere, so nothing shows a comma there. I would say plainly that the comma is not visible and the word is fixed by sense. Sense does fix it, and it is the only such sign.

4. **minor: the `:` after `gondolok` is probably not punctuation.** The two small marks stand in line with further dashes below them, and these run down into the solid right edge of the box around the quatrain (`crops/p31.png`). They look like the top of a dashed frame line. SOLUTION.md lists this `:` as on the card. Either drop that or mark it as doubtful. The stated punctuation in the plaintext is not otherwise affected.

5. **minor: undisclosed marks.**
   - `mindenséget`: a very small dot follows the 3 at the foot (`crops/minden.png`). If it counted as a sign mark, the key gives `3.` = v, `minvenséget`. It is far smaller than the writer's real dots, so `3` is the right call, but it rests partly on sense and should be listed.
   - `imádód`: a long thin stroke runs from under the last 3 up across the opening bracket (`crops/imadod.png`). It starts right of the 3 and has neither the place nor the hook of a sign comma, so I do not read `3,`, which would give no word. It may be a free comma or a slip. Not mentioned by the solver.
   - Dashed underlines under the `pecsétet` row, parts of `hűséges` and `(Árpád)`, and rule lines around the sections, are not mentioned. They look like ornament, and point 8 of the uncertainties should say so.

6. **minor: small factual slips in SOLUTION.md.**
   - `5 0 4.` occurs 4 times in all, so 3 more times in `hogyha`, not "4 more".
   - "30 distinct" counts the pseudo-token `5~l`. As transcribed the true count is 29. It becomes 30 again after finding 1, but for a different reason.
   - "with one sign not as seen" and the control claim hold, but the control list says `2` "nowhere else", so it gives no independent check for that sign; only `4.` and `6` recur.

## What I could not verify

- The HistoCrypt article the portal links; not checked by the solver or by me.
- The postmark date. I see Mezőkövesd rim letters and no legible date, as the solver says.
- The printed publisher's line. I read `Lepo...nd` at best, plus a triangle with 143; it does not bear on the message.
- Why the verses are numbered V and VI.
- Whether the one-dot `.1` also occurs on the sister cards. I did not check their scans; the solver should note this as a lead only and must not edit those directories.

## Register

After finding 1 is fixed, the card is complete in the sense of the run's rule: every word is read, and only one sign rests on sense alone. Type MASC is right.
