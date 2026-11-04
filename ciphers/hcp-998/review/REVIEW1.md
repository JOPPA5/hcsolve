ACCEPT

# Review 1 of hcp-998 (Claude Opus 5.5, reviewer, 2026-11-03)

## What I verified and how

1. **The solver's command.** `python3 -I ciphers/hcp-998/work/decode.py` runs from the repo root. Both source image hashes come out OK, and the output is identical to the plaintext claimed in SOLUTION.md: "mein sophin — vielen vielen dank für deinen lieben brief, sobald ich zeit habe schreibe ich dir. einstweilen sei zärtlich geküsst mein liebstes von deiner tr. freundin magda."

2. **Independent transcription and decode.** I rotated the hi-res picture side (`work/hires/…__pic.jpg`, 3469x2298) by 90° and cut it into overlapping two-line tiles (`review/work/L0a.jpg` … `L4b.jpg`, plus zooms `z_*.jpg`). I read every sign of all 9 cipher lines from these tiles myself and wrote the result down with my own sign names in `review/work/my_decode.py`. My reading gives 142 letter signs and 27 sign types, the same counts as the solver's. Decoding it gives exactly the solver's plaintext, character for character. The key covers every sign on the card. No sign is left unread or unused.

3. **Sign checks on the pixels (enlarged):**
   - t (lambda-like) and b (plain vertical stroke) are clearly different shapes ("zeit", "einstweilen", "zärtlich", "küsst", "liebstes" against "lieben", "brief", "sobald", "habe", "schreibe", "liebstes"). The key is not built on a merged sign.
   - d (long slanted stroke) and g (short horizontal stroke) are different. "Magda" shows both side by side, as `- /`, and "ge=" in line 6 is a horizontal stroke.
   - The two ü signs really are different. In "für" (line 2) it is a cup with a diaeresis. In "küsst" (line 7) it is a circle with an inner loop and a diaeresis. Both are single occurrences, and the solver discloses this.
   - The π-shaped l occurs only in "-len" (line 6). Elsewhere l is written T. This homophone is disclosed.
   - "Sophin": the last sign of the word is the same 6-shaped n as in "mein" and "vielen", not the circle e. The solver reports the word as written, which is correct.
   - The dash after "Sophin" is much longer than the g stroke. Reading it as punctuation is right.
   - The comma after "brief" is a slanted stroke that sits low, between lines 3 and 4. No word divider ∫ appears there. Reading it as a comma that also divides the words is plausible.
   - The diaeresis on x in "zärtlich" and the `=` hyphen marks under "schrei=", "einstwei=" and "ge=" are visible.
   - The date line "Am 25.11.01." is in plain Kurrent, as the solver says.

4. **Language and context.** The text is ordinary, idiomatic German of a 1901 friendship postcard. The key words are spread over the whole card, and frequent signs recur in independent words (mein x2, vielen x2, ich x2, deinen/deiner, lieben/liebstes). This rules out text forced onto noise. The addressee on the address side is Fräulein Sophie Goes, which matches "Sophin". The postmark dates fit the date line of 25.11.01.

5. **Steganography / stamp.** I looked at the stamp area at full resolution (`review/work/adr_stamp.jpg`). The 5-Pf Germania stamp is affixed and intact, and I found no writing around it, along the edges, or inside the painted picture. Unlike the Jolánka series, no hidden message is visible. What lies under the stamp cannot be checked from a scan, and the solver says so. The register type is therefore MASC, not "MASC + Steganography".

6. **Published solution.** The portal shows Not solved, with no transcription and no solution attached. I found no evidence that the solver used a published solution.

## Findings

1. **minor – the left postmark is mis-attributed.** SOLUTION.md (lines 6 and 50) calls the "26.11.01 7-8V" strike at the left of the address side a second BERLIN strike. My crop (`review/work/adr_leftpm.jpg`) shows only the end of the town name at the top of the ring, and those letters read "…CH", not BERLIN. This fits RIMBACH: the card arrived at Rimbach on 26.11 7-8V, was redirected the same day (postman's note "26/11") and reached Zwingenberg on 27.11. Please correct the description, giving the town name as only partly visible. The Berlin strike on the stamp is a separate strike, and its date is mostly covered.

2. **minor – the blue forwarding word.** In my crop (`review/work/adr_blue.jpg`) the word has the letter shapes n-a-ch-g-ſ-ch, so a reading "nachgesch[ickt]" followed by "26/11" is plausible. The solver already marks this word as not securely read. It is a single postal word, not part of the message, so it does not make the card partial. Optional: name "nachgesch[ickt]" as the likely reading.

3. **minor – the name in the translations.** The English and Slovak translations put "Sophie" / "Sofia" without comment, although the cipher has "Sophin". Add "(written 'Sophin')" or similar so the translation does not silently correct the text.

4. **minor – "tr."** Expanding it to "treuen" is conventional and is disclosed. No change is needed beyond keeping it bracketed, as it already is.

## What I could not verify

- Whether anything is written under the stamp (it is affixed; a scan only shows the front of the stamp).
- The exact readings of the purple Kurrent forwarding notes ("Diefenbach", "Schmitt"). They are postal handling, not message text, and the solver discloses them as partly read.
- The town name in the left postmark is only partly visible (see finding 1).
