# Focused opening audit — 2026-10-26 UTC

Re-read README, checked no markers, and re-opened unmodified original picture.jpg. No watcher/reviewer. This is solver re-inspection, not an independent review.

## Pixel observations

The derivative audit-*.png crops are enlarged original pixels with contrast adjustment. They do not reconstruct missing strokes. Original-coordinate boxes:

| Observation | Original crop x0,y0,x1,y1 | Finding |
|---|---|---|
| First word final glyph | 535,423,620,467 | Last two glyphs are an undotted box and a **top-and-left** corner with an interior dot. The final corner is NW-dot=S. The long top arm is clear; it is not SW-dot=M. Literal MEINES is retained. |
| First row last glyph | 771,425,804,463 | A thin left upright is visible alongside the heavy top/right/bottom strokes. Treat as closed box E, not right bracket D. The left stroke extends slightly above the box; note watermark proximity. |
| Third row first word | 198,496,355,542 | Five glyphs: SE-dot, O-dot, SW-dot, SW-dot, box. Literal KOMME. There is no missing prefixed glyph before the first corner in this margin. |
| KOMME final glyph | 325,503,355,536 | Left upright and the other three sides are all visible, albeit separated at the upper-left join. Box=E, resolving former E/D. |
| KRAEFTIGON penultimate glyph | 927,503,959,537 | Closed box with distinct dark round mark inside, away from the visible watermark strokes. Literal dotted box=O; do not silently print E. |
| Second row far right | 890,458,994,507 | Beyond the terminal N are separator-like ink and watermark letters. No support for appending an extra dotted corner to force MAEUSCHENS. |

## Key constraints and reading order

The omitted-J grid is supported by several separate words. SW-dot=M is also required in MAEUSCHEN; NW-dot=S occurs repeatedly in SCHLUCK, SUESSEN and GUTENACHTKUSS. Changing NW-dot to M merely to obtain MEINEM would break those independent groups. The first-row anomaly therefore cannot be repaired by a globally consistent swap of the two dotted corners while retaining the clear tail.

The text is laid out left-to-right in five horizontal rows, with separator strokes after word groups. The last row and signature follow that same direction. Reversing rows, individual words, or alternating row directions does not retain the clear tail in reading order and supplies no source-backed correction to MEINES/KOMME. No interlinear insertion was found above the first line or after MAEUSCHEN. This is a visual reading-order check, not an exhaustive route-cipher search.

## Current literal result

```
MEINES LIEBE
HERZIGEN MAEUSCHEN
KOMME ICH EINEN KRAEFTIGON
SCHLUCK UND EINEN SUESSEN
GUTENACHTKUSS
THEO
```

The source supports more exact letters than the previous version: both E/D alternatives resolved to E; the E/O alternative resolves provisionally to literal O. This does **not** resolve the opening grammar. Candidate intended forms such as MEINEM and KRAEFTIGEN remain normalizations which conflict with source glyphs; no intended verb has been established for KOMME. Author encipherment mistakes, an unresolved local convention, or a remaining manual misreading are possibilities, not findings. Keep partial status and no DONE.

## Unenhanced same-hand control check

Root initially questioned the center mark but had opened `audit-r3-last.png` (KOMME's final E), not `audit-r3-dot.png` (the KRAEFTIGON O). Root subsequently inspected the correct crop and agreed with the visible dot. This is shared solver source audit, not independent review.

`compare-boxes.py` creates `box-controls-unenhanced.png` directly from the original RGB pixels, nearest-neighbor enlarged at the same sixfold scale, **without contrast adjustment**. Four separate E boxes and two O boxes are shown beside the two targets. The KOMME final box has no comparable dark center; KRAEFTIGON has a small dark central mark resembling the two secure O controls. On specified 5×5 center patches, minimum grayscale values are 234 for KOMME E, 159 for KRAEFTIGON O, 229–232 for the four E controls, and 130/134 for the two O controls (0 black, 255 white). Corresponding center means are 238.16, 211.84, 235.00–237.12, and 207.64/207.80. These are descriptive pixels, not an ink classifier or a claim that intensity alone establishes provenance. Exact patches and values are in `box-control-measurements.json`.

Retain the E reading in KOMME and the literal O reading in KRAEFTIGON. No E/O downgrade is warranted by the wrong-filename concern. The control exercise also exposed approximate x-locators displaced in MAEUSCHEN and EINEN; ruler crops allowed those locators to be refined in the 90-position transcript without changing any shape token or letter. Original hashes and partial status are unchanged.
