# Štolba reconstruction: primary-source findings, 2026-10-11

Research only. No target solutions or plaintexts were searched. HCP332/334 source files were read locally; nothing in their directories was written.

## Access and evidence

The [publisher article](https://www.tandfonline.com/doi/abs/10.1080/01611194.2021.1998809), Eugen Antal and Pavol Zajac, *The first Czechoslovak cipher machine*, appeared online28 December2021 and in Cryptologia47(3),239–260(2023). Its accessible abstract describes a probable algorithm reconstruction and known-plaintext/ciphertext message-key recovery, while explicitly retaining unknown configuration. Publisher note7 says many six-letter daily settings are meaningful words in both1939 and1943. **I did not read its full text:** ordinary full/PDF requests were inaccessible/403. The author's [official announcement](https://uim.fei.stuba.sk/en/the-first-czechoslovak-cipher-machine/) was search-index accessible but direct retrieval returned502. No legal author manuscript or relevant simulator code was located in the bounded search. No access control was bypassed.

The [CryptoMuseum reconstruction](https://www.cryptomuseum.com/crypto/stolba/) incorporates Antal's2022 correspondence. It supplies these concrete constraints:

- Alphabet25, withoutW; plaintextW becomesVV.
- Six cipher rotors, three control rotors, fixed rotor order.
- Listed mappings take the left side as input, hence cipher mappings describe deciphering.
- A lever event selects one cipher rotor to advance; reverse operation was disabled.
- Control airflow starts atV through7,8,9; pins couple7→8,8→9,9→7.
- Unknown pin layouts and selector prevent a fully established stepping model.
- Daily settings have3+6 letters. Its1January1939 example isFUZ MILICA.
- Three-letter message key is encrypted twice; first three cipher rotors then receive that key.

`wirings.json` preserves its11 mappings. `wiring-validation.json` proves only25-symbol bijections and their inverses, **not full-machine correctness**.

The authors' [2019 primary conference paper](https://www.cryptomuseum.com/crypto/stolba/files/ecp19158003.pdf), p24, states machine daily keys were distributed for all1943. It points to VHA fund53(53-88/1-19), document404621/Taj.obr.1942. The1939 context points to KVV box2, document20.800/Taj.3.odd.1939, and MNO tajné box2, k.č.77/39/Taj.3.odd.1939. This paper does **not** disclose the needed15October1943 key. Thus there is an archival lead, not a recovered daily schedule.

## Specific opportunities and limits (our deductions)

HCP332 metadata dates the Budapest→Bratislava message15October1943. Its work transcription has a separateTRC prefix and a40-letter body with anO/D alternative, noW. That is compatible with the alphabet but does not identify Štolba. HCP334's literalFWXX? containsW: a faithful25-symbol cipher body cannot produceW. Preserve that conflict; only a source-supported glyph/error or external-header interpretation can remove it. Do not silently map ciphertextW→VV, since the documented expansion applies to plaintext preprocessing.

An Enigma reflector model introduces unsubstantiated constraints here. A25-point permutation must not be assigned Enigma's no-self-encryption rule. DailyFUZ MILICA is a1939 example, not the1943 target key. Meaningful six-letter settings suggest a later dictionary prior only after recovering actual date-specific settings or validating the model; guessing such a word is not evidence.

The most concrete next cryptanalytic test is an **indicator-only constraint model** if a six-letter encrypted double-message-key indicator can be established from the scan/protocol. LetD_s be a verified static deciphering permutation at six cipher offsetss. For candidate indicatorY1…Y6 imposeD_s1(Y1)=D_s4(Y4), D_s2(Y2)=D_s5(Y5), D_s3(Y3)=D_s6(Y6). Consecutive cipher states should advance exactly one coordinate modulo25 under the documented forward-only branch. Retain pins and selector as unknown shared functions; do not substitute invented notch patterns. When a control position repeats, shared pin/selector variables must give the same decisions, which is stronger than an arbitrary six-choice stepping sequence. Both pre/post-control and pre/post-character timings remain explicit hypotheses until the full reconstruction establishes them.

This tests a protocol relation without fitting a supposed target plaintext. First validate it on independently generated messages from a documented complete machine configuration, including static-entry orientation and indicator resets. An unrestricted unknown-function SAT witness would show compatibility with a relaxed model, not historical pin recovery. A body candidate needs complete forward reproduction, inverse verification, and alternate-witness/uniqueness checks. A proof of UNSAT would apply only to its declared orientation/timing/indicator assumptions.

**Immediate missing inputs:** legally accessible full2021 manuscript/supplement, actual1943 daily schedule, selector map, pin layout or constraints on it, entry-disc direction conventions, rotation-label sign/zero, event timing and indicator reset details. The primary sources found genuinely constrain the architecture, but do not supply these values. This research does not justify another Enigma-style simulator or any target solution claim.
