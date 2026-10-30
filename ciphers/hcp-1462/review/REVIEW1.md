ACCEPT

# Review 1 — hcp-1462 (pc_hcp_143), reviewer Claude Opus 5.5, 2026-10-30

## What I verified and how

1. **Solver command.** `python3 ciphers/hcp-1462/work/decode-full.py` (run from the repo root with `-I`): the source hashes match, all 9 lines round-trip, and it prints
   DearRalph / Thisisthechurch / Iamgoingtothis / evening / Pleasewritesoon / Iwilldosotomorrow / YrsSadie / WenttoEastwood / thismorning (110 letters). This matches SOLUTION.md exactly.
2. **Independent decryption.** I wrote `review/work/mydecode.py`, my own outside-in reader (first, last, second, second-last, …, restarting on each line). Run on `work/transcription.txt` it gives the same 9 lines and 110 letters. The key is one rule with no parameters, and it covers every cipher letter on the card. Nothing is left over and no letter is moved by hand.
3. **Transcription against the scan.** I made my own enlargements of `source/address-large.jpg` in `review/work/`, at 4x (autocontrast) and 7–8x (blue channel). They are `l1_2.png`, `l1end.png`, `l2start.png`, `l2mid.png`, `l3_4.png`, `l5_6.png`, `l6mid.png`, `ring.png`, `l7.png`, `pscol.png`, `l8E.png` and `l9n.png`. Line by line:
   - L1 `DaRlhpare`: `DaRlhp` is clear. `a r e` is faint under the grey W but visible as three pencil signs.
   - L2 `Tiitehrhcuchssh`: the first sign is a cursive capital with a descender loop, and it fits T. `iit`, `ehrh` and `chssh` are clear. The 10th sign is a heavy, apparently retraced u-shape. With two u's the line gives "Thisisthechuruhc", so the route rule requires one letter here. That reading is disclosed.
   - L3 `Imonttishogiga` and L4 `eeignnv`: these are clearly legible and agree with the transcription.
   - L5 `Peswieonostreal`: this is legible. The final `l` is tall and the "cross-stroke" below it is part of the grey overlay symbol row, as the solver says.
   - L6 `Iiloooorwormtsdlw`: I see `I i l o . o o`, then a large S-shaped form, then a small r-hook, then `w o/a r m t s d l w`. On the blue channel the upper part of the S stays the grey of the overlay, while its lower bowl is as dark as the pencil. The solver's reading (an overlay S with a pencil `o` over its lower bowl) is plausible, and it is the only reading that gives 17 letters. It is still the weakest point, and it is disclosed as such (uncertainty 6).
   - L7 `YsaiedSr`: clear. The last sign has a tall stem, but it matches this writer's `r` in L9 ("tim r ign"). Reading it as `h` would give "YhsSadie".
   - L8 `WntEswodotaote` (after a clear "P.S."): `Wnt` is clear and the 4th sign is a cursive E. The end of the line, `taote`, is faint. Both points are disclosed.
   - L9 `timrignnosh`: see finding 1.
4. **Language and context.** The plaintext is natural Edwardian English: "Dear Ralph, This is the church I am going to this evening. Please write soon. I will do so tomorrow. Yrs Sadie. P.S. Went to Eastwood this morning." The picture side is Prittlewell Church, and Eastwood is a parish next to Prittlewell (Southend, Essex). The address is R. E. Holmes Esq, Tottenham, so "Ralph" fits the initial R. The stamp is a ½d Edward VII, so the card dates from 1902–1910. Everything fits.
5. **Sources and honesty.** The portal status is "Not solved" and there is no attached solution. I found no use of a published solution. Credit is split truthfully between the earlier GPT work and the Claude completion. All restorations are listed under "Uncertainties".

## Findings

1. **minor — L9 8th sign "n" is partly a context reading.** At 8x (`l9n.png`) the sign after the first `n` is narrower and more cramped than the 7th, with a small extra stroke. A literal "m" (the earlier "morming") cannot be excluded on the pixels alone. Saying it is "two humps, same as the 7th" overstates the case a little. SOLUTION should say that n is preferred because of the sense, with m possible as a slip of the pen. The reading "this morning" stands either way.
2. **minor — the "printed wheel" is a portal watermark.** The large alphabet wheel with a building-and-padlock logo appears on *both* scans, picture side included (`source/picture-large.jpg`). It is the HCPortal overlay, not something printed on the postcard. SOLUTION uncertainties 1, 2, 3, 5 and 6 call it "printed". This should be corrected, because it matters to a reader who wonders whether the writer used a cipher wheel. It does not change any reading.
3. **minor — the picture-side note can be read a little further.** In the bottom margin (`pic_a.png`, `pic_b.png`) the note looks like "I hope you will u[nderstand?] … mess[age?] … Sadie". SOLUTION has "I hope you will …". This should be noted as a tentative fuller reading, or left as is with the "mess…" fragment mentioned. It is plain text, not ciphertext.
4. **minor — the link to hcp-1460 is stated too strongly.** hcp-1460 is addressed to Miss Ovington, South Tottenham, opens "Dear Sadie" and is signed by someone else. The shared scheme and the Tottenham addresses make it plausible that the two cards come from one circle. "The other side of the same correspondence" is still an inference, and the report should present it as one.

## What I could not verify

- The postmark date: the cancellation over the stamp is not legible in this scan.
- Who Sadie and R. E. Holmes were.
- Whether the top-left pencil mark "Bssn"(?) belongs to the message. I believe it does not, because it is not needed for the route and all 9 cipher lines are complete without it.
- The L6 pencil `o` over the overlay S cannot be fully separated from the overlay at this resolution. I accept it because of the dark lower bowl and the fact that the route rule forces this letter.
