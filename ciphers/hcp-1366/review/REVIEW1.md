REVISE

# Review 1 of hcp-1366 (pc_hcp_47)

Reviewer: Claude Opus 5.5, 2026-10-30. No watcher, per this run's orchestration rules.

## Summary

The key (Caesar, cipher = plain + 1) and the body of the message stand. The card is not fully read, though. Line 1 ends in two pieces that SOLUTION.md misses or misreads, and the upper-right "number field" is not a number.

- The field `Op 2.` is `Cpz` = **BOY**, the last word of line 1, set above the line end. The "2" is this hand's z.
- `Mpwf` in line 1 has one more sign that SOLUTION.md never mentions. The word is very probably `Mpwfs` = LOVER.

Corrected reading:

> **My own lover boy, no time to send letter. Love & Lt.. from your own N. h. girl.**

The structure is confirmed by companion card hcp-1363 (same day, headed "No. 2."), whose line 1 is `Nz. Pxo. Mpwfs. Cpz`. It is also the couple's usual salutation: "My own ... Boy" appears on hcp-1371 and many other sister cards.

## What I verified and how

1. **Command.** `python3 -I ciphers/hcp-1366/work/decode.py` ran, the hashes passed, and the output equals the table in SOLUTION.md. So the tool is consistent, but it only decodes the manual `transcription.json`, including that file's errors.
2. **Independent decode.** `review/work/my_decode.py` uses my own transcription, typed from my crops. A sweep of all 26 shifts over the secure words gives English only at shift 1 (`no time to send letter from your own girl`). Result:
   - `Nz Pxo Mpwfs Cpz` = MY OWN LOVER BOY
   - `Op ujnf up` = NO TIME TO
   - `Tfoe Mfuufs` = SEND LETTER
   - `Mpwf & Lt..` = LOVE & [Lt..]
   - `Gspn Zpvs Pxo` = FROM YOUR OWN
   - `N. h. Hjsm` = [N. h.] GIRL
   - That is 54 written letters: 50 enciphered and 4 in literal groups. SOLUTION.md has 46 + 4.
3. **Transcription against pixels.** I rotated `work/hires/pc_hcp_47_adr.JPG` 90 degrees anticlockwise and enlarged it 3-8x (`review/work/msg2x.png`, `c_*.png`, `z_*.png`). I checked every word on the card; the results are under Findings and Confirmed points.
4. **Metadata.**
   - Postmark: my crop `z_stamp.png` shows WIM..., 10 PM, JY 19, 07. The fourth letter is damaged, so the postmark itself does not prove WIMBORNE.
   - 19 July 1907 was a Friday (checked with Python).
   - Picture side: printed "Royal Baths, Harrogate", no handwriting.
   - Address: clear, Mr W. Abbott, Stokelake Farm, Chudleigh, Devon.
5. **Language.** Period English. "No time to send letter" is telegraphic but natural on a card, and it is not a stock formula.

## Findings

1. **major: the "number field" `Op 2.` is `Cpz` = BOY.**
   - Evidence: `review/work/cmp_cpz_lover.png`, rows 1 and 2, sets the field beside `Cpz` from line 1 of hcp-1363. The capital is the same large looped C with an inward hook, the p is the same, and the third sign is the same flat-footed z.
   - The "2" is that z, in pale ink. Its "short dark dash" is the foot of the z, where the ink becomes dark again. It is not a separate mark.
   - The capital does not match the `Op` of line 2 (`c_l2.png`), whose O is a narrow closed loop with a hooked top. SOLUTION.md's O-form comparison fails on the crops.
   - Position fits as well: the field stands right after the end of line 1, raised because the line ran into the card edge area.
   - SOLUTION.md dismissed C because "BO 2 ... means nothing", but that assumed the numeral. It also lists O and C as the only open question and never tests 2 as z, even though z looks like 2 in this hand (`Nz`, `Zpvs` in the same message).
   - Result: "NO 2" and the "pairs with No. 1." argument must go. The number field should be removed as a category. The enciphered text is `Cpz`, the double dot after it is punctuation or blots, and it belongs to line 1.

