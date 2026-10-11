# Boolean exact-cover cryptanalytic model — GPT-6.1 Sol

Work confined to this batch directory. HCP364 source/working files only read; no markers, browser, source modifications, or published target solutions. All target plaintext constraints are **conditional cover-quote hypotheses**, never recovered plaintext.

## Model and control verification

Instead of symbolic arrays/variable offsets, every stage chooses Boolean `(plaintext column, ciphertext chunk start)` assignments. Each column chooses one chunk start; every output position belongs to exactly one chosen chunk. A chosen chunk copies fixed-index character cells from its column. Complete exact occupancy forces a valid nonoverlapping concatenation of all columns, including irregular lengths. Redundant character-count constraints preserve the plaintext inventory at intermediate stages. `exact_cover.py` supports an unknown plaintext filler and bounded ciphertext substitutions.

When SAT, extracted readout permutations must independently re-encrypt the inferred fixed/template plaintext and independently invert it exactly. Original planted keys need not be unique; an alternative key with identical complete ciphertext is a valid recovery of a witness, not proof of unique historical keys.

Independent65-letter known-plaintext double16/17 controls solve in about0.09–0.76s versus the parent's earlier array-based15.8s control. A three-error control with unknown last filler recovered the original two keys, fillerR and exactly error positions5,21,44 in0.248s. Its re-encrypted ciphertext is exactly the **undamaged** control, differing from the intentionally damaged input in precisely those3positions. Files disclose complete control plaintext, ciphertext and planted keys.

## Important inventory pruning

For HCP364 raw omit3, the64-letter quote has deficitsN,E,V against65cipher letters; excess letters areR,C,M,U. With an unknown65th filler and at most3substitutions, all3errors are already required to supply N,E,V. Therefore the filler must consume one ofR/C/M/U; every changed position must replace one ofR/C/M/U by N/E/V. All other source letters must remain fixed. This is a necessary consequence of inventories and the saturated error budget, not a guess at glyph readings. It turns raw double16/17 from20s timeout into0.64s UNSAT. The separate error-control recovery validates this restricted encoding on a planted damaged message.

All14 possible indicator omissions were inventory-prechecked; only raw omit3 is feasible at<=3substitutions for this **specific64-letter quote + arbitrary filler**. This says nothing about a different quote formulation, punctuation/padding, other damage models, or plaintext.

## Complete double width16–22 sweep

`double-sweep-tight.jsonl` contains147records:49ordered widthpairs, each with a separate independently seeded known-plaintext control followed by two conditional target tests. All49controlsSAT and re-encrypt exactly;46returned the exact planted keypair,3returned alternative valid pairs. Control solver time58.05s total.

All49raw omit3 tests with<=3substitutions and all49tests of the parent's explicit glyph variant(tsnnd,eloen,ercuv) with0substitutions are UNSAT. Target solver time59.30s total; maximum5.76s. Every case has unknown last filler. This rigorously excludes **only these stated plaintext constraints in the two-stage standard columnar model and those widthpairs/readings/errorbounds**. It does not exclude tripleR/XQ or establish what the ciphertext says. Summary in double-summary.json; prechecks/template in target-cases.json.

Reproduce: `python3 batches/constraint-sol61/error_control.py` and `python3 batches/constraint-sol61/sweep_double_tight.py`, with z3-solver available at the explicitly inserted/private/tmp/hcsolve-z3. The sweep appends JSONL; use a new output file for a clean rerun. `double-sweep.jsonl` records a superseded, interrupted slower run before tight pruning and is NOT the completed sweep.

## Triple controls and alignment

A regular65-letter13/13/13 quote control recovers all three original independently planted keys in3.68s. Arbitrary65-letter16/17/18 and a separate280-letter16/17/18 control both timeout20s. A timeout gives no exclusion.

HistoricalR alignment can impose readout-key[n−1]=0 for each stage, or n,n+1,n+2. The model supports this using chunk path-rank labels; equal-width16/16/16 with n11 independently recovers all three planted keys, exact re-encryption and inverse in2.84s. Known-key checks for unequal aligned stages pass but are explicitly **not key recovery**. Unequal aligned16/17/18 controls n11 and11/12/13 still timeout20s under generic solver. A separate eager simplify/card2bv/bit-blast/sat backend is being tested with60s bounds. Alignment number11 is not established by HCP364's header; any target test remains conditional.

Completed gated equal16/16/16 n11 target tests: rawomit3<=3errors UNSAT7.15s; explicitglyphvariant0errors UNSAT0.543s. Eager backend recovers the unequal aligned16/17/18 n11 control with all three original keys in59.38s at a60s cap; its corresponding conditional target tests are running. These results are about fixed templates and alignment assumptions, not a recovered message.

Final equal16/16/16 alignment sweep covers n1..16, identical n in all three stages. Every alignment has an independent planted65-letter positive control; all16 recover valid three-stage keys with exact full re-encryption. Both conditional target readings were tested at every n: **32/32 UNSAT** (rawomit3<=3substitutions and explicitglyphvariantomit3 exact0substitutions, each with unknown last filler). n11 is in its separate report; other15 alignments are in aligned-equal-sweep.jsonl. This excludes only the fixed quote/template and model for these equal widths; unequal widths, incrementing alignment, other preprocessing and other plaintext remain open.

