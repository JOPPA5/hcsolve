# Conditional 10 × 10 double-columnar experiment (GPT-6.1 Sol)

The full literal working transcription has exactly 100 letters. Its leading `3100` is excluded as before; its role is unknown. Original source files were not modified. No candidate here is a claimed decipherment.

Two ordinary columnar transpositions with width ten on a complete 10 × 10 square reduce to independent row and column permutations. The first transpose emits plaintext columns in key order; the second emits original plaintext rows with the same first column ordering. This is a conditional model, not an identification of the historical cipher.

Unlike the width-20 experiment, this search **enumerates all 3,628,800 column orders**. Cross-row sums of frozen character 3/4/5-gram scores are precomputed for column tuples. It retains the best 64 column orders by *within-row* score, then **enumerates all 3,628,800 row orders for each** using exact additive character boundary scores. This is not exhaustive over all (10!)² pairs: a true column order outside the retained 64 is omitted. The best 2,000 full character candidates are reranked with the frozen lexical/POS score. `search-wide.cpp` retains 50,000 instead. All scorer inputs are independent of the planted plaintexts; no control phrase was injected into training.

`search-phrase.cpp` additionally scores cross-row 6–9-grams observed only in the existing UD Slovak SNK TRAIN corpus. It is a separate bounded test; adding longer phrase fragments did not solve the genuinely held-out control.

## Independent controls and limits

`controls.py` independently plants two key pairs for each of two 100-letter texts. The diplomatic authored text is a 100-letter fragment of a naturally authored message, related in style to the earlier route control. The real sentence is selected from **UD TEST**, not TRAIN:

> Genealógia alebo rodopis je pomocná historická veda skúmajúca vývoj rodov a vzťah medzi rodovo príbuznými jedincami.

NFD lowercase ASCII-letter normalization gives exactly 100 letters. The normalized complete sentence is absent from the TRAIN sentence set. TEST was newly downloaded for this experiment; frozen base models predate that download and use TRAIN and a public dictionary. Common individual words can of course occur in TRAIN/dictionary.

Both key pairs of the authored control recover exact plaintext and both keys at rank 0, under both base and longer-phrase searches. Both key pairs of the genuine held-out control recover the exact column order, **but fail to select the true row order**. All saved top-100 candidates mechanically reencrypt exactly, proving only their permutation consistency.

With correct columns, exhaustive base row scoring places 22,462 permutations strictly above truth (four ties within 0.001). The 50,000-candidate lexical reranking includes truth at rank **1,440** (zero based). The true full-text character/lexical/combined scores are -1580.48 / 27.4746 / -1525.53; an incoherent alternative scores -1544.75 / 32.2451 / -1480.26. This is concrete score bias and rank ambiguity, not evidence against transposition. No restart increase can fix the unchanged objective.

## Actual scout

Base, longer-phrase and wider-frontier searches use the entire unchanged 100-letter literal transcription at width ten. Their saved candidates are incoherent, despite exact mechanical reencryption. Given the held-out control failure, these are weak negative scouts and **do not exclude double columnar transposition**, other widths/fill conventions, triple transposition, different language, or corrected uncertain glyphs. The numeric prefix and damaged glyphs remain unresolved. No `DONE`, `FINAL`, report or register entry is created.

## Reproduction

From the repository root:

```sh
ciphers/hcp-393/work/square10/reproduce.sh
```

This compiles and runs the base and phrase controls plus actual scouts into `reproduced/`, preserving the original result logs. Read-only dependencies: `batches/scoring-sol61/model{3,4,5}.tsv`, lexical/POS files in that directory and `ciphers/hcp-363/work/segmented/bigrams.tsv` (loaded but unused by this exhaustive optimizer). `build-phrases.py` trains only existing UD TRAIN. `validate.py` checks all saved top-100 control/target candidates by independent inverse permutation and records exact recovery, false positives and source/corpus SHA256s. `rank.cpp` reproduces the exhaustive true-column row rank from `diagnostic-input.txt`; `diagnostic.cpp` reproduces the full-text scores.

For the wider held-out ranking:

```sh
clang++ -O3 -std=c++17 ciphers/hcp-393/work/square10/search-wide.cpp -o /tmp/hcp393-wide
/tmp/hcp393-wide batches/scoring-sol61 ciphers/hcp-363/work/segmented/bigrams.tsv ciphers/hcp-393/work/square10/heldout-0.txt ciphers/hcp-393/work/square10 ciphers/hcp-393/work/square10/diagnostic-input.txt
```

The final argument supplies expected text for **diagnostic rank reporting only**, after search and ranking; it never changes candidate scores or pruning. Seeds, all planting keys and normalization are saved in `controls.json`. Numerical rank ties use an explicit 0.001 tolerance only in `rank.cpp`; exact text/key validation uses equality.

## Odd number of equal-width passes: transposed scout

For three ordinary width-ten columnar passes, the complete square reduces to independently permuted rows and columns **plus overall matrix transpose**. `triple-control.py` encrypts the authored 100-letter control with three independently planted ordinary columnar keys (seed 393310), transposes the ciphertext, and supplies that transformed input to the same wider exhaustive search. It recovers exact full plaintext and both reduced permutation keys at rank 0; applying all three saved original encryption keys reproduces the original triple ciphertext exactly. This is independently checked in `validate.py`.

The actual literal 100-letter ciphertext is likewise transposed without changing or guessing a letter. The wider 50,000-frontier odd-pass scout remains incoherent (`target-transposed.wide-results.txt`). This structurally explores the equal-width-ten odd-pass class as a bounded scout; retention of only 64 column candidates and the demonstrated held-out rank bias prevent a complete family exclusion. The same conclusion applies to the even-pass scout. No additional SA restarts were used.
