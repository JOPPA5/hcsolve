REVISE

# Review 1 — HCP 1017 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-27. In short, **the decipherment and the key are correct.** I re-read both regions sign by sign from `source/picture.jpg` and get the same German message. The verdict is REVISE, not ACCEPT, because the frozen transcription differs from the scan in five places. In one of them a sign was missed (finding 1). In two, a dot that is plainly visible or plainly absent was overridden by what the word should be (findings 2 and 3). The other two are finding 4 (T/V) and finding 5 (the blotted M and the stray dot). The solver says writer errors are kept literally, but this was applied unevenly. None of the findings changes the meaning of the message.

## What I verified and how

1. **The documented command.** `python3 ciphers/hcp-1017/work/decode.py` runs, the source hashes match, and it prints the claimed 7 + 1 rows (213 positions), identical to the "Literal main-body reading" in `SOLUTION.md`.
2. **Independent decoder.** I wrote `review/work/my_decode.py`. It does not read any solver file. My sign-by-sign reading is recorded in my own notation: grid cell numbers 1–9, a dot suffix, the X wedges n/w/e/s, and D for the diamond. The script decodes it with the *standard* Pigpen key (A–I grid, J–R dotted grid, S–V X, W–Z dotted X). Output, `python3 -I review/work/my_decode.py`:
   ```
   L1   LIEBSTE ERNA WIE GET ES DIR HEUTE
   L2   HAST HOFFENTLICH KE{#}INE AUSSCHAELTE
   L3   GEBRIEGT WEIL DU SO SPAET HINAUFKAMST
   L4   DU KOMMST ALSO MORGEN DONNERSTAG ABEND
   L5   UND HOLEST MICH SEI BIS DAN AUO DAS
   L6   HERVLICHSTE GEGRUEST TON DEINEM
   L7   EJNAR
   margin(rot180)  TAUSEND TAUSEND GLUEHENDE BUESSE
   glyph positions: 214
   ```
   Every sign resolves under one standard key, with no sign needing two values. The writer's only non-standard form is the closed diamond for W, which the solver identified correctly. Both regions are covered: the 7-line body (picture rotated 270° CW) and the 4-group margin (picture rotated 180°).
3. **Reading the scan.** Crops are in `review/work/`. `body1x.png` is the rotated body. `L{1..7}_{0,1,2}.png` are 6× strips of every line. `z-*.png` and `zc-*.png` are 10–16× details of every disputed sign. `M_{0,1,2}.png` cover the margin. For the dot questions I also printed the pixel darkness of the cell as ASCII (`review/work/ascii.py`). This settles whether a dot is there better than the eye can at 1024 px. Differences from the solver are in findings 1–5; everything else matches sign for sign, including the crossed patch in `KE…INE` and the undotted ⊔ at the start of `BUESSE` (confirmed by ASCII: the cell is empty).
4. **Search for missed cipher text.** The address side is entirely plain: `Fräulein Erna Dahm, Altona, Gr. Bergstrasse 27`, printed Danish card text and two postmarks. On the picture side the only writing outside the two cipher regions is the plain date `14.6.05` and the underline below `EJNAR`. I found no third cipher region. One sign was missed *inside* the body, though (finding 1).
5. **Context.** 14 June 1905 was a Wednesday (`datetime`), so `MORGEN DONNERSTAG ABEND` fits. Both postmarks read 14.6.05 (Hamburg; Altona (Elbe) 6–7 N[achmittags]). The card was posted and delivered the same day, which fits a note between neighbours in Hamburg and Altona. The printed card is **Danish** (`BREVKORT. Paa denne Side skrives kun Adressen.`), and `Ejnar` is a Danish spelling of Einar. This independently supports the solver's EJNAR over EINAR/EYNAR, and it is a likely reason for the slightly unidiomatic German (`GET`, `AUSSCHAELTE`, `DAN`). The solver did not use either point.
6. **Prior solutions.** The portal shows no attached solution, and `SOURCES.md` credits the Schrödel 2021 collection paper as context only. I found no sign that a published reading was used. I did not repeat the literature check (see "could not verify").

## Findings

1. **major (transcription) / minor (meaning): `ABEN` is `ABEND`; the final D was missed.** Details: `review/work/z-aben.png`, `zc-aben-end.png`, `z-bottomedge.png` (original orientation). Line 4 ends at the bottom edge of the card. After `┘ ⊔ □ □·` (A B E N) there is a fifth, cramped sign squeezed against the edge. It is a top stroke, a right upright and a bottom stroke, i.e. an undotted ⊐ = **D**. The ASCII dump (columns 32–41, rows 11–21 of the crop at x=570, y=82) shows all three strokes. The solver lists `ABEN` among the writer's spelling errors ("ABEN and DAN are left as written, with no D/N silently inserted"). On the card it is not an error. Fix the body transcription (`… BR openT box box. openL`), the literal reading, the "writer errors" list and the position count (214, not 213).

