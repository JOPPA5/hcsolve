# HC Portal 357 work log

## Source and transcription — 2026-10-11

Solver: OpenAI GPT-6 Astra. The parent captured the portal's General, Description and Attachments tabs. Status: Not solved. No transcription or solution attachment was shown. I inspected the saved 1024-pixel-wide **large conversion**, not an original-resolution upload, and an enlarged crop. Its 17 five-letter groups form an intact-looking 6+6+5 layout; no lacuna is marked.

```
amaon yoato qcbzu mtrds ddnmn tooip
yzlro vpatv pnyly hndei raaza oznrc
cyiao ysoce rescm nnaaa vzvvk
```

The reviewer independently agrees with all 85 letters, while retaining possible n/m ambiguity in group 5 `ddnmn` and group 10 `hndei`. Both are now flagged. No hypothesis-driven correction has been made.

Additional clear text, two stamps `15. III. 1944`, and handwritten receipt time `17.45` are recorded in `work/scan-observations-review1.md`; immutable source metadata was not edited. Source-image SHA-256: `d3aad5eefa45c42e6921abdd61035eab01a02f28f986405c30f80667d0b3e5f3`.

## Header and indicator hypotheses

The header `685` is not wholly unexplained: the suffix **85 matches the letter count**. The same suffix pattern appears in the batch's 3100/100 letters, 755/55 letters and 5245/245 letters. The leading digit's meaning is unresolved; it is not uniformly the dispatch day.

Review 1 proposes prefix 6 as an indicator position, hence removal of group 6 `tooip`. This is a testable hypothesis. The repeated O at positions 2 and 3 can fit n=10 or n=20 in the documented R/XQ digit encoding. It does not establish the hypothesis.

**There is concrete counterevidence to treating the leading digit as the indicator position in general.** Figure 5 in the cited HistoCrypt paper (PDF page 8 / printed page 28) shows a worked example with alignment n=7 and indicator position ip=5, stated in its accompanying text, 55 payload letters and 60 transmitted letters. The handwritten numeric header is **360**. Its prefix 3 differs from both n and ip. The three grid widths are 21, 19 and 20, also not 3. This need not exclude a later/other convention in our telegram, so the requested group-6 control was still performed. Evidence and rendered page are retained under `batches/analysis-395-396/`.

Group 3 `qcbzu` was previously nominated because it contains all Q/B/U occurrences. That argument is weak: the paper explicitly allows Q as a plaintext separator for proper names, abbreviations and times; Q is not intrinsically an indicator tell. Unique B/U in 80 letters are only a weak distributional observation. Neither group 3 nor group 6 is established as an indicator.

## Statistics

Full 85-letter IC: 0.05742297. Removing group 3 leaves 80 letters, IC 0.06234177. The review-1 baseline also records group-6-removal statistics in `work/baseline.json`. Nonuniform frequencies are compatible with transposition but cannot establish R/XQ.

## Attempts and what their results mean

Run `sh ciphers/hcp-357/work/reproduce.sh` from the repository root to regenerate the diagnostics. It does not output a solved plaintext.

1. `baseline.py`: 2,818 simple row/column route variations across every one-group omission and no omission; 104 signed-Caesar/reversal controls. No coherent result among the stored best-scoring outputs.
2. `attack.cpp`: single-columnar simulated annealing, widths 2–30, 30 restarts × 20,000 proposed mutations per setting. Initially run for group 3 omitted (forward and reversed) and full 85 letters: 52.2 million proposed mutations. Review 1 adds group 6 omitted, forward and reversed: another 34.8 million. These are stochastic searches, not exhaustive distinct-key counts. Corpus scoring is heuristic.
3. `multistage.cpp`: initial two- and three-stage trials at equal widths 16–22, for 80-letter group-3-omitted and full 85-letter inputs. **These runs have no evidential weight for rejecting or supporting multiple transposition.** Reviewer planted controls with keys inside this searched space: the solver recovered 0/3 two-stage and 0/3 three-stage messages. The optimizer cannot find answers known to be present. Candidate scores around 176 therefore reflect false local optima, not progress toward a decipherment.

The reviewer recovered 3/3 planted width-11 single-columnar controls. That validates some attack ability in that control setting. Its negative results on this ciphertext are limited evidence against simple columnar hypotheses, not a proof excluding every width 2–30: the control did not establish success rates for all widths/transcriptions/indicator removals.

The historical paper gives R password lengths 16–22 but **no reason to assume the three widths are equal**. Its worked example actually uses 21,19,20. The prior equal-width search was therefore a convenience restriction unsupported by the source, in addition to its demonstrated lack of attack power. The method's stated message range is 50–250; neither our 80- nor 85-letter interpretation violates that range.

## Review 1 and current result

Review: Claude Opus 5.5, REVISE. Reproduction and checksums were independently confirmed. The requested group-6 single-columnar tests are saved as `results-group6.txt` and `results-group6-reverse.txt`; see the review-response section of SOLUTION.md for their result.

No supported cipher type, key or complete plaintext has been recovered. The title about handing over decorations remains metadata, not a forced crib. A negative result from the failed multi-stage optimizer says nothing about whether the cipher is R/XQ or solvable. Actual key sheets or a validated stronger cryptanalytic method would be required to make further progress.

The external reviewer polls markers; no watcher is launched. The accidental DONE1 was not a solved claim. After these revisions the main solver prepared the authorized two-page report of an **unresolved attempt**, rendered and visually inspected both pages, checked the unchanged image hash, and verified that no register entry exists. The FINAL marker closes this failed attempt, not a decipherment.
