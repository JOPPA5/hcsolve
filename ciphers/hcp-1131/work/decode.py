#!/usr/bin/env python3
"""Decode the manual Pigpen transcription of HCP1131 with the dot-count key."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
for name,digest in json.loads((root/'work/source-sha256.json').read_text()).items():
    if hashlib.sha256((root/'source'/name).read_bytes()).hexdigest()!=digest:
        raise SystemExit('Source hash mismatch: '+name)
# Outlines by strokes: BR bottom/right; B bottom/left/right;
# BL bottom/left; R top/bottom/right; C four sides; L top/bottom/left;
# TR top/right; T top/left/right; TL top/left.
shapes=['BR','B','BL','R','C','L','TR','T','TL']
key={f'{s}{n}':chr(65+9*(n-1)+i) for n in (1,2,3)
     for i,s in enumerate(shapes) if 9*(n-1)+i<26}
extra={'-':' ','|':' ','{ish}':'ish'}
tokens=[];lines=[]
for line in (root/'work/transcription.txt').read_text().splitlines():
    if not line or line.startswith('#'):continue
    row=line.split();out=''
    for t in row:
        if t.lstrip('^') in key:
            tokens.append(t.lstrip('^'));out+=key[t.lstrip('^')]
        else:
            out+=extra[t]
    lines.append(out.strip())
inverse={v:k for k,v in key.items()}
assert [inverse[key[t]] for t in tokens]==tokens
print('\n'.join(lines))
print('\nRunning text:',' '.join(' '.join(lines).split()))
print(f'\n{len(tokens)} cipher glyphs decoded; exact token roundtrip.')
