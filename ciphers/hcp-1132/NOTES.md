# Notes hcp-1132

2026-11-03: captured by Claude Opus 5.5 (orchestrator).

## 2026-11-03 - Claude Opus 5.5 (solver, round 1)

- Address side, left half: 21 vertical columns of pen dots/dashes = Morse. Reading orientation: card turned 90 deg
  anticlockwise; right-most column first, top to bottom; last words continue along the bottom edge (left to right).
- First automatic attempt (work/columns.py, fixed column centres) failed on the left half: columns there lean by up
  to 100 px and a 21st column was missed. work/track.py / track2.py (linking) were also unreliable; the final
  transcription was made by eye from zoom crops (work/zoom2.py, work/pair.py), with work/comps.json coordinates
  (work/components.py, threshold gray<172 and B-R<0 so that the pale brown dashes are kept and blue print dropped).
- Decoded with international Morse + É ..-.., Á .--.-, Ö ---.: "Édes jó kis uram! Kedves soraid megkaptam! Bocsás
  meg édesem hogy én nem válaszoltam soraidra de sok sok minden, [struck] ért mostanába, majd rövidesen elmondom,
  sokat, gondolva rád, számtalanszor csókol kis feleséged Anya. Este várlak!! Táncolunk."
- Dead ends: reading columns left-to-right gave nonsense; the three "?" squiggles at the bottom centre (x 990-1150,
  y 2040-2105) are plain question marks written upright, not Morse (not part of any column).
- Bottom line checked mark by mark: none of its marks can belong to the column above it (each would spoil a word).
- Residual points: segmentation by word sense in a few letters (ANYA, É in C1, Y in HOGY); C13's N is one heavy
  merged stroke; the final K shares the L-shaped stroke with C11's Á; C10 struck section unread (writer's deletion).
- Picture side: no writing. Plain notes: "Vigyázz a kis libákra !!!" (upside down), address Sődy Sándor, Csapó u. 97, Debrecen.
- Web search for a published solution: none found.

## 2026-11-03 - Claude Opus 5.5 (solver, after review 1: ACCEPT)

- Note corrected to three "!" (work/crops/note_upright.png). Orientation wording fixed: in the reading orientation the
  Copyright line is upside down (work/crops/morse_reading.png). Decode output unchanged. Stamp: no visible ink at its
  edges; nothing under it can be checked. Report, register entry and FINAL follow.
