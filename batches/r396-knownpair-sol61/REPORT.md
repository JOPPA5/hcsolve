# Conditional HCP387/396 known-pair key pilot

No key was recovered. This bounded pilot did not execute actual target key searches because neither exact formulation passed fresh blind controls. There is no target exclusion.

The published HCP387 draft and original ciphertext are read-only context from `batches/repeat396-387-sol61/REPORT.md`, explicitly attributed to the already solved record. The preferred final plaintext has 50 letters. Under the conditional omission of group 8 DWJPM, the original 387 body has one surplus P and one missing F. `conditional-pair.json` preserves the literal body and exactly three hypothetical P→F alternatives at body positions 3, 20 and 23. Printed Ps are source-supported; no alternative is a claimed glyph correction. The repeat 396 additionally differs at A/S and N/M; this pilot uses the original published pair and does not normalize the repeat.

The tested family is the independently primary-validated ordinary irregular three-stage R core at widths 21, 19, 20. Arbitrary readout permutations are unknown; no header-derived alignment or daily key is supplied. Hardware/procedure compatibility does not establish adoption or indicator omission for this pair.

Two fresh independent random key triples encrypted (1) an independently shuffled matched 50-letter inventory and (2) the known draft in its original order. Neither planted key nor alignment was supplied to blind recovery. A known-key encoding test passed in both formulations, including the full 50-letter encoder and inverse. The operative positive-control criterion is any consistent complete key, not recovery of the planted key.

The exact chunk-cover formulation and the structurally distinct source-position-tracing bit-vector formulation each returned UNKNOWN on both fresh controls at a 30-second limit. Position tracing includes exact irregular chunk starts and all same-letter occurrence alternatives; its four unique-letter anchors are D, F, V and M. These failures mean recovery performance is unvalidated, not that controls or targets lack solutions. No target cases were run after the failed controls. A second-witness/key-blocking uniqueness experiment requires a first SAT witness and therefore was not possible.

Counting diagnostics in `identifiability.json` show roughly 163.39 bits of distinct 50-letter anagrams and 183.30 bits of raw three-permutation key space. These counts do not prove target existence or nonuniqueness; no uniqueness claim is made. A future coupled same-day-message branch would introduce further unproved shared-key and language assumptions.

Reproduce from repository root:

```
python3 batches/r396-knownpair-sol61/pilot.py
python3 batches/r396-knownpair-sol61/position_pilot.py
```

Both solvers are copied from preserved prior batches, not modified in place. All generated keys, inputs and failures are retained. All processes exited. No cipher directory, source, marker or watcher was changed.
