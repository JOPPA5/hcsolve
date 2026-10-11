# Alternating ciphertext-column directions

This is a distinct conditional transposition branch, not a historical identification. Ordinary row writing is followed by keyed column readout, but directions alternate down/up by **readout rank**, with either starting direction. Arbitrary independent per-column reversal is not allowed. Both full ciphertext stream orderings are explored separately.

For a rectangular grid, ciphertext chunks have equal known length; reversing chunks at alternating readout ranks converts this hypothesis to the existing frozen column-fragment beam. For the one-long-column geometry (length modulo width = 1), the beam already enumerates which ciphertext chunk is long; each such hypothesized chunking is normalized by alternating reversal before search. The long chunk must occupy physical column 0. Other irregular remainders are outside this implementation.

`beam.cpp` and `one-long.cpp` copy the prior independent frozen beam, with only chunk direction normalization added. Scoring reads unchanged TRAIN models 2..5 from `batches/columnar-stratified/`, with the same weights 0.2/0.15/0.4/0.8 and beam size 10,000. No control truth or historical quote seeds the optimizer. Models are read-only and their hashes recorded.

Controls:

```
python3 batches/columnar-serpentine-sol61/experiment.py
python3 batches/columnar-serpentine-sol61/damage_control.py
python3 batches/columnar-serpentine-sol61/short_controls.py
```

Fresh held-out TEST passages explicitly excluded from TRAIN supply 85/100/115/400 controls for both geometries, new independent keys and starting directions. Both starting-direction searches are combined and ranked only by frozen model score before diagnostic truth comparison. Six of eight initial controls recover exactly: rectangular 85/100/400, one-long 100/115/400. Rectangular 115 and one-long 85 fail. Five randomly selected cipher erasures in each 400 control still give exact **masked** plaintext at rank 0; no missing character is filled. Supplemental fresh short controls recover rectangular 55 and one-long 55/65, while rectangular 65 fails. These are recovery successes/failures on stated instances, not universal guarantees by length.

Targets:

```
python3 batches/columnar-serpentine-sol61/targets.py
```

Only the complete literal bodies of HCP363/393/345/396/369 are explored, widths 2..26 where rectangular or one-long geometry applies, both whole-stream orderings and both alternating starting directions. An explicit standalone numeric header is separated from the body; no five-letter indicator omission, glyph correction, padding or additional plaintext constraint is introduced. HCP363 nonletter glyphs remain erasures. Other irregular grids remain untested. Negatives are heuristic failures, not exact family exclusions.

Each candidate retains physical width, complete readout column permutation and its per-rank direction list, together with whole-stream reversal. An independent position-based encoder and inverse verify every retained candidate; reencryption is algebraic consistency, not evidence of intelligible plaintext or the actual historical key. Raw outputs and complete control truths are retained. All writes confined to this batch; source/cipher files and other batches read-only. No markers, watchers, reviewer, register entry or published target solution lookup.
