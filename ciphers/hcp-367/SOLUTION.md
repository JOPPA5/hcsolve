# HC Portal 367 — unresolved

No plaintext or key is claimed. Solver: GPT-6 Astra.

The portal identifies MZV message489/1944 from Pissko to Bratislava, dated29 April1944, and says a repeated telegram remained indecipherable. The saved source is its displayed large image conversion; no attached transcription or solution was used.

My diplomatic transcription preserves uncertainty:

```
PHVEL AIASO CDRET X?ET? IUEMS COLEX OTDRE EEABA HBHKS
NSSDI JJRLI VXRSI PULDA AGNLK POELV XONTC RSNAO
```

The17-group/85-letter layout agrees with header185. No missing whole group is visible. Group4's tentative reading XAETN was used only in explicitly labeled diagnostic input. The underlined OTDRE and adjacent handwritten mark remain unresolved source features.

Reproduce implemented diagnostics from the repository root:

```
sh ciphers/hcp-367/work/reproduce.sh
```

This command does not produce a plaintext. Controlled single-columnar searches produced no supported reading. The optimizer recovered an80-letter width11 control but failed a width19 control, so its failures cannot exclude more complex transposition. R/XQ remains a contextual hypothesis, not an established type. There is no supported original-language plaintext or translation.

Source limitations, synthetic controls and exact tested cases are in NOTES.md. No register entry or completed-solution marker is appropriate.


## Additional28-letter C model (main solver,2026-10-11)

The primary VHÚ2020 article p107 retains Č and Š in a28-symbol substitution alphabet, so prior26-letter MASC searches are incomplete for that orthography. A separate28-symbol bijective-key search, with Č/Š folded only for language scoring, recovered two independent115-letter controls exactly afterfolding. Forward and reverse literal target transcriptions produced incoherent whole texts. Unknownsourceglyphs were erased for scoring rather than guessed. The test does not exclude the fullfamily or prove diacritic/keyuniqueness. Evidence/provenance/reproduction: `batches/c28-solvers/REPORT.md`, `summary.json`, and `ciphers/hcp-369/work/c28-controls.json`. No decryption isclaimed.


## Czech-language substitution scout — main solver, 2026-10-11

A separate Czech UD-CAC TRAIN-only 3/4/5-gram model tests the conditional Czech alternative. Two independent115-letter TEST controls recover all115 folded letters under26/28-symbol substitution, but both85-position controls with two erasures fail (44/83 and19/83). All16 targets across369/367/334/332, forward/reverse and26/28symbols, remain incoherent as full texts. Short-message negative results are especially weak after those failed controls. No Czech language identification or family exclusion is claimed. Frozen model provenance, controls, full keys/candidate texts and reproduction commands are in batches/czech-scoring/SOURCES.md, REPORT.md, controls.json and target-summary.json. Sources/transcription holes remain unchanged.
