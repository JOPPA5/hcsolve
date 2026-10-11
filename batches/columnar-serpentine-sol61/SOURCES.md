# Inputs and provenance

Frozen TRAIN language models `batches/columnar-stratified/model2.tsv` through `model5.tsv`, and independently calibrated `beam.cpp` / `one-long.cpp`, were read-only inputs. The two copied programs add only readout-rank alternating reversal. Model weights and beam budget are unchanged. Model hashes appear in provenance.json.

Control text: held-out Slovak UD TEST sentences from `ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu`, explicitly excluding literal sentences appearing in `ciphers/hcp-393/work/sk_snk-ud-train.conllu`. Both hashes and complete selected source sentences are recorded. Preparation strips nonletters and accents; it is a constructed control preparation, not an established historical telegram convention. Keys and direction bits are freshly independent and fully disclosed.

Target inputs: existing immutable/read-only solver transcriptions for HCP363,393,345,396,369. HCP363 uses transcription-raw.txt with erasures, others transcription.txt. No source scan or transcription was edited. No solution attachments, new portal fetch, browser, hidden API, historical target answer or online solution search was used. Alternating-column historical attribution is unsupported.
