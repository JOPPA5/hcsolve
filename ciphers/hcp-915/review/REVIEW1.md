ACCEPT

# Review 1 – hcp-915 (Ogham, "Tabhair dom póg")

Reviewer: Claude Opus 5.5, 2026-11-03. Solution under review: SOLUTION.md round 1 (Claude Opus 5.5).

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-915/work/decode.py` from the repo root: all four SHA-256 checks pass; output `dabair dom pog.` / `dabhair dom póg.`, identical to the claimed plaintext.
2. **Own transcription from the pixels.** I cropped the Ogham strip from work/hires/cpc_--_IE_____pic.jpg (3410x2265), turned it 90 degrees counter-clockwise (then the Ogham and the Gaelic-script line both read left to right) and enlarged each word 3–4x (review/work/strip_ccw.jpg, z_word1.jpg, z_word23.jpg, z_word3b.jpg, z_script.jpg). Sign by sign:
   - word 1: two strokes above only (D); one stroke across (A); one stroke starting at the stem and going below only (B); one stroke across (A); five short strokes across (I); five slanted strokes across (R); a dot above.
   - ":" separator.
   - word 2: two strokes above only (D); two strokes across (O); one slanted stroke across (M).
   - ":" separator.
   - word 3: a horizontal bar above the stem, not touching it (P by word sense); two strokes across with an acute above (Ó); two slanted strokes across (G); final dot below the stem.
   This matches the solver's transcription `H2 X1 B1^ X1 X5 M5 : H2 X2 M1 : P X2' M2 .` exactly.
3. **Own decoder.** review/work/verify.py (independent code, standard Ogham table, my own group list) prints `groups: 12 decoded: dabhair dom p?óg.` – same reading; only the bar (p) is not part of the standard table.
4. **Plain Gaelic-script line.** Read at 2x: Ꞇaḃaıꞃ ḋom póᵹ = "Tabhair dom póg", with a dot between b and a (lenition), a dot over d of "dom", an acute over o. It duplicates the Ogham and translates the printed caption "Give me a kiss" (the green caption above it is the play title "Arrah na Pogue").
5. **Coverage.** Every mark on the picture side is accounted for: 12 letter groups, 2 separators, final dot, lenition dot, acute. No writing elsewhere on the picture side.
6. **Address side / steganography.** The address side is blank: no address, no message, the printed STAMP box is empty and no stamp was ever affixed, so nothing can be hidden under one; nothing along the edges. The picture itself shows no added writing at this resolution. (The human's note about hidden messages under stamps concerns the Arokszállás/Jolánka series and does not apply to this Irish card, which has no stamp.)
7. **Language / context.** "Tabhair dom póg" is correct Irish for "Give me a kiss"; "dom" (older ḋom) is the normal prepositional form. Translations EN "Give me a kiss", SK "Daj mi bozk / Pobozkaj ma" are correct. Card: Lawrence, Dublin, undivided back ("The address to be written on this side"), consistent with c. 1900–1905; the solver's c. 1900–1910 is acceptable.
8. **Published solution.** The portal attaches none (status Not solved); the solver says so. I found no reason to think a published solution was used.

## Findings

1. **minor – first letter D vs T.** The first Ogham group clearly has two strokes above (D), not three (T). The solver reports this honestly and takes T only from the parallel plain line and word sense. Agreed; nothing to fix.
2. **minor – P as a bar is non-standard.** A horizontal bar above the stem is not a standard Ogham letter; reading it as p rests entirely on word sense ("póg") and the plain line. Disclosed (uncertainty 4). Nothing to fix.
3. **minor – dot position in word 1.** In the Ogham the lenition dot sits slightly to the right of the second a-stroke (above the a/i area), not "above the gap between the b-stroke and the following a-stroke" as SOLUTION.md says; in the script line it sits between b and a. The assignment to b is from spelling, which is fine, but the description of the Ogham position should be corrected or worded as "after b, not directly over it".
4. **minor – "17 groups" count.** SOLUTION.md says 17 stroke groups; the transcription has 12 letter groups plus 2 separators and 1 final dot (15 tokens), plus 2 diacritic marks. Fix the number or say what is counted.
5. **minor – decode.py prints the script line as a constant.** The Gaelic-script reading is hard-coded in the print statements rather than produced from a transcription; this is acceptable since that line is unenciphered, but the report should say it is a manual reading, not computed output.
6. **note for the register entry.** Type label MASC is acceptable (Ogham used as a fixed-script substitution, 1:1 letters). There is no steganography on this card, so "MASC + Steganography" should not be used here.

## What I could not verify

- The writer, date and recipient: the card is unused and unaddressed; dating rests only on the printed card.
- Whether the 2-stroke first letter is a deliberate convention of the writer or a slip; with only one such letter on the card it cannot be decided.
- Faint writing invisible at the scanned resolution cannot be excluded, but nothing is visible in the picture or the stamp box.
