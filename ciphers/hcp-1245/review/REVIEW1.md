REVISE

# Review 1 of HCP1245 (Claude Opus 5.5, reviewer, 2026-11-01)

The key, the transcription and 16 of 17 rows stand. One sign in row 7 is misread, and that misreading is what made the "weakest clause" (rows 6 to 9) nonsense. With the sign read as it stands on the card, the clause reads without emendation: *délről estére* "from noon to evening". The normalized text and the English and Slovak translations of that clause must be redone.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1245/work/decode.py` ran from the repo root. All four SHA-256 checks print OK, and the output matches the literal rows, `work/normalized.txt` and the SOLUTION.md text.
- **Independent decode.** `review/work/my_ledger.txt` is my own sign-class transcription of all 17 rows, made from my crops; `review/work/my_decode.py` has its own key table. It was not blind, because I had read the solver's text first. `review/work/diff_vs_solver.txt` holds the diff. The differences are:
  - my script does not separate d from h/p, so *hogy*, *szep*, *ha* print with d (expected, not a disagreement);
  - it prints no accents;
  - it shows my doubt about the opening of row 16;
  - row 7, the one real disagreement: **este** against the solver's **esze** (Finding 1).
- **Pixels.** I read every row on crops of `work/hires/...adr.jpg` (`review/work/a1`–`a5.png`). Enlarged: the *dél* word (`b1.png`), row 7 (`b2.png`, `b3.png`), the row 16 blot (`b4.png`), the stamp box (`b5.png`), the address (`b6.png`), a comparison sheet of every sz and t type (`cmp_st.png`), and the row 7 sign in its colour channels (`sign_row7.png`).
- **Key.** It is the HCP1216 family key unchanged and covers all signs except the row 16 blots. No value is invented for this card.
- **Context.** HCP1271 (16 March 1912, new workshop, Gyöngyöspüspöki) and HCP1244 (Gyöngyös home) fit. I checked the family for parallels: HCP1274 has *Sajnálattal kell tudatnom ... kénytelen vagyok*, which fits rows 4 to 8. The portal shows no solution, and the solution discloses this. I found no sign of a published text being used.
- **Picture side** (`review/work/verse.png`, rotated): printed verse only, no handwriting, as claimed. But see Finding 2.

## Findings

1. **Row 7, second sign is s + t, not s + z: read *estére*, not *ezér[t]* (major).** The ledger has `E ) Z E F E`. On `cmp_st.png` and `sign_row7.png` the sign is a bowl followed by a thick stem with a flat bar running right from its head. That is a gamma (t), heavily inked, like the gamma of *látszik* in row 12.
   - All the sz groups compared (rows 1, 2, 7 *leszek*, others) have a diagonal crossing the stem with an arm to the lower left. Here no arm crosses to the left of the stem, and paper shows between bowl and stem except where they touch at the top. The green channel shows no such arm.
   - The acute over the next e is a heavy, plain mark, and the row then continues r, e.
   - So the literal row is `este re | leszek kény`, i.e. **estére** "by/to evening". This needs none of the emendations the solver needed (*e-sz-é-r-e* → *ezér[t]*, with r+e for r+t). The family spells *este* normally (HCP1301).
   - The clause then reads: *sajnálattal kel[l] tudatni, hogy a levelei délről estére leszek kénytelen át[t]enni az írását*, "I must regretfully tell you that I shall be forced to move the writing of the letters from noon to evening."
   - The fix is `Z` → `T` in ledger row 7, plus SOLUTION.md (literal, Hungarian, English, Slovak, item 2), `work/normalized.txt` and NOTES.md. The claim "*ezér[t]* … a sense reading" and the inserted comma must go. The phrase "your letters [come?] from noon" is not on the card.
2. **The printed verse was not read, and it supports Finding 1 (major, disclosure and context).** SOLUTION.md dismisses the picture side as "only the printed verse". The verse is about writing a letter in the evening: "...ezt a levelemet / [es]tefelé hétkor, / [Sorr]entó előtt a nap leszáll. / [Rem]élem, hogy e pár sor írásom / [Te] édes, egészségben, / [jó] kedvben talál!" Its opening words sit at the left of the crop, so a full reading is still needed. Feri is playing on it: the printed lover writes "toward evening at seven", and he regrets having to move his letter-writing from noon to evening. Quote the verse in SOLUTION.md and use it in the case for the reading. This also explains the "playful" tone the solver noted without explaining.
3. **Status line and the "weakest clause" must be rewritten; `levelei` stays a small open point (minor).** After Finding 1 the clause is not "partly inferred", but the grammar is loose: *a levelei ... az írását* has a double object, and *levelei* formally means "his/her/your (Ön) letters" while the rest of the card uses *te*. Say this plainly. Give "the letters" in translation unless a reason is shown for "your". The English "your letters" is not needed for the sense.
4. **"The looped l settles it" is overstated (minor).** On `b1.png` the third Latin letter has a tall loop and then a low stroke that curls back toward the stem, closer to a b than the l's of *csokol* and *vesed* in the stamp box, which end on a rising tail. On shape alone *déb* is not excluded. What settles *dél* is *délről estére*. Change the argument in item 2 accordingly.
5. **Row 16: a candidate that fits the stroke order is missing (minor).** The solver's *enyém* does not fit, because the visible order is n-like strokes, e, then the y. The opening could be **m e ny e m**: blot plus two visible strokes = the three strokes of m; three bars = e; second blot with y descender = ny (two strokes under the ink, plus y); e; m. That is *menyem*, literally "my daughter-in-law", in older usage "bride". This is my hypothesis only and I do not claim it; the sense is not certain. Keep the word unread, as the solver correctly does, and list it with *nejem*.

## Register consequence

After Finding 1 only the one blotted word in row 16 is unread and the rest reads, so the card can count as complete under the run's rule. Before the fix it could not, because a whole clause lacked sense. Because the fix changes the normalized text and both translations of a whole clause, I recommend DONE2 for a short check of rows 6 to 9 only.

## Confirmed as disclosed

Plain Latin *t* (row 1), *dél* (row 6), *az* (row 8); two strokes over o in *-ről*; smeared n in *tudatni* (row 5); *kiny* (row 15); h/p and d/n calls by word sense; accents supplied editorially; *kel, atteni, mondja, mer* normalized; the crossed i in row 8 under the y descender; the stamp box as *csokol szamta lanszor hű ked vesed feri*. Spot checks of rows 1 to 5 and 10 to 17 agree sign by sign with the ledger.

## What I could not verify

- The word under the row 16 blots. Red and green channels did not help on the blot edge.
- *hű* in the stamp box: the ü dots coincide with print of the stamp indicia.
- The last address line was read with the family address as a guide; the HC Portal stamp and the ink overlap there.
- The day on the Gyöngyös postmark. The second strike's town name is only partly legible and I did not establish it.
- The first words of the verse, which I did not read in full.
- The historical point of moving the writing to evening (presumably the new work hours); nothing on the card states it.
