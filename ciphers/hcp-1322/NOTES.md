# Notes hcp-1322

2026-10-30: captured by Claude Opus 5.5 (orchestrator).

## 2026-10-30 — solver pass (Claude Opus 5.5) — PARTIAL, no marker

No earlier work on this number; no published solution found (searched the repo only; portal shows Not solved). The wheel across the scans is the portal watermark. Picture side: printed title BARNET CHURCH, no writing. Address (clear): Miss Wooster, The Grange, Shenley, Herts; postmark Barnet, 6.45 PM(?), DE 27 09.

Transcription (work/transcription.txt, from 3-6x crops of work/hires/pc_hcp_3_adr.JPG), 48 single capitals plus clear text:

    M G D A A H A S D
    A O H T T D M L A (in mins)
    A H A 15 to 11. S I W N M
    L D A W Y M M H B O T D
    F Y E D A A C E M C

Read points:
- L1 sign 2: G, the same open arc with mid bar as hcp-1337 L1 sign 2 (compared directly). Could look like a 6, but no digits sit among the letters except the time.
- L1 sign 7: A, a round lower-case-form a. It is NOT the Q of the sisters at this place (hcp-1337 has a clear Q with a stem tail), so this card really differs: M G D A A H A S D against M O/G D A A H Q S D.
- L2 clear words: "(in mins)" is the best reading; the stems are run together and "(mins)" with a stray stroke is possible. Dot over the first stem is clear. Reading of the words is not secure.
- L3 signs after the time: both are long looped signs. Taken as S then I, matching S and I on 1337 (L2 signs 2 and 4), but S/I/J cannot be firmly split here. The 1337 forms are also similar to each other.
- L4 signs 6-7: two M with no dot between; sign 5 is Y with a crossing stroke (T not excluded).
- L5 second A of "A A" is overwritten into a heavy blot; outline is A. The text ends with a short dash after C, nothing lost.

What it is: an initial-letter abbreviation, the same writing as the other Wooster cards, not a keyed cipher. Evidence: `python3 -I ciphers/hcp-1322/work/compare.py` (repo root; checks hashes; reads sister transcriptions read-only): shared opening with every sister (MGDAAH with 1337, DAAH with the rest), shared closing FYE / FYED (with 1334, 1336, 1338), SDAO with 1334; 2 E in 48 signs. Clear time "15 to 11" and "(in mins)" among the letters cannot be part of a letter substitution of running text. This is the earliest dated card of the set (27 Dec 1909; others Jan-Feb 1910).

Why it stops: one letter per word does not determine the word and no key exists; the body of this card is unique, so a full plaintext would be forcing words onto letters. No SOLUTION.md, no DONE1, no register entry.

Conjecture only, NOT a reading:
- M G D = My G... Darling. A A H ... S D: unknown, sisters have Q where this card has A.
- A H A 15 to 11: some arrival or meeting at 10:45; the time is the only fact stated in clear. Whether morning or evening is not given.
- M M H B O T D: "Many Many Happy ... Of The Day" fits the season but B is open, and H R ("Happy Returns") is not what is written.
- F Y E D A A C: From Your Ever Devoted And Affectionate C (the sisters' sign-off with C the sender's initial). E M C after it is unexplained; C E M C may be the sender's full initials or another formula. Do not treat any of this as settled.

What could settle it: a clear-text letter of the correspondence or a named sender. Further pixel work on this card cannot.
