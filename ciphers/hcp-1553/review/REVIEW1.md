REVISE

# Review 1 — HCP1553 (pc_hcp_234), Czech love postcard, Pepouš to Anna Tichá, 25 May 1903

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-29. Role: reviewer, round 1.

Summary: the family key and most of the reading are right, and the three
completions (G, the dash, DESET) hold up. But the transcription of the last two
rows has two wrong words that are not on the card. **"vroucích" (row 7) is
really DLOUHÝCH**, and **"věrně" (row 8) is really VĚČNĚ**. The SOLUTION.md command
also still prints the old partial text with placeholders, not the completed
reading. These are concrete fixes. The reading as a whole stands, so the
verdict is REVISE, not REJECT.

## What I verified and how

1. **Solver command.** I ran
   `.../python/bin/python3 ciphers/hcp-1553/work/decode.py`. Exit 0, hash checks
   PASS, 324 mapped units / 328 base letters / 4 CH / 1 unmapped / 2 spans. The
   output is identical to `work/literal.txt`, and it **still contains**
   `[obscured:unknown-length]` (twice) and `tele[unmapped:K]ramy`. It does not
   produce the completed plaintext claimed in "Completion and handover" (see
   finding 3).
2. **Independent decoder.** I wrote `review/work/indep_decode.py` with its own
   inverse key taken from the family key `ciphers/hcp-1545/work/key.json`. It
   accepts both `7` and `y` as J, because this card's records label J as `y`
   where the family uses `7`. It also has H = CH and K = G. On the solver's
   `work/transcription.txt` it reproduces the solver's literal text, with G in
   TELEGRAMY. Every symbol in the transcription is covered by the key. Symbol
   counts: 5:39, 4:29, 6:25, m:24, 3:22, h:21, 2:21, d:19, c:17, b:17, t:13,
   y:11, q:11, n:11, g:11, f:8, s:7, 8:7, 1:5, p:4, H:4, r:1, K:1, plus 2 spans.
   Note that r (= H) occurs only once in the solver's transcription. My
   corrected transcription adds a second r (see finding 1).
3. **Pixels.** I rotated `source/picture.jpg` 90° clockwise myself
   (`review/work/oriented.png`) and cut all eight rows into thirds at 5x
   (`review/work/R{1..8}_{0,1,2}.png`). I made 7–12x crops of every disputed
   place: `S2a.png`, `S2b.png`, `S2b_nn.png` (nearest neighbour, autocontrast),
   `K.png`, `r7_vroucich.png`, `r8_verne.png`, `r1_srdecko.png`, `r1_first.png`,
   `r3_anenka.png`, `r4_anunko.png`, `r1_stredu.png`, `r5_left.png`,
   `r5_moci.png`. I read rows 1–8 sign by sign against the transcription.
4. **Corrected transcription and decode.** These are in
   `review/work/transcription_reviewer.txt` and
   `review/work/decode_reviewer.txt`:

```text
srdecko moje jedine, tesim se na stredu nesmirne.
prijedu, jak ujednano, rychlikem o tri ctvrte na deset
rano. nezapomene anenka na podobenky, o jichz oka-
zani jsem prosil? tesim se, anunko, jiz touzebne, az
budu moci pri prijezdu svem tvou drahou rucku stisknou-
ti a zlibati. pro pripad nepredvidane prekazky plati
ujednane telegramy. zatim posila ti tisic dlouhych
vrelych pus touzici a vecne tvuj pepous.
```

5. **Context.** 25 May 1903 was a Monday, and the letter looks ahead to
   Wednesday ("na středu", i.e. 27 May). Sister card HCP1554 (same couple)
   arranges the same Wednesday meeting with a rychlík at 9:40, telegrams as a
   fallback, and the sign-off "věčně tvůj Pepouš". The Wednesday, the train,
   the telegrams and the signature here all agree with that card. The address
   side reads Anna Tichá, učitelka, Žirovnice u Počátek. It is consistent with
   the metadata.

## Findings

### 1. Row 7, last word: the card reads DLOUHÝCH, not VROUCÍCH — **major**
The solver records `fh32s4H` (v r o u c i ch). The pixels
(`review/work/r7_vroucich.png`, `R7_2.png`) show seven clear signs:
**t 8 3 2 r 1 ř**.

- The first sign is the crossbarred `t` (= D), identical to the `t` in
  `275tm6m3` (row 2) and `275tm6m5` (row 7). It is not the tall looped `f`
  (= V) seen in `cf5n df32` (row 5).
- The second sign is a clear figure-eight `8` (= L). It is not `h`.
- The fifth sign is the short `r` (= H). It is not the backwards-6 `s`.
- The sixth sign is a plain `1` (= Y). It is not the `4` (= I) with a
  bar-foot.

