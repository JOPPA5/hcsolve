ACCEPT

# hcp-1133 — Review round 1

Reviewer: Claude Opus 5.5, 2026-11-03. Solution under review: SOLUTION.md (round 1, Claude Opus 5.5), Morse code with a slash after each letter, International Morse plus É `..-..` and the writer's own Á `.-.--`.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1133/work/decode.py` (from the repo root). All four SHA-256 checks print OK. The output is exactly the claimed text:
   `B1 joined: VISELKENÉSELESUJTOTTTELJESEN`
   `B2 joined: REGGELVÁRTAMDÉLUTÁNHOGYÉRTSEMEZTKÉREMIRJONAZONNALAZÉGREKÉREMIRJONEGYLEVELET`
2. **Independent decoder.** `review/work/indep_decode.py` uses its own dichotomic-tree Morse table (no shared code with work/decode.py) and maps only É and the hypothesised Á as extras. Run: `python3 -I ciphers/hcp-1133/review/work/indep_decode.py ciphers/hcp-1133/work/morse_transcription.txt`. It gives the same two strings, and no group is left unknown (105 letter groups in all). Every group except the two Á occurrences is a standard International Morse letter or the standard Hungarian É.
3. **Transcription against the pixels.** I rotated the hi-res picture side 90° CCW myself (`review/work/rot.jpg`) and enlarged every Morse line 3x to 5x (`review/work/b1a.jpg`, `b1b.jpg`, `b1l1n.jpg`, `b1l2.jpg`, `b1l3.jpg`, `b2_0…b2_5.jpg`, `b2_left.jpg`, `l7.jpg`, `l7z.jpg`, `l7end.jpg`, `l9.jpg`, `l10.jpg`, `l11.jpg`, `l12.jpg`). I checked all 3 lines of B1 and all 14 lines of B2 sign by sign, and they agree with `work/morse_transcription.txt`. Specifically:
   - B1 line 1: the "N" of VISELKENÉSE (`b1l1n.jpg`, 5x) is a clear dash plus one dot followed by a slash. No second dot is hidden under the portal watermark. So "viselkenése" for "viselkedése" is a genuine writer's slip, and the solver discloses it correctly.
   - B1 line 2: `.---/-/---/-/-/` (JTOTT) is legible through the watermark "O".
   - B2 lines 2 and 4: the Á group is clearly dot, dash, dot, dash, dash both times (`b2_0.jpg`, `b2_1.jpg`). The writer's nonstandard Á is therefore read correctly, not forced.
   - The faint "thin tail ending in a dot" marks in lines 9 to 12 are visible as described. Read as dashes, they give AZONNAL, É and G, as the solver says.
4. **Plaintext.** Both Morse passages are fluent Hungarian of c. 1900 (`reggel vártam délután, hogy értsem ezt; kérem írjon azonnal, az égre kérem, írjon egy levelet`), and each runs on grammatically from the plain sentences around it. I spot-checked the plain parts against crops (`left_sziv.jpg`, `szepe.jpg`, `szepe2.jpg`, `bottom.jpg`, `bottom2.jpg`): "szívesen", "levelezőlapot azt írta, már nem küld", "De ne méltóztassék hinni, hogy én ily dolgokat egyhamar elfelejtek", "Öles betűkkel irotatt az bizonyos helyre", "Üdvözlettel Richter Antal" all agree with the pixels. The remaining residues ("Szépe(?)", "irotatt", "Jr.") are each a single word and are disclosed.
5. **Context.** Address side (`adr_small.jpg`): "Szépreményű Márthé Ilona kisasszonynak, Helyben, Jr. Eötvös utcza 7 sz.", with a 4-filler Turul stamp still attached. The postmark (`pm.jpg`) reads "…02 DEC 18", which agrees with the portal file name 1902-12-18. The dateline (`year.jpg`) clearly reads "1900". The solver reports both as written, which is correct.
6. **Published solution.** The portal shows Not solved, with no transcription or solution attached. I found nothing indicating that a published solution was used.

## Findings

1. **(minor) An undisclosed word-sense call in B2 line 7 (Z of "ezt").** The fourth mark of `--..` (`review/work/l7z.jpg`, 5x) is a short blob, about twice the length of a dot and half the length of a dash. Read as a dash, it would give `--.-` = Q ("EQT"). The Z reading is certainly right, but it rests partly on word sense, so it should be listed under the solver's uncertainty point 3 together with H and S.
2. **(minor) The list of faint dashes is incomplete.** Uncertainty point 2 lists five faint tail-plus-dot marks. There are at least two more of the same kind: the middle sign of R at the end of B2 line 7 (`l7end.jpg`: dot, faint tail and dot, dot = `.-.`) and the dash of A at the start of B2 line 9 (`l9.jpg`: dot, thin tail ending in a blob). Both are confirmed by the words (KÉR-EM, AZONNAL), so the reading does not change. The list should still be complete, or should say "for example".
3. **(minor) Slovak translation.** "na tom istom mieste" means "at the same place", but "az bizonyos helyre" means "to/onto that certain place". It should read something like "na isté miesto" ("Bolo to napísané obrovskými písmenami na isté miesto"). The English "in that certain place" is acceptable, though "onto" would be closer to the sublative -re.
4. **(minor) Address abbreviation.** "Jr." is left unexpanded. One possibility worth noting as a hypothesis only is a district abbreviation of Temesvár (for example Józsefváros). It is a single word, the address otherwise reads, and nothing needs to change beyond an optional note.
5. **(minor, informational) Steganography.** The stamp is still attached and covers part of the corner, so nothing under it can be checked. The solver discloses this. This card is not part of the Jolánka series, where hidden writing under the stamp is reported to be common. No hidden writing is visible in the picture or along the edges in my crops either, so no "Steganography" label is justified. The type label MASC/Morse, which is in the allowed list, fits.

## What I could not verify

- The area under the stamp. It is still attached, and no scan without the stamp exists.
- The exact meaning of "Szépe(?)" and of the address abbreviation "Jr.".
- Who Richter Antal and Márthé Ilona were (no external record found or searched beyond the solver's note).
- Why the dateline says 1900 and the postmark 1902. I can only confirm that both are read correctly.
