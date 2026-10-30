# HCP 1377 / pc_hcp_58 — Caesar (+1) English postcard to W. Abbott, 6 Dec 1907

Status: **whole message read (41 of 41 enciphered letters); review 1 verdict ACCEPT, four minor findings addressed, no decoded letter changed.** Two abbreviation groups are kept literal; the first word of row 2 has one disclosed sign-level point (see Uncertainties).

## Origin

HC Portal cryptogram 1377 (`pc_hcp_58`), portal status *Not solved*, no attached transcription or solution, date 1907-12-06, language Unknown, recipient "W. Abboú" (catalogue spelling); see `SOURCES.md`, `source/metadata.md`. No published solution of this card was found or used.

Picture side: printed "Dyserth Waterfall" (Valentine's Series on the address side); no handwriting seen. Address side: plain **Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon**; halfpenny Edward VII stamp; circular postmark reading WIMBORNE, a time line with 10, DE and a day digit that may be 5 or 6 (`work/stamp_up.png`), no year legible, so the postmark supports the month and place but does not prove the portal date. The message is on the left of the address side, turned 90° counter-clockwise (`work/reading.png`). 6 December 1907, the portal date, was a Friday, consistent with the plain heading and with the plain "Sat:" for "to-morrow"; 5 December 1907 was a Thursday, so the heading agrees with the portal date only if the digit is an incomplete 6.

Same recipient, hand and key as the FINAL cards hcp-1386 etc.; the key was tested on this card rather than assumed.

## Cipher and key

Caesar substitution: each plaintext letter is written as the **next** letter of the alphabet (decrypt −1, A→Z). Only part of the text is enciphered: the heading, the place name, the day and the initial groups are in clear.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Transcription and plaintext (all writing in the message block)

| Ciphertext (brackets: not enciphered) | Plaintext |
|---|---|
| [G. (or C.) H. Friday.] | G. (or C.) H. Friday. |
| J. bn. hpjoh up. | I. AM. GOING TO. |
| Cjlf up. [Wimborne] | BIKE TO. Wimborne |
| up. npsspx. [Sat:] | TO. MORROW. Sat: |
| Nz. [N. & L.] Gspn. Zpvs | MY. N. & L. FROM. YOUR |
| Pxo. [E. L.] Hjsm. | OWN. E. L. GIRL. |

English: *"G. (or C.) H. Friday. I am going to bike to Wimborne to-morrow, Sat. My N. & L. from your own E. L. girl."*

Slovak: *„G. (alebo C.) H. Piatok. Zajtra, v sobotu, idem na bicykli do Wimborne. Moje N. & L. od tvojho vlastného E. L. dievčaťa."*

(English is the plaintext language. "N. & L." and "E. L." are left unexpanded in both versions, so those groups are not translations.)

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1377/work/decode.py
```

It checks the SHA-256 of the two `source/` scans and the two `work/hires/` originals against `SOURCES.md`, decodes every enciphered token of `work/transcription.json`, tests the inverse round trip, and prints the plaintext and the letter count (41).

## Uncertainties

1. **`Cjlf` = BIKE, the least secure word.** Crops `work/crops/cjlf.png`, `cjlf2.png`. The first sign is a C body; this writer's heading G is built on the same body plus a tail, and the next stroke here is a descender with a hooked foot. I read that stroke as a separate **j**, not as a G tail, because the dot lies on the extension of its stem (a slanted hand's dot for j). Read as G it would give FIKE (or, dropping the j, FIE), neither of which fits. The `l` is a short looped stroke, not much taller than its neighbours, followed by an f with a looped descender. The reading is thus chosen partly by sense: C and the l are the two signs that the word decides as much as the pixels do.
2. **`N. & L.` and `E. L.`** are initial groups kept literal, as on sister cards hcp-1386 and hcp-1403 (signs compared with hcp-1386 `work/crops/nl.png`). Their meaning and whether they are enciphered are undecided (shifted values would be M. & K. and D. K.). The middle sign of `N. & L.` is an ampersand-like form. The `L` of `E. L.` has a small foot and could be argued as another form; I follow the matching sister sign.
3. **Minim letters.** Final `n` in `bn` and `Gspn` has a form close to u (`work/crops/n_end.png`, `bn2.png`); literal `bu`, `Gspu` give AT, FROT, which do not fit, and hand comparison with `Nz`-type cards supports n. `z` of `Nz` is the same short hooked form as on hcp-1386 (`nz1.png`). The `v` of `Zpvs` has a closed eye with a long exit stroke and is close to an o (literal `Zpos` = YONR); the same form is read `zpvs` on hcp-1386 band5, and YOUR is certain. The `J` of row 1 could equally be the writer's capital plain I; both give I, but the enciphered count would then be 40.
4. **`npsspx`:** the second tall sign is one p (same loop-and-bowl construction as the first p of the word), not f + p.
5. **Clear words.** "Wimborne" reads directly in clear letters (its cipher form would be Xjncpsof) and matches the postmark. "Sat:" is in clear as well. The heading initial is not established: the sign is a C body with a short stroke below, the same construction that hcp-1386 reads as "C. H.", and it differs from the writer's enciphered G in `Gspn`, so that G gives no support. It is printed as "G. (or C.)".
6. **Postmark:** day digit 5 or 6, year illegible (see Origin). The date rests on the portal; the reading of the message does not depend on it.

## Why it is correct

One fixed shift turns all 41 enciphered letters into English, with no adjustment by word. The sense fits evidence that the cipher does not supply: "to-morrow" next to clear "Sat:", which agrees with the clear "Friday", and Wimborne in clear as the post town on the postmark. Friday also fits the portal date, but the postmark does not independently confirm that date. The close repeats the couple's formula on FINAL sister cards ("My N. & L. from your own E. L. girl", hcp-1386). The one word that depends on interpretation is disclosed in Uncertainty 1; removing it would not affect any other word.

## Credits

Capture by Claude Opus 5.5 (orchestrator) 2026-10-30; transcription and decipherment by Claude Opus 5.5 as solver, 2026-10-30. No earlier work on this number. The key was first found on sister cards of this correspondence (see their SOLUTION.md for their credits).

## Response to review 1

Verdict ACCEPT. All four findings were minor; all accepted. No decoded letter changed.

1. **Heading "G" not established: fixed.** Compared on `review/work/seg0.png` and hcp-1386 `work/crops/band0.png`: same construction, and the same sign cannot be G here and C there without a reason. `work/transcription.json`, the table and both translations now give "G. (or C.)"; Uncertainty 5 says why.
2. **Postmark day: fixed.** On my own crop `work/stamp_up.png` (`work/stamp.py`, same box as the reviewer's) the digit after DE has a flat top and a separate lower arc, so it may be 5 or 6; no year. Origin, Uncertainty 6 and "Why it is correct" now say so, and the Friday heading is no longer counted as outside confirmation of the date.
3. **`v` of `Zpvs`: fixed.** On `review/work/z_pvs.png` the sign is close to an o. Disclosed in Uncertainty 3 with the hand comparison.
4. **`J` possibly a capital plain I: fixed.** One clause added to Uncertainty 3; the plaintext is the same either way. The count stays 41 under the stated reading, 40 under the alternative.

`python3 -I ciphers/hcp-1377/work/decode.py` was re-run after these changes: hashes OK, 41 letters, enciphered rows unchanged.
