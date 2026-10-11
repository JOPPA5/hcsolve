# Conditional Myszkowski transposition — main solver, OpenAI GPT

Independent primary ACA BANANA mechanism vector matches exactly. Both fresh UD Slovak TEST controls (100 positions with width8 repeated ranks,85 positions with width7 repeated ranks and two erasures) recover the full readable plaintext at rank0. No TEST sentence is in the frozen TRAIN model. Keys are independently randomized weak orders and are not required to be dictionary words.

The solver enumerates all onto assignments of columns to ordered ranks for widths2–8, including repeated ranks. Wider widths9–22 use1,747,285 distinct weak-order patterns generated from2,136,227 independently frozen Slovak morphological words (the exact wider-only count is included in each tested count). Dictionary search is incomplete at those widths; neither target words nor guessed titles were inserted. Scoring uses unchanged3/4/5-gram weights. Top100 whole candidates with keys are preserved for every case.

Targets: literal bodies of396,345,393,367,374,369,371,399,395,363, both directions. For396/345 all single-group omissions are additionally explicit conditional indicator hypotheses. Known '?' slots are erased and retained in position. No cipher is identified from a score alone: coherent full plaintext, exact re-encryption, source transcription validation and external review remain necessary before markers or register entries.

Reproduce: `python3 batches/myszkowski/build-keys.py`, compile solver.cpp with C++17, `python3 batches/myszkowski/controls.py`, then `python3 batches/myszkowski/targets.py`. Provenance is in SOURCES.md; controls.json/aca-vector.json/keyword-provenance.json supply exact controls and scope.

Initial72 scouts completed without a coherent full candidate; independent re-encryption passed every winning key.363 was handled as separately labeled literal erasures and A/B with X/A working readings; the original preliminary X runs are retained. Additional single-group omission cases367/374/393 and396 O-reading cases are running.

## Completed extended sweep
All206 saved cases are complete:39648,34528,39344,36736,37436,3636, and369/371/399/395 two each. The count includes preserved preliminary363 working-reading cases, distinct from later literal-erasure cases. Every case evaluates2,242,481 keys/patterns. Extended branches include every single-group omission393/367/374 and both396 C/O readings; these omissions are conditional hypotheses, not established indicators. No winning whole plaintext is coherent.

`python3 batches/myszkowski/verify-targets.py` independently re-encrypts all20,600 retained full candidates exactly, including erasures. This checks permutations and coverage only, not linguistic correctness or historical identification. Short widths are exhaustively searched; wider keyword patterns remain incomplete and the two positive controls do not guarantee recovery at every target length/key. No solution or marker was created.
