# Notes hcp-945

2026-11-03: captured by Claude Opus 5.5 (orchestrator).

## 2026-11-03 — Claude Opus 5.5 (solver)

- Looked at both sides of the card. The address side is plain (Frieda Necker, Malchow; Hagen 30.4.98). The cipher is four lines on the picture side, lower right: Arabic digits and Roman numerals with over- and under-bars.
- Checked the repo for similar systems. hcp-1114 (Hungarian) also uses digits and Roman numeral signs but has no key. hcp-946 (Erna Garbe) numbers the alphabet in Roman numerals, which does not fit here. So I built the key from this card alone.
- I tried a pure-vowel hypothesis (the Roman numerals stand for the vowels a e i o u) and a hypothesis of A1Z26 values. Neither fits: d is written V, and h = 8 matches A1Z26 only by chance.
- The breakthrough: the dot on the baseline recurs inside the words, so I read it as i. Then "S . II 6 II" gives "liebe", and line 1 reads "Meine liebe Frieda", which matches the addressee. Line 4, "V IV . 2 / II V IIII X 4 V", gives "Dein Eduard", which fixes V = d, IIII = u, X = a and 4 = r. Line 2 then reads "Reise heute nach".
- In line 3, the two hook strokes after the umlauted u are different signs. The first is the 7-like hook that means s in "Reise", and the second is the flagged 1 that means t in "heute". With the brown-ink 2 (n) at the end, the line reads "Neheim Hüsten", two neighbouring Sauerland towns about 50 km east of Hagen.
- Wrote work/transcription.txt, work/key.json and work/decode.py. The decoder checks the source hashes and asserts the plaintext. Wrote SOLUTION.md. The reading is complete; the residual points are listed there.

## 2026-11-03 — Claude Opus 5.5 (solver, after review 1)

- Review 1: ACCEPT, four minor findings. Answered in SOLUTION.md "Response to review 1". Uncertainty 4 now names s/t as resting on context; reading line, translations and decode.py summary now give "Neheim Hüsten" as two names (no 1941 hyphen). Re-ran decode.py: hashes OK, assertion passes.
- Re-checked stamp box and edges (Jolánka-series steganography concern): stamp still affixed, no writing visible around it, on edges or in the vignettes. Type stays MASC.
- Added work/cipher-block.jpg (crop of hi-res original), wrote report/report.md, rendered report/report.pdf, wrote register-entry.txt.
