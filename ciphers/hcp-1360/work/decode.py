#!/usr/bin/env python3
# Run from repo root: python3 -I ciphers/hcp-1360/work/decode.py
import hashlib, json, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for rel, want in json.load(open(os.path.join(D, 'work/source-sha256.json'))).items():
    got = hashlib.sha256(open(os.path.join(D, rel), 'rb').read()).hexdigest()
    if got != want:
        sys.exit('HASH MISMATCH ' + rel)
print('source hashes OK')
def shift(s, k):
    r = ''
    for c in s:
        if c.isalpha():
            b = 65 if c.isupper() else 97
            r += chr((ord(c) - b + k) % 26 + b)
        else:
            r += c
    return r
n = lit = 0
out = []
for line in json.load(open(os.path.join(D, 'work/transcription.json')))['lines']:
    c, p = [], []
    for t in line['tokens']:
        if isinstance(t, dict):
            c.append(t['literal']); p.append('[' + t['literal'] + ']')
            lit += sum(x.isalpha() for x in t['literal'])
        else:
            d = shift(t, -1)
            assert shift(d, 1) == t
            n += sum(x.isalpha() for x in t)
            c.append(t); p.append(d.upper())
    out.append(' '.join(p))
    print(' '.join(c).ljust(34), '|', ' '.join(p))
print('enciphered letters decoded:', n, '| abbreviation letters kept literal:', lit)
open(os.path.join(D, 'work/plaintext.txt'), 'w').write('\n'.join(out) + '\n')
