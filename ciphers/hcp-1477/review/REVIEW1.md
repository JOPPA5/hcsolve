ACCEPT

# Review 1 — HCP 1477 (pc_hcp_158), Rommehed postcard to Sara Erickson, 9 May 1904

Reviewer: Claude Opus 5.5, 2026-10-30. Round 1 (marker DONE1).

Note on independence: the round-1 solution was also produced by Claude Opus 5.5
(after triage by an OpenAI GPT session). I did not reuse the solver's transcription;
I re-read the strip from my own crops and wrote my own decoder.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1477/work/decode.py` from the repo root:
   source hashes OK, output identical to the plaintext in SOLUTION.md, 143 signs, 4 lines.
2. **Own crops.** `review/work/strip_cw.png` (right margin x=860–1000, rotated 90°
   clockwise, 2x), `rot.png`, and 5–12x enlargements of every line
   (`seg0-3.png`, `L1_*.png`, `l2_*.png`, `l3_*.png`, `l4_*.png`) plus spot crops
   `litapa.png`, `pa.png`, `pa2.png`, `vanskap.png`, `gingsbat.png`, `bat.png`.
   Location of the cipher (right margin, four lines, read bottom-to-top on the card,
   left column first) confirmed; the other texts on both sides are plain Swedish.
3. **Own transcription and decoder.** `review/work/my_decode.py` holds my own sign-by-sign
   reading in a separate notation and my own key. It yields 143 signs and the same
   plaintext as the solver except at the two points in findings 1 and 2. I checked
   every sign of all four lines against the crops, not a sample.
4. **Key consistency.** Each sign class maps to one consonant across the text. Every
   consonant except b and h is confirmed in several independent words (d, g, k, l, m, n,
   r, s, t, v many times; p in vänskap; b in blir/bandet/brister; h in har/härden).
   The digit part (b1 d3 g5 h6 k8 l9 = position in the row b c d f g h j k l) is a
   coherent, natural construction. Vowels in clear, with marks on å/ä/ö visible on the scan.
5. **Language.** The text is a rhymed, trochaic Swedish album/friendship verse
   (världen/härden, på/ändå, brister/mister, igen/vän). Spellings (trikt, brites, knits,
   värden) are the kind of phonetic spellings a private writer of 1904 would make.
   It fits a friendship postcard and the plain-text greeting on the same card.
   This is not words forced onto noise: 33 of 35 words are ordinary Swedish read with
   one fixed key.
6. **Sources.** Portal status "Not solved", no attached transcription/solution
   (source/metadata.md). Earlier GPT setup/triage and the later Claude work are credited.

## Findings

1. **minor — "på" (line 2) is written with two dots, not three; this is not disclosed.**
   In `pa2.png` (12x) the sign before å shows only two dots, spaced like every other
   ":" (= n); there is no third dot, and the tail of the "3" above ends clear of the
   gap. In *vänskap* (`vanskap.png`) the ⁝ clearly has three dots. Read literally the
   word is *nå*. *lita på* is certain from sense and rhyme (på/ändå), so the reading
   stands, but `work/transcription.txt` writes `P` as if three dots were visible.
   Fix: record it in Uncertainties as a writer slip (or two-dot variant) restored as p.
2. **minor — one g-like glyph is read in two ways by context.** The tall glyph with a
   descender in *trikt* (2nd consonant 8), *vänskap* (k) and *igen* (line 4, first word)
   looks the same in my crops (`L1_2.png`, `vanskap.png`, `l4_0.png`). The solver reads
   it as 8 = k twice and as 5 = g once. Uncertainties 3 and 5 mention the loose
   drawing, but do not say plainly that this is one glyph and the value is chosen by
   context. Read as g, the first word gives *trigt*, which is closer to *tryggt*.
   Fix: say this plainly and give *trigt* as an equal alternative.
3. **minor — word count.** SOLUTION.md says "31 of 33 words". The decoded text has
   35 words, of which 33 are ordinary words (the two exceptions are *ging sbät*).
4. **minor — line 7 is unread (properly disclosed).** In my crops *ingen ging sbät*
   (`gingsbat.png`, `bat.png`) is, sign for sign, what the solver says: heavy closed 5,
   i, :, 5, ÷, 1, ä, dash with dot below. The solver reports the line literally and
   does not adopt the conjecture *ingenting så lätt*. That is correct handling. The
   English and Slovak translations of that line should keep a clear gap marker
   rather than "one loses like a friend". That phrase reads as a full sentence, and
   it is not one.

No blocker or major findings.

## What I could not verify

- The source of the verse. I did no web search of my own. The solver reports two
  searches with no hit. The verse may be a published album verse ("Har du ingen vän i
  världen..."), and a source text could settle line 7.
- Whether the heavy closed 5 is a deliberate variant or a correction. I accept it as g
  from *glad*.
- The scan has only 674 px of height for the strip, so it is low resolution. The dots
  under and over the dashes (s vs t) are 1–2 px. I checked every one I could, and
  none contradicts the decoded words, but a better scan would make this firmer.
