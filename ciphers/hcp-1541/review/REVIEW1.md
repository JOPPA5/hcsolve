REVISE

# Review 1: HCP1541 / pc_hcp_222 (Pepouš to Anna Tichá, 19 Aug 1903)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-29. This is an independent review. I changed none of the solver's files and nothing in `source/`. My scripts and crops are in `review/work/`.

## Summary

The card uses the Anna Tichá / Pepouš family key, a simple substitution with a CH sign. It decodes into coherent Czech of 1903 that fits the card's date and address. The body of the reading stands, and so does U01 = G (SVAGRA). Two things need fixing, though.

- The completion's U03 claim ("`5 c 4` (EŠÍ) are still visible") does not match the pixels. The visible sign after the E is the tall angular cipher `s` (= C), not the round cipher `c` (= S/Š). TĚŠÍ is therefore a contextual reading, not a visible one.
- The single reproduction command and the transcription were never updated for the completion. They still print `sva[U01]ra`, `vecn[U02]tvuj` and `se [U03] na`.

## What I verified and how

1. **Solver command.** I ran `.../python3 ciphers/hcp-1541/work/decode.py`. It passes its 11 hashes and prints 19 rows, with 547 indexed units (546 keyed, 1 unassigned). Its output is identical to the "Literal Czech output" block, including the three `[U0n]` placeholders. It does **not** produce the completion's final text (SVAGRA, VĚČNĚ TVŮJ, TĚŠÍ).
2. **Independent decode.** `review/work/mydecode.py` uses my own table, written from the 22-entry key, with U01 = g. Run on `work/transcription.txt`, it gives the same plaintext letter for letter. It covers 546 keyed units, finds no unknown characters apart from the three U labels, and every key entry is used at least once. The key is the family key in `ciphers/hcp-1545/work/key.json`. There the `7`-shaped J sign is called `7`; in this directory it is called `y`, and on the scan it looks like a 7.
3. **Transcription against the scan.** `review/work/crop.py` rotates `source/picture.jpg` 90° clockwise (674×1024) and enlarges the crop.
   - Ordinary rows: I compared rows 3, 7, 8, 9, 13, 14, 15 and 16 (`r03.png`, `r07_09.png`, `r09_spravec.png`, `r09b.png`, `r12_14.png`, `r15_16.png`, `r15_s.png`) with the transcription sign by sign, at 2–6x. I found no discrepancy. PAMETNI / KNIHY DEKANSKE, ZHATIL and literal `cbh6f5s` SPRAVEC are on the scan as recorded.
   - U01 (`r11_svagra.png`, 5x): the scan clearly shows `c f 6 [k] h 6`. The sign is k-shaped (ascender, loop, kicked leg) and clearly different from the looped `g` (K) in `gd5h5r3` on the same row.
   - U02 (`r16_tail.png`, 4x; `r16_patch.png`, 8x): a green painted patch sits between `f5sm` and `df27`. There is room for about one sign, and only a speck of ink shows. Nothing in it can be identified.
   - U03 (`r17_tail.png`, `r17_full.png`, `r17_comp.png`, `r17_patch.png`, `r17_after.png`, 4–8x): see finding 1.
4. **Context.** The address side and the date `19./VIII.1903.` agree with the portal metadata (Anna Tichá, Pelhřimov, 1903-08-19). The vocabulary and spelling (nastoupiti, následkem čehož, pamětní kniha děkanská, brzkou zprávu) are normal Czech of around 1900. The content (a superior's leave, a postponed holiday, a closing nickname PEPOUŠ) matches the rest of the family.
5. **Sources.** The family key is credited as transferred from earlier cards and from the partial public study (maxim-egorov.dev) in both SOURCES.md and SOLUTION.md. The portal attaches no solution. I found no undisclosed published solution.
6. **G sign in the family.** On HCP1570, my own review found the same k-shaped sign in SVA?ROVA and in KOLE?I, both places where only G fits. HCP1553 and HCP1554 (TELE?RAM) are still under review. Taken together with this card, the k-shaped sign = G is well supported.

## Findings

1. **major: the U03 completion claims visible signs that the scan contradicts.** The completion says that after the patch "`5 c 4` (EŠÍ) are still visible". In `r17_after.png` and `r17_comp.png`, the sign between the E-like sign and the final `4` is a tall, slanted stroke with a small foot curl. It is not the round, open `c` that this writer uses for S/Š everywhere else. Compare `d5c4` (TĚŠÍ) in row 3 (`r03.png`), and `b2c b3c486` in row 16 and `c5` in row 17. The stroke instead matches the angular cipher `s` (= C), as in the final sign of `cbh6f5s` in row 9 (`r09b.png`) and of `n5c4s` / `d4c4s` in row 15 (`r15_s.png`). The visible remains therefore read `5 s 4` → ECI under the key, or perhaps `5 1 4`. The E-like sign is itself somewhat ambiguous between 5 and 3. In front of it, a bowl inside the patch fits `d` (T) but cannot be confirmed. "který se těší na opětnou brzkou zprávu" is clearly the intended sense. But it only works if the writer made a slip (C for Š) or the stroke is an unrecorded variant. **Fix:** record the visible signs as they are (e.g. `c5 [U03]5s4 m6`, with the first sign marked hidden). Mark TĚŠÍ as an editorial or contextual reading, and state the C/Š discrepancy. Do not describe the signs as visible ESI.
2. **major: the reproduction command does not produce the claimed final plaintext.** `work/decode.py` and `work/transcription.txt` were not updated in the "Completion and handover" section. The command still prints `sva[U01]ra`, `vecn[U02]tvuj` and `se [U03] na`. The README requires a single command that produces the full plaintext. The "Literal Czech output", "Editorial Czech reading" and Slovak translation sections also still show the older `[g?]` and `[U02]/[U03]` state, while the completion section gives a different final text. As a result, SOLUTION.md contains two conflicting final readings. **Fix:** add the G sign to the key, or give an explicit U01→g rule. Update the transcription for U03 as in finding 1. Have the command print the final literal text, with restorations marked (e.g. `vecn(e) tvuj`, `se (t)e?i na`). Make the editorial and translation sections agree with it.
3. **minor: U02 = E is a pure restoration.** The patch hides the sign entirely; I see no ink that identifies it, and its width allows about one sign. VĚČNĚ TVŮJ is a reasonable restoration and matches the closing formula on the sister cards. However, VĚČNÝ is equally possible from the pixels. The completion does say "restored from context", which is adequate, but the editorial text should also mark it (e.g. věčn[ě]).
4. **minor: the label `y` for J is inconsistent.** The sign is shaped like a 7 on the scan, and the completion itself writes TVUJ as `d f 2 7`, while key.json and the transcription call it `y`. The mapping is unaffected, but the labels should be made consistent or explained in one sentence.
5. **minor: the U01 cross-references cite unaccepted cards.** HCP1553 and HCP1554 had not been accepted when the completion was written, so the "three cards support one another" argument is partly circular. HCP1570's review independently confirms the k-shaped sign as G in two words, and that is the stronger reference to cite.

## What I could not verify

- The signs fully hidden under the painted patches (U02 and the first sign of U03), from a 674×1024 image. Neither pixels nor any rendering can establish their identity.
- Whether the row-17 stroke is a writer's slip or a rare variant of the round `c`. A higher-resolution scan would be needed to settle it.
- The historical identity of "Pepouš", the "Hradec", the "Ústí" deanery and the superior. None of these is claimed.
- I did not re-check the postmarks on the address side.
