ACCEPT

# Review 1 — HCP 1490 (pc_hcp_171), Pigpen fragments on a postcard to Annie Kepler, 1911

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-30. Role: try to refute the solution.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1490/work/decode.py` (from repo root):
   source hashes OK; literal standard layout gives `(?)ONEY / STNDAY N(I)GHU / ([b])DK`;
   card key (B2=U, BL2=T) gives `(?)ONEY / SUNDAY N(I)GHT / ([b])DK`. Matches SOLUTION.md.
2. **Independent decoder.** `review/work/indep_decode.py` builds the letter from cell index
   (A–I order BR,B,BL,R,C,L,TR,T,TL) + 9 × dot count, from my own token list (made from my
   crops, not from work/transcription.txt). Output:
   standard `?ONEY / STNDAY N#GHU / DK`; with T/U swap `?ONEY / SUNDAY N#GHT / DK`
   (`#` = TL with two dots, index 26, which has no letter — the solver's "I" sign).
   My token list agrees with the solver's on every sign.
3. **Transcription vs. scan.** Crops of `source/address-large.jpg` enlarged 6× and 12×
   with PIL (`review/work/crops.py`, `greet.png`, `body1.png`, `body2.png`, `sig.png`,
   `z_g12.png`, `z_y.png`, `z_i.png`, `z_end.png`). Sign by sign:
   - Greeting: (1) full square with a dark 4-/blob-shaped mark inside — dots not countable,
     correctly left unresolved; (2) top+left+bottom with one short dot/dash inside = O;
     (3) square, one central dot = N; (4) empty square = E; (5) top+right with two dots on
     the left = Y. Agreed.
   - Body: two dots + bottom/right = S; bottom/left/right (U-shape) with two dots;
     square + one dot = N; top/right/bottom (⊐) no dot = D; bottom/right no dot = A;
     top/right with two dots (12× crop: two clear dots left of the stroke) = Y | square +
     dot = N; top/left with **two** dots and a small inverted-V/x stroke beneath; top/right
     no dot = G; top/left/right no dot = H; below the line a bottom/left (∟) with two dots.
     All agreed; the final sign is indeed bottom+left with two dots (12× `z_end.png`).
   - Signature: script "b"/"6", then ⊐ (top/right/bottom, no dot) = D, then a U-shape
     with long left and right upstrokes and one dot inside = K. Agreed.
4. **Key / coverage.** Every pigpen sign is accounted for; no sign was dropped. The
   three-grid dot-count layout (0/1/2 dots) is the same cell order as the accepted sister
   cards HCP 1131/1189/1190 (there with 1/2/3 dots), where B3=T and BL3=U. On this card
   the two two-dot cells B2 and BL2 occur once each and the context needs U and T
   respectively: the swap is disclosed, and both decodings are printed.
5. **Language / context.** "I want to see you at the Party to-morrow night not SUNDAY
   NIGHT be sure and come" is natural 1911 American English; SUNDAY NIGHT is a
   10-letter fit with a word gap at the right place, repeated N (C1) in both words, and
   the Y/G pair sharing the TR cell with 2/0 dots. Address (Middletown, Frederick Co.,
   Md.), postmark 1911 and picture (Gapland, Md., ~10 km from Middletown) agree.
   "Hello ?ONEY" -> HONEY is plausible but, as the solver states, not read.
6. **Sources.** Portal status Not solved, no attached transcription/solution; SOURCES.md
   and SOLUTION.md say no published solution was used. I found nothing contradicting this.
   Credit to the earlier GPT triage is given.

## Findings

1. **minor — overstated count of clean signs.** "Why I believe it is correct" says
   "16 of 19 signs decode under one fixed standard Pigpen layout with no adjustment".
   The non-standard/unresolved signs are C*, B2, BL2, TL2x and [b] (five), so 14 of 19
   decode with no adjustment (or 14 of 18 if the script [b] is not counted as a cipher
   sign). Correct the figure in SOLUTION.md and the report.
2. **minor — HONEY presented without a marker in the translations.** The plaintext section
   correctly gives `[?]ONEY (= HONEY?)`, but the English and Slovak translations say
   "Hello Honey" / „Ahoj zlato" without brackets. Mark it as conjectural there too
   (e.g. "Hello [Honey?]").
3. **minor — the "I" of NIGHT is an unassigned cell, not just an anomalous I.** TL with two
   dots has no letter in the S–Z block (index 26). The solver discloses this; the report
   should state plainly that the I is supplied from the outline and the word, i.e. it is
   a contextual restoration of one letter, like U/T.
4. **minor — "Full message" line of decode.py is hard-coded.** The clear-text part cannot
   be generated from the transcription, which is fine, but the printout should say that
   the clear text is a manual transcription and only the capitals come from the decoder.
5. **minor — partial character.** The greeting's first letter and the signature's first
   sign are unread, so the cipher content is solved except for one letter and one
   (probably clear-script) initial. The register entry/report should describe it as
   "solved, with the first greeting letter unresolved", not as complete.

No blocker or major finding: the body reading SUNDAY NIGHT, ?ONEY and DK are supported
by the pixels and by one consistent key.

## What I could not verify

- The identity of the sender "[b]DK" and whether the "b" is a script initial or a
  malformed pigpen sign.
- Whether the T/U exchange is the writer's grid or two slips (one occurrence each).
- The meaning of the small inverted-V/x mark under the I-cell (correction? stray?).
- The first greeting sign: the inner mark may be an overwrite; neither HONEY nor any
  other word can be read from it.
