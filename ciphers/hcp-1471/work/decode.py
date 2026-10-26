#!/usr/bin/env python3
"""Decode own manual transcript with the two marked-A exceptions explicit."""
from pathlib import Path
import hashlib, json
p = Path(__file__).resolve().parents[1]
for name, digest in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest() == digest
tokens = (p/'work/transcription.txt').read_text().split()
observed = set(tokens)-{'/','?'}
key = {}
for t in observed:
    if t == 'A^':
        key[t] = 'A'
    else:
        assert len(t) == 1 and 'a' <= t <= 'z'
        key[t] = chr((ord(t)-97+1)%26+65)
assert len(set(key.values())) == len(key)
inverse = {v:k for k,v in key.items()}
out = []
for t in tokens:
    if t == '/':
        out.append(' ')
    elif t == '?':
        out.append('?')
    else:
        letter = key[t]
        assert inverse[letter] == t
        out.append(letter)
text = ''.join(out)
print(text)
assert sum(t not in ['/','?'] for t in tokens) == 16
assert tokens.count('A^') == 2
print('16 letters, including 2 marked-A exceptions. Source hashes and roundtrips passed.')
print('Manual scan alternatives: v→w in last word gives DOXNHEARTED; final c→e gives DOWNHEARTEF.')
print('These checks are not OCR or independent scan validation.')
