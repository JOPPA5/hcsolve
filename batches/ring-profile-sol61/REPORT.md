# Frozen TRAIN profile objective for known17 mixed-ring search

The proposed profile metric fixes a real ranking defect, and a genuinely changed search recovered one of two fresh independent controls. It does not solve HCP350 or establish its framing.

For output-ring permutation O and known displacement d_i, projected counts are n_t = count(O[c_i]-d_i=t mod26). Unknown input-letter assignment is a permutation of these 26 counts. Rearrangement gives its exact maximum unigram log likelihood: L = sum sorted(n)*sorted(log p_TRAIN). The frozen model is `ciphers/hcp-350/work/ring-unigrams.tsv`; no control/test count is a scoring target. The profile multinomial objective adds log(N!)-sum log(n!), which penalizes concentration inconsistent with TRAIN. The optimizer drops only constant log(N!).

`diagnose.py` compares saved IC candidate lists with independently known true rings, adding truth only after ranking. All five old controls put true above every retained IC false ring under multinomial profile and negative KL; concentration puts true last (rank252 for original385, rank301 for each355/365 control). Raw rearrangement LL alone gives ranks2,1,1,1,8. This is objective diagnosis, not recovery.

`ring_profile.cpp` changes the search objective, freezes 3000 random restarts ×10000 output-ring swap proposals, keeps300 candidates, and uses temperature .02+2*(1-(iteration mod2000)/2000). It retains the known17 schedule and supplied correct phase. All candidates then receive the unchanged TRAIN4gram MASC8×30000 search; only the highest language winner seeds joint8×100000 refinement. No truth-based selection. Two fresh windows are from held-out sentence offsets500 and650, independent random mixed rings, lengths385/+phase7 and365/−phase12. Negative orientation is represented by the exact reflected positive-ring equivalence established earlier.

| Fresh control | Fourgram final plaintext | Final output key | Pure5 post-refinement |
|---|---:|---:|---:|
| 385, positive | **385/385 exact** | **26/26**, up rotation | **385/385 exact** |
| 365, negative/reflected | 42/365, failed | 4/26 | 25/365, failed |

The successful input key matches24/26: G/W are exchanged and both are absent from the control. Every observed plaintext mapping is exact; a complete input alphabet is not identified. Independent full-text inverse and reencryption passed for every MASC candidate and final key, but those algebraic checks alone do not validate language. The385 plaintext equals the independently planted complete held-out text. Execution22.99s and28.88s respectively. Pure5 refinement uses the same frozen TRAIN5gram model and each unchanged operative4gram winner; it is not used to select between outputs.

Both fresh profile searches found spurious keys with better profile likelihood than truth (true rank301/301; max retained output-key overlap16/26 and13/26). Thus the metric itself can be overoptimized. Its value here is steering the output-ring search into a basin from which generic language refinement recovered385. It does not make the finite-sample TRAIN histogram uniquely identify a ring.

Reproduction: `python3 batches/ring-profile-sol61/diagnose.py` and `python3 batches/ring-profile-sol61/run.py`; the latter resumes preserved results. Compile source with clang++ -O3 -std=c++17 before a fresh run. `refine5.py` performs generic post-refinement. Read-only prior-batch MASC/joint binaries and frozen corpus models are documented in run.py. `manifest.json` freezes model hash and search settings; `fresh-diagnostic.json`, results.jsonl and results5-from4.json preserve results, keys, planted data, timings and verification. An initial parser failure (old MASC accepted integer IC score) was fixed in the batch-only double-score parser; no search output was changed.

Concrete next test: parent may run this changed objective on the explicit full385 target/all17 phases and the same declared crops, then generic language refinement under this fixed pipeline. One successful matching-length control supports an exploratory run; the failed365 control forbids treating a target failure as cipher/framing exclusion. No target search was run in this investigation. No source cipher directory, marker, or prior batch file was written; scans for350/351/334 markers remained empty.
