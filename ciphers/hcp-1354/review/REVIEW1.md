ACCEPT

# Review 1 of hcp-1354 / pc_hcp_35 (reviewer: Claude Opus 5.5, 2026-10-30)

The reading stands: Caesar -1, "Sudden. change in heading of letter Monday to post card received Sunday? For WHY! Loo. March 5th 07". I tried to break it on HEADING, on the day names, on the signature and on the letter count, and none of those attacks changes a word. Four minor corrections to the write-up remain, listed below.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1354/work/decode.py` prints "source hashes OK" and the same six lines as the table in SOLUTION.md, with 68 letters. `shasum -a 256` on source/ and work/hires/ matches SOURCES.md.
- **Independent decode.** `review/work/decode_review.py` has my own transcription, keyed from my crops, and an explicit substitution table. It gives the same plaintext and 68 letters. The only difference is one extra full stop (finding 2). Of the 26 shifts only -1 gives English. All 20 cipher letters present are covered, so nothing falls outside the key. Absent: a c k l r y.
- **Transcription against the scan.** I rotated the original `work/hires/pc_hcp_35_adr.JPG` myself (`review/work/rot.png`) and cropped every line at 4x (`r_l1a` to `r_l7`), then the doubtful signs at 6x to 8x (`x_cmp`, `x_xiz`, `x_left`, `y_sudd`, `y_sund`). Every word matches, subject to finding 1.
- **HEADING vs READING.** See finding 3. The pixels favour HEADING more firmly than SOLUTION.md says: the first sign is a dotted minim, and the s of `sfdfjwfe` is a different form. LEADING is also out, because `mfuufs` shows the m is a two-arch sign and this is a single stroke.
- **Other points in Uncertainties.**
  - `qptu`: the q has the same 9-shaped form with hooked tail as the G of `Gps`. Disclosed correctly.
  - `Npoebz`: the N, the long p, the bowl of e and the stem of b are all visible around the blot. The word is clearly not `Tvoebz`.
  - `mfuufs`: four minims between the two f signs, so uu holds.
  - `dbse`: the third sign is weak, as disclosed.
  - `Mpp`: same form as the closing of hcp-1398 (`work/closing.png` there).
- **Context.**
  - Postmark WIMBORNE 10 PM MR 5 07 confirmed, including the "5" and "07" lying over the stamp (`y_stamp.png`).
  - 5 March 1907 was a Tuesday (computed).
  - The picture caption reads "...kstone From Constitution Hill", so Parkstone is sound. Parkstone is close to Wimborne.
  - Address in clear: Mr W. Abbott, Stokelake Farm, Chudleigh, Devon.
  - Sister cards support the salutation remark: "My own dearest boy" on hcp-1350, 1356, 1357 and "My own E. L." on hcp-1374, 1376.
  - hcp-1350 is dated Thursday March 7th with no year; 7 March 1907 was a Thursday, so it may be the next card in the same exchange. That is a lead only.
- **Honesty.** The portal attaches no solution, and SOLUTION.md credits Claude Opus 5.5 alone. There are no completion or later-added sections, and no word in the table is restored from context. Finding 1 limits the literal claim that no letter is restored.

## Findings

1. **minor: `Tveefo` is less clean than presented.** The solver's "No letter is restored; each was read from the scan" overclaims here.
   - Evidence: `review/work/y_sudd.png`. After the T come a thick minim with a thin rising tick, then a solid black wedge with no visible eye, then one clear looped e, then f.
   - Compare the v of `Tvoebz` in `y_sund.png`, which is two minims. On that model the black wedge could be the second stroke of v, leaving only one e (`Tvefo`, 67 letters, SUDEN).
   - I prefer the solver's reading: minim plus tick as v, inked-over wedge as e, since the wedge is the darkest ink on the line and a fresh pen load could fill the eye. SUDDEN is not in doubt as the word.
   - Fix: disclose this in Uncertainties, and say the second d is inferred from a filled sign.

2. **minor: an undisclosed dot after `sfdfjwfe`.**
   - Evidence: `r_l5a.png` bottom right and `x_xiz.png` top. A heavy round dot lies just below the end of the word, at about x 687, y 1482 in `rot.png`, directly above the I of XIZ.
   - It is either a word-separator of the kind seen after `Tveefo`, `Jo`, `up`, `Mpp`, or a dot over that I. Neither changes a letter, but the claim of "all ciphertext on the card" should mention it.
   - Also unmentioned: a thin line runs from the X through the foot of the I into the foot of Z. It is either the Z's foot carried back or an underline, and it fits the emphasis of WHY.

3. **minor: Uncertainty 1 is factually wrong and understates the evidence.**
   - It says the card has no isolated lower-case i. It does: the second sign of `dibohf`.
   - `review/work/x_cmp.png` shows that sign beside the first sign of `ifbejoh`. Both are hooked minims with a dot up and to the right. The dot over `ifbejoh` sits just below the tail of the f from line 1 but is separate from it.
   - The j of `ifbejoh` is also dotted. SOLUTION.md mentions neither dot.
   - The contrast with hcp-1386's dotless x-height j is unnecessary. hcp-1398, with the same signature, has a dotted j descending below the line in `hjsm` (its `work/closing.png`).
   - Fix: rewrite the uncertainty with this evidence. HEADING can be stated as read rather than as the weakest word.

4. **minor: the sorting mark is probably 6, not 5.** With the card turned so that POST CARD reads upright, the mark is a tall stem with a closed lower loop (`review/work/y_pen.png`). "(5)" comes only from reading it in the rotated view. It is not part of the message, and I cannot tell how the sorter held the card.

## Not verified

- Whether a solution of this card is published elsewhere. I searched nothing beyond the repo; the orchestrator reports the AI register has no record, and the number is not in skip.txt or the mail list relayed by the user.
- What "heading" meant to the writer. The salutation reading is a reasonable interpretation and is labelled as one.
- Whether the signer's identity, the writer's sex and the link to hcp-1398 hold beyond hand, key and signature. "Your girl" on hcp-1398 supports "she" but does not prove it.
- Sunday delivery at Chudleigh-side addresses in 1907; "received Sunday" is simply what the card says.
