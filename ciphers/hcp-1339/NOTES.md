# Notes hcp-1339

2026-10-30: captured by Claude Opus 5.5 (orchestrator).

## 2026-10-30 Claude Opus 5.5 (solver): stopped as PARTIAL, no marker

No earlier work on this number. No SOLUTION.md written, because there is no key and no provable plaintext.

### Finding: an initial-letter shorthand, not a substitution
The message is English written as the first letter of each word, in dotted capitals, by a hand that changes letter forms freely. Mailed from Barnet to Miss Wooster, The Grange, Shenley, Herts, 10 Jan 1910, 9 AM. Evidence (`python3 -I ciphers/hcp-1339/work/tests.py` from the repo root; it also checks source hashes):
- All seven Wooster cards (1322, 1338, 1339, 1335, 1336, 1334, 1337; Dec 1909 to Feb 1910) open with the same nine letters MODAAHQSD, and close on a varying formula: ...FYDC, FYEDC, FYEAADC. A formula that grows by single letters behaves like added words.
- Letter counts (this card plus my rough, unreviewed readings of the sisters): A 44, D 41, H 19, F 19 against E 9. E is 3.4 %, not about 12.7 %. The word-initial model fits slightly better than the running-text model (-3.211 v -3.235 per letter), which is weak on its own.
- hcp-1322 keeps "15 to 11" and a word-like "(in MMS)" in clear among the letters.
- All 26 Caesar shifts of this card are nonsense. There are no vowels to speak of and the text is 33 letters, so a general substitution cannot be tested on this card alone; the points above are why I reject it, not a solver run.

### Transcription (work/transcription.txt; every sign seen at 3-6x in work/crops/)
    M O D A A H
    Q S D H A R R D
    ? H Y W G O A D
    W F L T A F K F
    L E D C
Doubtful signs:
- L1 sign 4: A, the tall form that also stands at L3 sign 7 and on the sisters' fourth place.
- L2 sign 4: H, alternative B. Flag, top loop and lower bowl match H on L1 and L3, but the foot is faded in a paper crease. Sister 1338 has H A M R D in that place.
- L3 sign 1: UNRESOLVED. A tall stem overwritten by two cross strokes, apparently a correction. Sisters would suggest D here (D H Y A G O A D), but the pixels do not show a D, so it stays "?".
- L3 sign 3: cursive Y (or J); same form as Y in hcp-1335 "H Y A".
- L4 sign 6: F by the sisters (F K); a short foot makes it look like E. Alternative E.
- L5 sign 1: the shape is the same as L on L4 sign 3. The sisters always have Y after the final F, so Y is the alternative; the pixels favour L.

### Hypothetical expansion: NOT a decipherment
Initials lose the words, so no method can prove any of this. It is my reconstruction from word sense:
- MODAAHQSD: "My Own Darling A[...], Arrived Home Quite Safely Dear". A second A could be a name or "Angel". The cards are nearly all posted Sunday night or Monday morning, which fits a weekend visit, then a note on getting home.
- H A R R D: perhaps "Had A Rough Ride Dear" (R R is the weakest part; also "Rather Rough", "Really Rotten"...).
- ? H Y W G O A D: perhaps "[Do] Hope You Were/Will Get(ting) On Alright Dear"; compare the recurring H Y A G O A D "Hope You Are Getting On Alright Dear" on 1338 and 1337.
- W F L T A F K F L/Y E D C: perhaps "With Fondest Love T... A... Fond Kisses From Your Ever Devoted C.". T A is unexplained; 1335 has the shorter W F L A K F Y D C, "With Fondest Love And Kisses From Your Devoted C.". The writer is known only as C.
The tone is a love letter; the recipient's own name is not on the message side.

### Why it stops
Every sign except L3 sign 1 has a reading, but the plaintext words are not recoverable from the letters: H A R R D or T A have many fits, and no key exists to test them against. Stating one expansion as the plaintext would be forcing words on initials, so no DONE1. The other Wooster cards (separate directories, not edited) could firm up the formulae, but not the free body text. Portal says Not solved; no published solution was seen, but I ran no outside search.
