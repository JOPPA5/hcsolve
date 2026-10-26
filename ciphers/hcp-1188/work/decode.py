#!/usr/bin/env python3
"""Decode manual Pigpen tokens; source hash check is not OCR validation."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
for name, expected in json.loads((root/'work/source-sha256.json').read_text()).items():
    if hashlib.sha256((root/'source'/name).read_bytes()).hexdigest() != expected:
        raise SystemExit(f'Source hash mismatch: {name}')

# BR bottom/right; B bottom/left/right; BL bottom/left;
# R top/bottom/right; C four sides; L top/bottom/left;
# TR top/right; T top/left/right; TL top/left.
shapes = ['BR','B','BL','R','C','L','TR','T','TL','V','>','<','^']
key = {f'{shape}{dot}': chr(65+2*i+dot)
       for i,shape in enumerate(shapes) for dot in (0,1)}
tokens = []
for line in (root/'work/transcription.txt').read_text().splitlines():
    if not line or line.startswith('#'):
        continue
    row = line.split()
    tokens.extend(t for t in row if t != '|')
    print(''.join(' ' if t == '|' else key[t] for t in row))
print(f'\n{len(tokens)} glyphs; {len(set(tokens))} distinct.')
print('Source hashes verified; manual transcription independently checked in review 1.')
print('Literal WRITINH and DARROW retained; WRITING is an editorial correction.')
