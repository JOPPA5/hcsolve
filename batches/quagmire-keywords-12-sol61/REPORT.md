# HCP334 restricted keyword Quagmire I / II experiment

No supported solution. All 30 target branches remain incoherent; heuristic failure does not exclude either general cipher family or this restricted dictionary family. No source or marker was changed.

Definitions: S is keyword position-to-letter alphabet; A is its inverse. QI: C=(A(P)+R) mod26, P=S(C−R). QII: C=S(P+R), P=A(C)−R. This is distinct from QIII, which keys both sides. ACA worked examples were independently reproduced: [QI](https://www.cryptogram.org/downloads/aca.info/ciphers/QuagmireI.pdf), [QII](https://www.cryptogram.org/downloads/aca.info/ciphers/QuagmireII.pdf). Every phase permits every absolute shift, including nonzero R0. No indicator-word restriction was assumed.

Frozen search: identical 18,098 TRAIN-derived deduplicated keyword alphabets from prior QIII batch; same Slovak TRAIN unigram/4gram/5gram models. Screen every alphabet with unigram phase shifts + six coordinate passes, retain128; four starts ×5000 proposals under4grams; retain64; four starts ×10000 under5grams; choose highest5gram without truth. RNG334330061. TEST sentences and independent key seeds differ from prior controls. Selection never uses planted plaintext/key.

| Model | T | Readable matches | Full26-letter maps/phase | Keyword | Seconds |
|---|---:|---:|---|---|---:|
| Q1 | 15 | 148/148 | True | prehrnala | 15.04 |
| Q1 | 3 | 148/148 | True | vyzdvihuje | 3.59 |
| Q1 | 9 | 148/148 | True | zamknut | 8.80 |
| Q2 | 15 | 148/148 | True | pokusat | 15.32 |
| Q2 | 3 | 148/148 | True | najdaromnejsie | 3.40 |
| Q2 | 9 | 148/148 | True | uniforma | 9.43 |

Each control has150positions and erasures at70/94; shifts independently drawn1..25. Blind recovery matches148observations AND every one of26input letters in every phase. This establishes recovery on these six independent fixtures, not general completeness. Missing plaintext is not claimed. Controls preserve splits, seed, full ciphertext, plaintext, complete keys in planted/result JSON.

Target: full150-position transcription hypothesis, ?DZQR erasure at70 plus five FWXX gap placements at90+gap. Literal W and all other observed source letters preserved. Three periods per model (3/9/15), all five placements,30branches. All saved320candidate rows per branch and control independently decrypted/re-encrypted against every observed ciphertext position, with independent ngram score checks (11,520rows total). Equal source/work hashes checked at completion. No candidate forms a whole coherent Slovak message. Alphabet keywords and local common-word fragments cannot establish a solution.

| Model | T | Highest5gram | Gap | Keyword |
|---|---:|---:|---:|---|
| Q1 | 3 | -571.069 | 0 | fatamorganu |
| Q1 | 9 | -498.186 | 2 | nepristojnosti |
| Q1 | 15 | -423.735 | 2 | nedorozumeniam |
| Q2 | 3 | -580.482 | 0 | sosolc |
| Q2 | 9 | -493.559 | 1 | bernolakovcov |
| Q2 | 15 | -400.923 | 2 | vypytoval |

The family is a narrower new dictionary restriction; T3 overlaps earlier arbitrary-alphabet QI/QII experiments but is not a duplicate of their recovery method. T9/T15 extend those prior target periods. No historical evidence presently identifies334 with a Quagmire system. Dictionary coverage, retained candidate pruning, language scoring, normalization, and the150-position erasure framing remain limitations.

Reproduce: `python3 batches/quagmire-keywords-12-sol61/build.py && clang++ -O3 -std=c++17 batches/quagmire-keywords-12-sol61/search.cpp -o batches/quagmire-keywords-12-sol61/search && python3 batches/quagmire-keywords-12-sol61/run.py`. Existing results are preserved; command deterministically overwrites only this batch. `manifest.json` contains corpus, dictionary, frozen models and source hashes.
