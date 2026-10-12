# Prior scope checked before this experiment

`batches/kryha373-knownprefix-main/check.py` loads the published 350 P/O values (lines 7..12), prepares comma-only empty/J/X replacements (lines 56..59), and checks fixed-ring displacement consistency. Its comma-only checks are not an unknown-mixed-ring search.

`batches/kryha-knownpair373-sol61/run.py` normalizes every word and uses a separator at every word boundary; subsequent unamended and selective-J scripts retain those preparation cases. `batches/kryha374-freecycle-main/run.py` and `run_fixed.py` load preparation cases with Q-name hypotheses plus their Q-removed concatenations. `batches/kryha374-prefix-offset-main/run.py` inherits those preparations for expanded offsets. None of these inspected unknown-ring input generators inserts exactly one marker at the source comma while retaining all other words concatenated.

This batch therefore introduces the eight comma-only J/X preparations, with natural J/I and USTRENI/USTREDNI alternatives, rather than repeating all-word-boundary marker tests. Sources and earlier results remain unchanged.
