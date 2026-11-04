ACCEPT

# Review 1 — hcp-916 (reviewer: Claude Opus 5.5, 2026-11-03)

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-916/work/decode.py` from the repo root: all four SHA-256 hashes OK. The output is exactly the one claimed in SOLUTION.md:
   `B joined: ILUSKÁMDRÁGAMIKORLÁTHATOM?KÉREMARANYOMÍRJON` / `T joined: MILLIOFORROCSOKÉDESEMNEK`.
2. **Independent transcription and decode.** I rotated the hires picture scan myself (`review/work/rot.jpg`), cut my own crops of every Morse line at 2–5x (bottom block: `review/work/L1_*.png`, `B_*.png`, `z_L2L.png`, `z_L3end.png`, `z_hook.png`, `B3R.png`; diagonal block rotated a further 53° and 57°: `top_rot*.png`, `T_*.png`, `T3start2.png`, `T3s_z2.png`, `T2s_z2.png`, `T23end.png`, `T3N.png`), and read every group again. My own table-driven decoder `review/work/my_decode.py`, which uses only standard International Morse plus É and flags non-standard groups, gives:
   ```
   B1 ILUSKÁ*MDRÁ*GA
   B2 MIKORLÁ*THATOM?
   B3 KÉREMARANYOM
   B4 <[hook]>RJON
   T1 MILLIOFOR
   T2 ROÄ(std)SOK
   T3 ÉDESEMNEK
   ```
   (Á* = the writer's `.-.--`, Ä(std) = the standard meaning of `.-.-`). Apart from the two flagged points, which the solver discloses, this agrees group for group with `work/morse_transcription.txt`.
3. **Signs I checked on the pixels.**
   - Bottom line 1: all three `.-.--` groups (ILUSKÁM, DRÁGA) have five elements. The dash cut by my crop boundary is the same dash that starts the next crop, so the overlap does not add one.
   - Bottom line 2: L in MIKOR**L**ÁTHATOM is clearly `.-..` with four elements (5x crop `z_L2L.png`), not `.-...`. The Á of LÁTHATOM is `.-.--`. The "?" is a hand-written question mark.
   - Bottom line 3: K, É `..-..`, R, E, M, A, R, A, N, Y `-.--` (`z_L3end.png`), O, M are all clear.
   - Bottom line 4: the first mark (`z_hook.png`) is a long horizontal stroke ending in a short down-slant with a tick, with a separate dot above it. It is not a Morse group. It reads most naturally as a cursive "í" with its accent, which supports the solver's Í. Then `.-./.---/---/-./` = RJON.
   - Diagonal line 1: `--/../.-../.-../../---/..-./---/.-./` = MILLIOFOR.
   - Diagonal line 2: the start is `.-.` = R (`T2s_z2.png`). C is `.-.-` with four separate, unambiguous elements. S, O, K follow.
   - Diagonal line 3: the start is `..-..` = É (`T3s_z2.png`, under the HCPORTAL overprint). N before EK is `-.` (`T3N.png`). The blotted middle dot of S is a single dot.
4. **Key coverage.** The whole Morse text is covered by one key: International Morse, Hungarian É, and the writer's `.-.--` for Á (three occurrences here, two on hcp-1133, all confirmed by the word). Only C = `.-.-` (one occurrence) and the Í mark depart from it, and both are disclosed as resting on word sense.
5. **Language and context.** "Iluskám drága, mikor láthatom? Kérem aranyom, írjon. Millió forró csók édesemnek." is natural Hungarian of c. 1904. Iluska/Ilus is the usual pet form of Ilona, the addressee's name on the address side ("Márthé Ilona úrhölgynek", which I confirmed on `review/work/adr_small.jpg`). The English and Slovak translations are correct.
6. **Dateline and postmark.** On my crops (`date.png`, `date2.png`) the dateline reads "T[superscript]v. 904 III./1.", and the postmark (`stamp.png`) reads "...90(4) APR 1". The month mismatch is disclosed.
7. **Stamp.** The 5-filler stamp is still on the card, so nothing under it can be inspected, and the solver says so. No writing shows at the stamp edges in my crop. (The human's note about steganography under stamps refers to the Jolánka series; this card is not in that family and its stamp is not removed.)
8. **Sources.** Portal status is "Not solved" with nothing attached. The key family is the solver's own sister card hcp-1133, which is credited. I found no undisclosed use of a published solution.

## Findings

1. **minor — undisclosed stray marks in bottom line 3.** Before R of ARANYOM a small isolated dot sits below the separator, and there is an ink blob on the separator after that R (`review/work/B3R.png`). Neither changes the reading, but Uncertainty 3 lists stray dots only for line 2. Add these for completeness.
2. **minor — top line 2 has no closing "/".** After the final `-.-` (K of CSÓK) no separator stroke is visible (`review/work/T23end.png`). The transcription file writes `-.-/`. This is harmless to the decode, but the transcription should match the card, or a comment should note it.
3. **minor — HCPORTAL collection overprint.** The modern "HCPORTAL.EU · Collection: Tobias Schrödel" stamp overlies the start of all three diagonal lines and the monogram. The readings beneath it are still clear on enlargement, but the report should mention that this overprint is modern and not part of the original.
4. **minor — monogram.** I agree that it cannot be read with confidence. To me it looks like a cursive capital A crossed by a stroke, with a looped second letter (possibly R) (`review/work/mono.png`). That would be compatible with "Antal Richter" of hcp-1133, but it is only a hypothesis and the solver is right not to claim it. A signature monogram is a single unread item, so it does not make the card partial.

## What I could not verify

- Whether anything is written under the stamp (stamp still attached).
- The exact reading of the superscript in "Tv." and therefore the expansion "Temesvár". It is plausible, given the Temesvár postmark and address, but it is an interpretation.
- The true identity behind the monogram.

## Register

MASC/Morse is an allowed label and fits the card. No steganography can be demonstrated on this card, so "MASC + Steganography" would not be justified. The reading is complete, apart from a disclosed one-letter word-sense call and the monogram, so a register entry is appropriate.
