#!/usr/bin/env python3
"""Bounded alphabet tests, not a decipherment claim."""
from pathlib import Path
import hashlib, json
p = Path(__file__).resolve().parents[1]
for name, digest in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest() == digest
raw = list(map(int,(p/'work/provisional-numbers.txt').read_text().split()))
assert len(raw) == 14 and all(1 <= n <= 26 for n in raw)
for fifth in [13,12]:
    nums = raw[:]
    nums[4] = fifth
    print('Provisional numbers:', nums)
    for offset in range(26):
        out = ''.join(chr((n-1+offset)%26+65) for n in nums)
        print(f'Forward offset {offset}: {out}')
    print('Reverse alphabet:', ''.join(chr(91-n) for n in nums))
print('Hashes passed. No meaningful plaintext established by this bounded screen.')
