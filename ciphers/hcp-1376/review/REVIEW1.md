ACCEPT

# Review 1: hcp-1376 / pc_hcp_57 (reviewer: Claude Opus 5.5, 2026-10-30)

I tried to refute the reading and could not. The key, the sign reading and the plaintext stand. Remaining points are minor. Solver and reviewer are both Claude Opus 5.5 on this card, so this is not an inter-vendor check.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1376/work/decode.py` runs. Output is identical to the table in SOLUTION.md; 54 letters read, 1 restored, 9 literal. I recounted these by hand: all three figures are right.
- **Hashes.** `shasum -a 256` on all four files matches SOURCES.md and transcription.json.
- **Independent decode.** `review/work/own_decode.py`, with tokens typed from my own crops and its own shift loop, gives: My Ow / Is was posted / Before / clearing / Its a Mystery / My from Your / Girl; 54 letters.
- **Coverage.** The one shift covers every enciphered token. The only plain items on the card are the heading, `2 hrs.`, and the abbreviations `E-L`, `N. & L.`.
- **Transcription.** From `work/hires/pc_hcp_57_adr.JPG`, rotated by me (`review/work/rot.png`), I made 3x crops of all rows (`a_head`, `b_l1` to `h_l7`) and 5–7x crops of each disputed place (`z1_px` to `z11_pm`). I read every sign in rows 1 to 7:
  - `Nz.`, `xbt.`, `qptufe`, `Cfgpsf.`, `dmfbsjoh`, `b.`, `Nztufsz`, `gspn.`, `Hjsm.` are all as transcribed.
  - `Cfgpsf`: the pale loop below the line is the f of this word, so six signs C f g p s f. The solver is right.
  - `dmfbsjoh`: the V under the line is the foot of j. The j of `Hjsm` on this card has the same check-shaped foot (`z6_girl`), so "slash plus caret" is rightly rejected.
  - `Px[o]`: compared with `Pxo` on hcp-1386 (`work/crops/band6.png`), the big-bowled P and the two-stroke x are the same forms. Also `E-L` and `Hjsm` match that band closely.
- **Date and context.** 9 Nov 1907 was a Saturday (computed). Postmark reads WIMBO…, NO 9, 07. The picture side is printed "Glastonbury Abbey looking West" with no handwriting. Address reads Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon. Wimborne and this recipient match the sister cards.
- **Language.** Natural Edwardian English. "Clearing" is good period usage for emptying a post box. Formula `Nz Pxo E L` and `N. & L. gspn zpvs` recur on FINAL sister cards.
- **Sources.** No published solution appears. 1376 is not in skip.txt or register-exclusions.json.

## Findings

1. **Minor: the restoration `Px[o]` is sound and disclosed.** No change needed to the reading. In support: the blot measures about 30 x 22 px in the original, near letter size, while this writer's stops are about 10 x 7 px (`z1_px`). It stands on the baseline in the place of the o. Pixels alone do not show an o, so it stays a restoration, as the solver says. One correction: "Why it is correct" says `Jt` is "the only token that does not decode to the expected word", yet `Px` without the restoration does not either. Say "the only fully legible token".

2. **Minor: evidence for the plain-"It" alternative in uncertainty 1 is stronger than stated.** The first sign of `Jt` has a large closed loop at the top (`z2_jt`), whereas the J of `Ju't` is a plain stroke with no loop (`z4_jut`). So the two "J"s are different forms, which fits a plain capital I in `It`, next to plain `2 hrs.`. The solver should mention this. The second sign is certainly the same as the t of `xbt` (hooked foot, dash), so `Jt` is the right transcription and the solver's disclosure of IS against IT is honest. Also, the final sign of `Ju't` is joined and has no free hooked foot, so "the same form as the final t of ... `Ju't`" is looser than for `xbt`. A half-shifted slip (J shifted, t not) is a third possible explanation and comes to the same sense.

3. **Minor: the English reading silently uses "It was".** The table prints IS, and the English line reads "It was posted". Mark the emendation in the English and Slovak lines, for example "[It] was posted", so a reader of the report sees it without reaching the Uncertainties.

4. **Minor: the "heavy dot below line 4" probably belongs to the J of `Ju't`.** It sits directly above the top of that J, about 30 px up and 8 px to the left in the original (`e_l4`, `f_l5`). It is likely a dot on the J, not punctuation of line 4. This does not affect the plaintext.

5. **Minor: `Zpvs` is confirmed in outline only.** The Z and the p stem are clear, and the p, v, s are pale and partly hidden by the loop of the f above (`z5_zpvs`). The count of signs and their general shapes fit, and the same group on hcp-1386 band6 looks the same, but v and u cannot be told apart here. The solver's "pale but visible" is a little generous; add that the v rests partly on the formula. YOUR is not in doubt.

6. **Minor: the postmark detail is incomplete.** There is a "10" above NO on the stamp (`z11_pm`). Sister cards report WIMBORNE 10 PM, and this time bears on the "clearing" remark. The letters after 10 are not legible enough for me to confirm PM here. Worth recording as 10 [PM?]. "That context is inferred" remains correct.

## What I could not verify

- The meaning of `E-L`, `N. & L.`, `G. H.`, and of the arrowed line below row 4.
- The heading number after "No." (3, 2 or 7), which is not ciphertext.
- Whether `Jt` is a slip or plain "It". The card cannot decide this.
- The physical card: all checks were on scans. Faint ink in rows 6–7 could hold detail a scan loses.
- That no published solution exists anywhere; I only saw none in the solver's files.
