# HCP 1451: second-line stroke comparison, 2026-10-26

Fresh manual inspection of both original JPEGs and the existing enlarged address inscription. No published text consulted, no OCR used. The printed picture side has no handwritten continuation.

`initial-comparison.png` contains unretouched crops of `message-large.jpg`, in order: line 1 initial, line 1 medial descending letter, line 2 initial, line 3 initial, line 3 medial descending letter. The crops compare shapes, not independently identified letters.

- The line-1 initial has a large oval upper/right loop and an open curved left entry. Its lower stroke is a short hooked return. This supports the existing capital G interpretation.
- The line-2 initial has a narrow upper loop, a small triangular enclosed shoulder at the baseline and a long broad lower loop. It is not a direct graphical match to the line-1 capital G.
- Its construction is closer to the line-3 initial, interpreted as cursive z in the ALWAYS hypothesis. This adds ZRNV / ZLNV as explicit alternatives, decoding AIME / AOME. It does not prove identity: initial capitals and lowercase forms can differ, and the cipher letter identities remain manual hypotheses.
- The line-1 medial f has a compact baseline loop and a long narrow descender. The disputed initial has a much wider descender plus a separate upper loop; F is possible only as a different case/allograph, not a repeated exact shape.
- The second small letter on line 2 has a low angular shoulder rather than a tall ascender. R is somewhat more visually plausible than a normal cursive lowercase l; lack of securely identified repeated exemplars prevents freezing it.
- The last two letters on line 2 appear n/v, but they also lack enough independent exemplars for a complete transcription claim.

English fluency cannot settle these observations. TIME, TOME, UIME, AIME and AOME are alternative outputs of unverified readings, not competing complete decipherments. No new complete word is established. The previous 16-letter manual Atbash hypothesis outside this line is unchanged, including literal LOVENG.

## Reproduction

`python3 ciphers/hcp-1451/work/decode-atbash.py` checks the saved source hashes and reproduces every listed alternative. These hashes establish unchanged inputs; the manual transcription is not validated by the decoder or its round trips.
