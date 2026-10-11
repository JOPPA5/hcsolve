# Slovak short-cipher scoring experiment

This work belongs to solver GPT-6.1 Sol; only HCP-332 and this batch directory were written. Original HCP-332 source is unchanged. Shared HCP-393 training corpus was read only. No published cipher solution was searched or used.

## Goal and independent data
The previous modern-corpus quadgram model fails its own 43-letter arbitrary substitution control: a garbled reading outranks true text. Downloaded primary LibreOffice Slovak dictionary/affixes (provenance and licenses in SOURCES.md and source/) to cover inflected vocabulary missing in the small UD corpus. Dictionary expansion approximates applicable affixes plus prefix/suffix crosses; it is not a complete Hunspell implementation. It ignores compound handling and continuation flags, and may overgenerate. Lowercase ASCII normalization merges diacritic distinctions. Model contains ~2.15M forms and 8,483 UD training sentences.

No control plaintext sentence is added to training. Model sees independent dictionary words, affix rules, UD characters and POS transitions. Individual control words naturally exist in the dictionary; this is lexical coverage, not sentence leakage. Hyperparameters and search design were developed using the first control, so the separately created second control tests generalization.

## Models and controls
- `mono.cpp`: dictionary/UD mixed 3/4/5gram score plus linear word-segmentation score. First run had an empty-word loader error and ignored all lexical data; `control43-result.txt` is invalid evidence. Corrected loader still fails exact control.
- `mono-longword.cpp`: stronger long-word reward. Ranks true first control above prior wrong readings but random optimization misses it.
- `mono-seeded.cpp`: fixes dictionary-pattern-derived word mappings during each local search. Anchors are generated from **all** matching rare-pattern windows, not supplied as cribs. Near recovery misses B/J.
- `mono-pos-seeded.cpp`: adds coarse POS transitions learned automatically from UD and POS masks from dictionary morphology. **Recovers first control exactly** with full expanded-dictionary seeds. `control43-pos-result.txt` and `control43-pos-check.json` provide the output. Unused ciphertext letters do not determine a unique complete26-letter key; success refers to exact observed-text decryption.
- A second independently encrypted length43 control, `vyslanectvoziadaodoslatnovuspravubezodkladu`, was created after the POS model was fixed. It **fails** under this model. Therefore no universal short-MASC recovery or family exclusion follows from the first success.
- `frequency/` favors actual UD running-text frequencies (1000× weight) over uniformly counted dictionary types (previous10×). `mono-frequency*` removes the superlinear long-word reward. Also tested stronger unknown-character penalties (`*-strict`). Neither version gives exact recovery of both controls. All outputs retained.

Dictionary-pattern seeds are **heuristics**, not exhaustive arbitrary-key search. Expanded dictionary seeds retain only windows with at most200 compatible words; some actual words are omitted by that cap. Core seeds use dictionary entry heads and observed UD tokens, improving natural-word coverage but still not exhaustive. Seeded optimizer: fixed RNG610332,2,000 swap proposals per starting key, keeping the candidate word mapping fixed. StatsJSON preserves seed counts/window choices. Some long-word/n-gram statistics reward plausible local fragments despite incorrect full messages; coherent full language and a deterministic key check remain necessary.

## Target
Bounded HCP-332 MASC search using the POS model and core dictionary seeds is saved in `ciphers/hcp-332/work/strong-*`. No supported full plaintext/key has emerged. No exclusion of MASC is claimed, because controls expose model/search limitations. Target language is assumed Slovak **only for this model**, following portal metadata; incorrect language metadata remains possible. This model does not test Czech, German or Hungarian competence.

## Reproduction
From repository root: `sh batches/scoring-sol61/reproduce.sh` rebuilds models from saved independent data, recreates the successful original control run, reruns the independent holdout, and applies the same fixed-seed algorithm to target variants. It can take several minutes. Other failed/random-search variants can be rerun from the same executable interfaces, with outputs in their corresponding named files. Scores are heuristic, not probabilities or calibrated confidence.
