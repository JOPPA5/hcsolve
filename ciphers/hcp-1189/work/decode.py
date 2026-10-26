#!/usr/bin/env python3
"""Mechanical decoding of disclosed manual glyph transcription; no OCR."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
for name, expected in json.loads((root/'work/source-sha256.json').read_text()).items():
    if hashlib.sha256((root/'source'/name).read_bytes()).hexdigest() != expected:
        raise SystemExit(f'Source hash mismatch: {name}')

# Named by visible strokes: BR bottom/right; B bottom/left/right;
# BL bottom/left; R top/bottom/right; C four sides; L top/bottom/left;
# TR top/right; T top/left/right; TL top/left.
shapes = ['BR','B','BL','R','C','L','TR','T','TL']
key = {f'{shape}{dots}': chr(65+(dots-1)*9+i)
       for dots in range(1,4) for i,shape in enumerate(shapes)
       if (dots-1)*9+i < 26}
tokens = []
for line in (root/'work/transcription.txt').read_text().splitlines():
    if not line or line.startswith('#'):
        continue
    row = line.split()
    tokens.extend(t for t in row if t in key)
    print(''.join(key[t] if t in key else (' ' if t == '|' else t) for t in row))
inverse = {v:k for k,v in key.items()}
assert [inverse[key[t]] for t in tokens] == tokens
print(f'\n{len(tokens)} glyphs, {len(set(tokens))} distinct; exact token roundtrip.')
print('Independent visual review is still pending.')
