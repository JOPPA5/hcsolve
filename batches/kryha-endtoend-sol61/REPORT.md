# Cipher-only end-to-end Kryha paired control

This bounded validation concerns a declared model, not a new decipherment of 350/351. Both cipher directories are untouched. Earlier paired language controls supplied the true output ring and residue differences; their positive results did not independently validate ciphertext-only cycle discovery. This batch removes those truth inputs.

## Declared family and blind inputs

Two independent fresh 385-letter paired controls use random mixed input/output rings, 23 selected stops on the primary 52-hole/179-unit wheel, and masks differing at one neighboring stop. The streams share the shifted relation A[i] = B[i+1] over 384 letters. Both encoders reset displacement zero. The solver is supplied only both ciphertexts, selected count 23, wheel geometry, the shift +1 relation, and frozen TRAIN statistics. Neither the one-stop difference constraint nor reset beta zero is supplied to the physical search. TEST segments at offsets 52000 and 54000 exclude prepared TRAIN sentence identities. Text preparation is the existing generic corpus preparation, not an asserted historical convention.

Generation uses independent random seeds 6173523111 and 6173523222. Separate `*-truth.json` files are inaccessible by convention to all search scripts. Only the audit loads truth, after final blind rankings are saved.

## Composition and provenance

1. `ransac.py` derives the common output-ring cycle and 23 residue powers from ciphertext only, using independent rank-48 GF(2)/GF(13) bases and bijective CRT solutions. All 12 unit gauges are retained. It receives no planted ring.
2. `fit_dp` receives each ciphertext-derived delta[j] = K[j+1] − K[j] and primary wheel geometry. All 52² anchor pairs are tested, allowing two distinct masks. No true mask, start or ring gauge is selected.
3. `enumerate-profile -1` enumerates all feasible physical paths. `-1` disables the old beta-zero constraint. The pooled histogram subtracts K[j] from shifted B, not K[0]. The generic frequency profile retains 100 seeds per feasible gauge.
4. `masc` uses four independent generic input-ring starts per retained path, frozen 2–5-gram scores, and no true input ring. `rerank` evaluates identity and all 325 input swaps under frozen pure 6- and 7-gram models separately.
5. `path-full` enumerates all physical paths under the current language-selected input ring, followed by all input swaps. Up to 10 strictly improving pure-6 rounds are permitted for every feasible gauge. Pure-7 rankings are retained independently throughout; scores of different n are never compared.
6. `save_ranked.py` freezes the strongest candidate within each n/gauge. `audit.py` then loads the quarantined truth and independently walks adjacent physical holes to decode and reencrypt each full 385-letter message.

Full-message origin is zero. B is evaluated with t = i − 1, including its previously unpaired first letter. The inferred relative offset is beta = K[0] − B's closing arc. No cropped-body or prefix omission is used. Physical B path is rotated back by one stop for full-message verification.

## Pilot result

RANSAC recovered 384/384 relations, with all 12 equivalent unit gauges. Ten were physically infeasible; two admitted 372 paths each. All 744 paths were enumerated. The pure-7 ranking selects the correct gauge and both exact original masks, reconstructing **385/385 letters in both messages**. Its output ring differs only by a +11 positional rotation; 24/26 input labels match under that gauge. The observed alphabet has 24 letters. The remaining two letters do not occur in these plaintexts, so exact reconstruction does not establish their ordering.

Pure-6 selects the same correct physical masks and output ring, but recovers only **371/385 letters in each message**, with 21/26 input slots equivalent. This is a retained failure of that language objective, not an end-to-end exact pass. The reverse unit gauge produces noise and ranks below the correct gauge under either objective. Every retained final candidate mechanically reencryption-checks both full messages; this check alone does not establish its plaintext.

## Second result

The second control recovered 384/384 relations. Ten gauges were infeasible; two had 1,272 paths each, all enumerated. Its pure-6 rank 0 recovers **385/385 letters twice**, both original masks and all **26/26 input labels**, with the output ring equivalent by a +24 rotation. Pure-7 rank 0 selects the same masks/output ring but only **353/385 and 352/385 letters**, with 24/26 input labels equivalent. Both literal outputs and failures are preserved in `second-blind-ranked.json` and `second-independent-audit.json`.

These are positive whole-chain candidate-recovery controls: each exact whole plaintext is present among the two predeclared objective winners, with no truth selected between stages. They are **not** a positive calibration of one universally selected language objective: pure-6 fails the first and pure-7 fails the second. A fully automatic single-winner pipeline remains unvalidated. No combined score or post-hoc choice was tuned to make both pass. Each objective ranks gauges internally; n=6 and n=7 scores are never compared. `rank_within_ngram` in the audits records this separately; the JSON list index across groups is not a shared rank.

## Reproduction and limits

See `reproduce.sh`. `pilot-blind-ranked.json` and `pilot-independent-audit.json` preserve the saved blind outputs and post-ranking truth comparison. Rankings are separate for n=6 and n=7. The scripts perform no target cipher writes, marker changes, watcher or reviewer starts.

The control is clean and satisfies the supplied shift hypothesis. It does not validate finding that hypothesis without a lead, robustness to transmission/source errors, unknown selected count, nonshared rings, selective extra presses, or rare alphabet assignments unsupported by observed letters. The frequency shortlist truncates initial language seeds, although subsequent fixed-input search enumerates all physical paths. No family exclusion or uniqueness claim follows.

Code credit: cycle recovery from `batches/kryha-shift23-sol61`; physical DP from `batches/kryha-two-mask-main`; profile/MASC from `batches/kryha-two-mask-reset-sol61`; pure6/7 ranking and full-path refinement from `batches/kryha-two-mask-refine-sol61`. Adaptations here allow arbitrary beta and replace old crop origin 20 by full origin zero. No model is trained on either TEST plaintext.

Implementation note: an initial pilot JSON serialization encountered a circular history reference after the completed searches. The history was detached and final rankings were reconstructed directly from already saved outputs without rerunning the searches. This did not expose truth or change ranking.
