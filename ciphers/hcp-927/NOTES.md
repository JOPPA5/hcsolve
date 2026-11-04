# Notes hcp-927

2026-11-03: captured by Claude Opus 5.5 (orchestrator).

## 2026-11-03 - Claude Opus 5.5 (solver) - result: PARTIAL, no marker

- Card: Soldatenkarte, Graudenz 19.6.10, to Gefr. Tamb. Pries(?), 4./IR 85, Rendsburg. There is no stamp,
  and the picture side has only the photo's own painted slogans.
- The left half of the address side holds Morse. Ink blob detection (work/blobs.py) and column grouping
  (work/cols2.py, with manual lines in strips3.py for the slanted left columns) were used. Every
  column was read by eye on rotated 2-3x strips (work/crops/L*, ML*, z_*).
- Main text: 19 vertical lines read top to bottom, taken right to left. It decodes completely:
  "Graudenz, den 19.6.10 Lieber Freund bedancke mich herzlich für deinen schönen Brief und den schönen
  Anschnauzer du hattest ja recht aber ich hab trotzdem ein par Tage gewartet mit der Antwort bis diese
  Karten fertig waren es grüszt Franz".
- Pitfalls: the auto grouping split one column (x 595/624) into two and merged others, so the left
  columns were redone with manual lines. A row-4 dot sits on top of column D's first dash (DIESE, not
  LIESE). FREUN+D: the D is squeezed beside the line foot. FRANZ: the Z is on a side line.
- Top 4 horizontal rows: L->R gives nonsense (G V V CH ...). They are written upside down. Reading
  rows 4,3,2,1 right to left with reversed element order gives "RESEREVE HAT NOCH 84 TAGE" (numerals in
  full 5-element form: ---.. = 8, ....- = 4). This matches the photo slogans "Reserve hat nur noch
  einige Wochen" and "die letzten 100".
- Dead end: the rest of row 1 after TAGE is [blot of 3 dots] ---- / -... -... / . --. I tried letters
  (S CH B B W/EM), other segmentations (NUS, DEBEM, TIE..), L->R, element reversal, full and cut
  numerals, and dot/dash swap. Nothing reads. This unread tail of several sign groups is why the
  card is partial under the batch rule (an unread clause anywhere on the card means partial).
- Address lines "Schwg(?)" and a struck-through word are unread (address, not message).
