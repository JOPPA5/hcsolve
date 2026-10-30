ACCEPT

# Review 1 of hcp-1377 / pc_hcp_58 (reviewer: Claude Opus 5.5, 2026-10-30)

The reading stands: Caesar +1 (decrypt -1), 41/41 enciphered letters, "I am going to bike to Wimborne to-morrow, Sat. My N. & L. from your own E. L. girl." I tried to break it on BIKE, on the minim letters and on the date, and did not succeed. Only minor issues remain.

## What I verified and how

- `python3 -I ciphers/hcp-1377/work/decode.py`: hashes OK, output equals the table in SOLUTION.md, 41 letters. decode.py contains no plaintext; it only shifts transcription.json.
- Independent decode, `review/work/decode_independent.py`, ciphertext re-keyed from my own reading of the card, own translate table: same plaintext, 41 letters. Per-row count 10+6+8+10+7 = 41. Shift -1 is the only one giving English on `up npsspx Zpvs Hjsm` (all 26 tried).
- Pixels: rotated the un-converted original myself (`review/work/crops*.py`, `reading.png`, `seg0-4.png`, `z_*.png`, 4-8x) and read every token sign by sign, comparing with hcp-1386 `work/crops/band0, band5, nl, nz1`.
- `Wimborne` re-enciphers to Xjncpsof, and the card plainly has clear letters with a dotted i: not enciphered, as claimed. `Sat:` and `Friday` also clear.
- 6 Dec 1907 was a Friday (computed).
- Picture side: printed "Dyserth Waterfall" only, no handwriting. Portal status and absent attachments taken from source/metadata.md.
- Not in skip.txt or register-exclusions.json.

## Sign-level results

- `J bn hpjoh up`: agreed. h-p-j-o-h all visible; j is the long check-shaped stroke as in `Hjsm`. n of `bn` is u-like (disclosed).
- `Cjlf`: agreed, and the solver's key argument holds. In `z_row2a.png` the C body stands free; the hooked stroke beside it is separate; extended upward, its stem passes within a few pixels of the heavy dot (at 5x: stem projects to about x=690, dot at about x=655, y=85). So that stroke is a dotted j, not a G tail. The next stem is taller than the j, with a hairline foot running into a looped-descender f: l is acceptable though loop is thin. No competing English word: BIDE (`e`) does not fit the sign or the sense, FIKE/FIE are rejected. "Bike" as a verb is good 1907 English,. Disclosed honestly as sense-supported.
- `up npsspx`: agreed; two identical p with loop-and-bowl descenders, ss, x; no f inside.
- `Nz`: agreed; same form as hcp-1386 nz1.png.
- `N. & L.`, `E. L.`: agreed; the whole `N & L Gspn Zpvs` row is nearly stroke-for-stroke hcp-1386 band5. Kept literal, disclosed.
- `Gspn`, `Pxo`, `Hjsm`: agreed.

## Findings

1. **minor: heading "G" is stated flatly in the plaintext but is not established.** The heading sign here has the same construction (C body plus short stroke below) as hcp-1386 band0, which that accepted solution reads as "C. H."; the same sign cannot be G here and C there without a reason. The writer's enciphered G in `Gspn` is a different form, so it gives no support. Uncertainty 5 only half says this. Evidence: `seg0.png`/`seg1.png` against hcp-1386 `band0.png`. Fix: print "G. (or C.) H." or note the conflict plainly.
2. **minor: day of the postmark is more legible than stated, and not clearly a 6.** Upright crop `stamp_up.png`: arc WIMBORNE, a line 10 + smudge (time), then DE and a digit with a flat top and separate lower arc, which looks like a 5 at least as much as a 6. No year digit is legible. 5 Dec 1907 was a Thursday, so the plain "Friday" only agrees with the portal date if the digit is an incomplete 6. The solver rightly says the postmark does not prove the date, but "Why it is correct" then counts "Friday heading on a Friday date" as outside evidence. Fix: state the digit as 5 or 6 and weaken that sentence; the message reading does not depend on it.
3. **minor: undisclosed sign point in `Zpvs`.** The v has a closed eye with a long exit stroke (`z_pvs.png`), and is close to an o; literal `Zpos` = YONR. Hand comparison settles it (same form in hcp-1386 band5, read `zpvs`), and YOUR is certain, but Uncertainty 3 covers minims only. Fix: one line.
4. **minor: `J` of row 1 could equally be the writer's capital plain I.** Both give I, so the plaintext is unaffected, but the count would be 40. Fix: one clause, or leave as is.

## What I could not verify

- Day and year of the postmark (finding 2); the date rests on the portal.
- Meaning of N. & L., E. L., G./C. H.
- Absence of a published solution beyond the solver's statement and the portal capture; I did not search separately. The orchestrator's register check covers ai.hcportal.eu.
- The identity of the writer and the Wimborne link beyond the postmark.
