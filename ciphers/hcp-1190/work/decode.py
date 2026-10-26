#!/usr/bin/env python3
"""Decode a manual Pigpen transcription. Does not perform OCR."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
for name, expected in json.loads((root/'work/source-sha256.json').read_text()).items():
    if hashlib.sha256((root/'source'/name).read_bytes()).hexdigest() != expected:
        raise SystemExit(f'Source hash mismatch: {name}')

# BR bottom/right; B bottom/left/right; BL bottom/left;
# R top/bottom/right; C all sides; L top/bottom/left;
# TR top/right; T top/left/right; TL top/left.
shapes = ['BR','B','BL','R','C','L','TR','T','TL']
key = {f'{shape}{dots}': chr(65+(dots-1)*9+i)
       for dots in range(1,4) for i,shape in enumerate(shapes)
       if (dots-1)*9+i < 26}
raw = [s.split() for s in (root/'work/transcription.txt').read_text().splitlines()
       if s.strip() and not s.startswith('#')]
letters = [t for row in raw for t in row if t not in ('-',',')]
for row in raw:
    print(''.join(key[t] if t in key else (' - ' if t == '-' else t) for t in row).strip())
plain = ''.join(key[t] for t in letters)
print(f'\n{len(letters)} glyphs decoded; {len(set(letters))} distinct glyphs.')
inverse = {v:k for k,v in key.items()}
assert [inverse[c] for c in plain] == letters
print('Symbol roundtrip exact. Manual transcription still requires independent review.')
