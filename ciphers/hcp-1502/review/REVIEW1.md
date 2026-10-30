ACCEPT

# Review 1 - HCP 1502 (pc_hcp_183), Morse love letter to "Nell", 10 May 1911

Reviewer: Claude Opus 5.5, 2026-10-30. Review files: `review/work/`.

## What I verified and how

1. **The solver's command.** `python3 ciphers/hcp-1502/work/decode.py` (from the repo root)
   checks the source hashes and prints exactly the plaintext claimed in SOLUTION.md
   (P.S. "SAVE ME ONE FOR SUNDAY I AM READY FOR ONE NOW NELL"; main letter "DEAR NELL ...
   YOURS GEORGI"), 233 letters. Source hashes OK.
2. **Independent decoder.** `review/work/mydecode.py` (own Morse table, written separately)
   decodes `work/transcription.txt` row by row: same text, 233 letters, no invalid group.
   Every row ends on a letter or word boundary that fits the words split over rows
   (SUND|AY, KIL|LING, Y|OURSELF, USU|AL, JUST A L|INE).
3. **Independent reading of the pixels.** `review/work/trace.py` + `rows.py` extract ink
   components from `source/address-large.jpg` (threshold 160), chain them into sloping rows
   and classify marks by length only (point <=4 px, dot <=17 px, dash longer, blot = thick
   short mark), then decode with no word knowledge. This crude machine read gives, among
   others: "ONE", "FOR", "I", "AS USU", "KIL", "OURSELF", "THIS WEE..", "ITS GRA..",
   "SWEETHEART", "IT SEE.S SU..H", "DEAREST TILL I SEE" (as DEAAEST), "OU WITH A.L",
   "LOVE ..ISES", "..ORGI". The errors are all of the expected kind (long dots counted as
   dashes, missed faint points); no row contradicts the solver's reading. The row
   structure (rows slope steeply down to the right, about 30 px over the card width) was
   checked: the row starting at y 606 is the one carrying "& KISSES" and ending at x 876,
   y 640; the YOU WITH ALL row ends at x 870, y 632.
4. **Visual checks on enlarged crops (5-6x)** of: A050 (SAVE: `... .- ...- .` + blot -
   clear), A064 (ME ONE), A135 (AM READY, the broken second dash of M), B222 (DEAR NELL,
   with a pixel profile across x 312-480), B265/B280 (AL / HOPE, YOU), B375 (ITS GRAND),
   B593 tail (ALL: the heavy mark at x 693-702 is the first dot of L, not a blot, which the
   solver read correctly), B607 tail (& KISSES, mark by mark with coordinates), B632
   (GEORGI).
   - DEAR NELL: profile shows N = dash 322-346, dot 351-356, point 361; E = 371-379; the
     cursive "1" of the date at 382-388 sits where the letter-end point should be;
     L = 393-398, 403-425, 433-437, 442-445, point 448; second L starts at the blob on the
     printed vertical line (453-460). Matches the solver's description.
   - KISSES: dash 612-633, point-sized dot 637-640, dash 643-666, point 671 (K);
     679-686 + broken 689-695, point 701 (I); 711-715, 722-730, 734-743, point 750 (S);
     760-766, 773-779, 782-792, point 798 (S); 805-814, point 819 (E); 828-835, 841-846,
     853-859, blot 868-876 (S). Reading confirmed.
   - ITS: the two I strokes are about half the length of the T dash that follows; reading
     `..` is supported by the pixels as well as by the sense.
   - GEORGI: `--.` (first dash short and faint), `.`, `---`, `.-.`, `--.`, `..`, then a
     word-end blot at about x 400-407; nothing else follows on that row before the card
     edge.
5. **Key / coverage.** Plain International Morse, no extra layer; every mark I sampled
   is accounted for; nothing on the address side outside the two blocks looks like
   unread Morse.
6. **Language and context.** Fluent, idiomatic English of the period ("just a line as
   usual", "it's grand weather for the job", "so long, dearest"); consistent with the
   card (cursive date "May 10th 1911", Gilberdyke R.S.O. postmarks MY 11 11, halfpenny
   Edward VII stamp, Miss O. Davy, Gilberdyke, E. Yorks). The P.S. ties in with the
   letter's "longing for Sunday".
7. **Sources / credit.** Portal status "Not solved", no attached solution; the GPT solver
   only did triage (as NOTES.md and SOLUTION.md say). No published solution found or used.

## Findings

1. **minor - signature row description.** SOLUTION.md (uncertainty 6) says "Nothing
   follows the final `..` before the card edge". In fact a word-end blot follows at about
   x 400-407, y 638 (crop `review/work/end1.png`). This does not change the reading (it
   confirms GEORGI ends there as a complete word), but the sentence should say so. The
   literal GEORGI (not "Georgie") is correctly kept unrestored.
2. **minor - the transcription does not mark the non-standard marks.** The heavy first dot
   of the second L of ALL (x 693-702, looks like a blot), the point-sized K dot, the
   broken M dash and the long I dots are only explained in prose; `transcription.txt`
   gives no row-level flag. Acceptable, but a short comment next to rows A135, B222,
   B375, B593, B607 would make the claim easier to check.
3. **minor - "Nell" vs Miss O. Davy.** Correctly left open. Note for the report that
   "Nell" may simply be a pet name; nothing on the card links it to the initial O.
4. **minor - row labels.** The labels give the y of the row's left end; because rows slope
   by about 30 px across the card, the right-hand halves of B593/B607 lie at y 620-640,
   among the left ends of B619/B632. Worth one sentence in the report so a reader can find
   the marks.

## What I could not verify

- I did not re-read every one of the 32 rows mark by mark; I checked about a third of them
  visually and the rest only through the crude machine read, which agrees but is noisy.
- Identity of the writer "Georgi(e)" and of Nell / Miss O. Davy; no genealogical lookup.
- Only the portal scan (1024x674) was available; no higher-resolution original.
