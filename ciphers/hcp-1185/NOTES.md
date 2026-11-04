# Notes hcp-1185

2026-11-03: captured by Claude Opus 5.5 (orchestrator).

## 2026-11-03 — solver session (Claude Opus 5.5): structural analysis, no reading

Result: PARTIAL. No key and no plaintext. No marker created.

What the card is
- Address side: plain Kurrent/Latin address "Frl. Hedwig Zipfel, Zeitz (Prov. Sachsen),
  Messerschmidtstraße 26" (street name read from the scan, not checked further). Postmarks
  KIEL 11.2.01 and ZEITZ 12.2.01. Stamp (5 Pf. Germania) is in place; nothing written
  around it; what lies under it cannot be seen on the scan. No cipher on the address side.
- Picture side: printed love scene, verse "Wenn die Blätter leise rauschen ...", printed
  notes "Bitte gegen das Licht zu halten" (hold-to-light card) and "Meteor's R.G.M. 38090".
  The whole free margin is filled with hand-drawn signs: a line along the top edge, a column
  down each side edge, about eight wavy rows in the lower right/centre, a short row under the
  picture at the left, and a full-width row along the bottom edge. Estimate 500-650 signs.
- Orientation: the writer turned the card while writing round the edge. The top line, rotated
  180 degrees (work/crops/topA_r.png, topB_r.png), shows the same dominant shapes (L, V) as
  the bottom block, and contains a sign that is an ordinary question mark in that
  orientation. The side columns are written sideways in the same way. So reading order is:
  block / bottom rows upright, the border rotated with the card; the exact start is not fixed.

Sign inventory (read on 3x enlargements, work/crops/L0_*.png ... L2_*.png, z1.png)
- Almost every sign is two straight strokes meeting at an angle (L, J, V, <, >, Lambda,
  7-shapes, plus slanted 45/135-degree variants), or a single stroke (/, \, |, -), often a
  stroke with a tiny hook at one end. Isolated dots stand after many signs, at baseline right.
- Signs sit at two heights: larger upright signs (V, L, |, -) on the line and smaller slanted
  strokes (/, \, <) dropped below it.
- Counts on two clean rows (42 signs): V 13, L 8, / 9, others (-, <, |, \, angle variants) 12.
  On the rotated top line the groups "L L / ." recur three times and "V L V \ ." once.
- Groups between dots are 1 to 8 signs long.

Hypotheses tested and why they fail or stay open
1. Pigpen (3x3 grid + X, with/without dot): edge-cell U-shapes and the closed box never
   appear, while single strokes are common. Not standard Pigpen; the dot-count variant of
   hcp-1131/1189/1190 (square outlines with 1-3 dots) does not fit at all.
2. Flag semaphore (two arms from a centre, 8 directions; Kiel is the naval base, 1901): the
   shape set fits geometrically (straight lines = D/L/R, 45/135/90-degree pairs), but
   international semaphore in either mirror orientation turns clear rows into nonsense
   (e.g. "J U L L ..."; repeated "L V" = "JU"/"PU"). German Kaiserliche Marine Winker tables
   not available to me; not tested beyond international semaphore.
3. One sign = one letter MASC: three shapes (V, L, /) make about 70% of the sample, far more
   skewed than German (top three letters about 35%). Either the shapes I merged are really
   several signs distinguished by orientation details I cannot fix reliably, or letters are
   written as several strokes (sign groups, e.g. a stroke code or broken-up Kurrent letters,
   with the dots as i-dots or separators). Neither was resolved.
4. Published solution: web search (Klausis Krypto-Kolumne, general) found none for this card.

Why it stops here
- The decisive step is a reliable sign classification of 500+ hand-drawn angles whose
  orientation varies continuously with the writer's slant and with the card's rotation; my
  classes are not stable enough to support a frequency or hill-climbing attack, and the
  frequency profile itself argues against a plain letter-per-sign substitution. Sister card
  hcp-1201 (same correspondent, Kiel -> Zeitz, 5.3.1901) has no work yet; its scan (picture
  side shown at large size) has no visible handwriting on the picture side.
- Suggested next step: segment the ink (work/seg/mask.py gives a usable black-ink mask for
  the plain-card areas; brown/light ink is partly lost) and measure each sign's stroke
  directions automatically, then test (a) German Winker tables of c. 1900 and (b) a
  stroke-group code against the measured classes.
