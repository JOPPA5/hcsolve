# Solver notes —2026-10-26
Faint Pigpen-like grid letters on message and address, cat picture no observed
cipher. CPU contrast stretch and enlarged message crop generated; substantially
better visible line outlines, but many internal marks still ambiguous.
Initial common interleaved and sequential-grid associations did not expose a
coherent reading; no complete transcript or key yet. HOW DO YOU / LIKE THIS
CARD is a tempting phrase pattern, not a reliable reading and not claimed.
Need glyph inventory and dot/mark distinctions before further cryptanalysis.
No marker/register entry. Proceed1478 to search easier standard example.

# 2026-10-30 — Claude Opus 5.5 (solver): key found, message read, address incomplete

Earlier entry (2026-10-26) is GPT work; its "HOW DO YOU / LIKE THIS CARD" guess
turns out correct, but was not a reading. Everything below was read afresh from
enlarged crops of source/address-large.jpg (work/crops/*.png, 5-12x, PIL autocontrast).

## Cipher
Not standard Pigpen. Every glyph is a 3x3-grid cell outline with exactly ONE dot,
and the dot's horizontal position (left/centre/right) selects one of three letters
in that cell (Rosicrucian-style 3-letters-per-cell Pigpen):
  ABC|DEF|GHI / JKL|MNO|PQR / STU|VWX|YZ  (cell shape as in ordinary Pigpen:
  A-C = bottom+right, D-F = bottom+left+right, ..., Y-Z = top+left).
No sister card in the repo uses this variant (hcp-899 is a stroke-count variant).
The key is confirmed by coherent English and by place names read before guessing:
BOURNEMOUTH (11 glyphs) and ENGLAND (7) in the address.

## Reading (work/transcription.txt, `python3 -I ciphers/hcp-1479/work/decode.py`)
Message (left): HOW. DO. YOU. LIKE, THIS: CARD..? / BEST. WISHES.. / FROM /
DOREEN.. / XMAS  (+ a separate plain cursive "St." below, not cipher; meaning
not established).
Address: MISS. [surname ~5 glyphs, unread] / [street, unread] RD. /
BOURNEMOUTH / ENGLAND.

Weak points in the read part: WISHES — W-cell looks closer to a box with a
left-centre dot than to an open-bottom cell, and the I is mostly hidden under the
watermark (only its dot and part of the vertical visible); DOREEN — dot positions
of O, R, 2nd E are only marginally distinguishable (O ~0.55, R ~0.6, E ~0.6 of cell
width) and R's right side is hidden; FROM — O dot at ~0.6. This writer's "right"
dots sit only slightly right of centre (cf. O in HOW = 0.65), so centre/right is
the hard distinction throughout.

## Why it stops (no marker)
The scan is only 1024 px wide and the HC Portal watermark (cipher disc + building
logo) lies directly on the address. R1 surname (after MISS) runs through the logo
dome/keyhole circle and a watermark band: shapes and dot positions of ~5 glyphs
cannot be fixed. R2 (street) starts in a cluster of grey symbols ("Fe#B9 Omega pi")
that cannot be separated from the watermark's ring symbols at this resolution;
only the final ". RD." (L.R B.L) is clear, preceded by something like "...ONE".
Guessing a surname/street would be forcing words onto noise. A higher-resolution
or unwatermarked scan would very likely finish it. Status: PARTIAL.
