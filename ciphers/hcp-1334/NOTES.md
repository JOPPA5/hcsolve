# Notes hcp-1334

2026-10-30: captured by Claude Opus 5.5 (orchestrator).

## 2026-10-30 Claude Opus 5.5 (solver): partial, no marker

Result: the letters are read, the cipher class is identified, but the message cannot be recovered uniquely. Picture side (A Sylvan Scene) has no writing. Postmark [BARNET] 9 AM JA 31 10, a Monday. To Miss Wooster, The Grange, Shenley, Herts; the address is plain.

Transcription (45 capitals, each followed by a stop; work/transcription.txt, from work/hires at 3-6x, crops in work/crops/):
M O D A A H Q / S D A O L W T D D / D E M W Y D H Y W / G O A D W E L T A / F K F Y E D C // set apart at the foot: B L T N

Sign calls to recheck:
- Line 1 sign 4, A: heavy stem and bar with a hairline left stroke. Same slot is A on the six sister cards.
- Line 2 sign 9, D: retraced or corrected with a blot and an upper flourish; an earlier letter may lie under it.
- Line 3 sign 2, E: looped script form with a bar and a C-like base. Not this correspondence's L (compare hcp-1338/1339 line 4), but less certain than the block E's.
- Line 3 signs 4 and 9, W: both show stem, return to mid-height, second down stroke, long rising tail, as the W of lines 2 and 4 and unlike the clean three-stroke N of B L T N. Sign 4 is partly swamped by heavy ink, so N is not excluded there. Sign 9 is the firmer W, and it agrees with H Y W G O D D on hcp-1339.
- Line 4 sign 1, G: the looped, descending script G of this writer, not Y; Y is always block.
- Line 5 sign 3, F: pale but clear.

Cipher class: initialism (first letter of each word), no substitution. Evidence:
1. Every capital is stopped individually, with no word grouping.
2. All seven cards (1322, 1334 to 1339; 27 Dec 1909 to 13 Feb 1910) open M O D A A H Q S D and end with F Y ... D C or F Y E ... C; closes vary by small steps (W E L T A F K / W F L A K). The stable frame sits exactly where a love letter has its salutation and valediction.
3. Hcp-1322 has plain insertions: 15 to 11, and a bracketed note (rough preview reading "in ms"). The clear time inside the capitals suggests abbreviation for privacy, not a cipher alphabet.
4. work/check.py: pooled rough readings give E 4.2%, vowels 26.8% (ordinary English about 12.7% and 38%). Under a word-initial frequency model shift 0 is best of 26. This statistic is weak: only 45 letters on this card, where a running-text model scores slightly better, and the pool repeats the frame. The sister readings are rough previews used for this test only. Points 1 to 3 carry the argument.
Same class as accepted hcp-1475 (ILMWAMWLM), but that card is nine letters forming one self-evident sentence.

Conjectural frame (NOT a reading; other wordings fit):
- M O D A: My Own Darling A[...]; A may be the addressee's initial.
- H Y W G O A D: Hope You Will Get On Alright, Dear/Darling. Sisters 1337/1338 have H Y A G O A D (Hope You Are Getting On...), and 1339 H Y W G O D D. The A/W alternation with fixed G O is the best internal evidence for initials.
- W E L T A F K F Y E D C: With E... Love T... A... F... Kisses From Your Ever Devoted C.; compare W F L A K F Y D C (With Fondest Love And Kisses From Your Devoted C.) on 1335/1337.
- C: writer's initial, not expanded.

Why it stops: the middle A H Q S D A O L W T D D D E M W Y D and the foot B L T N have no constraint. Each letter allows many words and no sister card contains a key or expansion, so any sentence offered would be invented. No SOLUTION.md and no DONE1: the task forbids forcing words. A reader who knows the couple, or a card in the same hand with a plain parallel, is what would move this.

Published solution: none found (repo search, one web search for the addressee; portal has none attached). Shared caveat for the Wooster set: an expansion of any one card should be proposed across all seven together.
Check: python3 -I ciphers/hcp-1334/work/check.py (from repo root; verifies source hashes, prints capitals and statistics; gives no plaintext).
