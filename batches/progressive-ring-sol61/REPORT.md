# Conditional progressive-ring scout: positive long control, unresolved targets

The newly tested family is C_i = O^{-1}(I(P_i)+i mod 26), with unknown bijective 26-letter input/output rings. The displacement advances one letter position per symbol. Initial offsets and opposite signs are absorbed into ring rotation/reflection, so one phase/sign representative suffices. This is not the verified 179-total programmable Kryha wheel and does not establish any historical machine attribution.

The frozen TRAIN histogram profile/MASC/joint pipeline was adapted from the earlier ring-profile batch. Sources and exact budgets are credited in SOURCES.md/manifest.json. Each known ciphertext generates 300 output-ring profile candidates; all receive frozen TRAIN 4-gram MASC scoring. The highest language winner alone seeds joint 4-gram refinement, followed by pure frozen 5-gram refinement from that unchanged winner. Finally every one of 325 input-ring swaps plus unchanged key is saved for each 4-/5-gram winner, with output ring fixed. No planted word/key or truth-based candidate selection occurs.

## Independent controls

Fresh Slovak UD TEST prepared sentences exclude any prepared sentence found anywhere in UD TRAIN. The reused models were trained only on the first 80% of complete TRAIN sentences. Control 385 is a genuine prepared corpus segment at new offset 8000; control 115 consists of a complete prepared sentence or complete sentence combination. Accents removed, numbers spelled, Q proper-name boundaries and X sentence boundaries are constructed preparation, explicitly disclosed. Both mixed rings and independent RNG seeds are in controls.json.

| Control | 4-gram joint | Pure 5-gram joint | Output ring | Neighbor coverage |
|---|---:|---:|---|---|
| 385 letters | 380/385 | **385/385 exact** | **26/26 exact up to rotation** | Exact text ranked first by 5-grams in both 326-key pools |
| 115 letters | 8/115 | 9/115, failed | Not recovered | Exact text absent from both pools |

Long 4-gram error was only a global input X/Z exchange. Its score 852.791 exceeded true score 840.639835, an actual scoring defect. Generic pure 5-grams repaired it, scoring the exact text 6.212063. Both long rings match all 26 planted positions under the common rotation gauge. W is absent from the plaintext, but bijection and 25 observed symbols determine the remaining input slot. Short truth scores exceed the failed winners (4-gram 145.101303 versus 84.9509; 5-gram -132.463562 versus -285.769), so discovery failed there. All retained output-ring profile scores exceeded truth, even in the successful long case: profile ranking is not itself a key-identification proof.

## Exploratory actual scope

The matching-length long positive control justifies a bounded conditional whole-body scout of HCP350 and HCP351, each 385 letters, forward/reverse. A weak short branch also tests whole HCP369 (115 letters), forward/reverse; its length-matched control failed and that branch remains exploratory. All literal symbols are retained; no presumed header/indicator is removed and no letter is filled. Every branch uses the unchanged pipeline and both input-neighbor pools.

All six actual branches completed. Whole 4-gram winners, whole 5-gram winners and highest-ranked neighbor candidates were inspected as complete messages. They are incoherent. No supported full plaintext/key was found. Isolated language-like words and exact reencryption are not decipherment evidence. No cipher family, framing, ring system or historical Kryha interpretation is excluded. Unknown alphabet conventions, prepared-symbol assumptions, transcription uncertainty and more complex stepping remain outside this finite condition.

## Independent checks and reproducibility

- 2,400 profile candidates independently rescored and checked as ring permutations.
- 2,400 MASC candidates, 16 joint winners and 5,216 complete neighbor keys independently inverted and reencrypted: **7,632 full checks passed**.
- Complete raw keys/texts, scores, candidate rankings, seeds, corpus/model hashes and budgets saved.
- Source cipher files unchanged. Marker scan for 350/351/369 empty; no watcher, reviewer, marker or register entry created.

Control commands are in README.md. Actual reproduction adds:

```sh
python3 batches/progressive-ring-sol61/targets.py
python3 batches/progressive-ring-sol61/refine5.py targets
python3 batches/progressive-ring-sol61/coverage.py
python3 batches/progressive-ring-sol61/check-all.py
```

`targets.py` and the primary pipeline resume existing completed stage files. Existing unchanged outputs should be archived before comparing parameter changes. `refine5.py` deterministically reruns its fixed winner refinement. Checks, coverage and inspection do not alter the optimizer's seeds or frozen models.
