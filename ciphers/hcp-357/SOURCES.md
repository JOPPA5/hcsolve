# Sources
Retrieved 2026-10-11 via rendered portal browser.
- source/metadata.md: all3 tabs https://crypto.hcportal.eu/dashboard/cryptograms/357 . Not solved; World War II, Slovakia, Diplomacy.
- source/cryptogram.jpg: displayed portal `-large` conversion (1024 pixels wide), not the original upload https://api.hcportal.eu/media/996/conversions/29441655400410-large.jpg .

## Context and statistical helper
- Antal, Zajac and Grošek, *Diplomatic Ciphers Used by Slovak Attaché During the WW2*, HistoCrypt 2020, pp.22–23, https://ep.liu.se/ecp/171/004/ecp2020_171_004.pdf . Consulted 2026-10-11 for the R/XQ method; not a solution to this message.
- `work/quadgrams.tsv` is copied byte-for-byte from `ciphers/hcp-393/work/quadgrams.tsv`, derived by that directory's `train.py` from the archived public Universal Dependencies Slovak SNK training text. Original corpus URL: https://raw.githubusercontent.com/UniversalDependencies/UD_Slovak-SNK/master/sk_snk-ud-train.conllu . Fourgram values are log occurrence counts, default unseen score −4. Helper-table SHA256: `2398fdb361697329f7a0ca13d5d17a85825d41d50296582fca1da34d9a3e46ee`. Used only to rank search candidates, not as a source of plaintext.
- `work/attack.cpp` adapted from the neighboring solver's `ciphers/hcp-393/work/attack.cpp`; `multistage.cpp` and `baseline.py` written for this attempt.


## Review-1 source limitations and added observations

The saved image is the portal's displayed `-large` conversion. No original-resolution file or original-download link was captured, so an original upload has not been retrieved and its availability is not asserted. No guessed original URL or hidden API was used. The parent performed browser acquisition; this revision used the preserved image locally. Scan observations omitted from portal metadata are added in `work/scan-observations-review1.md` without editing the immutable metadata.

The cited paper's Figure 5 was additionally inspected from its downloaded PDF on 2026-10-11; a rendered page is preserved at `batches/analysis-395-396/paper-page8.png` and the public paper at `batches/analysis-395-396/context-paper.pdf`. It is a historical method example, not a published solution of this target. It supplies counterevidence to a universal header-prefix-as-indicator-position rule, and demonstrates unequal stage widths.
