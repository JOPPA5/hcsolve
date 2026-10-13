# HCP1000 — existing published partial, still incomplete

## Publication history
The exact HCP1000 item appears in [crackciphers problem 134](https://crackciphers.com/problem/134), with a substantial partial German reading in [solution 134-1](https://crackciphers.com/problem/134/solution/1), dated 8 September 2026. This was found **before** attempting a new decipherment. The portal's `Not solved` flag therefore does not mean that no one has read the card.

The edition says the writer misses Fritz today, expects him back tomorrow and sends affectionate greetings. Several clauses and joins remain unresolved in that edition. The three complete closures elsewhere in that packet are HCP1004, HCP1106 and HCP1006, **not HCP1000**.

## Known public mechanism
Direct numerical alphabet A=1 through Z=25, with I/J sharing 9. The key was already public, including the 2020 Schmeh discussion. No new secret key has been recovered here. `work/public-key.json` preserves the mapping (9 is printed I; J requires linguistic interpretation).

## Current work
Both original images were archived unchanged. Working rotation, red-channel contrast and sharpening made the numerical body easier to inspect. The opening fragment in `work/opening-fragment.txt` reads `MEIN LIEBER FRITZ` with the known key. This is already consistent with the published partial, not a new plaintext discovery. The rest of the faded numerical stream has not been transcribed reliably enough to close the remaining joins.

Run `python3 ciphers/hcp-1000/work/decode-fragment.py` from the repository root to decode **only the recorded fragment**. There is no command for a source-verified complete plaintext. No DONE/FINAL marker or new-solution register entry is warranted.

A later source check using R-minus-G contrast (`work/opponent-reading.png`) improved background separation but did not yield a reliable additional numeric transcription. No new plaintext was accepted from it.
