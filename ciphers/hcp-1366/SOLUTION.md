# HCP 1366 / pc_hcp_47 — Caesar (+1) love postcard, 19 July 1907

Status: **whole message read; review 2 verdict ACCEPT, its minor findings addressed (no word changed); closed.** Two closing groups are kept literal (see Uncertainties).

> **My own loving boy, no time to send letter. Love & Lt.. from your own M. h. girl.**

## Origin

HC Portal cryptogram 1366 (`pc_hcp_47`), portal status *Not solved*, no attached transcription or solution (`SOURCES.md`, `source/metadata.md`). No published solution of this card was found or used; my only search was the repo and the orchestrator's register check.

Picture side: printed view "Royal Baths, Harrogate", no handwriting. Address side (Boots "Pelham" Series): halfpenny Edward VII stamp, postmark WIM... (only those three letters are firm and the next is damaged; WIMBORNE is taken from sister cards), 10 PM, JY 19, 07, agreeing with the portal date 1907-07-19. Addressed in clear to Mr. W. Abbott, Stokelake Farm, Chudleigh, Devon (portal spelling "W. Abboú"). 19 July 1907 was a Friday, matching the plain heading. The message fills the left half and is read after rotating the scan 90 degrees anticlockwise. Same hand and same Harrogate postcard use as hcp-1371, written three days later.

The plain "No. 1." is the first of two cards: companion hcp-1363 has the same date and postmark time and is headed "No. 2." Nothing more than that pairing is claimed.

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet. Decrypt by subtracting one.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

The key was taken as a hypothesis from the sister cards and confirmed here: it gives English for every word with no per-word adjustment. The heading "G. H. Friday." and the underlined "No. 1." are ordinary writing.

## Transcription and plaintext (all ciphertext on the card)

| Line | Ciphertext | Literal plaintext |
|---|---|---|
| plain | G. H. Friday. / No. 1. | (not enciphered) |
| 1 | Nz. Pxo. Mpwjoh Cpz.. | MY OWN LOVING BOY |
| 2 | Op. ujnf. up. | NO TIME TO |
| 3 | Tfoe Mfuufs | SEND LETTER |
| 4 | Mpwf. & Lt.. | LOVE & [Lt..] |
| 5 | Gspn. Zpvs. Pxo | FROM YOUR OWN |
| 6 | M. h. Hjsm | [M. h.] GIRL |

`Cpz` is the end of line 1, set higher because the line had reached the card edge. 51 enciphered letters, all decoded by the one key; 4 letters of abbreviation groups kept literal.

English (the plaintext language; the portal lists Unknown): *"My own loving boy, no time to send letter. Love & Lt.. from your own M. h. girl."*

Slovak: *„Môj vlastný milujúci chlapec, nemám čas poslať list. Láska & Lt.. od tvojho vlastného M. h. dievčaťa."*

