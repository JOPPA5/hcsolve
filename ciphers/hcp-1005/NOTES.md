# Notes hcp-1005

2026-11-03: captured by Claude Opus 5.5 (orchestrator).

## 2026-11-03 — Claude Opus 5.5 (solver), partial

Card: embossed patriotic card "Uns gebühret der Sieg!", postmark PÖLLWITZ (REUSS) 19.9.16, to "Fräulein Fränz", Pöllwitz.
Picture side: printed text only, no handwriting seen. Stamp not lifted (no image under it available).

Cipher: five rows of pencil numbers on the left of the address side, written with the card turned
90 deg (read after rotating the hires scan 90 deg counter-clockwise). Number substitution A=1 ... I=9,
K=10 ... Z=25 (no J; K vs J for 10 untested). Established by LIEBE = 11 9 5 2 5, ELSA = 5 11 18 1,
AM SONN(bar)TAG = 1. 12 18 14 13(bar) 19 1 7 (bar over 13 = doubled n), GRÜS|SE = 7 17 20 18 | 18 5.
Several 20s carry a u-bow / umlaut strokes above.

Token reading (work/decode.py):
  11 9 5 2 5 . 5 11 18 1 .            LIEBE. ELSA.
  18 17 9 2 9 2 5 . 1 . 12 18 14 13=  S R I B I B E . A. MSONN   (17 and the two 9/2 glyphs uncertain, under embossing)
  19 1 7 . 18 1 8 2 20" 13 1          TAG. S A H B Ü N A          (18 written over embossing)
  2 5 18 14 5 13 . 7 17 20" 18        B E S O E N . G R Ü S       (18 and 14 under embossing)
  18 5 20u 11 12 1 2 ?                S E U L M A B ?             (11 could be 18; last glyph a hooked 3/J-like sign)

Readable: "Liebe Elsa. ... am Sonntag. ... Grüsse ..." The word in row 2 (SRIBIBE, perhaps a child's
"schreibe", but the pixels do not give SCHREIBE), the clause SAHBÜNABESOEN in rows 3-4 and the
signature row (U L/S, M A B ?) do not read as German. "Max" for 12 1 23 would need the last two
glyphs to be one number 23, which is not clear. Not forcing words: the card stays PARTIAL, no marker.
No published solution found in the repo; no web search done.
