# HCP364: extension of the explicit single-long model

The first two stages have widths 16/16; the third ranges from 18 through 22. This extends the preserved positive 16/16/17 calibration without changing its evidence. Each column is written down the physical grid and columns are read in key order. All three physical column-zero ranks share an unknown n−1, with n in 1..16. This is a conditional common-alignment family, not a reading of header 1170.

The exact Boolean model explicitly packs the sole long column in each first stage (65=4×16+1), uses exact prefix paths in the third stage, and enforces both forward and reverse endpoint supports. A separate exhaustive audit covers 24 positive/negative toy cases with third widths 5 and 6, compared with all 288/1440 legal key triples respectively. Every result agrees.

Fresh full65 controls use the conditional quote with four sentence markers plus a final padding X, independently random keys, unknown n, and a ciphertext union containing the genuine cipher and a U/V-swapped alternative. The solver receives neither keys nor n. Each control has a 30-second search cap. Positive controls independently reproduce every planted key, n, variant, and the entire 65-character plaintext through encryption and inverse. No uniqueness claim is made.

| Widths | Blind control | Seconds | Corrected target | Seconds |
|---|---|---:|---|---:|
|16/16/18|SAT, all planted keys exact|22.62|All 16 n UNSAT|19.45|
|16/16/19|SAT, all planted keys exact|24.33|All 16 n UNSAT|29.66|
|16/16/20|UNKNOWN|30.01|Not run: failed calibration gate|—|
|16/16/21|SAT, all planted keys exact|1.98|All 16 n UNSAT|2.61|
|16/16/22|SAT, all planted keys exact|14.22|All 16 n UNSAT|8.30|

Target input is the existing corrected-source EXCUV/EXCVU union, omitting ITPKA, and the fixed-end-X quote. The quotation remains a hypothesis. Its 64-character template has the lexical X in TEXTOM plus four sentence X markers; final padding yields 65 characters with six literal Xs. The target checks use one compiled solver and ascending rank assumptions, capped at 15 seconds per rank; every attempted rank completed UNSAT, with no UNKNOWN. No target key or plaintext witness was found.

These exact results apply only to the stated stage order, common alignment, two source variants, omitted group, and fixed-end preparation. They do not rule out width20, other width orders, progressive alignment, free filler placement, other source readings, or the quoted reply itself. The width20 failed control supplies no exclusion.

Reproduction: `python3 batches/r364-two16-one17-sol61/extension/run.py` (repeats bounded searches); audit: `python3 batches/r364-two16-one17-sol61/extension/audit.py`; independent saved-witness checks: `python3 batches/r364-two16-one17-sol61/extension/verify.py`. Full keys, truth provenance/seeds, individual rank results, model metrics, hashes and independent verification are retained in adjacent JSON files. Original source hashes are unchanged; no cipher documents or markers were changed.