Eager unequal16/17/18 n11 corresponding glyph0error and raw<=3error target cases both timeout60s (aligned-eager-target-results.json), so no exclusion follows. Its incrementing11/12/13 control also timeout60s and no target was run for that unvalidated branch. Equal-width and double results are substantial exact conditional constraints, not a solution or family identification.

Additional same-family damage control: aligned16/16/16 n11 with unknown filler and3intentional substitutions recovers all3original keys, fillerR and the exact intended error positions0,2,3 in4.86s. Its predicted ciphertext exactly equals the undamaged control and independently inverts to the full true plaintext (aligned-equal-error-control.json). `re_encryption_exact:false` refers solely to equality against the intentionally damaged input; `undamaged_re_encryption_exact:true` states the successful control reconstruction unambiguously.

## Larger equal-width control gates

Independent quote+r65 controls at equal triple widths17,18,19,20,21,22 with each stage's column0 at readout rank11 all returned UNKNOWN at20s generic and60s eager caps (`equal17-22-n11.jsonl`). No target tests followed these failed control gates. These failures do not exclude the widths or historical systems. Native cardinality SAT, unique-letter position anchors, and explicit intermediate vocabulary strengthening likewise failed their matched17/21 controls at60s.

A separate rank-prefix assignment encoding (`rank_prefix.py`) models each column/readout-rank bijection and the number of long or short columns before each rank, rather than exact output occupancy. Known-key checks at17–22 pass but are encoding consistency checks only. Recovery benchmarks are in `rank-prefix-control-results.jsonl`; a timeout remains a control failure.

The previously passed unequal16/17/18 rank11 eager control justifies a sustained600s target test per reading, recorded in `sustained-unequal.jsonl` and `sustained-state.json`. Each uses the fixed64-letter conditional quote plus unknown final filler and omission3. Neither the quoted plaintext, indicator position, nor rank11 is established historically. SAT witnesses must re-encrypt/invert exactly within the declared error bound; a second complete keyset is sought by blocking the first witness. UNKNOWN remains no exclusion.

The passed unrestricted13/13/13 control also gates an alignment-free target branch: explicit glyph reading UNSAT6.00s and raw<=3 UNSAT22.07s, each with unknown final filler (`regular13-targets.jsonl`). This is a complete narrow exclusion without an assumed rank11. Deterministic CHB SAT branching on the matched17 control also times out60s; all six alternative rank-prefix17–22 control recoveries time out60s. Neither failed-control benchmark is a target exclusion.

## Revised exploratory policy

Blind planted-key recovery timeouts do not invalidate an exact encoding whose independent known-key encryption/constraint checks pass. The earlier conservative gates were an effort-allocation policy, not a prerequisite for interpreting exact SAT/UNSAT. Exploratory equal17–22 rank11 target cases now proceed despite blind-control UNKNOWN, each with its own known-key encoding check and 60s target bound (`exploratory-equal-targets.jsonl`). An UNSAT is conditional on the verified encoding and stated template/readings, not a general historical-family exclusion. SAT still requires independent complete re-encryption/inverse and a blocked-first-keyset second-witness attempt.

Additional unrestricted equal11 control recovers valid keys in6.83s, followed by glyph0 UNSAT8.98s and raw<=3 UNKNOWN60s. Unrestricted equal12,14,15 control recoveries all time out60s (`lower-width-sweep.jsonl`); these control failures establish no target exclusions.

## Completed sustained and exploratory targets

The unequal16/17/18 n11 preserved eager configuration returned UNKNOWN after600.021s for the explicit glyph reading and600.032s for raw<=3 (`sustained-unequal.jsonl`). Both runs complete, no SAT witness, no exclusion.

All12 exploratory equal-width17–22 n11 target cases returned UNKNOWN at60s each (`exploratory-equal-targets.jsonl`); all6 independent planted-known-key encoding checks pass with exact re-encryption and inverse. They are explicitly not blind key recovery. Total target/check solver time721.43s. No plaintext/key witness emerged and no width/reading exclusion follows.

The useful new exact restrictions in this continuation are alignment-free triple13^3 UNSAT for both fixed-template readings and triple11^3 UNSAT for the glyph reading. Triple11 raw remains UNKNOWN60s. Wider equal and unequal target branches remain unresolved. These statements concern the specified64-letter quote+arbitrary final filler, omission3, standard repeated columnar transposition, and declared damage bounds. They establish neither that the quote is right nor that the historical cipher belongs to this system. No source or state markers were modified by this continuation.

## Completed unaligned equal2–10,12,14,15 extension

`small-width-sweep.jsonl` contains24 conditional targets:17UNSAT and7UNKNOWN. Both readings at widths2–9 are UNSAT; width10 glyph0 is UNSAT20.95s, while raw<=3 is UNKNOWN60s. Both readings at12/14/15 are UNKNOWN60s. All9 newly independent blind controls2–10 are SAT with complete re-encryption and inverse; all12 known-key encoding checks pass. Prior12/14/15 blind-control UNKNOWN records are explicitly reused, without rerunning identical failed searches. Total target solver time448.66s. Summary: small-width-summary.json.

An independent solver-free exhaustive audit of all ordered triple keysets at widths2,3,4 agrees with all6 UNSAT results (`enumerate_small_audit.py`, enumerate-small-audit.json;8,216,13,824 keysets per reading). These smaller widths extend a generic model and are not a historical R16–22 identification. The quote remains only a hypothesis. This extension found no targetSAT and therefore no candidate plaintext, key, or second witness. No source or markers were changed.
