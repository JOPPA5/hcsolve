# Corrected HCP364 conditional double-columnar branch

All 49 ordered width pairs in 16..22 are UNSAT with the corrected EXC input, both finite EXCUV/EXCVU alternatives, and a free fifth X insertion at any position in the four-sentence-X quote template. Each exact case used a 15-second limit; all completed in under 1.4 seconds. No key witness was found.

This replaces the logically irrelevant old ERC-input double tests for this precise family. It excludes only two ordinary irregular columnar transpositions with these widths, the stipulated quote preparation, omission of original group 3, and either of these two source readings. It does not exclude a historical R triple, other preparation, other widths, or another plaintext. The reply may be contextual prose rather than encrypted content; its role remains conditional. The U/V order remains visually uncertain; inventory compatibility does not prove either reading.

Three independent fresh blind controls validated the newly combined unknown insertion and finite ciphertext alternative encoding: widths 16/22, 19/19, and 22/16; insertion positions 0, 37, and 64. The first uses a freshly randomized full-alphabet template; the latter two use the same quote template only as independently encrypted synthetic controls. All recovered the complete planted 65-letter plaintext. Every SAT result was independently encoded by explicit index gathering and inverted by column filling over all 65 positions. Target runs used no known key, alignment, or planted control truth.

The solver is an unchanged copy of `batches/r364-review-collation-sol61/exact_cover_insert.py`. `provenance.json` records the variants file hash; `controls.json`, individual target files, and `results.json` retain full results. Source files and cipher directories were not modified. No markers or watchers were created.

Reproduce from repository root:

```
python3 batches/r364-corrected-double-sol61/run.py
```
