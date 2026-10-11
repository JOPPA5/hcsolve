# Two distinct physical Kryha masks: feasibility control

This model attempts to realize observed cyclic displacement differences as the difference of two physical stop-arc sequences on the acquired 52-hole wheel. It does not recover plaintext or prove that this wheel was used.

The input wheel has adjacent distances 3 or 4 and circumference 179. Each candidate mask visits its selected holes in physical order through exactly one revolution. A returned pair is independently checked against these distances and the supplied differences modulo 26.

`python3 batches/kryha-two-mask-main/controls.py` runs two independently generated controls without supplying the masks to the solver. The five-stop control returns a valid pair in 0.49 s; it differs from the planted pair, demonstrating nonuniqueness. The matched 23-stop control returns UNKNOWN after 30 s. Consequently there is no demonstrated recovery power at the target size, and no negative target conclusion is justified. See `controls.json` for exact masks and results.

The relation used for a prospective target is ΔK[j] = arc351[j+1] − arc350[j] modulo 26, where K relates the common output cycle of 350[i] and 351[i+1]. Ciphertext body alignment, physical phase and ring coordinate gauge remain explicit assumptions. No actual pair of target masks has been recovered by this model.

## Exact dynamic programming replacement

The CP timeout was resolved by a different exact feasibility algorithm in `fit_dp.cpp`. For fixed initial holes a0, b0, the cumulative displacement difference fixes the residue `(coord(b) − coord(a) − coord(b0) + coord(a0)) mod 26` at every step. A candidate boundary pair can be reached exactly when a preceding reachable pair has both hole indices smaller. A two-dimensional prefix OR answers this existence query. Selected holes increase strictly and the last selected hole leaves room for completing exactly one physical revolution. All 52² initial-hole pairs are enumerated; each layer retains a witness predecessor.

Build with `clang++ -O3 -std=c++17 batches/kryha-two-mask-main/fit_dp.cpp -o batches/kryha-two-mask-main/fit_dp`, then run `python3 batches/kryha-two-mask-main/control_dp.py`. Four new independently random 23-stop controls all returned valid mask pairs in approximately 0.10 s each. Every returned arc sequence was independently recomputed and checked for circumference 179 and the full supplied difference sequence. Four five-stop controls also passed. Different planted and returned masks show that feasibility is not unique key recovery.

On all 12 unit-equivalent output-coordinate rows independently recovered in `batches/kryha-shift23-sol61/ransac-results.json`, only rows 5 and 6 admit physical two-mask realizations. Each has 15 feasible initial-hole pairs. The other ten have no realization under the exact wheel/relation assumptions. Results, initial witness masks and arc checks are in `dp-targets.json`. These are structural witnesses, not a plaintext solution. The algorithm currently retains one path per reachable state and one returned witness per coordinate row; it has not counted or enumerated all feasible paths. Both physical coordinate orientations and candidate-mask nonuniqueness remain relevant to language recovery.
