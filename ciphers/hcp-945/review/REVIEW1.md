ACCEPT

# Review 1 — hcp-945 (Hagen i.W. → Frieda Necker, Malchow, 30.4.1898)

Reviewer: Claude Opus 5.5, 2026-11-03. Solver: Claude Opus 5.5 (same day).

## What I verified and how

1. Solver command, run from repo root: `python3 -I ciphers/hcp-945/work/decode.py`
   Output: "source hashes OK", then `meine liebe frieda / reise heute nach / neheim hüsten / dein eduard`, the same as the plaintext in SOLUTION.md.
2. Independent decode: `review/work/my_decode.py`. I wrote my own sign transcription from the enlarged crops, using my own sign names, and my own key. Output: the same four lines. 19 sign types and 52 tokens. Every token maps, with no residue.
3. Pixels: I cropped the 3469x2298 original (`work/hires/..._pic.jpg`) line by line and enlarged it 2–4x (`review/work/line1..4*.jpg`, `l3mid.jpg`, `l2mid.jpg`). I checked every sign, as follows:
   - L1 `3 IV . 2 IV | ʃ . II 6 II | 7 4 . II V I`. The long ʃ (l), the long 7 (f), the 6 (b) and the curled II in "Frieda" are all clearly visible. Meine liebe Frieda.
   - L2 `4 IV . ʔ II | 8 IV IIII 1 II | ℓ X c 8`. The first sign of "nach" is the filled-loop variant of 2. The c is a small hook. Reise heute nach.
   - L3 `ℓ/2 VI 8 IV . 3 | 8 IIIÏ ʔ 1 II 2`. The diaeresis over the barred four strokes is plainly visible (l3mid.jpg). The final 2 is in a lighter brown ink, as disclosed. Neheim Hüsten.
   - L4 `V IV . 2 | II V IIII X 4 V`. Dein Eduard.
4. Address side: plain Kurrent "Fräulein Frieda Necker in Malchow in Mecklenburg". The postmarks are HAGEN (WESTF.) 30.4.98 and MALCHOW 1.5.98. The pencil marks "22" and "100" are dealer marks. I saw no writing in the stamp area or along the edges. The picture side has no other added writing in the vignettes or along the borders.
5. Language and context: the text is ordinary German of the period. The greeting matches the addressee. Neheim and Hüsten are real neighbouring Ruhr towns about 50 km east of Hagen.
6. Honesty: the portal shows Not solved, with no transcription or solution attached. The solver states that no published solution was used and that no web search was made.

## Findings

1. (minor) The second sign of "Neheim" looks to me more like a barred "VI" (or II with a slanted first stroke) than the A-shaped IV ligature. Both readings give e, and the solver already notes this in Uncertainty 2. The plaintext is not affected.
2. (minor) The two s-signs (the ʔ-hook in "Reise" and in "Hüsten") are not identical in shape. The one in "Hüsten" is close to the flagged 1 that follows it. The split s / t rests partly on word sense. SOLUTION.md says this for s in the key section, but Uncertainty 4 should list s and t among the signs that rest on context.
3. (minor) The German rendering "Neheim-Hüsten" uses the hyphenated name, which only came into use with the 1941 merger. The solver explains this, but the plaintext line itself would be more accurate as "nach Neheim[-]Hüsten". The card writes the two names as two words. The report should keep that note.
4. (minor) Stamp box: the stamp is still on the card, so nothing beneath it can be checked. This is disclosed. The concern raised for the Jolánka series (steganography under the stamp) cannot be tested here. Nothing visible suggests it. The register type MASC is appropriate unless something is found under the stamp.

## What I could not verify

- What is under the stamp.
- The identity of "Eduard" and his relation to Frieda Necker.
- Whether a published solution exists. I did not search the web either.
