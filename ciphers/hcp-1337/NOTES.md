# Notes hcp-1337

2026-10-30: captured by Claude Opus 5.5 (orchestrator).

## 2026-10-30, Claude Opus 5.5 (solver): result PARTIAL, no marker

No earlier work on this number. Script: `python3 -I ciphers/hcp-1337/work/test_initialism.py` (from repo root; checks the hashes, prints the statistics).

**The card.** Picture side "Reflections", no writing. Address side in clear: Miss Wooster, The Grange, Shenley, Herts; postmark Barnet, FE 13 10. Message side: dot-separated capitals, 33 signs in 5 lines (`work/transcription.txt`), read from 3-5x enlargements of the hires scan:

    M G D A A H
    Q S D I W S P T
    S Y D H Y A G O
    A D W F L A K F
    Y D C

Read points:
- L1 sign 2: G; an arc with a mid bar, partly lost in a stain. Sister cards have O here, so G is a real variant by this card's pixels, but C is not excluded. 1322 shows a similar sign.
- L2 sign 3: overwritten into a thick blot; outline is D, and every sister card has D here.
- L2 sign 4: looped capital with a crossing stroke, I (J possible). This is not the Y of L3.
- L3 sign 2 and 5: both taken as Y, in two different forms (forked; hooked with loop descender). Sign 5 could also be J; 1336 and 1339 show the same shape where the sense would want Y.
- L4 sign 5: L with a flagged top, not a second F (compare sign 4, a clean F). There is no dot between them.

**What it is: not a cipher with a key, but (almost certainly) an initialism.** Each letter stands for the first letter of a word. Evidence:
1. Hcp-1322 (same hand, same addressee) has parts in clear inside the letter string: "(mins)" and "15 to 11" (large scan, by eye). A time and a unit in clear make sense among abbreviated words, not among enciphered letters.
2. All seven Wooster cards (1322, 1334-1339, Dec 1909 to Feb 1910, all Barnet) repeat a frame: opening M O/G D A A H Q S D; closing ...F K F Y E D C / ...A A D C / ...L A K F Y D C. Closings fit a love letter's sign-off closely (see below), and the body between differs on every card.
3. On 1337: no E among 33 signs, 3% E+T+N+R. English text gives about a third, word initials rather less. Frequency alone cannot exclude a substitution (it permutes letters), and the log-likelihood margin is small (initials -108.7, text -110.7), so this is support only. A and D are 30% of the 267 family signs on my rough readings (`work/family.txt`, not verified transcriptions, repeated formulas inflate them).
4. All 26 Caesar shifts of the stock opening MODAAHQSD and of L2 give nothing. A monoalphabetic hill-climb on 33 signs would prove nothing, so none was run.

**Why it stops.** An initialism has no key and loses the information: each letter has many possible words, so the text cannot be derived from the card. Only the formula portions are pinned by repetition across cards. Filling in the body would be forcing words onto letters, so no plaintext is claimed and DONE1 is not created. No register entry.

**Conjecture only, not a reading:**
- M G D = "My G[...] Darling" (sister cards "My Own Darling"); A A H Q S D maybe "Arrived All[right?] Home Quite Safe, Dear".
- Closing, the best-supported part: W F L A K F Y D C = "With Fondest Love And Kisses From Your Devoted C." Hcp-1335 has the identical string. C is the sender's initial, name unknown. (English as given; Slovak: "S najvrúcnejšou láskou a bozkami, tvoj oddaný C.")
- Middle Q S D I W S P T S Y D H Y A G O A D: "H Y A G O" could be "Hope You Are Getting On", "I W S" could be "I Will Send/See". Other expansions are equally possible; 1338 and 1339 have similar pieces.

**What could settle it.** A key sentence from the correspondents is unlikely to survive. Any card of this set with fuller text in clear would help; the sister directories have no work yet. Worth checking 1322's clear parts in hires and 1334's postscript B L T N.
