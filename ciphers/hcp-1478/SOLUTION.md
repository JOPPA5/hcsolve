# hcp-1478 (pc_hcp_159) - solution, round 1

Card: Valentine's Series "Souvenir Post Card", picture side "Baptist Church,
Abergavenny" (Valentine 45734). Address side: "Mr Dixon, 3 St Nicholas St.,
Hereford", ½d green Edward VII stamp, Hereford(?) postmark 27 JU 07, matching
the portal date 1907-06-27. Portal status: Not solved; no transcription or
solution attached (see SOURCES.md). No published solution of this card was
found; the decipherment below is my own (Claude Opus 5.5, 2026-10-30).

Credit: setup, metadata capture, scan download and a first provisional
transcription with a bounded screen (Caesar, Atbash, keyboard shifts, all
negative) were done on 2026-10-26 by the earlier OpenAI GPT solver
(see NOTES.md). The transcription below is a new one made from enlarged crops;
it corrects several earlier readings (qkflglgqz -> qkpbgtgqr, qmccy -> jmxg,
km -> Rm, rymuot -> rymwt, qmckpe -> jmxkpe).

## Cipher type and key

Simple monoalphabetic substitution of a structured kind. For e...x every
letter is replaced by the letter two places away inside its block of four
(alphabet index XOR 2):

    plain : e f g h  i j k l  m n o p  q r s t  u v w x
    cipher: g h e f  k l i j  o p m n  s t q r  w x u v

The block a b c d does NOT follow XOR 2 on this card; the attested values fit
a rotation:

    plain : a b c d          y
    cipher: d a b c          y      (z not attested)

The message is written in cursive; the signature "Peggy" is in clear.
The key is reciprocal for e...x, so enciphering and deciphering are the same
operation there.

## Transcription (own, from source/address-large.jpg)

    Rm oy mup
    adrfkpe
    ukrf
    qkpbgtgqr
    jmxg htmo
    rymwt
    jmxkpe
            Peggy

## Plaintext

    To my own [bathing?] with sincerest love from [t] your loving
    Peggy   (signature in clear, written "Depgy"/"Pepgy"; "Peggy" is an interpretation)

English: "To my own [bathing(?)] with sincerest love from your loving Peggy."
(The language is English; the "translation" is the same text.)

Slovak: "Môjmu vlastnému [kúpajúcemu sa(?)] s najúprimnejšou láskou od tvojej
milujúcej Peggy."

## One command (from the repo root)

    python3 -I ciphers/hcp-1478/work/decode.py

It checks the SHA-256 of both source scans, prints the line-by-line literal
decryption and the reading. Output (2026-10-30):

    Rm oy mup    -> To my own
    adrfkpe      -> bathing
    ukrf         -> with
    qkpbgtgqr    -> sincerest
    jmxg htmo    -> love from
    rymwt        -> tyour
    jmxkpe       -> loving

## Uncertainties (all disclosed)

1. **First glyph of line 1 (Rm).** The glyph is a tall stem with a top loop,
   bowl and leg. I read it as a cursive capital R (cipher for T, as r -> t is
   used in "with", "from", "sincerest"). It is, however, similar to the
   writer's lowercase k; read as k the word would decode to "io", which is not
   a word. "To" rests on this capital-R interpretation.
2. **The abcd block and the word "bathing" (line 2).** The pixels clearly
   show "a d r f k p e"; r f k p e -> "thing" is certain under the key. The
   first two letters depend on the abcd part of the key, which is attested
   independently only by c -> b in "sincerest" (pure XOR 2 would give
   "sinderest"). Assuming the writer's abcd block is, like every other block,
   a permutation of abcd, cipher a, d must be two of {a, b, d}; the only
   English word "??thing" with those is "bathing" (b -> a, a -> d), which
   together with c -> b forces the rotation shown above. So "bathing" is the
   only reading consistent with the key, but the key for a/d comes from this
   word itself. Semantically "To my own bathing ..." is odd (one would expect
   "darling"); "darling" is excluded by the pixels: the 3rd and 4th glyphs are
   the same r and f as in "ukrf" (= "with"), i.e. t h, not r l.
   Possibly a writer's slip or a private joke; I report the literal result.
3. **Line 6 leading glyph.** "ymwt" = "your" (the cursive w looks like "uo").
   It is preceded by a separate r-shaped glyph that would decode to "t".
   It may be a false start / lead-in stroke; it is shown as "[t]" and not
   given a meaning.
4. **qkpbgtgqr.** The 3rd glyph is the writer's long-stem p whose bowl rises
   as a loop (read earlier as "fl"); the t is a looped stem with a crossbar
   that overruns the following g; the last two glyphs (earlier "yz") are q and
   r. Read as 9 letters it gives "sincerest" exactly (with c -> b).
5. **jmxg / jmxkpe.** The capital-J-like initial is the cipher j (= l); the
   cursive x is written like "ac"/"ↄc" and was earlier read as "ac"/"cc".
6. z and the plaintext letters j, k, p, q, u(as cipher w only), x, z are not
   (or barely) attested; they do not occur in the message.

## Why I believe it is correct

- One fixed, structured rule (index XOR 2 on e...x) turns 9 of the 11 cipher
  words into exact English words with no adjustment: To(*) my own ...thing
  with sincerest(*) love from your loving - and the message has the shape of
  a standard Edwardian postcard greeting ending above the clear signature
  "Peggy". (*) see uncertainties 1, 4.
- The key is not chosen word by word: it is a single systematic transform,
  checked across 18 distinct plaintext letters (e f g h i l m n o r s t v w y
  plus a b c in the abcd block).
- The earlier GPT screen (Caesar, Atbash, keyboard) was negative, consistent
  with this non-shift key.
- Residual weak points are listed above; the main one is the meaning of
  line 2.

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent) gave verdict **ACCEPT** with five
minor findings. Responses (Claude Opus 5.5, 2026-10-30):

1. **"bathing" and the abcd block are circular – mark as tentative.** Agreed
   and fixed. The plaintext in this file now reads "[bathing?]", and
   work/decode.py prints "[bathing?]" in the reading line (the literal
   line-by-line output still shows the bare decryption). The circularity
   (a, d derived from this word, c->b from one glyph of "sincerest") stays
   disclosed in uncertainty 2 and will be stated in the report.
2. **"To" rests on reading the first glyph as capital R.** Agreed; no change
   to the reading. It remains uncertainty 1 and will be stated in the report.
3. **Signature not literally "Peggy".** Agreed. On the reviewer's 7x crop
   (review/work/sig.png) the signature is written "Depgy" or "Pepgy": the
   capital has the bottom-left loop of a cursive D/P, and the third glyph has
   this writer's tall-stem p form. It does not decode under the key ("agney"/
   "ngney"). It is now transcribed as written, with "Peggy" given as an
   interpretation (a cursive g with a looped stem resembling p, or a slip),
   both here and in the output of work/decode.py.
4. **Leading r in line 6.** No change; remains disclosed as "[t]".
5. **Register type MASC.** Agreed; used in the register entry.

Re-run after the fixes (2026-10-30): `python3 -I ciphers/hcp-1478/work/decode.py`
-> "source hashes OK", the same seven literal lines as above, and
"Plaintext: To my own [bathing?] with sincerest love from [t]your loving -
Peggy (signature as written: Depgy/Pepgy)". No decoded letter changed.
