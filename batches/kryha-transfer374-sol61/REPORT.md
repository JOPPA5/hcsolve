# Conditional transfer of the 350/351 mixed alphabets to HCP-374

No coherent plaintext was recovered. This is a bounded, controlled test of a transferred-ring hypothesis, not evidence that the historical keys were shared and not an exclusion of Kryha.

The fixed P/O permutations are read from `ciphers/hcp-350/work/kryha-decipherment/key.json` (SHA in manifest.json). Their rare-symbol naming and word-internal I/J interpretation remain uncertain. The 52 physical-hole coordinates come from the verified wheel52.json; adjacent distances sum to 179. All presses in this branch are ordinary. No speculative extra J press was introduced.

The complete 85 ciphertext letters are used, forward, without deleting groups or filling unknowns. Source directories and markers were not changed. Eight variants independently represent each combination of group 2 CRTCS/CRTGS, group 5 SPQHO/SPQHQ, and group 12 TLIJY/TLIJV. A crop saved from the original source image supports the Q and V alternatives; the C/G reading overlaps the watermark and remains conditional. No reading was chosen to obtain a word.

## Algorithm and controls

A physical mask has m selected holes ordered clockwise, making exactly one traversal of the 52 holes. For every one of 52 starting holes and all 26 initial relative alphabet offsets, a beam chooses increasingly ordered physical holes. Each ordinal column projects its ciphertext letters through the fixed output ring, subtracts the real physical distance and 179 units per cycle, then uses the fixed input ring. Frozen TRAIN-only 2/3/4/5-gram scores accumulate within rows; the final complete 85-letter score includes row-boundary grams. The beam retains 128 paths per start/offset. This exploits physical ordering directly, rather than annealing arbitrary masks or scoring only frequency collisions. It is finite and incomplete.

Two fresh genuine prepared held-out TEST segments at offsets 45000 and 46000, with independent random 23-hole masks, physical starts and offsets, both recover all 85 letters and exact physical keys at rank 1. The optimizer receives only their ciphertext and the declared known rings. It does not read plaintexts or planted masks. Generic preparation and frozen model provenance are inherited from kryha-mask-sol61/prepare.py; neither TEST nor target was used in training. Whole planted controls and selected candidates pass an independently coded absolute-coordinate inverse and adjacent-wheel forward re-encryption.

Fresh 85-letter controls for all other counts 20–30 give exact rank-1 recovery for 20, 21 and 25. Counts 22,24,26,27,28,29,30 fail with 69,81,79,79,82,80,82 correct letters. The diagnostic compares planted score only after blind results: at 22,26–28,30 the false winner scores above the truth, while 24 and 29 lose a better truth during the finite beam. No target attacks were run for these failed counts. A separate v2 correction scores completed row-boundary grams before final beam truncation; it gives the same successes and failures, retained separately.

For the source-backed ambiguity in the transferred input-label names, a separately declared conditional preparation maps natural word J to I and sentence X to J. The scorer maps decoded J to TRAIN's X while preserving every literal output. This is not a proved historical convention. Two further genuine TEST85 controls at offsets 55000 and 56000, with new independent 23-hole masks/start/offset, both recover exactly at rank 1. Their generation and full inverse checks remain separate.

## Actual result and limits

All eight forward variants were tested at calibrated counts 20,21,23,25 under the ordinary frozen scorer. None produces a coherent whole message. The eight 23-stop variants were also tested under the independently calibrated preparation-aware scorer; none is coherent. Each run retains all 1352 best start/offset candidates and saves the top 20 complete keys and literal plaintexts. All 880 saved top-20 target candidates pass whole 85-letter re-encryption; that proves mechanical consistency only, not decipherment.

This does not exclude another mask omitted by the finite beam, other input/output alphabets, another stop count, a different preparation, press rule, or cipher system. The transferred rings may simply be from another daily key. No plaintext wording from the source description was supplied as a crib. Do not infer that a few accidental words such as `predal som` constitute a partial decipherment.

Reproduce from the repository root with:

```
batches/kryha-transfer374-sol61/reproduce.sh
```

Primary evidence: source-body-crop.jpg and source-variants.json; control-verification.json, count-controls.json, count-control-verification.json, count-controls-v2.json, control-j-verification.json, planted-control-verification.json; target-winners.json, target-count-winners.json, target-j-winners.json and per-run full keys. The report distinguishes calibration with supplied rings from actual unknown historical keys.

## Direction of communication: separate inverse-machine configurations

HCP-350/351 are outbound from Madrid, while HCP-374 is addressed to Madrid. This motivates a further *conditional* check of machine direction, without assuming either daily-key sharing or a historical inverse procedure. The physical input/output ring layouts are separately exchanged, and the displacement sign is separately reversed. With original input layout P and output positions O, the exchanged decoder has input layout `O inverse` and ciphertext positions `P inverse`; signs +1 and −1 multiply every real physical-wheel distance. Initial relative offset remains exhaustively 26-way. The ciphertext is never reversed.

Each of these four configurations received a new genuine TEST85 control at offsets 58000,58200,58400,58600, with independent new random masks/start/offset and the explicitly conditional J/I preparation described above. All four blindly recover all 85 letters at rank 1, and pass independent absolute-coordinate inversion and adjacent-wheel re-encryption. Only then was each configuration run at m23 on the complete G/Q/V preferred source variant, as requested. None yields a coherent message. Full control truth, blind candidates, keys, signs, texts and mechanical verification are retained in direction-results.json. This does not establish that any of those configurations was historically used.

The exact transferred key is now frozen in transferred-key.json, rather than reading a mutable future cipher key during reproduction. Its bytes match the original manifest SHA. No further expansion of this unsuccessful restricted transfer lead is justified by these results.
