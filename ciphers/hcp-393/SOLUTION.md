# Unsolved — HC Portal 393
Solver: OpenAI GPT-6 Astra, 2026-10-11.

No key or plaintext has been recovered. Cipher type remains unknown; letter frequencies make transposition plausible. No message translation is available.

The preserved source is a scan of MZV message 80226/1944, dated 7 August 1944, sent by Polyak to the Slovak legation in Bern. Portal status is Not solved. The supplied archival title says the subject concerns carrying out an instruction under 80216 and taking away a passport. This is context, not a claimed decipherment.

There was no attached transcription or solution. I manually transcribed the image into work/transcription.txt; uncertain characters are documented in NOTES.md. The working text has 100 letters, IC 0.0573737, preceded by 3100. Numeric prefix role is unknown.

## Reproduction
From the repository root:

```sh
sh ciphers/hcp-393/work/reproduce.sh
```

This trains Slovak fourgram scores from the preserved downloaded corpus, compiles a deterministic-seed annealing attack, and prints the strongest found irregular single-columnar candidate for widths 2–30 for original and reversed ciphertext. It reproduces **attempts, not plaintext**. It requires Python3 and a C++17 compiler. It reads the manual working transcription; no automatic image-to-plaintext command exists.

No candidate provides coherent full-message coverage. The search is heuristic and does not exclude the tested family. Ambiguous transcription, short length, other widths and multiple-stage transpositions remain unresolved. No DONE, FINAL or register entry is warranted.

A further finite geometric route test recovered its full100-letter independent control as the best candidate, but found no coherent target among637006 fill/read-route cases, including all possible5-letter omissions. Reproduce with `python3 ciphers/hcp-393/work/routes.py`. Arbitrary keyed and multiple transpositions remain open.

### Controlled 10 × 10 double-transposition scout (2026-10-11)

Still unresolved. An exact width-ten column-order search and exact row-order searches for 64 retained column candidates recover two independently planted 100-letter diplomatic controls completely. However, a real 100-letter Slovak sentence from independent UD TEST is ranked incorrectly under both the base and longer-phrase scorers, even though its column key is exact. A 50,000-candidate reranking includes truth at rank 1,440; this exposes scoring ambiguity rather than proving a different cipher.

Full literal 100-letter target scouts provide no coherent plaintext. They do not establish a key or exclude double columnar transposition. Source remains unchanged; `3100` and damaged glyphs remain uncertain. Evidence and executable reproduction: `work/square10/README.md` and `validation.json`. No full plaintext or translation is claimed.

The transposed 10 × 10 orientation was also scouted to cover the equal-width-ten odd-pass/triple structure. A three-key independently encrypted control passes exact recovery and reencryption; the actual transposed input still has no coherent candidate. This remains a bounded negative with the same pruning and scoring limitations.
