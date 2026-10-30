ACCEPT

# Review 1 — hcp-1480 (pc_hcp_161), reviewer Claude Opus 5.5, 2026-10-30

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1480/work/decode.py` (from repo root):
   the source hashes pass, it prints "61 signs, all mapped", and the plaintext matches
   SOLUTION.md word for word:
   `DEAREST ID / JUST A CARD / WITH LOVE AND / KISSES EVER / YOURS MY DEAREST / IDIE / WILL`.
2. **Independent decode.** I wrote my own transcription
   (`review/work/my_transcription.txt`, with my own labels made from the enlarged crops and
   not copied from the solver's legend) and my own decoder (`review/work/my_decode.py`).
   Output: `review/work/my_output.txt`. I diffed it against the solver's output
   (`review/work/solver_output.txt`), and the two are IDENTICAL. Counts: 61 signs, 20 shape
   classes, 19 letters. In my transcription the only merge is the O variant (dotted <). I see
   BOX/BOX_BAR, BAR/SLANT_BAR and DIV/CURVED_BAR_TWO_DOTS as the same sign drawn by hand, so I
   did not split them.
3. **Transcription vs scan.** I made autocontrast crops of every line at 4x
   (`review/work/r1..r5.png`) and of the critical groups at 8x
   (`mygroup.png`, `yo.png`, `idie.png`, `will.png`, `and.png`, `card.png`), all from
   `source/address-large.jpg`. I read every sign of every line. Each one agrees with the
   solver's transcription.
   - **The Claude-round restorations, judged on the pixels:**
     - *HOOK -> ARCH (Y):* `mygroup.png` at 8x shows the 2nd sign of the 2-sign group. It has a
       faint but clearly visible rounded upper arc that runs from the left foot to the right leg,
       and a dark base with a downward right tick. This is the same construction as the first
       sign of YOURS (`yo.png`). The merge is supported by the pixels and was not forced.
     - *BAR_LOWER_MARK -> T_STEM (M):* a dark top bar, a faint vertical stem below it, and a
       dark foot at the bottom. Together they form one T-shaped sign. It is clearly not the plain
       BAR (L) seen in LOVE and WILL. The pixels support the shape. Its value M rests only on
       context (singleton), and the solver discloses this.
     - *DOTTED_C (O):* `yo.png` shows a dot above a "<" with a long flat lower stroke. It is not
       the ÷ R sign, because there is no lower dot and the stroke is angled. The O reading is the
       only one that gives a word (YOURS). The stray dot is disclosed.
   - **Ordinary rows sampled:** DEAREST ID, JUST A CARD, WITH LOVE AND, KISSES EVER,
     IDIE, WILL all read cleanly, and repeated signs are drawn consistently.
4. **Key consistency and coverage.** Every one of the 61 signs is mapped, no sign class gets
   two letters, and no letter is served by two unrelated shapes (apart from the disclosed
   variant merges). I recomputed the repeat counts from my own transcription (E x9, S x7,
   D x6, I x6, …), and they agree with SOLUTION.md.
5. **Language and context.** The text is idiomatic Edwardian English postcard phrasing ("just a
   card with love and kisses, ever yours"). "Dearest Id … my dearest Idie" repeats one pet
   name, which an imposed reading on noise would be unlikely to produce. The English text
   fits the Swanage, Dorset address and the 1910 postmark. The solver keeps the names as
   enciphered and does not claim an identity.
6. **Sources.** The portal shows "Not solved" with no attached solution, and the orchestrator
   checked the AI register. The solver credits the earlier work truthfully: GPT
   (2026-10-26) did the transcription, the bulk of the key and the main reading, and Claude
   (2026-10-29) resolved the last 4 positions. I found no use of a published solution.

## Findings

1. **minor:** The values of the singletons C, H, J, K, M, N and of Y (x2) rest only on word
   context. SOLUTION.md already discloses this. The reading leaves no plausible alternative
   (JUST, CARD, WITH, KISSES, AND, YOURS MY), so this is not a defect. The report should keep
   the disclosure.
2. **minor:** `work/transcription-legend.md` still carries the superseded descriptions of
   HOOK, CURVED_DIV and BAR_LOWER_MARK in its earlier sections. Later notes correct them, but a
   reader of the legend alone could be confused. Mark those sections as superseded, or state
   the current label set at the top.
3. **minor:** `source/metadata.md` records the portal's Language as "Unknown" and Sender as
   "Unknown". The report should state that the language established is English, and that the
   signature reads "Will" while the sender's identity remains unknown.
4. **minor (presentation):** The signs look like a home-made scheme in which vowels take
   simple shapes (A circle, E square, I cross, O angle, U cup). It is not a Pigpen variant.
   Calling it "ad-hoc geometric MASC" (as in SOLUTION) is right. The register `type` should be
   MASC.

## What I could not verify

- Who "Will" and "Id/Idie" were, and how they relate to Mrs Light at Swanage Police Station.
- Whether the dot over the line-5 O has any meaning. It does not affect the reading.
- I had only the portal JPEGs (1024 px). The faint strokes of the T_STEM and the second ARCH
  sit at the limit of that resolution, but both are visible.