The groups are left unexpanded in both versions. Punctuation in the sentences is editorial.

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1366/work/decode.py
```

It checks the SHA-256 of the files in `source/` and `work/hires/`, decodes every token of `work/transcription.json`, checks the inverse round trip and prints the plaintext with the letter counts. It decodes a manual transcription made from the pixels, not the image itself. Crops are in `work/crops/`; `work/compare.py` builds `work/crops/cmp_mpwjoh.png` (it needs PIL and reads crops from hcp-1361 and hcp-1367).

## Uncertainties

1. **`Mpwjoh` (line 1; `crops/cmp_mpwjoh.png`).** The ink is partly pale, and the w ends in a dark stroke that does not visibly run into the j, as it does on hcp-1361 and hcp-1367. The j foot is an open left hook, as in `ujnf` and `Hjsm` on this card, and unlike the closed loop of f in `Mpwf` and `ujnf`. hcp-1361 has a straight tail, while on hcp-1367 the j's foot also hooks where it meets the C below, so that sister is closer than first stated. This j has no dot: the dark stroke above it is the foot of the p of `Cpz`. `Hjsm` has none either, so this is a habit of the hand, while the j of `ujnf` does have its dot. The o is a pale lens, and the h is the rise, sharp turn and fall to a blob. The rejected readings are in the Response to review 1 below.
2. **`Cpz` (upper right; `crops/top.png`).** The z is pale, with the dark dash at its foot. The same z, looking like a 2, follows `Cp` on hcp-1367. The two dots after it are read as punctuation or blots.
3. **`& Lt..` (line 4; `crops/kiss.png`).** Hooked looped capital L, then a c-like stroke with a short dash at its top right, then two dots: the same group as `& Lt..` on hcp-1371. The small sign is read as t by that parallel; c or r are not excluded. Shifted it gives "Ks", and "Love & Ks" might mean love and kisses. That is a hypothesis, not a reading, and the plaintext does not use it. The "&" is the ordinary looped form here.
4. **`M. h.` (line 6; `crops/ml.png`, last rows of `crops/cmp_mpwjoh.png`).** The first sign has three downstrokes like the M of `Mpwf`, against two in the N of `Nz`, and it matches `M-h` on hcp-1367. N stays possible, and hcp-1371 was transcribed `N.` in this slot. The second sign is a tall stroke with a short hump: h rather than L. Kept literal because this is a formula slot and neither reading is proved. Shifted: L. g.
5. **`Mfuufs` (line 3; `crops/letter.png`, `letter2.png`).** The ink runs out mid-word: u u and the f are very pale, and the upper part of the f shows two pale forms, a closed arch beside the second u and a separate c-like curl, with a long faint stem and looped foot. Three small black blots sit along the baseline between the second u and the final dark s. I take them as blots from a failing or recharged pen, not as signs, but cannot prove it. Six letters are read as the best count, not a proved one; the sign order fits LETTER and the same word on hcp-1371.
6. **`Tfoe` (`crops/send.png`).** The o is a squeezed dark stroke with no counter. N in its place gives no word. The f descender runs into the M of line 4; they are separate words.
7. **`Pxo` (line 1; `crops/w1.png`).** The o is a filled blob, as on hcp-1371; the same word is clear in line 5 (`crops/yown.png`). No separate dot follows it.
8. **`up` and `ujnf` (line 2).** This hand's u has an arch and looks like n; sister cards read it as u (`uibolt`, `Up`). Read as n, the words would be MO and MIME, which make no sentence, so the context decides. The j in `ujnf` is the slash with a hooked foot, with its dot clear above.
9. **`Hjsm` (`crops/hjsm.png`).** H, hooked slash j, large looped s, and a flattened m, as on sisters. Separator dots are kept only where seen.
10. **`Zpvs` (line 5; `crops/yown.png`).** The last sign is a small c- or r-shaped hook, unlike the large angular s of `Mfuufs` and `Hjsm` and closer to the e of `Tfoe`. Only YOUR makes sense, so context decides here, as for `up`.
11. **Heading.** The F of "Friday" is an ornate form like a looped I or J; the postmark date and calendar support Friday. Heading initials read G. H.; C. H. appears on some sisters. They are not part of the cipher.

## Why it is correct

One fixed shift, not tuned to this card, gives English for all 51 enciphered letters. `Op ujnf up Tfoe Mfuufs` = NO TIME TO SEND LETTER is a fresh sentence, not one of the couple's stock formulae, and it explains why this is a short card. Line 1 has the outline of the same line on hcp-1361 and hcp-1367, both FINAL. The closing matches the formula on hcp-1371 and others, and the heading agrees with postmark and calendar.

## Credits

Solved by Claude Opus 5.5 acting as solver, 2026-10-30. No earlier work on this number exists. The key and the comparison shapes come from sister-card work in this repo (OpenAI GPT solver and Claude Opus 5.5). The reading of `Cpz` and the discovery of the extra signs in line 1 are the reviewer's. `Mpwjoh` for this card was prompted by the review of hcp-1360, which reads the same outline there.

## Response to review 1

Re-run after the fixes: the command above passes its hashes and reports 51 enciphered + 4 literal letters.

1. **`Op 2.` is `Cpz` (major): agreed, fixed.** The capital and p match `Cpz` on hcp-1363, and the same sign sequence with a 2-like z stands under `Mpwjoh` on hcp-1367 (`crops/cmp_mpwjoh.png`, second row). The field is removed from `transcription.json` and `decode.py`, and `Cpz` joins line 1. "NO 2" is withdrawn.
2. **`Mpwfs` (major): extra ink agreed, reading not adopted.** You were right that ink after the `f` was omitted and that LOVE alone is not acceptable. But I read neither LOVER nor LOVED, because the stem I took as f in DONE1 is not an f.
   - In line 4 the f of `Mpwf` has a closed looped foot. The line 1 stem ends in an open left hook, like the j of `Hjsm` on this card (`crops/cmp_mpwjoh.png`, rows 4 and 5).
   - The closed sign after it, then the rise, sharp turn and fall to a blob, match the `oh` of `Mpwjoh Cpz` on hcp-1361 and hcp-1367, both FINAL (rows 1 to 3).
   - The review of hcp-1363 rejects s here because the disputed sign has no counterpart in this hand's s, and the review of hcp-1360 reads the same outline there as `Mpwjoh`. LOVER appears as a reading nowhere else in the repo.
   - So line 1 is `Nz Pxo Mpwjoh Cpz` = MY OWN LOVING BOY. The differences from those cards (see Uncertainty 1) are real, so this is the point for review 2 to test.
3. **Headline and coverage (major): fixed.** The quoted plaintext, table, both translations, `transcription.json`, `decode.py`, the counts and "Why it is correct" are updated. The count is now 51 + 4, not the 50 + 4 that follows from LOVER.
4. **"Numbers" uncertainty (minor): fixed.** The entry is gone, and Origin states the "No. 1." / "No. 2." pair with hcp-1363 and claims no more.
5. **WIMBORNE wording (minor): fixed.** Origin now gives WIM... as firm and the rest as from sister cards, which agrees with your `z_stamp.png`.

Beyond the findings:

- `N. h.` is now transcribed `M. h.`, because the first sign has M's three downstrokes on this card (`crops/cmp_mpwjoh.png`, last two rows), and the reviews of hcp-1360 and hcp-1363 make the same point. No word changes, as the group is literal.
- Your note on hcp-1360 and hcp-1362: `crops/love.png` here remains in place, but it shows the line 1 word as I misread it in DONE1. Those sisters should not rely on it as `Mpwf`. I have not edited them.

## Response to review 2

Verdict ACCEPT; all four findings are minor and all are accepted. I checked each on the reviewer's crops (`review/work/r2/a_zpvs.png`, `a_wjoh.png`, `a_ff.png`) and on `work/crops/cmp_mpwjoh.png`. No token of `work/transcription.json` changed, and `python3 -I ciphers/hcp-1366/work/decode.py` was re-run: hashes OK, 51 enciphered + 4 literal letters, same output.

1. **`Zpvs` final sign (minor): fixed.** The crop shows the small hook. New Uncertainty 10; the heading entry is now 11.
2. **Missing j dot (minor): fixed.** Uncertainty 1 now says so. In `a_wjoh.png` the dark stroke above the j is separate from it and belongs to the p of `Cpz`.
3. **hcp-1367 comparison (minor): fixed.** Uncertainty 1 no longer calls that tail straight; in `cmp_mpwjoh.png` row 2 it curls at the top of the C. hcp-1361 (row 3) remains straight. The j of `ujnf` is now cited beside `Hjsm`.
4. **Pale forms in `Mfuufs` (minor): fixed.** Uncertainty 5 now names the arch and the curl, and states six letters as the best count.

The report and register entry follow, as the review allows, without another round.
