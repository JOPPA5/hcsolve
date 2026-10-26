REVISE

# Review 1 — HCP 1511 / pc_hcp_192 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the thirteen words are right.** Read sign by sign from the scan, they give HOUSE, LOUISE, PORCH, LONG, WOODEN, STORE, SALOON, BARBER, SHOP, FRANKS, LIVERY, STA#BLES and LIBRARY. They fit the plain prose and the photograph. **The transcription and the key table, however, do not match the card for the letter Y** (finding 1), so the claim of "one alphabet … without per-word exceptions" is not supported as written. The verdict is REVISE because the meaning is secure while the key and record need correcting.

## What I verified and how

1. **The documented command.** `python3 ciphers/hcp-1511/work/decode.py` runs without error. The hash checks pass, and it prints the 13 words with "73 intact cipher letters". As the solver says, it maps hand-made tokens through the key and does not test the reading of the image.
2. **Independent reading of the scan.** I rotated `source/address-large.jpg` by 270° to make the prose upright (`review/work/msg_r.jpg`). I located every Pigpen group and made 4–10× crops of each (`review/work/w*.jpg`, `e8.jpg`, `cmp_*.jpg`). I read each sign as an outline plus dot before I opened the solver's transcription. My reading is in `review/work/my_transcription.txt`, where `?` marks a dot I cannot decide at 1024 px. I checked the top margin, the bottom margin and the picture side (`top.jpg`, source picture) and found no other cipher groups.
3. **Independent decoder.** `review/work/review_decode.py` is my own script and imports nothing from `work/`. It accepts either wedge assignment:
   ```
   --wedges=SOLVER (< U/V, > W/X, ^ Y/Z):  HOUSE LOUISE PORCH LONG (W|X)(O|P)O(C|D)E(M|N) STORE
       SALOON BARBER SHOP FRANKS LIVERW STA#BLES LIBRARW
   --wedges=ALT    (< U/V, ^ W/X, > Y/Z):  ... (Y|Z)(O|P)O(C|D)E(M|N) ... LIVERY STA#BLES LIBRARY
   solver's own tokens under ALT:          YOODEN ... LIVERW ... LIBRARW
   ```
   Token diff, solver → reviewer: line 11 `^0` → `>0`, line 13 `^0` → `>0`, and line 5 has undecided dots/shape on the first, second, fourth and sixth signs. All other signs agree in outline. Wherever I can see the dots, they agree as well.
4. **Context.** The plain prose reads, as far as I can make it out: "Dearest Edith, Here it is. The little HOUSE here at the left is where LOUISE & I were last Sun. afternoon on the PORCH. The LONG building at the side of the house is the WOODEN STORE. The Hotel has the sign on it. The SALOON, BARBER SHOP & FRANKS store & the LIVERY STABLES are on the right out of sight. The building with the x is where they have the LIBRARY. It is nothing now. Just full of old old magazines & papers. Last yr. they had books but they have all been taken. …" The picture side, "Part of Felton, California", shows a small house with a porch at the left, a long wooden building beside it, and the Grand Central Hotel with its sign. Every encrypted word lands where the prose and the photograph require it.
5. **Prior solutions.** The portal shows Not solved, with no attachment; this is recorded. I found nothing in the files suggesting that an outside solution was used.

## Findings

1. **major (transcription and key): the Y of LIVERY and LIBRARY is drawn `>`, not `^`.** See `review/work/cmp_livery_Y.jpg`, `cmp_library_Y.jpg` and `w13.jpg`. Both final signs are clean wedges pointing right, undotted. LIBRARY's is followed by a full stop. Neither is an upward wedge. The solver's key gives `>` = W/X, so the card as written decodes to LIVERW and LIBRARW. The only `>` in the solver's transcription is the W of WOODEN. That sign (`w5first.jpg`, `cmp_wooden_W.jpg`, `w5a.jpg`, `w5b.jpg`) is small and is crossed by the descender of "building" from the line above. To me it looks like a flat `>` or a `⊐`, and I cannot read it as a `^`. So one of two things is true:
   - (a) the writer's key has `>` = Y and the W of WOODEN is some other sign, in which case the key table is wrong; or
   - (b) `>` is used for both W and Y, in which case the key is inconsistent on this card.

   Either way, the statement "their values are applied consistently throughout, without per-word exceptions" is not true of the transcription as filed. The `^` tokens were evidently written to fit the key rather than read off the card. The words themselves are not in doubt.
2. **minor: dots and outlines not decidable at this resolution.** In WOODEN I cannot confirm the dot of D (`B1`) or of N (`TR1`), and I see a mark that may be a dot inside the second sign (O). The last sign of PORCH (`w3.jpg`) looks closed on all four sides, which would make it `C1` = J; H is certain from context. The L of STABLES looks nearly closed. These are normal Pigpen sloppiness, but the solver's text claims more than the image shows, and they should be listed by position.
3. **minor: unencrypted signs between cipher groups are not recorded.** After LOUISE and between SHOP and FRANKS there is a plain cursive ampersand (`+`/`Y`-like). It is not a Pigpen sign. The second one in particular looks like a cipher wedge, so the transcription should mark it as plain text, not leave it out silently.
4. **minor: no running text.** `SOLUTION.md` gives the 13 words and a paraphrase but not the message. Most of the prose is legible (see item 4 above). The report should give the plain text with the deciphered words in place, marking illegible stretches, because the encrypted words only make sense inside it.
5. **minor: date.** The postmark (`review/work/pm.jpg`) shows "…31 / 1913 / CAL." (month illegible). That is enough to date the card to 1913. `SOLUTION.md` says no date was established.

## Required for closing

- Re-transcribe lines 11 and 13 as `>0` and re-examine the first sign of WOODEN. Then either restate the key (`>` = Y/Z, with W's sign identified) or state openly that `>` serves for both W and Y on this card. Update the key table and the "consistently throughout" claim to match.
- List the undecidable dots and shapes (WOODEN, PORCH final, STABLES L) and record the two plain ampersands.
- In the report, give the running text with the words in place, and the 1913 postmark.

None of this changes the 13 deciphered words. If the record is corrected as described, I see no need for another review round.

## What I could not verify

- The exact shape of the W sign in WOODEN, which is overwritten by the line above. Higher-resolution scans would settle finding 1.
- What the blackened sign inside STABLES originally was.
- The identity of the writer and of "Franks". Whether the "x" mentioned in the prose is marked on the photograph: I see none at this resolution.
- Whether the solution has been published elsewhere. I relied on the solver's portal capture and register snapshot.
