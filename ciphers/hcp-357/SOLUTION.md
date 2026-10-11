# HC Portal 357 — unresolved attempt

**No plaintext or key has been recovered.** Solver: OpenAI GPT-6 Astra. Review 1: Claude Opus 5.5, REVISE; the reviewer agrees that the outcome must remain unresolved.

The source is MZV message 80132/1944, dated 15 March 1944, from Belnay to the Slovak legation in Sofia. The portal says Not solved. Its title concerns instructions for handing over decorations; that title is not a deciphered text. The preserved image is the portal's 1024-pixel-wide `-large` conversion, not a verified original-resolution upload.

I manually transcribed the image (no attached transcription):

```
amaon yoato qcbzu mtrds ddnmn tooip
yzlro vpatv pnyly hndei raaza oznrc
cyiao ysoce rescm nnaaa vzvvk
```

The independent reviewer agrees with all 85 letters. Possible n/m ambiguities remain in group 5 `ddnmn` and group 10 `hndei`. The scan contains no visibly marked missing ciphertext. Additional scan context, date stamps and handwritten receipt time 17.45 are recorded in `work/scan-observations-review1.md`.

The header `685` separates consistently as leading 6 plus body length 85. The leading digit's meaning remains unknown. Both the suggested group-3 indicator and the reviewer's group-6 indicator-position hypothesis were tested. Neither is established. R/XQ triple columnar transposition is only a historically motivated cipher-family hypothesis; there is no supported cipher type, key, original-language plaintext or translation.

Reproduce the diagnostic attacks from the repository root:

```
sh ciphers/hcp-357/work/reproduce.sh
```

This uses the manual transcription and produces search diagnostics. **It cannot produce full plaintext from the source**, because no successful decipherment exists. Single-columnar searches yielded incoherent candidates. The multi-stage optimizer failed to recover known planted controls, so its negative target results have **no evidential weight** concerning multiple transposition or solvability. No published solution was used; no register entry is appropriate.

## Response to review 1

1. **Multi-stage search — accepted and corrected.** NOTES.md and this document now state plainly that the equal-width two-/three-stage runs provide no evidence either way. The independent reviewer recovered 0/3 planted two-stage and 0/3 planted three-stage controls, whereas 3/3 single-columnar width-11 controls succeeded (`review/work/control.py`, findings in `review/REVIEW1.md`). Mutation volume and isolated word fragments do not constitute attack power. The single-columnar evidence is described with its actual control scope rather than as exhaustive exclusion of all tested widths.

2. **Header pattern and group 6 — suffix finding accepted; prefix hypothesis tested but not established.** The trailing 85 matches the letter count and the analogous batch headers. Group 6 `tooip` was removed and the single-columnar attack rerun at widths 2–30, in forward and reversed directions, with 30 restarts × 20,000 mutations per width. Both 29-result files are complete: `work/results-group6.txt` and `work/results-group6-reverse.txt`. No coherent plaintext was recovered. Best forward score: 136.605 at width 29; best reversed score: 125.829 at width 30. The 80-letter group's IC is 0.05791139. These are heuristic negative results, not a proof about R/XQ.

   New source evidence limits the proposed general prefix rule: the cited paper's **Figure 5** (PDF page 8 / printed page 28) shows an R/XQ example with **n=7, ip=5 and transmitted length 60**, yet a handwritten header **360**. The three widths are 21,19,20. Thus prefix 3 is neither n, ip nor first-stage width in that example. The rendered page is preserved in `batches/analysis-395-396/paper-page8.png`. This does not rule out a different convention in the present telegram; that is why the requested group-6 test was still run. Similarly, indicator consistency cannot by itself select O over C in cryptogram 396: it would be conditional on this unproved prefix rule.

3. **Q/B/U argument — accepted and weakened.** Q can be a plaintext separator under the documented preparation rules. Its presence is therefore not indicator evidence. The group-3 B/U concentration remains only a weak statistical observation. Neither group 3 nor group 6 is promoted into a recovered indicator.

4. **Unequal widths and range — accepted and clarified.** The paper does not justify equal stage lengths; Figure 5 actually uses 21,19,20. The earlier equal-width 16–22 search is an unsupported convenience restriction, independently of its failed controls. The paper's 50–250 message range is recorded; both 80- and 85-letter target interpretations fall within it.

5. **Source record — accepted and corrected.** SOURCES.md now explicitly identifies the saved file as the displayed `-large` conversion. No original-resolution upload or original-download link was captured, and no guessed URL was fetched. The existing source metadata remains immutable. Additional scan observations, including both `15. III. 1944` stamps and time `17.45`, are in `work/scan-observations-review1.md`. Both n/m ambiguity locations are recorded. The formatting-corrupted hash in NOTES.md was replaced with the verified unspaced SHA-256 `d3aad5eefa45c42e6921abdd61035eab01a02f28f986405c30f80667d0b3e5f3`.

The outcome remains **unresolved**. The two-page report at `report/report.pdf` records this failed attempt and the review corrections; its source and builder are stored alongside it. Both rendered pages were visually inspected. FINAL closes this reviewed attempt, not a successful decipherment. No register entry exists.
