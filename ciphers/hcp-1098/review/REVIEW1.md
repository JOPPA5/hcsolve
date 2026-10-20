ACCEPT

# Review 1 — HCP 1098 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-19. A simple A1Z26 (A=1 … Z=26) numerical substitution, correctly identified and completely and correctly read. I compared every line of `work/transcription.txt` with the scan and found no reading that changes a letter.

## What I verified and how

1. **Commands.** `python3 ciphers/hcp-1098/work/decrypt.py` exits 0 and prints the claimed text; `python3 ciphers/hcp-1098/work/audit.py` reports 312 numerical symbols, 22 lines, all groups decoded and re-encoded, and the readable English with the identical letter sequence.
2. **Own decoder.** A few lines of my own Python, reading `work/transcription.txt` directly (split on `/`, braces kept as cleartext, `chr(64+n)`), give the same text; the only difference is that mine does not rejoin the six line-break splits (`SATUR/DAY`, `HA/PPENS`, …), which the solver does and declares. 312 numbers, largest 25 (no Z needed).
3. **Transcription against the scan.** 4× crops of the whole numerical text (`review/work/r00–r04.png` for the right-hand column, `b0–b3.png` for the four long lines at the bottom). Every group matches the ledger. Where a digit is ambiguous (handwritten 5/6, 13/18, the `20`/`23` in the dark-inked spots, the groups under the HCPortal watermark), the reading in the ledger is the one the shape supports, and the alternatives would give non-words. On line 17 the writer struck out one sign before `4.1.25` (DAY); the ledger correctly ignores it.
4. **Cleartext spans.** `P.M.`, `or`, `Pine St.`, `Tues.`, `& Wed. forenoon.` and the final `P.M.` are written in ordinary script on the card, exactly where the ledger puts them.
5. **Context.** Address side: `Mr. Homer Wright, Bernardston, Mass.`, machine cancel Brattleboro, Vt., `MAR 25 … 11-30A 1909`. 25 March 1909 was a **Thursday**, so the text fits in detail: it was written on Wednesday evening ("to night"), after work "Tues. & Wed. forenoon"; "to morrow P.M." is Thursday afternoon; the visit is planned for Saturday. Brattleboro to Bernardston is a short rail trip, consistent with "the P.M. or evening train". `Pine St.` exists in Brattleboro.
6. **Sources and novelty.** No plaintext attached on the portal; the linked Schrödel 2021 paper does not contain this card (solver's check, not repeated by me). Status "Not solved" as recorded.

## Findings

1. **minor — `THEN`.** "more then I know of" is period spelling for "than"; the solver keeps the literal word and explains it. Fine; the English readable text could add "[than]".
2. **minor — sender.** Nothing on the card names the writer. "Netties" (literally `NETTIES`, no apostrophe) is a person's name in the possessive. The Slovak translation correctly leaves gender open (`pracoval(a)`). The report should not guess a name or relation.
3. **minor — protocol.** No report yet, as expected at `DONE1`.

## What I could not verify

- Nothing material. The novelty search is the solver's (one linked paper, portal status); A1Z26 postcards are often read privately, so "first decipherment" should not be claimed.
