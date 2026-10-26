#!/usr/bin/env python3
"""Caesar decoding of disclosed manual transcription, with source hashes."""
from pathlib import Path
import argparse,hashlib,json,re

root=Path(__file__).resolve().parents[1]
for name,digest in json.loads((root/'work/source-sha256.json').read_text()).items():
    if hashlib.sha256((root/'source'/name).read_bytes()).hexdigest()!=digest:
        raise SystemExit('Source hash mismatch: '+name)

def shift(text,n):
    out=[]
    for c in text:
        if 'a'<=c<='z':out.append(chr((ord(c)-97+n)%26+97))
        elif 'A'<=c<='Z':out.append(chr((ord(c)-65+n)%26+65))
        else:out.append(c)
    return ''.join(out)

p=argparse.ArgumentParser()
p.add_argument('--all-shifts',action='store_true')
args=p.parse_args()
cipher=(root/'work/ciphertext.txt').read_text()
if args.all_shifts:
    common=set('i the a to you of in and is was it how now if for am an'.split())
    rows=[]
    for n in range(26):
        plain=shift(cipher,n)
        score=sum(w in common for w in re.findall('[a-z]+',plain.lower()))
        rows.append({'shift':n,'common_word_hits':score,'text':plain})
    print(json.dumps(sorted(rows,key=lambda r:-r['common_word_hits']),indent=2))
else:
    plain=shift(cipher,13)
    assert shift(plain,13)==cipher
    print(plain,end='')
    print('Alphabetic positions:',sum(c.isascii() and c.isalpha() for c in cipher))
    print('ROT13 roundtrip exact; transcription is manual, not OCR.')
