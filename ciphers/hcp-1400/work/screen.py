#!/usr/bin/env python3
"""Bounded Caesar/Atbash screen on an UNVALIDATED manual Latin transcript."""
import json,hashlib,string
from pathlib import Path
r=Path(__file__).resolve().parents[1]
for name,h in json.loads((r/'work/source-sha256.json').read_text()).items():
 assert hashlib.sha256((r/'source'/name).read_bytes()).hexdigest()==h,name
lines=json.loads((r/'work/transcription.json').read_text())['provisional_screen_input']
s=' / '.join(lines).upper()
a=string.ascii_uppercase
def subst(t,k):return ''.join(k[a.index(c)] if c in a else c for c in t)
for n in range(26):
 print(f'Subtract {n:2d}: '+subst(s,a[-n:]+a[:-n] if n else a))
print('Atbash: '+subst(s,a[::-1]))
print('SOURCE HASHES PASS. Input remains provisional and is not a frozen image transcript.')
print('No key or plaintext selected. Failure of this literal screen cannot exclude Caesar with corrected readings.')
