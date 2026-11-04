# Notes hcp-980

2026-11-03: captured by Claude Opus 5.5 (orchestrator).

## 2026-11-03 — Claude Opus 5.5 (solver), attempt 1: PARTIAL, no marker

Card: Theux (BE) -> Arlon, 10 Aug 1907, to Armand Boutet, 14e de ligne 3/3.
Language almost certainly French (Theux, French picture caption). Picture side
holds only the printed verse "Sous les reflets de lune..." (publisher A&S 527);
no hand-written or hidden text seen there or around the stamp (stamp not
lifted, so the area under it cannot be checked from the scans).

Ciphertext: 5 short lines (about 44 glyphs) left of the address, made of dots,
dashes, diagonal strokes, angle shapes, stacked lines with dots, two dotted
circles. Provisional glyph transcription: work/transcription.txt.
Ink components measured with work/components.py (length of each stroke, gaps).

Web search (Schmeh blog, Schrödel HistoCrypt paper page): no published
solution of this card found. No sister card in the repo (no other Boutet /
Theux / Arlon card).

Hypotheses tried and why they stop:
1. Plain International Morse, each glyph one letter (stacked/rotated elements
   read in order): gives "J/AM D S | T D ? T D ? | M ? H" etc. Not French.
   The horizontal group ..-. (F) occurs 6-7 times, impossible for F.
2. Morse + Caesar shift (F->E, shift -1) and other shifts, dot/dash inverted,
   element order reversed: none gives French on line 2 (X B Q4 C2 F4).
3. Morse with free re-segmentation of the groups (..-. = ER / UE / IN):
   stream too ambiguous; no consistent French found.
4. Count-based (dot=1, dash=5) numbering: nonsense.
5. Pigpen dot-count family (hcp-1131/1189/1190): the glyphs are not cell
   outlines; does not fit.
6. Simple substitution on glyph identities. Promising but unconfirmed cribs:
   L1 word 2 has pattern ABCABC (H D3 U2 H D3 U2) -> LOULOU/TOUTOU/COUCOU;
   L1 word 1 X D3 V3 -> MON/TON/SON; L4 "( U2 V3 F4" -> UNE (U2=U, V3=N,
   F4=E agree with MON + xOUxOU). L4 end "L3 U2 C2" -> ?U? (QUI/LUI/PUI..).
   But L4 middle "L3 F4 X G F4" (?E??E) and L3 "G F4 H F4 O G F4" (?E?E??E)
   give no word consistent with the same key: FEMME needs X=G, which are
   visibly different angle forms; RESTE/VESTE (X=S) breaks L3; TETE needs
   H=G. No complete, consistent key found.
Open points for a next attempt: whether the long bars are word dividers or
letters; whether X's leading dot+dash is part of the glyph; the meaning of the
three-line vs two-line-with-dots signs; the smudged L5 block (possibly a
signature). Status: partial, no SOLUTION claim, no DONE marker.
