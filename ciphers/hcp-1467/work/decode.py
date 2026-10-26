#!/usr/bin/env python3
"""Decode manually transcribed Pigpen, preserving external punctuation cluster."""
from pathlib import Path
import hashlib, json
p = Path(__file__).resolve().parents[1]
for name, digest in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest() == digest
base = [('BR','AB'),('B','CD'),('BL','EF'),('R','GH'),('C','IJ'),
        ('L','KL'),('TR','MN'),('T','OP'),('TL','QR'),('V','ST'),
        ('>','UV'),('<','WX'),('^','YZ')]
key = {shape+str(dot):letter for shape,pair in base
       for dot,letter in enumerate(pair)}
inverse = {v:k for k,v in key.items()}
count = 0
for line in (p/'work/transcription.txt').read_text().splitlines():
    out = []
    for token in line.split():
        if token in key:
            value = key[token]
            assert inverse[value] == token
            count += 1
        elif token == '/':
            value = ' '
        elif token == 'DOT_CLUSTER':
            value = ' [EXTERNAL DOT CLUSTER] '
        elif token == '.':
            value = '.'
        else:
            raise ValueError(token)
        out.append(value)
    print(''.join(out))
print(f'{count} Pigpen letter positions; external dot cluster separately preserved.')
print('Source hashes and exact letter-key roundtrips passed; manual transcript, not OCR.')
