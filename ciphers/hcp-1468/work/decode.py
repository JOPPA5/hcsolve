#!/usr/bin/env python3
"""Decode frozen manual Morse excerpts only, leaving remaining ink outside scope."""
from pathlib import Path
import hashlib, json
p = Path(__file__).resolve().parents[1]
for name, digest in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest() == digest
codes = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---',
         '-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-',
         '..-','...-','.--','-..-','-.--','--..']
key = {code:chr(65+i) for i,code in enumerate(codes)}
inverse = {v:k for k,v in key.items()}
count = 0
for name in ['address-excerpts.txt','picture-prefix.txt']:
    print(name)
    for line in (p/'work'/name).read_text().splitlines():
        out = []
        for token in line.split():
            if token == '/':
                out.append(' ')
            else:
                letter = key[token]
                assert inverse[letter] == token
                count += 1
                out.append(letter)
        print(''.join(out))
print(f'{count} excerpt letters. Remaining code has not been fully transcribed.')
print('Source hashes and excerpt roundtrips passed; not OCR/full-message proof.')
