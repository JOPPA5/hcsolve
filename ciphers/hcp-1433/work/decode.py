#!/usr/bin/env python3
"""Decode frozen manual Morse fragments only; not a full-image decipherment."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
codes='.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split()
key=dict(zip(codes,'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
for name,digest in json.loads((root/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((root/'source'/name).read_bytes()).hexdigest()==digest,name
count=0
for line in (root/'work/transcription.txt').read_text().splitlines():
    if not line or line.startswith('#'): continue
    tokens=[x.strip() for x in line.split('/')]
    print(''.join(key[x] for x in tokens)); count+=len(tokens)
assert count==34
print('34 frozen letters. Source hashes checked. PARTIAL: final main row unresolved.')
