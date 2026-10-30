#!/usr/bin/env python3
"""HCP 1489: verify source hashes, extract the plaintext of the null cipher, and test it against chance."""
import hashlib, json, random
from pathlib import Path
root = Path(__file__).resolve().parents[1]
for name, digest in json.loads((root/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((root/'source'/name).read_bytes()).hexdigest() == digest, 'hash mismatch: ' + name
tr = json.loads((root/'work/transcription-v2.json').read_text())
key = json.loads((root/'work/key.json').read_text())
lines = tr['lines']; sig = key['signal_positions']
plain, nulls = '', ''
for n, line in enumerate(lines, 1):
    pos = set(sig[str(n)])
    assert all(0 <= p < len(line) for p in pos)
    shown = ''.join(c if i in pos else c.lower() for i, c in enumerate(line))
    print(f'{n}: {shown}')
    plain += ''.join(line[i] for i in sorted(pos))
    nulls += ''.join(c for i, c in enumerate(line) if i not in pos)
words = key['word_breaks']
assert ''.join(words) == plain, (plain, ''.join(words))
ct = ''.join(lines)
print('after signature:', tr['after_signature'], '| signature (cursive):', tr['signature_cursive'])
print(f'{len(ct)} signs on 7 lines; {len(plain)} plaintext letters, {len(nulls)} nulls (+ LET)')
print('PLAINTEXT:', ' '.join(words), '+ signature', tr['signature_cursive'])
# Chance test: how often does a random reordering of the same 144 signs contain each phrase
# as an ordered subsequence within a window no wider than on the card?
def window(s, p):
    best = None
    for st, c in enumerate(s):
        if c != p[0]: continue
        it, j, i = 0, 0, st
        while i < len(s) and j < len(p):
            if s[i] == p[j]: j += 1
            i += 1
        if j == len(p) and (best is None or i - st < best): best = i - st
    return best
rng = random.Random(1489)
for phrase in ('DEAR', 'WITHLOVEANDBESTWISHESFORYOURBIRTHDAY', 'FROMYOUR', 'NAN', 'DEAREST'):  # DEAREST: competing salutation (review 1)
    w = window(ct, phrase); hits = 0; N = 2000
    for _ in range(N):
        l = list(ct); rng.shuffle(l); r = window(''.join(l), phrase)
        hits += r is not None and r <= w
    print(f'  {phrase}: window {w} on card; random reorderings with window <= {w}: {hits}/{N}')
print('Source hashes OK.')
