# Independent language-model sources

Downloaded 2026-10-11 from primary LibreOffice dictionary repository. No cipher solution source used.

- `source/sk_SK.dic`: https://raw.githubusercontent.com/LibreOffice/dictionaries/master/sk_SK/sk_SK.dic . Slovak dictionary roots/flags/morphology; header160357 entries. Display page https://github.com/LibreOffice/dictionaries/blob/master/sk_SK/sk_SK.dic .
- `source/sk_SK.aff`: https://raw.githubusercontent.com/LibreOffice/dictionaries/master/sk_SK/sk_SK.aff . Affix rules; internal version2.4.8 dated2024-08-29.
- `source/README_en.txt`: https://raw.githubusercontent.com/LibreOffice/dictionaries/master/sk_SK/README_en.txt . Dictionary authorship/provenance.
- `source/LICENSE.txt`: https://raw.githubusercontent.com/LibreOffice/dictionaries/master/sk_SK/LICENSE.txt . License retained.
- Existing local read-only corpus `ciphers/hcp-393/work/sk_snk-ud-train.conllu`: Slovak SNK Universal Dependencies training corpus, already saved by prior solver. Used normalized sentence character sequences and token UPOS transitions. Source provenance remains recorded by HCP-393 owner; no modifications here.

Downloaded-file SHA256 hashes are in build-report.json. The master URL is mutable; saved bytes/hashes specify this experiment's source snapshot.

## German primary sources, downloaded2026-10-11

- german/source/de_gsd-ud-train.conllu and de_gsd-ud-test.conllu: https://raw.githubusercontent.com/UniversalDependencies/UD_German-GSD/master/de_gsd-ud-train.conllu and https://raw.githubusercontent.com/UniversalDependencies/UD_German-GSD/master/de_gsd-ud-test.conllu . Training sentences alone train the model; test is used only for independently selected controls. README.md and LICENSE retained from the same repository.
- german/source/de_DE_frami.dic, de_DE_frami.aff, README_de_DE_frami.txt, COPYING_GPLv2: https://github.com/LibreOffice/dictionaries/tree/master/de . Downloaded from raw.githubusercontent.com/LibreOffice/dictionaries/master/de/<filename>. Original Latin1 bytes retained; build.py normalizes and approximates affix expansion.

German hashes and counts are in german/build-report.json, test-control provenance in german/flat40-generation.json and heldout200-generation.json. Mutable master URLs are pinned for this experiment by retained source bytes and hashes. No published target solution was sought.
