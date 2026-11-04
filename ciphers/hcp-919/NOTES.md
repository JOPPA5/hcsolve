# Notes hcp-919

2026-11-03: captured by Claude Opus 5.5 (orchestrator).

## 2026-11-03 — Claude Opus 5.5 (solver), partial

Web search (Schrödel / Klausis Krypto Kolumne, "Bensberg 1908 Emmy Oberlausitz"): no published solution of this card found.

Card: picture side printed Tier-Post No. 6 "Ausgabe" (H. Starkloff, Meiningen), nothing hand-written there except the printed "H. St. 08". Address side: Fräulein Emmy Kr..., [Leuters?]dorf, Oberlausitz; postmark BENSBERG 3.1.08; pencil "79." left of address is a collector/number mark. Stamp still on the card (stamp box not inspectable underneath). Not related to the Emma Krumbholz cards hcp-974/976 (different hand, different cipher).

Message: 22 lines of pencil on the left half, an invented alphabet that mixes Latin-looking letters (o, v, e, c, n-like caret) with stroke signs (⊥, T, ⊢, +, ‡, =, ∟, 7, /) and broken/dotted slanted strokes (dot above, dot below, 2- and 3-segment strokes). Words are separated by spaces. Crops: work/crops/L??a/b.png (2.5x per half line), z*.png (3–6x). Helper work/zoom.py.

Key established from words that read (all monoalphabetic so far):
  = m · v e · o i · e n · "-." (dash + dot, always together) r · stroke with dot above d · / (plain long stroke) b · ⊢ l · 7 f · ʌ (caret) z · g-shaped sign g · 8/∂-shaped sign g (two g shapes, or one misread) · ∟ h · ⊥ s · + with dot below ü · 3-segment dotted stroke t · c ch (from "oc" ich, "=oc" mich) · ‡ k? (one occurrence) · "." alone a? (one occurrence)

Readings that support it:
  L1  =voev oeeo8 gv⊢ov/;v voenogv        Meine innig geliebte einzige
  L2  ∟v-.ʌve⊥ Y¦¦·v =ovʌv 7.ṭ-.          Herzens???e Mieze(?) für
  L3  ivoev ⊢ovlv ⊥ṭ⊥⊥v ‡.-.;v ...         deine liebe süsse Karte(?) ...
  L8  o==v-.  (again L17)                  immer
  L10 iv-. /-.ov7                          der Brief
  L12 ... Tv-. ive                         ...er den
  L13 oc ... oe                            ich ... in

Why it stops: from line 4 on almost every word contains clusters of dotted / broken slanted strokes (dot above, dot below, colon-like pairs, 2- and 3-segment strokes, and a separate baseline dot). At the scan resolution (about 3 px per dot) I could not sort these clusters into stable sign classes or decide where one sign ends and the next begins (e.g. L4 ":!.!⊥ve:.:e‡", L5 "∟;;v/o⊥∟v!;v =o;;.∂⊥c.⊢", L14 "1o:!..!.!.7"). Several shape classes (T, Y, ‡, +, ll, θ, ε, <) have no secure value yet; L7 "ivoc ivoe" (dei-ch dein?) does not read. Forcing values onto these clusters would be guessing, so no full plaintext and no marker.

Next steps for whoever continues: build a sign ledger of the dotted-stroke clusters by position (dot above / below / middle, number of segments) from the 3–6x crops, test whether they are a vowel/umlaut and a/t/u/o group (only a, o, u, t, w, k, p, ä, ö are still unplaced), and use the love-letter context (Meine innig geliebte einzige Herzens… / für deine liebe süsse Karte / der Brief / immer) as cribs.
