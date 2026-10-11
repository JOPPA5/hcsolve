# Sources and conventions

Primary algorithm references, consulted without searching for target solutions:

- CrypTool Porta: https://legacy.cryptool.org/en/cto/porta . Worked example GEHEIMNIS, KEY -> OPVZTNFTE. Standard class is floor(keyword letter / 2). This fixes the sign of class labels relative to old HCP332 code, without changing the set of 13 alphabets searched.
- CrypTool Beaufort: https://legacy.cryptool.org/en/cto/beaufort.html . Reciprocal C = K - P mod 26.
- CrypTool Vigenere: https://www.cryptool.org/en/cto/vigenere/ . C = P + K mod 26.

The old HCP332 exact_periodic.cpp and reciprocal.cpp supplied the family/formula context. The new implementation uses frozen 3/4/5-gram scores, incremental affected windows, blind monogram starts, random starts, annealing and exhaustive coordinate refinement. Corpus/model provenance and hashes are in provenance.json. No corpus/model files were modified. UD TEST sentences were excluded if also found verbatim normalized in TRAIN or previously used in the short-MASC controls. Whole sentences, sometimes two complete sentences combined to obtain the requested exact length, are recorded in controls.json. No target words or control truth were used as starting keys.

Variant Beaufort here means C = P - K, with inverse P = C + K. Every Vigenere candidate therefore has the same variant-Beaufort plaintext under negated key residues; both conventions are emitted without repeating the optimization.
