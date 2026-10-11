# Real 52-hole mask beam: positive conditional calibration, failed blind rings

A structural language beam recovers all three fresh physical masks when both mixed rings are supplied. It does not yet recover an unknown ring/mask key, so no actual cipher was attacked.

The immutable verified wheel supplies 52 adjacent effective distances summing 179. For a start hole h0 and the rth selected hole hr in positive cyclic order, the relative displacement is coordinate(hr)-coordinate(h0)+179 if the physical hole index wraps. After q complete selected-stop cycles, add 179q, equivalent to 23q mod26. All candidate masks are strictly increasing relative to their start around the actual wheel; no independent periodic increments are invented.

## Structural mask algorithm

For supplied ring permutations P/O and active count m, each proposed physical hole at ordinal column r determines all plaintext letters at positions r+qm. The beam assigns these columns in physical order, reserving enough remaining real holes to complete the mask. Language windows wholly inside a cycle row are scored as soon as their last column is assigned. Windows crossing a cycle boundary close at the final column, using retained first and last columns. All 52 possible starting holes are searched. Beam retains 256 paths per depth and four final masks per start (208 candidates/control). This is a bounded beam, not an exhaustive proof of mask recovery.

Frozen 2/3/4/5-gram weights are 0.1/0.15/0.4/0.8. Models 2/3 were generated only from first 80% complete UD TRAIN sentences, using the same preparation as the existing frozen ring 4/5 models. Unseen ngram floor is -n. Controls are independent genuine Slovak UD TEST segments of 385 letters at new prepared offsets 10000/11500/13000, excluding prepared sentences appearing anywhere in TRAIN. Accents removed, digits spelled, Q proper-name boundaries and X sentence markers are constructed control preparation, not established historical procedure. J takes only one ordinary press here; selective-J extra presses break the assumed ciphertext-position column model and remain outside this branch.

## Known-ring calibration

| Active stops | Full plaintext | Physical active mask | Starting stop | Rank among retained candidates |
|---|---|---|---|---|
|20|385/385 exact|Exact|Exact|0|
|26|385/385 exact|Exact|Exact|0|
|30|385/385 exact|Exact|Exact|0|

Both mixed input/output rings and the count are explicitly SUPPLIED in this calibration. Mask and starting phase are unknown to the beam. True whole scores are 472.874152,388.768657,559.840845. Independent direct-wheel traversal encoding agrees with a separate cumulative-coordinate inverse for all controls. All 624 retained masks independently reencrypt the complete ciphertext and their language scores match complete rescoring. Success demonstrates conditional mask recoverability, not actual cryptanalysis of unknown rings.

## Blind unknown-ring/mask alternation, failed

A separate fresh-control pilot supplies only m=26. It does not read planted masks, rings or plaintext. Eight independent random ring pairs initialize a 64-wide real-hole mask beam across all 52 starts, followed by 30000 joint input/output ring swap proposals. Four alternating passes renew the mask beam under the current rings and then refine the rings under its selected real mask. Whole frozen multi-gram language score alone chooses candidates. The current mask is preserved when a truncated beam returns a worse score; ring refinement retains its best state including its supplied seed. There is no standalone IC/pair/triple objective and no true-key seed.

All eight starts fail. Best whole score is -1112.01 versus true 388.768657; diagnostic maximum is only 25/385 matching letters across all 32 iterations, never selected by that overlap. Several runs stall after one pass. This is a coupled discovery/basin failure. It cannot be repaired merely by interpreting successful known-ring mask calibration as an unknown-ring solution. No unknown-m sweep or target350/351 attempt follows.

Every retained blind beam row and joint winner independently passes direct-wheel full inverse/reencryption and complete language rescoring: 6688 rows, comprising 32×208 masks plus 32 joint winners. Together with conditional calibration, 7312 complete candidate rows were checked. All candidate mask/ring keys, full texts, seeds, selection rules, corpus/model provenance and failed trajectories are saved. Correct reencryption confirms algebraic consistency only; it does not prove guessed target language.

## Reproduce

```sh
python3 batches/kryha-mask-sol61/prepare.py
clang++ -O3 -std=c++17 batches/kryha-mask-sol61/maskbeam.cpp -o batches/kryha-mask-sol61/maskbeam
clang++ -O3 -std=c++17 batches/kryha-mask-sol61/ringjoint.cpp -o batches/kryha-mask-sol61/ringjoint
python3 batches/kryha-mask-sol61/run-known.py
python3 batches/kryha-mask-sol61/check-known.py
python3 batches/kryha-mask-sol61/run-blind.py
python3 batches/kryha-mask-sol61/check-blind.py
```

These deterministic runs overwrite their own batch outputs; archive them before comparing changed parameters. The blind runner reads only control ciphertext, count, wheel geometry and frozen TRAIN models; planted data are introduced only afterward by the checker. Models and cipher sources outside this batch are read-only. No watcher, reviewer, marker or register entry created. No historical cipher family excluded.
