# Short MASC scout: HCP 396 and 345

No solution or coherent full target plaintext recovered. Source ciphers were read-only; scans were independently viewed again. Literal 396 has all 55 letters with both initial C/O readings of group 7. Literal 345 has all 65 letters. Forward and complete reverse order are tested. No group omission, erasure, inserted letter, forced title crib, watcher, reviewer or marker.

## Independent controls

`controls.json` preserves twelve fresh independently encrypted controls: genuine whole UD TEST sentences of exactly 55/65 letters in Slovak, German and Czech, at alphabets 26 and 28. Exact normalized sentences are absent from TRAIN, have no digits or PROPN tokens. No TEST sentence, true key or true word is provided to seed generation or search. Dictionary/anchor vocabulary and lexical/POS tables use frozen dictionaries/TRAIN only. Fixed encryption seeds, original sentences/IDs, raw/folded texts and complete keys are recorded.

Models are the frozen 3/4/5-grams in `batches/scoring-sol61/`, its `german/` subdirectory and `batches/czech-scoring/`. Scoring weights .15/.4/.8. Czech lexical/POS tables are newly derived strictly from Czech TRAIN; existing multigrams are symlinked read-only. `provenance.json` and `source-model-hashes.json` identify inputs and credit.

Both 26-letter German controls recover complete texts (65-letter truth initially rank 1, then lexical rank 0). Both 26-letter Czech controls recover complete texts after the revised generic anchor selection (65-letter truth multigram rank 0, lexical rank 7). Retaining multiple candidates matters: ranking the first candidate alone would lose a genuine positive control.

Slovak controls fail. The 55-letter genuine historical-sounding sentence contains the unfamiliar title "spahbed"; truth scores approximately -915.65 in grams, -947.30 combined, while false combined candidates score about -843.26. This is concrete short-text score overfit. The 65-letter Slovak truth scores -1012.03 combined, better than the best revised false candidate -1049.83, showing a search failure as well. There is no calibrated Slovak negative/exclusion claim.

Some 28-symbol folded controls are retained or appear one swap from a survivor; these are explicitly distinguished from exact RAW control recovery in control check JSONs. Raw Czech 28/65 truth is retained in the original lexical pass; raw German 28/65 truth is retained. 28/55 calibration remains incomplete, particularly for raw spelling. Neither language has complete strong raw-28 calibration at both lengths.

## Alphabet and key conventions

26 symbols: a..z. 28 symbols: a..z plus `{` and `|`, representing additional Č/Š plaintext symbols. Keys are full bijections over the raw alphabet. All multigram/lexical scoring folds `{` to c and `|` to s, so it cannot uniquely determine those diacritics. Every raw candidate is preserved and independently re-encrypted. The German 28-symbol test is an abstract expanded-alphabet scout using the same extra C/S symbols, NOT evidence of an authentic German alphabet or cipher convention. Unused key entries are arbitrary bijective completions; exact message recovery does not identify unused mappings.

## Search and diagnosed changes

Source credit: generic word-pattern anchors and compatible pair seeding adapt `batches/scoring-sol61/german/anchors-short.py`, `pairs.cpp` and `run-pairs.py`. Strict seed masks and frozen permutation/multigram/lexical conventions adapt `batches/scoring-sol61/mono-frequency-seeded-strict.cpp`; lexical implementation is copied from `ciphers/hcp-363/work/square-double/frozen-lex.hpp` without retraining it.

Initial anchors-v1: windows 6–25, dictionaries/TRAIN core, skip pattern classes over 200 matches, up to 1,000 longest/frequent anchors, 2,000 ranked compatible partial keys plus 128 fresh random seeds. Strict seeded search makes 1,000 proposals per seed; up to 64 distinct full-text candidates are then refined blindly with all substitution mappings unlocked for 10,000 proposals each. The controls are never read by this code. Both stages retain up to 64 full raw texts/keys.

Lexical pass generically constructs all single key swaps around every retained candidate, scores grams + 2*lexical/POS, then takes eight best starts through at most eight rounds of exhaustive improving key swaps. This is not a supplied known-word correction. It is justified by controls where the truth is not top-ranked or is exactly one key swap away. Lexical ranking can also demote truth (Czech 65), so both score channels remain preserved.

Failure diagnosis and version 2: common pair ranking could suppress single anchors; separate single-anchor preservation alone did NOT fix failed Slovak/Czech 65 controls. Outputs and versions are preserved, not overwritten. My initial preliminary pruning interpretation was incomplete.

Version 3 corrects the larger problem: instead of dropping all common-pattern windows, each window retains its top eight TRAIN-frequency dictionary words. Separate length-priority and TRAIN-frequency pools each reserve up to 1,000 anchors. Pairing uses 500 generic anchors; pairs have a separate cap of 1,000, alongside single anchors and 128 fresh random starts. This change exactly recovers Czech 26/65 with no ground-truth seed or word injection. It improves some Slovak partial scores, but does not solve the Slovak controls.

No identical restart expansion was used to disguise calibration failures. Existing logs and sources remain intact.

## Target attempts and findings

Version 1 ran all 36 combinations: three complete readings (345, 396-C, 396-O), forward/reverse, three languages, two alphabet sizes. Each has multigram and lexical/neighbor outputs. The substantively revised version 3 additionally tested 24 Slovak/Czech target combinations. Total 60 target searches / 120 saved stage outputs / 7,680 retained full raw candidate-key pairs. `validate-targets.py` independently checks all full decodings and inverse substitution re-encryptions. In reverse scenarios, this covers the entire reversed literal input; reversing the resulting ciphertext returns the exact original literal ordering.

Whole diverse candidates were inspected; representative complete readings are retained in `whole-text-inspection.json`, with all 64 candidates per stage in `target-summary.json` and individual logs. None reads as a supported whole Slovak, Czech or German message. Familiar fragments are not claimed as recovered words. Mathematical full re-encryption is only transformation correctness and is not proof of linguistic/historical correctness.

These target attempts remain exploratory wherever controls fail, especially Slovak and raw 28. Even matching German/Czech 26 controls only support those examples, not universal short-message reliability. No exclusion of MASC, other language, indicator-bearing variants, transposition or R is claimed. R remains a hypothesis; this is a genuinely different short-substitution scout.

## Reproduction

From repository root (commands overwrite only this batch's generated artifacts; saved version-specific logs are separate):

```sh
python3 batches/short-masc/prepare.py
python3 batches/short-masc/build-cs-lex.py
clang++ -O3 -std=c++17 batches/short-masc/mono.cpp -o batches/short-masc/mono
clang++ -O3 -std=c++17 batches/short-masc/lex-refine.cpp -o batches/short-masc/lex-refine
python3 batches/short-masc/run-controls.py
python3 batches/short-masc/run-lex-controls.py
python3 batches/short-masc/run-controls-v2.py
python3 batches/short-masc/run-controls-v3.py
python3 batches/short-masc/run-lex-controls-v3.py
python3 batches/short-masc/run-targets.py
python3 batches/short-masc/run-lex-targets.py
python3 batches/short-masc/run-targets-v3.py
python3 batches/short-masc/run-lex-targets-v3.py
python3 batches/short-masc/check-controls.py
python3 batches/short-masc/check-controls.py lex
python3 batches/short-masc/check-controls.py v2
python3 batches/short-masc/check-controls.py v3
python3 batches/short-masc/check-controls.py v3 lex
python3 batches/short-masc/validate-targets.py
```

All randomness is fixed in scripts. Truth-score invocations happen separately AFTER blind control searches; truth files are never used by seed or optimization calls. No published target solution was consulted.
