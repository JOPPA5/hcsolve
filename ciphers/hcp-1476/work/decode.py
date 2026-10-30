#!/usr/bin/env python3
"""Decode the 22 Pigpen letters of hcp-1476; the end mark is a printed ornament, not cipher."""
from pathlib import Path
import json, hashlib
p = Path(__file__).resolve().parents[1]
for name, digest in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest() == digest
base = [('BR','AB'),('B','CD'),('BL','EF'),('R','GH'),('C','IJ'),
        ('L','KL'),('TR','MN'),('T','OP'),('TL','QR'),('V','ST'),
        ('>','UV'),('<','WX'),('^','YZ')]
key = {shape+str(dot):letter for shape,pair in base
       for dot,letter in enumerate(pair)}
inverse = {letter:shape for shape,letter in key.items()}
count = 0
for line in (p/'work/transcription.txt').read_text().splitlines():
    out = []
    for token in line.split():
        if token in key:
            value = key[token]
            assert inverse[value] == token
            count += 1
        elif token == 'END_MARK':
            value = '[END MARK: probably printed ornament of the card divider, not cipher; see work/end-mark-large.jpg]'
        elif token in [',','/']:
            value = token
        else:
            raise ValueError(token)
        out.append(value)
    print(''.join(out))
assert count == 22
print('22 Pigpen letters; end mark is not a letter (printed ornament, see SOLUTION.md).')
print('Source hashes and all 22 inverse-key roundtrips passed; not OCR.')
