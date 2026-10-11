# Remaining paired discrepancies: independent main scan check

Main solver viewed both original 350 pages and the original 351 scan again after the common-cycle analysis. This is an independent visual reread, but not a blind transcription experiment: the discrepancy positions were already known. No expected cycle-predicted replacement letters were used to alter the readings.

The four residual interior disagreements involve these source groups and letters:

| 350 position | Literal source reading | 351 position | Literal source reading |
|---|---|---|---|
| 122 | LGHFN, G | 123 | ZSBBR, B |
| 230 | PCKGG, G | 231 | LVBMF, L |
| 239 | NKMXK, X | 240 | IIHUU, U |
| 315 | JEUNO, O | 316 | ZOACA, Z |

All eight printed glyphs support the retained working readings. A failed cycle correspondence at these cells therefore cannot simply be repaired as a transcription error. A transmission/operator error, genuinely different underlying plaintext, or a different model remains possible. Language recovery must retain both observations and disclose any disagreement instead of forcing either source to match a prediction.

Exact positions and original image SHA-256 hashes: `readings.json`. Original source files remain unchanged.

## Independent candidate-mechanics verification

`python3 batches/kryha-source-residuals-main/verify_candidates.py` independently walks adjacent physical holes for every character, without importing the solver's codec or cumulative-coordinate projection. All 400 complete candidate keys reproduce both 355-letter working bodies exactly. Source coverage is checked directly against the separately retained 385-letter variants; 30 framing letters per telegram remain outside this branch.

Every candidate in the strong variant retains six paired plaintext differences at zero-based 350 positions 80, 84, 121, 229, 238 and 314. Every strong-plus-moderate candidate retains four, at 121, 229, 238 and 314. Thus candidates have not silently repaired the source to obtain exact repeated plaintext. This confirms mechanics and retained discrepancies, not a linguistically correct historical plaintext. Key-file hashes and detailed checks are in `candidate-verification.json`.
