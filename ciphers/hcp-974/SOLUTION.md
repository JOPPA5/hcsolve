# hcp-974 — Solution (round 1)

Solver: Claude Opus 5.5, 2026-11-03. No earlier work on this number; no published solution found (portal status Not solved, no attachment; one web search for the plaintext phrase found nothing).

## Card
Picture postcard "Bad Brückenau, Kgl. Kurhaus" (publisher Hans Brust, Brückenau, print code 09 27113). Postmark BRÜCKENAU BAD ...27 (year not legible; print code suggests c. 1909). Addressed in plain German Kurrent to "Frau Emma Krumbholz, Heidelberg, Mittelstr. 18" (surname and street read from Kurrent, letters of "Krumbholz" partly by sense; portal: "Emma Kr"). The message is written sideways on the left half. The stamp is missing; the stamp box (enhanced crop work/crops/stamp.png) and the picture side show no hidden writing — only the collector numbers "3)" / "3". Faint later pencil letters (a collector's decoding attempt, e.g. "e u n" over line 3) are not part of the message.

## Cipher type and key
Partial monoalphabetic substitution (MASC): the ten letters a e i o u l m n r s are replaced by digits, all other letters are written plain in Latin cursive.

| digit | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|
| letter | a | e | i | o | u | l | m | n | r | s |

(the five vowels in order, then l m n r s in alphabetical order). Plain letters used: b c d f g h k t w z. The writer writes doubled letters once (gebesert, Eiweis, Waser, hel, nachmitag) — this is a feature of the ciphertext, every such word shows a single sign.

## Command (from repo root)
    python3 -I ciphers/hcp-974/work/decode.py
Checks SHA-256 of the four images, then decodes work/transcription.txt with the key.

## Plaintext (as written, line by line)
    mein zustand ist / bedeutend ge- / besert. eiweis / ist fast ganz / weg. eiter fin- / det der arzt / keinen mehr. / waser ist ganz / hel! morgen- sams- / tag nachmitag-

German, normalised: Mein Zustand ist bedeutend gebessert. Eiweiß ist fast ganz weg. Eiter findet der Arzt keinen mehr. Wasser ist ganz hell! Morgen – Samstag Nachmittag –

English: My condition has improved considerably. The albumin is almost completely gone. The doctor finds no more pus. The urine ("water") is quite clear! Tomorrow – Saturday afternoon –

Slovak: Môj stav sa výrazne zlepšil. Bielkovina je takmer úplne preč. Hnis už lekár nenachádza. Moč („voda") je celkom čistý! Zajtra – v sobotu popoludní –

## Uncertainties
1. "nach" (line 10): the sign before H is a looped form that starts like a small 6 and runs into a capital-C body. Read as one looped Latin capital C (giving "nach"); reading it as digit 6 (= l) would give "nalh", which is not a word. This one call rests on word sense.
2. 7 (= m) vs plain F: both are crossed long strokes; F has a curled J-tail at the foot (fast, findet), 7 has none (mein, mehr, Morgen, Samstag, nachmitag). Distinguished on the pixels, consistent with sense.
3. The message ends with a dash after "nachmitag": the sentence (presumably announcing arrival or a visit) is left unfinished by the writer, not lost. Nothing is missing at the card edge.
4. Line-end marks: " after "fin" and "sams" are continuation marks; "G2" at the end of line 2 continues as "ge-besert" without a mark.
5. Sender unsigned; recipient's surname "Krumbholz" from the Kurrent address is a reading, not ciphertext.

## Why it is correct
All 116 letter signs of the message (76 digit cipher signs plus 40 plain Latin letters; corrected from "94" after review 1) are decoded with one ten-digit key; there are no leftover signs. The key is systematic (vowels a–u = 1–5, then l m n r s = 6–0). The result is fluent German with a coherent medical subject (albumin, pus, urine — typical of a kidney/bladder cure) written from a spa (Bad Brückenau was a spa for kidney and bladder complaints), and recurring words decode identically (ist ×3, ganz ×2).

## Response to review 1

Verdict ACCEPT, three minor findings; the reading is unchanged.

1. Wrong sign count (minor) — fixed. "Why it is correct" now says 116 letter signs (76 digits + 40 plain letters). Re-counted from work/transcription.txt: 116 tokens; digit frequencies 1:10, 2:20, 3:10, 4:1, 5:2, 6:1, 7:5, 8:10, 9:7, 0:10 (= 76).
2. "C" in "nach" rests on word sense (minor) — agreed; kept as Uncertainty 1 and stated the same way in report/report.md.
3. Date (minor) — agreed; the report gives the date only as "27" of an unreadable month/year and "c. 1909" as an estimate from the publisher's print code "09".

Stamp box re-checked by the solver after the human's note that some postcard series carry a hidden message under the stamp: on the address scan and review/work/stamp_enh.png the stamp is lost and the box shows only glue stains and the BRÜCKENAU postmark, no writing; the picture side has only the printed caption and the collector's "3". Type stays MASC (not MASC + Steganography); what was under the lost stamp cannot be checked.

Reproduction re-run after the edits: `python3 -I ciphers/hcp-974/work/decode.py` — four SHA-256 checks OK, output identical to the plaintext above.
