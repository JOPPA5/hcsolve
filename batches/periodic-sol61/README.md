# Periodic polyalphabetic scout

This batch owns no cipher files or markers. Inputs are literal read-only transcriptions of HCP369,345,396,393,367,374. The numeric 3100 prefix of 393 is explicitly recorded separately. All other letters are retained. HCP367 unknowns remain periods, preserve their original positions and advance the key phase. HCP396 has distinct C/O readings at the first glyph of group 7. No unknown letter is guessed.

For every reading, both directions and the whole body plus every single five-letter group omission are searched. Group omissions are conditional generic indicator hypotheses, not confirmed indicators. Models are independently frozen Slovak, German and Czech. No family or language is excluded by lack of a coherent result.

Periods 1–3 are exhaustive: 26^T keys for Vigenere/Beaufort/variant, 13^T for Porta. Periods 4–16 use 24 starts and 2500 proposals per start for controls and whole targets. Omission scouts use 4 starts and 1000 proposals and are weaker exploratory searches. Four distinct full plaintexts are retained per family and period. Score weights are 0.15/0.4/0.8 for 3/4/5-grams. Windows crossing an erasure are omitted from scoring, while all positions retain key phase. Unknown key period is searched throughout 1–16 for every control.

All 48 independently keyed controls passed exact full plaintext recovery. They cover all four families, three languages, and lengths/periods 55/3,85/9,100/15,115/12. The 85-letter controls contain two erasures. True periods recovered each control at rank zero of that period. These positive controls establish performance on these specific samples, not exhaustive recovery for arbitrary short messages or all 16 periods. Repeated short-period keys can also be represented at period multiples; key length is not uniquely identified merely by plaintext recovery.

Reproduce from the repository root:

```sh
python3 batches/periodic-sol61/prepare.py
clang++ -O3 -std=c++17 batches/periodic-sol61/periodic.cpp -o batches/periodic-sol61/periodic
clang++ -O3 -std=c++17 batches/periodic-sol61/verify.cpp -o batches/periodic-sol61/verify
batches/periodic-sol61/verify batches/scoring-sol61 batches/periodic-sol61/sk-frequencies.tsv
```

Run periodic with arguments MODEL_DIRECTORY FREQUENCIES_TSV CASES_TSV; stdout is the retained candidate TSV, stderr is per-case progress. Use controls-sk.tsv, controls-de.tsv, controls-cs.tsv with their language model directories from provenance.json; use targets.tsv for each language. `python3 batches/periodic-sol61/check.py` independently reencrypts every complete candidate row using a separate Python table encoder and writes checks.json. The checker ignores an incomplete final output line if a process is still running. The `verify` binary checks the primary Porta example and 12,800 incremental score mutations against complete independent rescoring.

Every output row records label, family, period, rank within that period, score, comma-separated zero-based key residues and full plaintext. For Porta residues are pair classes 0–12, represented by keyword letters AB/CD/.../YZ. A readable entire message and independent reencryption are required for a solution. High scores, isolated words, and successful reencryption alone do not prove plaintext correctness.

The exact parallel invocation is `python3 batches/periodic-sol61/run.py controls`, then `python3 batches/periodic-sol61/run.py targets`. Each process has the fixed RNG seed 619369. Repeating a run overwrites that run's result files; archive outputs first if comparing changed parameters.

Final status: all 714 target/model runs completed; 185,856 retained control and target candidates independently reencrypted. No coherent full target solution. See SOLUTION.md and summary.json.
