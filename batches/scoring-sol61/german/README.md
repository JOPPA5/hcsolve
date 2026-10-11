# German short substitution scoring experiment

Primary sources are unchanged in source/: UD German GSD train/test and LibreOffice de_DE_frami dictionary, affix rules and licenses. build.py trains character models only on dictionary forms and UD train; test is excluded. build-report.json records hashes and expansion details. Normalization folds umlauts to A/O/U and sharp S to SS; alternative historical conventions remain untested. Affix expansion is approximate and compounds are not exhaustively generated.

Frozen mono-frequency-seeded-strict from the parent directory recovers both independently planted German controls exactly (40 and 43 letters). verification.json records full equality. Single-anchor runs on all eight HCP332 forward/reverse/O/D/prefix variants produced incoherent whole readings; they are not plaintext.

The target has a flatter letter distribution than those initial controls. matched-control.py therefore samples qualifying 40-letter windows from UD TEST only, with fixed seed, IC <= target and >=21 distinct letters. Eleven of 45,929 qualify. The sampled text is erwirtschaftsgipfelvonbundeskanzlerhelmu (IC .035897, 22 letters). Its source sentence, selection, random substitution and test hash are recorded in flat40-generation.json. This control is never inserted into the model or supplied as a crib.

Single-anchor optimization fails this matched control despite the true plaintext scoring better. Increasing maximum word length alone added no seeds. anchors.py and pairs.cpp generically enumerate non-overlapping compatible pairs of dictionary-pattern anchors, enforcing both directions of the bijection, deduplicate masks, prioritize assigned-letter coverage, and complete unknown permutations with fixed seed. All 2,726 compatible masks for this control were searched with 2,000 stochastic proposals each. It recovers exact whole plaintext (flat40-pair-check.json). The full alphabet on unused cipher letters remains unconstrained.

Reproduce the matched control:

```
python3 batches/scoring-sol61/german/anchors.py batches/scoring-sol61/german/flat40-cipher.txt batches/scoring-sol61/german/flat40-anchors
c++ -O3 -std=c++17 batches/scoring-sol61/german/pairs.cpp -o batches/scoring-sol61/german/pairs
batches/scoring-sol61/german/pairs batches/scoring-sol61/german/flat40-anchors.anchors.tsv batches/scoring-sol61/german/flat40-pair-seeds.txt 20000
batches/scoring-sol61/mono-frequency-seeded-strict batches/scoring-sol61/german batches/scoring-sol61/german/flat40-cipher.txt batches/scoring-sol61/german/flat40-pair-seeds.txt
```

run-pairs.py applies the unchanged method to the eight HCP332 readings, at most20,000 masks per reading. This is a bounded optimizer, not an exhaustive MASC exclusion. distribution.py in the parent directory describes modern-corpus rarity, not historical probabilities. quadgrams.tsv is a headerless count-score export for older solvers; model4.tsv has a floor header and log probabilities and must not be interchanged with it. heldout200-plain.txt is from test only with generation provenance, never used in model training.
