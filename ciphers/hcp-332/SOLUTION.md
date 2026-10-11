# HCP-332 — unresolved

No supported cipher type, key, original plaintext or translation has been established. The portal labels this unsolved and “Unsolvable”, and says the key was not included; those are source statements, not mathematical proof that it cannot be solved.

Manual transcription from `source/cryptogram.jpg`, with a watermark-obscured O/D variant:

`TRC KDUFA VHSFC OYAUB EJFNK QTNZE UG[O/D]ZR UBCIE GZZYK`

Eight five-letter groups follow TRC. Whether TRC is ciphertext or an indicator is unknown. The cleartext address is Ministry of Foreign Affairs, Bratislava; it is routing material, not recovered ciphertext plaintext.

Reproduce the bounded analysis from the repository root:

```sh
sh ciphers/hcp-332/work/reproduce.sh
```

This command produces attack/diagnostic results, **not a decryption**. Affine/reversed-affine tests and stochastic Vigenère periods 1–6 yield no coherent full reading. An invented Slovak Vigenère control of the same length is recovered exactly at its true period. Exact MASC pattern checks reject several speculative repetition/telegram cribs but do not reject the general MASC family. Details and limitations are in NOTES.md and work/structure.json.

No solution claim, DONE marker, PDF solution report or register entry is warranted. The original scan, leading-group interpretation, historical alphabet/system and missing key remain uncertain.

Second-pass analysis adds independently successful Beaufort, Porta and ordinary columnar-transposition controls, exact period1–4 enumeration for Vigenère/Beaufort/Porta, and a conditional ordinary-Playfair exclusion based on the ciphertext digraph ZZ. The general-substitution control fails, exposing short-text model overfitting; that attack supplies no valid exclusion of MASC. No coherent full target decipherment emerged.

Reproduce these additional checks with:

```sh
sh ciphers/hcp-332/work/reproduce-alternatives.sh
```

German dictionary/UD scoring now exactly recovers two independent short German substitution controls and a separate test-only40-letter control with the target IC and22 distinct letters using generic paired dictionary anchors. All saved forward/reverse German target candidates are incoherent; they do not establish plaintext. Historical machine context remains ambiguous (commercial Enigma K suggested, Kryha replacement in1943). Detailed limits and reproduction are in NOTES.md and batches/scoring-sol61/german/README.md. No cipher-family exclusion or solution follows from the negative bounded searches.

A further conditional Enigma check exhausts3,163,680 Enigma I settings and5,483,712 commercial-wiring settings per literal O/D40-letter body, with TRC as assumed initial window and no plugboard. Both models pass independent implementation controls and recover two40-letter plaintexts/settings exactly at rank1. No coherent target reading emerges from retained/reranked candidates. This neither identifies the historical machine nor excludes other Enigma keys/procedures; see work/enigma/README.md. Status remains unresolved.


## Additional28-letter C model (main solver,2026-10-11)

The primary VHÚ2020 article p107 retains Č and Š in a28-symbol substitution alphabet, so prior26-letter MASC searches are incomplete for that orthography. A separate28-symbol bijective-key search, with Č/Š folded only for language scoring, recovered two independent115-letter controls exactly afterfolding. Forward and reverse literal target transcriptions produced incoherent whole texts. Unknownsourceglyphs were erased for scoring rather than guessed. The test does not exclude the fullfamily or prove diacritic/keyuniqueness. Evidence/provenance/reproduction: `batches/c28-solvers/REPORT.md`, `summary.json`, and `ciphers/hcp-369/work/c28-controls.json`. No decryption isclaimed.


## Czech-language substitution scout — main solver, 2026-10-11

A separate Czech UD-CAC TRAIN-only 3/4/5-gram model tests the conditional Czech alternative. Two independent115-letter TEST controls recover all115 folded letters under26/28-symbol substitution, but both85-position controls with two erasures fail (44/83 and19/83). All16 targets across369/367/334/332, forward/reverse and26/28symbols, remain incoherent as full texts. Short-message negative results are especially weak after those failed controls. No Czech language identification or family exclusion is claimed. Frozen model provenance, controls, full keys/candidate texts and reproduction commands are in batches/czech-scoring/SOURCES.md, REPORT.md, controls.json and target-summary.json. Sources/transcription holes remain unchanged.
