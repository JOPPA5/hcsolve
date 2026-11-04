# SOLUTION hcp-914 (HC Portal cryptogram 914) — round 1

Solver: Claude Opus 5.5, 2026-11-03. No earlier work exists on this number; the portal attaches no transcription or solution (status Not solved). A short web search found no published solution of this card.

## The card
Austrian picture postcard, printed "Herzlichen Gruss aus der Ferne sendet ..." puzzle card (Lith. u. Druck v. Fritz Schemm, Kunstanstalt, Nürnberg; "Gesetzlich geschützt"). Addressed in German Kurrent: "Wolgeboren Fräulein Käthi Mayrhofer in Kremsmünster, Herrnstrasse" (portal: Käthe Mayrhöfer). 5 Heller Austrian stamp; arrival postmark KREMSMÜNSTER 25 6; the card file name gives 1900-06-25, Linz → Kremsmünster.

## Cipher type and key
The card is a printed self-explaining name grid ("Erklärung"): the sender writes, under each printed Fraktur letter, the position(s) that letter occupies in his/her name ("Name des Absenders") and in the place of sending ("Ort"). The printed example is "Carl Meier". Cryptographically this is a transposition of the letters of the name: the letter set is given in alphabetical order and the hand-written numbers give their order. There is no secret key; the "key" is the printed rule. The printed grid has one cell for I/J (Fraktur J), one for "Sch", and separate cells for Ä Ö Ü.

Register type label: Transposition.

## Transcription (read from work/hires/…__pic.jpg, enlarged 3x)
Name des Absenders: A 8, 12 · E 6 · I/J 4 · K 7 · L 1, 9 · O 2 · S 5 · Sch 11 · U 3, 10. All other cells empty.
Ort: I/J 2 · L 1 · N 3 · Z 4. All other cells empty.
Positions run 1–12 and 1–4 with no gap and no duplicate, which checks the transcription.

## Plaintext (German)
Name: L O U I S E K A L U SCH A → **Louise Kaluscha**
Ort: L I N Z → **Linz**

Full message with the printed text: "Herzlichen Gruss aus der Ferne sendet Louise Kaluscha, Linz."

English: "Louise Kaluscha [from] Linz sends cordial greetings from afar."
Slovak: "Srdečný pozdrav z diaľky posiela Louise Kaluscha, Linz."

Printed verse (not ciphertext): "In der Ferne hab' ich Deiner gedacht, / Beweis soll die Karte hier bringen, / Doch willst Du wissen wer sie Dir gebracht, / Musst mit dem Buchstabieren beginnen." — EN: "Far away I thought of you; this card shall be the proof; but if you want to know who sent it, you must begin by spelling." SK: "V diaľke som na teba myslel(a); dôkazom nech je táto karta; ak však chceš vedieť, kto ti ju poslal, musíš začať hláskovať."

## Command
From the repo root:

    python3 -I ciphers/hcp-914/work/decode.py

It checks the SHA-256 of all four source images, checks the position sequences are complete, and prints LOUISEKALUSCHA and LINZ.

## Uncertainties
- I vs J: the grid has a single I/J cell; I is chosen by word sense in both fields (Louise, Linz).
- Word division of the name (Louise | Kaluscha) is by sense; the grid carries no space. "Kaluscha" is a plausible German-Austrian spelling of the Slavic surname Kaluža/Kalusa; it cannot be verified from the card.
- Digit shapes: the 7 under K has a crossbar-like hook and the 1s under L and in Ort L have a flag; both read clearly as 7 and 1, and the complete 1–12 sequence confirms them.
- The sender's postmark beside the stamp is a partial duplex cancel; Linz as the place of posting rests on the deciphered "Ort", the portal file name, and the visible fragments, not on a clean strike.
- The stamp is still on the card; nothing can be said about writing under it. No other handwriting was found on either side (picture, edges, explanation column inspected at 2–3x). The pencil "25 €" bottom right is a modern dealer price.

## Why I believe it is correct
Every filled cell is used; the positions form exactly 1..12 and 1..4; the result is a normal personal name and a real town that matches the card's posting data (Linz, Upper Austria, ~35 km from Kremsmünster). The method is the one printed on the card itself.

## Response to review 1

Verdict ACCEPT; no change to the reading. Reproduction command re-run on 2026-11-03 from the repo root: `python3 -I ciphers/hcp-914/work/decode.py` → `source hashes OK`, `name_des_absenders: LOUISEKALUSCHA`, `ort: LINZ`.

1. (faint specks in Ort cells C/D/E) Agreed, disclosure added. I looked at the reviewer's crops review/work/ort0.jpg and ort_faint.jpg: the marks are very faint grey, scattered, slanted strokes running across the C/D cell rule into E, much lighter than the brown-black ink of the real numbers (L 1, I/J 2, N 3, Z 4). They form no digit shape and look like ink set-off or smudging. They are not read as numbers; the Ort positions 1–4 are already complete without them, so even if they were writing they could not add a fifth letter consistently. Added to the uncertainties below and to the report.
2. (steganography / stamp) Agreed. The stamp is still attached, so the area under it cannot be inspected; nothing hidden was found anywhere else on either side. The card is not of the Jolánka family (where the human's note says hidden messages sit under the stamp), and the type label stays "Transposition", not "+ Steganography". Stated explicitly in the report.
3. (nature of the card) Agreed. The report says plainly that this is a printed commercial puzzle card (Fritz Schemm, Nürnberg) with a printed self-explaining rule and example, so there is no secret key.
4. (Kaluscha / word division) No change needed; kept as an uncertainty in the report.

### Uncertainty added after review
- Ort grid, cells C and D (edge of E): faint grey specks/short strokes, not legible, not digit-shaped; read as ink set-off/smudge, not as numbers. The earlier sentence "No other handwriting was found" should be read with this exception.
