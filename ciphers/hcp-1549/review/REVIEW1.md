REVISE

# Review 1 – hcp-1549 (pc_hcp_230), Czech card to Anna Tichá, 2 Jul 1903

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-29. Role: reviewer, round 1.

## Summary

The identification stands: this is the Anna Tichá / "P." family homophone-free
substitution (digits for vowels, swapped consonant pairs, ř/tilde-r for CH), and
the key in `work/key.json` is identical to `ciphers/hcp-1520/work/key.json` and
equivalent to `ciphers/hcp-1545/work/key.json` (label `y` = `7` for J, `H` = `ř`
for CH). The message is coherent period Czech and the overall reading is right.

However, my sign-by-sign check of the scan found **several ordinary-row words that
the transcription renders as the expected Czech word, not as what is on the card**
(ZVASTE, KTERE, SICE, AČ, DU), and the four "literal anomalies" the solver
proposes editorial repairs for are, in three cases, artefacts of the solver's own
misreadings. In addition the single reproduction command does not produce the
plaintext that the "Completion" section claims. The reading stands; concrete
fixes are required.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1549/work/decode.py` (from repo
   root) exits 0, prints the literal base reading identical to `work/literal.txt`,
   with `[UNK:U1]`, `[H|CH]`, `[R|H]` still present and the counts 838 known units,
   7 CH, 2 bounded alternatives, 1 unknown region.
2. **Independent decoder.** `review/work/indep_decode.py` (own code, key typed from
   the hcp-1545 family key, H = CH, y = 7 = J) applied to the rows of
   `work/transcription.json`: output `review/work/indep_out.txt` is identical to
   `work/literal.txt` once the uncertainty tags are renamed. Every token maps; no
   unmapped label. So key and record are self-consistent and the whole record is
   covered.
3. **Key.** `diff` of key.json vs hcp-1520 key: identical. Matches hcp-1545.
4. **Scan check.** `review/work/crop.py`, `rot.py`, `segs.py` (PIL, run with -I)
   produced 4–12x crops of `source/picture.jpg`: every main row in four segments
   (`review/work/seg_T01…B05.png`), the left addition rotated
   (`left_top.png`, `left_bot.png`), the right addition (`right.png`), and focused
   crops of U1, A1, A2 and each "anomaly". L01–L11 and R01–R03 match the
   transcription glyph for glyph; T01, T02, T05, B02 and most of B03/B04 match.
   Discrepancies are listed below.
5. **Provenance.** SOURCES.md and SOLUTION.md credit the earlier family cards and
   Maxim Egorov's published partial study/key; no plaintext for this card is
   claimed from elsewhere. Earlier GPT solver work and the Claude completion are
   both labelled.

## Findings

1. **[major] T03 "VASTE" is a misread: a glyph is dropped; the card has `9f6cd5`
   = ZVASTE (→ *zvláště*, with L omitted by the writer).**
   Evidence: `review/work/t3vaste.png` (7x). Before `f6cd5` there is a clear
   `9`-shaped glyph with left-curling descender, the same shape as `q` (Z) in
   the immediately following `95` (ZE) (`review/work/t3after.png`). The record
   `y5 n4 f6cd5 84d3` omits it. "Je mi zvláště líto" (*I am especially sorry*)
   fits perfectly after "Je mi nevýslovně líto". The editorial repair "vážně?"
   is therefore wrong and must be replaced; the literal is ZVASTE (writer omitted
   L), and the known-unit count rises by one.

2. **[major] T04 "KTERO" is a misread: the card has `gd5h5` = KTERE.**
   Evidence: `review/work/t4ktero2.png` (10x): the last glyph has the same flagged
   top as the `5` two places earlier, not the flat `3`. *dívku, které si nade vše
   vážím* is correct Czech (vážit si + genitive). The "anomaly" and the editorial
   "kterou?" both disappear.

3. **[major] B01 "SNAD" (`cm6t`) is not what is written: the card has `c4s5` =
   SICE.** Evidence: `review/work/b01snad.png` (7x): four glyphs, `c`, a crossed
   `4`-type stroke (cf. `d4n` immediately after), the small `s` (C) glyph seen in
   `f2p5s` VUBEC, and a final flagged `5`. There is no `6` and no `t`. *a to sice
   tím spíše* is good period Czech. This is a word supplied from expectation,
   not read.

4. **[major] B04 "AS" (`6c`) is a misread: the card has `6s` = AČ.**
   Evidence: `review/work/b4as2.png` (8x) vs `review/work/t4vubec.png`: the second
   glyph is the `s` (C) shape of VUBEC, clearly different from the `c` (S) in the
   following `c5` (SE). *ač bude-li se chtíti nyní Anunka ještě se mnou sejíti* is
   correct archaic Czech ("if indeed…"). The editorial repair "až?" is wrong.

5. **[major] The single command does not produce the claimed plaintext.** The
   "Completion and handover" section claims DOKONCE, CHTEL and ZARMOUCENEHO, and
   status "complete reading", but `decode.py`, `transcription.json` and
   `literal.txt` still output `[UNK:U1]`, `[H|CH]TEL`, `ZA[R|H]MOUCENEHO`, and the
   top of SOLUTION.md still says "not a complete … decipherment". README step 4
   requires one command that yields the full plaintext. Update the record (with the
   restorations explicitly marked), the counts and the status text so that the
   file is internally consistent.

6. **[minor] B04 `d2` "TU" is literally `t2` = DU on the card.** Evidence:
   `review/work/b4tu2.png` (12x): the first glyph is the bowl-less crossed `t`
   (D) of `t3cd683` DOSTALO, not the bowled `d` (T) of CHTITI in the same row
   (`b4ch2.png`). Record it literally as DU and note the writer's T/D slip
   (*tu*), rather than silently normalising.

7. **[minor] B03 RUZNEHO: the H is written with the tall looped `h` (= R)
   shape.** Evidence: `review/work/b3ruz2.png` (12x) vs short `r` in `r3` of
   TAKOVEHO (T01) and SVEHO (L09). Literal is probably RUZNERO; record it or
   mark it as an uncertain sign, with *různého* as the editorial form.

8. **[minor] A2 / CHTEL: there is no CH mark at all.** `review/work/b2ch.png`:
   `rd58` has a plain `r`, while MODERNICH in the same row and CHTEL (T01) /
   CHTITI (B04) carry a clear tilde. The literal is HTEL; CHTEL is a correct
   editorial repair of an omitted tilde, and should be presented as such (not as
   "ownership of cap/mark uncertain", and not as a glyph reading).

9. **[minor] A1 ZARMOUCENEHO is supported by the pixels.** `review/work/l09b.png`:
   despite overinking and a crossing stem, the glyph has the tall looped ascender
   of `h` (R), unlike the short `r` (H) of SVEHO in the same row. The solver's
   justification is only linguistic; cite the shape instead.

10. **[minor] U1 DOKONCE is a plausible restoration, not a reading, and should be
    marked as such.** `review/work/u1b.png` (6x): `6 [blot] [heavy 3] g 3 m
    [blot] 5`. Positions 3–5 and 7 (K O N … E) are plain; position 2 is heavily
    overinked but O-shaped; positions 1 and 6 are blots whose outlines are
    compatible with `t` (D) and `s` (C) but do not prove them (the sixth blot
    has a descender the normal `s` lacks). "5 of 7 plain" overstates it
    (4 plain + 1 overinked). Keep DOKONCE but bracket D and C as restored in the
    plaintext and translation.

11. **[minor] L05 "SO": a faint mark sits above the `3` of `c3`.** `review/work/
    l05b.png`. It may be a correction toward `5` (SE). Mention it; the editorial
    *se* is fine.

12. **[minor] Presentation.** SOLUTION.md is cluttered with helper/"Root
    should…" process notes and superseded counts (836/838) that contradict each
    other; the report must be written for an outside reader. The left-addition
    "MNE NEJENOM BAVILO" is genuinely written `p6f483` (checked) – keeping it as
    literal is correct.

## Consequences for the text

Corrected literal readings: JE MI ZVASTE LITO (*zvláště*), …DIVKU, KTERE SI NADE
VSE VAZIM…, …A TO SICE TIM SPISE…, …ROZPRAVU DU (*tu*) AZ K OSOBNIMU SETKANI, AC
BUDE-LI SE CHTITI…, TAK RUZNE[R?]O. The Czech and Slovak editorial texts must be
updated accordingly (*zvláště / zvlášť*, *které*, *sice*, *ač*).

## What I could not verify

- Only the 1024-px portal image is available; very small diacritic-like marks
  (L05, U1) cannot be resolved further.
- The original glyphs under the two U1 blots are not recoverable from this scan.
- I did not compare q/g shapes exhaustively on every Z/K; the solver's
  assignments in PONEVADZ, URAZEL, VAZIM, ZNAM were accepted on context plus
  family convention and look consistent at 4x.
- Identity of "P." and the brother's maturita are not checked beyond the card.
