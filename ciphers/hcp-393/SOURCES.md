# Sources

Retrieved 2026-10-11 through rendered portal UI.
- `source/metadata.md`: all three tabs at https://crypto.hcportal.eu/dashboard/cryptograms/393 . Status Not solved; World War II, Slovakia, Diplomacy.
- `source/cryptogram.jpg`: attachment opened at full resolution; displayed image URL https://api.hcportal.eu/media/1094/conversions/59011655400569-large.jpg . No attached solution or transcription.

## Statistical helper (not cipher/solution source)
- `work/sk_snk-ud-train.conllu`: public Universal Dependencies Slovak SNK training corpus downloaded 2026-10-11 from https://raw.githubusercontent.com/UniversalDependencies/UD_Slovak-SNK/master/sk_snk-ud-train.conllu . Used for local fourgram scoring only. The exact downloaded bytes are preserved in work/ for reproducibility; train.py derives quadgrams.tsv. No candidate plaintext was imported from this corpus.

## 2026-10-11 independent 100-letter controls (GPT-6.1 Sol)

- `work/square10/sk_snk-ud-test.conllu`: public primary UD Slovak SNK TEST corpus, downloaded from https://raw.githubusercontent.com/UniversalDependencies/UD_Slovak-SNK/master/sk_snk-ud-test.conllu . It supplies an independent real 100-letter sentence; it was not added to frozen models. License/provenance: https://github.com/UniversalDependencies/UD_Slovak-SNK . Exact downloaded and existing TRAIN bytes are fingerprinted in `work/square10/validation.json`.
- The new 6–9-gram phrase experiment uses only the already recorded primary UD TRAIN corpus, never TEST. No published target solution was searched or consulted.
