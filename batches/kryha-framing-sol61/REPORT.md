# HCP350 conditional framing attack

All work here is diagnostic solver work, not an accepted solution. HCP350/351/334 source, work files, metadata and state markers remain unchanged. Marker snapshots accompany each result.

The literal350 and351 transcriptions both have385letters. Their first20letters agree at16positions and last10at9positions (`framing.json`). No document establishes an open indicator/header/trailer. The tested350 crops remove20leading **letters** (365remaining), or20leading+10trailingletters (355remaining). These are explicit framing hypotheses, not source corrections.

## Exact generic model and direction equivalence

Use the original17steps7,6,7,5,6,7,6,8,6,10,5,6,5,7,6,5,9 and arbitrary mixed26-letter input/output rings. Ciphertext at offsetd obeys c=O_inverse(I[p]+d). For negative steps, reflection I′=-I andO′=-O gives exactly the same ciphertext under positive steps: O′_inverse(I′[p]+d)=O_inverse(I[p]-d). In slot-to-letter notation P′[x]=P[-x]. This is a complete algebraic equivalence for arbitrary mixed rings, not a restriction to alphabetic rings.100independent randomized365-letter checks spanning all17phases pass (`reflection.json`). Initial constant relative offset is absorbed by arbitrary input-ring positions.

## Frozen procedure and independent calibration

Copied350 algorithms and compiled them locally. Models are read-only from350's previously validated385procedure; model hashes are inmanifest.json. Each case uses3000×10,000 IC proposals, up to300 distinct normalized outputrings, then8×30,000 generic MASC proposals for **every** retained ring. Selection is solely frozen Slovak quadgram score. Only its top-language seed gets8×100,000 joint proposals. Budgets/RNG/objective match the original procedure; no true-key or plaintext-based seed selection. Independent re-encryption and inverse checks cover every MASC and final candidate.

Four controls independently choose random mixed rings and different held-out text windows outside the training80% and outside the original385control window. Both planted signs are tested via proven reflection, with the correct supplied phase. These are not known-ring inversions.

| Length/sign | Exact letters | Exact whole plaintext | Key diagnostic |
|---|---:|---|---|
|365/+|30/365|No|Output8/26 positions up rotation|
|365/−|338/365|No|Output26/26; inputX→M→Z→X|
|355/+|337/355|No|Output26/26; inputX↔Q|
|355/−|95/355|No|Output21/26|

All four true outputrings have stronger projectedIC than10,000random permutations, yet optimized retainedIC values exceed the trueIC through sampling overfit. Two controls fail the basin search; two recover the complete outputring but the language objective prefers wrong global letter assignments:365/− wrong385.66 vs true328.75;355/+ wrong728.38 vs true710.93. Plaintext lettersX/Q include sentence/name markers under the stated corpus preparation; no truth-based relabeling is allowed. `control-diagnostics.json` separates key/closeness diagnostics from operative selection. No unique full-key claim is made, especially for unused input letters.

## Completed34 target scouts

All17phases for each crop ran once under positive steps;34complete scouts,10,200 retainedIC candidates with genericMASC,34top-language joint refinements. Best365candidate isphase2, score−352.805; best355isphase2, score−357.934. Complete top outputs are incoherent and do not support plaintext, key, or a header/trailer interpretation. Each final candidate exactly reproduces its cropped ciphertext, but arbitrary key-fit checks alone cannot establish linguistic correctness or explain omitted framing. Results include every final candidate and all ranked MASC candidates; summary4.json gives exact counts/timings.

These are bounded heuristic failures, **not mathematical exclusions** of either crop, original17step Kryha, or a broader machine family. The four independent literal-exact control failures particularly prevent promoting the target null result into an exclusion. No identical restarts were added, no source corrections made, no DONE/reviewer/watcher started.

## Fivegram continuation

At the parent's request, separate pure5gram generic MASC ranking/joint refinement uses the existing frozen350 Slovak5gram table, its raw log-count values and default−5floor. Search budgets/RNG remain fixed. It reuses the two relevant IC lists, avoiding identical IC restarts. This follows the standalone5gram structure of351's German control fix; a preliminary4+.3×5 score diagnostic is retained separately and was **not** used as this test's objective. A distinct single held-out sentence beyond the four original control windows provides an additional blind validation. Results are inresults5.jsonl; no target5gram claim is authorized merely by near-exact calibration.

Reproduce scouts: `python3 batches/kryha-framing-sol61/run.py` (resumes completed records/files).
Reproduce5gram calibration: `python3 batches/kryha-framing-sol61/run5.py` (resumes separately; binaries supplied alongside sources).

### Completed5gram calibration and exploratory extension

Full standalone5gram MASC reranking of all retained IC candidates followed by top-seed5gram joint refinement fails both earlier near-exact calibration cases:365/−66/365letters and355/+43/355. The separate longest complete held-out sentence afteroffset350 is139letters; its independent blind mixed-ring control also fails23/139. An initial request for a355-letter single sentence found none in that reserved pool; the runner records the complete139-letter sentence, not a concatenation mislabelled as a sentence. Failed attempts are retained honestly.

A different generic sequence—take the already operative4gram final language winner, then apply standalone5gram joint refinement—**recovers365/−exact365/365** in0.793s, with complete independent ciphertext reproduction and inverse. The fixed4gram winner was selected without truth. This repairs itsX/M/Z cycle.355/+remains337/355 because the frozen5gram objective still prefers the wrongX/Q swap. These are real scoring and basin limitations, not source glyph corrections. Results: results5-from4.json. No key uniqueness is claimed.

The parent authorized an exploratory extension of that post4→5sequence to all34 already selected target winners. Each gets8×100,000pure5 joint proposals once; IC and MASC are not repeated, original outputs preserved, no manual letter corrections or truth-selected seeds. All34complete. Best365isphase6, pure5score−1335.83; best355isphase8,−1316.65. Complete outputs remain incoherent. Every candidate exactly re-encrypts/inverts its entire declared crop; independent Python5gram evaluation confirms every reported C++score (`target-score5-independent-verification.json`). summary5-targets.json and target-postrefine5.jsonl retain every phase and key.

One repaired365control supports this exploratory improvement only; failed355and139controls prevent any claim of general robust recovery. No actual historical plaintext, key, or framing interpretation was recovered. All own processes completed. All final marker snapshots350/351/334remain empty; no source or marker writes.

Reproduce post4→5target extension: `python3 batches/kryha-framing-sol61/postrefine5_targets.py` (resumes completed records).
