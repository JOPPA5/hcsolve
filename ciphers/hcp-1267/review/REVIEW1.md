REVISE

# Review 1 of HCP1267 (Claude Opus 5.5, reviewer, 2026-11-01)

The reading stands: this is a Hungarian MASC card in the Jolánka family key, Feri to Jolánka, about his new M.Á.V. brakeman job. It needs concrete fixes first. The ledger has four sign errors, and one of them changes the content: the time "7.10" in row 7 rests on one mark counted twice.

## What I verified and how

- **Command:** `python3 -I ciphers/hcp-1267/work/decode.py` ran. All four SHA-256 checks gave OK. Its output is in `review/work/cmd.txt`. All 27 main rows appear unchanged in the SOLUTION.md literal block, checked by script; the stamp rows were compared by eye.
- **Independent decode:** `review/work/indep.py` has a key typed from the HCP1216 table, not imported from `decode.py`. It decodes 736 enciphered signs in the ledger, none unmapped, and gives the same letters. So the key is consistent and covers the whole ledger. A letter-level diff of literal against `work/normalized.txt` shows only the disclosed spellings, doublings and h->p choices, plus the clear text.
- **Pixels:** I read every main row and the 8 stamp rows sign by sign from my own crops of the un-converted `work/hires/*_adr.jpg`: 2x panels `review/work/L0-4`, `R0-4`, `b1`, `b2r`, `st`, and 3-5x montages `hook`, `spots`, `sp2`, `z1`. I looked at each restoration: row 20 [g], row 23 [a], S3 [o], S6 [l], and S2 at the tear. I did not re-read the sender's clear address beyond what the overview shows.
- **Language and context:** the text is natural Hungarian of the period with consistent semi-phonetic habits, not words forced onto noise. The railway content holds together (Rendező, Keleti pályaudvar, pay by day, km and hour) and fits the clear line "Holecz Ferencz M.A.V. fekezo Rakos Palota". The neighbouring card HCP1266 (brakeman exam, move to Rákospalota, address to follow) fits it independently and is not cited by the solver. Sándor appears on HCP1216 as well. The translations are faithful.
- **Honesty:** no published solution is used, and the portal attaches none. Non-blind use of the family key is disclosed.

## Findings

1. **major: row 7, one mark is counted twice, so "7.10" is not established.** The ledger has `E:' ) "7" "10"`, and the literal text prints `leés 7 10`. The scan shows only dotted three bars, ONE hook, then `1 0` (`review/work/z1.png`, first panel of `hook.png`). There is no other mark between é and 1. The ledger uses that hook as both the s of *és* and the numeral 7. The hook has the same form as the s sign in rows 1, 9 and 12 (`hook.png`, panels 2-4). There are two possible readings:
   - (a) *és 10-re Rendezőn kellett lennem*: "and I had to be at Rendező by 10". This uses every mark with no dropped letter, and I prefer it.
   - (b) *é[s] 7.10-re*: the hook is a figure 7 and the writer dropped s. There is no other 7 on the card to compare it with.

   The fix is to remove one token from the ledger and normalize to one reading, with the other disclosed. Then correct the Hungarian, English and Slovak texts, the "clear figures" lists under Cipher type and under Why it is correct, and the NOTES claim that plain "7 10" gave the time sentence.
2. **minor: row 14, ledger A should be E.** After the b of *idő-be* the sign has three bars (`spots.png`, panel 1), so the literal is `idöbe`, not `idöba`. The ledger reads `6 A`. The normalization *időbe[n]* is already right.
3. **minor: row 5, ledger E should be A, and Uncertainty 13 is wrong.** The sign after l in *lapot* has two bars (`sp2.png`, panel 1). The literal is `lahot`, not `lehot`. Remove the statement "three bars where lapot has a". This was a false oddity in the writer's spelling.
4. **minor: row 9, one s too many.** The ledger has `V I ) ) Z A`, but the scan shows one hook between i and z (`sp2.png`, panel 3). The literal is `visza`, the same as *viszafelé* in row 24. The normalization *összevissza* stands, but Uncertainty 13 should list it among the writer's spellings.
5. **minor: the p shape is described too narrowly.** In *naponta* (row 17), *pályaudvar* (row 23), *megkapja* (row 26) and probably *kaptam* (row 25), the sign is short stroke + long stroke, the same shape as d here (*udvara*, *adja*: `b1.png`, `spots.png`). It is not the h shape, long stroke + short tick, which *Pestre* and *lapot* use. So p calls can also collide with d, and Uncertainties 8 and 9 should say so. Item 4 then looks less anomalous. No word changes.
6. **minor: row 25, undisclosed small insertion.** The m of *vettessem* is written small below the line between e and l (`b1.png`). The reading is fine, but the ledger should note it, since a row-by-row reader will not find the sign in line.
7. **minor: claim wording.** "kelet ×3" is correct for *kellett* only; the string occurs 4 times, counting *Keleti*. The statement that the ledger holds "one token per written sign" is not true until findings 1 and 4 are fixed.

## Points checked and accepted

- Row 15 `k?e?l` is correctly disclosed: S, a faint Latin-looking e, and a heavy wave that is partly overwritten. It is a lone word, and the clause reads without it. I have no better reading.
- `n?` (row 13), `az?t` (row 24), `lahot?` (row 26, r/t shape with a dot below), and `k?` at rows 26 and 27 (looped, row-initial): disclosed, and the word-sense calls are sound.
- Row 20: the blot has the outline of g, and y follows. Row 23: the top bar shows above the blot, and that blot could be a or e. The word needs a. The dot beside r in row 20 is the dot of the i in row 21, not a mark on r.
- Row 23 "2": it has a loop and tail and is less cursive than the clear 2 of row 17, but no letter sign fits. The numeral is acceptable as disclosed.
- Stamp rows: *Isten vele*, *édese…*, *bold[o]g*, *viszont*, *látásra*, *csókolja*, *imádója*, *Feri* all stand on the crop. Leaving S2 unrestored after the tear is right.

## Could not verify

- Whether the row 7 hook is s or 7, which is shape evidence only (finding 1).
- The postmark date. I only see "21", so 1913-07-13 is the portal's. The clear sender's address is unclear under the postmarks.
- That Rendező means Rákosrendező: context only, disclosed.

## Register

No entry blockers once finding 1 is resolved: the only un-understood item is one lone word, and the rest reads. Type MASC. hcp-1267 is neither skipped nor excluded by a check of `skip.txt` and `register-exclusions.json`.
