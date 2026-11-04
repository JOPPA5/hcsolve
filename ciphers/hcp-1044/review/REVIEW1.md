ACCEPT

# Review 1 – hcp-1044 (Fritz Lehmann, card 16)

Reviewer: Claude Opus 5.5, 2026-11-03. Round 1, after DONE1.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1044/work/decode.py` (repo root): the SHA-256 checks of all four images print OK and
   the output is exactly the plaintext claimed in SOLUTION.md (ACH FRITZE MACH MIR / BLOSZ KEIN KIND / DENN DU WEISZT WIE / MEINE
   ELTERN SIND MACH / MIRS SPA"TER ODER FRN"HER / MIT DEM ALTEN N"BERZIEHEN / LIESE).
2. **Independent decoder.** `review/work/mydecode.py` (my own table A=2 … Z=26 without J, built from the alphabet string, not copied
   from the solver), run on the number lines of work/transcription.txt (`review/work/t.txt`): same output, letter for letter. All
   numbers used fall in 2–26, and every group maps to a letter; nothing is left over.
3. **Transcription against the pixels.** From the hi-res address scan in work/hires/ I made my own crop of the message block,
   rotated 90 degrees (`review/work/msg_rot.png`, quarters q0–q3.png) and 4x enlargements of the doubtful places (z_l1.png,
   z_l5a.png, z_l3_l4.png, z_fruh.png, z_uber.png, z_sig.png). I read every group of all six lines and the signature against the
   transcription; all 39 groups agree. Specific checks:
   - Line 1 "7.18.10.20.26.6" (FRITZE): the first sign is this writer's 7 (top bar plus downstroke), clearly different from the
     closed 4 of 2.4.9 (ACH) just before it.
   - Line 5 group 1 = 13.10.18.19 (MIRS): at 4x the third number has the lower 8-loop and the fourth number a closed upper loop with
     a descender (9), unlike the open crossed 4s of DENN (5.6.14.14) on line 3. The solver's correction from "MINN" is right.
   - Line 4 MEINE: the fourth number is under a heavy blot; a "1" and a crossed 4-shape are discernible, so 14 is supported, though
     partly helped by the word (see finding 3).
   - FRÜHER (7.18.14".9.6.18) and ÜBERZIEHEN (14".3.6.18.26.10.6.9.6.14): in both places the sign under the two dots is the open,
     crossed 14, not 21 (U in DU = 5.21). The 14" reading is what is written; the normalisation to Ü is by word sense and is
     disclosed (Uncertainty 1).
   - KIND: large retraced final 5, still a 5. SPÄTER: 2 with two dots above, as transcribed.
   - Signature 12.10.6.19.6: the fourth number has a closed loop and a descender like the 19 of MIRS; LIESE is the better reading,
     LIENE disclosed as alternative.
4. **Rest of the card.** Picture side (hi-res): printed photo card "Lieb' mich, und die Welt ist mein!" with a printed verse and
   KVG 2130/5; no handwriting in the picture, margins or verse area. Address side: stamp box empty and unused (no stamp, so no
   hidden writing under a stamp is possible on this scan), plain "Herrn Fritz Lehmann, Hier." plus a small pencil tick before
   "Herrn"; nothing else written. The whole card is accounted for.
5. **Language and context.** The plaintext is grammatical colloquial German (Fritze as Berlin/Silesian diminutive, "bloß",
   "mach mir's") and consistent with the other Lehmann cards (same key, same recipient, local "Hier" delivery). Key identical to
   the table in hcp-1113/SOLUTION.md (checked).
6. **Sources.** Portal shows Not solved, no transcription or solution attached. I found nothing indicating use of a published
   solution.

## Findings

1. **minor – sister cards called "finished".** SOLUTION.md says the key was "established on the finished Lehmann sister cards
   hcp-1113, hcp-1134 and hcp-1051". None of these has a FINAL marker (all are at REVIEWED1). The key works here on its own
   evidence, so this only needs rewording ("reviewed sister cards" or "sister cards in progress").
2. **minor – sentence division of lines 5–6 is editorial.** The card has no punctuation. SOLUTION.md splits it into "Mach mir's
   später oder früher mit dem Alten. Überziehen!" An equally natural reading is one clause, "mach mir's später oder früher mit dem
   Alten [= dem alten Überzieher?] überziehen", or similar. The letters are not in doubt, but the report should present the
   division and the meaning of "mit dem Alten" as interpretation and give the one-clause alternative. The English "Do it to me
   later or earlier" also leaves "später oder früher" opaque; say that its sense is unclear.
3. **minor – MEINE rests partly on word sense.** The blot covers most of the second digit of the fourth number. The visible
   strokes support 14, but the reading is also chosen because MEINE fits. Uncertainty 4 should say that.
4. **minor – no web search recorded.** SOLUTION.md says no web search was made. The orchestration allows a short search, and the
   portal links the HistoCrypt paper on the Schrödel collection (SOURCES.md). Either run the search or state in the report that
   it was not run. This does not affect the decipherment.

No blocker or major findings. The register type MASC is correct (number substitution; no steganography on this card).

## What I could not verify

- The physical card: only the scans. If anything is under the paper, or written in invisible ink, the scans do not show it.
- The intended meaning of "mit dem Alten" and of "später oder früher"; the letters are certain, the sense is not.
- Whether the writer meant 14" as a deliberate Ü sign or made a slip; both readings give the same plaintext.
- Date and place: the card has no postmark.
