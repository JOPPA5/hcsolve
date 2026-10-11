# Physical Kryha paired bridge with a supplied active-stop count

The reusable bridge is cloned from the read-only `batches/kryha-mask-pair-sol61/` implementation. This batch generalizes physical-stop ordinals, masks, beam nodes, profile histograms and schedule loaders to supplied counts 20 through 30. The ring alphabet stays 26. Clone hashes and source paths are recorded in `clone-provenance.json`. The 26-stop unknown-key search is not repeated here.

The 52 documented effective adjacent distances and unwrapped coordinates are read-only `batches/kryha-wheel-sol61/wheel52.json`. Every ordered selected-stop schedule walks one real wheel revolution and sums to 179; full-cycle residue is 23 modulo 26. Both complete 385-letter messages share unknown input/output rings, one unknown physical subset and one unknown starting selected stop. Both start/reset identically, with ordinary one-stop advancement after every character, including J. These are conditional assumptions for the target telegrams, not established historical operating rules.

`prepare.py` generates fresh independent held-out Slovak TEST paired controls for m=20 and m=30. Each uses independent random mixed rings, independently random physical subset/start, and independently selected TEST offsets. Every TEST sentence found anywhere in TRAIN is excluded. Search never opens `plant.json`. The count alone is supplied; no true key, mask, phase, plaintext or true-frequency profile seeds the optimizer.

## Unchanged search budgets

For each count, `pair-cycle` uses 32 blind output-ring starts and 20,000 proposals each, followed by ten greedy swap scans, using ordinal-column collision constraints with known 179-cycle displacement. Every retained ring receives eight independent physical mask/profile starts of 10,000 proposals each. All 256 mask/output-ring candidates receive four 15,000-proposal shared input-ring MASC starts. Only complete per-message frozen TRAIN 2/3/4/5-gram score selects the four seeds. Weights are 0.10/0.15/0.40/0.80; every window remains in its own message.

Each of four seeds receives four physical-mask/ring alternations. Physical mask beams enumerate all 52 starting holes, width 64, retaining four complete masks per start. Ordered hole constraints and cycle sums are mechanical, not free column shifts. The better existing mask may survive a truncated worse beam. Shared-ring refinement uses 30,000 proposals each time. The final generic winner is the highest language score across the four operative finals; calibration does not select the closest candidate to planted truth.

## Reproduction and verification

Compile `pair-{cycle,mask-profile,bridge-masc,mask,joint}.cpp` with `clang++ -O3 -std=c++17` into matching binary names. Run `prepare.py`, `check_mechanics.py`, then `run_controls.py`. Run `verify_case.py CONTROL_FOLDER COUNT` on complete cases. The mechanical check covers all eleven supported counts with fresh random known keys and 770 symbols each; it is a zero-proposal loader/encoder check and is not blind recovery or a count-26 discovery repeat.

`codec.encode` walks the original adjacent arcs; `codec.inverse` separately uses absolute selected-hole coordinates and full revolutions. Verification independently checks all full candidate encodings/inverses, permutation keys, physical schedules, cycle scores, profile likelihoods and message-separated n-grams. Saved incomplete `.partial` files are not completed results; completed stages are reused without identical reruns.

A target scout is permitted only after the corresponding fresh count control recovers both entire texts under generic final selection. Then only the whole source-preferred forward pair is attempted. No target source, canonical transcription, metadata, marker, watcher or reviewer is changed. A finite search failure cannot exclude a count or cipher family.

## Added coupled local neighborhood

The original m20 bridge's partial control prompted a substantive move family rather than more identical restarts. `pair-local-mask.cpp` jointly enumerates physical one-hole/start neighbors with every input-ring transposition and cyclic rotation, selecting only by the frozen complete language score. The output ring remains the operative blind output ring. `run_local.py CASE_FOLDER` applies this to the unchanged highest-scoring blind final. The full m20 control passes after this added stage; its earlier non-exact bridge and the m30 failure stay preserved separately.

Changing a starting stop shifts every other column displacement by the same C. Rotating the input ring by C can preserve those columns while repairing the starting-stop column. This exact relative-offset move is included generically; it is not a supplied true key. Local output is five lines: full score, 52 ring integers (26 input slots then 26 output positions), both full candidate texts, and the ordered physical stops.

Compile the additional `pair-local-mask.cpp` into `pair-local-mask`. Reproduce the whole preferred forward count-20 case with `python3 batches/kryha-count-pair-sol61/run_target20.py`; existing completed stages are reused. Verify each local winner separately with `verify_local.py CASE_FOLDER`. Summary outcome and independent root evidence are in `REPORT.md`. The batch is complete, but neither target is solved.
