#!/usr/bin/env python3
"""Decode a provisional manual glyph transcription; never infer missing glyphs."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
expected = json.loads((root / 'work/source-sha256.json').read_text())
for name, digest in expected.items():
    actual = hashlib.sha256((root / 'source' / name).read_bytes()).hexdigest()
    if actual != digest:
        raise SystemExit(f'Source hash mismatch: {name}')

# Outlines are named by their strokes: TL = top and left; T = top,
# left and right; TR = top and right; L = left, top and bottom;
# C = four sides; R = right, top and bottom; BL = bottom and left;
# B = bottom, left and right; BR = bottom and right.
# A–I occupy a reflected 3x3 grid; each additional numeral adds nine.
shapes = ['BR', 'B', 'BL', 'R', 'C', 'L', 'TR', 'T', 'TL']
key = {f'{s}{n}': chr(65 + (n - 1) * 9 + i)
       for n in range(1, 4) for i, s in enumerate(shapes)
       if (n - 1) * 9 + i < 26}
key.update({'?': '[?]', '|': ' ', '&': '&', ',': ',', '.': '.'})
count = unknown = 0
for line in (root / 'work/transcription.txt').read_text().splitlines():
    if not line or line.startswith('#'):
        continue
    tokens = line.split()
    count += sum(t in key and t[-1:] in '123' for t in tokens)
    unknown += tokens.count('?')
    print(''.join(key[t] for t in tokens))
print(f'\n{count} provisionally transcribed letter glyphs; {unknown} unresolved token(s).')
print('Closing lines remain untranscribed. This is not a full decipherment.')
