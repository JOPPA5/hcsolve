ACCEPT

# Review 1 – hcp-951 (reviewer: Claude Opus 5.5, 2026-11-03)

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-951/work/decode.py` (from repo root): all four SHA-256 checks print OK, and the output is `ILSE SCHWARZE / DOBELN / BREITE / STRASE NR 19`. This matches the plaintext claimed in SOLUTION.md.
2. **Independent decode.** `review/work/my_decode.py` holds my own reading of the number block, taken from my own crops of the hires scan rather than from the solver's transcription file, and decodes it with A=1..Z=26. Output: `ILSE SCHWARZE / DOBELN / BREITE / STRASE NR S`. The only difference is the final 19. The solver keeps it as a literal house number. I agree with that, because the plain note on the card reads "Breitestr. 19". Alternatives I tested: line 3 starting with 9 gives IREITE (not a word), and splitting "18265" as 18,2,6,5 gives ARBFE (not a word). So the solver's splits are the only ones that give words.
3. **Transcription against the pixels.** I made my own autocontrast crops of the four cipher rows from `work/hires/..._adr.jpg` (`review/work/r1.png` to `r4.png`) and checked every number:
   - Row 1: `9,12,19,5 ; 19,3,8,23,1,18265` is confirmed. The 8 in "3,8" is open at the top (&-like) but has the same shape as the 8s in "18" on rows 3 and 4. The last group really is written "18265" with no commas, as the solver disclosed.
   - Row 2: `4,15,2,5,12,14` is confirmed.
   - Row 3: `2,18,5,9,20,5` is confirmed. The first sign is a looped 2 of the same shape as the 2 in "20" on the same row. It is not shaped like the 9 at position 4 of that row. The B reading rests on the shape and is also supported by word sense and the plain note.
   - Row 4: `19,20,18,1,19,5 ; 14,18 ; 19` is confirmed.
   - 30 enciphered numbers, all between 1 and 26, all decoded. Coverage is 100%.
4. **Plain parts.**
   - The greeting "Viele Grüße von hier, sendet Ihnen wohl bekannt, doch rätselhaft genannt" and the closing "Noch alles Gute zum Jahreswechsel" read as claimed (overview `review/work/adr_small.jpg`).
   - The plain ink note (`review/work/note.png`) reads "Ilse Schwar[ze…struck] / Döbeln i/S / Breitestr. 19" and confirms the decryption independently.
5. **Context.** Döbeln is in Saxony ("i/S"), which matches the picture side (Döbeln, Bürgergarten). Breite Straße is a street in central Döbeln. The 6 Pf Hindenburg stamp and the slogan cancel "Vermeidet Rundfunk-Störungen!" fit 1940. The New Year wish fits the portal date of 5 January 1940. The German is natural for the period.
6. **Steganography check** (the human's note that some series hide text under the stamp). The picture side (`review/work/pic_small.jpg`) shows only the printed caption and the portal watermark. In the stamp box and the area above the slogan cancel (`review/work/topright.png`, and `review/work/purple.png`, a blue-minus-green channel difference), I see only a few faint violet specks and one short violet stroke left of the stamp. None of them forms letters or digits; they look like stray marks or ink transfer. Nothing written under the stamp can be checked from a scan. The solver disclosed this.
7. **Published solution.** The portal status is Not solved and the portal attaches no solution. The solver's search found nothing. I found no sign that a published solution was used.

## Findings

1. **minor – pencil remark: the unread word can be narrowed.** On my 2x crop (`review/work/pencil_word.png`) the word after the article clearly ends in "-fräulein": there is an ä with two dots, followed by u-l-e-i-n. The first part has a p with a long descender, then r/o and a looped letter. "Probe-" and "Post-" are both possible, but neither is certain. The article is half covered by the ink descender of the line above. A defensible reading is "Kennst du das/die […]fräulein [aus] Döbeln? !?", which means the remark asks whether he knows the young lady from Döbeln. The solver should write it as "[…]fräulein" rather than leaving the whole word unread.

   This is one word in a later pencil remark, outside the sender's message, and the rest of the line reads. Under the run's rule it does not make the card partial.
2. **minor – destination town.** The address clearly reads "Stürzbach". The real Thuringian Forest locality is Stützerbach, which is probably the place meant. SOLUTION.md and the report should mention this and not imply that "Stürzbach" is an attested place name.
3. **minor – undisclosed faint violet marks.** There are faint violet marks above the slogan cancel and to the left of the stamp, about x 2140–2200 and 2600–2750, y 60–420 in the hires scan. They are not mentioned. They do not read as text, but one sentence in the uncertainties would show the solver looked at them.
4. **minor – register type.** The type is MASC (A=1..Z=26). No steganographic content was found, so "MASC + Steganography" does not apply here.

## What I could not verify

- Whether anything is written under the stamp; it cannot be lifted from a scan.
- The exact first half of the pencil word, and its article.
- The identity of Ilse Schwarze and Hugo Dunkel.
