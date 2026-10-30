#!/usr/bin/env python3
"""hcp-1826: decode the transcription; run from the repo root. Verifies source hashes."""
import hashlib, os, collections
D = 'ciphers/hcp-1826/'
H = {'source/picture-large.jpg':'f2c9a9cddda730519865692517da4dbef33987aa0229dc0e96db0b6e5ee2ce67',
     'source/address-large.jpg':'540e53655416a385a366d759f90d2dc4b1f077d1c00c266bf2d23da286ab01a6',
     'work/hires/pc_hcp_507_pic.JPG':'49c87bb4e15d7a9843128f464a2aa10db752d7c0896fdc5ab6e247240e6ecf92',
     'work/hires/pc_hcp_507_adr.JPG':'5a4632768689c99808b61825abfb94636fa7e06cb814f99d4a185665265bfb94'}
for f, h in H.items():
    got = hashlib.sha256(open(D + f, 'rb').read()).hexdigest()
    assert got == h, f
print('source hashes OK')
KEY = {"X":"a","2'":"e","1'":"i","[0":"o","0]":"u","0'":"w","0":"y",
       "19":"b","18":"c","17":"d","16":"f","15":"g","14":"h","13":"j","12":"k","11":"l",
       "10":"m","9":"n","8":"p","6":"r","5":"s","4":"t","3":"v"}
out, used = [], collections.Counter()
for line in open(D + 'work/transcription.txt'):
    if line.startswith('#') or not line.strip():
        continue
    label, *toks = line.split()
    words, w = [], ''
    for t in toks:
        if t == '|':
            words.append(w); w = ''
        elif t == '.':
            w += '.'
        elif t.startswith('{'):
            w += t[1:-1]
        elif t.startswith('('):
            used[t] += 1
            n = t[1:-1]; w += KEY.get(n, KEY.get(n + "'")).upper()
        else:
            used[t] += 1
            w += KEY[t]          # KeyError = a token not covered by the key
    words.append(w)
    out.append(' '.join(words))
    print(f'{label:4}', out[-1])
print('\nTokens decoded:', sum(used.values()), '| distinct:', len(used), '| unkeyed: 0')
print('Literal plaintext:\n' + ' '.join(out))
