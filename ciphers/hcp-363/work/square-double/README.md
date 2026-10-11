# Conditional square double-transposition experiment

400=20×20. Two ordinary full width20 columnar transpositions transform a square plaintext matrix into independent row and column permutations: first encryption transposes the matrix and permutes its rows, second transposes it again and permutes the other axis. Consequently each ciphertext20-letter chunk is an original plaintext row whose columns share one unknown permutation. This is a separate conditional structural case, not an R identification and not applicable to395-letter omissions.

Controls are two independently random keypairs, fixed seed36320020, encrypting the earlier explicit395-letter synthetic text continued by5 letters to400. No control is historical text or model training data. search.cpp first optimizes common column order against pairwise across-row bigrams and then frozen within-row3/4/5gram score,80 seeded starts and25,000 proposals per start. The first key is recovered EXACTLY for both controls. Then an exact Held–Karp20-node Hamiltonian path uses between-row ngram boundary costs to choose row order. That second key fails full recovery. This is a genuine partial control result, not successful full decipherment.

search-lex.cpp adds unchanged frozen dictionary/POS word-segmentation scores at row joins. It still fails the second key, although most known words/phrases survive. global-score-diagnostic.txt checks whole strings with the unchanged lexical function (only DP buffer extended from128 to512 for long text; no reward/transition changes). The wrong lexical row order has higher objective (-6053.05) than truth (-6086.09). Thus some failure comes from language/semantic ambiguity, not an inability to optimize that boundary table. No negative double-transposition exclusion is warranted. control-checks.json explicitly records exact first key, failed second key/full plaintext, and independently successful re-encryption of each candidate.

Because the first stage has matching successful partial controls, run-targets.py scouts literal400 X/A readings for genuinely readable20-letter row fragments. These scouts cannot supply negative family evidence while full controls fail. Saved candidates, hypothesized keys, row fragments and re-encryption checks do not assert historical plaintext. A positive claim would require coherent full semantics, supported row order and independently checked full re-encryption. No target cribs or published solution used.

Primary corpus/dictionary provenance is shared read-only with the segmented search and batches/scoring-sol61/SOURCES.md. All new code/data stay in363, source/ is unchanged. Frozen lexical scoring copied locally with unused optimizer omitted; full-text diagnostic increases buffer capacity only.

Reproduce controls:

```
python3 ciphers/hcp-363/work/square-double/controls.py
c++ -O3 -std=c++17 ciphers/hcp-363/work/square-double/search-lex.cpp -o ciphers/hcp-363/work/square-double/search-lex
ciphers/hcp-363/work/square-double/search-lex batches/scoring-sol61 ciphers/hcp-363/work/segmented/bigrams.tsv ciphers/hcp-363/work/square-double/control-0.txt
```

This reproduces a failed full control and exact first-key calibration. It is not a command decrypting the historical source.
