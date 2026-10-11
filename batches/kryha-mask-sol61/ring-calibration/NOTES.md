# Known-mask unknown-ring calibration

Three further fresh 385-letter held-out controls use real 52-hole wheel masks at 20/26/30 active stops, independent random mixed rings and phases. Masks/phases are supplied as their exact physical step schedules; no true ring or plaintext enters optimization. Whole-ring discovery remains conditional on that supplied schedule. This is not blind unknown-mask recovery and does not justify attacking actual targets in the unrestricted ring family.

Generic profile/MASC/joint sources are adapted read-only from progressive-ring-sol61, replacing unit steps with the supplied real-wheel schedule. Frozen first-80%-TRAIN unigram,4gram,5gram models remain unchanged. Fresh TEST prepared offsets15000/16500/18000 exclude prepared sentences appearing anywhere in TRAIN. No target words, ring seeds or control-specific training. Preparation is disclosed in prepare.py: accents removed, digits spelled, Q proper-name boundaries and X sentence endings; exact385-letter segments. No selective-J extra press.

| Stops | 4-gram winner | Fixed 5-gram refinement | Output ring | Blind input-neighbor exact coverage |
|---|---:|---:|---|---|
|20|385/385|385/385 exact|26/26 up rotation|Rank0|
|26|352/385|380/385|26/26 up rotation|Rank2 after5 refinement|
|30|378/385|385/385 exact|26/26 up rotation|Ranks0/1 after5 refinement|

Pure5 refinement uses every unchanged4 winner; there is no truth-based seed choice. All325 input-ring swaps plus unchanged key are retained and ranked generically, output fixed. The m26 residual is a global F/G exchange; exact truth is retained at rank2, not the operative winner. m30 duplicate exact plaintext ranks differ only in unobserved input slots. No claim of a uniquely identified unused alphabet mapping. All three output rings are exactly identified up to the unavoidable common rotation, evaluated only after generic selection.

Independent direct traversal of the physical52-hole wheel reconstructs each supplied schedule and agrees with separately generated cumulative-coordinate encoding/inverse. All2862 language/neighbor candidate rows pass complete physical inverse and reencryption:900 MASC,6 joint winners,1956 input-neighbor candidates. All900 output-ring profile candidates are independently rescored and checked as permutations. Controls, masks, phases, truth keys, optimized keys, full texts, scores, rankings, corpus/model hashes and seeds are preserved separately.

Comparison with prior failures: mask beam with known rings recovered3/3 exact physical masks and starts; this known-mask profile/MASC pipeline recovers3/3 output rings and retains3/3 exact plaintexts in its fixed5 neighbor coverage. Earlier fully unknown-ring/mask alternation still failed. Thus the main bottleneck is coupled initialization/basin discovery, with remaining finite-sample input-language ranking ambiguity. Conditional successes do not establish unrestricted blind recovery.

A substantive future coupled initialization would start from independent physically legal approximate masks, run this unknown-ring profile/MASC stage to obtain language-selected ring seeds, then use the real-hole mask beam and joint refinement. Its seeds must be selected without true mask/rings/plaintext, and blind controls must pass before any unrestricted actual target. This differs from previous random-ring initialization; it is only a proposal here, not a validated solver. Do not expand identical failed random-ring restarts.

Reproduce after compiling profile.cpp,masc.cpp,joint.cpp,joint5.cpp with clang++ -O3 -std=c++17:

```sh
python3 batches/kryha-mask-sol61/ring-calibration/prepare.py
python3 batches/kryha-mask-sol61/ring-calibration/run.py
python3 batches/kryha-mask-sol61/ring-calibration/coverage.py
python3 batches/kryha-mask-sol61/ring-calibration/check.py
```

The optimizer runner reads only explicit ciphertext/schedule files and frozen models, never controls.json. Checkers introduce true data afterward. Stage files resume existing completed outputs. No previous batch failures, cipher files, watcher/reviewer or marker changed.
