ACCEPT

# Review 1 – hcp-1478 (pc_hcp_159), reviewer Claude Opus 5.5, 2026-10-30

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1478/work/decode.py` (repo root):
   source hashes OK; output identical to the plaintext in SOLUTION.md
   (`To my own bathing with sincerest love from [t]your loving - Peggy`).
2. **Independent decoder.** `review/work/indep.py` (own code, own transcription)
   decodes the seven lines with (a) a pure index-XOR-2 involution on the whole
   alphabet and (b) the solver's variant with the abcd block rotated.
   Output:
   - pure XOR 2: `to my own / cbthing / with / sinderest / love from / tyour / loving`
   - solver key: `to my own / bathing / with / sincerest / love from / tyour / loving`
   So 5 of 7 lines (`my own`, `with`, `love from`, `your`, `loving`) come out
   as English under one rule with no letter of the abcd block involved; the
   rule is systematic (e<->g, f<->h, i<->k, j<->l, m<->o, n<->p, q<->s,
   r<->t, u<->w, v<->x, y=y), not fitted word by word. The repeated
   initial `jmx-` in `jmxg` (love) and `jmxkpe` (loving) is strong internal
   confirmation.
3. **Coverage.** Cipher letters used: a b d e f g h j k m o p q r t u w x y.
   Every glyph of the transcription is decoded; the only glyphs that depend on
   the abcd part of the key are `a`, `d` in `adrfkpe` and `b` in `qkpbgtgqr`.
4. **Transcription vs. scan.** Own 4x crops of every line
   (`review/work/l1.png` … `l7.png`) and 7x crops of the doubtful spots
   (`l1a.png` first glyph, `l4a.png` "qkpb", `l5a.png` "jmxg", `l6b.png`
   line 6, `sig.png` signature). Results:
   - `oy mup`, `adrfkpe`, `ukrf`, `htmo`, `jmxkpe`: confirmed sign by sign.
     In `adrfkpe` the 3rd/4th glyphs are the same r and long-looped f as in
     `ukrf`; "darling" is indeed excluded by the pixels.
   - `qkpbgtgqr`: confirmed 9 glyphs; the 4th has a tall ascender with the
     bowl to the right (b, not a, not d); the t carries a long crossbar;
     the final glyph is an r-like z/r form. The old reading `qkflglgqz` is
     superseded correctly.
   - `jmxg`: initial is a long-descender J/q-like form, then m, the
     "ↄc"/"a"-like x, then looped g. Reading as j m x g is consistent with
     line 7.
   - Line 6: I see `r` + `y` (descender) + `m` + `w` (written "uo") + `t`
     with long crossbar; the leading r is a separate stroke. Agree with
     `rymwt`, `[t]` disclosed.
   - Line 1 first glyph: tall heavy stem with a top loop and a bowl+leg at
     x-height – the same construction as the writer's lowercase k, only
     larger. Capital R is plausible but not demonstrable (see finding 2).
5. **Context.** Picture side "Baptist Church, Abergavenny", Valentine 45734;
   address "Mr Dixon, 3 St Nicholas St., Hereford" (portal metadata says
   "Discon"); ½d Edward VII stamp; postmark "…27 / 07" matching 1907-06-27.
   An English Edwardian greeting fits. Period language: "with sincerest love
   from your loving" is a stock postcard formula.
6. **Sources/credit.** SOURCES.md and SOLUTION.md say no published solution
   was found; the portal page is "Not solved" with no attached solution. The
   earlier GPT work (setup, provisional transcription, negative Caesar/Atbash
   screen) is credited. I found no sister card with the same key
   (grep for XOR/"two places" in ciphers/*/SOLUTION.md hits only Czech-family
   cards with unrelated keys).

## Findings

1. **(minor) The word "bathing" (line 2) and the abcd block are circular and
   should be labelled as tentative everywhere.** The abcd values a->d, b->a
   are derived solely from `adrfkpe` itself, and c->b solely from one glyph
   in `qkpbgtgqr`. The pure XOR-2 rule (which governs every other letter)
   gives `cbthing` / `sinderest`. "To my own bathing" is not idiomatic; the
   solver discloses all of this (uncertainty 2), but the plaintext line and
   the future report should mark the word as e.g. "[bathing?]" rather than
   print it unmarked; "sincerest" is safe (the c->b deviation is a single
   glyph and the word is otherwise certain).
2. **(minor) "To" rests on reading a k-shaped glyph as capital R.** My 7x
   crop shows the same form as the writer's k, larger and heavier. Under the
   key k would give "Io". "To" is overwhelmingly likely from context and is
   disclosed (uncertainty 1); keep it disclosed in the report.
3. **(minor) The signature is not literally "Peggy".** At 7x
   (`review/work/sig.png`) it reads `D/P e p g(q) y`: the first capital has
   its loop at bottom left like a cursive D, and the third glyph has the tall
   stem and bowl of this writer's p (compare the p in `jmxkpe`), not a g.
   "Peggy in clear" is a reasonable interpretation (it does not decode under
   the key: XOR 2 gives "bgney", solver's key "agney"/"ngney"), but SOLUTION.md
   should transcribe the signature as written ("Depgy"/"Pepgy") and state that
   "Peggy" is an interpretation.
4. **(minor) Line 6 leading `r` unexplained.** Disclosed as `[t]`; fine.
   It might be a false start; no fix needed beyond keeping it disclosed.
5. **(minor) Register type.** The key is a monoalphabetic substitution
   (XOR-2 involution with an irregular abcd block); `MASC` is the right type.

## What I could not verify

- Whether the abcd block really is a rotation (only 3 glyphs bear on it; z is
  unattested). No independent text from this writer was found.
- Whether "bathing" is the intended word (private joke/nickname) or a writer's
  slip for something else; I found no alternative reading consistent with the
  pixels and the rest of the key.
- The postmark town: only "…REFO…"-like letters visible, consistent with
  Hereford but not fully legible.
