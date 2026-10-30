ACCEPT

# Review 1 — hcp-1476 (pc_hcp_157), Pigpen closing on postcard to W. Pooley, 1907-10-24

Reviewer: Claude Opus 5.5, 2026-10-29. Claimed reading: MY OWN DARLING, SWEETHEART.

## What I verified and how

1. **Solver command.** `python3 ciphers/hcp-1476/work/decode.py` from the repo root passes the
   source hash checks and prints `MYOWN` / `DARLING,/SWEETHEART` / `[UNINTERPRETED END MARK ...]`.
   The 22 letters match the claimed plaintext.
2. **Independent decoder.** `review/work/own_decode.py` uses its own encoding of the glyphs (sides
   drawn plus dot, and which way each X-grid wedge points). I wrote it from my own reading of the crops, not
   from `work/transcription.txt`. Output: `MYOWN` / `DARLINGSWEETHEART`, 22 glyphs. This is the same as the solver's output.
3. **Transcription against the scan.** I rotated `source/address-large.jpg` 90° clockwise
   (`review/work/upright-own.png`) and enlarged every cipher glyph 8–16× (`line1*.png`, `l2-*.png`,
   `sw.png`, `eth.png`, `own.png`, `w2.png`, `a1.png`, `t1.png`, `rt-end.png`, `endmark-color.png`).
   Sign by sign:
   - Line 1: `7`=M (TR), `Λ`=Y (wedge pointing up), then a comma, `Π`=O (TLR), a wedge (see F1), `7` with a dot=N. Correct
     apart from F1 and the omitted comma (F4).
   - Line 2: `⊔·`=D, `┘`=A (no dot; I checked at 14×), `Γ·`=R, `[·`=L, `□`=I, `7·`=N, `コ`=G, comma,
     `V`=S, `<`=W (partly overlaid by the descender of the cursive line above, but the vertex is on the left), `L`=E, `L`=E,
     wedge pointing down=T (dot unclear, see F2), `Z`-shaped TRB with a clear dot=H, `L`=E, `┘`=A, `Γ·`=R, V with a dot=T.
     All correct.
4. **Key and coverage.** The standard interleaved Pigpen key (A/B … Y/Z) explains all 22 glyphs. No glyph is left over, and
   no letter needs a second key. The text has no U/V or X, so the assignment of the left and right wedges (`>`=U/V, `<`=W/X)
   is supported only by the W in SWEETHEART. The key is still the standard one.
5. **Language and context.** "My own darling, sweetheart" is natural English of 1907. It fits its place right after the
   cursive "Bye Bye" on an English card (Laycock? postmark, 24 Oct, King Edward ½d stamp). The catalogue gives the language as "Unknown",
   but the solver correctly establishes English.
6. **End mark.** In `review/work/endmark-color.png` the mark is `—{•}—`: a symmetric shape with tapered ends, crisp, in
   jet-black ink. I measured the darkest-20-pixel mean (lower = darker): end mark 83, printed divider rule 83,
   printed card text 72. The handwritten cipher glyphs measure 97–103 and the cursive 116. The mark sits by the printed
   double divider rule, next to the printed "This space may be used for written or printed matter" legend. See F3.
7. **Published solution.** The portal attachments contain no solution. SOURCES.md and SOLUTION.md say so. I found nothing suggesting an
   undisclosed source.

## Findings

**F1 (minor): line-1 glyph 4 (the W of OWN) is not drawn as `<`.** In `review/work/own.png` it is a
`7`-like acute angle. Its vertex is at the upper right, and its arms run left and down-left. A small separate tick sits above it on the right.
Read literally under the key, a wedge with its vertex on the right is `>` = U/V, which gives "MY OUN". The W in
SWEETHEART (`w2.png`) is drawn correctly as `<`. The reading OWN is not in doubt, since no other reading makes sense. However, the
transcription records the glyph as `<0` without comment, and SOLUTION.md says all 22 letters "follow the
standard key". The solver should disclose that this glyph is malformed or drawn the wrong way round and is read as W from context. The solver should also say
that the tick is treated as a stray stroke, not a dot (a dot would give X).

**F2 (minor): the dot on the first T of SWEETHEART is not certain.** In `eth.png`/`t1.png` the
place where the dot would be is covered by the loop of a cursive descender from the line above. Without the dot the glyph would read S
("SWEESHEART"). Context settles it, but the uncertainty should be listed.

**F3 (minor): the end mark is most likely printed on the card, not written by the sender.** Its ink density matches the
printed rule and text, not the handwriting (see item 6 above). Its symmetric, tapered form is typographic. It also sits next to the printed
divider. The solver's conclusion (not a letter, and the cipher text is complete) is correct. The explanation, "a
decorative full stop or flourish closing the message", should be changed to "probably a printed ornament of the
card's divider", with the evidence given.

**F4 (minor): documentation is inconsistent.**
- `decode.py` still prints `[UNINTERPRETED END MARK ...]` and "1 nonstandard end mark remains uninterpreted",
  and the SOLUTION.md title still says "end mark unresolved". The 2026-10-29 completion section declares the
  reading complete.
- Earlier sections say "no DONE1/FINAL/register entry", which is no longer the state.
- The transcription leaves out the visible comma after MY (`Λ ,`), although it keeps the comma after DARLING.
- The text has many run-together tokens ("on2026-10-26", "All22", "all4sides").
- Credit should be explicit: the 22-letter reading is the GPT solver's work from 2026-10-26, and the end-mark completion is Claude Opus 5.5's from 2026-10-29.
  SOLUTION.md implies this but does not name the earlier model.

## What I could not verify

- I could not see the original card. In particular, I could not confirm under raking light or at higher resolution that the end mark is printed. That conclusion rests on
  ink density, form and position in a JPEG.
- The recipient W. Pooley and the "Charlie" of the message are not historically identified. Nothing in the reading depends on
  them.

## Verdict

ACCEPT. All 22 glyphs decode independently to MY OWN DARLING, SWEETHEART under the standard Pigpen key. The
transcription is correct apart from one malformed W, and the end mark is not cipher text. F1–F4 are disclosure and wording fixes that the solver should make
in the response to this review before FINAL. None of them changes the reading.
