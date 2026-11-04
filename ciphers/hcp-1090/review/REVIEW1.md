ACCEPT

# hcp-1090 – Review round 1

Reviewer: Claude Opus 5.5, 2026-11-03. Solution under review: SOLUTION.md (round 1, Claude Opus 5.5).

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1090/work/decode.py` (repo root): all four SHA-256
   hashes OK; output equals the claimed literal stream and edited plaintext in SOLUTION.md word for word.
2. **Independent reading of the pixels.** `review/work/strips.py` crops the Morse half of the hi-res
   address scan (x 0–1560) and rotates it 90° anticlockwise (`review/work/rot.png`), so the writer's lines
   become horizontal rows, rightmost column = top row. I read all 16 rows mark by mark from the strips
   `review/work/r0*_*.png` (overlapping 1250 px windows) and enlarged 3–5x every doubtful group with
   `review/work/crop.py` (z_*.png). I typed my own transcription into `review/work/my_decode.py`, which
   decodes with **standard** international/German Morse (no writer-specific values):

   ```
   LIEBERERNST / WIEGE5TESDIR / OWÄRESTDU / DOCH5IERWIE / SCHÖNWARES / VORVIERZE5N / TAGENUNDJET /
   ZTISTESMIRS / OLANGWEIL / IGKOMMEBA / LDICHFREUEMICH / SOSE5RAUFDA / SWIEDERSE5EN /
   ICHGR(u)5SEDICH / 5ERZLICHDEINE / ANNA
   ```

   My mark sequence is identical to work/transcription.txt in all 16 columns. The only difference
   from the solver's plaintext is that `.....` decodes as the digit 5 in standard Morse; replacing it by H
   gives exactly the solver's text.
3. **Reading order** confirmed independently: rows read top-to-bottom / left-to-right in the rotated view
   give continuous German, with words running across row ends (JET|ZT, S|O, LANGWEIL|IG, BA|LD, DA|S).
4. **Spot checks on enlargements** (all confirmed):
   - five-dot H in GEHT (z_r2h.png), HIER, VIERZEHN (inside the grey loop, z_loop1.png: exactly 5 dots,
     followed by `-.` N), SEHR, WIEDERSEHEN, HERZLICH (z_herz.png: 5 dots, E, `.-.`).
   - c05 insertion loop (z_loop2.png): 4 short dashes = CH, between `..` (I) and `..-.` (F).
   - G of TAGEN (z_g.png): long dash whose right end is a heavy blot, no gap, then a dash and a dot:
     `--.`. A split into `-.` `-.` (TANNEN) would need a gap that is not there.
   - MICH (z_mich.png): four dashes at the card edge, the fourth lower and short – CH.
   - DICH (z_logo.png): four dashes running through the printed publisher logo "9389" – CH.
   - ANNA (z_anna.png): `.-  -.  -.  .-`, letter gaps (≈40–47 px) only slightly larger than the
     A-inner gap; ANNA is the only natural split.
   - Grey letter in GR_SSE (z_mark2.png): in writing orientation a Kurrent u (sawtooth) with a curl
     above (the u-hook), in lighter ink than the Morse; then 5 dots, gap ~80 px, 3 dots, 1 dot.
5. **Date note** (z_date.png): "31. III. 11. ab. 9 U…" – read as the solver says; agrees with the
   postmark Oppenau 1.4.11.
6. **Picture side** (source/picture-large.jpg): Titisee view, no handwriting or hidden marks visible.
   **Stamp box** (z_stamp.png): Germania 5 Pf. intact, no writing visible around or along its edges;
   under the stamp cannot be examined from the scans.
7. **Coverage**: every Morse mark on the address side is accounted for; no leftover groups. Key =
   standard German Morse with the writer's five-dot H; no free parameters.
8. **Language and context**: idiomatic German of c. 1911 (O wärest du doch hier; vor vierzehn Tagen;
   ich freue mich so sehr auf das Wiedersehen); names and places (Ernst Häusler, Göggingen, Amt
   Meßkirch, Oppenau, Titisee – all Baden) fit. Translations (EN, SK) are faithful.
9. Not in skip.txt, not in register-exclusions.json; no published solution of this card was found by
   the solver and none is used.

## Findings

1. **minor – nature of the five-dot sign not stated.** `.....` is the standard Morse sign for the digit 5,
   not an invented sign. SOLUTION.md should say so ("the writer used the sign for 5 in place of H `....`,
   consistently, 6 times + once in GR_SSE"). This also explains the GRüHSE group: the writer's "H" is
   really his/her sign 5, so the literal stream is GR(u)5SE.
2. **minor – the grey letter is u, not ü, on the pixels.** The mark above the zigzag is a single curl
   (Kurrent u-hook), not two umlaut dots. The literal stream should then read GRuHSE (or note that ü is
   inferred: Kurrent ü is often written with the hook alone). The emendation GRÜSSE stands on sense, as
   disclosed.
3. **minor – undisclosed stray speck.** Before the five-dot H of GEHT there is a tiny faint speck
   (≈ 1/5 the size of a dot, rotated x ≈ 1090, z_r2h.png). Correctly ignored, but "every Morse mark is
   used" should mention that it was judged a pen touch; counting it would give six dots.
4. **minor – stamp.** In line with the collector's remark that cards in some series carry a message under
   the stamp, the report should say plainly that under the stamp could not be examined (already in
   uncertainty 7) and that nothing is visible around its edges.

No blocker or major issue: the reading is correct and complete; the single emendation (GRÜSSE) and the
other judgement calls (TAGEN blot, ANNA split, R of DIR placement) are disclosed.

Register: `MASC/Morse` is an allowed label for this card; the card is complete (no unread word or
clause), so an entry is appropriate after the minor fixes.

## What I could not verify

- Whatever may lie under the stamp (not visible on the scans).
- The ink colour/timing of the grey insertions (scan is near-greyscale); I accept that the loops and the
  Kurrent u are later additions by the same writer only on their position and lighter tone.
- The sender's identity beyond the signature "Anna".
