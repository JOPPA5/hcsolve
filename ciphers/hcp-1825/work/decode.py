#!/usr/bin/env python3
"""Decode a disclosed manual transcript; do not silently repair anomalies."""
from pathlib import Path
import hashlib,json
r=Path(__file__).resolve().parents[1]
for name,digest in json.loads((r/'work/source-sha256.json').read_text()).items():
    if hashlib.sha256((r/'source'/name).read_bytes()).hexdigest()!=digest:
        raise SystemExit('Source hash mismatch: '+name)
# BR bottom/right; B bottom/left/right; BL bottom/left; R top/bottom/right;
# C four sides; L top/bottom/left; TR top/right; T top/left/right;
# TL top/left. Wedges named by pointing direction.
shapes=['BR','B','BL','R','C','L','TR','T','TL','V','>','<','^']
key={f'{s}{d}':chr(65+2*i+d) for i,s in enumerate(shapes) for d in (0,1)}
known=[]
for line in (r/'work/transcription.txt').read_text().splitlines():
    if not line or line.startswith('#'):continue
    row=line.split();known.extend(t for t in row if t in key)
    extra={'|':' ','?':'?','.':'.'}
    print(''.join(key[t] if t in key else extra[t] for t in row))
inverse={v:k for k,v in key.items()}
assert [inverse[key[t]] for t in known]==known
print(f'\n{len(known)} letter glyphs; exact token roundtrip.')
assert len(known)==95
print('YOW and LIVE preserved literally; intended YOU and LOVE are interpretations.')
print('Manual transcript revised against independent review 1; source comma separators rendered as spaces.')