2. **major (transcription) / minor (meaning): `AUF` is written with a dotted ⊏, literally `AUO`.** Detail: `review/work/z-auf.png`, plus an ASCII dump at x=508, y=106. The third sign of `AUF` (line 5) has a clear, dark dot in the centre of the cell, as dark as the O dots in `HOLEST` and `ON`. In `HOFFENTLICH` and `HINAUFKAMST` the writer's F is undotted. `body-shapes.json` records this sign as `openR` (F), which is a silent normalization of a writer's slip. It should read `AU[O]` (for AUF) and be listed with the other writer errors.

3. **major (consistency of the literal reading) / minor (meaning): two dots the solver asserts are not visible.** Both are below the threshold where the eye could be misled, so I checked them with ASCII dumps.
   - **`GEKRIEGT`, 3rd sign** (`zc-k-gekriegt.png`; ASCII at x=40, y=52). The ⊔ cell is completely empty. In the same crop, the dot of the neighbouring R (┌·) shows clearly. The solver's "faint dot" is not in this scan, so the literal reading is **`GEBRIEGT`**.
   - **`HERZLICHSTE`, 4th sign** (`z-herz.png`; ASCII at x=60, y=128). This is an ∧ with an empty interior. Literally that is **V**, i.e. `HERVLICHSTE`.

   In both cases the intended word is certain. The point is method: for `BUESSE` the solver keeps the undotted ⊔ as a literal B and offers K only editorially, which is right. The same rule must apply to `GEKRIEGT` and `HERZLICHSTE`. Either mark them `GE[B→K]RIEGT` and `HER[V→Z]LICHSTE`, or say explicitly that dots are being supplied there. Together with `BUESSE`, the card shows a writer who sometimes drops the dot, which is itself worth one sentence in the report.

4. **minor: `[T/V]ON` is not a glyph ambiguity.** Detail: `review/work/z-von.png`. The sign is a clean `>`, the same form as every other T on the card, including the T of `GEGRUEST` immediately before it. By the card's own key it is unambiguously **T**. The correct record is literal `TON`, a writer's slip for `VON`, not an unresolved T/V position. `audit.py`, `body-shapes.json` (`TV` token) and the uncertainty section should be adjusted accordingly.

5. **minor: details not mentioned.**
   - (a) Line 5 has an isolated dot just *left* of the ∨ of `SEI` (`z-sei.png`). It is outside the cell, so it is not a dotted ∨ (= W). It is most likely a stray mark or punctuation, but it should be noted.
   - (b) The final M of `DEINEM` is a heavy ink blot (`z-deinem.png`), so its dot cannot be seen. M is inferred.
   - (c) The T of `GET` is heavily inked and may be a correction (`z-get.png`). It still reads `>`.
   - (d) The Danish printed card and the Danish name Ejnar (verification 5) belong in the context section, as do the two same-day postmarks.

6. **minor: the reproduction command only replays a manual transcript.** The solver says so openly, which is correct. Findings 1–3 show why the transcript needs a correction pass before `FINAL`. The optimizer and control experiments do not bear on these questions, because they validate the key, not the dots.

## Required for closing

- Body transcript: add the D of `ABEND`; record `AUF`'s third sign as `openR.`; record the `GEKRIEGT` K and the `HERZLICHSTE` Z as undotted (literal B and V) with the intended letters marked editorially; replace `TV` with `right` (literal T).
- Update the literal reading, the writer-error list (drop ABEN, add AUO, GEBRIEGT, HERVLICHSTE and TON), the position count and `audit.py`.
- Mention the stray dot before `SEI`, the blotted M, and the Danish context.

These are corrections of the record, not of the solution. If they are made, I see no need for another review round.

## What I could not verify

- Whether the "faint dots" the solver reports could be visible on the physical card or a higher-resolution scan. At the portal's 1024 px they are not there.
- The identity of the overwritten letter under the crossed patch in `KE…INE`. It is a dark triangle with a stroke through it, and I agree it should stay unassigned.
- Whether any individual decipherment of this card has been published (I relied on the solver's note on the Schrödel 2021 paper).
- Identification of the building in the photograph. It was not needed for the reading.

## Process note

While checking the solver's audit, I ran `python3 -I ciphers/hcp-1017/work/audit.py`. That script rewrites `work/audit.json`, whose mtime is now 2026-10-27 00:31. The script is deterministic over unchanged inputs, so the content should be identical, but the solver should be aware that the file was regenerated by the reviewer. No other solver or source file was touched.
