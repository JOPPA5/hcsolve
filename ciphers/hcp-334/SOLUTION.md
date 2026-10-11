# Unsolved — HC Portal334
Solver: OpenAI GPT-6 Astra,2026-10-11.

No verified key, cipher type, plaintext or translation has been recovered. No review marker or register entry is warranted.

## Source and damage
Portal identifies MZV75295/1943,19October1943, Spisiak to MZV Bratislava. Source image shows a Budapest dispatch strip. Status Not solved, tag Unsolvable and title referring to incompleteness are source characterizations, not proof of impossibility. Source is the portal's1024px large conversion, not original upload; preserved unchanged. No attached transcription or solution.

Manual reading found30 cipher groups. One starts beneath a folded flap (?DZQR), and another has only four clear letters (FWXX). A150-position model therefore includes148 read letters and two unknowns, but this model is unconfirmed. The second gap's five possible positions were tested. Some other letters remain uncertain. Header35 counts telegram words, not necessarily encrypted groups; it does not prove five entire cipher groups are missing.

## Results and controls
Gap-preserving period analysis found an exploratory signal at period15. Standard A–Z additive Vigenere attempts across periods1–20 and five gap placements did not produce coherent text. On two invented150-letter controls with identical gap positions, the same solver recovered period9 and15 keys and all148 known letters. These positive controls validate those cases, not exhaustive attack coverage.

The preserved text, damage and language evidence do not identify a cipher. Other omissions, letter errors, alphabet conventions and more complex systems remain open. An additional synthetic known-key transposition control demonstrates that retaining erasures preserves recoverable positions whereas deleting them changes the grid; it is not evidence334 uses that system.

## Reproduction
From repository root:

```sh
sh ciphers/hcp-334/work/reproduce.sh
```

Requires Python3 and C++17. This reproduces diagnostic tests, disclosed artificial controls and target attempts from the manual transcription. It does not perform source-image OCR or produce a historical plaintext. Complete uncertainty and results are in NOTES.md and work/. Further useful evidence would be a sharper original image or the associated telephone clarification/full retransmission; no missing text has been invented.

A further controlled Beaufort/Porta attack recovered all148 readable positions of four synthetic controls (periods9/15), but yielded no coherent target at periods1–24 across all five erasure placements. This expands attempted polyalphabetic systems without establishing an exclusion or a historical plaintext. Reproduce with `python3 ciphers/hcp-334/work/run-poly.py`; compile its C++ source with C++17 first.

German-language Vigenere/Beaufort/Porta checks also passed six independently held-out damaged controls, but produced no coherent target under the same1–24-period/five-gap model. This is an unsuccessful conditional search, not a family exclusion.

Further ciphertext-feedback tail tests and plaintext-feedback searches recovered their independent controls (the latter all150 positions, including erasures), but no coherent target under the disclosed lag/sign models. Exact recurrences and scripts are in NOTES.md. No decrypted historical text or key is claimed.

The German plaintext-feedback tests also recover all150 positions of six independent held-out controls; their target attempts remain incoherent. Source/transcription were not changed to improve scores.


## Additional28-letter C model (main solver,2026-10-11)

The primary VHÚ2020 article p107 retains Č and Š in a28-symbol substitution alphabet, so prior26-letter MASC searches are incomplete for that orthography. A separate28-symbol bijective-key search, with Č/Š folded only for language scoring, recovered two independent115-letter controls exactly afterfolding. Forward and reverse literal target transcriptions produced incoherent whole texts. Unknownsourceglyphs were erased for scoring rather than guessed. The test does not exclude the fullfamily or prove diacritic/keyuniqueness. Evidence/provenance/reproduction: `batches/c28-solvers/REPORT.md`, `summary.json`, and `ciphers/hcp-369/work/c28-controls.json`. No decryption isclaimed.


## Periodic mixed-alphabet extension (main solver, 2026-10-11)

Controlled Q1/Q2 models combine an arbitrary substitution alphabet with periodic shifts. Q1 recovers both invented controls exactly but changes one proper-name letter on each genuine TEST control; the correct controls are present in a blind all-single-swap neighborhood. Q2 recovers both its invented and genuine TEST T3 controls exactly at all148 readable positions. All25 Q1 and15 Q2 target cases remain globally incoherent. The shift spaces are enumerated within their stated periods, while alphabet search and Q1's64-candidate pruning remain heuristic. This is additional unsuccessful cryptanalysis, not family exclusion or a plaintext claim. Equations, controls, candidate neighborhoods and reproduction commands are in NOTES.md and work/.


## Czech-language substitution scout — main solver, 2026-10-11

A separate Czech UD-CAC TRAIN-only 3/4/5-gram model tests the conditional Czech alternative. Two independent115-letter TEST controls recover all115 folded letters under26/28-symbol substitution, but both85-position controls with two erasures fail (44/83 and19/83). All16 targets across369/367/334/332, forward/reverse and26/28symbols, remain incoherent as full texts. Short-message negative results are especially weak after those failed controls. No Czech language identification or family exclusion is claimed. Frozen model provenance, controls, full keys/candidate texts and reproduction commands are in batches/czech-scoring/SOURCES.md, REPORT.md, controls.json and target-summary.json. Sources/transcription holes remain unchanged.
