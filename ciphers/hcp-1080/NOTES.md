# Investigation log

2026-10-19: Source setup after fresh rendered Not solved status and all three tabs. Address to Mademoiselle Vera Dosch, Doyhières (reading to verify), Berne, Suisse. Picture is a portrait of a child, printed caption Prinz Luitpold v. Bayern. Cipher body consists of digits, mathematical-looking signs, and letter-like glyphs. Slashes may separate words. Rotating the working image 90 degrees clockwise aligns its lines. Do not treat all similar 1/l, 2/z, h/4 or 9/g shapes as identical without collation. No plaintext established. Numerical substitution/MASC is a hypothesis; arithmetic or multiple-symbol groups remain possible. German is a working language guess only; portal says Unknown.

## 2026-10-30 — Claude Opus 5.5 (solver): key largely established, reading still incomplete

Work done: fetched the original-resolution scan (work/hires/, see SOURCES.md); rotated the cipher block 90 deg clockwise (work/crops/hrot.png) and cut enlarged per-line crops (work/crops/H*, Z*, q*, leftmargin.png, bottom.png). 18 lines plus a marginal line along the card's bottom edge (partly cut off by the edge, partly overprinted by the photographer's imprint).

Plain text, not cipher: "M. 9.VI.14. -" (München, 9 June 1914), matching the portal date.

Cipher: monoalphabetic substitution, German (Bavarian colloquial forms), words separated by "/", "=" also used as the German line-end hyphen. Letters are written as digits, arithmetic signs and a few letter-like shapes. The earlier GPT crib SAMSTAG is confirmed (line 11 "5+35|+7").

Working key (sign -> letter); confidence in brackets:
  x e [sure] | : i/j [sure] | + a [sure] | - o [sure] | * (star) u [sure] | diaeresis over a sign = umlaut (¨* ü, ¨+ ä) [sure]
  λ (lambda-like) n [sure] | h r [sure] | 8 h [sure] | 5 s [sure] | 6 b [sure; once p in "symbathisch"?]
  | (tall plain stroke) t [sure] | short 1 (ı) c, only seen in ch/sch [probable]
  Λ (1 with flag) d [probable; may also be t in one word]
  0 l [sure] | 9 g [probable] | 2 v [probable] | 3 m and w — apparently two similar 3-shapes not yet separated on the pixels
  4 (open-top) w? [weak, "4x:0" weil?] | 7 (4-shape with descender) f in freute/erfreut, g in Samstag, y in symbathisch? — not separated yet
  ʒ (3 with descender) g in Morgen? | = ö in bildschön [probable]
  k, p, z, f are not yet securely identified.

Words decoded with that key (tentative; each still to be re-checked letter by letter):
  L1  Mein Verl! (Verl = Bavarian diminutive of Vera) … [":. ı. 7. 4x:0. 9:" unresolved]
  L2  die mich sehr freute! freue mich …
  L3  Mutti? über [20 W.!?] erfreut! über …
  L4  man wohl nicht mehr reden! ich dät' mich
  L5  … tot? genieren an ihrer Stelle! Mutt=
  L6  … ich Morgen ; komme? hier nur
  L7  … Bett … [ʒ:h18xλ, 9h:xʒxh0! unresolved]
  L8  der … [9¨+0|x! Kälte?] was nicht
  L9  dein … sah gestern die …
  L10 … das … bildschön
  L11 … vornehm(!) Samstag sahen mir
  L12 den … der Braunschweig? er
  L13 ist goldig sie halt eine …
  L14 … beide aber sehr symbathisch(sic?)
  L15 … schon seit Jahren an einer …
  L16–17 … ich mieter? …
  L18 … viele Bussis …

Why it stops here (no DONE marker): the key is clear, but a complete letter-by-letter reading is not yet in hand. Open problems: (1) the sign pairs 3/3 (m vs w), 7-shapes (f/g/y), Λ vs | (d/t), 9 vs a k-sign, and 4 vs h must be separated on the pixels before the remaining words can be fixed; (2) about 20 words are still unresolved (list above); (3) lines 16–18 and the right ends of lines 14–18 are overlaid by the blue postmark and the printed divider line; (4) the marginal line along the bottom edge ("5*03:h||0:…") is partly cut off by the card edge and overprinted by "Hofatelier A. Baumann Nachf., München Residenzstr. 12". Next step: per-sign instance sheets (crop every occurrence of each ambiguous sign side by side), then resolve the open words with the key and German/Bavarian vocabulary, then write work/decode.py with a full transcription.
