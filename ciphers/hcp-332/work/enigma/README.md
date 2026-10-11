# Conditional Enigma experiments for HCP332

These experiments do not identify the historical machine. They explicitly interpret separate TRC as the initial rotor windows, exclude it from the40-letter body, and assume no plugboard. Both literal O/D variants are used. Antal2020 describes unidentified K machines and a six-letter password convention, suggests commercial Enigma K as one possible machine, and says Kryha replaced machines in1943; none establishes TRC or this target as Enigma.

search.cpp tests Enigma I rotors I–V (60 left-to-right orders), stationary wide reflectors A/B/C and every26^3 ring triple:3,163,680 settings per input. Rotor windows advance before the signal. Notches are tied to displayed letters (Q/E/V/J/Z), independent of ring setting, and middle double-step is implemented. A/B/C wiring and all rotors are checked as permutations; reflectors are fixed-point-free involutions.

The implementation exactly matches both communication vectors in primary Py-Enigma docs (II IV V/BUL/B, plugboard AV BS CG DL FU HZ IN KM OW RX, WXC+BLA→KCH and BLA+THEXRUSSIANSXAREXCOMINGX→NIBLFMYMLLUFWCASCSSNVHAZ). controls.py compares100 independently random100-letter settings/rings/windows against unaltered downloaded Py-Enigma, and verifies reciprocity/no-self-encryption. Published KDO,KDP,KDQ,KER,LFS,LFT,LFU stepping is checked with the independent package. Plugboard support exists solely to verify those vectors; the searched family has no plugs.

40-letter controls are encrypted with independent Py-Enigma at TRC before any key search. German plaintext is from UD TEST only, excluded from model training, and matched to target IC/distinct-letter distribution. Slovak plaintext is first40 letters of an earlier separately planted43-letter holdout (previously exposed during scoring development, not injected into model). Frozen scorers are not tuned for these Enigma experiments. Both controls recover exact whole plaintext at rank1 under their matching-language multigrams and lexical reranker; settings match the planted keys for Enigma I. This validates specific in-family cases, not every plaintext/domain.

All settings are scored with unchanged Slovak/German3/4/5gram models from batches/scoring-sol61. Top1,000 per language are retained and reranked with unchanged dictionary/POS segmentation. Reranking is limited to those retained candidates. No coherent whole target reading was found; scored fragments are not decipherment. Reading uncertainty, wrong starting window, encrypted/message indicator, plugboard, other rotors, unknown wiring, historical encodings and other machines remain open.

commercial.cpp separately tests commercial rotor wirings given by the raymas implementation README (LPG...,SLV...,CJG...), turnoversY/E/N, QWERTZ entry wheel and IMET... reflector. All6 rotor orders,26^3 rings,26 manually set stationary-reflector positions and both entry-wheel orientations are enumerated:5,483,712 per input. The opposite entry orientation is included explicitly because wiring-table orientation must not be assumed from an unidentified machine. Reflector position is encoded as letterA–Z followed by entry direction0/1 in result files. Stationary means manually set and does not step with key presses. This is commercial wiring, not Swiss rewired rotors. The author repository's unfinished commercial test is NOT a usable published vector: it duplicates/misnames rotors and asserts empty text. Our controls instantiate correctly named/specifed rotors using its unchanged simulator;100 random100-letter settings (both orientations, varied rings/windows/reflector) agree exactly with C++. Reciprocity/permutations/involution are also checked. Hamer/Sullivan/Weierud corrected primary paper independently supports the shared entry/reflector and commercial settable-reflector convention, but its Swiss rotors are different.

Reproduce from repo root, with saved vendor packages and model files:

```
c++ -O3 -std=c++17 ciphers/hcp-332/work/enigma/search.cpp -o ciphers/hcp-332/work/enigma/search
c++ -O3 -std=c++17 ciphers/hcp-332/work/enigma/commercial.cpp -o ciphers/hcp-332/work/enigma/commercial
c++ -O3 -std=c++17 ciphers/hcp-332/work/enigma/rerank.cpp -o ciphers/hcp-332/work/enigma/rerank
python3 ciphers/hcp-332/work/enigma/controls.py
python3 ciphers/hcp-332/work/enigma/run.py
python3 ciphers/hcp-332/work/enigma/rerank.py
python3 ciphers/hcp-332/work/enigma/commercial-controls.py
python3 ciphers/hcp-332/work/enigma/commercial-run.py
python3 ciphers/hcp-332/work/enigma/commercial-rerank.py
```

These produce diagnostics and controls, not a target decryption. frozen-score.hpp copies only unchanged scoring functions, excluding optimizer, from batches/scoring-sol61/mono-frequency-seeded-strict.cpp. Primary packages/licenses retained in vendor; source hashes/provenance in provenance.json and ../../SOURCES.md. No original scan/metadata source is modified.
