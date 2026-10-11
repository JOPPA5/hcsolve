# Sources
Retrieved2026-10-11 through rendered portal UI.
- source/metadata.md: all3tabs https://crypto.hcportal.eu/dashboard/cryptograms/363 . Notsolved,WWII Slovakia Diplomacy Unsolvable.
- source/cryptogram.jpg: displayedlargeconversion https://api.hcportal.eu/media/1013/conversions/62651655400437-large.jpg . Notverifiedoriginaluploadresolution.

##Analysis helpers
- work/quadgrams.tsv copied read-only from393, whose train.py derives it from preserved UD Slovak SNK https://raw.githubusercontent.com/UniversalDependencies/UD_Slovak-SNK/master/sk_snk-ud-train.conllu . Statistical helper only, no targetplaintext.
- Initial work/columnar.cpp copied from345; improved version adds block-relocation mutation. Controls are invented testmessages explicitly stored with keys, never historical plaintext claims.
- Historical Rlength recommendation mentioned in NOTES derives from Antal,Zajac,Grošek, *Diplomatic Ciphers Used by Slovak Attaché During the WW2*, https://ep.liu.se/ecp/171/004/ecp2020_171_004.pdf ,pp22–23, read previously during395analysis. It does not identify/solve363.

## Segmentation-aware helper sources2026-10-11

- work/segmented/bigrams.tsv is independently derived from read-only ciphers/hcp-393/work/sk_snk-ud-train.conllu, primary Universal Dependencies Slovak SNK training corpus referenced above. Counts use normalized original sentence text, not synthetic controls.
- Frozen3/4/5gram helper models read-only from batches/scoring-sol61/, whose SOURCES.md/build-report.json retain primary LibreOffice Slovak dictionary/affix and UD provenance/licenses/hashes. This experiment does not add control sentences or target cribs to those models.
- New scripts/results in work/segmented/ are GPT-6.1 Sol's own conditional attack/calibration work. No published HCP363 plaintext consulted.
