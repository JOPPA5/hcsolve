#!/usr/bin/env python3
"""hcp-1408: verify source hashes, check the rebus segmentation against the
transcription sign by sign, and print the plaintext. Run from repo root:
  python3 -I ciphers/hcp-1408/work/decode.py"""
from pathlib import Path
import hashlib, json
root = Path(__file__).resolve().parents[1]
for name, digest in json.loads((root/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((root/'source'/name).read_bytes()).hexdigest() == digest, 'hash mismatch: '+name
print('source hashes OK')
rows = [s for s in (root/'work/transcription.txt').read_text().splitlines() if s and not s.startswith('#')]
assert list(map(len, rows)) == [5, 8, 11, 9, 11] and sum(map(len, rows)) == 44
key = json.loads((root/'work/rebus-key.json').read_text())
punct = [', ', '; ', '; ', '; ', '.']
out = []
for row, toks in zip(rows, key['lines']):
    assert ''.join(t[1] for t in toks) == row, (row, toks)   # every sign consumed exactly once
    words = [key['values'][t[0]] for t in toks]
    out.append((row, toks, words))
print('all 44 signs covered by the segmentation\n')
for row, toks, words in out:
    print(f"{row:12s} -> {' | '.join(t[1] for t in toks)}")
print()
title, *verse = [' '.join(w) for _, _, w in out]
def cap(s): return s[0].upper()+s[1:]
print('Heading: ' + cap(title).replace('O sigh', 'O, sigh') + '!')
fix = [lambda s: s.replace('cipher O', 'cipher, O'), lambda s: s.replace('cipher O', 'cipher, O'),
       lambda s: s.replace('cipher I', 'cipher, I'), lambda s: s.replace('cipher I', 'cipher, I')]
ends = [';', ';', ';', '.']
for f, s, e in zip(fix, verse, ends):
    print(cap(f(s)) + e)
