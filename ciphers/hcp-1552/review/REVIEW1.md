REVISE

# Review 1 – hcp-1552 (pc_hcp_233), Pepouš to Anna Tichá, 30 May 1903

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-29. Own files only in `review/`.

## Summary

The decipherment itself is right: this is the Anna Tichá family monoalphabetic
substitution, and the plaintext is coherent Czech of 1903 that fits the card
(sent from Prague 30 May 1903, the eve of Whitsun 31 May, so "svátky" fits; addressed to
Anna Tichá, teacher in Pelhřimov; mentions Žirovnice, her home town on other cards).
The 2026-10-29 completion of U1 as NAVRATU is visible in the pixels. Three
things still need fixing: one clear transcription error (ANINKA should be ANUNKA), one probable
one (SLIBANY), and a SOLUTION.md whose header, transcription and single command
still describe the partial state, so the reproducible output does not contain
the completed reading.

## What I verified and how

1. **Solver command.** `python3 ciphers/hcp-1552/work/decode.py` → exit 0; hash,
   inventory and inverse checks OK; 14 rows, 405 units, 408 letters, 3 CH, 1
   unknown span. Output equals the literal in SOLUTION.md. It still prints
   `na[U1:unknown-length]`, not NAVRATU.
2. **Independent decode.** `review/work/mydecode.py` (my own key table, with H as CH and
   ⟦U1⟧ passed through) applied to `work/transcription.txt` (`python3 -I
   review/work/mydecode.py work/transcription.txt > review/work/mine.txt`). The output is
   identical to `work/literal.txt` except for one trailing newline. No unmapped symbols.
3. **Key consistency.** `work/key.json` matches the family key in
   `ciphers/hcp-1545/work/key.json` class by class. The labels differ but the values
   are the same: the solver writes `y` for the J-sign the family writes `7` (on this
   card the glyph looks like a 7, as in `n375`, `bh574`, `7c5n`), and `H` for
   the family `ř`, the r-with-tilde CH sign. Every recorded unit is mapped.
4. **Transcription against the scan.** I made my own 4x crops of all 14 rows in two
   halves each (`review/work/rNN_0.png`, `rNN_1.png`), and 6–10x crops of the
   critical spots (`U1_x10.png`, `U1c_x9.png`, `row1_start.png`,
   `row3_aninka.png`, `r5_slibany_x8.png`, `r5_start_x6.png`). I read all rows
   against the transcription. Apart from findings 1 and 2, every word agrees, including
   the three CH units (`cf6ds4r̃`, `fh581r̃`, `2bh4nm1r̃`), the question marks,
   PODOBENKAMI, VYPODOB-/NITI, and JINY/ZIROVNICE behind the printed stems.
5. **U1 (the completion section).** At 9–10x the span after `m6` shows `f` (tall
   looped, crossing the print), `h` (ascender loop), a `6` that is overinked but has a
   recognizable loop and bowl, round `d`, `2`, and a full stop. That gives `m6fh6d2.` = NAVRATU,
   "po tvém návratu". The overinking looks like retracing, not cancellation. The
   reading is supported by the pixels, not only by the context. Accepted.
6. **TIK.** `row1_start.png` shows `d4c4s5h1 d4g,`. The second word has the same
   round d (= T) as the first word and as `t6d4` DATI in row 7, so TIK is what is written.
   The solver handles DIK correctly as a disclosed editorial emendation.
7. **Address side.** It carries only ordinary script: Velectěná Slečna / slečna Anna Tichá /
   učitelka t. č. v / Pelhřimově, Vlastnoručně dodati, Praha postmark. There is no ciphertext.
8. **Sources.** The use of the published family key and of the Egorov research is disclosed.
   No published plaintext of this card was used.

## Findings

1. **major – row 3, `6m4mg6` ANINKA is a misreading; the source has `6m2mg6` =
   ANUNKA.** At 6x (`review/work/row3_aninka.png`) the third sign is plainly the
   `2`/U form, identical to the `2` that starts the next word `2g84tm486`
   (UKLIDNILA) and unlike the `4`/I sign. "Anunka/Anuňka" is the pet name used for
   Anna throughout this family (ANUNKA/ANUNKO occur on hcp-1533, 1535, 1540, 1544,
   1545, 1547, 1553, 1554 and others). Correct the transcription, literal, plaintext,
   both translations and the counts (the unit count is unchanged; one I becomes U).
2. **minor/major – row 5, `c84p6m1` SLIBANY: the 5th sign looks like `5`, not
   `6`.** In `review/work/r5_slibany_x8.png` the sign after `p` has the top bar
   and the lower bowl of this writer's `5` (compare `f58415`, `c5` in
   `r5_start_x6.png`). It lacks the tall left-curving loop of his `6`. With `5` the
   word is SLIBENY = "slíbený", the standard form, which is what the solver's own
   editorial Czech already prints ("slíbený lístek"). So the literal SLIBANY and the
   editorial reading silently disagree. Re-examine the sign. If it is 5, correct the
   transcription. If you keep 6, disclose the editorial change.
3. **major – the completion is not carried into the reproducible record.**
   `work/transcription.txt`, `work/literal.txt`, `work/inventory.json` and
   `decode.py` still contain ⟦U1⟧ as an unknown-length span, with counts of 405/408. The
   README requires "a single command that produces the full plaintext". Replace ⟦U1⟧ with
   `fh6d2` (5 units → 410 units, 413 letters with 3 CH) and update the hashes and
   counts.
4. **major – SOLUTION.md contradicts itself about its status.** The title and opening
   still say "partial … cannot be claimed solved while that span remains unresolved".
   The "Uncertainties" section still says that VRATU "is excluded" and that "context
   alone cannot settle it". Only the appended completion section says "complete". Rewrite the head of
   the file so that it states the current claim (complete, with U1 read as NAVRATU from the
   pixels and the retraced ink disclosed) and keep the earlier caution as history.
5. **minor – translation errors in the completion section.** The Slovak has "mienš"
   (should be "mieniš") and keeps Czech "podobenkami" (Slovak "podobizňami", as in the
   earlier Slovak version). The earlier Czech editorial version still shows "na[nejasný
   úsek]". After the fixes, keep one Czech and one Slovak version, with Anunka.
6. **minor – label convention.** Mapping J as `y` and CH as `H`, while the family key files use `7` and `ř`,
   is harmless but makes cross-card comparison harder. Mention it in the key table
   ("y = the 7-shaped J sign").

## What I could not verify

- The scan is only 1024×674. The overinked letters of U1 and the 5/6 sign in finding 2 are
  read at the resolution limit. For U1 the shapes are clear enough. For finding 2 my
  reading is "probably 5", not certain.
- Whether the overinking at U1 hides an earlier, different word under the retraced
  `h6` cannot be determined from this image. Nothing suggests it.
- I did not re-run the portal or register checks myself. The orchestrator states the register was
  checked today.
