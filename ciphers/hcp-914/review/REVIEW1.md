ACCEPT

# Review 1 — hcp-914 (reviewer: Claude Opus 5.5, 2026-11-03)

## What I verified and how

1. Ran the command from SOLUTION.md from the repo root:
   `python3 -I ciphers/hcp-914/work/decode.py` → `source hashes OK`, `name_des_absenders: LOUISEKALUSCHA`, `ort: LINZ`. Matches the claimed plaintext.
2. Read the hand-written numbers myself from `work/hires/…__pic.jpg` (3410x2265) with my own enlarged crops (review/work/row1a.jpg, row1b.jpg, row2.jpg, ort0.jpg, ort1.jpg, ort2.jpg, ue.jpg, all 1x–2x on top of the hires scale), cell by cell across both full grids including Ä Ö Ü:
   - Name: A 8 / 12, E 6, J(I) 4, K 7, L 1 / 9, O 2, S 5, Sch 11, U 3 / 10. Every other cell is empty (B C D F G H M N P Q R T V W X Y Z Ä Ö Ü checked).
   - Ort: J(I) 2, L 1, N 3 (the 3 sits clearly inside the N cell, right of the M/N rule), Z 4. All other cells empty.
   - This is identical to work/transcription.json. The 7 under K (hooked stroke) and the flagged 1s are unambiguous; the 9 under L is clearly 9, not 4.
3. Independent decoder `review/work/indep_decode.py`, built from my own reading (not from the solver's JSON): name LOUISEKALUSCHA, ort LINZ; position sequences 1..12 and 1..4 complete with no duplicate.
4. Method check: I read the printed example in the "Erklärung" column (review/work/example.jpg, rotated): A 2, C 1, E 6/8, J 7, L 4, M 5, R 3/9 → my decoder gives CARLMEIER, exactly the printed "Carl Meier". So the solver's interpretation of the grid (number = position of that letter in the name) is the card's own rule and is confirmed.
5. Address side (review/work/adr_small.jpg): "Wolgeboren Fräulein Käthi Mayrhofer in Kremsmünster Herrnstrasse", Kremsmünster arrival 25 6, 5 Heller Franz Joseph stamp intact with a duplex cancel. Agrees with SOLUTION.md. Linz is a plausible origin (~35 km) and matches the portal file name.
6. Coverage: every filled cell on the card is used; no handwritten mark in the grid is left unexplained (except the faint specks in finding 1).
7. Language: "Louise Kaluscha" is a normal Austrian name form of c. 1900 (Kaluscha = Germanised Kaluža); "Linz" is a real town. The printed verse is transcribed and translated correctly into English and Slovak.
8. Published-solution check: the portal shows status Not solved with no attachment; the solver reports a negative web search. I found nothing contradicting that.

## Findings

1. (minor) In the Ort grid, cells C and D (and the edge of E) carry faint grey specks/short strokes (review/work/ort_faint.jpg, contrast-enhanced 3x). They are not digits and not legible; they look like ink set-off or smudging, not writing. SOLUTION.md says "No other handwriting was found" without mentioning them. Suggest one line in the uncertainties noting these marks and that they do not read as numbers.
2. (minor) Steganography check: the human's note for this batch concerns Jolánka cards, where messages are hidden under the stamp. This card is not of that family and its stamp is still attached, so nothing can be said about the area under it. The solver already discloses this; keep it explicit in the report, and do not label the card "+ Steganography" since nothing hidden was found.
3. (minor) Type label: "Transposition" is in this run's allowed list and fits the mechanism (letters given alphabetically, numbers give their order). The report should say plainly that this is a printed commercial puzzle card with a self-explaining rule, i.e. no secret key, so readers do not overrate it.
4. (minor) "Kaluscha" as surname and the Louise|Kaluscha word division are by sense and cannot be checked against outside records; already disclosed in SOLUTION.md. No change needed beyond keeping it in the report.

## What I could not verify

- The area under the stamp (stamp intact).
- The sender's identity in outside records (Louise Kaluscha, Linz, 1900).
- The sender's postmark text: the duplex strike on the stamp is partial; I cannot read "LINZ" in it with certainty.
