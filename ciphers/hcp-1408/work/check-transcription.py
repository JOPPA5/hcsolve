#!/usr/bin/env python3
"""Audit the manual source transcription, without claiming decipherment."""
from pathlib import Path
from collections import Counter
import hashlib,json
root=Path(__file__).resolve().parents[1]
for name,digest in json.loads((root/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((root/'source'/name).read_bytes()).hexdigest()==digest,name
rows=[s for s in (root/'work/transcription.txt').read_text().splitlines() if s and not s.startswith('#')]
assert list(map(len,rows))==[5,8,11,9,11]
for i,row in enumerate(rows,1):
    print(f'{i}: {row} ({len(row)} signs; {row.count("O")} O-like)')
print('Frequency:',dict(sorted(Counter(''.join(rows)).items())))
# Treating O as an unconstrained erased letter would permit mutually different
# rebus expansions. These are counterexamples to uniqueness, not solutions.
for candidate in ['URAQTILU','URABTILU']:
    assert len(candidate)==len(rows[1])
    assert all(a=='O' or a==b for a,b in zip(rows[1],candidate))
print('44 observed signs. No key or plaintext established.')
print('An O-as-wildcard rule does not give a unique reading.')
