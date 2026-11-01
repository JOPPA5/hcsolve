ACCEPT

# Review 2 of HCP1245 (Claude Opus 5.5, reviewer, 2026-11-01/02)

The corrected clause in rows 6 to 9 stands on the pixels. Key, transcription and translations hold. One word in row 16 stays unread, as disclosed, and the rest of the card reads, so it counts as complete under this run's rule. What remains is minor. Three findings need small fixes before FINAL, and none changes the reading.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1245/work/decode.py` from the repo root: all four hashes OK, and the literal rows and normalized text match SOLUTION.md.
- **Independent decode.** My sign-class ledger and key table (`review/work/my_ledger.txt`, `my_decode.py`), rerun as `review/work/r2/my_out2.txt`, compared by `review/work/r2/cmp2.py` against the solver's current ledger with accents off and d/h merged: 16 of 17 rows identical. The only difference is row 16 sign 2, which I leave open (Finding 2). This ledger came from round 1 and was not blind.
- **Rows 6 to 9, sign by sign** on fresh crops of the hires address side (`review/work/r2/r6a, r6b, r7a, r7b, r8a, r8b, r9.png`, 2.4x):
  - Row 6: a l e v e l e i, plain *dél*, r, o with two strokes, l.
  - Row 7: e, bowl + heavy gamma, e with a thick acute, r e l e, s z e k, k e ny. The t stands: no arm crosses left of the stem, unlike the true sz three signs later.
  - Row 8: t e l e n, a with a dot above, t t e n i, plain *az*, i, r, a with acute.
  - Row 9: s, a with acute, t, full stop.
  - The ledger matches all of this.
- **Other rows:** 3, 12 and 14 sign by sign (`r2/r3, r12, r14.png`), 15 to 17 (`r2/r15, r16a, r16b, r17.png`). No disagreement.
- **Printed verse:** read on the solver's `work/verse.png`. The quotation is exact, including *elött*, *irásom*, *jo*.
- **Family claims, checked in their SOLUTION.md files:** *estére* (HCP1276), *sajnálattal kell tudatni* (HCP1273), *Sajnálattal kell tudatnom* (HCP1274), *enyémnek mondhatom* (HCP1292), Gyöngyöspüspöki as the new address (HCP1271). All present.
- **Sources and register:** 1245 is not in `register-exclusions.json`. The solution reports no published solution; I found no sign of one being used, but I did not search outside the repo.

## Findings

1. **Normalized text adds an unmarked *a* (minor, fix).** Row 14 has `bolondja ket` with one a (on `r2/r14.png`: inverted T, two bars, k). The normalized text prints *bolondja a két szép szemednek* without brackets, while every other editorial addition (*kel[l], át[t]enni, mondjá[k], mer[t], ki[csi]ny*) is marked and item 7 lists them. Either print *bolondja [a] két* or *bolondja két*, in SOLUTION.md and `work/normalized.txt`.
2. **Row 16: the family's own word is not among the candidates (minor, fix).** *reményem* "my hope" should be listed, ahead of the others. It is my hypothesis and should stay unclaimed.
   - Order: r, e under the left blot; m as the visible strokes plus a third under the blot; e; ny under the second blot with the clear y; e; m. This keeps every visible mark in place, as *menyem* does, and also uses the extra width of the left blot.
   - Sense: *ha te leszel reményem, szívem, éltem nem lesz borús*, "if you will be my hope, my heart, my life will not be gloomy". *Reményem* is Feri's standing term for her: *egyetlen reményem* occurs in 18 of the HCP12xx/13xx SOLUTION.md files.
   - Weak point: the fit is tight. The blot spans about x 137 to 290 in the hires scan, and r + e + one stroke of m normally need about 170 to 190 px. The two visible strokes are also a long and a short one, not two equal m strokes.
   - For the same reason the description "two strokes (n...)" and the `N` in ledger row 16 commit to more than is seen. My own ledger leaves that sign open. Mark it in the ledger as uncertain, as the text already does in words.
3. **Detached mark in row 6 is not disclosed (minor, fix).** A clear dot stands above the left arm of the v of *levelei* (`r2/r6a.png`, x about 840). It is not explained. It may be a displaced accent, and it does not change the word. Add one line to uncertainty 2.
4. **Slovak is looser than the Hungarian (minor).** *A szerelmes mind bolond* is "Zaľúbení sú všetci blázni", not "Zaľúbený je vždy blázon". The English has it right.
5. **Plain *dél* stays a sense call, correctly disclosed (no action).** On `r2/r6b.png` the third letter is closer to b than to the stamp-box l's. I considered *Debrő* (Feldebrő, Aldebrő, both near Gyöngyös), since the writer drops letters, but no sentence comes of it, while *délről estére* pairs directly and matches the verse. *Levelei* could also be *levelei[m]*, given this writer's dropped endings; the solver's "the letters" remains safe.

## Confirmed as disclosed

Double object and the *levelei*/*te* mismatch; i of *írását* tangled with the y tail above; smeared n in *tudatni*; *kiny*; the pencil hook; *te* address against the family's *Ön*; the reason for the change being unstated.

## Register consequence

One word alone is unread and the rest reads, so the card may take a register entry once the review is addressed.

## What I could not verify

- The row 16 word: the blots hide it, and no candidate is proved.
- *hű* in the stamp box, and the last address line under the stamp and portal mark (rechecked only on the overview, not sign by sign).
- The day on the Gyöngyös strike.
- Why the writing moved to evening.
