# Public 373 known-prefix: invisible word-space advances

This is a bounded key-model experiment using the already published 373 plaintext as public context for unresolved 374. It is neither a new solution of 373 nor a recovered key for 374. The immutable source collation remains in `batches/kryha373-collation-sol61`; this batch writes only derived variants and results. No source words are added or deleted. No emitted Q, guessed words, or emitted space marker is introduced.

## Model and exact bounds

Two arbitrary 26-position alphabet permutations P/O and a period-m displacement sequence K obey `O[c_i] - P[p_i] = K[t_i mod m] + 179 floor(t_i/m) (mod 26)`, with A gauges fixed at zero. This is a necessary relaxed displacement model; passing it would not establish a physical wheel mask. Integer press indices t insert either one or two un-emitted advances between lexical words. `lexical` inserts at each word boundary, including a comma without whitespace; `whitespace` inserts only where the literal intervening source substring contains whitespace. These schedules are hypotheses, not historical facts.

The source prefix ends before literal `6.000`. The 128 variants are the Cartesian product of source USTRENI versus editorial USTREDNI (92/93 letters), natural J versus I, one/two advances, lexical/whitespace policy, ciphertext prefix omission zero/five, absolute ciphertext glyph 53 L/I, and glyph 90 E/A. Every variant tests all 51 periods 2..52: 6,528 cases. Glyph variants are applied before the five-letter omission. `schedule.py` retains the raw prefix, source words, literal gaps, and emitted-character press indices. `actual-results.jsonl` records each exact normalized plaintext, ciphertext, press indices, and branch identifier.

## Positive and algebra controls

The independent finite-helper audit and its proof are in `FINITE-AUDIT.md` and `finite-independent-audit.json`: 20 affine synthetic cases agree with a separate direct mod-26 enumeration of all 676 parameter pairs, including ten impossible partial-injection cases. Projection to free coordinates affecting observed slots is exact. Unobserved letter slots can be completed bijectively without changing any fitted equation.

Eight fresh 92/93-letter positive controls use independent physical-mask encoders and the same schedules. All 51 blind period scans uniquely accept their planted periods 20/23/30, with no remaining UNKNOWN. Complete known-prefix inverse/re-encryption is checked independently. The held-out 20-letter results are 20,18,20,20,20,19,20,20; this does not establish unique alphabet recovery. Original controls, timeout outputs, and truth files are preserved. Their retained summaries are in `controls-summary.json`.

## Result

All 6,528 cases completed: **6,520 UNSAT, 8 UNKNOWN, zero SAT**. The eight UNKNOWN cases are exclusively USTRENI, natural J, one extra advance at literal whitespace, period 52, across both omissions and all four glyph pairs. Each retained its 2,000 ms timeout; they are not exclusions. Exact counts are recorded in `actual-summary.json`; individual case evidence is append-only `actual-results.jsonl`. Larger active parameter products retain a 2,000 ms SMT timeout and are reported UNKNOWN if unresolved; the finite helper never silently truncates enumeration at its 50,000-combination dispatch threshold.

Run from the repository root: `python3 batches/kryha373-unemitted-spaces-sol61/actual.py`. The runner resumes only missing branch/period identifiers and preserves earlier results. There is no independent 373 plaintext claim, physical key, register entry, or completion marker from this batch.
