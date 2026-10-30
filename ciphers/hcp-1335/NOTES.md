# Notes hcp-1335

2026-10-30: captured by Claude Opus 5.5 (orchestrator).

## 2026-10-30 — solver pass (Claude Opus 5.5) — PARTIAL, no marker

Note: first crops, written to the shared scratchpad, were overwritten by a parallel worker (lines 2-5 showed hcp-1337's text). Everything below was re-read from work/crops/, cut from work/hires/pc_hcp_16_adr.JPG. The cipher wheel across the scan is the portal's watermark, not part of the card.

Transcription (36 signs, each followed by a dot; work/transcription.txt):

    M O D A A H Q / S D~ D N F N T W / F M D R~ D H Y A / F M B O W F L A K / F Y D C

Doubtful: line 2 sign 2 (D with an open, curled foot, could be R); line 3 sign 4 (R, partly A-like, sits on a paper crease). Line 1 sign 4 has a dark ink star on it; same cursive A as sign 5.

What this is: most likely NOT a letter-for-letter cipher but a first-letter abbreviation (each sign = the initial of one word, dots mark the words).
Evidence (`python3 -I ciphers/hcp-1335/work/analyse.py` from repo root; checks source hashes):
- All six sister cards (1322, 1334, 1336-1339; rough, unverified readings in work/sisters_rough.txt) share a frame: opening M O|G D A A H Q|A S D, closing W F L A K or W E L T A F K, then F Y D C / F Y E D C / F Y E A A D C. The frame varies by inserting or dropping single letters, as whole words would, which a letter cipher of running words would not do.
- Pooled 265 signs: E is 4.2% (English text ~12.7%, word-initial ~2%). Of all 26 Caesar shifts, shift 0 scores best under both models, and word-initial beats text-letter frequencies at shift 0 (-846.5 vs -858.1). Only 36 signs on this card, so this is supporting evidence only.
- hcp-1322 has "15 to 11" and "(in MMs)" in clear among the letters, so the writer is not encoding every character.

Tentative expansion (HYPOTHESIS, not a decipherment; expansions are guesses, most secure first):
- F Y D C = From Your Devoted C. (C = sender's initial; F Y E A A D C on 1338/1336 = From Your Ever And Always Devoted C.)
- W F L A K = With Fondest Love And Kisses.
- D H Y A F M B = Darling, Hope You Are Feeling Much Better (D H Y A G O on 1337/1338 = Hope You Are Getting On). O is open.
- M O D = My Own Darling (M G D on 1322, 1337: G open).
- A A H Q S = All At Home Quite S... (Safe? Satisfactory?) — weak. Next D = Darling? weak.
- D N F N T W F M D R — only "D N" = Do Not and "F M" = For Me are guessable; rest open.

Why it stops: one letter per word does not determine the word. The middle (about 15 signs) cannot be expanded uniquely, no key or clear-text version is known, and even the frame words are inference. Stating a full plaintext would be forcing words onto letters, so SOLUTION.md and DONE1 are not written. A real solution would need a companion letter or the C./Miss Wooster correspondence in clear. Not tried: full verified transcription of the six sisters (each has its own directory) and joint expansion across them, which could firm up the frame but not this card's unique middle.
