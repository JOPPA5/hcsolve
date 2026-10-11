# Exact two-mask path and input-ring refinement

Writes are confined to this batch. Source ciphers and the enumeration worker's files are read-only. No markers/watchers/reviewer are used.

`audit.py` builds frozen six- and seven-gram logcounts from the first 80% of TRAIN using the existing Q-proper-name/X-sentence preparation. It ranks all generic one-swap neighbors before reading control truth. `full_check.py` independently audits complete control messages and adjacent-wheel re-encryption. The original 2..5 score prefers the wrong Q/X assignment; pure6 and pure7 select the exact candidate. These separate metrics were investigated after observing a control discrepancy, not preregistered or independently validated on a second fresh control.

`build_path.py` copies the enumeration worker's exact admissible physical-path DFS into `path-refine.cpp`, replacing the profile objective with per-message frozen n-gram scoring for a supplied blind language-selected input ring. Every path respects the supplied displacement differences, ordered physical holes and one circumference of 179. The alphabet remains 26 letters, physical mask size 23. All 52×52 initial anchors and all feasible paths are visited. The two message projections use separate cumulative physical distances and subtract K[0] for B; no pooled histogram is used.

`run_path.py INPUT_JSON P_FILE LABEL N` supplies the known-output-ring conditional model, exact delta and a blind input-ring seed. `project_paths.py` projects its retained top100 paths. `rerank.cpp` evaluates identity and all325 input-ring swaps at every retained path, separately under pure6 and pure7. `alternate.py` alternates exhaustive fixed-ring path search and generic one-swap ring search, stopping on no strict score improvement or ten rounds. No known plaintext or true mask/ring seeds are supplied to those programs.

`check_paths.py` reconstructs each complete input message from the selected path and ring. B's mask is rotated back one stop, with relative initial offset beta=K[0]−previous-to-first arc modulo26 explicitly retained. It checks the full delta sequence and re-encrypts via independently summed adjacent-wheel arcs. Those checks establish a mechanically consistent key, not that target plaintext is correct.

The existing original profile pooling was later found to subtract K[0] where pooled A-aligned B histograms require K[j]. Its top100 starting seeds are disclosed as originating from a mismatched heuristic. Our per-mask projection and exhaustive fixed-P language search are unaffected. Original results remain preserved.

## Signed whole-message extension

`build_full.py` preserves every physical path but scores all385 positions using t=i−20−side (A origin full20, shifted B origin full21). Negative positions use mathematical floor division and residue0..22. `run_full.py`, `project_full.py`, `check_full_paths.py` and `alternate_full.py` decode/re-encrypt the entire385 strings without assuming omitted groups were unencrypted. B relative offset beta remains explicit. A fresh TEST offset44000/random seed2335035112 control passes blind whole385+385 recovery under pure6; pure7 does not pass and is not transferred independently.

`path-full-skip5.cpp` and `rerank-skip5.cpp` omit only language windows intersecting first5 letters; all385 symbols retain their original displacement and are fully decoded/re-encrypted. The same fresh control passes pure6 with all385 exact. This is an explicit first-group indicator alternative, not an assertion that an indicator exists. Actual source strong and strong-plus-moderate whole streams are kept separate.
