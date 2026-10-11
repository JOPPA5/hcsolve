# Sources and model provenance

Main OpenAI GPT solver developed a distinct native CP-SAT encoding: every physical column is a fixed-length interval at an unknown start, all intervals pack the exact output length without overlap; Element constraints connect every column character to its assigned output position. Intermediate inventories and physical column-0 ranks are explicit constraints.

Official OR-Tools Python/CP-SAT documentation read2026-10-11:
- https://developers.google.com/optimization/cp/cp_solver
- https://developers.google.com/optimization/install/python

OR-Tools9.15.6755, installed through public PyPI into /private/tmp/hcsolve-ortools. Local installed Python docstrings for add_element/new_interval_var inspected. Version written into every result. A restricted-network installation failed to resolve PyPI; a permitted network command succeeded. No repository dependency or system Python environment was changed.

Cipher convention credited to the independently verified physical-column encoder in batches/r364-primary-sol61/exact_cover.py and the primary HistoCrypt2020 example in batches/historical-context/r-example-verification.json. Their SMT encoding was not copied; solve.py implements a new interval/Element formulation and an independent position-based inverse. The fixed known-plaintext control sentence is an independently authored artificial message used previously in other calibration branches; fresh random keys are declared in controls.py. It is not a historical target plaintext or genuine heldout corpus sample. Truth keys are supplied solely in separate consistency checks, never in blind search.

Actual HCP364 quote, unknown filler, removed group, alignment, glyph/error assumptions remain conditional. No target plaintext or solution was imported. Original cipher sources are read-only.
