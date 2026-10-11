# Unknown alphabets with progressive d_i=i

Two independently keyed genuine held-out controls calibrate the conditional progressive26-position model. This is a distinct hypothesis from either actual programmable Kryha-wheel stepping or ordinary fixed-alphabet Vigenere. Unknown input/output alphabets are26 bijective permutations. Starting offset can be absorbed into the output ring; reversing displacement sign can be absorbed by reflecting both rings. No phase sweep is needed for this family.

TRAIN histogram profile generates300 output-ring candidates. Generic TRAIN 4-gram MASC ranks them; only its highest language score seeds joint refinement. Pure TRAIN 5-gram refinement uses each unchanged4-gram winner, for every control/target. No control truth or word/key seeds enter any optimization. Coverage enumerates all 325 input-ring swaps plus the unchanged key, keeping the output ring fixed and recording full keys/plaintexts/independent reencryption. Its candidates rank by frozen5-grams.

Control 385:4-grams yielded380/385 correct letters and exact output ring, with a single X/Z exchange; true4-gram score840.6398 was lower than selected852.791, an objective failure. Pure5-gram yielded385/385 exact plaintext, both rings26/26 correct up to common rotation. It also ranked exact plaintext first among all326 input neighbors of either winner. W is absent, but all25 observed symbols and bijection determine its remaining input slot. Control 115:4-gram8/115 and5-gram9/115, no exact neighbor. True language score exceeds the failed winner, showing discovery failure rather than a preference for that false text. This supports an exploratory long-text test, not a general recovery guarantee or short-message exclusion.

Reproduce from repo root:

```sh
python3 batches/progressive-ring-sol61/prepare.py
clang++ -O3 -std=c++17 batches/progressive-ring-sol61/profile.cpp -o batches/progressive-ring-sol61/profile
clang++ -O3 -std=c++17 batches/progressive-ring-sol61/masc.cpp -o batches/progressive-ring-sol61/masc
clang++ -O3 -std=c++17 batches/progressive-ring-sol61/joint.cpp -o batches/progressive-ring-sol61/joint
clang++ -O3 -std=c++17 batches/progressive-ring-sol61/joint5.cpp -o batches/progressive-ring-sol61/joint5
python3 batches/progressive-ring-sol61/run.py
python3 batches/progressive-ring-sol61/refine5.py
python3 batches/progressive-ring-sol61/diagnose.py
python3 batches/progressive-ring-sol61/coverage.py
```

`run.py` resumes existing profile/MASC/joint files. `refine5.py` recomputes standalone5-gram refinement from the fixed4-gram winners. `coverage.py` keeps the entire neighbor list; it does not select according to planted truth. `targets.py` runs whole literal350/351/369 forward/reverse;369 is an explicitly weak115-letter branch. `refine5.py targets` post-refines those unchanged winners. There is no silent framing removal or unknown-symbol substitution.

All scores are generic language scores, not plaintext correctness evidence. Full coherence and independent reencryption are required for a real target solution. Control success on385 and failure on115 must remain distinct.

Final status: six whole target branches completed; no coherent full target plaintext. All 7,632 retained language/neighbor keys passed independent full inverse and reencryption; all 2,400 profile candidates independently rescored. REPORT.md preserves the positive385/failed115 control distinction and limitations.
