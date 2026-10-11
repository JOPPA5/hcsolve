# Coupled two-message Kryha pilot

This batch tests HCP350 and HCP351 jointly under the conditional old fixed 17-step, one-lever-press model. Both messages share the same unknown pair of mixed 26-letter rings and phase. Displacement and step index reset at the start of each message. They are never encoded as a continued 770-letter stream. Their natural plaintexts need not coincide. The possible adjacent chronology and shared key are unproved; the 1943/1944 programmable 52-stop hardware is outside this model.

The phase sequence is `[7,6,7,5,6,7,6,8,6,10,5,6,5,7,6,5,9]`. With input slots P and cipher-letter positions O, plaintext at position i is P[(O[c_i]−d_i) mod 26]. The encoder independently uses the inverse permutations. Every recorded candidate is reencrypted and inverted across both full messages independently. A common unknown starting ring displacement is absorbed into the unknown ring permutation; the reset assumption imposes the same start on both messages. Different starting offsets or phases are outside this paired pilot. Negative stepping is represented exactly by reflecting both arbitrary rings; running sign +1 includes that equivalent family.

## Search and scoring

`pair_profile.cpp` pools projected slot frequencies from the two individually reset histograms. It searches 3,000 output-ring restarts, each 10,000 proposals, using the frozen TRAIN sorted-unigram multinomial profile likelihood. The 300 retained candidates feed `pair_masc.cpp`: eight 30,000-proposal shared input-ring searches each. These are reranked only by frozen TRAIN fourgram score. The language winner seeds `pair_refine.cpp`, eight 100,000-proposal joint-ring searches. Finally `pair_refine5.cpp` starts from that unchanged operative fourgram winner and uses a standalone frozen TRAIN fivegram score, with eight 100,000-proposal joint searches. Truth is never a seed or selection criterion.

N-grams stop at each message boundary: 764 fourgram windows or 762 fivegram windows for two 385-letter texts. The pooled profile has 770 symbol observations, not cross-message n-grams. Read-only scoring files are `ciphers/hcp-350/work/ring-{unigrams,4grams,5grams}.tsv`; prepared controls come from the remaining 20% held-out portion of the Slovak UD source, after the frozen model's first-80% training boundary. The constructed decimal-spelling, PROPN Q delimiters and sentence X preparation is a control convention, not an established Slovak telegram procedure.

## Reproduction

Compile each corresponding C++ source with `clang++ -O3 -std=c++17 SOURCE -o BINARY`. Run `python3 batches/kryha-pair-sol61/run_pair.py` for controls 0 and 1, `fresh_control2.py` for the additional independent negative-direction control, and `run_targets.py` for the literal and fixed source-preferred pair. Existing complete per-phase outputs are reused; `.partial` outputs are not evidence of completion. Target scheduling uses three independent process workers. Original cipher files are read-only.

`run_pair.verify` independently verifies every retained candidate against both ciphertexts and recomputes the frozen language score in Python. `reranked.json` preserves all 300 profile candidates per phase, both rings, and full text. `result.json` and `result5.json` preserve operative fourgram and fivegram winners. Exact re-encryption proves consistency with the candidate key; it does not establish a recovered natural plaintext.

## Input alternatives

Literal texts are the unchanged `ciphers/hcp-{350,351}/work/transcription.txt`. Preferred texts come exclusively from `batches/source-variants-350-351/{350,351}-source-preferred.txt`. Their supplied manifest is copied to `variant-manifest.json`; paths and hashes are in `input-provenance.json`. No extra glyph correction is permitted. The only preferred changes are 350 position 15 X→K, 351 position 8 U→J, and 351 position 378 M→K. Original scans, metadata and transcriptions remain unchanged.

The physical-source audit supports a possible 1 March 1944 sending chronology for 351, following 350's recorded 28 February, but an uncertain arrival stamp does not establish a daily shared cryptographic key. The visible first/last groups have no delimiters excluding them from the 385-letter bodies; unencrypted framing remains a possible interpretation rather than an input fact.
