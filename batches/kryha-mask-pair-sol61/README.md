# Real 52-hole shared-mask pair search

Read REPORT.md first. The physical histogram-profile bridge succeeds on a fresh blind 385+385 held-out control; earlier initialization strategies fail. Actual target results are separate. Source cipher directories are read-only.

Reproduce: `sh batches/kryha-mask-pair-sol61/reproduce.sh` from the repository root. Existing stage outputs are resumed, not discarded. Optimizers never read `control.json`; verification alone reads planted truth. Parent independently audits the positive control.

For count m=26, ordinary positive rotation advances 179 ≡ 23 (mod26) per complete selected-stop cycle. Each message independently resets at the same physical selected hole. Define pooled per-ordinal-column histogram H[j,z] from z = O[c_i] − 23 floor(i/26), j=i mod26. A physically legal ordered mask determines d[j] by the actual hole coordinate relative to its first hole, including the one-revolution wrap. The projected input-position histogram is N[u] = sum_j H[j,u+d[j]]. Unknown input-ring letter assignment is removed for initialization by sorting counts and frozen TRAIN unigram log-probabilities. Score is sum_k sorted(N)[k] sorted(log p)[k] − log(sorted(N)[k]!). This objective drives physical mask selection independently of an input ring.

The previous cycle pair-collision score supplies only partial output rings; its optimized rank overfits. Every blind output candidate enters the physical profile search and paired MASC. Whole-language winners then couple the physical mask beam to input/output ring refinement, with all language windows remaining inside their original individual body. No selected plaintext words or true ring/mask seed enter any discovery stage.

No watcher, reviewer process, cipher marker, register entry or source change is authorized in this batch. The parent handles source notes/finalization.
