#!/usr/bin/env python3
"""hcp-1470: decode the numeric line with A1Z26 (1=A ... 26=Z).
Checks source hashes, reads work/transcription.txt, prints the plaintext."""
from pathlib import Path
import hashlib, json
d = Path(__file__).resolve().parents[1]
for name, digest in json.loads((d/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((d/'source'/name).read_bytes()).hexdigest() == digest, name
print('source hashes OK')
lines = [l for l in (d/'work/transcription.txt').read_text().splitlines()
         if l.strip() and not l.startswith('#')]
for line in lines:
    nums = [int(x) for x in line.split('-')]
    assert all(1 <= n <= 26 for n in nums)
    print('cipher :', line, f'({len(nums)} numbers)')
    out = ''.join(chr(64 + n) for n in nums)
    print('literal:', out)
    print('segmented (editorial):', out[:4], out[4:])
