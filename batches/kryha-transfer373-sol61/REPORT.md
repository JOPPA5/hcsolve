# HCP-373: conditional transfer of the 350/351 mixed alphabets

No coherent decode was obtained under the tested transferred-ring configurations. Eight fresh 650-letter controls recover their complete texts, masks, physical starts and relative offsets exactly at rank 1; every actual full-message result is incoherent. This is validation of the bounded attack, not exclusion of Kryha or proof that the historical keys were shared.

## Published context and source boundary

HCP-373 is already publicly **Solved**. Main read all three rendered portal tabs and downloaded its cryptogram and published plaintext into `batches/solved-context-main/373/`; SOURCES.md discloses this prior publication. Message 80172, 17 May 1944, Országh to Legación Eslovaquia Madrid, discusses cellulose export/cancellation and prices. HCP-374 requests repetition of the final15 groups of message80172. This task seeks procedure/key evidence, not a claim of new plaintext recovery. No `ciphers/hcp-373` directory or marker was created.

The full provisional 650-letter transcription, snapshotted when it first became available, comes from `batches/kryha373-collation-sol61/ciphertext650.txt` and is snapshotted as target650.txt. Its ambiguous glyphs were still being independently collated (including ELDN[A/E], XX[A/E]ZT, HVAJ[A/E], CDFBS); it is not called pixel-certified. All 130 groups including initial KIDAH and the final15 groups are included. No partial target, group omission, reversal, letter filling or correction chosen by prose was used. The collation changed while these runs were in progress; the tested snapshot is retained unchanged, and later glyph changes are listed in source-provenance.json. These results must not be relabelled as tests of that later transcription. Source image, published-plaintext image, transcription and model hashes are retained in provenance.json. The published plaintext is disclosed but was never supplied to the transfer optimizer.

## Model and structural beam

P[slot] and O[cipher letter] are frozen from the 350/351 key in transferred-key.json, source SHA `1aada6a71c7e43d5e11e9680472536f4fccd16a754d8f9cfca728a2f2b788e97`. Sharing these alphabets with a later, opposite-direction Madrid communication is only a hypothesis. Their rare-letter labels and internal I/J convention remain uncertain.

The actual 52-hole wheel uses the verified adjacent distances summing to179. Each chosen mask makes exactly one clockwise revolution over selected holes; after m ordinary presses displacement advances179 (23 modulo26). All52 starting holes and26 relative ring offsets are tried. Within each start/offset, an ordered-hole language beam retains128 paths, scoring frozen TRAIN-only 2/3/4/5 grams within ordinal rows and adding complete boundary grams before final pruning. The code was upgraded to 768-character states,40 ordinal-row slots and normalized modular arithmetic; the old85-letter small arrays/offset constants are not reused unsafely at650.

The declared preparation-aware scorer maps raw J to TRAIN's X. Fresh control preparation replaces natural-word J by I and sentence X by J; this is an explicit conditional convention inspired by the 350/351 candidate, **not** an established historical rule. Every raw target letter and key remains unchanged in saved outputs. No selective-J extra press is assumed.

## Fresh controls and actual scope

Two independent genuine 650-letter TEST segments at offsets61000 and63000, with new random23-hole masks, starts and initial displacements, both recover exactly. The optimizer receives only ciphertext and the known-ring declaration; it does not read the planted mask or plaintext. Independent absolute-coordinate inversion and adjacent-wheel forward encoding verify the complete650 letters and keys.

Six further disjoint TEST650 segments at offsets65000,65700,66400,67100,67800,68500 calibrate:

- counts20,21,25 with original wheel roles and positive displacement;
- count23 with original roles and negative displacement;
- count23 with exchanged physical wheel roles, each displacement sign.

All six recover all650 letters and their exact masks/offsets at rank1. Exchanging roles makes the decode input layout `O inverse` and ciphertext-position map `P inverse`; changing sign negates every real physical-wheel distance. This models communication direction explicitly rather than reversing ciphertext order. Controls use separate random seeds and genuine held-out text; TEST and targets are absent from training.

Only after exact matched control success was each configuration run on the complete preferred650-letter ciphertext. Best actual scores are:

| Count | Roles | Sign | Best frozen score |
|---|---|---|---:|
|23|original|+|−2803.01|
|20|original|+|−2787.02|
|21|original|+|−2789.97|
|25|original|+|−2769.13|
|23|original|−|−2560.63|
|23|exchanged|+|−2763.61|
|23|exchanged|−|−2754.22|

None is a coherent whole message or a supported partial decipherment. Each run keeps1352 winning start/offset paths and saves the top20 full keys and raw650-letter outputs. All140 retained initial-variant actual keys re-encrypt the entire650-letter transcription exactly; this proves mechanical consistency only. The beam is finite, and supplied-ring control success does not establish historical ring transfer or completeness.

## Reproducibility and limits

From the repository root:

```
batches/kryha-transfer373-sol61/reproduce.sh
```

Relevant evidence: control-verification.json, controls.json, experiments-results.json (all additional controls and target keys), original-target-keys.json, all raw beam outputs, source-provenance.json and provenance.json. Source and cipher directories remain unchanged.

Unknown alphabets against the published plaintext are being investigated independently by another agent. This batch does not duplicate that work. Other stop counts, ring arrangements, prefix handling, preparation, stepping rules or cipher systems remain open; these negative results cannot be promoted to machine-family exclusion.

## Later source collation: independently retained full variant

The collation changed while the initial runs were in progress: positions233 E→A,268 A→E,270 A→E (one-based). The original tested snapshot is not overwritten. A final bounded rerun of exactly the same seven already-calibrated configurations uses target650-latest.txt, containing all three source-led corrections. Both650-letter source versions and their SHA hashes are retained. No additional model, count or search budget was introduced.

Every later-variant result remains incoherent. Best scores in the table order above are −2796.98,−2796.07,−2791.39,−2798.48,−2568.92,−2762.30,−-2755.81. The additional140 retained top20 keys all independently re-encrypt the complete corrected650-letter snapshot, for280 verified actual candidate keys across both variants. See latest-variant-results.json and separate raw outputs. Reproduction uses the frozen latest snapshot rather than silently importing a later change to the collation.
