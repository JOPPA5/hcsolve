# Notes hcp-1039

2026-11-03: captured by Claude Opus 5.5 (orchestrator).

## 2026-11-03 — Claude Opus 5.5 (solver), stopped as PARTIAL, no marker

Card: picture side carries ~9 lines (~170 signs) of invented symbols in ink over the
printed picture area, plus further signs written round the right margin (some
upside down, next to the printer's line "M. Kimmelstiel & Co. Hamburg"). Address
side was only cropped, not read in detail. Crops: work/crops/ (g*_a/b.png =
gridded 2x line crops of the hires original; s_*.png = 3-5x zooms).

Tools: work/hc.py, hc2.py, hc3.py (German quadgram + word hill-climb, using
batches/scoring-sol61/german). Free hill-climbs on a first rough transcription
(work/t0.txt, t1.txt) gave nothing; the language was found by hand from the
opening words.

What is established (by hand, on the pixels, language German):
- Line 1: 7 c Σ D | c Z D ∞ Σ M | M c L Σ c / E c ∇  -> "Mein einzig Geliebter"
- Line 2: ч c ∇ ∞ c D O O ⌒ ч - I Ƶ !  -> "Herzensschatz!"
- Line 3: ✓- 7 Σ E | ✓ Ǝ | O Σ c (dark ч) O E | ✓ - O  -> "Damit du siehst das(s)"
- Line 4 starts コ ⌒ ч | - D | ✓ Σ 7 ч  -> "ich an dich", ends O c D ✓ c -> "sende"
- Line 7: ... L Σ ⌒ ч O E c D | Ǝ D ✓ | M - D ∞ -> "(herz)lichsten und ganz"
- Line 8 ends: ... (dark sign) c ∇ / L c Σ / c  -> "(v)erbleibe"
- Line 9 probably "in unendlicher Liebe" (コ D | Ǝ D c D ✓ L ...) - not read sign by sign.
Core key so far: c=e, Σ=i, D/□=n, ∞=z, M=g, L=l, /=b, E(3 bars)=t, ∇=r,
ч=h, O=s, ⌒=c, -=a, ✓=d, Ǝ=u, 7=m.

Why it stops (not complete):
1. The system is not a clean one-to-one MASC as I read it: i appears as Σ, Z and
   コ; z as ∞ and Ƶ; t as E and I; the hook "7" is m in mein/damit but c in
   "dich". Either the writer used homophones or several of my sign classes are
   wrong. I could not separate these on the pixels with confidence.
2. Whole words remain unread or rest only on word sense: line 4 word 4
   (ᒐ - D コ ζ, perhaps "denke"/"danke"); line 5 "ich d?ir diese ?a?te"
   (a dark blot sign and an unknown ꭗ; "Karte" does not fit the sign count);
   line 6 (Ǝ D Σ c ∇ | ✓ c D | - Ƶ L c ∇ ч c ∇ ∞ - "unter/unser den
   allerherz-"? needs Σ=t/s and Ƶ=l, contradicting lines 1-2); line 8 opening
   (O Ë ✓ O ( D | ⅃ ‾ 7 O O c D - "süssen ... Grüssen/Küssen"? not consistent
   with the key); line 9 sign by sign.
3. The right-margin and upside-down signs (several short groups) and the address
   side have not been transcribed.
Gist (hypothesis only): "Mein einzig Geliebter Herzensschatz! Damit du siehst,
dass ich an dich [denke], sende ich [dir diese Karte] ... [aller]herzlichsten und
ganz [süssen ...] und verbleibe in unendlicher Liebe ..." - too many points rest on
word sense for a complete claim. Next step: a full sign ledger with one 5x crop
per sign occurrence, to decide which variant shapes are truly distinct.
