ACCEPT

# Review 1 — hcp-974 (Bad Brückenau → Emma Krumbholz, Heidelberg)

Reviewer: Claude Opus 5.5, 2026-11-03.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-974/work/decode.py` from the repo root: all four SHA-256 checks print OK; the output is identical, line by line, to the plaintext in SOLUTION.md (`mein zustand ist / bedeutend ge / besert. eiweis / ist fast ganz / weg. eiter fin" / det der arzt / keinen mehr. / waser ist ganz / hel! morgen- sams" / tag nachmitag-`).

2. **Independent transcription and decoding.** I rotated the un-converted hi-res address side myself (`review/work/crop.py`, output `review/work/msg_full.png`, overview `review/work/msg.png`) and wrote down the ten lines from my own reading, before comparing with `work/transcription.txt`. I derived the key on my own from the cribs (K23828 = keinen, 30T = ist, D29 = der, H26 = hel, 72H9 = mehr, 749G28 = morgen) in `review/work/my_decode.py`. Output:

   ```
   mein zustand ist / bedeutend ge / besert. eiweis / ist fast ganz / weg. eiter fin- /
   det der arzt / keinen mehr. / waser ist ganz / hel! morgen- sams- / tag nachmitag-
   cipher signs 76 plain letters 40 total 116
   ```

   My transcription matches the solver's sign for sign (116 letter tokens, 76 of them digits). The key 1–5 = a e i o u, 6–0 = l m n r s is consistent. All ten digits occur, each always gives the same letter, and no sign is left over. A, E, I, O, U, L, M, N, R, S never occur as plain Latin letters. The plain letters are only b c d f g h k t w z, so the split between digits and plain letters holds across the whole card.

3. **Sign-level checks on enlarged crops** (`review/work/l1.png`, `l4.png`, `l5.png`, `l9.png`, `l10.png`, 1.5–2x of the hi-res):
   - Line 1 "7238 Z50T18D 30T": the 7 has a crossbar and no foot curl. This matches 7 in mehr, Morgen, Samstag and nachmitag.
   - Lines 4 and 5, "F10T" and "F38"": the F has a crossbar and a hooked J-tail at the foot, which is clearly unlike the 7. The solver's 7/F distinction is visible on the pixels.
   - Line 9 "H26! 749G28- 0170"": clear. The final mark is a continuation sign.
   - Line 10, "81?H73T1G-": the sign after "81" has a small lower-left loop that runs into a C-like body. It could be taken for a 6 joined to something. Taken as 6 (= l) it gives "nalh", which is not German. The only reading that makes a word is a looped Latin capital C ("nach"). This call rests on word sense, and SOLUTION.md (Uncertainty 1) says so. I agree with it.
   - Line 8: the big ink blot sits on the 0 of "30T". The 3 and the T are clear and "ist" recurs, so the reading is safe.

4. **Stamp box and picture side** (with the colleagues' note in mind that hidden messages sit under stamps on some series). My enhanced crop `review/work/stamp_enh.png` (autocontrast plus contrast) shows that the stamp is lost. Only glue stains and the BRÜCKENAU postmark are left, with no writing in the box. The picture side (source/picture-large.jpg) has only the printed caption "Bad Brückenau / Kgl. Kurhaus" and a collector's "3". I found no steganographic part, so plain MASC is the right type, not "MASC + Steganography". One limit: what was under the lost stamp cannot be checked.

5. **Language and context.** The text is fluent German of around 1900–1910: a spa patient's health report (albumin almost gone, no more pus, urine clear). Bad Brückenau was a spa for kidney and bladder complaints, and the picture shows its Royal Kurhaus. The writer consistently writes a doubled letter only once (besert, Eiweis, Waser, hel, nachmitag), and SOLUTION.md says so. The translations are accurate.

6. **Sources.** The portal shows status Not solved and attaches no solution. I found no sign that a published solution was used. The card is outside skip.txt, and per the orchestrator's check it has no register record.

## Findings

1. **minor — wrong sign count.** "Why it is correct" says "All 94 cipher/plain signs". The solver's own `work/transcription.txt` has 116 letter tokens (76 digits plus 40 plain letters), and my count agrees: `grep -v '^#' work/transcription.txt | tr ' ' '\n' | grep -E '^[0-9A-Z]$' | wc -l` → 116. Please correct the figure.

2. **minor — "C" in "nach" rests on word sense.** It is disclosed, and I agree with the reading. The report should keep the sentence that this one sign is read from sense, not from its shape.

3. **minor — date.** Only "27" of the postmark is legible, and "09" is the publisher's print code. The report should give "c. 1909" as an estimate only, as SOLUTION.md already does.

## What I could not verify

- Whatever was under the stamp, which is now lost.
- The postmark date and year.
- The recipient's surname "Krumbholz" and the street "Mittelstr. 18". They look right on the scan, but they come from the handwritten address, not the cipher.
- The sender's identity, since the card is unsigned.
