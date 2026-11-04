# Notes hcp-1090

2026-11-03: captured by Claude Opus 5.5 (orchestrator).

## 2026-11-03 – Claude Opus 5.5 (solver, round 1)

- Address side: vertical columns of pen dots/dashes = Morse. Picture side (Titisee view): nothing hidden
  visible; stamp box not examinable. Short web search: no published solution of this card.
- Mark detection: `work/blobs.py <hires adr> work/blobs.json 150` (ink threshold 150; 120 missed faint
  dashes), column lines fitted by `work/columns2.py` (-> work/lines.json). Dots 10-25 px tall, dashes
  33-70 px; inner gaps <= ~45 px, letter gaps >= ~50 px (c00 is tighter: 23 vs 38).
- First trial decode top-to-bottom gave German words per column (LIEBER ERNST in the rightmost column,
  "AUF DA" + next-left column "S WIEDERSEHEN") -> reading order right-to-left columns.
- Writer's H = five dots (6 times); CH = ----. Grey insertion loops in c05 (----, CH of ICH) and c10
  (....., H of VIERZEHN). Grey script letter (looks like "3s") in c02 in the gap GR_SSE -> read ü;
  following group is ..... (writer's H) -> literal GRüHSE, emended GRÜSSE (word sense).
- c14: R of DIR written left of the column foot (x~1385, y 2068-2143).
- c01 bottom ends DEINE; extra short column c00 at far left bottom (x 54-74, y 1654-2112) = ANNA.
- Date note on the divider: "31. III. 11. ab. 9 U[hr]" (cut at edge).
- verify_marks.py residual differences, each checked on crops (work/crops/):
  c14 G's final dot is large (25 px) -> classed dash by detector; c10 grey loop dots/lines mixed in by
  y-sort; c09 blotted first dash of G (467-567, no gap: one dash; c9_G.png); c08 card bottom edge picked
  up; c06 smudged dot of A (1914-1940); c05 loop dashes beside the column and the 4th CH dash at the
  bottom edge (c5_end.png, c5_br.png); c03 a stroke of the printed publisher logo; c02 the CH dashes
  run over the printed logo and were excluded with it (visible on strip_h1_g0.png).
- Result: complete reading, one emendation (GRÜSSE). SOLUTION.md written; DONE1 created.

## 2026-11-03 – after review 1 (ACCEPT, 4 minor)
- Grey letter in GR_SSE now decoded literally as u (Kurrent u-hook, no umlaut dots); literal GRuHSE, emended GRÜSSE.
- Five-dot sign identified as Morse digit 5 used for H; stray speck before H of GEHT disclosed; stamp edges stated clean.
