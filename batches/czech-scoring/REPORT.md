# Czech MASC alternative — main solver, OpenAI GPT, 2026-10-11

Conditional language hypothesis only. Primary UD Czech-CAC TRAIN supplies sentence 3/4/5-gram frequencies, weighted .15/.4/.8; TEST supplies independent controls with random substitution keys. No target words or TEST text enter the models. Frozen build checksums and source provenance are in build-report.json and SOURCES.md. This corpus dates mainly from the 1970s/1980s; its language patterns are only a proxy for 1940s messages.

Both 115-letter independent controls recover their full folded plaintext under the 26/28-letter models. Both 85-position controls with two erasures fail (26-symbol 44/83, 28-symbol 19/83 correct); the correct text is absent even from all single-key-swap neighborhoods. These are diagnostic truths after search, never seeds or selection criteria. A 28-symbol success proves folded letters, not distinct Č/C or Š/S orthography or a unique unused-letter key.

Target scouts preserve literal transcriptions and erase '?' without shifting positions: 369,367,334,332, forward/reverse, both alphabet sizes. The shorter messages are exploratory after failed short controls. Complete keys, scores and whole candidate texts are in target-summary.json. No family exclusion can follow from negative scouts; no DONE or register entry should be created without a supported decipherment.

Reproduce from repository root: `python3 batches/czech-scoring/build.py`, compile mono26.cpp and mono28.cpp with C++17, `python3 batches/czech-scoring/controls.py`, then `python3 batches/czech-scoring/targets.py`. Only TRAIN/TEST download copies are read; cryptogram source files are not edited.

All16 scouts completed. Inspection of their complete texts found no supported reading. No marker or register entry created.
