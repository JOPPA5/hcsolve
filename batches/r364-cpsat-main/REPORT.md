# Native interval CP-SAT known-plaintext experiment

This experiment does not recover HCP364. It tests an exact representation of triple irregular columnar transposition and two propagation/search improvements against independently encrypted controls. No actual HCP364 ciphertext was submitted to these runners.

## Model and independent validation

`solve.py` represents each physical column as a fixed-length interval. NoOverlap packs these intervals into a stream of exactly the same total length. Element constraints copy complete columns into the next stage. Intermediate letter inventories, optional daily ranks of physical column zero, unknown fillers and bounded substitution errors are explicit. Keys are full column readout permutations, and all returned witnesses are independently re-encrypted and inverted by the runner.

The independently written audit in `../r364-cpsat-audit-sol61/REPORT.md` compares this unchanged model against exhaustive permutation enumeration. All 216 small cases agree: 106 SAT and 110 UNSAT, including 86 structural same-inventory negative cases. In total 348,192 admissible key triples were enumerated. This validates the tested small domain; it does not establish feasible search performance at historical widths.

## Blind controls and limits

`controls.json` uses an independently authored 65-letter test string, not recovered historical plaintext. Double-width 8/9 controls succeed both with and without supplied keys. The triple-width 21/19/20, daily rank 7 control succeeds when the planted keys are explicitly supplied as a consistency test, but the blind run returns UNKNOWN after 60 seconds. Supplied keys are never described as recovery.

`anchor_engine.py` adds redundant propagation of the full multistage coordinates of unique letters, preserving the base model in `solve.py`. Both the existing blind control and a fresh 65-letter cover-quote-plus-R fixture at daily rank 5 remain UNKNOWN after 60 seconds each. The new fixture uses independently shuffled keys, absent from the blind search inputs. This is a propagation failure to obtain a witness within the budget, not UNSAT.

`optimize_engine.py` changes the objective to minimize Hamming distance and uses CP-SAT large-neighborhood search, initialized solely by previously recovered blind Hungarian candidate keys. Three 65-letter fixtures retain 17, 17 and 16 ciphertext mismatches after 60 seconds each: no improvement over the initial 48/65, 48/65 and 49/65 matches. All saved predictions are valid encodings under their complete candidate keys, but differ from the observed ciphertext and are not solutions. Truth keys were not used as hints.

## Reproduction

The dependency is OR-Tools 9.15.6755 in `/private/tmp/hcsolve-ortools`; provenance is in SOURCES.md. Run from the repository root:

```
python3 batches/r364-cpsat-main/controls.py
python3 batches/r364-cpsat-main/anchor_controls.py
python3 batches/r364-cpsat-main/optimize_controls.py
```

The JSON files preserve fixtures, explicit assumptions, statuses, elapsed times, keys and mismatch positions where available. Completed runs leave no process active. No source, solution, review or marker was changed by these runners.
