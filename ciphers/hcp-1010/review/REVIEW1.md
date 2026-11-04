REVISE

# Review 1 – hcp-1010 (reviewer: Claude Opus 5.5, 2026-11-03)

## Summary
The key (A–M without J = 1–12 ascending, N–Z = 25–13 descending) and the reading of the two upside-down lines and of the fence boards are confirmed on the pixels. The solution is not complete, though: the card has a fourth enciphered group, written on the brim of the young man's hat, which the solver did not see. SOLUTION.md says "every number on the card is used", and that is wrong. The reading that is there stands. The missing group has to be transcribed, decoded and disclosed before FINAL.

## What I verified and how
1. Solver command. `python3 -I ciphers/hcp-1010/work/decode.py` from the repo root: the hashes are OK, and the output matches the claimed plaintext exactly (A: `DeR BURScHE IST KÜHNER. HIER WIE SIE SEHEN.`, B: `WAS WIRD WoHL IM NÄCHSTEN MOMENT HIER GESCHEHEN.`, C: `VER BOT EN ER WEG`).
2. Independent decoder. `python3 -I ciphers/hcp-1010/review/work/decode_review.py` builds the key separately and runs on my own transcription. It gives the same A, B and C. It also decodes the hat-brim group (finding 1).
3. Transcription against the scan. I read work/hires/cpc_--_DE__DE_Hier__pic.jpg (3469×2298) with my own crops in review/work/:
   - Bottom lines, turned 180° (b0–b3.png, stamp_r/b.png). Every visible digit of A and B matches the transcription, including the umlaut strokes over 1 (nächsten) and the dark mark over 18 (kühner). The full stop after `21` (kühner) and the final stops are present.
   - Restorations. Each one is disclosed and plausible:
     - "Der": only a faint dot between 4 and 21. E is the only letter that fits D?R.
     - "Bursche": a 2 is visible inside the stamp's "O" and a `20` after the "F". The 1 of 21 and the 3 are under the stamp letters and cannot be seen.
     - "wohl": `16 2` is visible, then the stamp's "O", then `8 11`.
     These rest on word sense, and SOLUTION.md says so.
   - Fence boards (fence2.png, fence3.png, fence17.png). `2 24 19`, `5 25` and `5 21 16 5 7` are clear. In the first group, `5 21` is clear, but the first number is damaged at the board edge: it looks like `17` or `13`. 17 (V) rests partly on word sense (VER-botener). See finding 3.
   - Address side and stamp box (stampbox.png). The address is in plain Kurrent, and the stamp box holds only glue residue with no writing. I agree with the solver.
   - The rest of the picture: the girl's head and hat (girl.png), the boy's collar (collar.png: a row of five dots that are not digits, probably decoration or idle pencil dots), the foliage and the path. I found no other digits apart from finding 1.
4. Language and context. The German is grammatical and colloquial for around 1900 and fits the embossed scene (a lad courting a girl at a fence). Local delivery ("Hier, Rathskeller") is consistent with a short teasing note. No date or signature is visible.
5. Sources. No solution is attached on the portal. I found no sign that a published solution was used.

## Findings

1. **[major] Unreported ciphertext on the boy's hat brim.** On the picture side, on the brim of the young man's hat (hires about x 2300–2560, y 850–1180), there are pencil numerals. They read upright with the card turned 90° clockwise (review/work/hat_cw.png, hat5_r.png, hat_hp.png). My reading is `7 2? 18 20 2?`. The second group is `21` or `24`: its last stroke is crossed like this writer's 4, but it could be a hooked 1. The last group runs into the dark shading of the brim, and only its 2 is clear.
   - With 21, the group decodes to GRUS(S), i.e. "Gruß"/"Gruss", a natural closing.
   - With 24 it gives GOUS…, which is not a word.
   The solver's transcription, decoder and plaintext omit this group. SOLUTION.md claims "decodes all three passages with no leftover sign; every number on the card is used", which is false. The solver must:
   - transcribe the group (and state which digits are uncertain);
   - add it to work/transcription.txt and the decoder output;
   - give the plaintext and translations;
   - correct the "Why it is correct" claim;
   - describe it as a second steganographic placement.

   This group is a single short word (a greeting), and the rest of the card reads, so the card can still count as complete once it is handled. But it has to be handled.

2. **[minor] Orientation stated for the fence text.** SOLUTION.md and the transcription header say the fence group is read "with the card turned 90° clockwise". In my crops of the scan as published, the fence numerals are upright only after a 90° counter-clockwise turn (PIL rotate(+90), fence2.png). The hat-brim numerals are the ones that need a clockwise turn. Please correct the direction, or state which image orientation it refers to.

3. **[minor] First fence number partly rests on word sense.** The first sign of C is at the board edge and is smudged (fence17.png). It could be read as 13 (Z) as well as 17 (V). 17 is chosen because VERBOTENER is the only word that fits. Add this to the Uncertainties list alongside the stamp restorations.

4. **[minor] Clause boundary.** The point after `kühner` is on the card. "Der Bursche ist kühner. Hier, wie Sie sehen." and "… ist kühner hier, wie Sie sehen." are both offered. This is already disclosed and is fine. The English translation in the report should say that it follows one of the two readings.

5. **[minor] Register type.** `MASC + Steganography` is appropriate: the ciphertext is hidden on the fence boards and the hat brim as well as under the picture. This also agrees with the human remark relayed in this run that cards in this kind of series carry hidden messages in the picture. Keep that label once finding 1 is fixed.

## What I could not verify
- The digits under the HCPortal collection stamp (the 1 of 21 and the 3 in "Bursche", the 4 in "wohl"). Channel separation (R/G/B) did not lift the stamp ink, so these remain restorations.
- The exact last digit(s) of the hat-brim group, and whether a final 20 (second S) or another sign is hidden in the dark brim shading.
- Date, sender and place: there is no postmark and no signature, and the stamp has been removed.
