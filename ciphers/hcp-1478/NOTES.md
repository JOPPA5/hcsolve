# Solver log —2026-10-26
Fresh Not solved, all3tabs read, both sources captured. Alphabetic cursive
cipher; signature appears ordinary Peggy (not a deciphered name).
Own provisional transcription in work/provisional.txt has uncertain letter
identities (notably first glyph, q/g, c/n, and long middle word). It is not
frozen as exact source text. Body crop enlarged for future inspection.
Tested all26Caesar shifts, Atbash, adjacent-key QWERTY shifts in both
directions, direct/reverse QWERTY alphabet substitutions; none gave a coherent
whole reading from that provisional transcript. This is only a bounded
screen and says nothing about all possible substitutions or a corrected
transcription. No plaintext/key established, no marker/register entry.
Next1477 needs fresh inspection. No watcher launched.

# Solver log - 2026-10-30 (Claude Opus 5.5)
Re-transcribed everything from 4-7x enlarged crops (scratch crops, not kept):
Rm oy mup / adrfkpe / ukrf / qkpbgtgqr / jmxg htmo / rymwt / jmxkpe / Peggy.
Dead ends: Slovak quadgram hill-climb (only Slovak tables in repo - useless);
"To my own darling" with a free MASC gave conflicts (ukrf, girl/with).
Breakthrough: cribs own/my/with/from/loving/love all obey plain index XOR 2
(e<->g, f<->h, i<->k, l<->j, m<->o, n<->p, r<->t, s<->q, v<->x, w<->u), y=y.
"qkpbgtgqr" = sincerest with c->b (not XOR 2); "adrfkpe" = ??thing, "rf" are
the same glyphs as in ukrf (so not "darling"); with a block-permutation
assumption only "bathing" fits -> abcd block rotation a->d b->a c->b d->c.
First glyph read as capital R (T); a lead-in r before ymwt (your) unexplained.
Decoder: work/decode.py (checks source hashes). SOLUTION.md rewritten; DONE1.
