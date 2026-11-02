ACCEPT

# Review 1 of hcp-1140

Reviewer: Claude Opus 5.5, 2026-11-02. Round 1. Only `review/` was written.

## What I verified and how

1. **Command.** `python3 -I ciphers/hcp-1140/work/decode.py` runs, the hashes of all 4 scans pass, and its output matches the plaintext in SOLUTION.md word for word.
2. **Independent decode.** `review/work/indep.py` holds my own sign-by-sign reading, typed from my crops rather than from `decode.py`, in card rows. It gives 125 signs and 22 distinct signs. All 22 are in the key and none of the key is unused. It decodes to the claimed text, with `hik ekt` where the solver reads `hisz eszt`, and with `kedres` in the second salutation.
3. **Transcription against pixels.** I read all ten cipher rows (header, rows 3 to 8, last line) from `work/hires/*_adr.jpg` at 2x to 7x with contrast enhancement (`review/work/crops2.py`), not a sample. Marks that change the letter were checked individually: 3 / 3, / 3., 5 / 5,, 6 / 6,, 7 / 7, / 7., 8 / 8,, 1 / 1. / 1: / 1' / .1 / 1,. I agree with every sign in the SOLUTION.md ciphertext block.
4. **Restorations, one by one.**
   - `hisz eszt` (`z7h.png`, `z7e.png`): both 7s have no dot, as disclosed. Sense reading, clearly labelled. `5 1 7` for `hisz` also stands in the ciphertext of hcp-1152, line 3, by the same writer, and `aszt` for azt on hcp-1151, 1154 and 1161 supports the spelling. No competing reading of `hik ekt` was found, and the sentence is good Hungarian with it.
   - `Kedres` (`a3L.png`): the comma under the second 3 is unmistakable. It is kept as written and disclosed.
   - Header `Margitkám` (`over2.png`): the 3 and 4 overlap, and the dot of `1.` is a blot. A short comma stroke at the foot of the 3 and the 4's comma can both be seen, as claimed; the former is merged with the 3's tail. The word is the same as in row 3.
   - `.1` (`dot4.png`, `a7L.png`): a round dot left of the 1 in both places. On row 4 it is clearer than the solver says, so the `így` alternative in uncertainty 4 is not needed.
   - End of row 5, `7.` past the margin line (`end5.png`): the dot is clear.
5. **Open text.** All verses, the greeting, the closing line and the address were read from crops (`v1`, `v2`, `o1`, `o2`, `t1`, `t2`). `maradtam` was also read on the red channel to suppress the olive print (`marad_r.png`): m-a-r-a, then the writer's `ol`-shaped d, then a clearly crossed t and `am`. The middle is cramped, as disclosed. The word is read and stands alone.
6. **Date and place.** `XII/10` is written with an overbar on the X. The year is 1915 with a looped 5. The postmark gives MEZŐK… 915 DE, with the day illegible.
7. **Key.** The values agree with the FINAL tables of hcp-1174 and 1179, plus `.1` = u, `4.` = gy and `6` = j, which also stand on hcp-1152. No value was set from this card alone. Coverage of the cipher signs is total.
8. **Language and fit.** The plaintext is natural Hungarian, and the spellings and themes fit the writer (the complaint that she does not write; `elviselni hisz` on hcp-1161). The English and Slovak translations are accurate. Sz. A., Sziber Margitka, Szomolya, u. p. Bogács all fit.
9. **Sources.** No sign of a published solution being used. The HistoCrypt article not being checked is disclosed.

## Findings

1. **minor: silent doubled letter in the open greeting.** The first open line ends `üdv-` with a hyphen (`udv.png`) and the next begins `vözöllek` (`udv2.png`), so the card appears to have `üdv-vözöllek`. SOLUTION.md prints `üdvözöllek` without comment, though it says the writer's other slips are kept or noted. Note it in Uncertainties.
2. **minor: `ú` versus `u`.** SOLUTION.md gives `.1` as "u, ú". hcp-1152 separates `.1` = u from `-1` = ú, so the card as written has `ugy`, `ugysem`, and `úgy` is the normalised form. SOLUTION.md should say so. It should also cite hcp-1152 (and hcp-1168, its source for `.1`) in support, since it presents the sign as established only here. It is still true that no FINAL table lists it.
3. **minor: sign count mismatch.** SOLUTION.md says 22 distinct signs; `decode.py` prints 23, because it counts its internal token `7~sz` as a sign. The correct number on the card is 22.
4. **minor: uncertainty 4 is overstated.** The row 4 dot is clear at 6x (`dot4.png`). The `így` alternative can be dropped or weakened.
5. **minor: undisclosed marks.** Thin diagonal strokes run down the right of the second verse, next to `Sz. A.`, and rule lines separate the sections, with a `>`-like curve at the right end of the `dalt` line. Row 8's `>` and the closing `)` look like the same kind of mark. They carry no text as far as I can see, but SOLUTION.md mentions only some of them.
6. **minor: register entry.** When it is written, the type label is MASC. The `hisz eszt` and `Kedres` notes should carry into the report.

## Could not verify

- The HistoCrypt article linked by the portal was not read, by the solver or by me, so I cannot say whether it covers this card.
- Whether the verses are printed or the writer's own.
- The postmark day, and the meaning of `>` and `)`.
- The reading of `maradtam` is partly leaned on hcp-1170, itself not FINAL; the pixels here support it but do not settle every letter.
- `hisz eszt` rests on sense; pixels alone give `hik ekt`.
