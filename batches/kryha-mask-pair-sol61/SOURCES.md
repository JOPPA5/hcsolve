# Sources and reusable implementation

No published target solution was consulted. All source cipher directories remain read-only.

- Physical geometry: `batches/kryha-wheel-sol61/wheel52.json`, independently transcribed and verified there from the primary NSA historical manual. Its 52 adjacent angular-distance values total 179; any 26 selected stops complete a cycle with displacement 23 modulo 26. This does not establish historical use for 350/351.
- Held-out controls: UD Slovak SNK TEST, `ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu`; every prepared sentence also present anywhere in UD TRAIN is excluded. Manifest records corpus SHA256 and fresh offsets 23500/25000. Preparation uses accent stripping, spoken digits, Q proper-name markers and X sentence separators. No TEST training or supplied plaintext word/key seed.
- Frozen scoring: TRAIN-only `batches/kryha-mask-sol61/model2.tsv`, `model3.tsv`; TRAIN-only `ciphers/hcp-350/work/ring-{4,5}grams.tsv` and `ring-unigrams.tsv`.
- Paired profile adapts `batches/kryha-mask-sol61/ring-calibration/profile.cpp`; pair MASC/joint use its fixed-mask ring objective. Physical ordered-hole beam adapts `batches/kryha-mask-sol61/maskbeam.cpp`. Pooled cycle objective adapts `batches/kryha-cycle-sol61/cycle.cpp`. Earlier failure records are unchanged.

The known count 26, shared rings, shared physical starting stop, reset per message, positive rotation and ordinary single press after every letter are explicit control assumptions. Selective J spacers break this ordinary-step model. None of these assumptions is asserted for actual cipher messages.
- Compensated-anchor refinement: read-only source credit to `batches/kryha-count-pair-sol61/pair-local-mask.cpp`, copied into this batch. It exhaustively scores selected/unselected hole exchanges and cyclic starts jointly with 325 input-ring swaps and 25 nonidentity input-ring rotations; eight strictly improving sweeps maximum. No source file in that active sibling batch is edited.
- Independent positive385control audit by root: `batches/kryha-pair-main-audit/verification.json`, absolute-coordinate physical encoder/inverter separate from this batch's walker.
- New355control: same UD TEST preparation and complete TRAIN-sentence exclusion, new fixed offsets32000/34000, independent random RNG52771355; full manifest and direct encoder/inverse preserved in `framing355-control/`.
