#!/usr/bin/env python3
"""Decode own manual scan transcript; hash checks are not OCR."""
from pathlib import Path
import hashlib, json, re
p = Path(__file__).resolve().parents[1]
for name, digest in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest() == digest
numeric = (p/'work/numbers.txt').read_text().splitlines()
greeting = []
count = 0
for line in numeric:
    nums = list(map(int, line.split()))
    assert all(1 <= n <= 26 for n in nums)
    word = ''.join(chr(64+n) for n in nums)
    assert [ord(c)-64 for c in word] == nums
    greeting.append(word)
    count += len(nums)
raw = (p/'work/transcription.txt').read_text()
def dec(m):
    w = m.group()
    return w[-1:] + w[:-1]
def enc(m):
    w = m.group()
    return w[1:] + w[:1]
body = re.sub(r'[A-Za-z]+', dec, raw)
assert re.sub(r'[A-Za-z]+', enc, body) == raw
print(' '.join(greeting))
print(body, end='')
print(f'Numeric positions: {count}; cursive letters: {len(re.findall(r"[A-Za-z]", raw))}')
print('All source hashes and exact inverse-key roundtrips passed.')