Decoded: **d l o u h y ch** → *dlouhých*: "tisíc dlouhých vřelých pus" ("a
thousand long, warm kisses"). This is idiomatic. "Vroucích" was supplied from
expectation and is not on the card. It also changes the counts: one more
mapped unit (7 against 6 before the CH unit) and a second `r`/H. All records
need correcting: transcription, inventory, literal, counts, the Czech text, the
Slovak translation and the decoder's hash manifest.

### 2. Row 8: the card reads VĚČNĚ, not VĚRNĚ — **major**
The solver records `f5hm5` (v e r n e). In `review/work/r8_verne.png` and
`R8_1.png` the fourth sign is the short backwards-6 / "s" form, the same sign
as the C in `srde-c-ko` (row 1, 5th sign) and in `n3s4` = *moci*
(`r5_moci.png`). It is not the tall `h` (= R) with its ascender, which appears
in `m5cn4hm5` (row 1). Decoded: `f5sm5` → **vecne** → *věčně*. The signature is
"a věčně tvůj Pepouš". It matches the closing formula on sister card HCP1554
("…a věčně tvůj Pepouš").

### 3. The single command does not produce the claimed final plaintext — **major**
The README requires "a single command that produces the full plaintext". Two
places are out of step with the completed reading:

- `work/decode.py` and `work/key.json` still have no G, so the output keeps
  `tele[unmapped:K]ramy`.
- Both spans are still printed as `[obscured:unknown-length]`.

The "Completion and handover" section changes the reading only in prose. The
key (adding K → G), the transcription (removing S2a, and setting S2b to a
restored `t`, flagged as a restoration) and the decoder must be updated so that
the command prints the final text. Restorations should stay marked in the
records, for example `<t?>`, rather than being silently replaced.

### 4. G for the k-shaped sign: correct, but the support is overstated — **minor**
The sign (`review/work/K.png`) is a clear k-form: an ascender with a loop and a
kicked leg. It is visually distinct from the `h` (= R) right after it, which
gives TELE-k-h-AMY. HCP1541's `svagra.png` shows the identical k-form, also
followed by `h`, in `cf6khs` → SVAGRA. Two independent words with the same
sign make G well supported, and the family key has no other G sign.

However, SOLUTION.md says "four cards with one consistent assignment establish
the family's G sign". All of HCP1541, 1554 and 1570 are themselves only at
DONE1, completed by the same solver on the same day and not yet reviewed. On
1554 the earlier solver recorded the TELEGRAM spot as an *overlapped
unknown-length* span, not a clean k-sign. Please state the actual evidence
(this card and 1541, plus 1570 if verified) and call it a family assignment
inferred from context.

### 5. DESET is a context restoration and should be labelled one — **minor**
In `S2b.png` and `S2b_nn.png` the overinked sign has a tall stem with a top
flick and a crossbar. It is compatible with the crossbarred `t` (= D), but the
heavy ink (perhaps a correction) makes it impossible to identify on the pixels
alone. Only *deset* fits `?ESET` after "o tři čtvrtě na", so the reading is
right. It should still be marked as restored from context with visual support,
not as read. The claim that the time "agrees with HCP1554 (rychlíkem v 9:40)"
is loose: "tři čtvrtě na deset" is 9:45, and 9:40 is only close. Say
"consistent with", not "agrees".

### 6. Span 1 is only a dash — accepted — **minor (documentation)**
`S2a.png` shows a faint short horizontal stroke between `g` and `2`, with no
letter body. "jak ujednáno" is complete without it. The completion's reading is
supported. The records should still keep the stroke as a non-letter mark
rather than delete it.

### 7. ANENKA: the 3rd sign is not the card's normal 5 form — **minor**
In `r3_anenka.png` the third sign is a looped "ℓ/e" shape. It differs from the
card's regular `5` (as in `m5`, `n5m5` in the same row) and is not clearly the
`2` (= U) either (compare `6m2mg3` in `r4_anunko.png` and `t2` in
`r1_stredu.png`). Reading it as E (ANENKA) is plausible: it may be a plaintext
"e" slip or a 5 variant. A reading ANUNKA, matching "Anunko" on row 4, cannot
be excluded. SOLUTION.md calls ANENKA "the literal candidate base form" but
does not say this sign is visually anomalous. Disclose it.

### 8. Row 1, first sign — **minor**
The first sign of *srdéčko* (`r1_first.png`) is a closed-loop "s" with a long
lead-in. It is not the open `c` form (= S) used in `d5c4n c5` and `cdh5t2`, and
not the short backwards-6 `s` (= C). The transcription records it as `c`
without comment. The decode SRDECKO is certain from context. Note it as a
word-initial S variant.

### 9. Label inconsistency with the family key — **minor**
This card's records label J as `y`. The family key (hcp-1545) and the solver's
own completion text (`76g` for JAK) use `7`. The labels are internally
consistent, but SOLUTION.md should say so, so that the family keys can be
compared.

## Things checked and found correct
- Rows 1–6, row 7 up to TISIC, and row 8 apart from VĚČNĚ, sign by sign: the
  q/g (Z/K) labels, the four CH units (each with a visible caron on the r-form),
  the overlaps at STREDU, NEZAPOMENE and PREKAZKY, and the hyphenations
  OKA-/ZANI and STISKNOU-/TI.
- Row 2 suffix `5c5d` → ESET (four separate signs).
- Date 25./V.1903 and the address text.
- Provenance: the earlier GPT solver work and the Claude completion are both
  credited. The family key and the published partial study (Egorov) are
  disclosed. The portal shows no attached solution.

## Could not verify
- Whether the overinked sign before ESET was originally another letter that
  was corrected to D. The pixels do not settle it.
- The k-sign on HCP1554 and HCP1570 (I checked only HCP1541's crop).
- Whether the anomalous third sign of ANENKA is E or U.
- Postmark day (indistinct).