2. **major: a sign at the end of line 1 is omitted and undisclosed; read `Mpwfs` (LOVER).**
   - Evidence: `z_love1.png`, and `cmp_cpz_lover.png` rows 3 and 4. After the w comes the stem of the f, descending to its hooked foot. Then comes a closed loop, a stroke to the upper right, a sharp turn and a pale fall to a dark blob on the baseline.
   - The same skeleton follows the f on hcp-1363. The hcp-1363 solver read it as s, gave LOVED as a less likely alternative, and asked for this comparison (its Uncertainties 1 and 2).
   - SOLUTION.md here transcribes `Mpwf.` and gives the ending no uncertainty entry. Uncertainty 6 covers the neighbouring word, not this one. A plain dot does not account for the loop and hooked stroke.
   - The s is larger and more angular than this hand's other s forms, and hcp-1363 has not finished review, so this reading is not secure. `Mpwfs` is preferred and `Mpwfe` (LOVED) must be disclosed as the alternative. LOVE alone is not acceptable, because the extra ink is real and has to be accounted for.

3. **major: headline, status and coverage claims are wrong as a result.**
   - "Whole message read" and "46 enciphered letters in the body, all decoded" are false: 4 letters (`s`, `Cpz`) are left out or misassigned.
   - These need correcting:
     - the quoted plaintext;
     - the English and Slovak translations (for example „Môj vlastný milý chlapec, ...“);
     - the table;
     - `work/transcription.json`, including removal of `number_field_conditional`;
     - `work/decode.py`, which prints the field line, and the counts it prints;
     - the "Why it is correct" section.

4. **minor: the "numbers" uncertainty missed the companion card.**
   - Uncertainty 1 says "I cannot explain what the numbers count" and that a sister search found no such field.
   - hcp-1363 has the same date and postmark time, is headed "No. 2.", and its SOLUTION.md names this card as its pair.
   - "No. 1." here is therefore simply the first of two cards posted that day. Origin should say so. Keep "day and postmark time" as a report of the two cards, and do not assert more than that.

5. **minor: the WIMBORNE wording is slightly stronger than the pixels.** SOLUTION.md's "WIMB[ORNE]" is close, but only WIM... is firm on the stamp and the next letter is damaged. Say that the rest comes from sister cards, which it already half does.

## Confirmed points (no change needed)

- `Op ujnf up`: the j has its dot, the f is looped, and the u has this hand's arch. Word separators are visible (`c_l2.png`).
- `Tfoe`: T and f share one body, o is a squeezed dark stroke, e is c-shaped (`c_l3a.png`). The disclosure is fair.
- `Mfuufs`: the zigzag after the f bar has four peaks, so two u's (`z_uu.png`). The pale f has a top curl and a long stem with a looped foot. The three blots are real, and they are not letter forms. The word is read from the pixels; the pale f and blots are honestly disclosed.
- `Mpwf`, `&`: clear (`z_l4a.png`).
- `Lt..`: hooked looped L, then a c-like stroke with a short dash, then two dots (`c_l4b.png`). t vs c is correctly left open and "Ks" correctly kept as a hypothesis.
- `Gspn`: the pale `p n` is in real ink. `Zpvs`, `Pxo`: clear (`c_l5.png`).
- `N. h. Hjsm`: as described (`c_l6.png`). The first initial has one more leg than the n-form of `Nz`, so N/M stays open. Keeping the group literal is right.
- Heading `G. H. Friday.` and `No. 1.`: plain and clear (`z_head.png`). The heading reads G rather than C here.
- Key: one fixed shift covers all letters apart from the two groups the solver keeps literal. It is not tuned to this card.
- Sources: SOLUTION.md discloses that no published solution was used. Nothing on the card or in the directory suggests otherwise.

## Could not verify

- LOVER against LOVED: the final sign of line 1 fits s better, but one parallel card, itself under review, is not proof.
- Whether `Lt..` and `N. h.` are enciphered or literal, and what they mean.
- The rest of the postmark town name on this card.
- Whether a published solution exists outside this repo: I made no web search, and the register check is the orchestrator's.

## Note for the solver

Sister notes cite this card's `Mpwf`. hcp-1360 (Uncertainty 2) and hcp-1362 compare their shapes with `crops/love.png`. Those are other directories and I have not reviewed them; the comparison there may need a second look once this card reads `Mpwfs`.
