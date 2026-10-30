#!/usr/bin/env python3
"""hcp-1321: run from repo root: python3 -I ciphers/hcp-1321/work/decode.py"""
import hashlib, json, math, os, sys
D = 'ciphers/hcp-1321'
H = {'source/picture-large.jpg': '6c05c6798ed904a0e765c229dfd904c678c9b3f40ca717944397f1f11849ec62',
     'source/address-large.jpg': '448d6a7eb46427630099162d4de55094d6b33eaa332086479616e24cc52b92da',
     'work/hires/pc_hcp_2_pic.JPG': 'ba4f536d9175a2d3881c0304b279259cb1286d822ffc6dcfcf9be960b9644bca',
     'work/hires/pc_hcp_2_adr.JPG': 'ede1869719e3ebfac20b5c3482bf00f4527b60bebd794a9ae17fd59280bcf0f3'}
for p, h in H.items():
    got = hashlib.sha256(open(f'{D}/{p}', 'rb').read()).hexdigest()
    if got != h: sys.exit(f'HASH MISMATCH {p}')
print('source hashes OK')
key = json.load(open(f'{D}/work/key.json'))
out = []
for line in open(f'{D}/work/transcription.txt'):
    if line.startswith('#') or not line.strip(): continue
    w = ''
    for t in line.split():
        w += ' ' if t == '|' else '&' if t == '&' else key[t]
    out.append(w)
print('\n'.join(out))
txt = ''.join(out); n = sum(c.isalpha() for c in txt)
print(f'{n} signs, {len(key)} distinct; every sign keyed')
# structure check: shapes occupy unbroken alphabet blocks
order = sorted(key, key=lambda k: key[k])
blocks = [order[0][:2]]
for k in order[1:]:
    if k[:2] != blocks[-1]: blocks.append(k[:2])
print('shape sequence along the alphabet:', ' '.join(blocks), '(each shape once = unbroken blocks)')
sizes = {}
for k in key: sizes[k[:2]] = sizes.get(k[:2], 0) + 1
arr = math.factorial(len(key))
for v in sizes.values(): arr //= math.factorial(v)
print(f'chance of unbroken blocks for a random assignment: {math.factorial(len(sizes))}/{arr} = {math.factorial(len(sizes))/arr:.1e}')
